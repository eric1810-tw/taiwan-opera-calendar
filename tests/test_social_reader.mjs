import test from 'node:test';
import assert from 'node:assert/strict';
import { determineStatus, utcToTaipeiIso, extractFacebookTimeText } from '../scripts/social_reader.mjs';

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
