# 巡檢報告 2026-11-26_0311（patrol-v2，正式）

## 結論

| 項目 | 結果 |
| --- | --- |
| 執行 | 開始 2026-11-26T03:11:34+08:00；結果 進行中；步驟 preflight:done、collect:done、pack:done、judge:done、check:done、verify:done、review:skipped、apply:done、publish:done、report:running |
| 來源 | 21 個：完整 5、部分 16、失敗 0、未讀 0 |
| 資料 | 送判讀 59 篇／圖 3 張；變更提案 0、確認一致 8、送查證 9（成立 0、與卡相同 2、查無佐證不收 7）、退回 0、漏處置 0；已過期不收 12、遠期暫存 31 |
| 寫入 | 寫入 0、add_card 拒絕 0、審查未通過 0 |
| 發布 | verified；SHA 175066b94b92364f64291c2c7483e0830ce943e4；Actions 45685568308 |

## 模型與用量

| 角色 | 模型 | 依據 |
| --- | --- | --- |
| main | claude-sonnet-5-5 | get_session self：effort=medium |
| judge | sonnet | Agent 工具 model 參數；effort=medium |
| verify | opus | Agent 工具 model 參數；effort=medium |

- 判讀批次 3；送出貼文 59 篇、圖片 3 張、正文約 10554 字
- 略過（已判讀未變動）57 篇；窗口外 80 篇
- 第二次審查：無（0 項）

## 來源

| 來源 | 狀態 | 範圍 | 說明 |
| --- | --- | --- | --- |
| threads:joe_huang_k_w | 部分 | 首屏 4 篇、累積 16 篇；最新 2026-11-23T00:01:53+08:00、最舊 2026-11-07T16:49:05+08:00；捲動 1 次、停止原因 reached-window；圖片下載 24 張 | 不變式通過；證據 /Users/eric/aiwork/taiwan-opera-calendar/patrol_evidence/2026-11-26_0311/threads_joe_huang… |
| threads:h.akito_1996 | 部分 | 首屏 8 篇、累積 8 篇；最新 2026-11-25T19:15:12+08:00、最舊 2026-09-27T00:04:33+08:00；捲動 3 次、停止原因 no-new-after-3；圖片下載 16 張 | 不變式通過；證據 /Users/eric/aiwork/taiwan-opera-calendar/patrol_evidence/2026-11-26_0311/threads_h.akito_1… |
| threads:the_rin.lpm | 部分 | 首屏 5 篇、累積 5 篇；最新 2026-11-25T15:16:09+08:00、最舊 2026-10-01T22:31:26+08:00；捲動 3 次、停止原因 no-new-after-3；圖片下載 6 張 | 不變式通過；證據 /Users/eric/aiwork/taiwan-opera-calendar/patrol_evidence/2026-11-26_0311/threads_the_rin.l… |
| threads:xuefeng_lu_ | 完整 | 7 天窗口讀完（停止原因 reached-window）；窗口內 2 篇皆有處置；圖片 1 張皆已判讀 | 不變式通過、逐篇處置完成 |
| threads:yuzhongluo | 部分 | 首屏 4 篇、累積 4 篇；最新 2026-11-26T00:24:41+08:00、最舊 2026-11-24T02:33:53+08:00；捲動 3 次、停止原因 no-new-after-3；圖片下載 5 張 | 不變式通過；證據 /Users/eric/aiwork/taiwan-opera-calendar/patrol_evidence/2026-11-26_0311/threads_yuzhonglu… |
| threads:taiwaneseopera168 | 部分 | 首屏 4 篇、累積 4 篇；最新 2026-11-25T20:00:44+08:00、最舊 2026-08-16T02:33:12+08:00；捲動 3 次、停止原因 no-new-after-3；圖片下載 2 張 | 不變式通過；證據 /Users/eric/aiwork/taiwan-opera-calendar/patrol_evidence/2026-11-26_0311/threads_taiwanese… |
| threads:jing__1017 | 部分 | 首屏 7 篇、累積 7 篇；最新 2026-11-25T22:52:09+08:00、最舊 2026-10-28T19:50:21+08:00；捲動 3 次、停止原因 no-new-after-3；圖片下載 8 張 | 不變式通過；證據 /Users/eric/aiwork/taiwan-opera-calendar/patrol_evidence/2026-11-26_0311/threads_jing__101… |
| threads:hilang.on.tour | 完整 | 7 天窗口讀完（停止原因 reached-window）；窗口內 0 篇皆有處置；圖片 0 張皆已判讀 | 不變式通過、逐篇處置完成 |
| threads:yolin1991 | 部分 | 首屏 5 篇、累積 5 篇；最新 2026-11-25T15:39:20+08:00、最舊 2026-11-23T10:52:34+08:00；捲動 3 次、停止原因 no-new-after-3；圖片下載 5 張 | 不變式通過；證據 /Users/eric/aiwork/taiwan-opera-calendar/patrol_evidence/2026-11-26_0311/threads_yolin1991… |
| threads:yilan_taiwan | 部分 | 首屏 4 篇、累積 4 篇；最新 2026-11-25T23:54:46+08:00、最舊 2026-11-20T16:14:20+08:00；捲動 3 次、停止原因 no-new-after-3；圖片下載 6 張 | 不變式通過；證據 /Users/eric/aiwork/taiwan-opera-calendar/patrol_evidence/2026-11-26_0311/threads_yilan_tai… |
| facebook:sunhope.fans | 部分 | 首屏 2 篇、累積 9 篇；最新 2026-11-24T03:13:01+08:00、最舊 2026-11-06T01:22:00+08:00；捲動 1 次、停止原因 reached-window；圖片下載 16 張 | 不變式通過；證據 /Users/eric/aiwork/taiwan-opera-calendar/patrol_evidence/2026-11-26_0311/facebook_sunhope.… |
| facebook:HsiaoHsiYuan1913 | 部分 | 首屏 3 篇、累積 11 篇；最新 2026-05-07T12:00:00+08:00、最舊 2026-05-07T12:00:00+08:00；捲動 1 次、停止原因 reached-window；圖片下載 18 張 | 不變式通過；證據 /Users/eric/aiwork/taiwan-opera-calendar/patrol_evidence/2026-11-26_0311/facebook_HsiaoHsi… |
| facebook:100063868113954 | 部分 | 首屏 4 篇、累積 14 篇；最新 2026-11-25T03:13:22+08:00、最舊 2026-11-11T07:29:00+08:00；捲動 2 次、停止原因 reached-window；圖片下載 17 張 | 不變式通過；證據 /Users/eric/aiwork/taiwan-opera-calendar/patrol_evidence/2026-11-26_0311/facebook_10006386… |
| facebook:MingHuaYuanTianTaiwaneseOpera | 部分 | 首屏 3 篇、累積 12 篇；最新 2026-11-24T03:13:35+08:00、最舊 2026-10-09T12:00:00+08:00；捲動 1 次、停止原因 reached-window；圖片下載 32 張 | 不變式通過；證據 /Users/eric/aiwork/taiwan-opera-calendar/patrol_evidence/2026-11-26_0311/facebook_MingHuaY… |
| facebook:61574134933376 | 部分 | 首屏 2 篇、累積 10 篇；最新 2026-11-23T03:13:45+08:00、最舊 2026-10-14T12:00:00+08:00；捲動 1 次、停止原因 reached-window；圖片下載 21 張 | 不變式通過；證據 /Users/eric/aiwork/taiwan-opera-calendar/patrol_evidence/2026-11-26_0311/facebook_61574134… |
| facebook:mhysun | 部分 | 首屏 3 篇、累積 11 篇；最新 2026-11-23T03:13:56+08:00、最舊 2026-10-31T23:10:00+08:00；捲動 1 次、停止原因 reached-window；圖片下載 50 張 | 不變式通過；證據 /Users/eric/aiwork/taiwan-opera-calendar/patrol_evidence/2026-11-26_0311/facebook_mhysun.j… |
| facebook:61594936681482 | 完整 | 7 天窗口讀完（停止原因 reached-window）；窗口內 0 篇皆有處置；圖片 0 張皆已判讀 | 不變式通過、逐篇處置完成 |
| facebook:lanyang.opera | 部分 | 首屏 3 篇、累積 11 篇；最新 2026-11-24T03:14:16+08:00、最舊 2026-09-22T12:00:00+08:00；捲動 1 次、停止原因 reached-window；圖片下載 15 張 | 不變式通過；證據 /Users/eric/aiwork/taiwan-opera-calendar/patrol_evidence/2026-11-26_0311/facebook_lanyang.… |
| facebook:Taichungpuppettheater | 完整 | 7 天窗口讀完（停止原因 reached-window）；窗口內 1 篇皆有處置；圖片 5 張皆已判讀 | 不變式通過、逐篇處置完成 |
| culture | 部分 | total 503、fetchedAt 2026-11-22T10:46:46+08:00、戲曲紀錄 9 筆 | moc_records 已 88 小時未更新 |
| issues | 完整 | 3 筆皆有處置 | 逐筆處置完成 |

- OPENTIX：sitemap 810 個活動、本輪有變 624、抓取 250、戲曲相關且未過期 30、延後 374、錯誤 0

## 遠期場次（超過 120 天，進入 120 天內自動重驗）

| 貼文 | 內容 |
| --- | --- |
| https://www.facebook.com/photo/?fbid=1560228489482771 | 明華園天字戲劇團｜《重返：愛河戀夢》｜臺灣戲曲中心 大表演廳｜2027-06-05、2027-06-06 |
| https://www.facebook.com/MingHuaYuanTianTaiwaneseOpera/reels_tab | 明華園天字戲劇團｜《重返：愛河戀夢》｜臺灣戲曲中心 大表演廳｜2027-06-05、2027-06-06 |
| https://www.threads.com/@taiwaneseopera168/post/DfWAAt6CT5a | 烏貓戲出｜《白賊七》｜高雄中山堂劇場(高雄市左營區實踐路71號)｜2027-04-17、2027-04-18 |
| https://www.threads.com/@taiwaneseopera168/post/DfWAAt6CT5a | 薪傳歌仔戲劇團｜《封神榜．文王食子》｜高雄中山堂劇場(高雄市左營區實踐路71號)｜2027-04-24、2027-04-25 |
| https://www.threads.com/@jing__1017/post/DfzIPO8E6F0 | 烏貓戲出｜《白賊七》｜高雄中山堂劇場｜2027-04-17、2027-04-18 |
| https://www.threads.com/@jing__1017/post/DfzIPO8E6F0 | 薪傳歌仔戲劇團｜《封神榜·文王食子》｜高雄中山堂劇場｜2027-04-24、2027-04-25 |
| https://www.threads.com/@taiwaneseopera168/post/Df1HM9wEdDa | 烏貓戲出｜《白賊七》｜高雄中山堂劇場｜2027-04-17、2027-04-18 |
| https://www.threads.com/@taiwaneseopera168/post/Df1HM9wEdDa | 薪傳歌仔戲劇團｜《封神榜·文王食子》｜高雄中山堂劇場｜2027-04-24、2027-04-25 |
| https://www.threads.com/@yuzhongluo/post/DgGCMHkEl8q | 薪傳歌仔戲劇團｜《陳世美-反奸》開鑼式｜保安宮庭園（台北市大同區哈密街61號）｜2027-04-11 |
| https://www.threads.com/@yuzhongluo/post/DgGCMHkEl8q | 春明歌劇團｜《五毒亂唐-大聖降魔》｜保安宮庭園（台北市大同區哈密街61號）｜2027-04-12 |
| https://www.threads.com/@yuzhongluo/post/DgGCMHkEl8q | 羅裕誴歌劇團｜《滄海神醫》｜保安宮庭園（台北市大同區哈密街61號）｜2027-04-13 |
| https://www.threads.com/@yuzhongluo/post/DgGCMHkEl8q | 秀琴歌劇團｜《林投姐》｜保安宮庭園（台北市大同區哈密街61號）｜2027-04-14 |
| https://www.threads.com/@yuzhongluo/post/DgGCMHkEl8q | 秀琴歌劇團｜《盤絲洞》｜保安宮庭園（台北市大同區哈密街61號）｜2027-04-15 |
| https://www.threads.com/@yuzhongluo/post/DgGCMHkEl8q | 孫凱琳歌劇團｜恨鎖天倫夢｜保安宮庭園（台北市大同區哈密街61號）｜2027-04-16 |
| https://www.threads.com/@yuzhongluo/post/DgGCMHkEl8q | 孫凱琳歌劇團｜情渡千年｜保安宮庭園（台北市大同區哈密街61號）｜2027-04-17 |
| https://www.threads.com/@yuzhongluo/post/DgGCMHkEl8q | 民安歌劇團｜包公審烏盆｜保安宮庭園（台北市大同區哈密街61號）｜2027-04-18 |
| https://www.threads.com/@yuzhongluo/post/DgGCMHkEl8q | 鴻明歌劇團｜一文錢｜保安宮庭園（台北市大同區哈密街61號）｜2027-04-19 |
| https://www.threads.com/@yuzhongluo/post/DgGCMHkEl8q | 國立臺灣戲曲學院歌仔戲學系高職部｜《魚美人》｜保安宮庭園（台北市大同區哈密街61號）｜2027-04-21 |
| https://www.threads.com/@yuzhongluo/post/DgGCMHkEl8q | 國立臺灣戲曲學院歌仔戲學系學院部｜《鐵面情》｜保安宮庭園（台北市大同區哈密街61號）｜2027-04-22 |
| https://www.threads.com/@yuzhongluo/post/DgGCMHkEl8q | 小金枝歌劇團｜一念恩仇｜保安宮庭園（台北市大同區哈密街61號）｜2027-04-23 |
| https://www.threads.com/@yuzhongluo/post/DgGCMHkEl8q | 唐美雲歌仔戲團青年團｜哪吒傳｜保安宮庭園（台北市大同區哈密街61號）｜2027-04-24 |
| https://www.threads.com/@yuzhongluo/post/DgGCMHkEl8q | 明華園玄字戲劇團｜三打白骨精｜保安宮庭園（台北市大同區哈密街61號）｜2027-04-26 |
| https://www.threads.com/@yuzhongluo/post/DgGCMHkEl8q | 蘭陽戲劇團｜福氣臨門｜保安宮庭園（台北市大同區哈密街61號）｜2027-04-28 |
| https://www.threads.com/@yuzhongluo/post/DgGCMHkEl8q | 保安宮杏壇歌仔戲社｜宋宮秘史｜保安宮庭園（台北市大同區哈密街61號）｜2027-04-29 |
| https://www.threads.com/@yuzhongluo/post/DgGCMHkEl8q | 臺北市永樂國小歌仔戲劇團｜義女情｜保安宮庭園（台北市大同區哈密街61號）｜2027-04-30 |
| https://www.threads.com/@yuzhongluo/post/DgGCMHkEl8q | 文惜歌仔戲劇團｜《龍鳳餅》｜保安宮庭園（台北市大同區哈密街61號）｜2027-05-01 |
| https://www.threads.com/@yuzhongluo/post/DgGCMHkEl8q | 陳麗香歌仔戲團｜雙遊庵｜保安宮庭園（台北市大同區哈密街61號）｜2027-05-02 |
| https://www.threads.com/@yuzhongluo/post/DgGCMHkEl8q | 一心戲劇團｜《刺客列傳魚腸劍》｜保安宮庭園（台北市大同區哈密街61號）｜2027-05-03 |
| https://www.threads.com/@yuzhongluo/post/DgGCMHkEl8q | 李靜芳歌仔戲團｜穆桂英破洪州(祭祀公業吳家記酬神戲)｜保安宮庭園（台北市大同區哈密街61號）｜2027-05-04 |
| https://www.threads.com/@yuzhongluo/post/DgGCBBfD3VQ | 羅裕誴歌劇團｜《滄海神醫》｜保安宮庭園（台北市大同區哈密街61號）｜2027-04-13 |
| https://www.threads.com/@yuzhongluo/post/DgGCBBfD3VQ | 文惜歌仔戲劇團｜《龍鳳餅》｜保安宮庭園（台北市大同區哈密街61號）｜2027-05-01 |

## 紀錄檔

- 本輪狀態：/Users/eric/aiwork/taiwan-opera-calendar/patrol_state/runs/2026-11-26_0311/state.json
- 巡檢紀錄：patrol_runs/2026-11-26_0311.json（/Users/eric/aiwork/taiwan-opera-calendar）
- 證據：patrol_evidence/2026-11-26_0311/
- 產生時間：2026-11-26T03:29:41+08:00
