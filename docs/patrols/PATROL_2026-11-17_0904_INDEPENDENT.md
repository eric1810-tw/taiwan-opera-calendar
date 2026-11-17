# 巡檢報告 2026-11-17_0904（patrol-v2，正式）

## 結論

| 項目 | 結果 |
| --- | --- |
| 執行 | 開始 2026-11-17T09:04:17+08:00；結果 進行中；步驟 preflight:done、collect:done、pack:done、judge:done、check:done、verify:done、review:done、apply:done、publish:done、report:running |
| 來源 | 20 個：完整 3、部分 17、失敗 0、未讀 0 |
| 資料 | 送判讀 207 篇／圖 4 張；變更提案 15、確認一致 15、送查證 57（成立 3、與卡相同 2、查無佐證不收 52）、退回 0、漏處置 0；已過期不收 83、遠期暫存 8 |
| 寫入 | 寫入 1、add_card 拒絕 12、審查未通過 2 |
| 發布 | verified；SHA 456db3259ee537f184141110a2783a07e21305d3；Actions 43997220799 |

## 模型與用量

| 角色 | 模型 | 依據 |
| --- | --- | --- |
| main | claude-sonnet-5-5 | get_session self：effort=medium |
| judge | sonnet | Agent 工具 model 參數；effort=medium |
| verify | opus | Agent 工具 model 參數；effort=medium |
| review | opus | Agent 工具 model 參數；effort=medium |

- 判讀批次 9；送出貼文 207 篇、圖片 4 張、正文約 70465 字
- 略過（已判讀未變動）117 篇；窗口外 25 篇
- 第二次審查：有（15 項）

## 來源

| 來源 | 狀態 | 範圍 | 說明 |
| --- | --- | --- | --- |
| threads:joe_huang_k_w | 部分 | 首屏 5 篇、累積 9 篇；最新 2026-11-16T16:30:38+08:00、最舊 2026-11-08T14:16:48+08:00；捲動 1 次、停止原因 reached-window；圖片下載 7 張 | 不變式通過；證據 /Users/eric/aiwork/taiwan-opera-calendar/patrol_evidence/2026-11-17_0904/threads_joe_huang… |
| threads:h.akito_1996 | 部分 | 首屏 5 篇、累積 11 篇；最新 2026-11-16T19:56:04+08:00、最舊 2026-09-27T00:04:33+08:00；捲動 3 次、停止原因 reached-window；圖片下載 9 張 | 不變式通過；證據 /Users/eric/aiwork/taiwan-opera-calendar/patrol_evidence/2026-11-17_0904/threads_h.akito_1… |
| threads:the_rin.lpm | 部分 | 首屏 4 篇、累積 8 篇；最新 2026-11-16T19:23:08+08:00、最舊 2026-09-26T14:32:03+08:00；捲動 2 次、停止原因 reached-window；圖片下載 13 張 | 不變式通過；證據 /Users/eric/aiwork/taiwan-opera-calendar/patrol_evidence/2026-11-17_0904/threads_the_rin.l… |
| threads:xuefeng_lu_ | 完整 | 7 天窗口讀完（停止原因 reached-window）；窗口內 3 篇皆有處置；圖片 0 張皆已判讀 | 不變式通過、逐篇處置完成 |
| threads:yuzhongluo | 部分 | 首屏 4 篇、累積 22 篇；最新 2026-11-17T05:31:05+08:00、最舊 2026-11-09T00:31:27+08:00；捲動 10 次、停止原因 reached-window；圖片下載 28 張 | 不變式通過；證據 /Users/eric/aiwork/taiwan-opera-calendar/patrol_evidence/2026-11-17_0904/threads_yuzhonglu… |
| threads:taiwaneseopera168 | 部分 | 首屏 3 篇、累積 29 篇；最新 2026-11-17T00:19:39+08:00、最舊 2026-08-16T02:33:12+08:00；捲動 19 次、停止原因 no-new-after-3；圖片下載 51 張 | 不變式通過；證據 /Users/eric/aiwork/taiwan-opera-calendar/patrol_evidence/2026-11-17_0904/threads_taiwanese… |
| threads:jing__1017 | 部分 | 首屏 5 篇、累積 25 篇；最新 2026-11-17T01:15:21+08:00、最舊 2026-10-28T19:50:21+08:00；捲動 9 次、停止原因 reached-window；圖片下載 32 張 | 不變式通過；證據 /Users/eric/aiwork/taiwan-opera-calendar/patrol_evidence/2026-11-17_0904/threads_jing__101… |
| threads:hilang.on.tour | 完整 | 7 天窗口讀完（停止原因 reached-window）；窗口內 0 篇皆有處置；圖片 0 張皆已判讀 | 不變式通過、逐篇處置完成 |
| threads:yolin1991 | 部分 | 首屏 4 篇、累積 6 篇；最新 2026-11-16T13:26:48+08:00、最舊 2026-11-10T06:54:04+08:00；捲動 1 次、停止原因 reached-window；圖片下載 6 張 | 不變式通過；證據 /Users/eric/aiwork/taiwan-opera-calendar/patrol_evidence/2026-11-17_0904/threads_yolin1991… |
| facebook:sunhope.fans | 部分 | 首屏 3 篇、累積 20 篇；最新 無、最舊 無；捲動 20 次、停止原因 max-scrolls；圖片下載 28 張 | 不變式通過；證據 /Users/eric/aiwork/taiwan-opera-calendar/patrol_evidence/2026-11-17_0904/facebook_sunhope.… |
| facebook:HsiaoHsiYuan1913 | 部分 | 首屏 3 篇、累積 23 篇；最新 無、最舊 無；捲動 20 次、停止原因 max-scrolls；圖片下載 38 張 | 不變式通過；證據 /Users/eric/aiwork/taiwan-opera-calendar/patrol_evidence/2026-11-17_0904/facebook_HsiaoHsi… |
| facebook:100063868113954 | 部分 | 首屏 3 篇、累積 21 篇；最新 無、最舊 無；捲動 20 次、停止原因 max-scrolls；圖片下載 44 張 | 不變式通過；證據 /Users/eric/aiwork/taiwan-opera-calendar/patrol_evidence/2026-11-17_0904/facebook_10006386… |
| facebook:MingHuaYuanTianTaiwaneseOpera | 部分 | 首屏 1 篇、累積 21 篇；最新 無、最舊 無；捲動 20 次、停止原因 max-scrolls；圖片下載 55 張 | 不變式通過；證據 /Users/eric/aiwork/taiwan-opera-calendar/patrol_evidence/2026-11-17_0904/facebook_MingHuaY… |
| facebook:61574134933376 | 部分 | 首屏 1 篇、累積 21 篇；最新 無、最舊 無；捲動 20 次、停止原因 max-scrolls；圖片下載 48 張 | 不變式通過；證據 /Users/eric/aiwork/taiwan-opera-calendar/patrol_evidence/2026-11-17_0904/facebook_61574134… |
| facebook:mhysun | 部分 | 首屏 1 篇、累積 21 篇；最新 無、最舊 無；捲動 20 次、停止原因 max-scrolls；圖片下載 93 張 | 不變式通過；證據 /Users/eric/aiwork/taiwan-opera-calendar/patrol_evidence/2026-11-17_0904/facebook_mhysun.j… |
| facebook:61594936681482 | 部分 | 首屏 1 篇、累積 7 篇；最新 無、最舊 無；捲動 7 次、停止原因 no-new-after-3；圖片下載 23 張 | 不變式通過；證據 /Users/eric/aiwork/taiwan-opera-calendar/patrol_evidence/2026-11-17_0904/facebook_61594936… |
| facebook:lanyang.opera | 部分 | 首屏 1 篇、累積 23 篇；最新 無、最舊 無；捲動 20 次、停止原因 max-scrolls；圖片下載 38 張 | 不變式通過；證據 /Users/eric/aiwork/taiwan-opera-calendar/patrol_evidence/2026-11-17_0904/facebook_lanyang.… |
| facebook:Taichungpuppettheater | 部分 | 首屏 4 篇、累積 27 篇；最新 無、最舊 無；捲動 20 次、停止原因 max-scrolls；圖片下載 34 張 | 不變式通過；證據 /Users/eric/aiwork/taiwan-opera-calendar/patrol_evidence/2026-11-17_0904/facebook_Taichung… |
| culture | 部分 | total 501、fetchedAt 2026-11-15T10:19:38+08:00、戲曲紀錄 9 筆 | moc_records 已 47 小時未更新 |
| issues | 完整 | 3 筆皆有處置 | 逐筆處置完成 |

- OPENTIX：sitemap 798 個活動、本輪有變 630、抓取 250、戲曲相關且未過期 31、延後 380、錯誤 0

## 卡片變更

| 編號 | 動作 | 來源 | 內容 | 差異 | 審查 | 寫入 |
| --- | --- | --- | --- | --- | --- | --- |
| chg-001 | add | https://www.threads.com/@yuzhongluo/post/Dfz1sz3GeC4 | 羅裕誴歌劇團｜《楊排風掛帥》｜大龍峒保安宮庭園廣場｜2026-11-20 正戲 19:00 |  | approve：原文「115.11.20 [農曆10/12] (五)19:00 地點：大龍峒保安宮庭園廣場」與海報「11/20(五)1… | rejected artist-not-in-quote |
| chg-002 | add | https://www.facebook.com/photo/?fbid=122315789156250015 | 小金枝歌劇團｜《棄老山傳奇》｜高雄中山堂劇場戶外陽光草坪｜2026-11-27 正戲 19:00 |  | approve：原文「11/27（五）小金枝歌劇團《棄老山傳奇》」「每場次開演時間｜19:00」「演出地點｜高雄中山堂劇場戶外陽光草坪… | rejected badgeType-not-free |
| chg-003 | add | https://www.facebook.com/photo/?fbid=122315789156250015 | 新和興總團｜《秦英掛帥》｜高雄中山堂劇場戶外陽光草坪｜2026-11-28 正戲 19:00 |  | approve：原文「11/28（六）新和興總團《秦英掛帥》」，2026-11-28 為週六；時間 19:00、地點、免費均出自同一貼… | rejected badgeType-not-free |
| chg-004 | add | https://www.facebook.com/photo/?fbid=122315789156250015 | 藝華園戲劇團｜《八仙傳奇－張果老與藍采和》｜高雄中山堂劇場戶外陽光草坪｜2026-11-29 正戲 19:00 |  | approve：原文「11/29（日）藝華園戲劇團《八仙傳奇－張果老與藍采和》」，2026-11-29 為週日；時間、地點、免費出自同… | rejected badgeType-not-free |
| chg-005 | add | https://www.facebook.com/photo/?fbid=122315789156250015 | 新藝芳歌劇團｜《金蟾緣》｜高雄中山堂劇場戶外陽光草坪｜2026-12-03 正戲 19:00 |  | approve：原文「12/03（四）新藝芳歌劇團《金蟾緣》」，2026-12-03 為週四；時間、地點、免費出自同貼文共同欄位。 | rejected badgeType-not-free |
| chg-006 | add | https://www.facebook.com/photo/?fbid=122315789156250015 | 佩儀歌劇團｜《吳漢殺妻》｜高雄中山堂劇場戶外陽光草坪｜2026-12-04 正戲 19:00 |  | approve：原文「12/04（五）佩儀歌劇團《吳漢殺妻》」，2026-12-04 為週五；時間、地點、免費出自同貼文共同欄位。 | rejected badgeType-not-free |
| chg-007 | add | https://www.facebook.com/photo/?fbid=122315789156250015 | 文惜歌仔戲劇團｜《焰火長槍：火帥與玉龍的背影》｜高雄中山堂劇場戶外陽光草坪｜2026-12-05 正戲 19:00 |  | approve：原文「12/05（六）文惜歌仔戲劇團《焰火長槍：火帥與玉龍的背影》」，2026-12-05 為週六；時間、地點、免費出… | rejected badgeType-not-free |
| chg-008 | add | https://www.facebook.com/photo/?fbid=122315789156250015 | 繡花園戲劇團｜《姜子牙下山》｜高雄中山堂劇場戶外陽光草坪｜2026-12-06 正戲 19:00 |  | approve：原文「12/06（日）繡花園戲劇團《姜子牙下山》」，2026-12-06 為週日；時間、地點、免費出自同貼文共同欄位。 | rejected badgeType-not-free |
| chg-009 | add | https://www.facebook.com/photo/?fbid=122315789156250015 | 春明歌劇團｜《玉虛戰歌．天命之戰》｜高雄中山堂劇場戶外陽光草坪｜2026-12-11 正戲 19:00 |  | approve：原文「12/11（五）春明歌劇團《玉虛戰歌．天命之戰》」，2026-12-11 為週五；時間、地點、免費出自同貼文共同… | rejected badgeType-not-free |
| chg-010 | add | https://www.facebook.com/photo/?fbid=122315789156250015 | 水錦歌劇團｜《對面夫妻～韋馱與觀音》｜高雄中山堂劇場戶外陽光草坪｜2026-12-12 正戲 19:00 |  | approve：原文「12/12（六）水錦歌劇團《對面夫妻～韋馱與觀音》」，2026-12-12 為週六；時間、地點、免費出自同貼文共… | rejected badgeType-not-free |
| chg-011 | add | https://www.facebook.com/photo/?fbid=122315789156250015 | 明華園星字戲劇團｜《斷案青天－陰錯陽差》｜高雄中山堂劇場戶外陽光草坪｜2026-12-13 正戲 19:00 |  | approve：原文「12/13（日）明華園星字戲劇團《斷案青天－陰錯陽差》」，2026-12-13 為週日；時間、地點、免費出自同貼… | rejected badgeType-not-free |
| chg-012 | add | https://www.facebook.com/MingHuaYuanTianTaiwaneseOpera/reels_tab | 明華園天字戲劇團｜東隆宮外台演出｜高雄市鳳山區林森路60巷49號【東隆宮】｜2026-12-08 正戲 未公布 |  | approve：親看高解析戲路表（ac743edd…jpg）：「10/30 12/08 二 高雄市鳳山區林森路60巷49號【東隆宮】農… | added  |
| chg-013 | add（查證成立） | http://karensie.blogspot.com/2015/12/1041224.html（原貼文 https://www.opentix.life/event/2080109546140397568） | 一心戲劇團｜《閻王的假期》｜臺北市藝文推廣處城市舞台｜2026-12-05 正戲 14:30、2026-12-06 正戲 14:30 |  | approve：部落格售票彙整（115/11/07更）原文「12/05(六)-12/06(日)14:30 一心戲劇團 《閻王的假期》 … | rejected badgeType-not-ticket |
| chg-014 | add（查證成立） | http://karensie.blogspot.com/2015/12/1041224.html（原貼文 https://www.opentix.life/event/2112431894778032129） | 奇巧劇團｜《鞍馬天狗》十週年慶生派對｜臺南文創園區 漂丿白鷺live house｜2026-12-06 正戲 15:00、2026-12-06 正戲 19:00 |  | needs-check：原文「12/06(日)15:00&19:00奇巧劇團《鞍馬天狗》十週年慶生派對 KURAMA TENGU -The 1… | held  |
| chg-015 | update（查證成立） | https://web.ncku.edu.tw/p/406-1000-299280,r4153.php?Lang=zh-tw（原貼文 https://www.facebook.com/MingHuaYuanTianTaiwaneseOpera/reels_tab） | 明華園天字戲劇團｜《喜脈緣》｜成大校園｜2026-11-24 正戲 19:00 |  | needs-check：提案把 location 由現卡「成功大學校園(歷史系館前方小廣場)」改為較籠統的「成大校園」，屬資訊退化；且成大頁面… | held  |

## 遠期場次（超過 120 天，進入 120 天內自動重驗）

| 貼文 | 內容 |
| --- | --- |
| https://www.facebook.com/photo/?fbid=1560228489482771 | 明華園天字戲劇團｜《重返：愛河戀夢》｜臺灣戲曲中心 大表演廳｜2027-06-05、2027-06-06 |
| https://www.facebook.com/MingHuaYuanTianTaiwaneseOpera/reels_tab | 明華園天字戲劇團｜《重返：愛河戀夢》｜臺灣戲曲中心 大表演廳｜2027-06-05、2027-06-06 |
| https://www.threads.com/@taiwaneseopera168/post/DfWAAt6CT5a | 烏貓戲出｜《白賊七》｜高雄中山堂劇場(高雄市左營區實踐路71號)｜2027-04-17、2027-04-18 |
| https://www.threads.com/@taiwaneseopera168/post/DfWAAt6CT5a | 薪傳歌仔戲劇團｜《封神榜．文王食子》｜高雄中山堂劇場(高雄市左營區實踐路71號)｜2027-04-24、2027-04-25 |
| https://www.threads.com/@taiwaneseopera168/post/DfWAAt6CT5a | 燕玲戲劇團｜《韓信設窖安軍心》｜高雄中山堂劇場(高雄市左營區實踐路71號)｜2027-03-20、2027-03-21 |
| https://www.threads.com/@jing__1017/post/DfzIPO8E6F0 | 燕玲戲劇團｜《韓信設窖安軍心》｜高雄中山堂劇場｜2027-03-20、2027-03-21 |
| https://www.threads.com/@jing__1017/post/DfzIPO8E6F0 | 烏貓戲出｜《白賊七》｜高雄中山堂劇場｜2027-04-17、2027-04-18 |
| https://www.threads.com/@jing__1017/post/DfzIPO8E6F0 | 薪傳歌仔戲劇團｜《封神榜·文王食子》｜高雄中山堂劇場｜2027-04-24、2027-04-25 |

## 紀錄檔

- 本輪狀態：/Users/eric/aiwork/taiwan-opera-calendar/patrol_state/runs/2026-11-17_0904/state.json
- 巡檢紀錄：patrol_runs/2026-11-17_0904.json（/Users/eric/aiwork/taiwan-opera-calendar）
- 證據：patrol_evidence/2026-11-17_0904/
- 產生時間：2026-11-17T09:40:27+08:00
