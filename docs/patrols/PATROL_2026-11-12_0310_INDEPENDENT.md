# 巡檢報告 2026-11-12_0310（patrol-v2，正式）

## 需要 Eric 決定

- 判讀有 4 篇沒有逐篇處置，已列待查（見報告）

## 結論

| 項目 | 結果 |
| --- | --- |
| 執行 | 開始 2026-11-12T03:10:50+08:00；結果 進行中；步驟 preflight:done、collect:done、pack:done、judge:done、check:done、verify:done、review:done、apply:done、publish:done、report:running |
| 來源 | 20 個：完整 4、部分 16、失敗 0、未讀 0 |
| 資料 | 送判讀 209 篇／圖 18 張；變更提案 21、確認一致 17、送查證 58（成立 3、與卡相同 7、查無佐證不收 49）、退回 0、漏處置 4；已過期不收 80、遠期暫存 5 |
| 寫入 | 寫入 8、add_card 拒絕 11、審查未通過 2 |
| 發布 | verified；SHA 5198b7ff255fc2a8409f22868feaf3e63f5355f2；Actions 43091264088 |

## 模型與用量

| 角色 | 模型 | 依據 |
| --- | --- | --- |
| main | claude-sonnet-5-5 | get_session self：effort=medium |
| judge | sonnet | Agent 工具 model 參數；effort=medium |
| verify | opus | Agent 工具 model 參數；effort=medium |
| review | opus | Agent 工具 model 參數；effort=medium |

- 判讀批次 9；送出貼文 209 篇、圖片 18 張、正文約 72359 字
- 略過（已判讀未變動）105 篇；窗口外 30 篇
- 第二次審查：有（21 項）

## 來源

| 來源 | 狀態 | 範圍 | 說明 |
| --- | --- | --- | --- |
| threads:joe_huang_k_w | 部分 | 首屏 4 篇、累積 9 篇；最新 2026-11-11T21:25:43+08:00、最舊 2026-11-03T12:50:20+08:00；捲動 2 次、停止原因 reached-window；圖片下載 14 張 | 不變式通過；證據 /Users/eric/aiwork/taiwan-opera-calendar/patrol_evidence/2026-11-12_0310/threads_joe_huang… |
| threads:h.akito_1996 | 完整 | 7 天窗口讀完（停止原因 reached-window）；窗口內 0 篇皆有處置；圖片 0 張皆已判讀 | 不變式通過、逐篇處置完成 |
| threads:the_rin.lpm | 部分 | 首屏 4 篇、累積 10 篇；最新 2026-11-10T19:03:41+08:00、最舊 2026-09-26T14:32:03+08:00；捲動 3 次、停止原因 reached-window；圖片下載 15 張 | 不變式通過；證據 /Users/eric/aiwork/taiwan-opera-calendar/patrol_evidence/2026-11-12_0310/threads_the_rin.l… |
| threads:xuefeng_lu_ | 完整 | 7 天窗口讀完（停止原因 reached-window）；窗口內 3 篇皆有處置；圖片 0 張皆已判讀 | 不變式通過、逐篇處置完成 |
| threads:yuzhongluo | 部分 | 首屏 4 篇、累積 21 篇；最新 2026-11-12T02:52:37+08:00、最舊 2026-11-04T12:33:05+08:00；捲動 8 次、停止原因 reached-window；圖片下載 24 張 | 不變式通過；證據 /Users/eric/aiwork/taiwan-opera-calendar/patrol_evidence/2026-11-12_0310/threads_yuzhonglu… |
| threads:taiwaneseopera168 | 部分 | 首屏 3 篇、累積 43 篇；最新 2026-11-11T21:15:07+08:00、最舊 2026-08-16T02:33:12+08:00；捲動 20 次、停止原因 reached-window；圖片下載 83 張 | 不變式通過；證據 /Users/eric/aiwork/taiwan-opera-calendar/patrol_evidence/2026-11-12_0310/threads_taiwanese… |
| threads:jing__1017 | 部分 | 首屏 4 篇、累積 22 篇；最新 2026-11-11T23:24:18+08:00、最舊 2026-10-28T19:50:21+08:00；捲動 8 次、停止原因 reached-window；圖片下載 46 張 | 不變式通過；證據 /Users/eric/aiwork/taiwan-opera-calendar/patrol_evidence/2026-11-12_0310/threads_jing__101… |
| threads:hilang.on.tour | 完整 | 7 天窗口讀完（停止原因 reached-window）；窗口內 0 篇皆有處置；圖片 0 張皆已判讀 | 不變式通過、逐篇處置完成 |
| threads:yolin1991 | 部分 | 首屏 4 篇、累積 9 篇；最新 2026-11-11T11:21:57+08:00、最舊 2026-11-03T21:11:25+08:00；捲動 3 次、停止原因 reached-window；圖片下載 9 張 | 不變式通過；證據 /Users/eric/aiwork/taiwan-opera-calendar/patrol_evidence/2026-11-12_0310/threads_yolin1991… |
| facebook:sunhope.fans | 部分 | 首屏 3 篇、累積 20 篇；最新 無、最舊 無；捲動 20 次、停止原因 max-scrolls；圖片下載 26 張 | 不變式通過；證據 /Users/eric/aiwork/taiwan-opera-calendar/patrol_evidence/2026-11-12_0310/facebook_sunhope.… |
| facebook:HsiaoHsiYuan1913 | 部分 | 首屏 3 篇、累積 23 篇；最新 無、最舊 無；捲動 20 次、停止原因 max-scrolls；圖片下載 38 張 | 不變式通過；證據 /Users/eric/aiwork/taiwan-opera-calendar/patrol_evidence/2026-11-12_0310/facebook_HsiaoHsi… |
| facebook:100063868113954 | 部分 | 首屏 3 篇、累積 20 篇；最新 無、最舊 無；捲動 20 次、停止原因 max-scrolls；圖片下載 39 張 | 不變式通過；證據 /Users/eric/aiwork/taiwan-opera-calendar/patrol_evidence/2026-11-12_0310/facebook_10006386… |
| facebook:MingHuaYuanTianTaiwaneseOpera | 部分 | 首屏 1 篇、累積 23 篇；最新 無、最舊 無；捲動 20 次、停止原因 max-scrolls；圖片下載 61 張 | 不變式通過；證據 /Users/eric/aiwork/taiwan-opera-calendar/patrol_evidence/2026-11-12_0310/facebook_MingHuaY… |
| facebook:61574134933376 | 部分 | 首屏 1 篇、累積 5 篇；最新 無、最舊 無；捲動 4 次、停止原因 no-new-after-3；圖片下載 16 張 | 不變式通過；證據 /Users/eric/aiwork/taiwan-opera-calendar/patrol_evidence/2026-11-12_0310/facebook_61574134… |
| facebook:mhysun | 部分 | 首屏 3 篇、累積 19 篇；最新 無、最舊 無；捲動 20 次、停止原因 max-scrolls；圖片下載 70 張 | 不變式通過；證據 /Users/eric/aiwork/taiwan-opera-calendar/patrol_evidence/2026-11-12_0310/facebook_mhysun.j… |
| facebook:61594936681482 | 部分 | 首屏 1 篇、累積 7 篇；最新 無、最舊 無；捲動 7 次、停止原因 no-new-after-3；圖片下載 23 張 | 不變式通過；證據 /Users/eric/aiwork/taiwan-opera-calendar/patrol_evidence/2026-11-12_0310/facebook_61594936… |
| facebook:lanyang.opera | 部分 | 首屏 1 篇、累積 23 篇；最新 無、最舊 無；捲動 20 次、停止原因 max-scrolls；圖片下載 38 張 | 不變式通過；證據 /Users/eric/aiwork/taiwan-opera-calendar/patrol_evidence/2026-11-12_0310/facebook_lanyang.… |
| facebook:Taichungpuppettheater | 部分 | 首屏 1 篇、累積 25 篇；最新 無、最舊 無；捲動 20 次、停止原因 max-scrolls；圖片下載 42 張 | 不變式通過；證據 /Users/eric/aiwork/taiwan-opera-calendar/patrol_evidence/2026-11-12_0310/facebook_Taichung… |
| culture | 部分 | total 504、fetchedAt 2026-11-08T09:58:57+08:00、戲曲紀錄 9 筆 | moc_records 已 89 小時未更新 |
| issues | 完整 | 3 筆皆有處置 | 逐筆處置完成 |

- OPENTIX：sitemap 823 個活動、本輪有變 637、抓取 250、戲曲相關且未過期 36、延後 387、錯誤 0

## 卡片變更

| 編號 | 動作 | 來源 | 內容 | 差異 | 審查 | 寫入 |
| --- | --- | --- | --- | --- | --- | --- |
| chg-001 | add | https://www.threads.com/@taiwaneseopera168/post/DfWAAt6CT5a | 後場作戲｜出塵入凡—陳芸楚小旦專場｜高雄中山堂劇場｜2027-03-06 正戲 14:30、2027-03-07 正戲 14:30 |  | approve：海報圖 5b5cd72d 確認寫『後場作戲／出塵入凡—陳芸楚小旦專場／2027戲曲新秀專場舞臺／3/6 Sat. 14… | added  |
| chg-002 | add | https://www.facebook.com/photo/?fbid=122315789156250015 | 小金枝歌劇團｜《棄老山傳奇》｜高雄中山堂劇場戶外陽光草坪｜2026-11-27 正戲 19:00 |  | approve：原文寫『11/27（五）小金枝歌劇團《棄老山傳奇》』『每場次開演時間｜19:00』『演出地點｜高雄中山堂劇場戶外陽光草… | rejected badgeType-not-free |
| chg-003 | add | https://www.facebook.com/photo/?fbid=122315789156250015 | 新和興總團｜《秦英掛帥》｜高雄中山堂劇場戶外陽光草坪｜2026-11-28 正戲 19:00 |  | approve：原文寫『11/28（六）新和興總團《秦英掛帥》』，開演時間統一 19:00，地點是高雄中山堂劇場戶外陽光草坪，免費入場… | rejected badgeType-not-free |
| chg-004 | add | https://www.facebook.com/photo/?fbid=122315789156250015 | 藝華園戲劇團｜《八仙傳奇－張果老與藍采和》｜高雄中山堂劇場戶外陽光草坪｜2026-11-29 正戲 19:00 |  | approve：原文寫『11/29（日）藝華園戲劇團《八仙傳奇－張果老與藍采和》』，時間 19:00、地點高雄中山堂劇場戶外陽光草坪，… | rejected badgeType-not-free |
| chg-005 | add | https://www.facebook.com/photo/?fbid=122315789156250015 | 新藝芳歌劇團｜《金蟾緣》｜高雄中山堂劇場戶外陽光草坪｜2026-12-03 正戲 19:00 |  | approve：原文寫『12/03（四）新藝芳歌劇團《金蟾緣》』，時間 19:00，地點對得上。2026-12-03 是星期四。同一天… | rejected badgeType-not-free |
| chg-006 | add | https://www.facebook.com/photo/?fbid=122315789156250015 | 佩儀歌劇團｜《吳漢殺妻》｜高雄中山堂劇場戶外陽光草坪｜2026-12-04 正戲 19:00 |  | approve：原文寫『12/04（五）佩儀歌劇團《吳漢殺妻》』，時間 19:00，地點對得上。2026-12-04 是星期五，沒有重… | rejected badgeType-not-free |
| chg-007 | add | https://www.facebook.com/photo/?fbid=122315789156250015 | 文惜歌仔戲劇團｜《焰火長槍：火帥與玉龍的背影》｜高雄中山堂劇場戶外陽光草坪｜2026-12-05 正戲 19:00 |  | approve：原文寫『12/05（六）文惜歌仔戲劇團《焰火長槍：火帥與玉龍的背影》』，時間 19:00，地點對得上。2026-12-… | rejected badgeType-not-free |
| chg-008 | add | https://www.facebook.com/photo/?fbid=122315789156250015 | 繡花園戲劇團｜《姜子牙下山》｜高雄中山堂劇場戶外陽光草坪｜2026-12-06 正戲 19:00 |  | approve：原文寫『12/06（日）繡花園戲劇團《姜子牙下山》』，時間 19:00，地點對得上。2026-12-06 是星期日。現… | rejected badgeType-not-free |
| chg-009 | add | https://www.facebook.com/photo/?fbid=122315789156250015 | 春明歌劇團｜《玉虛戰歌．天命之戰》｜高雄中山堂劇場戶外陽光草坪｜2026-12-11 正戲 19:00 |  | approve：原文寫『12/11（五）春明歌劇團《玉虛戰歌．天命之戰》』，時間 19:00，地點對得上。2026-12-11 是星期… | rejected badgeType-not-free |
| chg-010 | add | https://www.facebook.com/photo/?fbid=122315789156250015 | 水錦歌劇團｜《對面夫妻～韋馱與觀音》｜高雄中山堂劇場戶外陽光草坪｜2026-12-12 正戲 19:00 |  | approve：原文寫『12/12（六）水錦歌劇團《對面夫妻～韋馱與觀音》』，時間 19:00，地點對得上。2026-12-12 是星… | rejected badgeType-not-free |
| chg-011 | add | https://www.facebook.com/photo/?fbid=122315789156250015 | 明華園星字戲劇團｜《斷案青天－陰錯陽差》｜高雄中山堂劇場戶外陽光草坪｜2026-12-13 正戲 19:00 |  | approve：原文寫『12/13（日）明華園星字戲劇團《斷案青天－陰錯陽差》』，時間 19:00，地點對得上。2026-12-13 … | rejected badgeType-not-free |
| chg-012 | add | https://www.threads.com/@yuzhongluo/post/Dfm36lfmUhX | 羅裕諒歌劇團｜楊排風掛帥｜臺北市大龍峒保安宮｜2026-11-20 正戲 19:00 |  | reject：troupe 欄的劇團名字打錯了。海報圖 d54b2f5a 左上角的團名書法字，以及右上『團長、導演｜羅裕誴』，第三個… | held  |
| chg-013 | add | https://www.threads.com/@jing__1017/post/DfmopfwicDS | 民安歌劇團｜《包公審烏盆》｜松山車站南側交4廣場｜2026-11-28 正戲 19:00 |  | approve：節目冊第 12 頁（圖 5fa6489b）寫『民安歌劇團／11/28（六）19:00／《包公審烏盆》』，側欄寫『演出地… | added  |
| chg-014 | add | https://www.threads.com/@jing__1017/post/DfmopfwicDS | 明華園日團歌仔戲｜《鬼菩薩》｜松山車站南側交4廣場｜2026-11-29 正戲 19:00 |  | approve：節目冊第 13 頁（圖 0000864e）寫『明華園日團歌仔戲／11/29（日）19:00／《鬼菩薩》』，地點是松山車… | added  |
| chg-015 | add | https://www.threads.com/@jing__1017/post/DfmopfwicDS | 新聲劇坊｜《新．女兒國》｜松山車站南側交4廣場｜2026-11-30 正戲 19:00 |  | approve：節目冊第 14 頁（圖 b6279f47）寫『新聲劇坊／11/30（一）19:00／《新．女兒國》』，地點是松山車站南… | added  |
| chg-016 | add | https://www.threads.com/@jing__1017/post/DfmopfwicDS | 薪傳歌仔戲劇團｜《三娘教子》｜松山車站南側交4廣場｜2026-12-01 正戲 19:00 |  | approve：節目冊第 15 頁（圖 5f51ef36）寫『薪傳歌仔戲劇團／12/01（二）19:00／《三娘教子》』，地點是松山車… | added  |
| chg-017 | add | https://www.threads.com/@jing__1017/post/DfmopfwicDS | 金麟戲劇團｜《青石引—九尾傾心》｜松山車站南側交4廣場｜2026-12-02 正戲 19:00 |  | approve：節目冊第 16 頁（圖 5b48bb67）寫『金麟戲劇團／12/02（三）19:00／《青石引—九尾傾心》』，地點是松… | added  |
| chg-018 | add | https://www.threads.com/@jing__1017/post/DfmopfwicDS | 陳美雲歌劇團｜《父子情》｜松山車站南側交4廣場｜2026-12-03 正戲 19:00 |  | approve：節目冊第 17 頁（圖 46add10d）寫『陳美雲歌劇團／12/03（四）19:00／《父子情》』，地點是松山車站南… | added  |
| chg-019 | update（查證成立） | https://www.npac-weiwuying.org/news/69f7f60b28083100085720f3（原貼文 https://www.facebook.com/photo/?fbid=1676744383818446） | 明華園戲劇總團｜《烏龍天下》｜衛武營國家藝術文化中心歌劇院｜2026-12-19 正戲 14:30、2026-12-20 正戲 14:30 | time：卡 未公布 → 文 2026-12-19 正戲 14:30；time：卡 未公布 → 文 2026-12-20 正戲 14:30 | approve：衛武營官網〈2026下半年主辦節目指南〉的協辦區寫『12/19(六)14:30、12/20(日)14:30 歌劇院 明… | updated  |
| chg-020 | add（查證成立） | https://www.opentix.life/event/2090269380048343041（原貼文 https://www.opentix.life/event/2090269380048343041） | 薪傳歌仔戲劇團｜《蒼原孤雁》｜臺灣戲曲中心小表演廳｜2026-11-14 正戲 14:30 |  | approve：OPENTIX 活動頁【小表演廳】寫『11/14（六）14:30 薪傳歌仔戲劇團《蒼原孤雁》 前場習藝生｜許博淵、吳育… | rejected location-not-in-quote,badgeType-not-ticket |
| chg-021 | add（查證成立） | https://anncr.co/Event/EWAIAK65616（原貼文 https://www.opentix.life/event/2080109546140397568） | 一心戲劇團｜《閻王的假期》｜臺北市藝文推廣處城市舞台（臺北市松山區八德路三段25號）｜2026-12-05 正戲 14:30、2026-12-06 正戲 14:30 |  | needs-check：日期、時間、劇團、劇目、主演都有原文支持：『場次時間 2026.12.05 (六) 14:30、2026.12.06 … | held  |

## 待查與退回

| 類別 | 貼文 | 原因 | 說明 |
| --- | --- | --- | --- |
| 漏處置 | threads:taiwaneseopera168:DfWONmSCdfQ | revision-mismatch |  |
| 漏處置 | facebook:100063868113954:1658401932965395 | missing-or-duplicate-disposition |  |
| 漏處置 | facebook:100063868113954:1655504973255091 | missing-or-duplicate-disposition |  |
| 漏處置 | facebook:100063868113954:1655155203290068 | missing-or-duplicate-disposition |  |

## 遠期場次（超過 120 天，進入 120 天內自動重驗）

| 貼文 | 內容 |
| --- | --- |
| https://www.facebook.com/photo/?fbid=1560228489482771 | 明華園天字戲劇團｜《重返：愛河戀夢》｜臺灣戲曲中心 大表演廳｜2027-06-05、2027-06-06 |
| https://www.facebook.com/MingHuaYuanTianTaiwaneseOpera/reels_tab | 明華園天字戲劇團｜《重返：愛河戀夢》｜臺灣戲曲中心 大表演廳｜2027-06-05、2027-06-06 |
| https://www.threads.com/@taiwaneseopera168/post/DfWAAt6CT5a | 烏貓戲出｜《白賊七》｜高雄中山堂劇場(高雄市左營區實踐路71號)｜2027-04-17、2027-04-18 |
| https://www.threads.com/@taiwaneseopera168/post/DfWAAt6CT5a | 薪傳歌仔戲劇團｜《封神榜．文王食子》｜高雄中山堂劇場(高雄市左營區實踐路71號)｜2027-04-24、2027-04-25 |
| https://www.threads.com/@taiwaneseopera168/post/DfWAAt6CT5a | 燕玲戲劇團｜《韓信設窖安軍心》｜高雄中山堂劇場(高雄市左營區實踐路71號)｜2027-03-20、2027-03-21 |

## 紀錄檔

- 本輪狀態：/Users/eric/aiwork/taiwan-opera-calendar/patrol_state/runs/2026-11-12_0310/state.json
- 巡檢紀錄：patrol_runs/2026-11-12_0310.json（/Users/eric/aiwork/taiwan-opera-calendar）
- 證據：patrol_evidence/2026-11-12_0310/
- 產生時間：2026-11-12T03:53:19+08:00
