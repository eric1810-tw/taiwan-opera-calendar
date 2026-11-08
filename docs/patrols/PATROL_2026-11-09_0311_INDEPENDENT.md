# 巡檢報告 2026-11-09_0311（patrol-v2，正式）

## 需要 Eric 決定

- 前幾天的巡檢沒有完成：2026-11-06：輪次 2026-11-06_0851 沒有跑完
- 判讀有 1 篇沒有逐篇處置，已列待查（見報告）

## 結論

| 項目 | 結果 |
| --- | --- |
| 執行 | 開始 2026-11-09T03:11:29+08:00；結果 進行中；步驟 preflight:done、collect:done、pack:done、judge:done、check:done、verify:done、review:done、apply:done、publish:done、report:running |
| 來源 | 20 個：完整 3、部分 17、失敗 0、未讀 0 |
| 資料 | 送判讀 226 篇／圖 10 張；變更提案 35、確認一致 25、送查證 65（成立 1、與卡相同 0、查無佐證不收 65）、退回 0、漏處置 1；已過期不收 87、遠期暫存 4 |
| 寫入 | 寫入 3、add_card 拒絕 11、審查未通過 21 |
| 發布 | verified；SHA c97aaadb8ff553f74ce552a284e75eef38179cb5；Actions 42516618519 |

## 模型與用量

| 角色 | 模型 | 依據 |
| --- | --- | --- |
| main | claude-sonnet-5-5 | get_session self：effort=medium |
| judge | sonnet | Agent 工具 model 參數；effort=medium |
| verify | opus | Agent 工具 model 參數；effort=medium |
| review | opus | Agent 工具 model 參數；effort=medium |

- 判讀批次 10；送出貼文 226 篇、圖片 10 張、正文約 73262 字
- 略過（已判讀未變動）121 篇；窗口外 42 篇
- 第二次審查：有（35 項）

## 來源

| 來源 | 狀態 | 範圍 | 說明 |
| --- | --- | --- | --- |
| threads:joe_huang_k_w | 部分 | 首屏 4 篇、累積 10 篇；最新 2026-11-08T14:16:48+08:00、最舊 2026-10-31T19:53:42+08:00；捲動 2 次、停止原因 reached-window；圖片下載 19 張 | 不變式通過；證據 /Users/eric/aiwork/taiwan-opera-calendar/patrol_evidence/2026-11-09_0311/threads_joe_huang… |
| threads:h.akito_1996 | 部分 | 首屏 4 篇、累積 6 篇；最新 2026-11-04T17:59:03+08:00、最舊 2026-09-27T00:04:33+08:00；捲動 1 次、停止原因 reached-window；圖片下載 4 張 | 不變式通過；證據 /Users/eric/aiwork/taiwan-opera-calendar/patrol_evidence/2026-11-09_0311/threads_h.akito_1… |
| threads:the_rin.lpm | 部分 | 首屏 4 篇、累積 7 篇；最新 2026-11-08T16:11:56+08:00、最舊 2026-09-26T14:32:03+08:00；捲動 2 次、停止原因 reached-window；圖片下載 12 張 | 不變式通過；證據 /Users/eric/aiwork/taiwan-opera-calendar/patrol_evidence/2026-11-09_0311/threads_the_rin.l… |
| threads:xuefeng_lu_ | 完整 | 7 天窗口讀完（停止原因 reached-window）；窗口內 5 篇皆有處置；圖片 0 張皆已判讀 | 不變式通過、逐篇處置完成 |
| threads:yuzhongluo | 部分 | 首屏 4 篇、累積 23 篇；最新 2026-11-09T00:32:31+08:00、最舊 2026-10-26T14:07:54+08:00；捲動 4 次、停止原因 reached-window；圖片下載 23 張 | 不變式通過；證據 /Users/eric/aiwork/taiwan-opera-calendar/patrol_evidence/2026-11-09_0311/threads_yuzhonglu… |
| threads:taiwaneseopera168 | 部分 | 首屏 5 篇、累積 46 篇；最新 2026-11-09T01:18:16+08:00、最舊 2026-08-16T02:33:12+08:00；捲動 20 次、停止原因 max-scrolls；圖片下載 64 張 | 不變式通過；證據 /Users/eric/aiwork/taiwan-opera-calendar/patrol_evidence/2026-11-09_0311/threads_taiwanese… |
| threads:jing__1017 | 部分 | 首屏 4 篇、累積 40 篇；最新 2026-11-07T20:51:15+08:00、最舊 2026-10-28T19:50:21+08:00；捲動 14 次、停止原因 reached-window；圖片下載 43 張 | 不變式通過；證據 /Users/eric/aiwork/taiwan-opera-calendar/patrol_evidence/2026-11-09_0311/threads_jing__101… |
| threads:hilang.on.tour | 完整 | 7 天窗口讀完（停止原因 reached-window）；窗口內 0 篇皆有處置；圖片 0 張皆已判讀 | 不變式通過、逐篇處置完成 |
| threads:yolin1991 | 部分 | 首屏 4 篇、累積 16 篇；最新 2026-11-09T01:51:16+08:00、最舊 2026-10-09T19:47:26+08:00；捲動 1 次、停止原因 reached-window；圖片下載 16 張 | 不變式通過；證據 /Users/eric/aiwork/taiwan-opera-calendar/patrol_evidence/2026-11-09_0311/threads_yolin1991… |
| facebook:sunhope.fans | 部分 | 首屏 2 篇、累積 20 篇；最新 無、最舊 無；捲動 20 次、停止原因 max-scrolls；圖片下載 26 張 | 不變式通過；證據 /Users/eric/aiwork/taiwan-opera-calendar/patrol_evidence/2026-11-09_0311/facebook_sunhope.… |
| facebook:HsiaoHsiYuan1913 | 部分 | 首屏 3 篇、累積 23 篇；最新 無、最舊 無；捲動 20 次、停止原因 max-scrolls；圖片下載 38 張 | 不變式通過；證據 /Users/eric/aiwork/taiwan-opera-calendar/patrol_evidence/2026-11-09_0311/facebook_HsiaoHsi… |
| facebook:100063868113954 | 部分 | 首屏 2 篇、累積 22 篇；最新 無、最舊 無；捲動 20 次、停止原因 max-scrolls；圖片下載 48 張 | 不變式通過；證據 /Users/eric/aiwork/taiwan-opera-calendar/patrol_evidence/2026-11-09_0311/facebook_10006386… |
| facebook:MingHuaYuanTianTaiwaneseOpera | 部分 | 首屏 1 篇、累積 22 篇；最新 無、最舊 無；捲動 20 次、停止原因 max-scrolls；圖片下載 55 張 | 不變式通過；證據 /Users/eric/aiwork/taiwan-opera-calendar/patrol_evidence/2026-11-09_0311/facebook_MingHuaY… |
| facebook:61574134933376 | 部分 | 首屏 2 篇、累積 19 篇；最新 無、最舊 無；捲動 20 次、停止原因 max-scrolls；圖片下載 34 張 | 不變式通過；證據 /Users/eric/aiwork/taiwan-opera-calendar/patrol_evidence/2026-11-09_0311/facebook_61574134… |
| facebook:mhysun | 部分 | 首屏 1 篇、累積 21 篇；最新 無、最舊 無；捲動 20 次、停止原因 max-scrolls；圖片下載 93 張 | 不變式通過；證據 /Users/eric/aiwork/taiwan-opera-calendar/patrol_evidence/2026-11-09_0311/facebook_mhysun.j… |
| facebook:61594936681482 | 部分 | 首屏 1 篇、累積 7 篇；最新 無、最舊 無；捲動 7 次、停止原因 no-new-after-3；圖片下載 23 張 | 不變式通過；證據 /Users/eric/aiwork/taiwan-opera-calendar/patrol_evidence/2026-11-09_0311/facebook_61594936… |
| facebook:lanyang.opera | 部分 | 首屏 2 篇、累積 22 篇；最新 無、最舊 無；捲動 20 次、停止原因 max-scrolls；圖片下載 27 張 | 不變式通過；證據 /Users/eric/aiwork/taiwan-opera-calendar/patrol_evidence/2026-11-09_0311/facebook_lanyang.… |
| facebook:Taichungpuppettheater | 部分 | 首屏 1 篇、累積 26 篇；最新 無、最舊 無；捲動 20 次、停止原因 max-scrolls；圖片下載 42 張 | 不變式通過；證據 /Users/eric/aiwork/taiwan-opera-calendar/patrol_evidence/2026-11-09_0311/facebook_Taichung… |
| culture | 完整 | 9 筆皆有處置 | 逐筆處置完成 |
| issues | 部分 | state=all 共 3 則（含留言） | 已讀取；處置待判讀後確認 |

- OPENTIX：sitemap 814 個活動、本輪有變 601、抓取 250、戲曲相關且未過期 36、延後 351、錯誤 0

## 卡片變更

| 編號 | 動作 | 來源 | 內容 | 差異 | 審查 | 寫入 |
| --- | --- | --- | --- | --- | --- | --- |
| chg-001 | add | https://www.threads.com/@taiwaneseopera168/post/DfQ5lKaiQVF | 小金枝歌劇團｜《棄老山傳奇》｜高雄中山堂劇場戶外陽光草坪｜2026-11-27 正戲 19:00 |  | approve：source.text（taiwaneseopera168 2026-11-03）「11/27(五)小金枝歌劇團《棄老… | rejected badgeType-not-free |
| chg-002 | add | https://www.threads.com/@taiwaneseopera168/post/DfQ5lKaiQVF | 新和興總團｜《秦英掛帥》｜高雄中山堂劇場戶外陽光草坪｜2026-11-28 正戲 19:00 |  | approve：原文「11/28(六)新和興總團《秦英掛帥》」、統一 19:00、中山堂陽光草坪、免費；11/28 為週六。sched… | rejected badgeType-not-free |
| chg-003 | add | https://www.threads.com/@taiwaneseopera168/post/DfQ5lKaiQVF | 藝華園戲劇團｜《八仙傳奇－張果老與藍采和》｜高雄中山堂劇場戶外陽光草坪｜2026-11-29 正戲 19:00 |  | approve：原文「11/29(日)藝華園戲劇團《八仙傳奇－張果老與藍采和》」、19:00、中山堂陽光草坪、免費；11/29 為週日… | rejected badgeType-not-free |
| chg-004 | add | https://www.threads.com/@taiwaneseopera168/post/DfQ5lKaiQVF | 新藝芳歌劇團｜《金蟾緣》｜高雄中山堂劇場戶外陽光草坪｜2026-12-03 正戲 19:00 |  | approve：原文「12/03(四)新藝芳歌劇團《金蟾緣》」、19:00、中山堂陽光草坪、免費；12/03 為週四。chg-014、… | rejected badgeType-not-free |
| chg-005 | add | https://www.threads.com/@taiwaneseopera168/post/DfQ5lKaiQVF | 佩儀歌劇團｜《吳漢殺妻》｜高雄中山堂劇場戶外陽光草坪｜2026-12-04 正戲 19:00 |  | approve：原文「12/04(五)佩儀歌劇團《吳漢殺妻》」、19:00、中山堂陽光草坪、免費；12/04 為週五。chg-015、… | rejected badgeType-not-free |
| chg-006 | add | https://www.threads.com/@taiwaneseopera168/post/DfQ5lKaiQVF | 文惜歌仔戲劇團｜《焰火長槍：火帥與玉龍的背影》｜高雄中山堂劇場戶外陽光草坪｜2026-12-05 正戲 19:00 |  | approve：原文「12/05(六)文惜歌仔戲劇團《焰火長槍：火帥與玉龍的背影》」、19:00、中山堂陽光草坪、免費；12/05 為… | rejected badgeType-not-free |
| chg-007 | add | https://www.threads.com/@taiwaneseopera168/post/DfQ5lKaiQVF | 繡花園戲劇團｜《姜子牙下山》｜高雄中山堂劇場戶外陽光草坪｜2026-12-06 正戲 19:00 |  | approve：原文「12/06(日)繡花園戲劇團《姜子牙下山》」、19:00、中山堂陽光草坪、免費；12/06 為週日。chg-01… | rejected badgeType-not-free |
| chg-008 | add | https://www.threads.com/@taiwaneseopera168/post/DfQ5lKaiQVF | 春明歌劇團｜《玉虛戰歌．天命之戰》｜高雄中山堂劇場戶外陽光草坪｜2026-12-11 正戲 19:00 |  | approve：原文「12/11(五)春明歌劇團《玉虛戰歌．天命之戰》」、19:00、中山堂陽光草坪、免費；12/11 為週五。chg… | rejected badgeType-not-free |
| chg-009 | add | https://www.threads.com/@taiwaneseopera168/post/DfQ5lKaiQVF | 水錦歌劇團｜《對面夫妻～韋馱與觀音》｜高雄中山堂劇場戶外陽光草坪｜2026-12-12 正戲 19:00 |  | approve：原文「12/12(六)水錦歌劇團《對面夫妻～韋馱與觀音》」、19:00、中山堂陽光草坪、免費；12/12 為週六。ch… | rejected badgeType-not-free |
| chg-010 | add | https://www.threads.com/@taiwaneseopera168/post/DfQ5lKaiQVF | 明華園星字戲劇團｜《斷案青天－陰錯陽差》｜高雄中山堂劇場戶外陽光草坪｜2026-12-13 正戲 19:00 |  | approve：原文「12/13(日)明華園星字戲劇團《斷案青天－陰錯陽差》」、19:00、中山堂陽光草坪、免費；12/13 為週日。… | rejected badgeType-not-free |
| chg-011 | add | https://www.threads.com/@jing__1017/post/DfR48oeiau2 | 小金枝歌劇團｜《棄老山傳奇》｜高雄中山堂劇場戶外陽光草坪｜2026-11-27 正戲 19:00 |  | reject：重複建卡：與 chg-001 同劇團、同劇目、同日 2026-11-27 19:00、同地點（jing__1017 轉… | held  |
| chg-012 | add | https://www.threads.com/@jing__1017/post/DfR48oeiau2 | 新和興總團｜《秦英掛帥》｜高雄中山堂劇場戶外陽光草坪｜2026-11-28 正戲 19:00 |  | reject：重複建卡：與 chg-002（新和興總團《秦英掛帥》11/28 19:00 中山堂）同一場，應併入 chg-002 的… | held  |
| chg-013 | add | https://www.threads.com/@jing__1017/post/DfR48oeiau2 | 藝華園戲劇團｜《八仙傳奇－張果老與藍采和》｜高雄中山堂劇場戶外陽光草坪｜2026-11-29 正戲 19:00 |  | reject：重複建卡：與 chg-003（藝華園《八仙傳奇－張果老與藍采和》11/29）同一場，應併入 chg-003 的 als… | held  |
| chg-014 | add | https://www.threads.com/@jing__1017/post/DfR48oeiau2 | 新藝芳歌劇團｜《金蟾緣》｜高雄中山堂劇場戶外陽光草坪｜2026-12-03 正戲 19:00 |  | reject：重複建卡：與 chg-004（新藝芳《金蟾緣》12/03）同一場，應併入 chg-004 的 alsoSources。 | held  |
| chg-015 | add | https://www.threads.com/@jing__1017/post/DfR48oeiau2 | 佩儀歌劇團｜《吳漢殺妻》｜高雄中山堂劇場戶外陽光草坪｜2026-12-04 正戲 19:00 |  | reject：重複建卡：與 chg-005（佩儀《吳漢殺妻》12/04）同一場，應併入 chg-005 的 alsoSources。 | held  |
| chg-016 | add | https://www.threads.com/@jing__1017/post/DfR48oeiau2 | 文惜歌仔戲劇團｜《焰火長槍：火帥與玉龍的背影》｜高雄中山堂劇場戶外陽光草坪｜2026-12-05 正戲 19:00 |  | reject：重複建卡：與 chg-006（文惜《焰火長槍》12/05）同一場，應併入 chg-006 的 alsoSources。 | held  |
| chg-017 | add | https://www.threads.com/@jing__1017/post/DfR48oeiau2 | 繡花園戲劇團｜《姜子牙下山》｜高雄中山堂劇場戶外陽光草坪｜2026-12-06 正戲 19:00 |  | reject：重複建卡：與 chg-007（繡花園《姜子牙下山》12/06）同一場，應併入 chg-007 的 alsoSource… | held  |
| chg-018 | add | https://www.threads.com/@jing__1017/post/DfR48oeiau2 | 春明歌劇團｜《玉虛戰歌．天命之戰》｜高雄中山堂劇場戶外陽光草坪｜2026-12-11 正戲 19:00 |  | reject：重複建卡：與 chg-008（春明《玉虛戰歌．天命之戰》12/11）同一場，應併入 chg-008 的 alsoSou… | held  |
| chg-019 | add | https://www.threads.com/@jing__1017/post/DfR48oeiau2 | 水錦歌劇團｜《對面夫妻～韋馱與觀音》｜高雄中山堂劇場戶外陽光草坪｜2026-12-12 正戲 19:00 |  | reject：重複建卡：與 chg-009（水錦《對面夫妻～韋馱與觀音》12/12）同一場，應併入 chg-009 的 alsoSo… | held  |
| chg-020 | add | https://www.threads.com/@jing__1017/post/DfR48oeiau2 | 明華園星字戲劇團｜《斷案青天－陰錯陽差》｜高雄中山堂劇場戶外陽光草坪｜2026-12-13 正戲 19:00 |  | reject：重複建卡：與 chg-010（明華園星字《斷案青天－陰錯陽差》12/13）同一場，應併入 chg-010 的 also… | held  |
| chg-021 | add | https://www.facebook.com/MingHuaYuanTianTaiwaneseOpera/reels_tab | 明華園天字戲劇團｜財神宮外台演出｜屏東縣潮州鎮彭城路125巷42-3號【財神宮】｜2026-11-22 其他 未公布 |  | approve：親自看過海報 ac743edd…jpg（明華園天字戲劇團115年農曆10月戲路表）：「10/14 11/22 日 屏東… | added  |
| chg-022 | add | https://www.facebook.com/MingHuaYuanTianTaiwaneseOpera/reels_tab | 明華園天字戲劇團｜東隆宮外台演出｜高雄市鳳山區林森路60巷49號【東隆宮】｜2026-12-08 其他 未公布 |  | needs-check：海報 ac743edd…jpg 確有「10/30 12/08 二 高雄市鳳山區林森路60巷49號【東隆宮】」，但同列另… | held  |
| chg-023 | add | https://www.facebook.com/photo/?fbid=122315789156250015 | 小金枝歌劇團｜《棄老山傳奇》｜高雄中山堂劇場戶外陽光草坪｜2026-11-27 正戲 19:00 |  | reject：重複建卡：與 chg-001（小金枝《棄老山傳奇》11/27 19:00 中山堂）同一場，FB 61574134933… | held  |
| chg-024 | add | https://www.facebook.com/photo/?fbid=122315789156250015 | 新和興總團｜《秦英掛帥》｜高雄中山堂劇場戶外陽光草坪｜2026-11-28 正戲 19:00 |  | reject：重複建卡：與 chg-002（新和興《秦英掛帥》11/28）同一場，應併入 alsoSources。 | held  |
| chg-025 | add | https://www.facebook.com/photo/?fbid=122315789156250015 | 藝華園戲劇團｜《八仙傳奇－張果老與藍采和》｜高雄中山堂劇場戶外陽光草坪｜2026-11-29 正戲 19:00 |  | reject：重複建卡：與 chg-003（藝華園《八仙傳奇》11/29）同一場，應併入 alsoSources。 | held  |
| chg-026 | add | https://www.facebook.com/photo/?fbid=122315789156250015 | 新藝芳歌劇團｜《金蟾緣》｜高雄中山堂劇場戶外陽光草坪｜2026-12-03 正戲 19:00 |  | reject：重複建卡：與 chg-004（新藝芳《金蟾緣》12/03）同一場，應併入 alsoSources。 | held  |
| chg-027 | add | https://www.facebook.com/photo/?fbid=122315789156250015 | 佩儀歌劇團｜《吳漢殺妻》｜高雄中山堂劇場戶外陽光草坪｜2026-12-04 正戲 19:00 |  | reject：重複建卡：與 chg-005（佩儀《吳漢殺妻》12/04）同一場，應併入 alsoSources。 | held  |
| chg-028 | add | https://www.facebook.com/photo/?fbid=122315789156250015 | 文惜歌仔戲劇團｜《焰火長槍：火帥與玉龍的背影》｜高雄中山堂劇場戶外陽光草坪｜2026-12-05 正戲 19:00 |  | reject：重複建卡：與 chg-006（文惜《焰火長槍》12/05）同一場，應併入 alsoSources。 | held  |
| chg-029 | add | https://www.facebook.com/photo/?fbid=122315789156250015 | 繡花園戲劇團｜《姜子牙下山》｜高雄中山堂劇場戶外陽光草坪｜2026-12-06 正戲 19:00 |  | reject：重複建卡：與 chg-007（繡花園《姜子牙下山》12/06）同一場，應併入 alsoSources。 | held  |
| chg-030 | add | https://www.facebook.com/photo/?fbid=122315789156250015 | 春明歌劇團｜《玉虛戰歌．天命之戰》｜高雄中山堂劇場戶外陽光草坪｜2026-12-11 正戲 19:00 |  | reject：重複建卡：與 chg-008（春明《玉虛戰歌》12/11）同一場，應併入 alsoSources。 | held  |
| chg-031 | add | https://www.facebook.com/photo/?fbid=122315789156250015 | 水錦歌劇團｜《對面夫妻～韋馱與觀音》｜高雄中山堂劇場戶外陽光草坪｜2026-12-12 正戲 19:00 |  | reject：重複建卡：與 chg-009（水錦《對面夫妻》12/12）同一場，應併入 alsoSources。 | held  |
| chg-032 | add | https://www.facebook.com/photo/?fbid=122315789156250015 | 明華園星字戲劇團｜《斷案青天－陰錯陽差》｜高雄中山堂劇場戶外陽光草坪｜2026-12-13 正戲 19:00 |  | reject：重複建卡：與 chg-010（明華園星字《斷案青天》12/13）同一場，應併入 alsoSources。 | held  |
| chg-033 | add | https://www.facebook.com/mhysun/reels_tab | 明華園總團｜《蓬萊仙島・漢鍾離》｜斗六藝術水岸園區｜2026-11-15 正戲 19:00 |  | approve：明華園官方 FB 原文「11/15（日）晚上7:00 明華園總團將再次來到雲林，在斗六藝術水岸園區帶來《蓬萊仙島・漢鍾… | added  |
| chg-034 | add | https://www.facebook.com/Taichungpuppettheater/reels_tab | 台中木偶劇團｜『波比大冒險』｜臺中市屯區藝文中心-茄苳樹區｜2026-11-14 正戲 15:00 |  | approve：台中木偶劇團官方 FB 原文「演出時間｜11月14日（六）15:00」「入場方式｜免費入場」「演出地點｜臺中市屯區藝文… | added  |
| chg-035 | add（查證成立） | https://www.opentix.life/event/2090269380048343041（原貼文 https://www.opentix.life/event/2090269380048343041） | 薪傳歌仔戲劇團｜戲釀青春──2026育成聯合展演《蒼原孤雁》｜臺灣戲曲中心小表演廳｜2026-11-14 正戲 14:30 |  | approve：OPENTIX 官方節目頁（主辦：國立傳統藝術中心）【小表演廳】列「11/14（六）14:30 薪傳歌仔戲劇團《蒼原孤… | rejected location-not-in-quote,title-not-in-quote,badgeType-not-ticket |

## 待查與退回

| 類別 | 貼文 | 原因 | 說明 |
| --- | --- | --- | --- |
| 漏處置 | threads:yolin1991:DffVY78D04n | revision-mismatch |  |

## 遠期場次（超過 120 天，進入 120 天內自動重驗）

| 貼文 | 內容 |
| --- | --- |
| https://www.facebook.com/photo/?fbid=1560228489482771 | 明華園天字戲劇團｜《重返：愛河戀夢》｜臺灣戲曲中心 大表演廳｜2027-06-05、2027-06-06 |
| https://www.facebook.com/MingHuaYuanTianTaiwaneseOpera/reels_tab | 明華園天字戲劇團｜《重返：愛河戀夢》｜臺灣戲曲中心 大表演廳｜2027-06-05、2027-06-06 |
| https://www.threads.com/@taiwaneseopera168/post/DfWAAt6CT5a | 烏貓戲出｜《白賊七》｜高雄中山堂劇場(高雄市左營區實踐路71號)｜2027-04-17、2027-04-18 |
| https://www.threads.com/@taiwaneseopera168/post/DfWAAt6CT5a | 薪傳歌仔戲劇團｜《封神榜．文王食子》｜高雄中山堂劇場(高雄市左營區實踐路71號)｜2027-04-24、2027-04-25 |

## 紀錄檔

- 本輪狀態：/Users/eric/aiwork/taiwan-opera-calendar/patrol_state/runs/2026-11-09_0311/state.json
- 巡檢紀錄：patrol_runs/2026-11-09_0311.json（/Users/eric/aiwork/taiwan-opera-calendar）
- 證據：patrol_evidence/2026-11-09_0311/
- 產生時間：2026-11-09T03:45:56+08:00
