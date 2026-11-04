# 巡檢報告 2026-11-04_2245（patrol-v2，正式）

## 需要 Eric 決定

- 判讀有 3 篇沒有逐篇處置，已列待查（見報告）

## 結論

| 項目 | 結果 |
| --- | --- |
| 執行 | 開始 2026-11-04T22:45:06+08:00；結果 進行中；步驟 preflight:done、collect:done、pack:done、judge:done、check:done、verify:done、review:done、apply:done、publish:done、report:running |
| 來源 | 20 個：完整 2、部分 18、失敗 0、未讀 0 |
| 資料 | 送判讀 244 篇／圖 13 張；變更提案 39、確認一致 36、送查證 55（成立 8、與卡相同 9、查無佐證不收 42）、退回 0、漏處置 3；已過期不收 80、遠期暫存 2 |
| 寫入 | 寫入 1、add_card 拒絕 15、審查未通過 23 |
| 發布 | verified；SHA 32beac3d741e2bd780c938a4f410a6dac6ddae8e；Actions 41856878668 |

## 模型與用量

| 角色 | 模型 | 依據 |
| --- | --- | --- |
| main | claude-sonnet-5-5 | get_session self：effort=medium |
| judge | sonnet | Agent 工具 model 參數；effort=medium |
| verify | opus | Agent 工具 model 參數；effort=medium |
| review | opus | Agent 工具 model 參數；effort=medium |

- 判讀批次 10；送出貼文 244 篇、圖片 13 張、正文約 79283 字
- 略過（已判讀未變動）122 篇；窗口外 20 篇
- 第二次審查：有（39 項）

## 來源

| 來源 | 狀態 | 範圍 | 說明 |
| --- | --- | --- | --- |
| threads:joe_huang_k_w | 部分 | 首屏 5 篇、累積 8 篇；最新 2026-11-03T21:56:59+08:00、最舊 2026-10-26T21:28:30+08:00；捲動 1 次、停止原因 reached-window；圖片下載 13 張 | 不變式通過；證據 /Users/eric/aiwork/taiwan-opera-calendar/patrol_evidence/2026-11-04_2245/threads_joe_huang… |
| threads:h.akito_1996 | 部分 | 首屏 4 篇、累積 10 篇；最新 2026-11-04T17:59:03+08:00、最舊 2026-09-27T00:04:33+08:00；捲動 3 次、停止原因 reached-window；圖片下載 9 張 | 不變式通過；證據 /Users/eric/aiwork/taiwan-opera-calendar/patrol_evidence/2026-11-04_2245/threads_h.akito_1… |
| threads:the_rin.lpm | 部分 | 首屏 4 篇、累積 7 篇；最新 2026-11-04T19:56:52+08:00、最舊 2026-09-26T14:32:03+08:00；捲動 2 次、停止原因 reached-window；圖片下載 8 張 | 不變式通過；證據 /Users/eric/aiwork/taiwan-opera-calendar/patrol_evidence/2026-11-04_2245/threads_the_rin.l… |
| threads:xuefeng_lu_ | 完整 | 7 天窗口讀完（停止原因 reached-window）；窗口內 5 篇皆有處置；圖片 0 張皆已判讀 | 不變式通過、逐篇處置完成 |
| threads:yuzhongluo | 部分 | 首屏 4 篇、累積 13 篇；最新 2026-11-04T13:27:13+08:00、最舊 2026-10-28T01:48:13+08:00；捲動 5 次、停止原因 reached-window；圖片下載 28 張 | 不變式通過；證據 /Users/eric/aiwork/taiwan-opera-calendar/patrol_evidence/2026-11-04_2245/threads_yuzhonglu… |
| threads:taiwaneseopera168 | 部分 | 首屏 5 篇、累積 40 篇；最新 2026-11-04T19:44:04+08:00、最舊 2026-08-16T02:33:12+08:00；捲動 20 次、停止原因 max-scrolls；圖片下載 33 張 | 不變式通過；證據 /Users/eric/aiwork/taiwan-opera-calendar/patrol_evidence/2026-11-04_2245/threads_taiwanese… |
| threads:jing__1017 | 部分 | 首屏 6 篇、累積 48 篇；最新 2026-11-04T22:07:26+08:00、最舊 2026-10-28T19:50:21+08:00；捲動 20 次、停止原因 max-scrolls；圖片下載 40 張 | 不變式通過；證據 /Users/eric/aiwork/taiwan-opera-calendar/patrol_evidence/2026-11-04_2245/threads_jing__101… |
| threads:hilang.on.tour | 完整 | 7 天窗口讀完（停止原因 reached-window）；窗口內 0 篇皆有處置；圖片 0 張皆已判讀 | 不變式通過、逐篇處置完成 |
| threads:yolin1991 | 部分 | 首屏 4 篇、累積 7 篇；最新 2026-11-04T17:09:46+08:00、最舊 2026-10-28T18:34:21+08:00；捲動 2 次、停止原因 reached-window；圖片下載 7 張 | 不變式通過；證據 /Users/eric/aiwork/taiwan-opera-calendar/patrol_evidence/2026-11-04_2245/threads_yolin1991… |
| facebook:sunhope.fans | 部分 | 首屏 3 篇、累積 21 篇；最新 無、最舊 無；捲動 20 次、停止原因 max-scrolls；圖片下載 27 張 | 不變式通過；證據 /Users/eric/aiwork/taiwan-opera-calendar/patrol_evidence/2026-11-04_2245/facebook_sunhope.… |
| facebook:HsiaoHsiYuan1913 | 部分 | 首屏 1 篇、累積 24 篇；最新 無、最舊 無；捲動 20 次、停止原因 max-scrolls；圖片下載 50 張 | 不變式通過；證據 /Users/eric/aiwork/taiwan-opera-calendar/patrol_evidence/2026-11-04_2245/facebook_HsiaoHsi… |
| facebook:100063868113954 | 部分 | 首屏 1 篇、累積 22 篇；最新 無、最舊 無；捲動 20 次、停止原因 max-scrolls；圖片下載 60 張 | 不變式通過；證據 /Users/eric/aiwork/taiwan-opera-calendar/patrol_evidence/2026-11-04_2245/facebook_10006386… |
| facebook:MingHuaYuanTianTaiwaneseOpera | 部分 | 首屏 1 篇、累積 22 篇；最新 無、最舊 無；捲動 20 次、停止原因 max-scrolls；圖片下載 65 張 | 不變式通過；證據 /Users/eric/aiwork/taiwan-opera-calendar/patrol_evidence/2026-11-04_2245/facebook_MingHuaY… |
| facebook:61574134933376 | 部分 | 首屏 2 篇、累積 19 篇；最新 無、最舊 無；捲動 20 次、停止原因 max-scrolls；圖片下載 34 張 | 不變式通過；證據 /Users/eric/aiwork/taiwan-opera-calendar/patrol_evidence/2026-11-04_2245/facebook_61574134… |
| facebook:mhysun | 部分 | 首屏 1 篇、累積 19 篇；最新 無、最舊 無；捲動 20 次、停止原因 max-scrolls；圖片下載 83 張 | 不變式通過；證據 /Users/eric/aiwork/taiwan-opera-calendar/patrol_evidence/2026-11-04_2245/facebook_mhysun.j… |
| facebook:61594936681482 | 部分 | 首屏 1 篇、累積 7 篇；最新 無、最舊 無；捲動 7 次、停止原因 no-new-after-3；圖片下載 23 張 | 不變式通過；證據 /Users/eric/aiwork/taiwan-opera-calendar/patrol_evidence/2026-11-04_2245/facebook_61594936… |
| facebook:lanyang.opera | 部分 | 首屏 1 篇、累積 22 篇；最新 無、最舊 無；捲動 20 次、停止原因 max-scrolls；圖片下載 39 張 | 不變式通過；證據 /Users/eric/aiwork/taiwan-opera-calendar/patrol_evidence/2026-11-04_2245/facebook_lanyang.… |
| facebook:Taichungpuppettheater | 部分 | 首屏 4 篇、累積 25 篇；最新 無、最舊 無；捲動 20 次、停止原因 max-scrolls；圖片下載 28 張 | 不變式通過；證據 /Users/eric/aiwork/taiwan-opera-calendar/patrol_evidence/2026-11-04_2245/facebook_Taichung… |
| culture | 部分 | total 1316、fetchedAt 2026-11-04T10:51:44+08:00、戲曲紀錄 27 筆 | 資料新鮮；逐筆處置待判讀後確認 |
| issues | 部分 | state=all 共 3 則（含留言） | 已讀取；處置待判讀後確認 |

- OPENTIX：sitemap 854 個活動、本輪有變 709、抓取 250、戲曲相關且未過期 31、延後 459、錯誤 0

## 卡片變更

| 編號 | 動作 | 來源 | 內容 | 差異 | 審查 | 寫入 |
| --- | --- | --- | --- | --- | --- | --- |
| chg-001 | update | https://www.threads.com/@taiwaneseopera168/post/DfUYCCIiUBU | 明華園天字戲劇團｜《真假皇后》｜澎湖石泉朱王廟｜2026-11-04 正戲 未公布 |  | reject：artist 填「孫詩雯」不成立：原文說孫詩雯是在「2024年由明華園黃字戲劇團」的售票公演中「飾演張紅瑩」，沒有說她… | held  |
| chg-002 | add | https://www.threads.com/@taiwaneseopera168/post/DfQ5lKaiQVF | 小金枝歌劇團｜《棄老山傳奇》｜高雄中山堂劇場戶外陽光草坪｜2026-11-27 正戲 19:00 |  | approve：原文「11/27(五)小金枝歌劇團《棄老山傳奇》」「每場次開演時間｜19:00」「高雄中山堂劇場戶外陽光草坪」「免費入… | rejected badgeType-not-free |
| chg-003 | add | https://www.threads.com/@taiwaneseopera168/post/DfQ5lKaiQVF | 新和興總團｜《秦英掛帥》｜高雄中山堂劇場戶外陽光草坪｜2026-11-28 正戲 19:00 |  | approve：原文「11/28(六)新和興總團《秦英掛帥》」，統一開演 19:00，地點和免費入場都對。chg-013、chg-02… | rejected badgeType-not-free |
| chg-004 | add | https://www.threads.com/@taiwaneseopera168/post/DfQ5lKaiQVF | 藝華園戲劇團｜《八仙傳奇－張果老與藍采和》｜高雄中山堂劇場戶外陽光草坪｜2026-11-29 正戲 19:00 |  | approve：原文「11/29(日)藝華園戲劇團《八仙傳奇－張果老與藍采和》」，19:00，地點正確。chg-014、chg-024… | rejected badgeType-not-free |
| chg-005 | add | https://www.threads.com/@taiwaneseopera168/post/DfQ5lKaiQVF | 新藝芳歌劇團｜《金蟾緣》｜高雄中山堂劇場戶外陽光草坪｜2026-12-03 正戲 19:00 |  | approve：原文「12/03(四)新藝芳歌劇團《金蟾緣》」，19:00，地點正確。chg-015、chg-025 與這筆重複。 | rejected badgeType-not-free |
| chg-006 | add | https://www.threads.com/@taiwaneseopera168/post/DfQ5lKaiQVF | 佩儀歌劇團｜《吳漢殺妻》｜高雄中山堂劇場戶外陽光草坪｜2026-12-04 正戲 19:00 |  | approve：原文「12/04(五)佩儀歌劇團《吳漢殺妻》」，19:00，地點正確。chg-016、chg-026 與這筆重複。 | rejected badgeType-not-free |
| chg-007 | add | https://www.threads.com/@taiwaneseopera168/post/DfQ5lKaiQVF | 文惜歌仔戲劇團｜《焰火長槍：火帥與玉龍的背影》｜高雄中山堂劇場戶外陽光草坪｜2026-12-05 正戲 19:00 |  | approve：原文「12/05(六)文惜歌仔戲劇團《焰火長槍：火帥與玉龍的背影》」，19:00，地點正確。chg-017、chg-0… | rejected badgeType-not-free |
| chg-008 | add | https://www.threads.com/@taiwaneseopera168/post/DfQ5lKaiQVF | 繡花園戲劇團｜《姜子牙下山》｜高雄中山堂劇場戶外陽光草坪｜2026-12-06 正戲 19:00 |  | approve：原文「12/06(日)繡花園戲劇團《姜子牙下山》」，19:00，地點正確。chg-018、chg-028 與這筆重複。 | rejected badgeType-not-free |
| chg-009 | add | https://www.threads.com/@taiwaneseopera168/post/DfQ5lKaiQVF | 春明歌劇團｜《玉虛戰歌．天命之戰》｜高雄中山堂劇場戶外陽光草坪｜2026-12-11 正戲 19:00 |  | approve：原文「12/11(五)春明歌劇團《玉虛戰歌．天命之戰》」，19:00，地點正確。chg-019、chg-029 與這筆… | rejected badgeType-not-free |
| chg-010 | add | https://www.threads.com/@taiwaneseopera168/post/DfQ5lKaiQVF | 水錦歌劇團｜《對面夫妻～韋馱與觀音》｜高雄中山堂劇場戶外陽光草坪｜2026-12-12 正戲 19:00 |  | approve：原文「12/12(六)水錦歌劇團《對面夫妻～韋馱與觀音》」，19:00，地點正確。chg-020、chg-030 與這… | rejected badgeType-not-free |
| chg-011 | add | https://www.threads.com/@taiwaneseopera168/post/DfQ5lKaiQVF | 明華園星字戲劇團｜《斷案青天－陰錯陽差》｜高雄中山堂劇場戶外陽光草坪｜2026-12-13 正戲 19:00 |  | approve：原文「12/13(日)明華園星字戲劇團《斷案青天－陰錯陽差》」，19:00，地點正確。chg-021、chg-031 … | rejected badgeType-not-free |
| chg-012 | add | https://www.threads.com/@jing__1017/post/DfR48oeiau2 | 小金枝歌劇團｜《棄老山傳奇》｜高雄中山堂劇場戶外陽光草坪｜2026-11-27 正戲 19:00 |  | reject：重複建卡：與 chg-002 是同一場（11/27 小金枝《棄老山傳奇》，高雄中山堂草坪 19:00），內容一致。ji… | held  |
| chg-013 | add | https://www.threads.com/@jing__1017/post/DfR48oeiau2 | 新和興總團｜《秦英掛帥》｜高雄中山堂劇場戶外陽光草坪｜2026-11-28 正戲 19:00 |  | reject：重複建卡：與 chg-003 是同一場（11/28 新和興總團《秦英掛帥》），應併為 alsoSources。 | held  |
| chg-014 | add | https://www.threads.com/@jing__1017/post/DfR48oeiau2 | 藝華園戲劇團｜《八仙傳奇－張果老與藍采和》｜高雄中山堂劇場戶外陽光草坪｜2026-11-29 正戲 19:00 |  | reject：重複建卡：與 chg-004 是同一場（11/29 藝華園《八仙傳奇－張果老與藍采和》），應併為 alsoSource… | held  |
| chg-015 | add | https://www.threads.com/@jing__1017/post/DfR48oeiau2 | 新藝芳歌劇團｜《金蟾緣》｜高雄中山堂劇場戶外陽光草坪｜2026-12-03 正戲 19:00 |  | reject：重複建卡：與 chg-005 是同一場（12/03 新藝芳《金蟾緣》），應併為 alsoSources。 | held  |
| chg-016 | add | https://www.threads.com/@jing__1017/post/DfR48oeiau2 | 佩儀歌劇團｜《吳漢殺妻》｜高雄中山堂劇場戶外陽光草坪｜2026-12-04 正戲 19:00 |  | reject：重複建卡：與 chg-006 是同一場（12/04 佩儀《吳漢殺妻》），應併為 alsoSources。 | held  |
| chg-017 | add | https://www.threads.com/@jing__1017/post/DfR48oeiau2 | 文惜歌仔戲劇團｜《焰火長槍：火帥與玉龍的背影》｜高雄中山堂劇場戶外陽光草坪｜2026-12-05 正戲 19:00 |  | reject：重複建卡：與 chg-007 是同一場（12/05 文惜《焰火長槍》），應併為 alsoSources。 | held  |
| chg-018 | add | https://www.threads.com/@jing__1017/post/DfR48oeiau2 | 繡花園戲劇團｜《姜子牙下山》｜高雄中山堂劇場戶外陽光草坪｜2026-12-06 正戲 19:00 |  | reject：重複建卡：與 chg-008 是同一場（12/06 繡花園《姜子牙下山》），應併為 alsoSources。 | held  |
| chg-019 | add | https://www.threads.com/@jing__1017/post/DfR48oeiau2 | 春明歌劇團｜《玉虛戰歌．天命之戰》｜高雄中山堂劇場戶外陽光草坪｜2026-12-11 正戲 19:00 |  | reject：重複建卡：與 chg-009 是同一場（12/11 春明《玉虛戰歌．天命之戰》），應併為 alsoSources。 | held  |
| chg-020 | add | https://www.threads.com/@jing__1017/post/DfR48oeiau2 | 水錦歌劇團｜《對面夫妻～韋馱與觀音》｜高雄中山堂劇場戶外陽光草坪｜2026-12-12 正戲 19:00 |  | reject：重複建卡：與 chg-010 是同一場（12/12 水錦《對面夫妻～韋馱與觀音》），應併為 alsoSources。 | held  |
| chg-021 | add | https://www.threads.com/@jing__1017/post/DfR48oeiau2 | 明華園星字戲劇團｜《斷案青天－陰錯陽差》｜高雄中山堂劇場戶外陽光草坪｜2026-12-13 正戲 19:00 |  | reject：重複建卡：與 chg-011 是同一場（12/13 明華園星字《斷案青天－陰錯陽差》），應併為 alsoSources。 | held  |
| chg-022 | add | https://www.facebook.com/photo/?fbid=122315789156250015 | 小金枝歌劇團｜《棄老山傳奇》｜高雄中山堂劇場戶外陽光草坪｜2026-11-27 正戲 19:00 |  | reject：重複建卡：與 chg-002 是同一場（11/27 小金枝《棄老山傳奇》）。這則 Facebook 貼文（看來是主辦「… | held  |
| chg-023 | add | https://www.facebook.com/photo/?fbid=122315789156250015 | 新和興總團｜《秦英掛帥》｜高雄中山堂劇場戶外陽光草坪｜2026-11-28 正戲 19:00 |  | reject：重複建卡：與 chg-003 是同一場（11/28 新和興總團《秦英掛帥》），應併為 alsoSources。 | held  |
| chg-024 | add | https://www.facebook.com/photo/?fbid=122315789156250015 | 藝華園戲劇團｜《八仙傳奇－張果老與藍采和》｜高雄中山堂劇場戶外陽光草坪｜2026-11-29 正戲 19:00 |  | reject：重複建卡：與 chg-004 是同一場（11/29 藝華園《八仙傳奇》），應併為 alsoSources。 | held  |
| chg-025 | add | https://www.facebook.com/photo/?fbid=122315789156250015 | 新藝芳歌劇團｜《金蟾緣》｜高雄中山堂劇場戶外陽光草坪｜2026-12-03 正戲 19:00 |  | reject：重複建卡：與 chg-005 是同一場（12/03 新藝芳《金蟾緣》），應併為 alsoSources。 | held  |
| chg-026 | add | https://www.facebook.com/photo/?fbid=122315789156250015 | 佩儀歌劇團｜《吳漢殺妻》｜高雄中山堂劇場戶外陽光草坪｜2026-12-04 正戲 19:00 |  | reject：重複建卡：與 chg-006 是同一場（12/04 佩儀《吳漢殺妻》），應併為 alsoSources。 | held  |
| chg-027 | add | https://www.facebook.com/photo/?fbid=122315789156250015 | 文惜歌仔戲劇團｜《焰火長槍：火帥與玉龍的背影》｜高雄中山堂劇場戶外陽光草坪｜2026-12-05 正戲 19:00 |  | reject：重複建卡：與 chg-007 是同一場（12/05 文惜《焰火長槍》），應併為 alsoSources。 | held  |
| chg-028 | add | https://www.facebook.com/photo/?fbid=122315789156250015 | 繡花園戲劇團｜《姜子牙下山》｜高雄中山堂劇場戶外陽光草坪｜2026-12-06 正戲 19:00 |  | reject：重複建卡：與 chg-008 是同一場（12/06 繡花園《姜子牙下山》），應併為 alsoSources。 | held  |
| chg-029 | add | https://www.facebook.com/photo/?fbid=122315789156250015 | 春明歌劇團｜《玉虛戰歌．天命之戰》｜高雄中山堂劇場戶外陽光草坪｜2026-12-11 正戲 19:00 |  | reject：重複建卡：與 chg-009 是同一場（12/11 春明《玉虛戰歌》），應併為 alsoSources。 | held  |
| chg-030 | add | https://www.facebook.com/photo/?fbid=122315789156250015 | 水錦歌劇團｜《對面夫妻～韋馱與觀音》｜高雄中山堂劇場戶外陽光草坪｜2026-12-12 正戲 19:00 |  | reject：重複建卡：與 chg-010 是同一場（12/12 水錦《對面夫妻》），應併為 alsoSources。 | held  |
| chg-031 | add | https://www.facebook.com/photo/?fbid=122315789156250015 | 明華園星字戲劇團｜《斷案青天－陰錯陽差》｜高雄中山堂劇場戶外陽光草坪｜2026-12-13 正戲 19:00 |  | reject：重複建卡：與 chg-011 是同一場（12/13 明華園星字《斷案青天》），應併為 alsoSources。 | held  |
| chg-032 | change（由「一致」轉）（查證成立） | https://culture.tainan.gov.tw/act_month/Details?Parser=99,5,44,,,,25429（原貼文 https://www.threads.com/@joe_huang_k_w/post/DfQ7AS6CdKQ） | 古都木偶戲劇團｜《臺灣風雲錄-戰火波瀾》｜【大內區】大內國小｜2026-11-07 正戲 19:00 | location：卡 臺南市大內區大內國小 → 文 【大內區】大內國小 | reject：這筆是由 confirm 轉成 change，但 diffs 唯一的差異是 location 的寫法：卡片寫「臺南市大… | held  |
| chg-033 | change（查證成立） | https://n.yam.com/Article/20261026226244（原貼文 https://www.threads.com/@the_rin.lpm/post/DfUZMCME7Ac） | 秀琴歌劇團｜《玉石變》｜莊泰路、國營路口總醮壇｜2026-11-07 扮仙 18:30、2026-11-07 正戲 19:00 | time：卡 19:00 → 文 2026-11-07 扮仙 18:30；location：卡 新北市新莊區中正路143號（保元宮） → 文 莊泰路、國營路口總醮壇 | approve：原文（蕃新聞 10/26，引用保元宮 10/22 官方海報）明確寫「同一天的總醮壇，則由秀琴歌劇團演出。18:30至1… | rejected location-not-in-quote |
| chg-034 | add（查證成立） | https://n.yam.com/Article/20261026226244（原貼文 https://www.threads.com/@the_rin.lpm/post/DfUZMCME7Ac） | 陳錫煌掌中戲｜《天下財主》｜保元宮本廟｜2026-11-07 扮仙 11:00、2026-11-07 正戲 14:00 |  | approve：原文「陳錫煌掌中戲安排在保元宮本廟，官方海報列出三個時段：11:00至12:00扮仙戲、14:00至16:00《天下財… | added  |
| chg-035 | add（查證成立） | https://n.yam.com/Article/20261026226244（原貼文 https://www.threads.com/@the_rin.lpm/post/DfUZMCME7Ac） | 陳錫煌掌中戲｜《劈山救母》｜保元宮本廟｜2026-11-07 正戲 18:30 |  | approve：原文「18:30至20:30《劈山救母》」，同日在保元宮本廟，和 chg-034 是同一天的不同場次，分開建卡合理；這… | rejected duplicate |
| chg-036 | add（查證成立） | https://www.opentix.life/event/2090269380048343041（原貼文 https://www.opentix.life/event/2090269380048343041） | 民權歌劇團｜戲釀青春──2026育成聯合展演｜《鐵弓緣》選段｜臺北市士林區文林路751號（臺灣戲曲中心小舞台）｜2026-11-06 正戲 19:30 |  | approve：OPENTIX 官方節目頁「【小舞台】 11/06（五）19:30 民權歌劇團《鐵弓緣》選段」，地址為文林路751號，… | rejected location-not-in-quote,title-not-in-quote,badgeType-not-ticket |
| chg-037 | add（查證成立） | https://www.opentix.life/event/2090269380048343041（原貼文 https://www.opentix.life/event/2090269380048343041） | 一心戲劇團｜戲釀青春──2026育成聯合展演｜經典折子《借扇》、《秀嬋申冤》、《虹霓關》｜臺北市士林區文林路751號（臺灣戲曲中心小表演廳）｜2026-11-07 正戲 14:30 |  | approve：OPENTIX 官方頁「【小表演廳】 11/07（六）14:30 一心戲劇團 經典折子《借扇》、《秀嬋申冤》、《虹霓關… | rejected location-not-in-quote,title-not-in-quote,badgeType-not-ticket |
| chg-038 | add（查證成立） | https://www.opentix.life/event/2090269380048343041（原貼文 https://www.opentix.life/event/2090269380048343041） | 薪傳歌仔戲劇團｜戲釀青春──2026育成聯合展演｜《蒼原孤雁》｜臺北市士林區文林路751號（臺灣戲曲中心小表演廳）｜2026-11-14 正戲 14:30 |  | approve：OPENTIX 官方頁「11/14（六）14:30 薪傳歌仔戲劇團《蒼原孤雁》」，在小表演廳，日期、時間、場地正確；庫… | rejected location-not-in-quote,title-not-in-quote,badgeType-not-ticket |
| chg-039 | add（查證成立） | https://cloud.culture.tw/frontsite/inquiry/eventInquiryAction.do?method=showEventDetail&uid=6aaacec826b324165c32e41c（原貼文 https://www.opentix.life/event/2099337927309197313） | 烏貓戲出｜《燈殼樓的委託-小戲蟲拜先生》｜大稻埕戲苑曲藝場｜2026-11-28 正戲 11:00、2026-11-28 正戲 14:30、2026-11-29 正戲 11:00、2026-11-29 正戲 14:30、2026-12-1… |  | needs-check：8 個場次（11/28、11/29、12/12、12/13 各 11:00 和 14:30）與 iCulture 列表… | held  |

## 待查與退回

| 類別 | 貼文 | 原因 | 說明 |
| --- | --- | --- | --- |
| 漏處置 | threads:jing__1017:DfFPe2zidiO | revision-mismatch |  |
| 漏處置 | threads:jing__1017:DfFOKfrCWgq | revision-mismatch |  |
| 漏處置 | threads:jing__1017:DfFJ-aHk3ng | revision-mismatch |  |

## 遠期場次（超過 120 天，進入 120 天內自動重驗）

| 貼文 | 內容 |
| --- | --- |
| https://www.facebook.com/photo/?fbid=1560228489482771 | 明華園天字戲劇團｜《重返：愛河戀夢》｜臺灣戲曲中心 大表演廳｜2027-06-05、2027-06-06 |
| https://www.facebook.com/MingHuaYuanTianTaiwaneseOpera/reels_tab | 明華園天字戲劇團｜《重返：愛河戀夢》｜臺灣戲曲中心 大表演廳｜2027-06-05、2027-06-06 |

## 紀錄檔

- 本輪狀態：/Users/eric/aiwork/taiwan-opera-calendar/patrol_state/runs/2026-11-04_2245/state.json
- 巡檢紀錄：patrol_runs/2026-11-04_2245.json（/Users/eric/aiwork/taiwan-opera-calendar）
- 證據：patrol_evidence/2026-11-04_2245/
- 產生時間：2026-11-04T23:22:01+08:00
