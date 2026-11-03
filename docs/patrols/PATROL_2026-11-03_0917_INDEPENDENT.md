# 巡檢報告 2026-11-03_0917（patrol-v2，正式）

## 結論

| 項目 | 結果 |
| --- | --- |
| 執行 | 開始 2026-11-03T09:17:12+08:00；結果 進行中；步驟 preflight:done、collect:done、pack:done、judge:done、check:done、review:done、apply:done、publish:done、report:running |
| 來源 | 20 個：完整 2、部分 18、失敗 0、未讀 0 |
| 資料 | 送判讀 262 篇／圖 18 張；變更提案 6、確認一致 23、待查 38、退回 0、漏處置 0 |
| 寫入 | 寫入 2、add_card 拒絕 3、審查未通過 1 |
| 發布 | verified；SHA 7a5a06b75c882bfcce9311ed66074af6e158c475；Actions 41561536940 |

## 模型與用量

| 角色 | 模型 | 依據 |
| --- | --- | --- |
| main | claude-opus-5-5 | /model 切換為 claude-opus-5-5（本對話）；get_session 早先回報 sonnet/medium 為切換前 |
| judge | sonnet | Agent 工具 model 參數；effort=medium |
| review | opus | Agent 工具 model 參數；effort=high |

- 判讀批次 11；送出貼文 262 篇、圖片 18 張、正文約 80747 字
- 略過（已判讀未變動）84 篇；窗口外 31 篇
- 第二次審查：有（6 項）

## 來源

| 來源 | 狀態 | 範圍 | 說明 |
| --- | --- | --- | --- |
| threads:joe_huang_k_w | 部分 | 首屏 5 篇、累積 8 篇；最新 2026-10-31T20:13:38+08:00、最舊 2026-10-25T21:42:54+08:00；捲動 1 次、停止原因 reached-window；圖片下載 13 張 | 不變式通過；證據 /Users/eric/aiwork/taiwan-opera-calendar/patrol_evidence/2026-11-03_0917/threads_joe_huang… |
| threads:h.akito_1996 | 部分 | 首屏 4 篇、累積 10 篇；最新 2026-10-31T21:49:49+08:00、最舊 2026-09-27T00:04:33+08:00；捲動 2 次、停止原因 reached-window；圖片下載 9 張 | 不變式通過；證據 /Users/eric/aiwork/taiwan-opera-calendar/patrol_evidence/2026-11-03_0917/threads_h.akito_1… |
| threads:the_rin.lpm | 部分 | 首屏 4 篇、累積 7 篇；最新 2026-11-01T20:37:03+08:00、最舊 2026-09-26T14:32:03+08:00；捲動 2 次、停止原因 reached-window；圖片下載 8 張 | 不變式通過；證據 /Users/eric/aiwork/taiwan-opera-calendar/patrol_evidence/2026-11-03_0917/threads_the_rin.l… |
| threads:xuefeng_lu_ | 完整 | 7 天窗口讀完（停止原因 reached-window）；窗口內 5 篇皆有處置；圖片 0 張皆已判讀 | 不變式通過、逐篇處置完成 |
| threads:yuzhongluo | 部分 | 首屏 4 篇、累積 12 篇；最新 2026-11-02T15:14:28+08:00、最舊 2026-10-26T14:14:27+08:00；捲動 4 次、停止原因 reached-window；圖片下載 13 張 | 不變式通過；證據 /Users/eric/aiwork/taiwan-opera-calendar/patrol_evidence/2026-11-03_0917/threads_yuzhonglu… |
| threads:taiwaneseopera168 | 部分 | 首屏 5 篇、累積 37 篇；最新 2026-11-02T20:03:30+08:00、最舊 2026-08-16T02:33:12+08:00；捲動 20 次、停止原因 max-scrolls；圖片下載 35 張 | 不變式通過；證據 /Users/eric/aiwork/taiwan-opera-calendar/patrol_evidence/2026-11-03_0917/threads_taiwanese… |
| threads:jing__1017 | 部分 | 首屏 5 篇、累積 41 篇；最新 2026-11-03T01:04:06+08:00、最舊 2026-10-27T01:24:02+08:00；捲動 15 次、停止原因 reached-window；圖片下載 34 張 | 不變式通過；證據 /Users/eric/aiwork/taiwan-opera-calendar/patrol_evidence/2026-11-03_0917/threads_jing__101… |
| threads:hilang.on.tour | 完整 | 7 天窗口讀完（停止原因 reached-window）；窗口內 0 篇皆有處置；圖片 0 張皆已判讀 | 不變式通過、逐篇處置完成 |
| threads:yolin1991 | 部分 | 首屏 4 篇、累積 8 篇；最新 2026-11-02T20:26:56+08:00、最舊 2026-10-24T10:49:47+08:00；捲動 2 次、停止原因 reached-window；圖片下載 8 張 | 不變式通過；證據 /Users/eric/aiwork/taiwan-opera-calendar/patrol_evidence/2026-11-03_0917/threads_yolin1991… |
| facebook:sunhope.fans | 部分 | 首屏 1 篇、累積 21 篇；最新 無、最舊 無；捲動 20 次、停止原因 max-scrolls；圖片下載 42 張 | 不變式通過；證據 /Users/eric/aiwork/taiwan-opera-calendar/patrol_evidence/2026-11-03_0917/facebook_sunhope.… |
| facebook:HsiaoHsiYuan1913 | 部分 | 首屏 1 篇、累積 24 篇；最新 無、最舊 無；捲動 20 次、停止原因 max-scrolls；圖片下載 50 張 | 不變式通過；證據 /Users/eric/aiwork/taiwan-opera-calendar/patrol_evidence/2026-11-03_0917/facebook_HsiaoHsi… |
| facebook:100063868113954 | 部分 | 首屏 3 篇、累積 21 篇；最新 無、最舊 無；捲動 20 次、停止原因 max-scrolls；圖片下載 48 張 | 不變式通過；證據 /Users/eric/aiwork/taiwan-opera-calendar/patrol_evidence/2026-11-03_0917/facebook_10006386… |
| facebook:MingHuaYuanTianTaiwaneseOpera | 部分 | 首屏 1 篇、累積 24 篇；最新 無、最舊 無；捲動 20 次、停止原因 max-scrolls；圖片下載 66 張 | 不變式通過；證據 /Users/eric/aiwork/taiwan-opera-calendar/patrol_evidence/2026-11-03_0917/facebook_MingHuaY… |
| facebook:61574134933376 | 部分 | 首屏 1 篇、累積 21 篇；最新 無、最舊 無；捲動 20 次、停止原因 max-scrolls；圖片下載 66 張 | 不變式通過；證據 /Users/eric/aiwork/taiwan-opera-calendar/patrol_evidence/2026-11-03_0917/facebook_61574134… |
| facebook:mhysun | 部分 | 首屏 1 篇、累積 19 篇；最新 無、最舊 無；捲動 20 次、停止原因 max-scrolls；圖片下載 83 張 | 不變式通過；證據 /Users/eric/aiwork/taiwan-opera-calendar/patrol_evidence/2026-11-03_0917/facebook_mhysun.j… |
| facebook:61594936681482 | 部分 | 首屏 1 篇、累積 7 篇；最新 無、最舊 無；捲動 8 次、停止原因 no-new-after-3；圖片下載 23 張 | 不變式通過；證據 /Users/eric/aiwork/taiwan-opera-calendar/patrol_evidence/2026-11-03_0917/facebook_61594936… |
| facebook:lanyang.opera | 部分 | 首屏 2 篇、累積 21 篇；最新 無、最舊 無；捲動 20 次、停止原因 max-scrolls；圖片下載 26 張 | 不變式通過；證據 /Users/eric/aiwork/taiwan-opera-calendar/patrol_evidence/2026-11-03_0917/facebook_lanyang.… |
| facebook:Taichungpuppettheater | 部分 | 首屏 3 篇、累積 26 篇；最新 無、最舊 無；捲動 20 次、停止原因 max-scrolls；圖片下載 24 張 | 不變式通過；證據 /Users/eric/aiwork/taiwan-opera-calendar/patrol_evidence/2026-11-03_0917/facebook_Taichung… |
| culture | 部分 | total 1287、fetchedAt 2026-11-02T10:01:43+08:00、戲曲紀錄 26 筆 | 資料新鮮；逐筆處置待判讀後確認 |
| issues | 部分 | state=all 共 3 則（含留言） | 已讀取；處置待判讀後確認 |

- OPENTIX：sitemap 847 個活動、本輪有變 803、抓取 250、戲曲相關且未過期 22、延後 553、錯誤 0

## 卡片變更

| 編號 | 動作 | 來源 | 內容 | 差異 | 審查 | 寫入 |
| --- | --- | --- | --- | --- | --- | --- |
| chg-001 | change（由「一致」轉） | https://www.threads.com/@the_rin.lpm/post/DfMv3UpE52E | 秀琴歌劇團｜《玉石變》｜首醮總醮壇（國營路&莊泰路交叉口，近輔大捷運站3號出口）｜2026-11-07 扮仙 18:30、2026-11-07 正戲 19:00 | time：卡 19:00 → 文 2026-11-07 扮仙 18:30；location：卡 新北市新莊區中正路143號（保元宮） → 文 首醮總醮壇（國營路&莊泰路交叉口，近輔大捷運站3號出口） | approve：source.text 明載「演出日期｜11月7日（星期六）」「演出地點｜首醮總醮壇（國營路&莊泰路交叉口，近輔大捷運… | rejected different-account,no-change-keyword |
| chg-002 | change（由「一致」轉） | https://www.threads.com/@jing__1017/post/DfFOKfrCWgq | 秀琴歌劇團｜《玉石變》｜首醮總醮壇（國營路&莊泰路交叉口，近輔大捷運站3號出口）｜2026-11-07 扮仙 18:30、2026-11-07 正戲 19:00 | time：卡 19:00 → 文 2026-11-07 扮仙 18:30；location：卡 新北市新莊區中正路143號（保元宮） → 文 首醮總醮壇（國營路&莊泰路交叉口，近輔大捷運站3號出口） | approve：source.text「11月7日首醮大普當晚，新莊保元宮隆重邀請「秀琴歌劇團」…《玉石變》」，演出資訊與 chg-0… | rejected different-account,no-change-keyword |
| chg-003 | add | https://www.threads.com/@yolin1991/post/DfPTgGSGshX | 新吉義林歌劇團｜高雄左營謝家濟公禪師聖誕外台演出｜高雄左營 謝家濟公禪師｜2026-11-07 正戲 未公布 |  | approve：原文「新吉義林歌劇團 演出資訊…演出日期：11月7日（六）⏰演出時間：待公布 📍演出地點：高雄左營 謝家濟公禪師」，海… | added  |
| chg-004 | add | https://www.threads.com/@yolin1991/post/DfPTgGSGshX | 新吉義林歌劇團｜雲林四湖參天宮廣場外台演出｜雲林四湖參天宮廣場｜2026-11-08 正戲 未公布、2026-11-09 正戲 未公布、2026-11-10 正戲 未公布、2026-11-11 正戲 未公布 |  | approve：同一篇新吉義林貼文寫「預告一下11/8-11/11 雲林四湖參天宮廣場 演出四天」，11/8、11/9、11/10、1… | added  |
| chg-005 | change（由「一致」轉） | https://www.facebook.com/photo/?fbid=1747812420683800 | 尚和歌仔戲劇團｜【驫•馬的心事】｜未公布｜2026-12-12 正戲 未公布、2026-12-13 正戲 未公布、2026-12-19 正戲 未公布、2026-12-20 正戲 未公布 | date：卡 2026/12/12（六）–12/13（日） → 文 2026-12-12、2026-12-13、2026-12-19、2026-12-20 | reject：目標卡 sh-2026-12-12-madexinshi-1 是《馬的心事－上》12/12–13，下集 12/19–2… | held  |
| chg-006 | change（由「一致」轉） | facebook:61574134933376:5a5635caeeb3 | 繡花園戲劇團｜《孫臏兵法》｜臺南市柳營區 柳營代天院｜2026-11-18 扮仙 19:00、2026-11-18 正戲 19:30 | time：卡 晚上 7:30 → 文 2026-11-18 扮仙 19:00 | approve：原文「演出日期｜2026/11/18（三）」「臺南市柳營區 柳營代天院（臺南市柳營區東昇里中山西路一段362號）」「晚… | rejected different-account,no-change-keyword |

## 待查與退回

| 類別 | 貼文 | 原因 | 說明 |
| --- | --- | --- | --- |
| 待查 | https://www.threads.com/@taiwaneseopera168/post/DfPQ0eniUAF | date-out-of-range |  |
| 待查 | https://www.threads.com/@taiwaneseopera168/post/DfPLvHzCZPU | date-out-of-range,time-not-in-quote |  |
| 待查 | https://www.threads.com/@taiwaneseopera168/post/DfMpM1kiehe | date-out-of-range |  |
| 待查 | https://www.threads.com/@taiwaneseopera168/post/DfMi-AbCdDo | date-out-of-range |  |
| 待查 | https://www.threads.com/@taiwaneseopera168/post/DfJ89egCajx | judge-needs-check | 布袋戲貼文正文為空且無圖，無法判讀 |
| 待查 | https://www.threads.com/@jing__1017/post/DfIHIDNEzTz | date-out-of-range |  |
| 待查 | https://www.threads.com/@jing__1017/post/DfH2FVyCar- | judge-needs-check | 崑曲扮仙工作坊介紹，正文無日期時間，細節在下一篇，且為已過日期 |
| 待查 | https://www.threads.com/@jing__1017/post/DfH2F_4iUk2 | judge-needs-check | 工作坊10/31已過，且無明確劇團、與歌仔戲關聯為間接，劇種看不出來 |
| 待查 | https://www.threads.com/@jing__1017/post/DfFPe2zidiO | judge-needs-check | 僅農曆9/22無國曆日期，無明確團名，且已過期 |
| 待查 | https://www.threads.com/@jing__1017/post/DfFJ-aHk3ng | judge-needs-check | 有日期與地點但無演出時間，且10/31、11/1均已過 |
| 待查 | https://www.threads.com/@jing__1017/post/DfCefnVCWiZ | date-out-of-range |  |
| 待查 | https://www.threads.com/@jing__1017/post/DfAWHhpk3Pm | date-out-of-range,date-not-in-quote |  |
| 待查 | https://www.facebook.com/sunhope.fans/reels_tab | date-not-in-quote |  |
| 待查 | https://www.facebook.com/permalink.php?story_fbid=pfbid031ihxSoBF3spkdTpaZLsNRebUk7xaz34qxmAGSxWeprXLiC8GLY6Wi1YA4PDBv9Q2l&id=61568887880066 | date-not-in-quote |  |
| 待查 | https://www.facebook.com/photo/?fbid=1659595476179374 | date-out-of-range |  |
| 待查 | https://www.facebook.com/photo/?fbid=1658401932965395 | date-out-of-range |  |
| 待查 | https://www.facebook.com/photo/?fbid=1655504973255091 | date-out-of-range |  |
| 待查 | https://www.facebook.com/photo/?fbid=1655155203290068 | date-out-of-range |  |
| 待查 | https://www.facebook.com/photo/?fbid=1654012383404350 | date-out-of-range |  |
| 待查 | https://www.facebook.com/photo/?fbid=1546668374148203 | judge-needs-check | 補助計畫名單公告，只有三週區間，沒有各團場次日期、時間 |
| 待查 | https://www.facebook.com/photo/?fbid=122179998656804497 | judge-needs-check | 農曆7月行程只有農曆日期、無年份與時間，無法換算 |
| 待查 | https://www.facebook.com/reel/1129849869722476/ | date-not-in-quote,time-not-in-quote |  |
| 待查 | https://www.facebook.com/photo/?fbid=1597080095765334 | date-not-in-quote,time-not-in-quote |  |
| 待查 | https://www.opentix.life/event/1863403624657735681 | judge-needs-check | 臺北戲棚為京劇、布袋戲、民俗技藝等綜合節目，各場次劇種未列，無法判斷哪些場次屬布袋戲。 |
| 待查 | https://www.opentix.life/event/2090269380048343041 | judge-needs-check | 育成聯合展演共 10 團，可見的簡介被截斷，看不出各場次劇團與劇目，無法確認與既有卡片《少年岳雲》的對應。 |
| 待查 | https://www.opentix.life/program/2080173157578416129 | puppet-not-budaixi |  |
| 待查 | https://www.opentix.life/program/2112035354878472193 | puppet-not-budaixi |  |
| 待查 | https://www.opentix.life/program/2088104133013299200 | judge-needs-check | 文化部紀錄僅見「偶偶偶劇團」與兒童劇名，無布袋／掌中證據，不可因名稱有偶就當布袋戲；既有卡片 moc-2088104133013299200-dec93f 劇種建議複查 |
| 待查 | https://github.com/eric1810-tw/taiwan-opera-calendar/issues/9 | judge-needs-check | 回報未寫劇團全名（僅「春美」）與劇種，多數場次無時間，且來源為 FB 連結無法驗證，不建卡 |
| 待查 | https://www.threads.com/@taiwaneseopera168/post/DfOgYAUCf4F | date-out-of-range,date-not-in-quote |  |
| 待查 | https://www.threads.com/@taiwaneseopera168/post/DfOgYAUCf4F | date-out-of-range,date-not-in-quote |  |
| 待查 | https://www.threads.com/@taiwaneseopera168/post/DfEdAMwEZOX | time-not-in-quote |  |
| 待查 | https://www.threads.com/@taiwaneseopera168/post/DfEdAMwEZOX | time-not-in-quote |  |
| 待查 | facebook:HsiaoHsiYuan1913:470934175033129 | image-illegible | 極度模糊，無法辨識任何文字 |
| 待查 | facebook:HsiaoHsiYuan1913:470934175033129 | image-illegible | 圖片低解析且被裁切，無日期 |
| 待查 | https://www.threads.com/@yolin1991/post/DfMBg4LGrm_ | judge-needs-check | 只寫「國曆11月第一站！大內」，無劇團、日期、時間，圖為自拍 |
| 待查 | https://www.facebook.com/photo/?fbid=3334478559932759 | judge-needs-check | 文字寫11月，但圖為109年舊海報(農曆9/22~23與2026年11/7-8不符)，來源矛盾 |
| 待查 | https://www.facebook.com/photo/?fbid=1534005115438442 | date-out-of-range,date-not-in-quote |  |

## 紀錄檔

- 本輪狀態：/Users/eric/aiwork/taiwan-opera-calendar/patrol_state/runs/2026-11-03_0917/state.json
- 巡檢紀錄：patrol_runs/2026-11-03_0917.json（/Users/eric/aiwork/taiwan-opera-calendar）
- 證據：patrol_evidence/2026-11-03_0917/
- 產生時間：2026-11-03T09:43:31+08:00
