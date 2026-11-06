# 巡檢報告 2026-11-07_0311（patrol-v2，正式）

## 需要 Eric 決定

- 前幾天的巡檢沒有完成：2026-11-06：輪次 2026-11-06_0851 沒有跑完

## 結論

| 項目 | 結果 |
| --- | --- |
| 執行 | 開始 2026-11-07T03:11:33+08:00；結果 進行中；步驟 preflight:done、collect:done、pack:done、judge:done、check:done、verify:done、review:done、apply:done、publish:done、report:running |
| 來源 | 20 個：完整 2、部分 18、失敗 0、未讀 0 |
| 資料 | 送判讀 229 篇／圖 14 張；變更提案 40、確認一致 39、送查證 59（成立 5、與卡相同 4、查無佐證不收 52）、退回 0、漏處置 0；已過期不收 58、遠期暫存 4 |
| 寫入 | 寫入 1、add_card 拒絕 16、審查未通過 23 |
| 發布 | verified；SHA 3fe2998a88eb13e4456412e1bb930d6a85e3d44b；Actions 42283073221 |

## 模型與用量

| 角色 | 模型 | 依據 |
| --- | --- | --- |
| main | claude-sonnet-5-5 | get_session self：effort=medium |
| judge | sonnet | Agent 工具 model 參數；effort=medium |
| verify | opus | Agent 工具 model 參數；effort=medium |
| review | opus | Agent 工具 model 參數；effort=medium |

- 判讀批次 10；送出貼文 229 篇、圖片 14 張、正文約 76920 字
- 略過（已判讀未變動）132 篇；窗口外 21 篇
- 第二次審查：有（40 項）

## 來源

| 來源 | 狀態 | 範圍 | 說明 |
| --- | --- | --- | --- |
| threads:joe_huang_k_w | 部分 | 首屏 4 篇、累積 9 篇；最新 2026-11-06T18:32:27+08:00、最舊 2026-10-29T17:10:13+08:00；捲動 2 次、停止原因 reached-window；圖片下載 13 張 | 不變式通過；證據 /Users/eric/aiwork/taiwan-opera-calendar/patrol_evidence/2026-11-07_0311/threads_joe_huang… |
| threads:h.akito_1996 | 部分 | 首屏 4 篇、累積 9 篇；最新 2026-11-04T17:59:03+08:00、最舊 2026-09-27T00:04:33+08:00；捲動 2 次、停止原因 reached-window；圖片下載 6 張 | 不變式通過；證據 /Users/eric/aiwork/taiwan-opera-calendar/patrol_evidence/2026-11-07_0311/threads_h.akito_1… |
| threads:the_rin.lpm | 部分 | 首屏 4 篇、累積 7 篇；最新 2026-11-05T19:01:27+08:00、最舊 2026-09-26T14:32:03+08:00；捲動 2 次、停止原因 reached-window；圖片下載 8 張 | 不變式通過；證據 /Users/eric/aiwork/taiwan-opera-calendar/patrol_evidence/2026-11-07_0311/threads_the_rin.l… |
| threads:xuefeng_lu_ | 完整 | 7 天窗口讀完（停止原因 reached-window）；窗口內 5 篇皆有處置；圖片 0 張皆已判讀 | 不變式通過、逐篇處置完成 |
| threads:yuzhongluo | 部分 | 首屏 4 篇、累積 10 篇；最新 2026-11-06T20:36:15+08:00、最舊 2026-10-29T17:04:37+08:00；捲動 3 次、停止原因 reached-window；圖片下載 25 張 | 不變式通過；證據 /Users/eric/aiwork/taiwan-opera-calendar/patrol_evidence/2026-11-07_0311/threads_yuzhonglu… |
| threads:taiwaneseopera168 | 部分 | 首屏 4 篇、累積 41 篇；最新 2026-11-06T22:15:43+08:00、最舊 2026-08-16T02:33:12+08:00；捲動 20 次、停止原因 max-scrolls；圖片下載 66 張 | 不變式通過；證據 /Users/eric/aiwork/taiwan-opera-calendar/patrol_evidence/2026-11-07_0311/threads_taiwanese… |
| threads:jing__1017 | 部分 | 首屏 4 篇、累積 35 篇；最新 2026-11-06T20:49:51+08:00、最舊 2026-10-28T19:50:21+08:00；捲動 15 次、停止原因 no-new-after-3；圖片下載 40 張 | 不變式通過；證據 /Users/eric/aiwork/taiwan-opera-calendar/patrol_evidence/2026-11-07_0311/threads_jing__101… |
| threads:hilang.on.tour | 完整 | 7 天窗口讀完（停止原因 reached-window）；窗口內 0 篇皆有處置；圖片 0 張皆已判讀 | 不變式通過、逐篇處置完成 |
| threads:yolin1991 | 部分 | 首屏 4 篇、累積 9 篇；最新 2026-11-06T12:51:58+08:00、最舊 2026-10-28T18:34:21+08:00；捲動 3 次、停止原因 reached-window；圖片下載 9 張 | 不變式通過；證據 /Users/eric/aiwork/taiwan-opera-calendar/patrol_evidence/2026-11-07_0311/threads_yolin1991… |
| facebook:sunhope.fans | 部分 | 首屏 2 篇、累積 19 篇；最新 無、最舊 無；捲動 20 次、停止原因 max-scrolls；圖片下載 25 張 | 不變式通過；證據 /Users/eric/aiwork/taiwan-opera-calendar/patrol_evidence/2026-11-07_0311/facebook_sunhope.… |
| facebook:HsiaoHsiYuan1913 | 部分 | 首屏 3 篇、累積 23 篇；最新 無、最舊 無；捲動 20 次、停止原因 max-scrolls；圖片下載 38 張 | 不變式通過；證據 /Users/eric/aiwork/taiwan-opera-calendar/patrol_evidence/2026-11-07_0311/facebook_HsiaoHsi… |
| facebook:100063868113954 | 部分 | 首屏 2 篇、累積 21 篇；最新 無、最舊 無；捲動 20 次、停止原因 max-scrolls；圖片下載 48 張 | 不變式通過；證據 /Users/eric/aiwork/taiwan-opera-calendar/patrol_evidence/2026-11-07_0311/facebook_10006386… |
| facebook:MingHuaYuanTianTaiwaneseOpera | 部分 | 首屏 1 篇、累積 23 篇；最新 無、最舊 無；捲動 20 次、停止原因 max-scrolls；圖片下載 61 張 | 不變式通過；證據 /Users/eric/aiwork/taiwan-opera-calendar/patrol_evidence/2026-11-07_0311/facebook_MingHuaY… |
| facebook:61574134933376 | 部分 | 首屏 2 篇、累積 19 篇；最新 無、最舊 無；捲動 20 次、停止原因 max-scrolls；圖片下載 34 張 | 不變式通過；證據 /Users/eric/aiwork/taiwan-opera-calendar/patrol_evidence/2026-11-07_0311/facebook_61574134… |
| facebook:mhysun | 部分 | 首屏 1 篇、累積 19 篇；最新 無、最舊 無；捲動 20 次、停止原因 max-scrolls；圖片下載 84 張 | 不變式通過；證據 /Users/eric/aiwork/taiwan-opera-calendar/patrol_evidence/2026-11-07_0311/facebook_mhysun.j… |
| facebook:61594936681482 | 部分 | 首屏 1 篇、累積 7 篇；最新 無、最舊 無；捲動 7 次、停止原因 no-new-after-3；圖片下載 23 張 | 不變式通過；證據 /Users/eric/aiwork/taiwan-opera-calendar/patrol_evidence/2026-11-07_0311/facebook_61594936… |
| facebook:lanyang.opera | 部分 | 首屏 1 篇、累積 22 篇；最新 無、最舊 無；捲動 20 次、停止原因 max-scrolls；圖片下載 39 張 | 不變式通過；證據 /Users/eric/aiwork/taiwan-opera-calendar/patrol_evidence/2026-11-07_0311/facebook_lanyang.… |
| facebook:Taichungpuppettheater | 部分 | 首屏 1 篇、累積 26 篇；最新 無、最舊 無；捲動 20 次、停止原因 max-scrolls；圖片下載 47 張 | 不變式通過；證據 /Users/eric/aiwork/taiwan-opera-calendar/patrol_evidence/2026-11-07_0311/facebook_Taichung… |
| culture | 部分 | total 1335、fetchedAt 2026-11-06T11:02:19+08:00、戲曲紀錄 27 筆 | 資料新鮮；逐筆處置待判讀後確認 |
| issues | 部分 | state=all 共 3 則（含留言） | 已讀取；處置待判讀後確認 |

- OPENTIX：sitemap 864 個活動、本輪有變 658、抓取 250、戲曲相關且未過期 42、延後 408、錯誤 0

## 卡片變更

| 編號 | 動作 | 來源 | 內容 | 差異 | 審查 | 寫入 |
| --- | --- | --- | --- | --- | --- | --- |
| chg-001 | add | https://www.threads.com/@taiwaneseopera168/post/DfZcD7ciVYP | 明華園黃字戲劇團｜《三抄府》｜嘉義市北香湖廣場｜2026-11-08 正戲 19:00 |  | approve：原文「明華園黃字戲劇團 🪭戲碼：《三抄府》 ⏰️11/8(日) 19:00 嘉義市北香湖廣場」與海報「11/08 19… | rejected artist-not-in-quote |
| chg-002 | add | https://www.threads.com/@taiwaneseopera168/post/DfWONmSCdfQ | 明華園天字戲劇團｜《喜脈緣》｜成功大學校園(歷史系館前方小廣場)｜2026-11-24 正戲 19:00 |  | approve：戲路表圖 11/24 列「成功大學95週年校慶活動 明華園天字戲劇團-《喜脈緣》 18:15開放進場 19:00正式開… | added  |
| chg-003 | add | https://www.threads.com/@taiwaneseopera168/post/DfWAAt6CT5a | 後場作戲｜出塵入凡—陳芸楚小旦專場｜高雄中山堂劇場｜2027-03-06 正戲 14:30、2027-03-07 正戲 14:30 |  | needs-check：日期、時間、地點與海報「3/6 Sat. 14:30 3/7 Sun. 14:30 高雄中山堂劇場」相符；但原文說此系… | held  |
| chg-004 | add | https://www.threads.com/@taiwaneseopera168/post/DfQ5lKaiQVF | 小金枝歌劇團｜《棄老山傳奇》｜高雄中山堂劇場戶外陽光草坪｜2026-11-27 正戲 19:00 |  | approve：原文「11/27(五)小金枝歌劇團《棄老山傳奇》」「每場次開演時間｜19:00」「演出地點｜高雄中山堂劇場戶外陽光草坪… | rejected badgeType-not-free |
| chg-005 | add | https://www.threads.com/@taiwaneseopera168/post/DfQ5lKaiQVF | 新和興總團｜《秦英掛帥》｜高雄中山堂劇場戶外陽光草坪｜2026-11-28 正戲 19:00 |  | approve：原文「11/28(六)新和興總團《秦英掛帥》」，19:00、高雄中山堂劇場戶外陽光草坪、免費入場皆出自原文；無既有卡。… | rejected badgeType-not-free |
| chg-006 | add | https://www.threads.com/@taiwaneseopera168/post/DfQ5lKaiQVF | 藝華園戲劇團｜《八仙傳奇－張果老與藍采和》｜高雄中山堂劇場戶外陽光草坪｜2026-11-29 正戲 19:00 |  | approve：原文「11/29(日)藝華園戲劇團《八仙傳奇－張果老與藍采和》」，時間地點同系列統一說明；無既有卡。chg-016、c… | rejected badgeType-not-free |
| chg-007 | add | https://www.threads.com/@taiwaneseopera168/post/DfQ5lKaiQVF | 新藝芳歌劇團｜《金蟾緣》｜高雄中山堂劇場戶外陽光草坪｜2026-12-03 正戲 19:00 |  | approve：原文「12/03(四)新藝芳歌劇團《金蟾緣》」，19:00、高雄中山堂劇場戶外陽光草坪；無既有卡。chg-017、ch… | rejected badgeType-not-free |
| chg-008 | add | https://www.threads.com/@taiwaneseopera168/post/DfQ5lKaiQVF | 佩儀歌劇團｜《吳漢殺妻》｜高雄中山堂劇場戶外陽光草坪｜2026-12-04 正戲 19:00 |  | approve：原文「12/04(五)佩儀歌劇團《吳漢殺妻》」，19:00、同地點；無既有卡。chg-018、chg-028 為同場重… | rejected badgeType-not-free |
| chg-009 | add | https://www.threads.com/@taiwaneseopera168/post/DfQ5lKaiQVF | 文惜歌仔戲劇團｜《焰火長槍：火帥與玉龍的背影》｜高雄中山堂劇場戶外陽光草坪｜2026-12-05 正戲 19:00 |  | approve：原文「12/05(六)文惜歌仔戲劇團《焰火長槍：火帥與玉龍的背影》」，19:00、同地點；無既有卡。chg-019、c… | rejected badgeType-not-free |
| chg-010 | add | https://www.threads.com/@taiwaneseopera168/post/DfQ5lKaiQVF | 繡花園戲劇團｜《姜子牙下山》｜高雄中山堂劇場戶外陽光草坪｜2026-12-06 正戲 19:00 |  | approve：原文「12/06(日)繡花園戲劇團《姜子牙下山》」，19:00、同地點；無既有卡。chg-020、chg-030 為同… | rejected badgeType-not-free |
| chg-011 | add | https://www.threads.com/@taiwaneseopera168/post/DfQ5lKaiQVF | 春明歌劇團｜《玉虛戰歌．天命之戰》｜高雄中山堂劇場戶外陽光草坪｜2026-12-11 正戲 19:00 |  | approve：原文「12/11(五)春明歌劇團《玉虛戰歌．天命之戰》」，19:00、同地點；無既有卡。chg-021、chg-031… | rejected badgeType-not-free |
| chg-012 | add | https://www.threads.com/@taiwaneseopera168/post/DfQ5lKaiQVF | 水錦歌劇團｜《對面夫妻～韋馱與觀音》｜高雄中山堂劇場戶外陽光草坪｜2026-12-12 正戲 19:00 |  | approve：原文「12/12(六)水錦歌劇團《對面夫妻～韋馱與觀音》」，19:00、同地點；無既有卡。chg-022、chg-03… | rejected badgeType-not-free |
| chg-013 | add | https://www.threads.com/@taiwaneseopera168/post/DfQ5lKaiQVF | 明華園星字戲劇團｜《斷案青天－陰錯陽差》｜高雄中山堂劇場戶外陽光草坪｜2026-12-13 正戲 19:00 |  | approve：原文「12/13(日)明華園星字戲劇團《斷案青天－陰錯陽差》」，19:00、同地點；無既有卡。chg-023、chg-… | rejected badgeType-not-free |
| chg-014 | add | https://www.threads.com/@jing__1017/post/DfR48oeiau2 | 小金枝歌劇團｜《棄老山傳奇》｜高雄中山堂劇場戶外陽光草坪｜2026-11-27 正戲 19:00 |  | reject：重複建卡：jing__1017 轉貼同一則「外臺歌仔戲2.0交流匯演」，劇團、劇目、日期 11/27、地點與 chg-… | held  |
| chg-015 | add | https://www.threads.com/@jing__1017/post/DfR48oeiau2 | 新和興總團｜《秦英掛帥》｜高雄中山堂劇場戶外陽光草坪｜2026-11-28 正戲 19:00 |  | reject：重複建卡：與 chg-005（11/28 新和興總團《秦英掛帥》高雄中山堂戶外陽光草坪）同場，應併為補充來源。 | held  |
| chg-016 | add | https://www.threads.com/@jing__1017/post/DfR48oeiau2 | 藝華園戲劇團｜《八仙傳奇－張果老與藍采和》｜高雄中山堂劇場戶外陽光草坪｜2026-11-29 正戲 19:00 |  | reject：重複建卡：與 chg-006（11/29 藝華園戲劇團《八仙傳奇－張果老與藍采和》）同場，應併為補充來源。 | held  |
| chg-017 | add | https://www.threads.com/@jing__1017/post/DfR48oeiau2 | 新藝芳歌劇團｜《金蟾緣》｜高雄中山堂劇場戶外陽光草坪｜2026-12-03 正戲 19:00 |  | reject：重複建卡：與 chg-007（12/03 新藝芳歌劇團《金蟾緣》）同場，應併為補充來源。 | held  |
| chg-018 | add | https://www.threads.com/@jing__1017/post/DfR48oeiau2 | 佩儀歌劇團｜《吳漢殺妻》｜高雄中山堂劇場戶外陽光草坪｜2026-12-04 正戲 19:00 |  | reject：重複建卡：與 chg-008（12/04 佩儀歌劇團《吳漢殺妻》）同場，應併為補充來源。 | held  |
| chg-019 | add | https://www.threads.com/@jing__1017/post/DfR48oeiau2 | 文惜歌仔戲劇團｜《焰火長槍：火帥與玉龍的背影》｜高雄中山堂劇場戶外陽光草坪｜2026-12-05 正戲 19:00 |  | reject：重複建卡：與 chg-009（12/05 文惜歌仔戲劇團《焰火長槍》）同場，應併為補充來源。 | held  |
| chg-020 | add | https://www.threads.com/@jing__1017/post/DfR48oeiau2 | 繡花園戲劇團｜《姜子牙下山》｜高雄中山堂劇場戶外陽光草坪｜2026-12-06 正戲 19:00 |  | reject：重複建卡：與 chg-010（12/06 繡花園戲劇團《姜子牙下山》）同場，應併為補充來源。 | held  |
| chg-021 | add | https://www.threads.com/@jing__1017/post/DfR48oeiau2 | 春明歌劇團｜《玉虛戰歌．天命之戰》｜高雄中山堂劇場戶外陽光草坪｜2026-12-11 正戲 19:00 |  | reject：重複建卡：與 chg-011（12/11 春明歌劇團《玉虛戰歌．天命之戰》）同場，應併為補充來源。 | held  |
| chg-022 | add | https://www.threads.com/@jing__1017/post/DfR48oeiau2 | 水錦歌劇團｜《對面夫妻～韋馱與觀音》｜高雄中山堂劇場戶外陽光草坪｜2026-12-12 正戲 19:00 |  | reject：重複建卡：與 chg-012（12/12 水錦歌劇團《對面夫妻～韋馱與觀音》）同場，應併為補充來源。 | held  |
| chg-023 | add | https://www.threads.com/@jing__1017/post/DfR48oeiau2 | 明華園星字戲劇團｜《斷案青天－陰錯陽差》｜高雄中山堂劇場戶外陽光草坪｜2026-12-13 正戲 19:00 |  | reject：重複建卡：與 chg-013（12/13 明華園星字戲劇團《斷案青天－陰錯陽差》）同場，應併為補充來源。 | held  |
| chg-024 | add | https://www.facebook.com/photo/?fbid=122315789156250015 | 小金枝歌劇團｜《棄老山傳奇》｜高雄中山堂劇場戶外陽光草坪｜2026-11-27 正戲 19:00 |  | reject：重複建卡：Facebook 同一則匯演公告（fbid=122315789156250015），與 chg-004（11… | held  |
| chg-025 | add | https://www.facebook.com/photo/?fbid=122315789156250015 | 新和興總團｜《秦英掛帥》｜高雄中山堂劇場戶外陽光草坪｜2026-11-28 正戲 19:00 |  | reject：重複建卡：與 chg-005（11/28 新和興總團《秦英掛帥》）同場，應併為補充來源。 | held  |
| chg-026 | add | https://www.facebook.com/photo/?fbid=122315789156250015 | 藝華園戲劇團｜《八仙傳奇－張果老與藍采和》｜高雄中山堂劇場戶外陽光草坪｜2026-11-29 正戲 19:00 |  | reject：重複建卡：與 chg-006（11/29 藝華園戲劇團）同場，應併為補充來源。 | held  |
| chg-027 | add | https://www.facebook.com/photo/?fbid=122315789156250015 | 新藝芳歌劇團｜《金蟾緣》｜高雄中山堂劇場戶外陽光草坪｜2026-12-03 正戲 19:00 |  | reject：重複建卡：與 chg-007（12/03 新藝芳歌劇團）同場，應併為補充來源。 | held  |
| chg-028 | add | https://www.facebook.com/photo/?fbid=122315789156250015 | 佩儀歌劇團｜《吳漢殺妻》｜高雄中山堂劇場戶外陽光草坪｜2026-12-04 正戲 19:00 |  | reject：重複建卡：與 chg-008（12/04 佩儀歌劇團）同場，應併為補充來源。 | held  |
| chg-029 | add | https://www.facebook.com/photo/?fbid=122315789156250015 | 文惜歌仔戲劇團｜《焰火長槍：火帥與玉龍的背影》｜高雄中山堂劇場戶外陽光草坪｜2026-12-05 正戲 19:00 |  | reject：重複建卡：與 chg-009（12/05 文惜歌仔戲劇團）同場，應併為補充來源。 | held  |
| chg-030 | add | https://www.facebook.com/photo/?fbid=122315789156250015 | 繡花園戲劇團｜《姜子牙下山》｜高雄中山堂劇場戶外陽光草坪｜2026-12-06 正戲 19:00 |  | reject：重複建卡：與 chg-010（12/06 繡花園戲劇團）同場，應併為補充來源。 | held  |
| chg-031 | add | https://www.facebook.com/photo/?fbid=122315789156250015 | 春明歌劇團｜《玉虛戰歌．天命之戰》｜高雄中山堂劇場戶外陽光草坪｜2026-12-11 正戲 19:00 |  | reject：重複建卡：與 chg-011（12/11 春明歌劇團）同場，應併為補充來源。 | held  |
| chg-032 | add | https://www.facebook.com/photo/?fbid=122315789156250015 | 水錦歌劇團｜《對面夫妻～韋馱與觀音》｜高雄中山堂劇場戶外陽光草坪｜2026-12-12 正戲 19:00 |  | reject：重複建卡：與 chg-012（12/12 水錦歌劇團）同場，應併為補充來源。 | held  |
| chg-033 | add | https://www.facebook.com/photo/?fbid=122315789156250015 | 明華園星字戲劇團｜《斷案青天－陰錯陽差》｜高雄中山堂劇場戶外陽光草坪｜2026-12-13 正戲 19:00 |  | reject：重複建卡：與 chg-013（12/13 明華園星字戲劇團）同場，應併為補充來源。 | held  |
| chg-034 | add | https://www.facebook.com/mhysun/reels_tab | 明華園總團｜《獅子王》｜桃園市龍潭運動公園｜2026-11-07 正戲 19:00 |  | approve：孫翠鳳官方貼文「11/7（六）桃園龍潭｜《獅子王》」「11月7日（星期六）晚上7:00」「桃園市龍潭運動公園」「免費入… | rejected artist-not-in-quote,badgeType-not-free |
| chg-035 | add | https://www.facebook.com/mhysun/reels_tab | 明華園總團｜《劍神呂洞賓》｜北港1911好庫文化產業園區停車場｜2026-11-08 正戲 19:00 |  | approve：同貼文「11/8（日）雲林北港｜《劍神呂洞賓》」「11月8日（星期日）晚上7:00」「北港1911好庫文化產業園區停車… | rejected artist-not-in-quote |
| chg-036 | change（由「一致」轉）（查證成立） | https://culture.tainan.gov.tw/act_month/Details?Parser=99,5,44,,,,25429（原貼文 https://www.threads.com/@joe_huang_k_w/post/DfQ7AS6CdKQ） | 古都木偶戲劇團｜《臺灣風雲錄-戰火波瀾》｜【大內區】大內國小｜2026-11-07 正戲 19:00 | location：卡 臺南市大內區大內國小 → 文 【大內區】大內國小 | reject：confirm 轉 change，唯一 diff 是 location「臺南市大內區大內國小」→「【大內區】大內國小」… | held  |
| chg-037 | change（查證成立） | https://n.yam.com/Article/20261026226244（原貼文 https://www.threads.com/@the_rin.lpm/post/DfUZMCME7Ac） | 秀琴歌劇團｜《玉石變》｜莊泰路、國營路口總醮壇（新莊保元宮建醮）｜2026-11-07 扮仙 18:30、2026-11-07 正戲 19:00 | time：卡 19:00 → 文 2026-11-07 扮仙 18:30；location：卡 新北市新莊區中正路143號（保元宮） → 文 莊泰路、國營路口總醮壇（新莊保元宮建醮） | approve：蕃新聞引廟方「保元藝文醮」官方海報：「同一天的總醮壇，則由秀琴歌劇團演出。18:30至19:00是扮仙戲《大五福三仙大… | rejected location-not-in-quote |
| chg-038 | add（查證成立） | https://www.opentix.life/event/2090269380048343041（原貼文 https://www.opentix.life/event/2090269380048343041） | 一心戲劇團｜戲釀青春──2026育成聯合展演：一心戲劇團 經典折子《借扇》、《秀嬋申冤》、《虹霓關》｜臺灣戲曲中心小表演廳（臺北市士林區文林路751號）｜2026-11-07 正戲 14:30 |  | approve：OPENTIX 主辦頁「【小表演廳】 11/07（六）14:30 一心戲劇團 經典折子《借扇》、《秀嬋申冤》、《虹霓關… | rejected location-not-in-quote,title-not-in-quote,badgeType-not-ticket |
| chg-039 | add（查證成立） | https://www.opentix.life/event/2090269380048343041（原貼文 https://www.opentix.life/event/2090269380048343041） | 臺北木偶劇團｜戲釀青春──2026育成聯合展演：臺北木偶劇團《雷萬春打虎》｜臺灣戲曲中心小舞台（臺北市士林區文林路751號）｜2026-11-08 正戲 14:30 |  | needs-check：OPENTIX「【小舞台】11/08（日）14:30 臺北木偶劇團《雷萬春打虎》」日期時間地點正確且無既有卡；但原文未… | held  |
| chg-040 | add（查證成立） | https://www.opentix.life/event/2090269380048343041（原貼文 https://www.opentix.life/event/2090269380048343041） | 薪傳歌仔戲劇團｜戲釀青春──2026育成聯合展演：薪傳歌仔戲劇團《蒼原孤雁》｜臺灣戲曲中心小表演廳（臺北市士林區文林路751號）｜2026-11-14 正戲 14:30 |  | approve：OPENTIX「【小表演廳】11/14（六）14:30 薪傳歌仔戲劇團《蒼原孤雁》」，日期、時間、廳別、劇團劇目正確；… | rejected location-not-in-quote,title-not-in-quote,badgeType-not-ticket |

## 遠期場次（超過 120 天，進入 120 天內自動重驗）

| 貼文 | 內容 |
| --- | --- |
| https://www.facebook.com/photo/?fbid=1560228489482771 | 明華園天字戲劇團｜《重返：愛河戀夢》｜臺灣戲曲中心 大表演廳｜2027-06-05、2027-06-06 |
| https://www.facebook.com/MingHuaYuanTianTaiwaneseOpera/reels_tab | 明華園天字戲劇團｜《重返：愛河戀夢》｜臺灣戲曲中心 大表演廳｜2027-06-05、2027-06-06 |
| https://www.threads.com/@taiwaneseopera168/post/DfWAAt6CT5a | 烏貓戲出｜《白賊七》｜高雄中山堂劇場(高雄市左營區實踐路71號)｜2027-04-17、2027-04-18 |
| https://www.threads.com/@taiwaneseopera168/post/DfWAAt6CT5a | 薪傳歌仔戲劇團｜《封神榜．文王食子》｜高雄中山堂劇場(高雄市左營區實踐路71號)｜2027-04-24、2027-04-25 |

## 紀錄檔

- 本輪狀態：/Users/eric/aiwork/taiwan-opera-calendar/patrol_state/runs/2026-11-07_0311/state.json
- 巡檢紀錄：patrol_runs/2026-11-07_0311.json（/Users/eric/aiwork/taiwan-opera-calendar）
- 證據：patrol_evidence/2026-11-07_0311/
- 產生時間：2026-11-07T03:50:26+08:00
