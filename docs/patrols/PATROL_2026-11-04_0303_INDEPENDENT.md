# 巡檢報告 2026-11-04_0303（patrol-v2，正式）

## 結論

| 項目 | 結果 |
| --- | --- |
| 執行 | 開始 2026-11-04T03:03:29+08:00；結果 進行中；步驟 preflight:done、collect:done、pack:done、judge:done、check:done、verify:done、review:done、apply:done、publish:done、report:running |
| 來源 | 20 個：完整 2、部分 18、失敗 0、未讀 0 |
| 資料 | 送判讀 247 篇／圖 23 張；變更提案 42、確認一致 37、送查證 31（成立 7、與卡相同 9、查無佐證不收 19）、退回 0、漏處置 0；已過期不收 84、遠期暫存 1 |
| 寫入 | 寫入 1、add_card 拒絕 19、審查未通過 22 |
| 發布 | verified；SHA 2dcfd543ecbce9cb042653bf90e7bca626a69d50；Actions 41705001532 |

## 模型與用量

| 角色 | 模型 | 依據 |
| --- | --- | --- |
| main | claude-sonnet-5-5 | get_session self：effort=medium |
| judge | sonnet | Agent 工具 model 參數；effort=medium |
| verify | opus | Agent 工具 model 參數；effort=medium |
| review | opus | Agent 工具 model 參數；effort=medium |

- 判讀批次 10；送出貼文 247 篇、圖片 23 張、正文約 77093 字
- 略過（已判讀未變動）103 篇；窗口外 17 篇
- 第二次審查：有（42 項）

## 來源

| 來源 | 狀態 | 範圍 | 說明 |
| --- | --- | --- | --- |
| threads:joe_huang_k_w | 部分 | 首屏 5 篇、累積 8 篇；最新 2026-11-03T21:56:59+08:00、最舊 2026-10-26T21:28:30+08:00；捲動 1 次、停止原因 reached-window；圖片下載 13 張 | 不變式通過；證據 /Users/eric/aiwork/taiwan-opera-calendar/patrol_evidence/2026-11-04_0303/threads_joe_huang… |
| threads:h.akito_1996 | 部分 | 首屏 4 篇、累積 9 篇；最新 2026-11-04T03:02:08+08:00、最舊 2026-09-27T00:04:33+08:00；捲動 2 次、停止原因 reached-window；圖片下載 9 張 | 不變式通過；證據 /Users/eric/aiwork/taiwan-opera-calendar/patrol_evidence/2026-11-04_0303/threads_h.akito_1… |
| threads:the_rin.lpm | 部分 | 首屏 4 篇、累積 7 篇；最新 2026-11-01T20:37:03+08:00、最舊 2026-09-26T14:32:03+08:00；捲動 2 次、停止原因 reached-window；圖片下載 8 張 | 不變式通過；證據 /Users/eric/aiwork/taiwan-opera-calendar/patrol_evidence/2026-11-04_0303/threads_the_rin.l… |
| threads:xuefeng_lu_ | 完整 | 7 天窗口讀完（停止原因 reached-window）；窗口內 5 篇皆有處置；圖片 0 張皆已判讀 | 不變式通過、逐篇處置完成 |
| threads:yuzhongluo | 部分 | 首屏 4 篇、累積 11 篇；最新 2026-11-03T23:45:00+08:00、最舊 2026-10-28T01:48:13+08:00；捲動 3 次、停止原因 reached-window；圖片下載 22 張 | 不變式通過；證據 /Users/eric/aiwork/taiwan-opera-calendar/patrol_evidence/2026-11-04_0303/threads_yuzhonglu… |
| threads:taiwaneseopera168 | 部分 | 首屏 4 篇、累積 41 篇；最新 2026-11-04T00:49:50+08:00、最舊 2026-08-16T02:33:12+08:00；捲動 20 次、停止原因 max-scrolls；圖片下載 36 張 | 不變式通過；證據 /Users/eric/aiwork/taiwan-opera-calendar/patrol_evidence/2026-11-04_0303/threads_taiwanese… |
| threads:jing__1017 | 部分 | 首屏 6 篇、累積 35 篇；最新 2026-11-04T01:53:02+08:00、最舊 2026-10-28T19:50:21+08:00；捲動 15 次、停止原因 no-new-after-3；圖片下載 34 張 | 不變式通過；證據 /Users/eric/aiwork/taiwan-opera-calendar/patrol_evidence/2026-11-04_0303/threads_jing__101… |
| threads:hilang.on.tour | 完整 | 7 天窗口讀完（停止原因 reached-window）；窗口內 0 篇皆有處置；圖片 0 張皆已判讀 | 不變式通過、逐篇處置完成 |
| threads:yolin1991 | 部分 | 首屏 4 篇、累積 9 篇；最新 2026-11-03T21:11:25+08:00、最舊 2026-10-25T22:39:55+08:00；捲動 3 次、停止原因 reached-window；圖片下載 9 張 | 不變式通過；證據 /Users/eric/aiwork/taiwan-opera-calendar/patrol_evidence/2026-11-04_0303/threads_yolin1991… |
| facebook:sunhope.fans | 部分 | 首屏 3 篇、累積 20 篇；最新 無、最舊 無；捲動 20 次、停止原因 max-scrolls；圖片下載 27 張 | 不變式通過；證據 /Users/eric/aiwork/taiwan-opera-calendar/patrol_evidence/2026-11-04_0303/facebook_sunhope.… |
| facebook:HsiaoHsiYuan1913 | 部分 | 首屏 1 篇、累積 24 篇；最新 無、最舊 無；捲動 20 次、停止原因 max-scrolls；圖片下載 50 張 | 不變式通過；證據 /Users/eric/aiwork/taiwan-opera-calendar/patrol_evidence/2026-11-04_0303/facebook_HsiaoHsi… |
| facebook:100063868113954 | 部分 | 首屏 2 篇、累積 21 篇；最新 無、最舊 無；捲動 20 次、停止原因 max-scrolls；圖片下載 48 張 | 不變式通過；證據 /Users/eric/aiwork/taiwan-opera-calendar/patrol_evidence/2026-11-04_0303/facebook_10006386… |
| facebook:MingHuaYuanTianTaiwaneseOpera | 部分 | 首屏 3 篇、累積 22 篇；最新 無、最舊 無；捲動 20 次、停止原因 max-scrolls；圖片下載 50 張 | 不變式通過；證據 /Users/eric/aiwork/taiwan-opera-calendar/patrol_evidence/2026-11-04_0303/facebook_MingHuaY… |
| facebook:61574134933376 | 部分 | 首屏 3 篇、累積 19 篇；最新 無、最舊 無；捲動 20 次、停止原因 max-scrolls；圖片下載 34 張 | 不變式通過；證據 /Users/eric/aiwork/taiwan-opera-calendar/patrol_evidence/2026-11-04_0303/facebook_61574134… |
| facebook:mhysun | 部分 | 首屏 3 篇、累積 19 篇；最新 無、最舊 無；捲動 20 次、停止原因 max-scrolls；圖片下載 66 張 | 不變式通過；證據 /Users/eric/aiwork/taiwan-opera-calendar/patrol_evidence/2026-11-04_0303/facebook_mhysun.j… |
| facebook:61594936681482 | 部分 | 首屏 1 篇、累積 7 篇；最新 無、最舊 無；捲動 7 次、停止原因 no-new-after-3；圖片下載 23 張 | 不變式通過；證據 /Users/eric/aiwork/taiwan-opera-calendar/patrol_evidence/2026-11-04_0303/facebook_61594936… |
| facebook:lanyang.opera | 部分 | 首屏 2 篇、累積 21 篇；最新 無、最舊 無；捲動 20 次、停止原因 max-scrolls；圖片下載 24 張 | 不變式通過；證據 /Users/eric/aiwork/taiwan-opera-calendar/patrol_evidence/2026-11-04_0303/facebook_lanyang.… |
| facebook:Taichungpuppettheater | 部分 | 首屏 3 篇、累積 25 篇；最新 無、最舊 無；捲動 20 次、停止原因 max-scrolls；圖片下載 24 張 | 不變式通過；證據 /Users/eric/aiwork/taiwan-opera-calendar/patrol_evidence/2026-11-04_0303/facebook_Taichung… |
| culture | 部分 | total 1315、fetchedAt 2026-11-03T11:48:15+08:00、戲曲紀錄 27 筆 | 資料新鮮；逐筆處置待判讀後確認 |
| issues | 部分 | state=all 共 3 則（含留言） | 已讀取；處置待判讀後確認 |

- OPENTIX：sitemap 850 個活動、本輪有變 735、抓取 250、戲曲相關且未過期 28、延後 485、錯誤 0

## 卡片變更

| 編號 | 動作 | 來源 | 內容 | 差異 | 審查 | 寫入 |
| --- | --- | --- | --- | --- | --- | --- |
| chg-001 | add | https://www.threads.com/@taiwaneseopera168/post/DfQ5lKaiQVF | 小金枝歌劇團｜《棄老山傳奇》｜高雄中山堂劇場戶外陽光草坪｜2026-11-27 正戲 19:00 |  | approve：Threads taiwaneseopera168 原文「11/27…小金枝歌劇團《棄老山傳奇》」，另載「每場次開演時… | rejected badgeType-not-free |
| chg-002 | add | https://www.threads.com/@taiwaneseopera168/post/DfQ5lKaiQVF | 新和興總團｜《秦英掛帥》｜高雄中山堂劇場戶外陽光草坪｜2026-11-28 正戲 19:00 |  | approve：Threads taiwaneseopera168 原文「11/28…新和興總團《秦英掛帥》」，另載「每場次開演時間｜… | rejected badgeType-not-free |
| chg-003 | add | https://www.threads.com/@taiwaneseopera168/post/DfQ5lKaiQVF | 藝華園戲劇團｜《八仙傳奇－張果老與藍采和》｜高雄中山堂劇場戶外陽光草坪｜2026-11-29 正戲 19:00 |  | approve：Threads taiwaneseopera168 原文「11/29…藝華園戲劇團《八仙傳奇－張果老與藍采和》」，另載… | rejected badgeType-not-free |
| chg-004 | add | https://www.threads.com/@taiwaneseopera168/post/DfQ5lKaiQVF | 新藝芳歌劇團｜《金蟾緣》｜高雄中山堂劇場戶外陽光草坪｜2026-12-03 正戲 19:00 |  | approve：Threads taiwaneseopera168 原文「12/03…新藝芳歌劇團《金蟾緣》」，另載「每場次開演時間｜… | rejected badgeType-not-free |
| chg-005 | add | https://www.threads.com/@taiwaneseopera168/post/DfQ5lKaiQVF | 佩儀歌劇團｜《吳漢殺妻》｜高雄中山堂劇場戶外陽光草坪｜2026-12-04 正戲 19:00 |  | approve：Threads taiwaneseopera168 原文「12/04…佩儀歌劇團《吳漢殺妻》」，另載「每場次開演時間｜… | rejected badgeType-not-free |
| chg-006 | add | https://www.threads.com/@taiwaneseopera168/post/DfQ5lKaiQVF | 文惜歌仔戲劇團｜《焰火長槍：火帥與玉龍的背影》｜高雄中山堂劇場戶外陽光草坪｜2026-12-05 正戲 19:00 |  | approve：Threads taiwaneseopera168 原文「12/05…文惜歌仔戲劇團《焰火長槍：火帥與玉龍的背影》」，… | rejected badgeType-not-free |
| chg-007 | add | https://www.threads.com/@taiwaneseopera168/post/DfQ5lKaiQVF | 繡花園戲劇團｜《姜子牙下山》｜高雄中山堂劇場戶外陽光草坪｜2026-12-06 正戲 19:00 |  | approve：Threads taiwaneseopera168 原文「12/06…繡花園戲劇團《姜子牙下山》」，另載「每場次開演時… | rejected badgeType-not-free |
| chg-008 | add | https://www.threads.com/@taiwaneseopera168/post/DfQ5lKaiQVF | 春明歌劇團｜《玉虛戰歌．天命之戰》｜高雄中山堂劇場戶外陽光草坪｜2026-12-11 正戲 19:00 |  | approve：Threads taiwaneseopera168 原文「12/11…春明歌劇團《玉虛戰歌．天命之戰》」，另載「每場次… | rejected badgeType-not-free |
| chg-009 | add | https://www.threads.com/@taiwaneseopera168/post/DfQ5lKaiQVF | 水錦歌劇團｜《對面夫妻～韋馱與觀音》｜高雄中山堂劇場戶外陽光草坪｜2026-12-12 正戲 19:00 |  | approve：Threads taiwaneseopera168 原文「12/12…水錦歌劇團《對面夫妻～韋馱與觀音》」，另載「每場… | rejected badgeType-not-free |
| chg-010 | add | https://www.threads.com/@taiwaneseopera168/post/DfQ5lKaiQVF | 明華園星字戲劇團｜《斷案青天－陰錯陽差》｜高雄中山堂劇場戶外陽光草坪｜2026-12-13 正戲 19:00 |  | approve：Threads taiwaneseopera168 原文「12/13…明華園星字戲劇團《斷案青天－陰錯陽差》」，另載「… | rejected badgeType-not-free |
| chg-011 | add | https://www.threads.com/@jing__1017/post/DfR48oeiau2 | 小金枝歌劇團｜《棄老山傳奇》｜高雄中山堂劇場戶外陽光草坪｜2026-11-27 正戲 19:00 |  | reject：內容本身正確（jing__1017 原文與 taiwaneseopera168 相同場次），但與 chg-001 是同… | held  |
| chg-012 | add | https://www.threads.com/@jing__1017/post/DfR48oeiau2 | 新和興總團｜《秦英掛帥》｜高雄中山堂劇場戶外陽光草坪｜2026-11-28 正戲 19:00 |  | reject：內容本身正確（jing__1017 原文與 taiwaneseopera168 相同場次），但與 chg-002 是同… | held  |
| chg-013 | add | https://www.threads.com/@jing__1017/post/DfR48oeiau2 | 藝華園戲劇團｜《八仙傳奇－張果老與藍采和》｜高雄中山堂劇場戶外陽光草坪｜2026-11-29 正戲 19:00 |  | reject：內容本身正確（jing__1017 原文與 taiwaneseopera168 相同場次），但與 chg-003 是同… | held  |
| chg-014 | add | https://www.threads.com/@jing__1017/post/DfR48oeiau2 | 新藝芳歌劇團｜《金蟾緣》｜高雄中山堂劇場戶外陽光草坪｜2026-12-03 正戲 19:00 |  | reject：內容本身正確（jing__1017 原文與 taiwaneseopera168 相同場次），但與 chg-004 是同… | held  |
| chg-015 | add | https://www.threads.com/@jing__1017/post/DfR48oeiau2 | 佩儀歌劇團｜《吳漢殺妻》｜高雄中山堂劇場戶外陽光草坪｜2026-12-04 正戲 19:00 |  | reject：內容本身正確（jing__1017 原文與 taiwaneseopera168 相同場次），但與 chg-005 是同… | held  |
| chg-016 | add | https://www.threads.com/@jing__1017/post/DfR48oeiau2 | 文惜歌仔戲劇團｜《焰火長槍：火帥與玉龍的背影》｜高雄中山堂劇場戶外陽光草坪｜2026-12-05 正戲 19:00 |  | reject：內容本身正確（jing__1017 原文與 taiwaneseopera168 相同場次），但與 chg-006 是同… | held  |
| chg-017 | add | https://www.threads.com/@jing__1017/post/DfR48oeiau2 | 繡花園戲劇團｜《姜子牙下山》｜高雄中山堂劇場戶外陽光草坪｜2026-12-06 正戲 19:00 |  | reject：內容本身正確（jing__1017 原文與 taiwaneseopera168 相同場次），但與 chg-007 是同… | held  |
| chg-018 | add | https://www.threads.com/@jing__1017/post/DfR48oeiau2 | 春明歌劇團｜《玉虛戰歌．天命之戰》｜高雄中山堂劇場戶外陽光草坪｜2026-12-11 正戲 19:00 |  | reject：內容本身正確（jing__1017 原文與 taiwaneseopera168 相同場次），但與 chg-008 是同… | held  |
| chg-019 | add | https://www.threads.com/@jing__1017/post/DfR48oeiau2 | 水錦歌劇團｜《對面夫妻～韋馱與觀音》｜高雄中山堂劇場戶外陽光草坪｜2026-12-12 正戲 19:00 |  | reject：內容本身正確（jing__1017 原文與 taiwaneseopera168 相同場次），但與 chg-009 是同… | held  |
| chg-020 | add | https://www.threads.com/@jing__1017/post/DfR48oeiau2 | 明華園星字戲劇團｜《斷案青天－陰錯陽差》｜高雄中山堂劇場戶外陽光草坪｜2026-12-13 正戲 19:00 |  | reject：內容本身正確（jing__1017 原文與 taiwaneseopera168 相同場次），但與 chg-010 是同… | held  |
| chg-021 | add | facebook:61574134933376:5bbb89945b6e | 繡花園戲劇團｜【姜子牙下山】｜高雄中山堂戶外陽光草坪｜2026-12-06 正戲 未公布 |  | reject：繡花園自家貼文「12/6(日) 高雄中山堂戶外陽光草坪」【姜子牙下山】，和 chg-007 是同一場（外臺歌仔戲2.0… | held  |
| chg-022 | add | https://www.facebook.com/photo/?fbid=122315789156250015 | 小金枝歌劇團｜《棄老山傳奇》｜高雄中山堂劇場戶外陽光草坪｜2026-11-27 正戲 19:00 |  | reject：內容本身正確（FB 貼文 122315789156250015 的場次表與 Threads 版相同），但與 chg-0… | held  |
| chg-023 | add | https://www.facebook.com/photo/?fbid=122315789156250015 | 新和興總團｜《秦英掛帥》｜高雄中山堂劇場戶外陽光草坪｜2026-11-28 正戲 19:00 |  | reject：內容本身正確（FB 貼文 122315789156250015 的場次表與 Threads 版相同），但與 chg-0… | held  |
| chg-024 | add | https://www.facebook.com/photo/?fbid=122315789156250015 | 藝華園戲劇團｜《八仙傳奇－張果老與藍采和》｜高雄中山堂劇場戶外陽光草坪｜2026-11-29 正戲 19:00 |  | reject：內容本身正確（FB 貼文 122315789156250015 的場次表與 Threads 版相同），但與 chg-0… | held  |
| chg-025 | add | https://www.facebook.com/photo/?fbid=122315789156250015 | 新藝芳歌劇團｜《金蟾緣》｜高雄中山堂劇場戶外陽光草坪｜2026-12-03 正戲 19:00 |  | reject：內容本身正確（FB 貼文 122315789156250015 的場次表與 Threads 版相同），但與 chg-0… | held  |
| chg-026 | add | https://www.facebook.com/photo/?fbid=122315789156250015 | 佩儀歌劇團｜《吳漢殺妻》｜高雄中山堂劇場戶外陽光草坪｜2026-12-04 正戲 19:00 |  | reject：內容本身正確（FB 貼文 122315789156250015 的場次表與 Threads 版相同），但與 chg-0… | held  |
| chg-027 | add | https://www.facebook.com/photo/?fbid=122315789156250015 | 文惜歌仔戲劇團｜《焰火長槍：火帥與玉龍的背影》｜高雄中山堂劇場戶外陽光草坪｜2026-12-05 正戲 19:00 |  | reject：內容本身正確（FB 貼文 122315789156250015 的場次表與 Threads 版相同），但與 chg-0… | held  |
| chg-028 | add | https://www.facebook.com/photo/?fbid=122315789156250015 | 繡花園戲劇團｜《姜子牙下山》｜高雄中山堂劇場戶外陽光草坪｜2026-12-06 正戲 19:00 |  | reject：內容本身正確（FB 貼文 122315789156250015 的場次表與 Threads 版相同），但與 chg-0… | held  |
| chg-029 | add | https://www.facebook.com/photo/?fbid=122315789156250015 | 春明歌劇團｜《玉虛戰歌．天命之戰》｜高雄中山堂劇場戶外陽光草坪｜2026-12-11 正戲 19:00 |  | reject：內容本身正確（FB 貼文 122315789156250015 的場次表與 Threads 版相同），但與 chg-0… | held  |
| chg-030 | add | https://www.facebook.com/photo/?fbid=122315789156250015 | 水錦歌劇團｜《對面夫妻～韋馱與觀音》｜高雄中山堂劇場戶外陽光草坪｜2026-12-12 正戲 19:00 |  | reject：內容本身正確（FB 貼文 122315789156250015 的場次表與 Threads 版相同），但與 chg-0… | held  |
| chg-031 | add | https://www.facebook.com/photo/?fbid=122315789156250015 | 明華園星字戲劇團｜《斷案青天－陰錯陽差》｜高雄中山堂劇場戶外陽光草坪｜2026-12-13 正戲 19:00 |  | reject：內容本身正確（FB 貼文 122315789156250015 的場次表與 Threads 版相同），但與 chg-0… | held  |
| chg-032 | add | https://www.facebook.com/photo/?fbid=1572037354954872 | 蘭陽戲劇團｜《錯配姻緣》｜新城紫雲宮（宜蘭縣蘇澳鎮新城里新城南路175號）｜2026-11-07 正戲 18:30 |  | approve：蘭陽戲劇團官方 FB 原文「11/7（六）晚上6:30 ※本場次為福宴場 劇目｜《錯配姻緣》 地點｜新城紫雲宮（宜蘭縣… | rejected badgeType-not-free |
| chg-033 | add | https://www.facebook.com/photo/?fbid=1572037354954872 | 蘭陽戲劇團｜《錯配姻緣》｜嶺腳永安宮（宜蘭縣蘇澳鎮港邊里嶺腳路104號）｜2026-11-22 正戲 18:00 |  | approve：蘭陽戲劇團官方 FB 原文「11/22（日）晚上6:00 ※本場次為福宴場 劇目｜《錯配姻緣》 地點｜嶺腳永安宮（…港… | rejected badgeType-not-free |
| chg-034 | add | https://www.facebook.com/photo/?fbid=1572037354954872 | 蘭陽戲劇團｜《福氣臨門》｜大湖普恩廟（宜蘭縣員山鄉逸仙村大安路121號）｜2026-11-23 正戲 18:30 |  | approve：蘭陽戲劇團官方 FB 原文「11/23（一）晚上6:30 ※本場次為福宴場 劇目｜《福氣臨門》 地點｜大湖普恩廟（…員… | rejected badgeType-not-free |
| chg-035 | add | https://www.facebook.com/photo/?fbid=1572037354954872 | 蘭陽戲劇團｜《求草救夫》｜利澤簡永安宮（宜蘭縣五結鄉利澤村利澤路26號）｜2026-11-26 正戲 19:30 |  | approve：蘭陽戲劇團官方 FB 原文「11/26（四）晚上7:30 劇目｜《求草救夫》 地點｜利澤簡永安宮（…五結鄉利澤村利澤路… | rejected badgeType-not-free |
| chg-036 | change（查證成立） | https://n.yam.com/Article/20261026226244（原貼文 https://www.threads.com/@the_rin.lpm/post/DfMv3UpE52E） | 秀琴歌劇團｜《玉石變》｜新北市新莊區莊泰路與國營路交叉口（保元宮建醮總醮壇）｜2026-11-07 扮仙 18:30、2026-11-07 正戲 19:00 | time：卡 19:00 → 文 2026-11-07 扮仙 18:30；location：卡 新北市新莊區中正路143號（保元宮） → 文 新北市新莊區莊泰路與國營路交叉口（保元宮建醮總醮壇） | approve：蕃新聞 2026/10/26 報導引用保元宮官方海報：「同一天的總醮壇，則由秀琴歌劇團演出。18:30至19:00是扮… | rejected location-not-in-quote |
| chg-037 | add（查證成立） | https://www.ttdac.taichung.gov.tw/na4700118767679823531/naArticleContent（原貼文 https://www.facebook.com/photo/?fbid=1544102917729719） | 台中木偶劇團｜戶外親子兒童劇演出｜屯區藝文中心 戶外．茄苳樹區｜2026-11-14 正戲 15:00 |  | needs-check：屯區藝文中心頁面：台中木偶劇團《波比大冒險》戶外親子兒童劇，115/11/14(六) 15:00，戶外．茄苳樹區，免費… | held  |
| chg-038 | add（查證成立） | https://www.ncfta.gov.tw/News_Content.aspx?n=5178&s=264641（原貼文 https://www.opentix.life/event/2090269380048343041） | 民權歌劇團｜《鐵弓緣》｜臺灣戲曲中心小舞台（臺北市士林區文林路751號）｜2026-11-06 正戲 19:30 |  | approve：傳藝中心 2026-11-03 新聞稿節目資訊：「演出地點：臺灣戲曲中心小舞台 … 11/06(五)19:30民權歌劇… | rejected badgeType-not-ticket |
| chg-039 | add（查證成立） | https://www.ncfta.gov.tw/News_Content.aspx?n=5178&s=264641（原貼文 https://www.opentix.life/event/2090269380048343041） | 臺北木偶劇團｜《雷萬春打虎》｜臺灣戲曲中心小舞台（臺北市士林區文林路751號）｜2026-11-08 正戲 14:30 |  | approve：同一份新聞稿「臺灣戲曲中心小舞台 … 11/08(日)14:30臺北木偶劇團《雷萬春打虎》」，內文說明這是「布袋戲經典… | rejected badgeType-not-ticket |
| chg-040 | add（查證成立） | https://www.ncfta.gov.tw/News_Content.aspx?n=5178&s=264641（原貼文 https://www.opentix.life/event/2090269380048343041） | 陳錫煌傳統掌中劇團｜《孫臏鬥海潮》｜臺灣戲曲中心小舞台（臺北市士林區文林路751號）｜2026-11-22 正戲 14:30 |  | approve：同一份新聞稿「臺灣戲曲中心小舞台 … 11/22(日)14:30陳錫煌傳統掌中劇團《孫臏鬥海潮》」，內文寫「布袋戲經典… | added  |
| chg-041 | add（查證成立） | https://www.ncfta.gov.tw/News_Content.aspx?n=5178&s=264641（原貼文 https://www.opentix.life/event/2090269380048343041） | 一心戲劇團｜經典折子《借扇》、《秀嬋申冤》、《虹霓關》｜臺灣戲曲中心小表演廳（臺北市士林區文林路751號）｜2026-11-07 正戲 14:30 |  | approve：同一份新聞稿「演出地點：臺灣戲曲中心小表演廳 11/07(六)14:30一心戲劇團 經典折子《借扇》、《秀嬋申冤》、《… | rejected badgeType-not-ticket |
| chg-042 | add（查證成立） | https://www.ncfta.gov.tw/News_Content.aspx?n=5178&s=264641（原貼文 https://www.opentix.life/event/2090269380048343041） | 薪傳歌仔戲劇團｜《蒼原孤雁》｜臺灣戲曲中心小表演廳（臺北市士林區文林路751號）｜2026-11-14 正戲 14:30 |  | approve：同一份新聞稿「臺灣戲曲中心小表演廳 … 11/14(六)14:30薪傳歌仔戲劇團《蒼原孤雁》」，日期、時間、場地、劇目… | rejected badgeType-not-ticket |

## 遠期場次（超過 120 天，進入 120 天內自動重驗）

| 貼文 | 內容 |
| --- | --- |
| https://www.facebook.com/photo/?fbid=1560228489482771 | 明華園天字戲劇團｜《重返：愛河戀夢》｜臺灣戲曲中心 大表演廳｜2027-06-05、2027-06-06 |

## 紀錄檔

- 本輪狀態：/Users/eric/aiwork/taiwan-opera-calendar/patrol_state/runs/2026-11-04_0303/state.json
- 巡檢紀錄：patrol_runs/2026-11-04_0303.json（/Users/eric/aiwork/taiwan-opera-calendar）
- 證據：patrol_evidence/2026-11-04_0303/
- 產生時間：2026-11-04T03:38:34+08:00
