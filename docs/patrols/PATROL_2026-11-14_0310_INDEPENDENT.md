# 巡檢報告 2026-11-14_0310（patrol-v2，正式）

## 結論

| 項目 | 結果 |
| --- | --- |
| 執行 | 開始 2026-11-14T03:10:52+08:00；結果 進行中；步驟 preflight:done、collect:done、pack:done、judge:done、check:done、verify:done、review:done、apply:done、publish:done、report:running |
| 來源 | 20 個：完整 5、部分 15、失敗 0、未讀 0 |
| 資料 | 送判讀 210 篇／圖 14 張；變更提案 1、確認一致 25、送查證 68（成立 1、與卡相同 7、查無佐證不收 62）、退回 0、漏處置 0；已過期不收 77、遠期暫存 5 |
| 寫入 | 寫入 0、add_card 拒絕 1、審查未通過 0 |
| 發布 | verified；SHA dbb8e75ab925592371ecae679999bd2856a6968d；Actions 43495297896 |

## 模型與用量

| 角色 | 模型 | 依據 |
| --- | --- | --- |
| main | claude-sonnet-5-5 | get_session self：effort=medium |
| judge | sonnet | Agent 工具 model 參數；effort=medium |
| verify | opus | Agent 工具 model 參數；effort=medium |
| review | opus | Agent 工具 model 參數；effort=medium |

- 判讀批次 9；送出貼文 210 篇、圖片 14 張、正文約 72121 字
- 略過（已判讀未變動）114 篇；窗口外 31 篇
- 第二次審查：有（1 項）

## 來源

| 來源 | 狀態 | 範圍 | 說明 |
| --- | --- | --- | --- |
| threads:joe_huang_k_w | 部分 | 首屏 5 篇、累積 11 篇；最新 2026-11-13T21:52:34+08:00、最舊 2026-11-05T18:00:50+08:00；捲動 2 次、停止原因 reached-window；圖片下載 14 張 | 不變式通過；證據 /Users/eric/aiwork/taiwan-opera-calendar/patrol_evidence/2026-11-14_0310/threads_joe_huang… |
| threads:h.akito_1996 | 完整 | 7 天窗口讀完（停止原因 reached-window）；窗口內 0 篇皆有處置；圖片 0 張皆已判讀 | 不變式通過、逐篇處置完成 |
| threads:the_rin.lpm | 部分 | 首屏 4 篇、累積 10 篇；最新 2026-11-12T19:18:17+08:00、最舊 2026-09-26T14:32:03+08:00；捲動 3 次、停止原因 reached-window；圖片下載 15 張 | 不變式通過；證據 /Users/eric/aiwork/taiwan-opera-calendar/patrol_evidence/2026-11-14_0310/threads_the_rin.l… |
| threads:xuefeng_lu_ | 完整 | 7 天窗口讀完（停止原因 reached-window）；窗口內 2 篇皆有處置；圖片 0 張皆已判讀 | 不變式通過、逐篇處置完成 |
| threads:yuzhongluo | 部分 | 首屏 4 篇、累積 22 篇；最新 2026-11-13T18:52:39+08:00、最舊 2026-11-06T20:36:15+08:00；捲動 8 次、停止原因 reached-window；圖片下載 23 張 | 不變式通過；證據 /Users/eric/aiwork/taiwan-opera-calendar/patrol_evidence/2026-11-14_0310/threads_yuzhonglu… |
| threads:taiwaneseopera168 | 部分 | 首屏 3 篇、累積 41 篇；最新 2026-11-13T22:17:16+08:00、最舊 2026-08-16T02:33:12+08:00；捲動 20 次、停止原因 reached-window；圖片下載 56 張 | 不變式通過；證據 /Users/eric/aiwork/taiwan-opera-calendar/patrol_evidence/2026-11-14_0310/threads_taiwanese… |
| threads:jing__1017 | 部分 | 首屏 5 篇、累積 16 篇；最新 2026-11-13T19:38:05+08:00、最舊 2026-10-28T19:50:21+08:00；捲動 6 次、停止原因 reached-window；圖片下載 31 張 | 不變式通過；證據 /Users/eric/aiwork/taiwan-opera-calendar/patrol_evidence/2026-11-14_0310/threads_jing__101… |
| threads:hilang.on.tour | 完整 | 7 天窗口讀完（停止原因 reached-window）；窗口內 0 篇皆有處置；圖片 0 張皆已判讀 | 不變式通過、逐篇處置完成 |
| threads:yolin1991 | 部分 | 首屏 4 篇、累積 8 篇；最新 2026-11-12T23:41:50+08:00、最舊 2026-11-05T16:28:03+08:00；捲動 2 次、停止原因 reached-window；圖片下載 8 張 | 不變式通過；證據 /Users/eric/aiwork/taiwan-opera-calendar/patrol_evidence/2026-11-14_0310/threads_yolin1991… |
| facebook:sunhope.fans | 部分 | 首屏 1 篇、累積 21 篇；最新 無、最舊 無；捲動 20 次、停止原因 max-scrolls；圖片下載 43 張 | 不變式通過；證據 /Users/eric/aiwork/taiwan-opera-calendar/patrol_evidence/2026-11-14_0310/facebook_sunhope.… |
| facebook:HsiaoHsiYuan1913 | 部分 | 首屏 1 篇、累積 24 篇；最新 無、最舊 無；捲動 20 次、停止原因 max-scrolls；圖片下載 50 張 | 不變式通過；證據 /Users/eric/aiwork/taiwan-opera-calendar/patrol_evidence/2026-11-14_0310/facebook_HsiaoHsi… |
| facebook:100063868113954 | 部分 | 首屏 1 篇、累積 22 篇；最新 無、最舊 無；捲動 20 次、停止原因 max-scrolls；圖片下載 51 張 | 不變式通過；證據 /Users/eric/aiwork/taiwan-opera-calendar/patrol_evidence/2026-11-14_0310/facebook_10006386… |
| facebook:MingHuaYuanTianTaiwaneseOpera | 部分 | 首屏 1 篇、累積 23 篇；最新 無、最舊 無；捲動 20 次、停止原因 max-scrolls；圖片下載 61 張 | 不變式通過；證據 /Users/eric/aiwork/taiwan-opera-calendar/patrol_evidence/2026-11-14_0310/facebook_MingHuaY… |
| facebook:61574134933376 | 部分 | 首屏 1 篇、累積 18 篇；最新 無、最舊 無；捲動 20 次、停止原因 max-scrolls；圖片下載 43 張 | 不變式通過；證據 /Users/eric/aiwork/taiwan-opera-calendar/patrol_evidence/2026-11-14_0310/facebook_61574134… |
| facebook:mhysun | 部分 | 首屏 1 篇、累積 20 篇；最新 無、最舊 無；捲動 20 次、停止原因 max-scrolls；圖片下載 92 張 | 不變式通過；證據 /Users/eric/aiwork/taiwan-opera-calendar/patrol_evidence/2026-11-14_0310/facebook_mhysun.j… |
| facebook:61594936681482 | 部分 | 首屏 1 篇、累積 7 篇；最新 無、最舊 無；捲動 7 次、停止原因 no-new-after-3；圖片下載 23 張 | 不變式通過；證據 /Users/eric/aiwork/taiwan-opera-calendar/patrol_evidence/2026-11-14_0310/facebook_61594936… |
| facebook:lanyang.opera | 部分 | 首屏 3 篇、累積 22 篇；最新 無、最舊 無；捲動 20 次、停止原因 max-scrolls；圖片下載 25 張 | 不變式通過；證據 /Users/eric/aiwork/taiwan-opera-calendar/patrol_evidence/2026-11-14_0310/facebook_lanyang.… |
| facebook:Taichungpuppettheater | 部分 | 首屏 1 篇、累積 25 篇；最新 無、最舊 無；捲動 20 次、停止原因 max-scrolls；圖片下載 42 張 | 不變式通過；證據 /Users/eric/aiwork/taiwan-opera-calendar/patrol_evidence/2026-11-14_0310/facebook_Taichung… |
| culture | 完整 | 9 筆皆有處置 | 逐筆處置完成 |
| issues | 完整 | 3 筆皆有處置 | 逐筆處置完成 |

- OPENTIX：sitemap 824 個活動、本輪有變 651、抓取 250、戲曲相關且未過期 36、延後 401、錯誤 0

## 卡片變更

| 編號 | 動作 | 來源 | 內容 | 差異 | 審查 | 寫入 |
| --- | --- | --- | --- | --- | --- | --- |
| chg-001 | add（查證成立） | https://www.ncfta.gov.tw/News_Content.aspx?n=5178&s=264641（原貼文 https://www.opentix.life/event/2090269380048343041） | 薪傳歌仔戲劇團｜《蒼原孤雁》（戲釀青春──2026駐團演訓計畫 育成聯合展演）｜臺灣戲曲中心小表演廳｜2026-11-14 正戲 14:30 |  | approve：日期／時間／地點／劇團／劇目皆出自 source.text 節目資訊段「演出地點：臺灣戲曲中心小表演廳 … 11/14… | rejected title-not-in-quote,badgeType-not-ticket |

## 遠期場次（超過 120 天，進入 120 天內自動重驗）

| 貼文 | 內容 |
| --- | --- |
| https://www.facebook.com/photo/?fbid=1560228489482771 | 明華園天字戲劇團｜《重返：愛河戀夢》｜臺灣戲曲中心 大表演廳｜2027-06-05、2027-06-06 |
| https://www.facebook.com/MingHuaYuanTianTaiwaneseOpera/reels_tab | 明華園天字戲劇團｜《重返：愛河戀夢》｜臺灣戲曲中心 大表演廳｜2027-06-05、2027-06-06 |
| https://www.threads.com/@taiwaneseopera168/post/DfWAAt6CT5a | 烏貓戲出｜《白賊七》｜高雄中山堂劇場(高雄市左營區實踐路71號)｜2027-04-17、2027-04-18 |
| https://www.threads.com/@taiwaneseopera168/post/DfWAAt6CT5a | 薪傳歌仔戲劇團｜《封神榜．文王食子》｜高雄中山堂劇場(高雄市左營區實踐路71號)｜2027-04-24、2027-04-25 |
| https://www.threads.com/@taiwaneseopera168/post/DfWAAt6CT5a | 燕玲戲劇團｜《韓信設窖安軍心》｜高雄中山堂劇場(高雄市左營區實踐路71號)｜2027-03-20、2027-03-21 |

## 紀錄檔

- 本輪狀態：/Users/eric/aiwork/taiwan-opera-calendar/patrol_state/runs/2026-11-14_0310/state.json
- 巡檢紀錄：patrol_runs/2026-11-14_0310.json（/Users/eric/aiwork/taiwan-opera-calendar）
- 證據：patrol_evidence/2026-11-14_0310/
- 產生時間：2026-11-14T03:46:44+08:00
