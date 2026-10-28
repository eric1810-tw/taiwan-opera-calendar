#!/usr/bin/env node
// 新社群讀取器：首屏先存證、每次捲動後累積、以貼文 ID 去重、記錄停止原因。
// 啟動方式與 scripts/social_reader.mjs 相同：child_process.spawn 原生 Edge＋~/.patrol-edge，
// 不用 puppeteer／playwright，不加 mock keychain 等參數，不讀設定檔內任何資料檔。
// 每個來源完成（含每次重試）就在 stdout 輸出一行 JSON，交給 Python 立即 record。
import { execFileSync, spawn } from 'node:child_process';
import { createHash } from 'node:crypto';
import { existsSync, lstatSync, mkdirSync, readFileSync, readlinkSync, writeFileSync } from 'node:fs';
import { createServer } from 'node:net';
import os from 'node:os';
import path from 'node:path';
import { fileURLToPath } from 'node:url';
import {
  checkEdgeLock,
  generateFacebookPostKey,
  isAuthorPost,
  isFacebookLoginWall,
  normalizeFacebookPostUrl,
  normalizePostUrl,
  parseFacebookTime,
  utcToTaipeiIso,
  calculateMinMaxTimes,
} from '../social_reader.mjs';

export const PATROL_PROFILE = path.join(os.homedir(), '.patrol-edge');
const EDGE_BIN = '/Applications/Microsoft Edge.app/Contents/MacOS/Microsoft Edge';
const sleep = ms => new Promise(r => setTimeout(r, ms));

// --- 純函式（tests/test_social_capture.mjs） ---

export function threadsPostCode(url) {
  const m = String(url || '').match(/\/post\/([A-Za-z0-9_-]+)/);
  return m ? m[1] : '';
}

export function facebookPostId(url) {
  const s = String(url || '');
  let m = s.match(/[?&](?:story_fbid|fbid)=([A-Za-z0-9]+)/);
  if (m) return m[1];
  m = s.match(/\/(?:posts|videos|reel)\/([A-Za-z0-9]+)/);
  if (m) return m[1];
  return '';
}

export function facebookKey(handle, url, text) {
  const id = facebookPostId(url);
  return id ? `facebook:${handle}:${id}` : generateFacebookPostKey(handle, text);
}

// 累積器：同一 key 保留較長正文、合併圖片；記錄第一次出現的捲動輪次
export function createAccumulator() {
  const map = new Map();
  return {
    add(posts, round) {
      let added = 0;
      for (const p of posts) {
        const prev = map.get(p.postKey);
        if (!prev) {
          map.set(p.postKey, { ...p, firstSeenRound: round });
          added++;
        } else {
          if ((p.text || '').length > (prev.text || '').length) prev.text = p.text;
          prev.images = Array.from(new Set([...(prev.images || []), ...(p.images || [])]));
          if (!prev.datetime && p.datetime) prev.datetime = p.datetime;
          if (!prev.url && p.url) prev.url = p.url;
        }
      }
      return added;
    },
    keys() { return Array.from(map.keys()); },
    values() { return Array.from(map.values()); },
    has(k) { return map.has(k); },
  };
}

// 停止條件：到 7 天窗口、連續 N 輪沒有新貼文、捲動上限
export function decideStop({ round, maxScrolls, noNewRounds, lowestVisibleAt, windowStartMs, noNewLimit = 3 }) {
  if (lowestVisibleAt) {
    const t = new Date(lowestVisibleAt).getTime();
    if (!isNaN(t) && t < windowStartMs) return 'reached-window';
  }
  if (noNewRounds >= noNewLimit) return `no-new-after-${noNewLimit}`;
  if (round >= maxScrolls) return 'max-scrolls';
  return null;
}

// 不變式：首屏與回頂部再讀到的貼文都必須在輸出內；守門帳號的已知貼文在窗口內必須出現
export function checkInvariants({ finalKeys, firstScreenKeys, headRecheckKeys = [], knownPosts = [], windowStartMs, loginWall, nowMs = Date.now() }) {
  const final = new Set(finalKeys);
  const problems = [];
  if (!loginWall && firstScreenKeys.length === 0) problems.push('first-screen-empty');
  const lost = firstScreenKeys.filter(k => !final.has(k));
  if (lost.length) problems.push('first-screen-lost');
  const headLost = headRecheckKeys.filter(k => !final.has(k));
  if (headLost.length) problems.push('head-recheck-missing');
  const missingKnown = knownPosts
    // 只要求「讀取當下已經發布、且在窗口內」的已知貼文；讀取後才發的不算漏讀
    // 已確認被作者刪除的（deletedConfirmedAt）不再要求
    .filter(kp => !kp.deletedConfirmedAt)
    .filter(kp => !kp.postedAt || (new Date(kp.postedAt).getTime() >= windowStartMs && new Date(kp.postedAt).getTime() <= nowMs))
    .map(kp => kp.postKey)
    .filter(k => !final.has(k));
  if (missingKnown.length) problems.push('known-post-missing');
  return { ok: problems.length === 0, problems, lost, headLost, missingKnown };
}

// --- CDP ---

function getFreePort() {
  return new Promise((resolve, reject) => {
    const srv = createServer();
    srv.listen(0, '127.0.0.1', () => {
      const port = srv.address().port;
      srv.close(() => resolve(port));
    });
    srv.on('error', reject);
  });
}

export function resolveProfile(testProfile) {
  if (!testProfile) return PATROL_PROFILE;
  const resolved = path.resolve(testProfile);
  const tmpRoots = [os.tmpdir(), '/tmp', '/private/tmp', '/private/var/folders', '/var/folders'].map(p => path.resolve(p));
  if (resolved === PATROL_PROFILE || !tmpRoots.some(r => resolved.startsWith(r + path.sep))) {
    throw new Error('測試設定檔必須是暫存目錄，且不得是 ~/.patrol-edge');
  }
  return resolved;
}

// 上一輪被中斷時留下的 Edge：父程序已結束（ppid 1）、參數是本程式的 headless 組合、指向同一設定檔
export function isOrphanPatrolEdge({ ppid, command }, profileDir) {
  return ppid === 1 && command.includes('/MacOS/Microsoft Edge ') && command.includes('--headless=new')
    && command.includes(`--user-data-dir=${profileDir} `);
}

function lockOwnerPid(profileDir) {
  try {
    const lockPath = path.join(profileDir, 'SingletonLock');
    if (!lstatSync(lockPath).isSymbolicLink()) return null;
    const pid = parseInt(readlinkSync(lockPath).split('-').pop(), 10);
    return Number.isNaN(pid) ? null : pid;
  } catch {
    return null;
  }
}

async function releaseOrphanEdge(profileDir) {
  const pid = lockOwnerPid(profileDir);
  if (!pid) return null;
  let info;
  try {
    const out = execFileSync('ps', ['-ww', '-o', 'ppid=,command=', '-p', String(pid)], { encoding: 'utf-8' }).trim();
    const m = out.match(/^(\d+)\s+(.*)$/s);
    if (!m) return null;
    info = { ppid: parseInt(m[1], 10), command: m[2] + ' ' };
  } catch {
    return null;  // 程序已不在：舊鎖，checkEdgeLock 會略過
  }
  if (!isOrphanPatrolEdge(info, profileDir)) return null;
  const alive = () => { try { process.kill(pid, 0); return true; } catch { return false; } };
  try { process.kill(pid, 'SIGTERM'); } catch {}
  for (let i = 0; i < 50 && alive(); i++) await sleep(100);
  if (alive()) { try { process.kill(pid, 'SIGKILL'); } catch {} }
  for (let i = 0; i < 30 && alive(); i++) await sleep(100);
  process.stderr.write(`已結束上一輪留下的 Edge（PID ${pid}）\n`);
  return pid;
}

async function launchEdge(profileDir) {
  await releaseOrphanEdge(profileDir);
  checkEdgeLock(profileDir);
  const port = await getFreePort();
  const args = [
    '--headless=new',
    `--remote-debugging-port=${port}`,
    `--user-data-dir=${profileDir}`,
    '--lang=zh-TW',
    '--no-first-run',
    '--no-default-browser-check',
    '--window-size=1280,2000',
    'about:blank',
  ];
  const proc = spawn(EDGE_BIN, args, { stdio: 'ignore' });
  // 本程式被結束（SIGTERM／SIGINT／SIGHUP）時先關 Edge，不留下佔住設定檔的程序
  const onSignal = sig => {
    try { proc.kill('SIGKILL'); } catch {}
    process.exit(sig === 'SIGINT' ? 130 : 143);
  };
  const signals = ['SIGTERM', 'SIGINT', 'SIGHUP'];
  for (const sig of signals) process.on(sig, onSignal);
  const onExit = () => { try { proc.kill('SIGKILL'); } catch {} };
  process.on('exit', onExit);
  let tabs = null;
  for (let i = 0; i < 40; i++) {
    try {
      const res = await fetch(`http://127.0.0.1:${port}/json`);
      tabs = await res.json();
      if (tabs && tabs.length) break;
    } catch {
      await sleep(300);
    }
  }
  if (!tabs) {
    const exited = proc.exitCode !== null;
    proc.kill();
    throw new Error(exited ? 'Edge 啟動後立即結束（設定檔可能被其他程序佔用）' : '無法連線到 Edge DevTools');
  }
  const pageTab = tabs.find(t => t.type === 'page') || tabs[0];
  const ws = new WebSocket(pageTab.webSocketDebuggerUrl);
  await new Promise((resolve, reject) => { ws.onopen = resolve; ws.onerror = reject; });
  let id = 0;
  const pend = new Map();
  ws.onmessage = e => {
    try {
      const m = JSON.parse(e.data);
      if (pend.has(m.id)) { pend.get(m.id)(m); pend.delete(m.id); }
    } catch {}
  };
  const send = (method, params = {}) => new Promise((resolve, reject) => {
    const i = ++id;
    const timer = setTimeout(() => { pend.delete(i); reject(new Error(`CDP 逾時：${method}`)); }, 45000);
    pend.set(i, m => { clearTimeout(timer); resolve(m); });
    try { ws.send(JSON.stringify({ id: i, method, params })); } catch (err) { clearTimeout(timer); reject(err); }
  });
  const evaluate = async expr => {
    const res = await send('Runtime.evaluate', { expression: expr, returnByValue: true, awaitPromise: true });
    return res.result?.result?.value;
  };
  const escape = async () => {
    try {
      await send('Input.dispatchKeyEvent', { type: 'rawKeyDown', key: 'Escape', code: 'Escape', windowsVirtualKeyCode: 27 });
      await send('Input.dispatchKeyEvent', { type: 'keyUp', key: 'Escape', code: 'Escape', windowsVirtualKeyCode: 27 });
    } catch {}
  };
  const screenshot = async () => {
    const shot = await send('Page.captureScreenshot', { format: 'png', captureBeyondViewport: false });
    return shot.result?.data ? Buffer.from(shot.result.data, 'base64') : null;
  };
  const close = async () => {
    try { ws.close(); } catch {}
    try { proc.kill(); } catch {}
    await new Promise(r => { if (proc.exitCode !== null) r(); else { proc.once('exit', r); setTimeout(r, 5000); } });
    if (proc.exitCode === null) { try { proc.kill('SIGKILL'); } catch {} }
    for (const sig of signals) process.off(sig, onSignal);
    process.off('exit', onExit);
  };
  await send('Page.enable');
  await send('Runtime.enable');
  return { send, evaluate, escape, screenshot, close };
}

// --- 頁面擷取程式（在頁面內執行） ---

const THREADS_EXTRACT = `
(() => {
  const res = [];
  for (const t of document.querySelectorAll('time[datetime]')) {
    const a = t.closest('a[href*="/post/"]') || (t.parentElement && t.parentElement.querySelector('a[href*="/post/"]'));
    if (!a) continue;
    let container = t;
    let cur = t.parentElement;
    while (cur && cur !== document.body) {
      if (cur.querySelectorAll('time[datetime]').length === 1) { container = cur; cur = cur.parentElement; } else break;
    }
    if (container === t && t.parentElement) container = t.parentElement;
    const rect = container.getBoundingClientRect();
    res.push({
      rawDatetime: t.getAttribute('datetime'),
      rawUrl: a.href,
      text: (container.innerText || '').replace(/\\s+/g, ' ').trim().slice(0, 4000),
      images: Array.from(container.querySelectorAll('img')).filter(i => (i.naturalWidth || i.width || 0) > 150).map(i => i.src),
      top: rect.top + window.scrollY,
    });
  }
  return res;
})()`;

const FB_EXPAND = `
(() => {
  for (const msg of document.querySelectorAll('[data-ad-rendering-role="story_message"]')) {
    for (const b of msg.querySelectorAll('[role="button"], span, div')) {
      const txt = (b.innerText || '').replace(/\\s+/g, '');
      if (txt === '查看更多' || txt === '顯示更多' || txt === 'Seemore') { try { b.click(); } catch {} }
    }
  }
})()`;

const FB_EXTRACT = `
(() => {
  const res = [];
  for (const m of document.querySelectorAll('[data-ad-rendering-role="story_message"]')) {
    let container = m;
    for (let k = 0; k < 25 && container.parentElement; k++) {
      const p = container.parentElement;
      if (p.querySelectorAll('[data-ad-rendering-role="story_message"]').length > 1) break;
      container = p;
    }
    let href = null, timeText = null;
    const links = Array.from(container.querySelectorAll('a[href]'));
    for (const pass of [/posts|story_fbid|permalink|videos|reel/, /photo/]) {
      for (const a of links) {
        const h = a.getAttribute('href') || a.href || '';
        if (h.includes('comment_id=')) continue;
        if (pass.test(h)) { href = h; timeText = (a.getAttribute('aria-label') || '').trim() || null; break; }
      }
      if (href) break;
    }
    const rect = container.getBoundingClientRect();
    res.push({
      rawHref: href,
      timeText,
      text: (m.innerText || '').slice(0, 4000),
      images: Array.from(container.querySelectorAll('img')).filter(i => (i.naturalWidth || i.width || 0) > 150).map(i => i.src),
      top: rect.top + window.scrollY,
    });
  }
  return res;
})()`;

function normalizeThreads(raw, handle) {
  const out = [];
  for (const p of raw || []) {
    const url = normalizePostUrl(p.rawUrl);
    if (!url) continue;
    if (handle && !isAuthorPost(url, handle)) continue;
    const code = threadsPostCode(url);
    if (!code) continue;
    out.push({
      postKey: `threads:${handle}:${code}`,
      url,
      datetime: utcToTaipeiIso(p.rawDatetime) || p.rawDatetime,
      text: p.text,
      images: p.images || [],
      top: p.top,
    });
  }
  return out;
}

function normalizeFacebook(raw, handle, fetchedAt) {
  const out = [];
  for (const p of raw || []) {
    if (!(p.text || '').trim()) continue;
    let url = '';
    if (p.rawHref) url = normalizeFacebookPostUrl(p.rawHref.startsWith('/') ? `https://www.facebook.com${p.rawHref}` : p.rawHref);
    out.push({
      postKey: facebookKey(handle, url, p.text),
      url,
      timeText: p.timeText || null,
      datetime: p.timeText ? parseFacebookTime(p.timeText, fetchedAt) : null,
      text: p.text,
      images: p.images || [],
      top: p.top,
    });
  }
  return out;
}

async function waitFor(cdp, expr, seconds) {
  for (let i = 0; i < seconds; i++) {
    await sleep(1000);
    if (await cdp.evaluate(expr)) return true;
  }
  return false;
}

async function capture(cdp, source, opts) {
  const { kind, handle, url } = source;
  const fetchedAt = new Date().toISOString();
  const windowStartMs = opts.nowMs - opts.windowDays * 86400000;
  await cdp.send('Page.navigate', { url });
  const readyExpr = kind === 'threads'
    ? `Array.from(document.querySelectorAll('time[datetime]')).some(t => t.closest('a[href*="/post/"]'))`
    : `document.querySelectorAll('[data-ad-rendering-role="story_message"]').length > 0`;
  if (kind === 'facebook') { await sleep(3000); await cdp.escape(); }
  const ready = await waitFor(cdp, readyExpr, opts.readySeconds);

  const pageInfo = await cdp.evaluate(`(() => ({
    href: location.href,
    text: (document.body ? document.body.innerText : '').slice(0, 3000),
    dialog: Boolean(document.querySelector('div[role="dialog"]')),
    email: Boolean(document.querySelector('input[name="email"]')),
    loginForm: Boolean(document.querySelector('form[action*="login"]')),
    story: document.querySelectorAll('[data-ad-rendering-role="story_message"]').length,
  }))()`) || {};
  const loginWall = kind === 'threads'
    ? Boolean((pageInfo.href || '').includes('/login') || (!ready && /登入|Log in|建立新帳號/.test(pageInfo.text || '')))
    : isFacebookLoginWall({ storyMessageCount: pageInfo.story || 0, hasEmailInput: pageInfo.email, hasLoginForm: pageInfo.loginForm, isLoginUrl: (pageInfo.href || '').includes('/login') });

  const extract = async () => {
    if (kind === 'facebook') { await cdp.evaluate(FB_EXPAND); await sleep(300); }
    const raw = await cdp.evaluate(kind === 'threads' ? THREADS_EXTRACT : FB_EXTRACT);
    return kind === 'threads' ? normalizeThreads(raw, handle) : normalizeFacebook(raw, handle, fetchedAt);
  };

  const acc = createAccumulator();
  // 1. 首屏：捲動前先存證
  const first = await extract();
  acc.add(first, 0);
  const firstScreenKeys = first.map(p => p.postKey);
  const firstShot = await cdp.screenshot().catch(() => null);

  // 2. 逐段捲動、每次累積
  let round = 0;
  let noNewRounds = 0;
  let stopReason = null;
  while (!stopReason) {
    round++;
    if (kind === 'facebook') await cdp.escape();
    await cdp.evaluate(`window.scrollBy(0, ${opts.scrollStep})`);
    await sleep(kind === 'threads' ? opts.threadsWaitMs : opts.facebookWaitMs);
    const posts = await extract();
    const added = acc.add(posts, round);
    noNewRounds = added === 0 ? noNewRounds + 1 : 0;
    const lowest = posts.filter(p => p.datetime).sort((a, b) => b.top - a.top)[0];
    stopReason = decideStop({ round, maxScrolls: opts.maxScrolls, noNewRounds, lowestVisibleAt: lowest?.datetime, windowStartMs });
  }

  // 3. 回頂部重讀首屏，做為獨立對照
  await cdp.evaluate('window.scrollTo(0, 0)');
  await sleep(2000);
  const head = await extract();
  acc.add(head, round + 1);
  const headRecheckKeys = head.map(p => p.postKey);

  const posts = acc.values().map(({ top, ...rest }) => rest);
  const invariants = checkInvariants({
    finalKeys: acc.keys(),
    firstScreenKeys,
    headRecheckKeys: [],
    knownPosts: source.knownPosts || [],
    windowStartMs,
    loginWall,
    nowMs: opts.nowMs,
  });
  // 回頂部才第一次出現的貼文：資料已補進輸出，但代表首屏當時未載完整，列為警告
  const firstSeen = new Map(acc.values().map(p => [p.postKey, p.firstSeenRound]));
  invariants.warnings = [];
  invariants.headNew = headRecheckKeys.filter(k => firstSeen.get(k) === round + 1);
  if (invariants.headNew.length) invariants.warnings.push('head-recheck-found-new');
  const { oldestPostAt, newestPostAt } = calculateMinMaxTimes(posts);
  return {
    source: source.key, url, kind, handle, fetchedAt, ready, loginWall,
    firstScreen: { postKeys: firstScreenKeys, count: firstScreenKeys.length },
    headRecheck: { postKeys: headRecheckKeys },
    scrolls: round, stopReason, invariants,
    posts, oldestPostAt, newestPostAt,
    _firstShot: firstShot,
  };
}

async function downloadImages(posts, mediaDir, cdp) {
  mkdirSync(mediaDir, { recursive: true });
  for (const p of posts) {
    p.media = [];
    for (const src of p.images || []) {
      let buf = null;
      let method = 'node-fetch';
      try {
        const res = await fetch(src, { signal: AbortSignal.timeout(20000) });
        if (res.ok) buf = Buffer.from(await res.arrayBuffer());
      } catch {}
      if (!buf && cdp) {
        method = 'page-fetch';
        try {
          const b64 = await cdp.evaluate(`fetch(${JSON.stringify(src)}).then(r => r.ok ? r.arrayBuffer() : null).then(ab => {
            if (!ab) return null; let s = ''; const u = new Uint8Array(ab);
            for (let i = 0; i < u.length; i += 0x8000) s += String.fromCharCode.apply(null, u.subarray(i, i + 0x8000));
            return btoa(s); }).catch(() => null)`);
          if (b64) buf = Buffer.from(b64, 'base64');
        } catch {}
      }
      if (!buf || buf.length < 1000) { p.media.push({ src, status: 'failed' }); continue; }
      const sha = createHash('sha256').update(buf).digest('hex');
      const ext = buf[0] === 0x89 ? 'png' : (buf.slice(8, 12).toString() === 'WEBP' ? 'webp' : 'jpg');
      const file = path.join(mediaDir, `${sha}.${ext}`);
      if (!existsSync(file)) writeFileSync(file, buf);
      p.media.push({ src, status: 'downloaded', sha256: sha, file, bytes: buf.length, method });
    }
  }
}

export async function run({ sources, outDir, mediaDir, testProfile, opts = {}, emit = obj => process.stdout.write(JSON.stringify(obj) + '\n') }) {
  const options = {
    windowDays: 7, maxScrolls: 20, scrollStep: 1200, threadsWaitMs: 1800, facebookWaitMs: 2500,
    readySeconds: 20, nowMs: Date.now(), retries: 3, ...opts,
  };
  mkdirSync(outDir, { recursive: true });
  const profile = resolveProfile(testProfile);
  const cdp = await launchEdge(profile);
  try {
    for (const source of sources) {
      let result = null;
      for (let attempt = 1; attempt <= options.retries + 1; attempt++) {
        const url = attempt === 4 && source.kind === 'facebook' ? `${source.url.replace(/\/$/, '')}/posts/` : source.url;
        const startedAt = new Date().toISOString();
        try {
          result = await capture(cdp, { ...source, url }, options);
          result.error = null;
        } catch (err) {
          result = { source: source.key, url, kind: source.kind, handle: source.handle, fetchedAt: startedAt, posts: [], error: String(err.message || err), stopReason: 'error', invariants: { ok: false, problems: ['error'] } };
        }
        result.attempt = attempt;
        const failed = result.error || result.loginWall || result.posts.length === 0 || result.invariants.problems.includes('first-screen-lost');
        if (!failed || attempt === options.retries + 1) break;
        emit({ type: 'attempt', source: source.key, attempt, url, state: 'failed', posts: result.posts.length, loginWall: !!result.loginWall, error: result.error, stopReason: result.stopReason, problems: result.invariants.problems });
        await sleep(attempt === 1 ? 2000 : attempt === 2 ? 30000 : 60000);
      }
      const base = source.key.replace(':', '_');
      if (result._firstShot) writeFileSync(path.join(outDir, `${base}.first.png`), result._firstShot);
      delete result._firstShot;
      if (mediaDir && result.posts.length) await downloadImages(result.posts, mediaDir, cdp);
      const jsonPath = path.join(outDir, `${base}.json`);
      writeFileSync(jsonPath, JSON.stringify(result, null, 2));
      emit({ type: 'source', source: source.key, path: jsonPath, attempt: result.attempt, posts: result.posts.length, loginWall: !!result.loginWall, error: result.error || null, stopReason: result.stopReason, problems: result.invariants.problems, newestPostAt: result.newestPostAt || null, oldestPostAt: result.oldestPostAt || null, firstScreen: result.firstScreen?.count ?? 0, scrolls: result.scrolls ?? 0, images: result.posts.reduce((n, p) => n + (p.media || []).filter(m => m.status === 'downloaded').length, 0) });
    }
  } finally {
    await cdp.close();
  }
}

async function main() {
  const args = process.argv.slice(2);
  const get = name => { const i = args.indexOf(name); return i >= 0 ? args[i + 1] : null; };
  const sourcesPath = get('--sources');
  const outDir = get('--out');
  if (!sourcesPath || !outDir) {
    console.error('用法: node scripts/patrol_v2/social_capture.mjs --sources <sources.json> --out <dir> [--media <dir>] [--test-profile <暫存目錄>] [--opts <json>]');
    process.exit(2);
  }
  const sources = JSON.parse(readFileSync(sourcesPath, 'utf-8'));
  const opts = get('--opts') ? JSON.parse(get('--opts')) : {};
  await run({ sources, outDir, mediaDir: get('--media'), testProfile: get('--test-profile'), opts });
}

const isMain = process.argv[1] && fileURLToPath(import.meta.url) === path.resolve(process.argv[1]);
if (isMain) {
  main().catch(err => { console.error('執行失敗：', err); process.exit(1); });
}
