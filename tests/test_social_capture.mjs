import { test } from 'node:test';
import assert from 'node:assert/strict';
import { createServer } from 'node:http';
import { existsSync, mkdtempSync, readFileSync, rmSync } from 'node:fs';
import os from 'node:os';
import path from 'node:path';
import {
  checkInvariants,
  createAccumulator,
  decideStop,
  facebookKey,
  facebookPostId,
  resolveProfile,
  run,
  threadsPostCode,
} from '../scripts/patrol_v2/social_capture.mjs';

const EDGE = '/Applications/Microsoft Edge.app/Contents/MacOS/Microsoft Edge';

test('貼文碼與 FB 貼文 ID 擷取', () => {
  assert.equal(threadsPostCode('https://www.threads.com/@yuzhongluo/post/De1UV_Ikxkl'), 'De1UV_Ikxkl');
  assert.equal(facebookPostId('https://www.facebook.com/photo/?fbid=1650076190464636'), '1650076190464636');
  assert.equal(facebookPostId('https://www.facebook.com/x/posts/pfbid02nbH9JZ'), 'pfbid02nbH9JZ');
  assert.equal(facebookKey('h', 'https://www.facebook.com/photo/?fbid=123', '任意'), 'facebook:h:123');
  assert.match(facebookKey('h', '', '沒有網址的貼文'), /^facebook:h:[0-9a-f]{12}$/);
});

test('累積器：以 ID 去重、保留較長正文、合併圖片', () => {
  const acc = createAccumulator();
  assert.equal(acc.add([{ postKey: 'a', text: '短', images: ['1'] }], 0), 1);
  assert.equal(acc.add([{ postKey: 'a', text: '比較長的正文', images: ['2'] }, { postKey: 'b', text: 'x' }], 1), 1);
  const a = acc.values().find(p => p.postKey === 'a');
  assert.equal(a.text, '比較長的正文');
  assert.deepEqual(a.images, ['1', '2']);
  assert.equal(a.firstSeenRound, 0);
});

test('停止條件與停止原因', () => {
  const windowStartMs = Date.parse('2026-10-17T00:00:00+08:00');
  assert.equal(decideStop({ round: 1, maxScrolls: 20, noNewRounds: 0, lowestVisibleAt: '2026-10-16T10:00:00+08:00', windowStartMs }), 'reached-window');
  assert.equal(decideStop({ round: 5, maxScrolls: 20, noNewRounds: 3, lowestVisibleAt: null, windowStartMs }), 'no-new-after-3');
  assert.equal(decideStop({ round: 20, maxScrolls: 20, noNewRounds: 0, lowestVisibleAt: null, windowStartMs }), 'max-scrolls');
  assert.equal(decideStop({ round: 2, maxScrolls: 20, noNewRounds: 1, lowestVisibleAt: '2026-10-20T00:00:00+08:00', windowStartMs }), null);
});

test('不變式：已知貼文不在輸出 → known-post-missing（10/24 03:08 舊結果）', () => {
  // 舊讀取器 2026-10-24_0304 對 yuzhongluo 的實際輸出：9 篇，最新 10/19，沒有 10/23 兩篇
  const fixture = JSON.parse(readFileSync(new URL('./fixtures/patrol_v2/threads_yuzhongluo_2026-10-24_0304.json', import.meta.url)));
  const finalKeys = fixture.posts.map(p => p.postKey);
  const r = checkInvariants({
    finalKeys,
    firstScreenKeys: finalKeys.slice(0, 3),
    knownPosts: [{ postKey: 'threads:yuzhongluo:De1UV_Ikxkl', postedAt: '2026-10-23T18:14:03+08:00' }],
    windowStartMs: Date.parse('2026-10-17T03:08:00+08:00'),
    nowMs: Date.parse('2026-10-24T03:08:15+08:00'),
    loginWall: false,
  });
  assert.equal(r.ok, false);
  assert.deepEqual(r.missingKnown, ['threads:yuzhongluo:De1UV_Ikxkl']);
  assert.ok(r.problems.includes('known-post-missing'));
});

test('案例7：03:12 才發的貼文，03:08 讀取時不要求必須出現', () => {
  const r = checkInvariants({
    finalKeys: ['threads:yuzhongluo:De1UV_Ikxkl'],
    firstScreenKeys: ['threads:yuzhongluo:De1UV_Ikxkl'],
    knownPosts: [{ postKey: 'threads:yuzhongluo:De2R8XSkiWT', postedAt: '2026-10-24T03:12:18+08:00' }],
    windowStartMs: Date.parse('2026-10-17T03:08:00+08:00'),
    nowMs: Date.parse('2026-10-24T03:08:15+08:00'),
    loginWall: false,
  });
  assert.equal(r.ok, true);
});

test('已確認刪除的已知貼文不再要求', () => {
  const r = checkInvariants({
    finalKeys: ['a'], firstScreenKeys: ['a'],
    knownPosts: [{ postKey: 'threads:yuzhongluo:De2R8XSkiWT', postedAt: '2026-10-24T03:12:18+08:00', deletedConfirmedAt: '2026-10-24T23:50:00+08:00' }],
    windowStartMs: 0, nowMs: Date.parse('2026-10-25T03:00:00+08:00'), loginWall: false,
  });
  assert.equal(r.ok, true);
});

test('不變式：未登入卻首屏 0 篇 → first-screen-empty', () => {
  const r = checkInvariants({ finalKeys: [], firstScreenKeys: [], windowStartMs: 0, loginWall: false });
  assert.ok(r.problems.includes('first-screen-empty'));
});

test('測試設定檔不得是 ~/.patrol-edge 或非暫存目錄', () => {
  assert.throws(() => resolveProfile(path.join(os.homedir(), '.patrol-edge')));
  assert.throws(() => resolveProfile('/Users/eric/somewhere'));
  const tmp = mkdtempSync(path.join(os.tmpdir(), 'cap-'));
  assert.equal(resolveProfile(tmp), path.resolve(tmp));
  rmSync(tmp, { recursive: true, force: true });
});

// --- 動態列表回歸測試：模擬 Threads 捲動後移除上方節點 ---

const POSTS = (() => {
  const list = [
    { code: 'PINNEDold01', at: '2026-09-01T02:00:00Z', text: '置頂舊文' },
    { code: 'De2R8XSkiWT', at: '2026-10-23T19:12:18Z', text: '就在今天｜10/24（六）16:30 地點改在新營文化中心館內演出' },
    { code: 'De1UV_Ikxkl', at: '2026-10-23T10:14:03Z', text: '府城有神・人間有情 10/24（六）16:30 薪瀛舞台' },
  ];
  let t = Date.parse('2026-10-23T02:00:00Z');
  for (let i = 0; i < 30; i++) {
    t -= 10 * 3600 * 1000;
    list.push({ code: `Old${String(i).padStart(4, '0')}xx`, at: new Date(t).toISOString(), text: `舊貼文 ${i}` });
  }
  return list;
})();

function virtualPage() {
  const data = JSON.stringify(POSTS);
  return `<!doctype html><html><head><meta charset="utf-8"></head><body style="margin:0">
<div id="list" style="position:relative"></div>
<script>
const POSTS = ${data}; const H = 600;
const list = document.getElementById('list');
list.style.height = (POSTS.length * H) + 'px';
function render() {
  const top = window.scrollY - 1200, bottom = window.scrollY + window.innerHeight + 1200;
  list.innerHTML = '';
  POSTS.forEach((p, i) => {
    const y = i * H;
    if (y + H < top || y > bottom) return;   // 視窗外的節點不存在（被回收）
    const div = document.createElement('div');
    div.style.cssText = 'position:absolute;left:0;right:0;height:' + H + 'px;top:' + y + 'px';
    div.innerHTML = '<a href="/@yuzhongluo/post/' + p.code + '"><time datetime="' + p.at + '">t</time></a><p>' + p.text + '</p>';
    list.appendChild(div);
  });
}
setTimeout(render, 300);
window.addEventListener('scroll', render);
</script></body></html>`;
}

test('動態列表：新讀取器保留首屏的 De1UV_Ikxkl／De2R8XSkiWT（舊做法只讀最後畫面會漏）', { skip: !existsSync(EDGE) || process.env.SKIP_EDGE === '1', timeout: 180000 }, async () => {
  const server = createServer((req, res) => { res.writeHead(200, { 'content-type': 'text/html; charset=utf-8' }); res.end(virtualPage()); });
  await new Promise(r => server.listen(0, '127.0.0.1', r));
  const port = server.address().port;
  const profile = mkdtempSync(path.join(os.tmpdir(), 'patrol-capture-test-'));
  const out = mkdtempSync(path.join(os.tmpdir(), 'patrol-capture-out-'));
  try {
    const events = [];
    await run({
      sources: [{ key: 'threads:yuzhongluo', kind: 'threads', handle: 'yuzhongluo', url: `http://127.0.0.1:${port}/@yuzhongluo`,
        knownPosts: [{ postKey: 'threads:yuzhongluo:De1UV_Ikxkl', postedAt: '2026-10-23T18:14:03+08:00' }] }],
      outDir: out,
      testProfile: profile,
      opts: { nowMs: Date.parse('2026-10-24T05:00:00+08:00'), threadsWaitMs: 400, readySeconds: 10, retries: 0 },
      emit: e => events.push(e),
    });
    const result = JSON.parse(readFileSync(path.join(out, 'threads_yuzhongluo.json'), 'utf-8'));
    const keys = result.posts.map(p => p.postKey);
    assert.ok(keys.includes('threads:yuzhongluo:De1UV_Ikxkl'), '必須保留 De1UV_Ikxkl');
    assert.ok(keys.includes('threads:yuzhongluo:De2R8XSkiWT'), '必須保留 De2R8XSkiWT');
    assert.equal(result.invariants.ok, true, JSON.stringify(result.invariants));
    assert.equal(result.stopReason, 'reached-window');
    assert.ok(result.firstScreen.postKeys.includes('threads:yuzhongluo:De1UV_Ikxkl'));
    // 舊做法對照：捲到最後才讀 DOM，那時頁面上只剩視窗附近的節點，首屏貼文已不存在
    const lastScrollY = result.scrolls * 1200;
    const domAtEnd = POSTS.filter((p, i) => !(i * 600 + 600 < lastScrollY - 1200 || i * 600 > lastScrollY + 2000 + 1200)).map(p => p.code);
    assert.ok(!domAtEnd.includes('De1UV_Ikxkl'), '模擬頁面確實會回收首屏節點');
    const event = events.find(e => e.type === 'source');
    assert.equal(event.problems.length, 0);
  } finally {
    server.close();
    rmSync(profile, { recursive: true, force: true });
    rmSync(out, { recursive: true, force: true });
  }
});
