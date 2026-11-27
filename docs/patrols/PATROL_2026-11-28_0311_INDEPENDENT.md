# 巡檢報告 2026-11-28_0311（patrol-v2，正式）

## 結論

| 項目 | 結果 |
| --- | --- |
| 執行 | 開始 2026-11-28T03:11:13+08:00；結果 進行中；步驟 preflight:done、collect:done、pack:done、judge:done、check:done、verify:done、review:done、apply:done、publish:done、report:running |
| 來源 | 21 個：完整 7、部分 14、失敗 0、未讀 0 |
| 資料 | 送判讀 67 篇／圖 14 張；變更提案 3、確認一致 6、送查證 9（成立 1、與卡相同 0、查無佐證不收 8）、退回 0、漏處置 0；已過期不收 10、遠期暫存 31 |
| 寫入 | 寫入 0、add_card 拒絕 2、審查未通過 1 |
| 發布 | verified；SHA bc078eb625733001f5d25ebcec2424da704b9e49；Actions 46056846823 |

## 模型與用量

| 角色 | 模型 | 依據 |
| --- | --- | --- |
| main | claude-sonnet-5-5 | get_session self：effort=medium |
| judge | sonnet | Agent 工具 model 參數；effort=medium |
| verify | opus | Agent 工具 model 參數；effort=medium |
| review | opus | Agent 工具 model 參數；effort=medium |

- 判讀批次 3；送出貼文 67 篇、圖片 14 張、正文約 15224 字
- 略過（已判讀未變動）52 篇；窗口外 83 篇
- 第二次審查：有（3 項）

## 來源

| 來源 | 狀態 | 範圍 | 說明 |
| --- | --- | --- | --- |
| threads:joe_huang_k_w | 完整 | 7 天窗口讀完（停止原因 reached-window）；窗口內 5 篇皆有處置；圖片 4 張皆已判讀 | 不變式通過、逐篇處置完成 |
| threads:h.akito_1996 | 部分 | 首屏 8 篇、累積 8 篇；最新 2026-11-25T19:15:12+08:00、最舊 2026-09-27T00:04:33+08:00；捲動 3 次、停止原因 no-new-after-3；圖片下載 16 張 | 不變式通過；證據 /Users/eric/aiwork/taiwan-opera-calendar/patrol_evidence/2026-11-28_0311/threads_h.akito_1… |
| threads:the_rin.lpm | 部分 | 首屏 5 篇、累積 5 篇；最新 2026-11-26T18:08:05+08:00、最舊 2026-10-01T22:31:26+08:00；捲動 3 次、停止原因 no-new-after-3；圖片下載 6 張 | 不變式通過；證據 /Users/eric/aiwork/taiwan-opera-calendar/patrol_evidence/2026-11-28_0311/threads_the_rin.l… |
| threads:xuefeng_lu_ | 完整 | 7 天窗口讀完（停止原因 reached-window）；窗口內 3 篇皆有處置；圖片 0 張皆已判讀 | 不變式通過、逐篇處置完成 |
| threads:yuzhongluo | 部分 | 首屏 4 篇、累積 4 篇；最新 2026-11-28T02:21:22+08:00、最舊 2026-11-26T13:46:33+08:00；捲動 3 次、停止原因 no-new-after-3；圖片下載 18 張 | 不變式通過；證據 /Users/eric/aiwork/taiwan-opera-calendar/patrol_evidence/2026-11-28_0311/threads_yuzhonglu… |
| threads:taiwaneseopera168 | 部分 | 首屏 8 篇、累積 8 篇；最新 2026-11-27T18:17:02+08:00、最舊 2026-08-16T02:33:12+08:00；捲動 3 次、停止原因 no-new-after-3；圖片下載 24 張 | 不變式通過；證據 /Users/eric/aiwork/taiwan-opera-calendar/patrol_evidence/2026-11-28_0311/threads_taiwanese… |
| threads:jing__1017 | 部分 | 首屏 8 篇、累積 8 篇；最新 2026-11-27T20:04:52+08:00、最舊 2026-10-28T19:50:21+08:00；捲動 3 次、停止原因 no-new-after-3；圖片下載 11 張 | 不變式通過；證據 /Users/eric/aiwork/taiwan-opera-calendar/patrol_evidence/2026-11-28_0311/threads_jing__101… |
| threads:hilang.on.tour | 完整 | 7 天窗口讀完（停止原因 reached-window）；窗口內 0 篇皆有處置；圖片 0 張皆已判讀 | 不變式通過、逐篇處置完成 |
| threads:yolin1991 | 部分 | 首屏 5 篇、累積 5 篇；最新 2026-11-27T13:55:30+08:00、最舊 2026-11-25T12:29:01+08:00；捲動 3 次、停止原因 no-new-after-3；圖片下載 7 張 | 不變式通過；證據 /Users/eric/aiwork/taiwan-opera-calendar/patrol_evidence/2026-11-28_0311/threads_yolin1991… |
| threads:yilan_taiwan | 部分 | 首屏 4 篇、累積 4 篇；最新 2026-11-25T23:54:46+08:00、最舊 2026-11-20T16:14:20+08:00；捲動 1 次、停止原因 reached-window；圖片下載 6 張 | 不變式通過；證據 /Users/eric/aiwork/taiwan-opera-calendar/patrol_evidence/2026-11-28_0311/threads_yilan_tai… |
| facebook:sunhope.fans | 部分 | 首屏 3 篇、累積 9 篇；最新 2026-11-27T03:12:39+08:00、最舊 2026-11-06T23:40:00+08:00；捲動 1 次、停止原因 reached-window；圖片下載 15 張 | 不變式通過；證據 /Users/eric/aiwork/taiwan-opera-calendar/patrol_evidence/2026-11-28_0311/facebook_sunhope.… |
| facebook:HsiaoHsiYuan1913 | 部分 | 首屏 3 篇、累積 11 篇；最新 2026-05-07T12:00:00+08:00、最舊 2026-05-07T12:00:00+08:00；捲動 1 次、停止原因 reached-window；圖片下載 18 張 | 不變式通過；證據 /Users/eric/aiwork/taiwan-opera-calendar/patrol_evidence/2026-11-28_0311/facebook_HsiaoHsi… |
| facebook:100063868113954 | 部分 | 首屏 3 篇、累積 13 篇；最新 2026-11-26T03:13:00+08:00、最舊 2026-11-18T13:57:00+08:00；捲動 1 次、停止原因 reached-window；圖片下載 16 張 | 不變式通過；證據 /Users/eric/aiwork/taiwan-opera-calendar/patrol_evidence/2026-11-28_0311/facebook_10006386… |
| facebook:MingHuaYuanTianTaiwaneseOpera | 部分 | 首屏 3 篇、累積 12 篇；最新 2026-11-26T03:13:10+08:00、最舊 2026-10-11T12:00:00+08:00；捲動 1 次、停止原因 reached-window；圖片下載 30 張 | 不變式通過；證據 /Users/eric/aiwork/taiwan-opera-calendar/patrol_evidence/2026-11-28_0311/facebook_MingHuaY… |
| facebook:61574134933376 | 部分 | 首屏 3 篇、累積 10 篇；最新 2026-11-27T03:13:21+08:00、最舊 2026-10-19T12:00:00+08:00；捲動 1 次、停止原因 reached-window；圖片下載 17 張 | 不變式通過；證據 /Users/eric/aiwork/taiwan-opera-calendar/patrol_evidence/2026-11-28_0311/facebook_61574134… |
| facebook:mhysun | 部分 | 首屏 3 篇、累積 11 篇；最新 2026-11-27T03:13:32+08:00、最舊 2026-11-06T10:07:00+08:00；捲動 1 次、停止原因 reached-window；圖片下載 50 張 | 不變式通過；證據 /Users/eric/aiwork/taiwan-opera-calendar/patrol_evidence/2026-11-28_0311/facebook_mhysun.j… |
| facebook:61594936681482 | 完整 | 7 天窗口讀完（停止原因 reached-window）；窗口內 0 篇皆有處置；圖片 0 張皆已判讀 | 不變式通過、逐篇處置完成 |
| facebook:lanyang.opera | 部分 | 首屏 3 篇、累積 11 篇；最新 2026-11-24T03:13:53+08:00、最舊 2026-09-22T12:00:00+08:00；捲動 1 次、停止原因 reached-window；圖片下載 15 張 | 不變式通過；證據 /Users/eric/aiwork/taiwan-opera-calendar/patrol_evidence/2026-11-28_0311/facebook_lanyang.… |
| facebook:Taichungpuppettheater | 完整 | 7 天窗口讀完（停止原因 reached-window）；窗口內 0 篇皆有處置；圖片 0 張皆已判讀 | 不變式通過、逐篇處置完成 |
| culture | 完整 | 8 筆皆有處置 | 逐筆處置完成 |
| issues | 完整 | 3 筆皆有處置 | 逐筆處置完成 |

- OPENTIX：sitemap 819 個活動、本輪有變 634、抓取 250、戲曲相關且未過期 32、延後 384、錯誤 0

## 卡片變更

| 編號 | 動作 | 來源 | 內容 | 差異 | 審查 | 寫入 |
| --- | --- | --- | --- | --- | --- | --- |
| chg-001 | add | https://www.threads.com/@taiwaneseopera168/post/DgO4Q7VEfN8 | 新和興總團｜《秦英掛帥》｜傳藝高雄園區 中山堂劇場戶外陽光草坪｜2026-11-28 正戲 19:00 |  | approve：source.text 明載「新和興總團《秦英掛帥》 11/28(六)19:00 開演」「傳藝高雄園區 中山堂劇場戶外… | rejected artist-not-in-quote |
| chg-002 | add | https://www.facebook.com/MingHuaYuanTianTaiwaneseOpera/posts/pfbid04gqa3jQTw7TEzSgsRkBsx3F9fqLFJjwi8M2CnWvfHrUfg6HtVrd49y3F7g71gXo1l | 明華園天字戲劇團｜《一曲台灣情．歌聲傳戲韻》｜屏東縣立圖書館總館｜2026-11-29 其他 09:30 |  | approve：海報（2c54dd…）明確：《一曲台灣情．歌聲傳戲韻》明華園天字戲劇團 陳昭錦、11/29(日) 09:30-11:3… | rejected title-not-in-quote,duplicate |
| chg-003 | add（查證成立） | https://www.tw-yishin.com/%e6%bc%94%e5%87%ba%e6%96%b0%e8%a8%8a/2026%e4%b8%80%e5%bf%83%e6%88%b2%e5%8a%87%e5%9c%98%e3%80%8a%e9%96%bb%e7%8e%8b%e7%9a%84%e5%81%87%e6%9c%9f%e3%80%8b/（原貼文 https://www.opentix.life/event/2080109546140397568） | 一心戲劇團｜《閻王的假期》｜城市舞台｜2026-12-05 正戲 14:30、2026-12-06 正戲 14:30 |  | needs-check：日期、時間、地點、票價都對得上原文「演出時間：2026/12/05(六)14:30 2026/12/06(日)14:3… | held  |

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

- 本輪狀態：/Users/eric/aiwork/taiwan-opera-calendar/patrol_state/runs/2026-11-28_0311/state.json
- 巡檢紀錄：patrol_runs/2026-11-28_0311.json（/Users/eric/aiwork/taiwan-opera-calendar）
- 證據：patrol_evidence/2026-11-28_0311/
- 產生時間：2026-11-28T03:28:42+08:00
