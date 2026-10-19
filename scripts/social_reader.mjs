#!/usr/bin/env node
import { spawn, execSync } from 'node:child_process';
import { existsSync, mkdirSync, writeFileSync, lstatSync, readlinkSync, readdirSync, statSync, rmSync } from 'node:fs';
import { createServer } from 'node:net';
import path from 'node:path';
import { fileURLToPath } from 'node:url';

// --- 純函式（由 tests/test_social_reader.mjs 測試） ---

export function determineStatus(posts, loginWall) {
  if (!posts || posts.length === 0) {
    return { state: 'failed', media: 'unread' };
  }
  return { state: 'partial', media: 'unread' };
}

export function isFacebookLoginWall({ storyMessageCount = 0, hasEmailInput = false, hasLoginForm = false, isLoginUrl = false }) {
  const hasLoginField = Boolean(hasEmailInput || hasLoginForm || isLoginUrl);
  return storyMessageCount === 0 && hasLoginField;
}

export function isSeeMoreButton(rawText) {
  if (!rawText || typeof rawText !== 'string') return false;
  const clean = rawText.replace(/\s+/g, '');
  return clean === '查看更多' || clean === '顯示更多' || clean === 'Seemore';
}

export function utcToTaipeiIso(utcStr) {
  const d = new Date(utcStr);
  if (isNaN(d.getTime())) return null;
  const tpe = new Date(d.getTime() + 8 * 60 * 60 * 1000);
  const Y = tpe.getUTCFullYear();
  const M = String(tpe.getUTCMonth() + 1).padStart(2, '0');
  const D = String(tpe.getUTCDate()).padStart(2, '0');
  const h = String(tpe.getUTCHours()).padStart(2, '0');
  const m = String(tpe.getUTCMinutes()).padStart(2, '0');
  const s = String(tpe.getUTCSeconds()).padStart(2, '0');
  return `${Y}-${M}-${D}T${h}:${m}:${s}+08:00`;
}

export function extractFacebookTimeText(raw) {
  if (!raw) return '';
  return String(raw).replace(/[\u034f\u200b-\u200d\ufeff]/g, '').trim();
}

export function parseFacebookTime(timeText, fetchedAt = new Date().toISOString()) {
  if (!timeText || typeof timeText !== 'string') return null;
  const raw = timeText.replace(/[\u034f\u200b-\u200d\ufeff]/g, '').trim();
  const base = new Date(fetchedAt);
  if (isNaN(base.getTime())) return null;

  function toTaipeiIso(d) {
    const tpe = new Date(d.getTime() + 8 * 60 * 60 * 1000);
    const Y = tpe.getUTCFullYear();
    const M = String(tpe.getUTCMonth() + 1).padStart(2, '0');
    const D = String(tpe.getUTCDate()).padStart(2, '0');
    const h = String(tpe.getUTCHours()).padStart(2, '0');
    const m = String(tpe.getUTCMinutes()).padStart(2, '0');
    const s = String(tpe.getUTCSeconds()).padStart(2, '0');
    return `${Y}-${M}-${D}T${h}:${m}:${s}+08:00`;
  }

  // 1. 分鐘：N分鐘 / N 分鐘
  let m = raw.match(/^(\d+)\s*分鐘/);
  if (m) {
    const mins = parseInt(m[1], 10);
    return toTaipeiIso(new Date(base.getTime() - mins * 60 * 1000));
  }

  // 2. 小時：N小時 / N 小時
  m = raw.match(/^(\d+)\s*小時/);
  if (m) {
    const hours = parseInt(m[1], 10);
    return toTaipeiIso(new Date(base.getTime() - hours * 3600 * 1000));
  }

  // 3. 天：N天 / N 天
  m = raw.match(/^(\d+)\s*天/);
  if (m) {
    const days = parseInt(m[1], 10);
    return toTaipeiIso(new Date(base.getTime() - days * 86400 * 1000));
  }

  // 4. 週：N週 / N 週
  m = raw.match(/^(\d+)\s*週/);
  if (m) {
    const weeks = parseInt(m[1], 10);
    return toTaipeiIso(new Date(base.getTime() - weeks * 7 * 86400 * 1000));
  }

  // 5. 昨天：昨天 HH:MM 或 昨天 上午/下午H:MM
  m = raw.match(/^昨天\s*(上午|下午)?\s*(\d{1,2}):(\d{2})/);
  if (m) {
    const ampm = m[1];
    let h = parseInt(m[2], 10);
    const min = parseInt(m[3], 10);
    if (ampm === '下午' && h < 12) h += 12;
    if (ampm === '上午' && h === 12) h = 0;
    const tpeBase = new Date(base.getTime() + 8 * 60 * 60 * 1000);
    const prevDay = new Date(Date.UTC(tpeBase.getUTCFullYear(), tpeBase.getUTCMonth(), tpeBase.getUTCDate() - 1, h - 8, min, 0));
    return toTaipeiIso(prevDay);
  }

  // 6. 完整日期：YYYY年M月D日 星期X 上午/下午H:MM
  m = raw.match(/^(\d{4})年(\d{1,2})月(\d{1,2})日(?:\s*星期[一二三四五六日天])?\s*(上午|下午)?\s*(\d{1,2}):(\d{2})/);
  if (m) {
    const Y = parseInt(m[1], 10);
    const M = parseInt(m[2], 10) - 1;
    const D = parseInt(m[3], 10);
    const ampm = m[4];
    let h = parseInt(m[5], 10);
    const min = parseInt(m[6], 10);
    if (ampm === '下午' && h < 12) h += 12;
    if (ampm === '上午' && h === 12) h = 0;
    const dt = new Date(Date.UTC(Y, M, D, h - 8, min, 0));
    return toTaipeiIso(dt);
  }

  // 7. 月日：M月D日 或 M月D日 上午/下午H:MM
  m = raw.match(/^(\d{1,2})月(\d{1,2})日(?:\s*(上午|下午)?\s*(\d{1,2}):(\d{2}))?/);
  if (m) {
    const M = parseInt(m[1], 10) - 1;
    const D = parseInt(m[2], 10);
    const ampm = m[3];
    let h = m[4] ? parseInt(m[4], 10) : 12;
    const min = m[5] ? parseInt(m[5], 10) : 0;
    if (ampm === '下午' && h < 12) h += 12;
    if (ampm === '上午' && h === 12) h = 0;

    const tpeBase = new Date(base.getTime() + 8 * 60 * 60 * 1000);
    let Y = tpeBase.getUTCFullYear();
    let dt = new Date(Date.UTC(Y, M, D, h - 8, min, 0));
    if (dt.getTime() > base.getTime()) {
      Y -= 1;
      dt = new Date(Date.UTC(Y, M, D, h - 8, min, 0));
    }
    return toTaipeiIso(dt);
  }

  return null;
}

export function isAuthorPost(postUrl, handle) {
  if (!postUrl || !handle) return false;
  try {
    const parsed = new URL(postUrl);
    const targetPrefix = `/@${handle.toLowerCase()}/post/`;
    return parsed.pathname.toLowerCase().startsWith(targetPrefix);
  } catch {
    const targetPrefix = `/@${handle.toLowerCase()}/post/`;
    return postUrl.toLowerCase().includes(targetPrefix);
  }
}

export function normalizePostUrl(rawUrl) {
  if (!rawUrl || typeof rawUrl !== 'string') return null;
  if (rawUrl.includes('comment_id=')) return null;
  return rawUrl.split('?')[0];
}

export function calculateMinMaxTimes(posts) {
  if (!posts || !Array.isArray(posts)) {
    return { oldestPostAt: null, newestPostAt: null };
  }
  const validTimes = posts
    .map(p => p.datetime)
    .filter(t => t && typeof t === 'string' && !isNaN(new Date(t).getTime()));

  if (validTimes.length === 0) {
    return { oldestPostAt: null, newestPostAt: null };
  }

  validTimes.sort((a, b) => new Date(a).getTime() - new Date(b).getTime());
  return {
    oldestPostAt: validTimes[0],
    newestPostAt: validTimes[validTimes.length - 1]
  };
}

// --- CDP 助手 ---

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

const sleep = ms => new Promise(r => setTimeout(r, ms));

export function cleanOldEvidence(evidenceBaseDir = 'patrol_evidence') {
  if (!existsSync(evidenceBaseDir)) return;
  const now = Date.now();
  const fourteenDaysMs = 14 * 24 * 60 * 60 * 1000;
  try {
    const entries = readdirSync(evidenceBaseDir, { withFileTypes: true });
    for (const entry of entries) {
      if (entry.isDirectory()) {
        const dirPath = path.join(evidenceBaseDir, entry.name);
        try {
          const stat = statSync(dirPath);
          if (now - stat.mtimeMs > fourteenDaysMs) {
            rmSync(dirPath, { recursive: true, force: true });
            console.log(`[清理舊證據] 已刪除 14 天前的證據目錄：${entry.name}`);
          }
        } catch {}
      }
    }
  } catch {}
}

export function checkEdgeLock(profileDir = '/Users/eric/.patrol-edge') {
  const lockPath = path.join(profileDir, 'SingletonLock');
  try {
    const stat = lstatSync(lockPath);
    if (stat.isSymbolicLink()) {
      const target = readlinkSync(lockPath);
      const parts = target.split('-');
      const pid = parseInt(parts[parts.length - 1], 10);
      if (!isNaN(pid)) {
        try {
          process.kill(pid, 0);
          throw new Error(`設定檔已被其他 Edge 程序（PID ${pid}）佔用，請先關閉。`);
        } catch (e) {
          if (e.code === 'EPERM') {
            throw new Error(`設定檔已被其他 Edge 程序（PID ${pid}，權限限制）佔用，請先關閉。`);
          }
          // ESRCH: 舊 stale lock，程序已結束，略過
        }
      }
    }
  } catch (err) {
    if (err.message.includes('設定檔已被其他 Edge')) throw err;
  }
}

async function launchEdge(port, profileDir = '/Users/eric/.patrol-edge') {
  checkEdgeLock(profileDir);

  const edgeBin = '/Applications/Microsoft Edge.app/Contents/MacOS/Microsoft Edge';
  const args = [
    '--headless=new',
    `--remote-debugging-port=${port}`,
    `--user-data-dir=${profileDir}`,
    '--lang=zh-TW',
    '--no-first-run',
    '--no-default-browser-check',
    '--window-size=1280,2000',
    'about:blank'
  ];

  const proc = spawn(edgeBin, args, { stdio: 'ignore' });

  let tabs = null;
  for (let i = 0; i < 30; i++) {
    try {
      const res = await fetch(`http://127.0.0.1:${port}/json`);
      tabs = await res.json();
      if (tabs && tabs.length > 0) break;
    } catch {
      await sleep(300);
    }
  }

  if (!tabs) {
    proc.kill();
    throw new Error('無法連線到 Edge DevTools WebSocket');
  }

  const pageTab = tabs.find(t => t.type === 'page') || tabs[0];
  const ws = new WebSocket(pageTab.webSocketDebuggerUrl);
  await new Promise((resolve, reject) => {
    ws.onopen = resolve;
    ws.onerror = reject;
  });

  let id = 0;
  const pend = new Map();
  ws.onmessage = e => {
    try {
      const m = JSON.parse(e.data);
      if (pend.has(m.id)) {
        pend.get(m.id)(m);
        pend.delete(m.id);
      }
    } catch {}
  };

  const send = (method, params = {}) => new Promise((resolve, reject) => {
    const i = ++id;
    pend.set(i, resolve);
    try {
      ws.send(JSON.stringify({ id: i, method, params }));
    } catch (err) {
      reject(err);
    }
  });

  const evaluate = async (expr) => {
    const res = await send('Runtime.evaluate', {
      expression: expr,
      returnByValue: true,
      awaitPromise: true
    });
    return res.result?.result?.value;
  };

  const sendEscape = async () => {
    try {
      await send('Input.dispatchKeyEvent', {
        type: 'rawKeyDown',
        key: 'Escape',
        code: 'Escape',
        windowsVirtualKeyCode: 27
      });
      await send('Input.dispatchKeyEvent', {
        type: 'keyUp',
        key: 'Escape',
        code: 'Escape',
        windowsVirtualKeyCode: 27
      });
    } catch {}
  };

  const captureScreenshot = async (clip = null) => {
    const params = {
      format: 'png',
      captureBeyondViewport: false
    };
    if (clip) {
      params.clip = clip;
    }
    const shot = await send('Page.captureScreenshot', params);
    if (shot.result?.data) {
      return Buffer.from(shot.result.data, 'base64');
    }
    return null;
  };

  const close = async () => {
    try { ws.close(); } catch {}
    try { proc.kill(); } catch {}
  };

  await send('Page.enable');
  await send('Runtime.enable');

  return { proc, ws, send, evaluate, sendEscape, captureScreenshot, close };
}

// --- 登入確認模式 ---

async function runCheckLogin() {
  console.log('啟動 Edge 進行登入確認（--check-login）...');
  const port = await getFreePort();
  const cdp = await launchEdge(port);

  let threadsPassed = false;
  let fbPassed = false;

  try {
    console.log('正在檢查 Threads 登入態...');
    await cdp.send('Page.navigate', { url: 'https://www.threads.com/' });
    let hasTime = false;
    for (let i = 0; i < 15; i++) {
      await sleep(1000);
      const times = await cdp.evaluate("document.querySelectorAll('time[datetime]').length");
      if (times > 0) {
        hasTime = true;
        break;
      }
    }
    const threadsUrl = (await cdp.evaluate("window.location.href")) || '';
    const threadsText = (await cdp.evaluate("document.body.innerText.slice(0, 3000)")) || '';
    const threadsHasLoginBtn = /登入|登录|Log in|建立新帳號/.test(threadsText) && threadsUrl.includes('/login');

    console.log(`Threads: 登入按鈕/頁面=${threadsHasLoginBtn ? '有' : '無'}, 首頁貼文時間=${hasTime ? '有' : '無'}`);
    threadsPassed = (!threadsHasLoginBtn && hasTime);

    console.log('正在檢查 Facebook 登入態...');
    await cdp.send('Page.navigate', { url: 'https://www.facebook.com/' });
    await sleep(5000);
    const fbInfo = await cdp.evaluate(`(() => {
      const url = window.location.href;
      const hasLoginInput = Boolean(document.querySelector('input[name="email"], button[name="login"]'));
      const hasFeed = Boolean(document.querySelector('div[role="feed"], [role="main"]'));
      const isLoginUrl = url.includes('/login');
      const bodyText = document.body.innerText.slice(0, 3000);
      return { url, hasLoginInput, hasFeed, isLoginUrl, bodyText };
    })()`);

    const fbLoginWall = fbInfo.isLoginUrl || fbInfo.hasLoginInput;
    console.log(`Facebook: 登入頁/輸入框=${fbLoginWall ? '有' : '無'}, 動態消息=${fbInfo.hasFeed ? '有' : '無'}`);
    fbPassed = (!fbLoginWall && fbInfo.hasFeed);

  } finally {
    await cdp.close();
  }

  const result = {
    threads: { passed: threadsPassed },
    facebook: { passed: fbPassed },
    allPassed: threadsPassed && fbPassed
  };

  console.log('登入確認結果：', JSON.stringify(result, null, 2));
  if (!result.allPassed) {
    process.exit(1);
  }
}

// --- 抓取 Threads 來源 ---

async function scrapeThreads(cdp, url, handle) {
  await cdp.send('Page.navigate', { url });
  let hasTime = false;
  for (let i = 0; i < 15; i++) {
    await sleep(1000);
    const n = await cdp.evaluate("document.querySelectorAll('time[datetime]').length");
    if (n > 0) {
      hasTime = true;
      break;
    }
  }

  const currentUrl = (await cdp.evaluate("window.location.href")) || '';
  const bodyText = (await cdp.evaluate("document.body.innerText.slice(0, 3000)")) || '';
  const hasDialog = await cdp.evaluate("Boolean(document.querySelector('div[role=\"dialog\"]'))");
  const loginWall = currentUrl.includes('/login') || /登入|登录|Log in|建立新帳號/.test(bodyText) || (hasDialog && /登入/.test(bodyText));

  let scrolls = 0;
  let lastCount = 0;
  let noNewPostCount = 0;
  const sevenDaysAgo = Date.now() - 7 * 24 * 60 * 60 * 1000;

  for (let i = 0; i < 15; i++) {
    await cdp.evaluate("window.scrollBy(0, 2500)");
    scrolls++;
    await sleep(1500);

    const count = (await cdp.evaluate("document.querySelectorAll('time[datetime]').length")) || 0;
    if (count === lastCount) {
      noNewPostCount++;
    } else {
      noNewPostCount = 0;
    }
    lastCount = count;

    const oldestIso = await cdp.evaluate(`
      (() => {
        const times = document.querySelectorAll('time[datetime]');
        if (!times.length) return null;
        return times[times.length - 1].getAttribute('datetime');
      })()
    `);
    if (oldestIso) {
      const oldestTime = new Date(oldestIso).getTime();
      if (!isNaN(oldestTime) && oldestTime < sevenDaysAgo) {
        break;
      }
    }

    if (noNewPostCount >= 2) {
      break;
    }
  }

  // 擷取貼文（容器：從 time 往上找，取仍然只包含 1 個 time[datetime] 的最外層祖先）
  const rawPosts = await cdp.evaluate(`
    (() => {
      const times = document.querySelectorAll('time[datetime]');
      const res = [];
      for (const t of times) {
        const dt = t.getAttribute('datetime');
        const a = t.closest('a[href*="/post/"]') || t.parentElement.querySelector('a[href*="/post/"]');
        const postLink = a ? a.href : null;
        if (!postLink) continue;

        let container = t;
        let cur = t.parentElement;
        while (cur && cur !== document.body) {
          const count = cur.querySelectorAll('time[datetime]').length;
          if (count === 1) {
            container = cur;
            cur = cur.parentElement;
          } else {
            break;
          }
        }

        let nested = false;
        if (container === t && t.parentElement) {
          container = t.parentElement;
          nested = true;
        }

        const text = (container.innerText || '').replace(/\\s+/g, ' ').trim().slice(0, 2000);
        const imgs = Array.from(container.querySelectorAll('img'))
          .filter(img => (img.naturalWidth || img.width || 0) > 150)
          .map(img => img.src);

        res.push({
          rawDatetime: dt,
          rawUrl: postLink,
          text,
          nested,
          images: imgs
        });
      }
      return res;
    })()
  `) || [];

  // 作者過濾、網址正規化與去重
  const seenUrls = new Set();
  const posts = [];
  for (const p of rawPosts) {
    const cleanUrl = normalizePostUrl(p.rawUrl);
    if (!cleanUrl) continue;
    if (handle && !isAuthorPost(cleanUrl, handle)) {
      continue;
    }
    if (seenUrls.has(cleanUrl)) continue;
    seenUrls.add(cleanUrl);

    posts.push({
      url: cleanUrl,
      datetime: utcToTaipeiIso(p.rawDatetime) || p.rawDatetime,
      text: p.text,
      nested: p.nested || false,
      images: p.images
    });
  }

  const { oldestPostAt, newestPostAt } = calculateMinMaxTimes(posts);

  return {
    url,
    fetchedAt: new Date().toISOString(),
    loginWall,
    posts,
    oldestPostAt,
    newestPostAt,
    scrolls
  };
}

// --- 抓取 Facebook 來源 ---

async function scrapeFacebook(cdp, url) {
  const fetchedAt = new Date().toISOString();
  await cdp.send('Page.navigate', { url });
  await sleep(4000);

  // 1. 頁面載入後先送一次 Escape 鍵關閉通知面板
  await cdp.sendEscape();

  // 等待 story_message 出現（最多 15 秒）
  for (let i = 0; i < 15; i++) {
    await sleep(1000);
    const n = await cdp.evaluate("document.querySelectorAll('[data-ad-rendering-role=\"story_message\"]').length");
    if (n > 0) break;
  }

  const currentUrl = (await cdp.evaluate("window.location.href")) || '';
  const initialCheck = await cdp.evaluate(`
    (() => {
      const storyCount = document.querySelectorAll('[data-ad-rendering-role="story_message"]').length;
      const hasEmail = Boolean(document.querySelector('input[name="email"]'));
      const hasForm = Boolean(document.querySelector('form[action*="login"]'));
      const isLogin = window.location.href.includes('/login');
      return { storyCount, hasEmail, hasForm, isLogin };
    })()
  `) || { storyCount: 0, hasEmail: false, hasForm: false, isLogin: false };

  const loginWall = isFacebookLoginWall({
    storyMessageCount: initialCheck.storyCount,
    hasEmailInput: initialCheck.hasEmail,
    hasLoginForm: initialCheck.hasForm,
    isLoginUrl: initialCheck.isLogin
  });

  let scrolls = 0;
  let lastCount = 0;
  let noNewCount = 0;
  const sevenDaysAgo = Date.now() - 7 * 24 * 60 * 60 * 1000;

  for (let i = 0; i < 15; i++) {
    // 3. 「查看更多」只能點 story_message 裡面的元素
    await cdp.evaluate(`
      (() => {
        const msgs = document.querySelectorAll('[data-ad-rendering-role="story_message"]');
        for (const msg of msgs) {
          const btns = Array.from(msg.querySelectorAll('[role="button"], span, div'));
          for (const b of btns) {
            const txt = (b.innerText || '').replace(/\\s+/g, '');
            if (txt === '查看更多' || txt === '顯示更多' || txt === 'Seemore') {
              try { b.click(); } catch {}
            }
          }
        }
      })()
    `);
    await sleep(300);

    const hasPostDialog = await cdp.evaluate(`
      (() => {
        const dlg = document.querySelector('[role="dialog"]');
        return Boolean(dlg && (dlg.innerText || '').includes('的貼文'));
      })()
    `);
    if (hasPostDialog) {
      await cdp.sendEscape();
    }

    // 每次捲動前也送一次 Escape
    await cdp.sendEscape();

    // 捲動 2500px，間隔 2.5 秒
    await cdp.evaluate("window.scrollBy(0, 2500)");
    scrolls++;
    await sleep(2500);

    const count = (await cdp.evaluate("document.querySelectorAll('[data-ad-rendering-role=\"story_message\"]').length")) || 0;
    if (count === lastCount) {
      noNewCount++;
    } else {
      noNewCount = 0;
    }
    lastCount = count;

    // 檢查已辨識貼文中最舊一篇是否早於 7 天前
    const oldestCandidateText = await cdp.evaluate(`
      (() => {
        const msgs = document.querySelectorAll('[data-ad-rendering-role="story_message"]');
        for (let idx = msgs.length - 1; idx >= 0; idx--) {
          const m = msgs[idx];
          let c = m;
          for (let k = 0; k < 25 && c.parentElement; k++) {
            const p = c.parentElement;
            if (p.querySelectorAll('[data-ad-rendering-role="story_message"]').length > 1) break;
            c = p;
          }
          const links = Array.from(c.querySelectorAll('a[href]'));
          for (const a of links) {
            const h = a.getAttribute('href') || '';
            if (/posts|story_fbid|permalink|videos|reel/.test(h) && !h.includes('comment_id=')) {
              const aria = a.getAttribute('aria-label');
              if (aria) return aria;
            }
          }
        }
        return null;
      })()
    `);
    if (oldestCandidateText) {
      const parsedDt = parseFacebookTime(oldestCandidateText, fetchedAt);
      if (parsedDt) {
        const t = new Date(parsedDt).getTime();
        if (!isNaN(t) && t < sevenDaysAgo) {
          break;
        }
      }
    }

    if (noNewCount >= 3) {
      break;
    }
  }

  // 擷取貼文
  const rawPosts = await cdp.evaluate(`
    (() => {
      const msgs = Array.from(document.querySelectorAll('[data-ad-rendering-role="story_message"]'));
      const res = [];
      const seen = new Set();

      for (const m of msgs) {
        // text 取 story_message 自身 innerText，最長 2000 字
        const text = (m.innerText || '').slice(0, 2000);

        // 容器：從 story_message 往上找，取仍只包含 1 個 story_message 的最外層祖先
        let container = m;
        for (let k = 0; k < 25 && container.parentElement; k++) {
          const p = container.parentElement;
          if (p.querySelectorAll('[data-ad-rendering-role="story_message"]').length > 1) break;
          container = p;
        }

        // 貼文連結：優先找符合 /posts/、story_fbid、/permalink、/videos/、/reel/ 的 a；若無則找 /photo/
        let postUrl = null;
        let timeText = null;
        const links = Array.from(container.querySelectorAll('a[href]'));

        for (const a of links) {
          const rawHref = a.getAttribute('href') || a.href || '';
          if (rawHref.includes('comment_id=')) continue;
          if (/posts|story_fbid|permalink|videos|reel/.test(rawHref)) {
            let h = rawHref.split('?')[0];
            if (h.startsWith('/')) {
              h = 'https://www.facebook.com' + h;
            }
            postUrl = h;
            const aria = a.getAttribute('aria-label');
            if (aria) {
              timeText = aria.trim();
            }
            break;
          }
        }

        if (!postUrl) {
          for (const a of links) {
            const rawHref = a.getAttribute('href') || a.href || '';
            if (rawHref.includes('comment_id=')) continue;
            if (/photo/.test(rawHref)) {
              let h = rawHref.split('?')[0];
              if (h.startsWith('/')) {
                h = 'https://www.facebook.com' + h;
              }
              postUrl = h;
              const aria = a.getAttribute('aria-label');
              if (aria) {
                timeText = aria.trim();
              }
              break;
            }
          }
        }

        // 圖片：容器內寬度 > 150 的 img
        const imgs = Array.from(container.querySelectorAll('img'))
          .filter(img => (img.naturalWidth || img.width || 0) > 150)
          .map(img => img.src);

        // 去重：有連結用連結當 key，沒有用 text 前 80 字
        const key = postUrl || text.slice(0, 80);
        if (!key || seen.has(key)) continue;
        seen.add(key);

        res.push({
          postUrl,
          text,
          timeText,
          images: imgs
        });
      }
      return res;
    })()
  `) || [];

  const posts = [];
  for (const p of rawPosts) {
    const parsedDt = p.timeText ? parseFacebookTime(p.timeText, fetchedAt) : null;
    posts.push({
      url: p.postUrl || '',
      timeText: p.timeText || null,
      datetime: parsedDt,
      text: p.text,
      images: p.images
    });
  }

  const { oldestPostAt, newestPostAt } = calculateMinMaxTimes(posts);

  return {
    url,
    fetchedAt,
    loginWall,
    posts,
    oldestPostAt,
    newestPostAt,
    scrolls
  };
}

// --- 執行巡檢 ---

async function runScrape(runFile, outDir, targetSource) {
  if (!existsSync(outDir)) {
    mkdirSync(outDir, { recursive: true });
  }

  // 2-5 第 2 點：刪除 patrol_evidence 中 14 天前的子目錄
  cleanOldEvidence('patrol_evidence');

  const summaryOut = execSync(`python3 scripts/patrol_progress.py summary --run ${runFile}`, { encoding: 'utf-8' });
  const summary = JSON.parse(summaryOut);
  const sources = summary.sources || {};

  const keysToProcess = Object.keys(sources).filter(k => {
    if (targetSource && k !== targetSource) return false;
    return k.startsWith('threads:') || k.startsWith('facebook:');
  });

  console.log(`準備處理 ${keysToProcess.length} 個社群來源...`);

  const port = await getFreePort();
  const cdp = await launchEdge(port);

  try {
    for (const key of keysToProcess) {
      console.log(`\n=== 開始處理來源：${key} ===`);
      const runData = JSON.parse(execSync(`cat ${runFile}`, { encoding: 'utf-8' }));
      let currentUrl = runData.sources?.[key]?.url || '';
      const handle = key.startsWith('threads:') ? key.replace('threads:', '') : null;

      let attempt = 1;
      let finalData = null;

      while (attempt <= 4) {
        console.log(`[${key}] 嘗試第 ${attempt} 次...`);
        let scrapeRes = null;
        try {
          if (key.startsWith('threads:')) {
            scrapeRes = await scrapeThreads(cdp, currentUrl, handle);
          } else {
            scrapeRes = await scrapeFacebook(cdp, currentUrl);
          }
        } catch (err) {
          console.error(`[${key}] 抓取拋出異常：`, err.message);
          scrapeRes = { url: currentUrl, fetchedAt: new Date().toISOString(), loginWall: true, posts: [], scrolls: 0, oldestPostAt: null, newestPostAt: null };
        }

        scrapeRes.attempt = attempt;
        finalData = scrapeRes;

        const status = determineStatus(scrapeRes.posts, scrapeRes.loginWall);
        console.log(`[${key}] 第 ${attempt} 次結果：${scrapeRes.posts.length} 篇貼文，狀態=${status.state}`);

        if (status.state !== 'failed' || attempt >= 4) {
          break;
        }

        const scope = `第 ${attempt} 次嘗試：擷取 0 篇；登入牆＝${scrapeRes.loginWall ? '是' : '否'}`;
        const recordCmd = [
          'python3', 'scripts/patrol_progress.py', 'record',
          '--run', runFile,
          '--source', key,
          '--state', 'failed',
          '--method', 'social-reader-cdp',
          '--url', currentUrl,
          '--media', 'unread',
          '--scope', scope,
          '--detail', `嘗試第 ${attempt} 次失敗`
        ];
        execSync(recordCmd.map(x => `"${x.replace(/"/g, '\\"')}"`).join(' '));

        attempt++;
        if (attempt === 2) {
          console.log(`[${key}] 第 1 次重試：重新載入...`);
          await sleep(2000);
        } else if (attempt === 3) {
          console.log(`[${key}] 第 2 次重試：等待 30 秒後重新開啟...`);
          await sleep(30000);
        } else if (attempt === 4) {
          if (key.startsWith('facebook:')) {
            const fbHandle = key.replace('facebook:', '');
            currentUrl = `https://www.facebook.com/${fbHandle}/posts/`;
            console.log(`[${key}] 第 3 次重試：開 posts 子頁 ${currentUrl}...`);
          } else {
            console.log(`[${key}] 第 3 次重試：等待 60 秒後重新開個人頁...`);
          }
          await sleep(60000);
        }
      }

      const jsonPath = path.join(outDir, `${key.replace(':', '_')}.json`);
      writeFileSync(jsonPath, JSON.stringify(finalData, null, 2));

      try {
        let shotBuf = null;
        if (key.startsWith('facebook:')) {
          shotBuf = await cdp.captureScreenshot({ x: 280, y: 0, width: 720, height: 1800, scale: 1 });
        } else {
          shotBuf = await cdp.captureScreenshot();
        }
        if (shotBuf) {
          const pngPath = path.join(outDir, `${key.replace(':', '_')}.png`);
          writeFileSync(pngPath, shotBuf);
        }
      } catch (err) {
        console.error(`[${key}] 截圖失敗：`, err.message);
      }

      const finalStatus = determineStatus(finalData.posts, finalData.loginWall);
      const postCount = finalData.posts.length;
      const latestPostAt = finalData.newestPostAt || '無';
      const oldestPostAt = finalData.oldestPostAt || '無';
      const unparsedCount = finalData.posts.filter(p => !p.datetime).length;
      const finalScope = `擷取 ${postCount} 篇（本人／頂層）；最新 ${latestPostAt}、最舊 ${oldestPostAt}；含未辨識時間 ${unparsedCount} 篇；登入牆＝${finalData.loginWall ? '是' : '否'}；證據 ${jsonPath}`;

      console.log(`[${key}] 最終 record：${finalStatus.state}，${finalScope}`);
      const recordFinal = [
        'python3', 'scripts/patrol_progress.py', 'record',
        '--run', runFile,
        '--source', key,
        '--state', finalStatus.state,
        '--method', 'social-reader-cdp',
        '--url', finalData.url,
        '--media', finalStatus.media,
        '--scope', finalScope,
        '--detail', `CDP 捲動 ${finalData.scrolls} 次，共保留 ${postCount} 篇（本人/頂層）貼文`
      ];
      execSync(recordFinal.map(x => `"${x.replace(/"/g, '\\"')}"`).join(' '));
    }
  } finally {
    await cdp.close();
  }
}

// --- CLI 入口 ---

async function main() {
  const args = process.argv.slice(2);
  if (args.includes('--check-login')) {
    await runCheckLogin();
    return;
  }

  let runFile = null;
  let outDir = null;
  let sourceKey = null;

  for (let i = 0; i < args.length; i++) {
    if (args[i] === '--run') runFile = args[++i];
    if (args[i] === '--out') outDir = args[++i];
    if (args[i] === '--source') sourceKey = args[++i];
  }

  if (!runFile || !outDir) {
    console.error('用法: node scripts/social_reader.mjs --run patrol_runs/<輪>.json --out patrol_evidence/<輪>/ [--source <鍵>] [--check-login]');
    process.exit(1);
  }

  await runScrape(runFile, outDir, sourceKey);
}

const isMainModule = process.argv[1] && fileURLToPath(import.meta.url) === path.resolve(process.argv[1]);
if (isMainModule) {
  main().catch(err => {
    console.error('執行失敗：', err);
    process.exit(1);
  });
}
