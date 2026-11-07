# 巡檢報告 2026-11-08_0311（patrol-v2，正式）

## 需要 Eric 決定

- 前幾天的巡檢沒有完成：2026-11-06：輪次 2026-11-06_0851 沒有跑完
- 判讀有 2 篇沒有逐篇處置，已列待查（見報告）

## 結論

| 項目 | 結果 |
| --- | --- |
| 執行 | 開始 2026-11-08T03:11:25+08:00；結果 進行中；步驟 preflight:done、collect:done、pack:done、judge:done、check:done、verify:done、review:done、apply:done、publish:done、report:running |
| 來源 | 20 個：完整 2、部分 18、失敗 0、未讀 0 |
| 資料 | 送判讀 226 篇／圖 11 張；變更提案 37、確認一致 32、送查證 51（成立 5、與卡相同 0、查無佐證不收 50）、退回 0、漏處置 2；已過期不收 77、遠期暫存 4 |
| 寫入 | 寫入 4、add_card 拒絕 10、審查未通過 23 |
| 發布 | verified；SHA c2f09c2d8742a4432c45d6835966ca0cc6750319；Actions 42408203279 |

## 模型與用量

| 角色 | 模型 | 依據 |
| --- | --- | --- |
| main | claude-sonnet-5-5 | get_session self：effort=medium |
| judge | sonnet | Agent 工具 model 參數；effort=medium |
| verify | opus | Agent 工具 model 參數；effort=medium |
| review | opus | Agent 工具 model 參數；effort=medium |

- 判讀批次 10；送出貼文 226 篇、圖片 11 張、正文約 77820 字
- 略過（已判讀未變動）125 篇；窗口外 22 篇
- 第二次審查：有（37 項）

## 來源

| 來源 | 狀態 | 範圍 | 說明 |
| --- | --- | --- | --- |
| threads:joe_huang_k_w | 部分 | 首屏 4 篇、累積 10 篇；最新 2026-11-08T01:16:21+08:00、最舊 2026-10-30T22:54:08+08:00；捲動 3 次、停止原因 reached-window；圖片下載 20 張 | 不變式通過；證據 /Users/eric/aiwork/taiwan-opera-calendar/patrol_evidence/2026-11-08_0311/threads_joe_huang… |
| threads:h.akito_1996 | 部分 | 首屏 4 篇、累積 6 篇；最新 2026-11-04T17:59:03+08:00、最舊 2026-09-27T00:04:33+08:00；捲動 1 次、停止原因 reached-window；圖片下載 4 張 | 不變式通過；證據 /Users/eric/aiwork/taiwan-opera-calendar/patrol_evidence/2026-11-08_0311/threads_h.akito_1… |
| threads:the_rin.lpm | 部分 | 首屏 4 篇、累積 7 篇；最新 2026-11-07T15:40:32+08:00、最舊 2026-09-26T14:32:03+08:00；捲動 2 次、停止原因 reached-window；圖片下載 9 張 | 不變式通過；證據 /Users/eric/aiwork/taiwan-opera-calendar/patrol_evidence/2026-11-08_0311/threads_the_rin.l… |
| threads:xuefeng_lu_ | 部分 | 首屏 4 篇、累積 5 篇；最新 2026-11-06T06:58:42+08:00、最舊 2026-10-31T17:24:08+08:00；捲動 3 次、停止原因 no-new-after-3；圖片下載 0 張 | 不變式通過；證據 /Users/eric/aiwork/taiwan-opera-calendar/patrol_evidence/2026-11-08_0311/threads_xuefeng_l… |
| threads:yuzhongluo | 部分 | 首屏 4 篇、累積 10 篇；最新 2026-11-06T20:36:15+08:00、最舊 2026-10-29T17:04:37+08:00；捲動 3 次、停止原因 reached-window；圖片下載 25 張 | 不變式通過；證據 /Users/eric/aiwork/taiwan-opera-calendar/patrol_evidence/2026-11-08_0311/threads_yuzhonglu… |
| threads:taiwaneseopera168 | 部分 | 首屏 4 篇、累積 43 篇；最新 2026-11-07T20:27:52+08:00、最舊 2026-08-16T02:33:12+08:00；捲動 20 次、停止原因 max-scrolls；圖片下載 66 張 | 不變式通過；證據 /Users/eric/aiwork/taiwan-opera-calendar/patrol_evidence/2026-11-08_0311/threads_taiwanese… |
| threads:jing__1017 | 部分 | 首屏 6 篇、累積 41 篇；最新 2026-11-07T20:51:15+08:00、最舊 2026-10-28T19:50:21+08:00；捲動 14 次、停止原因 reached-window；圖片下載 46 張 | 不變式通過；證據 /Users/eric/aiwork/taiwan-opera-calendar/patrol_evidence/2026-11-08_0311/threads_jing__101… |
| threads:hilang.on.tour | 完整 | 7 天窗口讀完（停止原因 reached-window）；窗口內 0 篇皆有處置；圖片 0 張皆已判讀 | 不變式通過、逐篇處置完成 |
| threads:yolin1991 | 部分 | 首屏 4 篇、累積 9 篇；最新 2026-11-06T12:51:58+08:00、最舊 2026-10-28T18:34:21+08:00；捲動 3 次、停止原因 reached-window；圖片下載 9 張 | 不變式通過；證據 /Users/eric/aiwork/taiwan-opera-calendar/patrol_evidence/2026-11-08_0311/threads_yolin1991… |
| facebook:sunhope.fans | 部分 | 首屏 4 篇、累積 21 篇；最新 無、最舊 無；捲動 20 次、停止原因 max-scrolls；圖片下載 25 張 | 不變式通過；證據 /Users/eric/aiwork/taiwan-opera-calendar/patrol_evidence/2026-11-08_0311/facebook_sunhope.… |
| facebook:HsiaoHsiYuan1913 | 部分 | 首屏 1 篇、累積 24 篇；最新 無、最舊 無；捲動 20 次、停止原因 max-scrolls；圖片下載 50 張 | 不變式通過；證據 /Users/eric/aiwork/taiwan-opera-calendar/patrol_evidence/2026-11-08_0311/facebook_HsiaoHsi… |
| facebook:100063868113954 | 部分 | 首屏 3 篇、累積 21 篇；最新 無、最舊 無；捲動 20 次、停止原因 max-scrolls；圖片下載 48 張 | 不變式通過；證據 /Users/eric/aiwork/taiwan-opera-calendar/patrol_evidence/2026-11-08_0311/facebook_10006386… |
| facebook:MingHuaYuanTianTaiwaneseOpera | 部分 | 首屏 1 篇、累積 23 篇；最新 無、最舊 無；捲動 20 次、停止原因 max-scrolls；圖片下載 61 張 | 不變式通過；證據 /Users/eric/aiwork/taiwan-opera-calendar/patrol_evidence/2026-11-08_0311/facebook_MingHuaY… |
| facebook:61574134933376 | 部分 | 首屏 2 篇、累積 19 篇；最新 無、最舊 無；捲動 20 次、停止原因 max-scrolls；圖片下載 34 張 | 不變式通過；證據 /Users/eric/aiwork/taiwan-opera-calendar/patrol_evidence/2026-11-08_0311/facebook_61574134… |
| facebook:mhysun | 部分 | 首屏 1 篇、累積 20 篇；最新 無、最舊 無；捲動 20 次、停止原因 max-scrolls；圖片下載 89 張 | 不變式通過；證據 /Users/eric/aiwork/taiwan-opera-calendar/patrol_evidence/2026-11-08_0311/facebook_mhysun.j… |
| facebook:61594936681482 | 部分 | 首屏 1 篇、累積 7 篇；最新 無、最舊 無；捲動 7 次、停止原因 no-new-after-3；圖片下載 23 張 | 不變式通過；證據 /Users/eric/aiwork/taiwan-opera-calendar/patrol_evidence/2026-11-08_0311/facebook_61594936… |
| facebook:lanyang.opera | 部分 | 首屏 1 篇、累積 23 篇；最新 無、最舊 無；捲動 20 次、停止原因 max-scrolls；圖片下載 38 張 | 不變式通過；證據 /Users/eric/aiwork/taiwan-opera-calendar/patrol_evidence/2026-11-08_0311/facebook_lanyang.… |
| facebook:Taichungpuppettheater | 部分 | 首屏 1 篇、累積 27 篇；最新 無、最舊 無；捲動 20 次、停止原因 max-scrolls；圖片下載 47 張 | 不變式通過；證據 /Users/eric/aiwork/taiwan-opera-calendar/patrol_evidence/2026-11-08_0311/facebook_Taichung… |
| culture | 完整 | 9 筆皆有處置 | 逐筆處置完成 |
| issues | 部分 | state=all 共 3 則（含留言） | 已讀取；處置待判讀後確認 |

- OPENTIX：sitemap 842 個活動、本輪有變 633、抓取 250、戲曲相關且未過期 40、延後 383、錯誤 0

## 卡片變更

| 編號 | 動作 | 來源 | 內容 | 差異 | 審查 | 寫入 |
| --- | --- | --- | --- | --- | --- | --- |
| chg-001 | add | https://www.threads.com/@taiwaneseopera168/post/DfZcD7ciVYP | 明華園黃字戲劇團｜《三抄府》｜嘉義市北香湖廣場｜2026-11-08 正戲 19:00 |  | needs-check：日期、時間、地點、劇團、劇目都對得上原文「⏰️11/8(日) 19:00 嘉義市北香湖廣場」，海報也印「11/08 1… | held  |
| chg-002 | add | https://www.threads.com/@taiwaneseopera168/post/DfQ5lKaiQVF | 小金枝歌劇團｜《棄老山傳奇》｜高雄中山堂劇場戶外陽光草坪｜2026-11-27 正戲 19:00 |  | approve：原文「11/27(五)小金枝歌劇團《棄老山傳奇》」「每場次開演時間｜19:00」「演出地點｜高雄中山堂劇場戶外陽光草坪… | rejected badgeType-not-free |
| chg-003 | add | https://www.threads.com/@taiwaneseopera168/post/DfQ5lKaiQVF | 新和興總團｜《秦英掛帥》｜高雄中山堂劇場戶外陽光草坪｜2026-11-28 正戲 19:00 |  | approve：原文「11/28(六)新和興總團《秦英掛帥》」，共用 19:00、高雄中山堂劇場戶外陽光草坪、免費入場，星期相符。 | rejected badgeType-not-free |
| chg-004 | add | https://www.threads.com/@taiwaneseopera168/post/DfQ5lKaiQVF | 藝華園戲劇團｜《八仙傳奇－張果老與藍采和》｜高雄中山堂劇場戶外陽光草坪｜2026-11-29 正戲 19:00 |  | approve：原文「11/29(日)藝華園戲劇團《八仙傳奇－張果老與藍采和》」，共用時間、地點、免費入場，星期相符。 | rejected badgeType-not-free |
| chg-005 | add | https://www.threads.com/@taiwaneseopera168/post/DfQ5lKaiQVF | 新藝芳歌劇團｜《金蟾緣》｜高雄中山堂劇場戶外陽光草坪｜2026-12-03 正戲 19:00 |  | approve：原文「12/03(四)新藝芳歌劇團《金蟾緣》」，共用時間、地點、免費入場，星期相符。 | rejected badgeType-not-free |
| chg-006 | add | https://www.threads.com/@taiwaneseopera168/post/DfQ5lKaiQVF | 佩儀歌劇團｜《吳漢殺妻》｜高雄中山堂劇場戶外陽光草坪｜2026-12-04 正戲 19:00 |  | approve：原文「12/04(五)佩儀歌劇團《吳漢殺妻》」，共用時間、地點、免費入場，星期相符。 | rejected badgeType-not-free |
| chg-007 | add | https://www.threads.com/@taiwaneseopera168/post/DfQ5lKaiQVF | 文惜歌仔戲劇團｜《焰火長槍：火帥與玉龍的背影》｜高雄中山堂劇場戶外陽光草坪｜2026-12-05 正戲 19:00 |  | approve：原文「12/05(六)文惜歌仔戲劇團《焰火長槍：火帥與玉龍的背影》」，共用時間、地點、免費入場，星期相符。 | rejected badgeType-not-free |
| chg-008 | add | https://www.threads.com/@taiwaneseopera168/post/DfQ5lKaiQVF | 繡花園戲劇團｜《姜子牙下山》｜高雄中山堂劇場戶外陽光草坪｜2026-12-06 正戲 19:00 |  | approve：原文「12/06(日)繡花園戲劇團《姜子牙下山》」，共用時間、地點、免費入場，星期相符。 | rejected badgeType-not-free |
| chg-009 | add | https://www.threads.com/@taiwaneseopera168/post/DfQ5lKaiQVF | 春明歌劇團｜《玉虛戰歌．天命之戰》｜高雄中山堂劇場戶外陽光草坪｜2026-12-11 正戲 19:00 |  | approve：原文「12/11(五)春明歌劇團《玉虛戰歌．天命之戰》」，共用時間、地點、免費入場，星期相符。 | rejected badgeType-not-free |
| chg-010 | add | https://www.threads.com/@taiwaneseopera168/post/DfQ5lKaiQVF | 水錦歌劇團｜《對面夫妻～韋馱與觀音》｜高雄中山堂劇場戶外陽光草坪｜2026-12-12 正戲 19:00 |  | approve：原文「12/12(六)水錦歌劇團《對面夫妻～韋馱與觀音》」，共用時間、地點、免費入場，星期相符。 | rejected badgeType-not-free |
| chg-011 | add | https://www.threads.com/@taiwaneseopera168/post/DfQ5lKaiQVF | 明華園星字戲劇團｜《斷案青天－陰錯陽差》｜高雄中山堂劇場戶外陽光草坪｜2026-12-13 正戲 19:00 |  | approve：原文「12/13(日)明華園星字戲劇團《斷案青天－陰錯陽差》」，共用時間、地點、免費入場，星期相符。 | rejected badgeType-not-free |
| chg-012 | add | https://www.threads.com/@jing__1017/post/DfR48oeiau2 | 小金枝歌劇團｜《棄老山傳奇》｜高雄中山堂劇場戶外陽光草坪｜2026-11-27 正戲 19:00 |  | reject：跟 chg-002 是同一場（11/27 小金枝《棄老山傳奇》高雄中山堂草坪 19:00），只是 jing__1017… | held  |
| chg-013 | add | https://www.threads.com/@jing__1017/post/DfR48oeiau2 | 新和興總團｜《秦英掛帥》｜高雄中山堂劇場戶外陽光草坪｜2026-11-28 正戲 19:00 |  | reject：跟 chg-003 是同一場（11/28 新和興總團《秦英掛帥》），只是另一個帳號轉貼，會重複建卡；來源應併進 chg… | held  |
| chg-014 | add | https://www.threads.com/@jing__1017/post/DfR48oeiau2 | 藝華園戲劇團｜《八仙傳奇－張果老與藍采和》｜高雄中山堂劇場戶外陽光草坪｜2026-11-29 正戲 19:00 |  | reject：跟 chg-004 是同一場（11/29 藝華園《八仙傳奇－張果老與藍采和》），會重複建卡；來源應併進 chg-004。 | held  |
| chg-015 | add | https://www.threads.com/@jing__1017/post/DfR48oeiau2 | 新藝芳歌劇團｜《金蟾緣》｜高雄中山堂劇場戶外陽光草坪｜2026-12-03 正戲 19:00 |  | reject：跟 chg-005 是同一場（12/03 新藝芳《金蟾緣》），會重複建卡；來源應併進 chg-005。 | held  |
| chg-016 | add | https://www.threads.com/@jing__1017/post/DfR48oeiau2 | 佩儀歌劇團｜《吳漢殺妻》｜高雄中山堂劇場戶外陽光草坪｜2026-12-04 正戲 19:00 |  | reject：跟 chg-006 是同一場（12/04 佩儀《吳漢殺妻》），會重複建卡；來源應併進 chg-006。 | held  |
| chg-017 | add | https://www.threads.com/@jing__1017/post/DfR48oeiau2 | 文惜歌仔戲劇團｜《焰火長槍：火帥與玉龍的背影》｜高雄中山堂劇場戶外陽光草坪｜2026-12-05 正戲 19:00 |  | reject：跟 chg-007 是同一場（12/05 文惜《焰火長槍》），會重複建卡；來源應併進 chg-007。 | held  |
| chg-018 | add | https://www.threads.com/@jing__1017/post/DfR48oeiau2 | 繡花園戲劇團｜《姜子牙下山》｜高雄中山堂劇場戶外陽光草坪｜2026-12-06 正戲 19:00 |  | reject：跟 chg-008 是同一場（12/06 繡花園《姜子牙下山》），會重複建卡；來源應併進 chg-008。 | held  |
| chg-019 | add | https://www.threads.com/@jing__1017/post/DfR48oeiau2 | 春明歌劇團｜《玉虛戰歌．天命之戰》｜高雄中山堂劇場戶外陽光草坪｜2026-12-11 正戲 19:00 |  | reject：跟 chg-009 是同一場（12/11 春明《玉虛戰歌．天命之戰》），會重複建卡；來源應併進 chg-009。 | held  |
| chg-020 | add | https://www.threads.com/@jing__1017/post/DfR48oeiau2 | 水錦歌劇團｜《對面夫妻～韋馱與觀音》｜高雄中山堂劇場戶外陽光草坪｜2026-12-12 正戲 19:00 |  | reject：跟 chg-010 是同一場（12/12 水錦《對面夫妻～韋馱與觀音》），會重複建卡；來源應併進 chg-010。 | held  |
| chg-021 | add | https://www.threads.com/@jing__1017/post/DfR48oeiau2 | 明華園星字戲劇團｜《斷案青天－陰錯陽差》｜高雄中山堂劇場戶外陽光草坪｜2026-12-13 正戲 19:00 |  | reject：跟 chg-011 是同一場（12/13 明華園星字《斷案青天－陰錯陽差》），會重複建卡；來源應併進 chg-011。 | held  |
| chg-022 | add | https://www.facebook.com/photo/?fbid=122315789156250015 | 小金枝歌劇團｜《棄老山傳奇》｜高雄中山堂劇場戶外陽光草坪｜2026-11-27 正戲 19:00 |  | reject：跟 chg-002（以及 chg-012）是同一場（11/27 小金枝《棄老山傳奇》），這是 Facebook 上同一… | held  |
| chg-023 | add | https://www.facebook.com/photo/?fbid=122315789156250015 | 新和興總團｜《秦英掛帥》｜高雄中山堂劇場戶外陽光草坪｜2026-11-28 正戲 19:00 |  | reject：跟 chg-003 是同一場（11/28 新和興《秦英掛帥》），FB 同一份公告，會重複建卡；來源應併進 chg-00… | held  |
| chg-024 | add | https://www.facebook.com/photo/?fbid=122315789156250015 | 藝華園戲劇團｜《八仙傳奇－張果老與藍采和》｜高雄中山堂劇場戶外陽光草坪｜2026-11-29 正戲 19:00 |  | reject：跟 chg-004 是同一場（11/29 藝華園《八仙傳奇》），會重複建卡；來源應併進 chg-004。 | held  |
| chg-025 | add | https://www.facebook.com/photo/?fbid=122315789156250015 | 新藝芳歌劇團｜《金蟾緣》｜高雄中山堂劇場戶外陽光草坪｜2026-12-03 正戲 19:00 |  | reject：跟 chg-005 是同一場（12/03 新藝芳《金蟾緣》），會重複建卡；來源應併進 chg-005。 | held  |
| chg-026 | add | https://www.facebook.com/photo/?fbid=122315789156250015 | 佩儀歌劇團｜《吳漢殺妻》｜高雄中山堂劇場戶外陽光草坪｜2026-12-04 正戲 19:00 |  | reject：跟 chg-006 是同一場（12/04 佩儀《吳漢殺妻》），會重複建卡；來源應併進 chg-006。 | held  |
| chg-027 | add | https://www.facebook.com/photo/?fbid=122315789156250015 | 文惜歌仔戲劇團｜《焰火長槍：火帥與玉龍的背影》｜高雄中山堂劇場戶外陽光草坪｜2026-12-05 正戲 19:00 |  | reject：跟 chg-007 是同一場（12/05 文惜《焰火長槍》），會重複建卡；來源應併進 chg-007。 | held  |
| chg-028 | add | https://www.facebook.com/photo/?fbid=122315789156250015 | 繡花園戲劇團｜《姜子牙下山》｜高雄中山堂劇場戶外陽光草坪｜2026-12-06 正戲 19:00 |  | reject：跟 chg-008 是同一場（12/06 繡花園《姜子牙下山》），會重複建卡；來源應併進 chg-008。 | held  |
| chg-029 | add | https://www.facebook.com/photo/?fbid=122315789156250015 | 春明歌劇團｜《玉虛戰歌．天命之戰》｜高雄中山堂劇場戶外陽光草坪｜2026-12-11 正戲 19:00 |  | reject：跟 chg-009 是同一場（12/11 春明《玉虛戰歌》），會重複建卡；來源應併進 chg-009。 | held  |
| chg-030 | add | https://www.facebook.com/photo/?fbid=122315789156250015 | 水錦歌劇團｜《對面夫妻～韋馱與觀音》｜高雄中山堂劇場戶外陽光草坪｜2026-12-12 正戲 19:00 |  | reject：跟 chg-010 是同一場（12/12 水錦《對面夫妻》），會重複建卡；來源應併進 chg-010。 | held  |
| chg-031 | add | https://www.facebook.com/photo/?fbid=122315789156250015 | 明華園星字戲劇團｜《斷案青天－陰錯陽差》｜高雄中山堂劇場戶外陽光草坪｜2026-12-13 正戲 19:00 |  | reject：跟 chg-011 是同一場（12/13 明華園星字《斷案青天》），會重複建卡；來源應併進 chg-011。 | held  |
| chg-032 | add | https://www.facebook.com/photo/?fbid=1690749119084639 | 明華園總團｜《劍神呂洞賓》｜北港1911好庫文化產業園區停車場｜2026-11-08 正戲 19:00 |  | approve：原文「11/8（日）雲林北港｜《劍神呂洞賓》」「11月8日（星期日）晚上7:00」「北港1911好庫文化產業園區停車場… | added  |
| chg-033 | add（查證成立） | https://taiwanpost.net/2026/lubaimedia/179261（原貼文 https://www.threads.com/@taiwaneseopera168/post/Dfb5YcOiYWE） | 明華園黃字戲劇團｜《三抄府》｜嘉義市北香湖廣場｜2026-11-08 正戲 19:00 |  | approve：臺灣郵報原文「11月8日（日）晚上7點明華園黃字戲劇團《三抄府》嘉義市北香湖廣場，免費入場」，跟 chg-001 的海… | added  |
| chg-034 | add（查證成立） | https://taiwanpost.net/2026/lubaimedia/179261（原貼文 https://www.threads.com/@taiwaneseopera168/post/Dfb5YcOiYWE） | 大地華園劇團｜《劉全進瓜》｜嘉義市北香湖廣場｜2026-11-13 正戲 19:00 |  | approve：原文「11月13日（五）晚上7點大地華園劇團《劉全進瓜》嘉義市北香湖廣場，免費入場」，星期相符，歌仔戲，schedul… | added  |
| chg-035 | add（查證成立） | https://taiwanpost.net/2026/lubaimedia/179261（原貼文 https://www.threads.com/@taiwaneseopera168/post/Dfb5YcOiYWE） | 明華園戲劇總團｜《貓神》｜嘉義舊燈會區—空軍市場｜2026-11-14 正戲 19:00 |  | approve：原文「11月14日晚上7點明華園戲劇總團《貓神》嘉義舊燈會區—空軍市場，免費入場」，地點跟北香湖分開列，沒有混淆，歌仔… | added  |
| chg-036 | add（查證成立） | https://www.opentix.life/event/2090269380048343041（原貼文 https://www.opentix.life/event/2090269380048343041） | 臺北木偶劇團｜戲釀青春──2026育成聯合展演《雷萬春打虎》｜臺灣戲曲中心小舞台（臺北市士林區文林路751號）｜2026-11-08 正戲 14:30 |  | needs-check：日期、時間、地點對得上 OPENTIX 原文「【小舞台】11/08（日）14:30 臺北木偶劇團《雷萬春打虎》」。疑點… | held  |
| chg-037 | add（查證成立） | https://www.opentix.life/event/2090269380048343041（原貼文 https://www.opentix.life/event/2090269380048343041） | 薪傳歌仔戲劇團｜戲釀青春──2026育成聯合展演《蒼原孤雁》｜臺灣戲曲中心小表演廳（臺北市士林區文林路751號）｜2026-11-14 正戲 14:30 |  | needs-check：原文「【小表演廳】11/14（六）14:30 薪傳歌仔戲劇團《蒼原孤雁》」，日期、時間、地點、劇團、劇目、劇種都對，s… | held  |

## 待查與退回

| 類別 | 貼文 | 原因 | 說明 |
| --- | --- | --- | --- |
| 漏處置 | facebook:mhysun:1649270353232516 | revision-mismatch |  |
| 漏處置 | facebook:mhysun:1649090029917215 | revision-mismatch |  |

## 遠期場次（超過 120 天，進入 120 天內自動重驗）

| 貼文 | 內容 |
| --- | --- |
| https://www.facebook.com/photo/?fbid=1560228489482771 | 明華園天字戲劇團｜《重返：愛河戀夢》｜臺灣戲曲中心 大表演廳｜2027-06-05、2027-06-06 |
| https://www.facebook.com/MingHuaYuanTianTaiwaneseOpera/reels_tab | 明華園天字戲劇團｜《重返：愛河戀夢》｜臺灣戲曲中心 大表演廳｜2027-06-05、2027-06-06 |
| https://www.threads.com/@taiwaneseopera168/post/DfWAAt6CT5a | 烏貓戲出｜《白賊七》｜高雄中山堂劇場(高雄市左營區實踐路71號)｜2027-04-17、2027-04-18 |
| https://www.threads.com/@taiwaneseopera168/post/DfWAAt6CT5a | 薪傳歌仔戲劇團｜《封神榜．文王食子》｜高雄中山堂劇場(高雄市左營區實踐路71號)｜2027-04-24、2027-04-25 |

## 紀錄檔

- 本輪狀態：/Users/eric/aiwork/taiwan-opera-calendar/patrol_state/runs/2026-11-08_0311/state.json
- 巡檢紀錄：patrol_runs/2026-11-08_0311.json（/Users/eric/aiwork/taiwan-opera-calendar）
- 證據：patrol_evidence/2026-11-08_0311/
- 產生時間：2026-11-08T03:51:44+08:00
