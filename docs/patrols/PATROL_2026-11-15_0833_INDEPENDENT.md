# 巡檢報告 2026-11-15_0833（patrol-v2，正式）

## 需要 Eric 決定

- 判讀有 1 篇沒有逐篇處置，已列待查（見報告）

## 結論

| 項目 | 結果 |
| --- | --- |
| 執行 | 開始 2026-11-15T08:33:40+08:00；結果 進行中；步驟 preflight:done、collect:done、pack:done、judge:done、check:done、verify:done、review:done、apply:done、publish:done、report:running |
| 來源 | 20 個：完整 4、部分 16、失敗 0、未讀 0 |
| 資料 | 送判讀 203 篇／圖 1 張；變更提案 13、確認一致 12、送查證 62（成立 2、與卡相同 7、查無佐證不收 53）、退回 0、漏處置 1；已過期不收 87、遠期暫存 5 |
| 寫入 | 寫入 0、add_card 拒絕 11、審查未通過 2 |
| 發布 | verified；SHA 816738eccd65e90d773c0fc4525bb49054432768；Actions 43661689653 |

## 模型與用量

| 角色 | 模型 | 依據 |
| --- | --- | --- |
| main | claude-sonnet-5-5 | get_session self：effort=medium |
| judge | sonnet | Agent 工具 model 參數；effort=medium |
| verify | opus | Agent 工具 model 參數；effort=medium |
| review | opus | Agent 工具 model 參數；effort=medium |

- 判讀批次 9；送出貼文 203 篇、圖片 1 張、正文約 69052 字
- 略過（已判讀未變動）116 篇；窗口外 27 篇
- 第二次審查：有（13 項）

## 來源

| 來源 | 狀態 | 範圍 | 說明 |
| --- | --- | --- | --- |
| threads:joe_huang_k_w | 部分 | 首屏 5 篇、累積 8 篇；最新 2026-11-13T21:52:34+08:00、最舊 2026-11-08T01:16:21+08:00；捲動 1 次、停止原因 reached-window；圖片下載 11 張 | 不變式通過；證據 /Users/eric/aiwork/taiwan-opera-calendar/patrol_evidence/2026-11-15_0833/threads_joe_huang… |
| threads:h.akito_1996 | 部分 | 首屏 4 篇、累積 7 篇；最新 2026-11-15T03:21:36+08:00、最舊 2026-09-27T00:04:33+08:00；捲動 1 次、停止原因 reached-window；圖片下載 5 張 | 不變式通過；證據 /Users/eric/aiwork/taiwan-opera-calendar/patrol_evidence/2026-11-15_0833/threads_h.akito_1… |
| threads:the_rin.lpm | 部分 | 首屏 3 篇、累積 8 篇；最新 2026-11-12T19:18:17+08:00、最舊 2026-09-26T14:32:03+08:00；捲動 2 次、停止原因 reached-window；圖片下載 13 張 | 不變式通過；證據 /Users/eric/aiwork/taiwan-opera-calendar/patrol_evidence/2026-11-15_0833/threads_the_rin.l… |
| threads:xuefeng_lu_ | 完整 | 7 天窗口讀完（停止原因 reached-window）；窗口內 2 篇皆有處置；圖片 0 張皆已判讀 | 不變式通過、逐篇處置完成 |
| threads:yuzhongluo | 部分 | 首屏 4 篇、累積 23 篇；最新 2026-11-14T18:50:52+08:00、最舊 2026-11-06T20:36:15+08:00；捲動 9 次、停止原因 reached-window；圖片下載 24 張 | 不變式通過；證據 /Users/eric/aiwork/taiwan-opera-calendar/patrol_evidence/2026-11-15_0833/threads_yuzhonglu… |
| threads:taiwaneseopera168 | 部分 | 首屏 4 篇、累積 38 篇；最新 2026-11-15T03:38:07+08:00、最舊 2026-08-16T02:33:12+08:00；捲動 20 次、停止原因 reached-window；圖片下載 52 張 | 不變式通過；證據 /Users/eric/aiwork/taiwan-opera-calendar/patrol_evidence/2026-11-15_0833/threads_taiwanese… |
| threads:jing__1017 | 部分 | 首屏 6 篇、累積 19 篇；最新 2026-11-15T01:40:16+08:00、最舊 2026-10-28T19:50:21+08:00；捲動 7 次、停止原因 reached-window；圖片下載 31 張 | 不變式通過；證據 /Users/eric/aiwork/taiwan-opera-calendar/patrol_evidence/2026-11-15_0833/threads_jing__101… |
| threads:hilang.on.tour | 完整 | 7 天窗口讀完（停止原因 reached-window）；窗口內 0 篇皆有處置；圖片 0 張皆已判讀 | 不變式通過、逐篇處置完成 |
| threads:yolin1991 | 部分 | 首屏 4 篇、累積 8 篇；最新 2026-11-15T00:51:36+08:00、最舊 2026-11-06T12:51:58+08:00；捲動 2 次、停止原因 reached-window；圖片下載 8 張 | 不變式通過；證據 /Users/eric/aiwork/taiwan-opera-calendar/patrol_evidence/2026-11-15_0833/threads_yolin1991… |
| facebook:sunhope.fans | 部分 | 首屏 3 篇、累積 20 篇；最新 無、最舊 無；捲動 20 次、停止原因 max-scrolls；圖片下載 26 張 | 不變式通過；證據 /Users/eric/aiwork/taiwan-opera-calendar/patrol_evidence/2026-11-15_0833/facebook_sunhope.… |
| facebook:HsiaoHsiYuan1913 | 部分 | 首屏 1 篇、累積 24 篇；最新 無、最舊 無；捲動 20 次、停止原因 max-scrolls；圖片下載 50 張 | 不變式通過；證據 /Users/eric/aiwork/taiwan-opera-calendar/patrol_evidence/2026-11-15_0833/facebook_HsiaoHsi… |
| facebook:100063868113954 | 部分 | 首屏 3 篇、累積 20 篇；最新 無、最舊 無；捲動 20 次、停止原因 max-scrolls；圖片下載 39 張 | 不變式通過；證據 /Users/eric/aiwork/taiwan-opera-calendar/patrol_evidence/2026-11-15_0833/facebook_10006386… |
| facebook:MingHuaYuanTianTaiwaneseOpera | 部分 | 首屏 1 篇、累積 21 篇；最新 無、最舊 無；捲動 20 次、停止原因 max-scrolls；圖片下載 55 張 | 不變式通過；證據 /Users/eric/aiwork/taiwan-opera-calendar/patrol_evidence/2026-11-15_0833/facebook_MingHuaY… |
| facebook:61574134933376 | 部分 | 首屏 1 篇、累積 18 篇；最新 無、最舊 無；捲動 20 次、停止原因 max-scrolls；圖片下載 43 張 | 不變式通過；證據 /Users/eric/aiwork/taiwan-opera-calendar/patrol_evidence/2026-11-15_0833/facebook_61574134… |
| facebook:mhysun | 部分 | 首屏 1 篇、累積 20 篇；最新 無、最舊 無；捲動 20 次、停止原因 max-scrolls；圖片下載 92 張 | 不變式通過；證據 /Users/eric/aiwork/taiwan-opera-calendar/patrol_evidence/2026-11-15_0833/facebook_mhysun.j… |
| facebook:61594936681482 | 部分 | 首屏 1 篇、累積 7 篇；最新 無、最舊 無；捲動 7 次、停止原因 no-new-after-3；圖片下載 23 張 | 不變式通過；證據 /Users/eric/aiwork/taiwan-opera-calendar/patrol_evidence/2026-11-15_0833/facebook_61594936… |
| facebook:lanyang.opera | 部分 | 首屏 3 篇、累積 22 篇；最新 無、最舊 無；捲動 20 次、停止原因 max-scrolls；圖片下載 25 張 | 不變式通過；證據 /Users/eric/aiwork/taiwan-opera-calendar/patrol_evidence/2026-11-15_0833/facebook_lanyang.… |
| facebook:Taichungpuppettheater | 部分 | 首屏 3 篇、累積 25 篇；最新 無、最舊 無；捲動 20 次、停止原因 max-scrolls；圖片下載 33 張 | 不變式通過；證據 /Users/eric/aiwork/taiwan-opera-calendar/patrol_evidence/2026-11-15_0833/facebook_Taichung… |
| culture | 完整 | 9 筆皆有處置 | 逐筆處置完成 |
| issues | 完整 | 3 筆皆有處置 | 逐筆處置完成 |

- OPENTIX：sitemap 802 個活動、本輪有變 613、抓取 250、戲曲相關且未過期 34、延後 363、錯誤 0

## 卡片變更

| 編號 | 動作 | 來源 | 內容 | 差異 | 審查 | 寫入 |
| --- | --- | --- | --- | --- | --- | --- |
| chg-001 | add | https://www.facebook.com/MingHuaYuanTianTaiwaneseOpera/reels_tab | 明華園天字戲劇團｜東隆宮外台演出｜高雄市鳳山區林森路60巷49號【東隆宮】｜2026-12-08 正戲 未公布 |  | needs-check：海報 ac743edd 最後一列確實寫『10/30 12/08 二 高雄市鳳山區林森路60巷49號【東隆宮】』，日期、… | held  |
| chg-002 | add | https://www.facebook.com/photo/?fbid=122315789156250015 | 小金枝歌劇團｜《棄老山傳奇》｜高雄中山堂劇場戶外陽光草坪｜2026-11-27 正戲 19:00 |  | approve：原文『11/27（五）小金枝歌劇團《棄老山傳奇》』、『每場次開演時間｜19:00』、『演出地點｜高雄中山堂劇場戶外陽光… | rejected badgeType-not-free |
| chg-003 | add | https://www.facebook.com/photo/?fbid=122315789156250015 | 新和興總團｜《秦英掛帥》｜高雄中山堂劇場戶外陽光草坪｜2026-11-28 正戲 19:00 |  | approve：原文『11/28（六）新和興總團《秦英掛帥》』，再加上統一的 19:00 開演和中山堂戶外陽光草坪，都正確。11/28… | rejected badgeType-not-free |
| chg-004 | add | https://www.facebook.com/photo/?fbid=122315789156250015 | 藝華園戲劇團｜《八仙傳奇－張果老與藍采和》｜高雄中山堂劇場戶外陽光草坪｜2026-11-29 正戲 19:00 |  | approve：原文『11/29（日）藝華園戲劇團《八仙傳奇－張果老與藍采和》』，19:00、中山堂戶外陽光草坪都對得上，星期也一致。… | rejected badgeType-not-free |
| chg-005 | add | https://www.facebook.com/photo/?fbid=122315789156250015 | 新藝芳歌劇團｜《金蟾緣》｜高雄中山堂劇場戶外陽光草坪｜2026-12-03 正戲 19:00 |  | approve：原文『12/03（四）新藝芳歌劇團《金蟾緣》』，19:00、地點都正確。12/03 是星期四，和原文一致。沒有重複卡。 | rejected badgeType-not-free |
| chg-006 | add | https://www.facebook.com/photo/?fbid=122315789156250015 | 佩儀歌劇團｜《吳漢殺妻》｜高雄中山堂劇場戶外陽光草坪｜2026-12-04 正戲 19:00 |  | approve：原文『12/04（五）佩儀歌劇團《吳漢殺妻》』，19:00、地點都正確。12/04 是星期五，和原文一致。沒有重複卡。 | rejected badgeType-not-free |
| chg-007 | add | https://www.facebook.com/photo/?fbid=122315789156250015 | 文惜歌仔戲劇團｜《焰火長槍：火帥與玉龍的背影》｜高雄中山堂劇場戶外陽光草坪｜2026-12-05 正戲 19:00 |  | approve：原文『12/05（六）文惜歌仔戲劇團《焰火長槍：火帥與玉龍的背影》』，劇團名和劇目都逐字相符，19:00、地點正確，星… | rejected badgeType-not-free |
| chg-008 | add | https://www.facebook.com/photo/?fbid=122315789156250015 | 繡花園戲劇團｜《姜子牙下山》｜高雄中山堂劇場戶外陽光草坪｜2026-12-06 正戲 19:00 |  | approve：原文『12/06（日）繡花園戲劇團《姜子牙下山》』，19:00、地點正確。12/06 是星期日，和原文一致。沒有重複卡。 | rejected badgeType-not-free |
| chg-009 | add | https://www.facebook.com/photo/?fbid=122315789156250015 | 春明歌劇團｜《玉虛戰歌．天命之戰》｜高雄中山堂劇場戶外陽光草坪｜2026-12-11 正戲 19:00 |  | approve：原文『12/11（五）春明歌劇團《玉虛戰歌．天命之戰》』，19:00、地點正確。12/11 是星期五，和原文一致。沒有… | rejected badgeType-not-free |
| chg-010 | add | https://www.facebook.com/photo/?fbid=122315789156250015 | 水錦歌劇團｜《對面夫妻～韋馱與觀音》｜高雄中山堂劇場戶外陽光草坪｜2026-12-12 正戲 19:00 |  | approve：原文『12/12（六）水錦歌劇團《對面夫妻～韋馱與觀音》』，19:00、地點正確。12/12 是星期六，和原文一致。沒… | rejected badgeType-not-free |
| chg-011 | add | https://www.facebook.com/photo/?fbid=122315789156250015 | 明華園星字戲劇團｜《斷案青天－陰錯陽差》｜高雄中山堂劇場戶外陽光草坪｜2026-12-13 正戲 19:00 |  | approve：原文『12/13（日）明華園星字戲劇團《斷案青天－陰錯陽差》』，19:00、地點正確。12/13 是星期日，和原文一致… | rejected badgeType-not-free |
| chg-012 | update（查證成立） | https://web.ncku.edu.tw/p/406-1000-299280,r4153.php?Lang=zh-tw（原貼文 https://www.facebook.com/MingHuaYuanTianTaiwaneseOpera/reels_tab） | 明華園天字戲劇團｜《喜脈緣》｜成大校園｜2026-11-24 正戲 19:00 |  | needs-check：目標卡 auto-20261124-7ac65a66 和成大頁面講的是同一場：11/24 19:00 開演，明華園天字… | held  |
| chg-013 | add（查證成立） | https://www.tw-yishin.com/%e6%bc%94%e5%87%ba%e6%96%b0%e8%a8%8a/2026%e4%b8%80%e5%bf%83%e6%88%b2%e5%8a%87%e5%9c%98%e3%80%8a%e9%96%bb%e7%8e%8b%e7%9a%84%e5%81%87%e6%9c%9f%e3%80%8b/（原貼文 https://www.opentix.life/event/2080109546140397568） | 一心戲劇團｜《閻王的假期》｜臺北市藝文推廣處城市舞台（臺北市松山區八德路三段25號）｜2026-12-05 正戲 14:30、2026-12-06 正戲 14:30 |  | approve：一心戲劇團官網原文『演出時間：2026/12/05(六)14:30 2026/12/06(日)14:30』、『地點：城… | rejected location-not-in-quote,artist-not-in-quote |

## 待查與退回

| 類別 | 貼文 | 原因 | 說明 |
| --- | --- | --- | --- |
| 漏處置 | facebook:100063868113954:1658401932965395 | revision-mismatch |  |

## 遠期場次（超過 120 天，進入 120 天內自動重驗）

| 貼文 | 內容 |
| --- | --- |
| https://www.facebook.com/photo/?fbid=1560228489482771 | 明華園天字戲劇團｜《重返：愛河戀夢》｜臺灣戲曲中心 大表演廳｜2027-06-05、2027-06-06 |
| https://www.facebook.com/MingHuaYuanTianTaiwaneseOpera/reels_tab | 明華園天字戲劇團｜《重返：愛河戀夢》｜臺灣戲曲中心 大表演廳｜2027-06-05、2027-06-06 |
| https://www.threads.com/@taiwaneseopera168/post/DfWAAt6CT5a | 烏貓戲出｜《白賊七》｜高雄中山堂劇場(高雄市左營區實踐路71號)｜2027-04-17、2027-04-18 |
| https://www.threads.com/@taiwaneseopera168/post/DfWAAt6CT5a | 薪傳歌仔戲劇團｜《封神榜．文王食子》｜高雄中山堂劇場(高雄市左營區實踐路71號)｜2027-04-24、2027-04-25 |
| https://www.threads.com/@taiwaneseopera168/post/DfWAAt6CT5a | 燕玲戲劇團｜《韓信設窖安軍心》｜高雄中山堂劇場(高雄市左營區實踐路71號)｜2027-03-20、2027-03-21 |

## 紀錄檔

- 本輪狀態：/Users/eric/aiwork/taiwan-opera-calendar/patrol_state/runs/2026-11-15_0833/state.json
- 巡檢紀錄：patrol_runs/2026-11-15_0833.json（/Users/eric/aiwork/taiwan-opera-calendar）
- 證據：patrol_evidence/2026-11-15_0833/
- 產生時間：2026-11-15T09:10:05+08:00
