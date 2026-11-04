# 巡檢報告 2026-11-05_0311（patrol-v2，正式）

## 結論

| 項目 | 結果 |
| --- | --- |
| 執行 | 開始 2026-11-05T03:11:31+08:00；結果 進行中；步驟 preflight:done、collect:done、pack:done、judge:done、check:done、verify:done、review:done、apply:done、publish:done、report:running |
| 來源 | 20 個：完整 2、部分 18、失敗 0、未讀 0 |
| 資料 | 送判讀 224 篇／圖 1 張；變更提案 35、確認一致 26、送查證 53（成立 8、與卡相同 5、查無佐證不收 44）、退回 0、漏處置 0；已過期不收 75、遠期暫存 2 |
| 寫入 | 寫入 8、add_card 拒絕 16、審查未通過 11 |
| 發布 | verified；SHA 1eaa53236943b4b68ba93767122b17ac1563f829；Actions 41901248822 |

## 模型與用量

| 角色 | 模型 | 依據 |
| --- | --- | --- |
| main | claude-sonnet-5-5 | get_session self：effort=medium |
| judge | sonnet | Agent 工具 model 參數；effort=medium |
| verify | opus | Agent 工具 model 參數；effort=medium |
| review | opus | Agent 工具 model 參數；effort=medium |

- 判讀批次 9；送出貼文 224 篇、圖片 1 張、正文約 75791 字
- 略過（已判讀未變動）148 篇；窗口外 21 篇
- 第二次審查：有（35 項）

## 來源

| 來源 | 狀態 | 範圍 | 說明 |
| --- | --- | --- | --- |
| threads:joe_huang_k_w | 部分 | 首屏 5 篇、累積 8 篇；最新 2026-11-03T21:56:59+08:00、最舊 2026-10-26T21:28:30+08:00；捲動 1 次、停止原因 reached-window；圖片下載 13 張 | 不變式通過；證據 /Users/eric/aiwork/taiwan-opera-calendar/patrol_evidence/2026-11-05_0311/threads_joe_huang… |
| threads:h.akito_1996 | 部分 | 首屏 4 篇、累積 10 篇；最新 2026-11-04T17:59:03+08:00、最舊 2026-09-27T00:04:33+08:00；捲動 3 次、停止原因 reached-window；圖片下載 9 張 | 不變式通過；證據 /Users/eric/aiwork/taiwan-opera-calendar/patrol_evidence/2026-11-05_0311/threads_h.akito_1… |
| threads:the_rin.lpm | 部分 | 首屏 4 篇、累積 7 篇；最新 2026-11-04T19:56:52+08:00、最舊 2026-09-26T14:32:03+08:00；捲動 2 次、停止原因 reached-window；圖片下載 8 張 | 不變式通過；證據 /Users/eric/aiwork/taiwan-opera-calendar/patrol_evidence/2026-11-05_0311/threads_the_rin.l… |
| threads:xuefeng_lu_ | 完整 | 7 天窗口讀完（停止原因 reached-window）；窗口內 4 篇皆有處置；圖片 0 張皆已判讀 | 不變式通過、逐篇處置完成 |
| threads:yuzhongluo | 部分 | 首屏 4 篇、累積 10 篇；最新 2026-11-04T13:27:13+08:00、最舊 2026-10-28T23:34:12+08:00；捲動 3 次、停止原因 reached-window；圖片下載 25 張 | 不變式通過；證據 /Users/eric/aiwork/taiwan-opera-calendar/patrol_evidence/2026-11-05_0311/threads_yuzhonglu… |
| threads:taiwaneseopera168 | 部分 | 首屏 5 篇、累積 40 篇；最新 2026-11-04T19:44:04+08:00、最舊 2026-08-16T02:33:12+08:00；捲動 20 次、停止原因 max-scrolls；圖片下載 33 張 | 不變式通過；證據 /Users/eric/aiwork/taiwan-opera-calendar/patrol_evidence/2026-11-05_0311/threads_taiwanese… |
| threads:jing__1017 | 部分 | 首屏 5 篇、累積 46 篇；最新 2026-11-04T22:07:26+08:00、最舊 2026-10-28T19:50:21+08:00；捲動 17 次、停止原因 reached-window；圖片下載 40 張 | 不變式通過；證據 /Users/eric/aiwork/taiwan-opera-calendar/patrol_evidence/2026-11-05_0311/threads_jing__101… |
| threads:hilang.on.tour | 完整 | 7 天窗口讀完（停止原因 reached-window）；窗口內 0 篇皆有處置；圖片 0 張皆已判讀 | 不變式通過、逐篇處置完成 |
| threads:yolin1991 | 部分 | 首屏 4 篇、累積 7 篇；最新 2026-11-04T17:09:46+08:00、最舊 2026-10-28T18:34:21+08:00；捲動 2 次、停止原因 reached-window；圖片下載 7 張 | 不變式通過；證據 /Users/eric/aiwork/taiwan-opera-calendar/patrol_evidence/2026-11-05_0311/threads_yolin1991… |
| facebook:sunhope.fans | 部分 | 首屏 2 篇、累積 19 篇；最新 無、最舊 無；捲動 20 次、停止原因 max-scrolls；圖片下載 26 張 | 不變式通過；證據 /Users/eric/aiwork/taiwan-opera-calendar/patrol_evidence/2026-11-05_0311/facebook_sunhope.… |
| facebook:HsiaoHsiYuan1913 | 部分 | 首屏 3 篇、累積 23 篇；最新 無、最舊 無；捲動 20 次、停止原因 max-scrolls；圖片下載 38 張 | 不變式通過；證據 /Users/eric/aiwork/taiwan-opera-calendar/patrol_evidence/2026-11-05_0311/facebook_HsiaoHsi… |
| facebook:100063868113954 | 部分 | 首屏 1 篇、累積 22 篇；最新 無、最舊 無；捲動 20 次、停止原因 max-scrolls；圖片下載 60 張 | 不變式通過；證據 /Users/eric/aiwork/taiwan-opera-calendar/patrol_evidence/2026-11-05_0311/facebook_10006386… |
| facebook:MingHuaYuanTianTaiwaneseOpera | 部分 | 首屏 1 篇、累積 22 篇；最新 無、最舊 無；捲動 20 次、停止原因 max-scrolls；圖片下載 65 張 | 不變式通過；證據 /Users/eric/aiwork/taiwan-opera-calendar/patrol_evidence/2026-11-05_0311/facebook_MingHuaY… |
| facebook:61574134933376 | 部分 | 首屏 2 篇、累積 19 篇；最新 無、最舊 無；捲動 20 次、停止原因 max-scrolls；圖片下載 34 張 | 不變式通過；證據 /Users/eric/aiwork/taiwan-opera-calendar/patrol_evidence/2026-11-05_0311/facebook_61574134… |
| facebook:mhysun | 部分 | 首屏 3 篇、累積 19 篇；最新 無、最舊 無；捲動 20 次、停止原因 max-scrolls；圖片下載 66 張 | 不變式通過；證據 /Users/eric/aiwork/taiwan-opera-calendar/patrol_evidence/2026-11-05_0311/facebook_mhysun.j… |
| facebook:61594936681482 | 部分 | 首屏 1 篇、累積 7 篇；最新 無、最舊 無；捲動 7 次、停止原因 no-new-after-3；圖片下載 23 張 | 不變式通過；證據 /Users/eric/aiwork/taiwan-opera-calendar/patrol_evidence/2026-11-05_0311/facebook_61594936… |
| facebook:lanyang.opera | 部分 | 首屏 1 篇、累積 22 篇；最新 無、最舊 無；捲動 20 次、停止原因 max-scrolls；圖片下載 37 張 | 不變式通過；證據 /Users/eric/aiwork/taiwan-opera-calendar/patrol_evidence/2026-11-05_0311/facebook_lanyang.… |
| facebook:Taichungpuppettheater | 部分 | 首屏 1 篇、累積 27 篇；最新 無、最舊 無；捲動 20 次、停止原因 max-scrolls；圖片下載 46 張 | 不變式通過；證據 /Users/eric/aiwork/taiwan-opera-calendar/patrol_evidence/2026-11-05_0311/facebook_Taichung… |
| culture | 部分 | total 1316、fetchedAt 2026-11-04T10:51:44+08:00、戲曲紀錄 27 筆 | 資料新鮮；逐筆處置待判讀後確認 |
| issues | 部分 | state=all 共 3 則（含留言） | 已讀取；處置待判讀後確認 |

- OPENTIX：sitemap 854 個活動、本輪有變 547、抓取 250、戲曲相關且未過期 44、延後 297、錯誤 0

## 卡片變更

| 編號 | 動作 | 來源 | 內容 | 差異 | 審查 | 寫入 |
| --- | --- | --- | --- | --- | --- | --- |
| chg-001 | add | https://www.threads.com/@taiwaneseopera168/post/DfQ5lKaiQVF | 小金枝歌劇團｜《棄老山傳奇》｜高雄中山堂劇場戶外陽光草坪｜2026-11-27 正戲 19:00 |  | reject：與 chg-011 為同一場（11/27 小金枝歌劇團《棄老山傳奇》高雄中山堂草坪 19:00），兩筆皆 action… | held  |
| chg-002 | add | https://www.threads.com/@taiwaneseopera168/post/DfQ5lKaiQVF | 新和興總團｜《秦英掛帥》｜高雄中山堂劇場戶外陽光草坪｜2026-11-28 正戲 19:00 |  | reject：與 chg-012 重複（11/28 新和興總團《秦英掛帥》19:00），兩筆皆 add；保留主辦 FB 來源的 ch… | held  |
| chg-003 | add | https://www.threads.com/@taiwaneseopera168/post/DfQ5lKaiQVF | 藝華園戲劇團｜《八仙傳奇－張果老與藍采和》｜高雄中山堂劇場戶外陽光草坪｜2026-11-29 正戲 19:00 |  | reject：與 chg-013 重複（11/29 藝華園戲劇團《八仙傳奇－張果老與藍采和》19:00），兩筆皆 add；保留 ch… | held  |
| chg-004 | add | https://www.threads.com/@taiwaneseopera168/post/DfQ5lKaiQVF | 新藝芳歌劇團｜《金蟾緣》｜高雄中山堂劇場戶外陽光草坪｜2026-12-03 正戲 19:00 |  | reject：與 chg-014 重複（12/03 新藝芳歌劇團《金蟾緣》19:00），兩筆皆 add；保留 chg-014，本筆來… | held  |
| chg-005 | add | https://www.threads.com/@taiwaneseopera168/post/DfQ5lKaiQVF | 佩儀歌劇團｜《吳漢殺妻》｜高雄中山堂劇場戶外陽光草坪｜2026-12-04 正戲 19:00 |  | reject：與 chg-015 重複（12/04 佩儀歌劇團《吳漢殺妻》19:00），兩筆皆 add；保留 chg-015，本筆來… | held  |
| chg-006 | add | https://www.threads.com/@taiwaneseopera168/post/DfQ5lKaiQVF | 文惜歌仔戲劇團｜《焰火長槍：火帥與玉龍的背影》｜高雄中山堂劇場戶外陽光草坪｜2026-12-05 正戲 19:00 |  | reject：與 chg-016 重複（12/05 文惜歌仔戲劇團《焰火長槍：火帥與玉龍的背影》19:00），兩筆皆 add；保留 … | held  |
| chg-007 | add | https://www.threads.com/@taiwaneseopera168/post/DfQ5lKaiQVF | 繡花園戲劇團｜《姜子牙下山》｜高雄中山堂劇場戶外陽光草坪｜2026-12-06 正戲 19:00 |  | reject：與 chg-017 重複（12/06 繡花園戲劇團《姜子牙下山》19:00），兩筆皆 add；保留 chg-017，本… | held  |
| chg-008 | add | https://www.threads.com/@taiwaneseopera168/post/DfQ5lKaiQVF | 春明歌劇團｜《玉虛戰歌．天命之戰》｜高雄中山堂劇場戶外陽光草坪｜2026-12-11 正戲 19:00 |  | reject：與 chg-018 重複（12/11 春明歌劇團《玉虛戰歌．天命之戰》19:00），兩筆皆 add；保留 chg-01… | held  |
| chg-009 | add | https://www.threads.com/@taiwaneseopera168/post/DfQ5lKaiQVF | 水錦歌劇團｜《對面夫妻～韋馱與觀音》｜高雄中山堂劇場戶外陽光草坪｜2026-12-12 正戲 19:00 |  | reject：與 chg-019 重複（12/12 水錦歌劇團《對面夫妻～韋馱與觀音》19:00），兩筆皆 add；保留 chg-0… | held  |
| chg-010 | add | https://www.threads.com/@taiwaneseopera168/post/DfQ5lKaiQVF | 明華園星字戲劇團｜《斷案青天－陰錯陽差》｜高雄中山堂劇場戶外陽光草坪｜2026-12-13 正戲 19:00 |  | reject：與 chg-020 重複（12/13 明華園星字戲劇團《斷案青天－陰錯陽差》19:00），兩筆皆 add；保留 chg… | held  |
| chg-011 | add | https://www.facebook.com/photo/?fbid=122315789156250015 | 小金枝歌劇團｜《棄老山傳奇》｜高雄中山堂劇場戶外陽光草坪｜2026-11-27 正戲 19:00 |  | approve：主辦臺灣歌仔戲中心 FB 原文『11/27（五）小金枝歌劇團《棄老山傳奇》』『每場次開演時間｜19:00』『演出地點｜… | rejected badgeType-not-free |
| chg-012 | add | https://www.facebook.com/photo/?fbid=122315789156250015 | 新和興總團｜《秦英掛帥》｜高雄中山堂劇場戶外陽光草坪｜2026-11-28 正戲 19:00 |  | approve：原文『11/28（六）新和興總團《秦英掛帥》』，19:00、地點、免費皆出自原文；11/28 為週六相符。 | rejected badgeType-not-free |
| chg-013 | add | https://www.facebook.com/photo/?fbid=122315789156250015 | 藝華園戲劇團｜《八仙傳奇－張果老與藍采和》｜高雄中山堂劇場戶外陽光草坪｜2026-11-29 正戲 19:00 |  | approve：原文『11/29（日）藝華園戲劇團《八仙傳奇－張果老與藍采和》』，19:00、地點、免費相符；11/29 為週日。 | rejected badgeType-not-free |
| chg-014 | add | https://www.facebook.com/photo/?fbid=122315789156250015 | 新藝芳歌劇團｜《金蟾緣》｜高雄中山堂劇場戶外陽光草坪｜2026-12-03 正戲 19:00 |  | approve：原文『12/03（四）新藝芳歌劇團《金蟾緣》』，19:00、地點、免費相符；12/03 為週四。 | rejected badgeType-not-free |
| chg-015 | add | https://www.facebook.com/photo/?fbid=122315789156250015 | 佩儀歌劇團｜《吳漢殺妻》｜高雄中山堂劇場戶外陽光草坪｜2026-12-04 正戲 19:00 |  | approve：原文『12/04（五）佩儀歌劇團《吳漢殺妻》』，19:00、地點、免費相符；12/04 為週五。 | rejected badgeType-not-free |
| chg-016 | add | https://www.facebook.com/photo/?fbid=122315789156250015 | 文惜歌仔戲劇團｜《焰火長槍：火帥與玉龍的背影》｜高雄中山堂劇場戶外陽光草坪｜2026-12-05 正戲 19:00 |  | approve：原文『12/05（六）文惜歌仔戲劇團《焰火長槍：火帥與玉龍的背影》』，19:00、地點、免費相符；12/05 為週六。 | rejected badgeType-not-free |
| chg-017 | add | https://www.facebook.com/photo/?fbid=122315789156250015 | 繡花園戲劇團｜《姜子牙下山》｜高雄中山堂劇場戶外陽光草坪｜2026-12-06 正戲 19:00 |  | approve：原文『12/06（日）繡花園戲劇團《姜子牙下山》』，19:00、地點、免費相符；12/06 為週日。 | rejected badgeType-not-free |
| chg-018 | add | https://www.facebook.com/photo/?fbid=122315789156250015 | 春明歌劇團｜《玉虛戰歌．天命之戰》｜高雄中山堂劇場戶外陽光草坪｜2026-12-11 正戲 19:00 |  | approve：原文『12/11（五）春明歌劇團《玉虛戰歌．天命之戰》』，19:00、地點、免費相符；12/11 為週五。 | rejected badgeType-not-free |
| chg-019 | add | https://www.facebook.com/photo/?fbid=122315789156250015 | 水錦歌劇團｜《對面夫妻～韋馱與觀音》｜高雄中山堂劇場戶外陽光草坪｜2026-12-12 正戲 19:00 |  | approve：原文『12/12（六）水錦歌劇團《對面夫妻～韋馱與觀音》』，19:00、地點、免費相符；12/12 為週六。 | rejected badgeType-not-free |
| chg-020 | add | https://www.facebook.com/photo/?fbid=122315789156250015 | 明華園星字戲劇團｜《斷案青天－陰錯陽差》｜高雄中山堂劇場戶外陽光草坪｜2026-12-13 正戲 19:00 |  | approve：原文『12/13（日）明華園星字戲劇團《斷案青天－陰錯陽差》』，19:00、地點、免費相符；12/13 為週日。 | rejected badgeType-not-free |
| chg-021 | add | https://www.facebook.com/lanyang.opera/reels_tab | 蘭陽戲劇團｜《錯配姻緣》｜新城紫雲宮（宜蘭縣蘇澳鎮新城里新城南路175號）｜2026-11-07 正戲 18:30 |  | approve：蘭陽戲劇團官方 11 月行程：『11/7（六）晚上6:30』『劇目｜《錯配姻緣》』『地點｜新城紫雲宮（宜蘭縣蘇澳鎮新城… | added  |
| chg-022 | add | https://www.facebook.com/lanyang.opera/reels_tab | 蘭陽戲劇團｜《錯配姻緣》｜嶺腳永安宮（宜蘭縣蘇澳鎮港邊里嶺腳路104號）｜2026-11-22 正戲 18:00 |  | approve：原文『11/22（日）晚上6:00』『《錯配姻緣》』『嶺腳永安宮（宜蘭縣蘇澳鎮港邊里嶺腳路104號）』『免費觀賞』；與… | added  |
| chg-023 | add | https://www.facebook.com/lanyang.opera/reels_tab | 蘭陽戲劇團｜《福氣臨門》｜大湖普恩廟（宜蘭縣員山鄉逸仙村大安路121號）｜2026-11-23 正戲 18:30 |  | approve：原文『11/23（一）晚上6:30』『《福氣臨門》』『大湖普恩廟（宜蘭縣員山鄉逸仙村大安路121號）』『免費觀賞』；1… | added  |
| chg-024 | add | https://www.facebook.com/lanyang.opera/reels_tab | 蘭陽戲劇團｜《求草救夫》｜利澤簡永安宮（宜蘭縣五結鄉利澤村利澤路26號）｜2026-11-26 正戲 19:30 |  | approve：原文『11/26（四）晚上7:30』『《求草救夫》』『利澤簡永安宮（宜蘭縣五結鄉利澤村利澤路26號）』『免費觀賞』；1… | added  |
| chg-025 | add | https://www.opentix.life/event/2042431673524826113 | 吳萬響掌中劇團｜雲林奇譚麥寮借屍還魂｜雲林表演廳｜2026-11-29 正戲 14:30 |  | approve：OPENTIX『主辦：吳萬響掌中劇團』『場次：2026-11-29 14:30｜地點：雲林表演廳』『票價：100元』；… | added  |
| chg-026 | update | https://www.opentix.life/event/2079821135483363329 | 明華園戲劇總團｜《烏龍天下》｜臺中國家歌劇院大劇院｜2026-12-05 正戲 14:30、2026-12-06 正戲 14:30 | time：卡 未公布 → 文 2026-12-05 正戲 14:30；time：卡 未公布 → 文 2026-12-06 正戲 14:30 | approve：currentCard 時間為『未公布』，OPENTIX 活動頁（即卡片 link 同一 event 20798211… | updated  |
| chg-027 | add | https://www.opentix.life/event/2041775304994054145 | 五洲勝義閣掌中劇團｜《原來你佇咧》｜米倉劇場｜2026-12-12 正戲 14:30 |  | approve：OPENTIX『主辦：五洲勝義閣掌中劇團』『場次：2026-12-12 14:30｜地點：米倉劇場（桃園市桃園區新生路… | added  |
| chg-028 | change（查證成立） | https://n.yam.com/Article/20261026226244（原貼文 https://www.threads.com/@jing__1017/post/DfFOKfrCWgq） | 秀琴歌劇團｜《玉石變》｜新北市新莊區莊泰路與國營路交叉口（保元宮建醮總醮壇）｜2026-11-07 扮仙 18:30、2026-11-07 正戲 19:00 | time：卡 19:00 → 文 2026-11-07 扮仙 18:30；location：卡 新北市新莊區中正路143號（保元宮） → 文 新北市新莊區莊泰路與國營路交叉口（保元宮建醮總醮壇） | approve：蕃新聞 2026-10-26 報導引保元宮官方藝文醮海報：『同一天的總醮壇，則由秀琴歌劇團演出。18:30至19:00… | rejected location-not-in-quote |
| chg-029 | add（查證成立） | https://www.opentix.life/event/2090269380048343041（原貼文 https://www.opentix.life/event/2090269380048343041） | 民權歌劇團｜《鐵弓緣》選段｜臺灣戲曲中心小舞台｜2026-11-06 正戲 19:30 |  | approve：OPENTIX（主辦國立傳統藝術中心）『【小舞台】11/06（五）19:30 民權歌劇團《鐵弓緣》選段』；民權歌劇團為… | rejected location-not-in-quote,badgeType-not-ticket |
| chg-030 | add（查證成立） | https://www.opentix.life/event/2090269380048343041（原貼文 https://www.opentix.life/event/2090269380048343041） | 臺北木偶劇團｜《雷萬春打虎》｜臺灣戲曲中心小舞台｜2026-11-08 正戲 14:30 |  | approve：同頁『11/08（日）14:30 臺北木偶劇團《雷萬春打虎》』列於【小舞台】，地點、時間未與其他場錯配。臺北木偶劇團為… | rejected location-not-in-quote,badgeType-not-ticket |
| chg-031 | add（查證成立） | https://www.opentix.life/event/2090269380048343041（原貼文 https://www.opentix.life/event/2090269380048343041） | 一心戲劇團｜經典折子《借扇》、《秀嬋申冤》、《虹霓關》｜臺灣戲曲中心小表演廳｜2026-11-07 正戲 14:30 |  | approve：同頁『【小表演廳】11/07（六）14:30 一心戲劇團 經典折子《借扇》、《秀嬋申冤》、《虹霓關》』；地點正確歸於小… | rejected location-not-in-quote,badgeType-not-ticket |
| chg-032 | add（查證成立） | https://www.opentix.life/event/2090269380048343041（原貼文 https://www.opentix.life/event/2090269380048343041） | 薪傳歌仔戲劇團｜《蒼原孤雁》｜臺灣戲曲中心小表演廳｜2026-11-14 正戲 14:30 |  | approve：同頁『【小表演廳】…11/14（六）14:30 薪傳歌仔戲劇團《蒼原孤雁》』；地點小表演廳、時間相符，11/14 為週… | rejected location-not-in-quote,badgeType-not-ticket |
| chg-033 | add（查證成立） | https://kinotw.com/show/moc-6aaacec826b324165c32e41c-dba40c9c（原貼文 https://www.opentix.life/event/2099337927309197313） | 烏貓戲出｜《燈殼樓的委託-小戲蟲拜先生》｜大稻埕戲苑曲藝場｜2026-11-28 正戲 11:00、2026-11-28 正戲 14:30、2026-11-29 正戲 11:00、2026-11-29 正戲 14:30、2026-12-1… |  | approve：KinoTW 頁：烏貓戲出《燈殼樓的委託-小戲蟲拜先生》大稻埕戲苑曲藝場，『11/28（週六）11:00 14:30 … | added  |
| chg-034 | add（查證成立） | https://kinotw.com/show/moc-6a7a050026b32427d06043a4-83f10878（原貼文 https://www.opentix.life/event/2080109546140397568） | 一心戲劇團｜《閻王的假期》｜臺北市藝文推廣處城市舞台｜2026-12-05 正戲 14:30、2026-12-06 正戲 14:30 |  | approve：KinoTW 頁：一心戲劇團《閻王的假期》臺北市藝文推廣處城市舞台，『12/5（週六）14:30 12/6（週日）14… | rejected artist-not-in-quote |
| chg-035 | add（查證成立） | https://kinotw.com/show/moc-6ada44bd26b3245efc75370e-52244a29（原貼文 https://www.opentix.life/event/2112431894778032129） | 奇巧劇團｜《鞍馬天狗》十週年慶生派對｜臺南文創園區 漂丿白鷺live house｜2026-12-06 正戲 15:00、2026-12-06 正戲 19:00 |  | needs-check：日期 12/6、15:00／19:00、地點臺南文創園區漂丿白鷺 live house 與原文相符；但節目是『十週年慶… | held  |

## 遠期場次（超過 120 天，進入 120 天內自動重驗）

| 貼文 | 內容 |
| --- | --- |
| https://www.facebook.com/photo/?fbid=1560228489482771 | 明華園天字戲劇團｜《重返：愛河戀夢》｜臺灣戲曲中心 大表演廳｜2027-06-05、2027-06-06 |
| https://www.facebook.com/MingHuaYuanTianTaiwaneseOpera/reels_tab | 明華園天字戲劇團｜《重返：愛河戀夢》｜臺灣戲曲中心 大表演廳｜2027-06-05、2027-06-06 |

## 紀錄檔

- 本輪狀態：/Users/eric/aiwork/taiwan-opera-calendar/patrol_state/runs/2026-11-05_0311/state.json
- 巡檢紀錄：patrol_runs/2026-11-05_0311.json（/Users/eric/aiwork/taiwan-opera-calendar）
- 證據：patrol_evidence/2026-11-05_0311/
- 產生時間：2026-11-05T03:54:10+08:00
