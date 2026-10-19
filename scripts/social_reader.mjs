#!/usr/bin/env node
import { spawn, execSync } from 'node:child_process';
import { existsSync, mkdirSync, writeFileSync } from 'node:fs';
import { createServer } from 'node:net';
import path from 'node:path';

// --- 純函式（由 tests/test_social_reader.mjs 測試） ---

export function determineStatus(posts, loginWall) {
  if (!posts || posts.length === 0) {
    return { state: 'failed', media: 'unread' };
  }
  return { state: 'partial', media: 'unread' };
}

export function utcToTaipeiIso(utcStr) {
  const d = new Date(utcStr);
  if (isNaN(d.getTime())) return null;
  // +8 小時
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
  return String(raw).trim();
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

async function launchEdge(port, profileDir = '/Users/eric/.patrol-edge') {
  // 檢查是否有正在運行的 Edge 使用該 profile
  try {
    const check = execSync(`pgrep -fl "user-data-dir=${profileDir}"`, { encoding: 'utf-8', stdio: ['ignore', 'pipe', 'ignore'] });
    if (check && check.trim()) {
      throw new Error(`設定檔已被其他 Edge 程序佔用，請先關閉：\n${check}`);
    }
  } catch (e) {
    if (e.message.includes('設定檔已被其他 Edge')) throw e;
    // pgrep 返回 1 代表無行程，正常
  }

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

  // 等待 CDP 連線
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

  const captureScreenshot = async () => {
    const shot = await send('Page.captureScreenshot', {
      format: 'png',
      captureBeyondViewport: true
    });
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

  return { proc, ws, send, evaluate, captureScreenshot, close };
}

// --- 登入確認模式 ---

async function runCheckLogin() {
  console.log('啟動 Edge 進行登入確認（--check-login）...');
  const port = await getFreePort();
  const cdp = await launchEdge(port);

  let threadsPassed = false;
  let fbPassed = false;

  try {
    // 檢查 Threads
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

    // 檢查 Facebook
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

async function scrapeThreads(cdp, url) {
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

    // 檢查最舊一篇是否早於 7 天前
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

  // 擷取貼文
  const rawPosts = await cdp.evaluate(`
    (() => {
      const times = document.querySelectorAll('time[datetime]');
      const res = [];
      for (const t of times) {
        const dt = t.getAttribute('datetime');
        const a = t.closest('a[href*="/post/"]') || t.parentElement.querySelector('a[href*="/post/"]');
        const postLink = a ? a.href : null;
        if (!postLink) continue;

        // 往上找外層貼文容器（包含貼文正文）
        let cur = t;
        let card = null;
        for (let k = 0; k < 12 && cur.parentElement; k++) {
          cur = cur.parentElement;
          if (cur.innerText && cur.innerText.length > 30 && cur.querySelector('time[datetime]')) {
            card = cur;
          }
        }
        const container = card || cur;
        const text = (container.innerText || '').replace(/\\s+/g, ' ').trim().slice(0, 2000);
        const imgs = Array.from(container.querySelectorAll('img'))
          .filter(img => (img.naturalWidth || img.width || 0) > 150)
          .map(img => img.src);

        res.push({
          rawDatetime: dt,
          url: postLink,
          text,
          images: imgs
        });
      }
      return res;
    })()
  `) || [];


  // 去重並換算時間
  const seenUrls = new Set();
  const posts = [];
  for (const p of rawPosts) {
    if (seenUrls.has(p.url)) continue;
    seenUrls.add(p.url);
    posts.push({
      url: p.url,
      datetime: utcToTaipeiIso(p.rawDatetime) || p.rawDatetime,
      text: p.text,
      images: p.images
    });
  }

  let oldestPostAt = null;
  if (posts.length > 0) {
    oldestPostAt = posts[posts.length - 1].datetime;
  }

  return {
    url,
    fetchedAt: new Date().toISOString(),
    loginWall,
    posts,
    oldestPostAt,
    scrolls
  };
}

// --- 抓取 Facebook 來源 ---

async function scrapeFacebook(cdp, url) {
  await cdp.send('Page.navigate', { url });
  let hasArticle = false;
  for (let i = 0; i < 15; i++) {
    await sleep(1000);
    const n = await cdp.evaluate("document.querySelectorAll('[role=\"article\"], div[data-pagelet*=\"Timeline\"]').length");
    if (n > 0) {
      hasArticle = true;
      break;
    }
  }

  const currentUrl = (await cdp.evaluate("window.location.href")) || '';
  const bodyText = (await cdp.evaluate("document.body.innerText.slice(0, 3000)")) || '';
  const hasDialog = await cdp.evaluate("Boolean(document.querySelector('div[role=\"dialog\"]'))");
  const loginWall = currentUrl.includes('/login') || /登入|登录|Log in|建立新帳號/.test(bodyText) || (hasDialog && /登入/.test(bodyText));

  let scrolls = 0;
  for (let i = 0; i < 8; i++) {
    // 展開「查看更多」
    await cdp.evaluate(`
      (() => {
        const btns = Array.from(document.querySelectorAll('div[role="button"]'))
          .filter(b => /查看更多|顯示更多|See more/.test(b.innerText || ''));
        for (const b of btns) {
          try { b.click(); } catch {}
        }
      })()
    `);
    await sleep(500);

    await cdp.evaluate("window.scrollBy(0, 2500)");
    scrolls++;
    await sleep(1500);
  }

  const rawPosts = await cdp.evaluate(`
    (() => {
      const articles = document.querySelectorAll('[role="article"]');
      const res = [];
      for (const art of articles) {
        const text = (art.innerText || '').replace(/\\s+/g, ' ').trim().slice(0, 2000);
        const linkElem = art.querySelector('a[href*="/posts/"], a[href*="/permalink"], a[href*="story_fbid"]');
        const postUrl = linkElem ? linkElem.href : null;
        const timeText = linkElem ? (linkElem.getAttribute('aria-label') || linkElem.innerText || '').trim() : '';

        const imgs = Array.from(art.querySelectorAll('img'))
          .filter(img => (img.naturalWidth || img.width || 0) > 150)
          .map(img => img.src);

        if (text.length > 10 || postUrl) {
          res.push({
            url: postUrl || '',
            text,
            timeText,
            images: imgs
          });
        }
      }
      return res;
    })()
  `) || [];

  const seenUrls = new Set();
  const posts = [];
  for (const p of rawPosts) {
    const key = p.url || p.text.slice(0, 50);
    if (seenUrls.has(key)) continue;
    seenUrls.add(key);
    posts.push({
      url: p.url,
      timeText: extractFacebookTimeText(p.timeText),
      datetime: null,
      text: p.text,
      images: p.images
    });
  }

  let oldestPostAt = null;
  if (posts.length > 0) {
    oldestPostAt = posts[posts.length - 1].datetime || posts[posts.length - 1].timeText;
  }

  return {
    url,
    fetchedAt: new Date().toISOString(),
    loginWall,
    posts,
    oldestPostAt,
    scrolls
  };
}

// --- 執行巡檢 ---

async function runScrape(runFile, outDir, targetSource) {
  if (!existsSync(outDir)) {
    mkdirSync(outDir, { recursive: true });
  }

  // 取得 summary
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
      // 讀取該來源原始網址
      const runData = JSON.parse(execSync(`cat ${runFile}`, { encoding: 'utf-8' }));
      const sourceUrl = runData.sources?.[key]?.url || '';

      let attempt = 1;
      let finalData = null;

      while (attempt <= 4) {
        console.log(`[${key}] 嘗試第 ${attempt} 次...`);
        let scrapeRes = null;
        try {
          if (key.startsWith('threads:')) {
            scrapeRes = await scrapeThreads(cdp, sourceUrl);
          } else {
            scrapeRes = await scrapeFacebook(cdp, sourceUrl);
          }
        } catch (err) {
          console.error(`[${key}] 抓取拋出異常：`, err.message);
          scrapeRes = { url: sourceUrl, fetchedAt: new Date().toISOString(), loginWall: true, posts: [], scrolls: 0 };
        }

        scrapeRes.attempt = attempt;
        finalData = scrapeRes;

        const status = determineStatus(scrapeRes.posts, scrapeRes.loginWall);
        console.log(`[${key}] 第 ${attempt} 次結果：${scrapeRes.posts.length} 篇貼文，狀態=${status.state}`);

        if (status.state !== 'failed' || attempt >= 4) {
          break;
        }

        // 失敗重試前先 record 此次嘗試
        const scope = `第 ${attempt} 次嘗試：擷取 0 篇；登入牆＝${scrapeRes.loginWall ? '是' : '否'}`;
        const recordCmd = [
          'python3', 'scripts/patrol_progress.py', 'record',
          '--run', runFile,
          '--source', key,
          '--state', 'failed',
          '--method', 'social-reader-cdp',
          '--url', sourceUrl,
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
          console.log(`[${key}] 第 3 次重試：切換網址模式...`);
          // 切換網址
          if (key.startsWith('threads:')) {
            const handle = key.replace('threads:', '');
            sourceUrl = `https://www.threads.com/search?q=${handle}`;
          } else {
            const handle = key.replace('facebook:', '');
            sourceUrl = `https://m.facebook.com/${handle}`;
          }
        }
      }

      // 儲存證據 JSON
      const jsonPath = path.join(outDir, `${key.replace(':', '_')}.json`);
      writeFileSync(jsonPath, JSON.stringify(finalData, null, 2));

      // 截圖並儲存 PNG
      try {
        const shotBuf = await cdp.captureScreenshot();
        if (shotBuf) {
          const pngPath = path.join(outDir, `${key.replace(':', '_')}.png`);
          writeFileSync(pngPath, shotBuf);
        }
      } catch (err) {
        console.error(`[${key}] 截圖失敗：`, err.message);
      }

      // 判定最終狀態
      const finalStatus = determineStatus(finalData.posts, finalData.loginWall);
      const postCount = finalData.posts.length;
      const latestPostAt = postCount > 0 ? (finalData.posts[0].datetime || finalData.posts[0].timeText || '無') : '無';
      const oldestPostAt = postCount > 0 ? (finalData.oldestPostAt || '無') : '無';
      const finalScope = `擷取 ${postCount} 篇；最新 ${latestPostAt}、最舊 ${oldestPostAt}；登入牆＝${finalData.loginWall ? '是' : '否'}；證據 ${jsonPath}`;

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
        '--detail', `CDP 捲動 ${finalData.scrolls} 次，共保留 ${postCount} 篇貼文`
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

import { fileURLToPath } from 'node:url';

const isMainModule = process.argv[1] && fileURLToPath(import.meta.url) === path.resolve(process.argv[1]);
if (isMainModule) {
  main().catch(err => {
    console.error('執行失敗：', err);
    process.exit(1);
  });
}

