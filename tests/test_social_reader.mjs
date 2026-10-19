import test from 'node:test';
import assert from 'node:assert/strict';
import {
  determineStatus,
  utcToTaipeiIso,
  extractFacebookTimeText,
  parseFacebookTime,
  isAuthorPost,
  normalizePostUrl,
  calculateMinMaxTimes,
  isFacebookLoginWall,
  isSeeMoreButton
} from '../scripts/social_reader.mjs';

// --- 原有 5 項保留 ---

test('0 篇貼文判定為 failed', () => {
  const status = determineStatus([], false);
  assert.equal(status.state, 'failed');
  assert.equal(status.media, 'unread');
});

test('登入牆且 0 篇判定為 failed', () => {
  const status = determineStatus([], true);
  assert.equal(status.state, 'failed');
  assert.equal(status.media, 'unread');
});

test('有貼文判定為 partial 且 media=unread（永遠不判 complete）', () => {
  const posts = [{ text: '演出公告', url: 'https://threads.net/@user/post/123' }];
  const status = determineStatus(posts, false);
  assert.equal(status.state, 'partial');
  assert.equal(status.media, 'unread');
});

test('UTC 時間換算為 Asia/Taipei (+08:00)', () => {
  const utc = '2026-09-26T06:32:03.000Z';
  const taipei = utcToTaipeiIso(utc);
  assert.equal(taipei, '2026-09-26T14:32:03+08:00');
});

test('Facebook timeText 原樣保留', () => {
  assert.equal(extractFacebookTimeText('3天'), '3天');
  assert.equal(extractFacebookTimeText('10月15日'), '10月15日');
  assert.equal(extractFacebookTimeText('昨天 下午3:20'), '昨天 下午3:20');
});

// --- 008 新增測試 ---

test('作者過濾：/@other/post/x 被排除，/@The_Rin.lpm/post/y 對 handle the_rin.lpm 保留', () => {
  assert.equal(isAuthorPost('https://www.threads.com/@other/post/x', 'the_rin.lpm'), false);
  assert.equal(isAuthorPost('https://www.threads.com/@The_Rin.lpm/post/y', 'the_rin.lpm'), true);
  assert.equal(isAuthorPost('https://www.threads.com/@someone/post/z', '1013.yr_'), false);
  assert.equal(isAuthorPost('https://www.threads.com/@1013.yr_/post/123', '1013.yr_'), true);
});

test('網址正規化：去掉參數；帶 comment_id 的被略過', () => {
  const cleanUrl = normalizePostUrl('https://www.facebook.com/lanyang.opera/posts/pfbid123?mibextid=123');
  assert.equal(cleanUrl, 'https://www.facebook.com/lanyang.opera/posts/pfbid123');

  const commentUrl = normalizePostUrl('https://www.facebook.com/lanyang.opera/posts/pfbid123?comment_id=999');
  assert.equal(commentUrl, null);

  const cleanThreads = normalizePostUrl('https://www.threads.com/@user/post/abc?x=1&y=2');
  assert.equal(cleanThreads, 'https://www.threads.com/@user/post/abc');
});

test('parseFacebookTime：7 種格式各一例 + 1 種無法辨識格式', () => {
  const base = '2026-10-19T14:00:00+08:00';

  // 1. 分鐘
  assert.equal(parseFacebookTime('17分鐘', base), '2026-10-19T13:43:00+08:00');
  // 2. 小時
  assert.equal(parseFacebookTime('2小時', base), '2026-10-19T12:00:00+08:00');
  // 3. 天
  assert.equal(parseFacebookTime('3天', base), '2026-10-16T14:00:00+08:00');
  // 4. 週
  assert.equal(parseFacebookTime('3週', base), '2026-09-28T14:00:00+08:00');
  // 5. 昨天
  assert.equal(parseFacebookTime('昨天 下午3:20', base), '2026-10-18T15:20:00+08:00');
  // 6. 月日
  assert.equal(parseFacebookTime('10月15日', base), '2026-10-15T12:00:00+08:00');
  // 7. 完整日期
  assert.equal(parseFacebookTime('2026年9月22日 星期二上午12:26', base), '2026-09-22T00:26:00+08:00');
  // 8. 無法辨識
  assert.equal(parseFacebookTime('剛剛好', base), null);
});

test('最舊與最新：輸入順序打亂時，結果仍然正確', () => {
  const posts = [
    { datetime: '2026-10-18T10:00:00+08:00' },
    { datetime: '2026-10-12T10:00:00+08:00' },
    { datetime: '2026-10-19T10:00:00+08:00' },
    { datetime: '2026-10-15T10:00:00+08:00' }
  ];
  const { oldestPostAt, newestPostAt } = calculateMinMaxTimes(posts);
  assert.equal(oldestPostAt, '2026-10-12T10:00:00+08:00');
  assert.equal(newestPostAt, '2026-10-19T10:00:00+08:00');

  // 若全部沒有時間
  const noTimes = [{ datetime: null }, { datetime: null }];
  const resNo = calculateMinMaxTimes(noTimes);
  assert.equal(resNo.oldestPostAt, null);
  assert.equal(resNo.newestPostAt, null);
});

// --- 009 新增測試 ---

test('登入牆新判定：無 story_message 且有登入表單/網址才算登入牆', () => {
  // 有貼文時，就算網頁內有登入按鈕也不算登入牆
  assert.equal(isFacebookLoginWall({ storyMessageCount: 3, hasEmailInput: true, hasLoginForm: true, isLoginUrl: false }), false);

  // 無貼文且有 email input -> true
  assert.equal(isFacebookLoginWall({ storyMessageCount: 0, hasEmailInput: true, hasLoginForm: false, isLoginUrl: false }), true);

  // 無貼文且網址含 /login -> true
  assert.equal(isFacebookLoginWall({ storyMessageCount: 0, hasEmailInput: false, hasLoginForm: false, isLoginUrl: true }), true);

  // 無貼文且無登入欄位/網址 -> false（僅是未發文或未載入，非登入牆）
  assert.equal(isFacebookLoginWall({ storyMessageCount: 0, hasEmailInput: false, hasLoginForm: false, isLoginUrl: false }), false);
});

test('查看更多按鈕文字判定：文字去除空白後完全等於指定關鍵字', () => {
  assert.equal(isSeeMoreButton('查看更多'), true);
  assert.equal(isSeeMoreButton(' 顯示更多 '), true);
  assert.equal(isSeeMoreButton('See more'), true);
  assert.equal(isSeeMoreButton('查看更多留言'), false);
  assert.equal(isSeeMoreButton('回覆'), false);
  assert.equal(isSeeMoreButton(''), false);
});
