# 巡檢報告 2026-10-29_0311（patrol-v2，正式）

## 需要 Eric 決定

- 發布未完成：Actions 40756427405 結論 failure
- 發布未完成：公開三檔與本機不一致

## 結論

| 項目 | 結果 |
| --- | --- |
| 執行 | 開始 2026-10-29T03:11:24+08:00；結果 進行中；步驟 preflight:done、collect:done、pack:done、judge:done、check:done、review:done、apply:done、publish:done、report:running |
| 來源 | 21 個：完整 4、部分 16、失敗 1、未讀 0 |
| 資料 | 送判讀 261 篇／圖 17 張；變更提案 2、確認一致 43、待查 55、退回 0、漏處置 0 |
| 寫入 | 寫入 2、add_card 拒絕 0、審查未通過 0 |
| 發布 | verified；SHA c105acfdd7f184993ad1386150488a6cdb549bb0；Actions 40809551182 |

## 模型與用量

| 角色 | 模型 | 依據 |
| --- | --- | --- |
| main | claude-sonnet-5-5 | get_session self：effort=medium |
| judge | sonnet | Agent 工具 model 參數；effort=medium |
| review | opus | Agent 工具 model 參數；effort=high |

- 判讀批次 11；送出貼文 261 篇、圖片 17 張、正文約 79553 字
- 略過（已判讀未變動）86 篇；窗口外 28 篇
- 第二次審查：有（2 項）

## 來源

| 來源 | 狀態 | 範圍 | 說明 |
| --- | --- | --- | --- |
| threads:joe_huang_k_w | 部分 | 首屏 4 篇、累積 11 篇；最新 2026-10-26T21:28:30+08:00、最舊 2026-10-18T13:12:12+08:00；捲動 2 次、停止原因 reached-window；圖片下載 12 張 | 不變式通過；證據 /Users/eric/aiwork/taiwan-opera-calendar/patrol_evidence/2026-10-29_0311/threads_joe_huang… |
| threads:h.akito_1996 | 部分 | 首屏 6 篇、累積 6 篇；最新 2026-10-28T17:42:12+08:00、最舊 2026-09-27T00:04:33+08:00；捲動 3 次、停止原因 no-new-after-3；圖片下載 6 張 | 不變式通過；證據 /Users/eric/aiwork/taiwan-opera-calendar/patrol_evidence/2026-10-29_0311/threads_h.akito_1… |
| threads:the_rin.lpm | 完整 | 7 天窗口讀完（停止原因 reached-window）；窗口內 0 篇皆有處置；圖片 0 張皆已判讀 | 不變式通過、逐篇處置完成 |
| threads:1013.yr_ | 失敗 | 首屏 0 篇、累積 0 篇；最新 無、最舊 無；捲動 3 次、停止原因 no-new-after-3；圖片下載 0 張 | 問題：first-screen-empty；證據 /Users/eric/aiwork/taiwan-opera-calendar/patrol_evidence/2026-10-29_0311/t… |
| threads:xuefeng_lu_ | 完整 | 7 天窗口讀完（停止原因 reached-window）；窗口內 4 篇皆有處置；圖片 0 張皆已判讀 | 不變式通過、逐篇處置完成 |
| threads:yuzhongluo | 部分 | 首屏 4 篇、累積 33 篇；最新 2026-10-28T23:34:12+08:00、最舊 2026-10-20T12:05:15+08:00；捲動 15 次、停止原因 reached-window；圖片下載 65 張 | 不變式通過；證據 /Users/eric/aiwork/taiwan-opera-calendar/patrol_evidence/2026-10-29_0311/threads_yuzhonglu… |
| threads:taiwaneseopera168 | 部分 | 首屏 5 篇、累積 35 篇；最新 2026-10-28T22:06:52+08:00、最舊 2026-08-16T02:33:12+08:00；捲動 15 次、停止原因 reached-window；圖片下載 29 張 | 不變式通過；證據 /Users/eric/aiwork/taiwan-opera-calendar/patrol_evidence/2026-10-29_0311/threads_taiwanese… |
| threads:jing__1017 | 部分 | 首屏 4 篇、累積 28 篇；最新 2026-10-29T01:29:17+08:00、最舊 2026-10-22T01:58:53+08:00；捲動 10 次、停止原因 reached-window；圖片下載 33 張 | 不變式通過；證據 /Users/eric/aiwork/taiwan-opera-calendar/patrol_evidence/2026-10-29_0311/threads_jing__101… |
| threads:hilang.on.tour | 完整 | 7 天窗口讀完（停止原因 reached-window）；窗口內 0 篇皆有處置；圖片 0 張皆已判讀 | 不變式通過、逐篇處置完成 |
| threads:yolin1991 | 部分 | 首屏 4 篇、累積 8 篇；最新 2026-10-28T18:34:21+08:00、最舊 2026-10-20T21:07:23+08:00；捲動 2 次、停止原因 reached-window；圖片下載 8 張 | 不變式通過；證據 /Users/eric/aiwork/taiwan-opera-calendar/patrol_evidence/2026-10-29_0311/threads_yolin1991… |
| facebook:sunhope.fans | 部分 | 首屏 3 篇、累積 21 篇；最新 無、最舊 無；捲動 20 次、停止原因 max-scrolls；圖片下載 31 張 | 不變式通過；證據 /Users/eric/aiwork/taiwan-opera-calendar/patrol_evidence/2026-10-29_0311/facebook_sunhope.… |
| facebook:HsiaoHsiYuan1913 | 部分 | 首屏 1 篇、累積 24 篇；最新 無、最舊 無；捲動 20 次、停止原因 max-scrolls；圖片下載 50 張 | 不變式通過；證據 /Users/eric/aiwork/taiwan-opera-calendar/patrol_evidence/2026-10-29_0311/facebook_HsiaoHsi… |
| facebook:100063868113954 | 部分 | 首屏 3 篇、累積 21 篇；最新 無、最舊 無；捲動 20 次、停止原因 max-scrolls；圖片下載 49 張 | 不變式通過；證據 /Users/eric/aiwork/taiwan-opera-calendar/patrol_evidence/2026-10-29_0311/facebook_10006386… |
| facebook:MingHuaYuanTianTaiwaneseOpera | 部分 | 首屏 1 篇、累積 23 篇；最新 無、最舊 無；捲動 20 次、停止原因 max-scrolls；圖片下載 65 張 | 不變式通過；證據 /Users/eric/aiwork/taiwan-opera-calendar/patrol_evidence/2026-10-29_0311/facebook_MingHuaY… |
| facebook:61574134933376 | 部分 | 首屏 1 篇、累積 20 篇；最新 無、最舊 無；捲動 20 次、停止原因 max-scrolls；圖片下載 61 張 | 不變式通過；證據 /Users/eric/aiwork/taiwan-opera-calendar/patrol_evidence/2026-10-29_0311/facebook_61574134… |
| facebook:mhysun | 部分 | 首屏 1 篇、累積 19 篇；最新 無、最舊 無；捲動 20 次、停止原因 max-scrolls；圖片下載 79 張 | 不變式通過；證據 /Users/eric/aiwork/taiwan-opera-calendar/patrol_evidence/2026-10-29_0311/facebook_mhysun.j… |
| facebook:61594936681482 | 部分 | 首屏 1 篇、累積 7 篇；最新 無、最舊 無；捲動 7 次、停止原因 no-new-after-3；圖片下載 23 張 | 不變式通過；證據 /Users/eric/aiwork/taiwan-opera-calendar/patrol_evidence/2026-10-29_0311/facebook_61594936… |
| facebook:lanyang.opera | 部分 | 首屏 1 篇、累積 22 篇；最新 無、最舊 無；捲動 20 次、停止原因 max-scrolls；圖片下載 39 張 | 不變式通過；證據 /Users/eric/aiwork/taiwan-opera-calendar/patrol_evidence/2026-10-29_0311/facebook_lanyang.… |
| facebook:Taichungpuppettheater | 部分 | 首屏 2 篇、累積 26 篇；最新 無、最舊 無；捲動 20 次、停止原因 max-scrolls；圖片下載 25 張 | 不變式通過；證據 /Users/eric/aiwork/taiwan-opera-calendar/patrol_evidence/2026-10-29_0311/facebook_Taichung… |
| culture | 部分 | total 1363、fetchedAt 2026-10-27T09:46:26+08:00、戲曲紀錄 30 筆 | moc_records 已 41 小時未更新 |
| issues | 完整 | 2 筆皆有處置 | 逐筆處置完成 |

- OPENTIX：sitemap 1036 個活動、本輪有變 776、抓取 250、戲曲相關且未過期 22、延後 526、錯誤 0

## 卡片變更

| 編號 | 動作 | 來源 | 內容 | 差異 | 審查 | 寫入 |
| --- | --- | --- | --- | --- | --- | --- |
| chg-001 | add | https://www.opentix.life/event/2079024127582380033 | 明華園星字戲劇團｜2026 正港雄有戲《功德嘉年華》｜駁二正港小劇場（高雄市 鼓山區蓬萊路99號 駁二藝術特區蓬萊倉庫 B9棟）｜2026-11-13 正戲 13:30、2026-11-14 正戲 14:30、2026-11-15 正戲 … |  | approve：三場的日期和時間都與 source.text 逐字對上（「場次：2026-11-13 13:30」「場次：2026-1… | added  |
| chg-002 | add | https://www.opentix.life/event/2095095175039627264 | 全樂閣木偶劇團｜2026武俠新篇章《俠虎征途》｜屏東演藝廳實驗劇場（屏東縣 屏東市民生路4-17號）｜2026-11-14 正戲 19:30 |  | approve：日期、時間、地點都與 source.text 的「場次：2026-11-14 19:30｜地點：屏東演藝廳實驗劇場（屏… | added  |

## 待查與退回

| 類別 | 貼文 | 原因 | 說明 |
| --- | --- | --- | --- |
| 待查 | https://www.threads.com/@joe_huang_k_w/post/De84KuwCZYv | time-not-in-quote |  |
| 待查 | https://www.threads.com/@yuzhongluo/post/De_2I12GYGv | date-out-of-range,date-not-in-quote |  |
| 待查 | https://www.threads.com/@yuzhongluo/post/De8JbMFk2OH | date-out-of-range,date-not-in-quote |  |
| 待查 | https://www.threads.com/@yuzhongluo/post/De8JQY1mbpE | date-out-of-range,date-not-in-quote |  |
| 待查 | https://www.threads.com/@yuzhongluo/post/De8JMhjmaBe | date-out-of-range,date-not-in-quote |  |
| 待查 | https://www.threads.com/@yuzhongluo/post/De4o7SfE50m | judge-needs-check | 「下一場9月18日」為農曆且未寫時間，地點聖巡北極殿與既有卡片聖巡代天宮不同，無法確認 |
| 待查 | https://www.threads.com/@taiwaneseopera168/post/DfCX6aeiYrJ | date-out-of-range |  |
| 待查 | https://www.threads.com/@taiwaneseopera168/post/DfCNCqyiVRa | date-out-of-range |  |
| 待查 | https://www.threads.com/@taiwaneseopera168/post/DfBoVdckYwq | date-out-of-range |  |
| 待查 | https://www.threads.com/@taiwaneseopera168/post/De_0ly7CWE4 | date-out-of-range |  |
| 待查 | https://www.threads.com/@taiwaneseopera168/post/De9NUuMCdaI | date-out-of-range |  |
| 待查 | https://www.threads.com/@jing__1017/post/De1gDXdCYOT | date-out-of-range |  |
| 待查 | https://www.threads.com/@jing__1017/post/De1gDXdCYOT | date-out-of-range |  |
| 待查 | https://www.threads.com/@jing__1017/post/DezjluUk4To | judge-needs-check | 此篇只有劇情介紹，無時間與地點；同活動資料在 DezjmaXkw2e，已在表 auto-20261031-7d7c89f5 |
| 待查 | https://www.threads.com/@yolin1991/post/De3GTIVGsTS | judge-needs-check | 當日演出因風雨取消，但正文未寫明場次，表中也無對應卡片（對應 10/24 已過期） |
| 待查 | https://www.facebook.com/photo/?fbid=1733072965491079 | judge-needs-check | 10/31 岡山文化中心分館圖書館歌仔繪本活動，額滿且正文無時間與正式地址 |
| 待查 | https://www.facebook.com/photo/?fbid=1716331140498595 | time-not-in-quote |  |
| 待查 | https://www.facebook.com/photo/?fbid=1716331140498595 | time-not-in-quote |  |
| 待查 | https://www.facebook.com/photo/?fbid=1716331140498595 | time-not-in-quote |  |
| 待查 | https://www.facebook.com/photo/?fbid=1655504973255091 | judge-needs-check | 奕萱行程 10/29 茄萣、11/1-11/10 朱王廟與既有卡片相符，但全文未寫劇團與劇種，datetime 為 null；已由戲路表覆蓋 |
| 待查 | facebook:100063868113954:435d2d53d596 | judge-needs-check | 同上：行程與卡片相符，但全文未寫劇團與劇種，datetime 為 null |
| 待查 | https://www.facebook.com/photo/?fbid=1655155203290068 | judge-needs-check | 同上；另提到 11/23 快閃台北但無地點時間，不能建卡 |
| 待查 | https://www.facebook.com/photo/?fbid=1654012383404350 | judge-needs-check | 貼文稱行程有異動，列 10/27 小北、10/29 茄萣、11/1-11/10 朱王廟（未再列 10/28 茄萣，卡片為 10/28-10/29），但未寫劇團、未說明異動內容，需看圖或人工確認 |
| 待查 | https://www.facebook.com/photo/?fbid=1653026506836271 | judge-needs-check | 行程（10/26-27 小北、10/28-29 茄萣）已由戲路表確認並在卡片，但本文未寫劇團，datetime 為 null |
| 待查 | https://www.facebook.com/photo/?fbid=1652519793553609 | judge-needs-check | 行程已由戲路表覆蓋，但本文未寫劇團，datetime 為 null |
| 待查 | facebook:100063868113954:cd692ac83d13 | judge-needs-check | 本文未寫劇團；10/25 場次已過期，10/26 起行程已由戲路表覆蓋 |
| 待查 | https://www.facebook.com/photo/?fbid=1639097094895879 | date-out-of-range |  |
| 待查 | https://www.facebook.com/photo/?fbid=1639097094895879 | date-out-of-range |  |
| 待查 | https://www.facebook.com/photo/?fbid=1639097094895879 | date-out-of-range |  |
| 待查 | https://www.facebook.com/photo/?fbid=1639097094895879 | date-out-of-range |  |
| 待查 | https://www.facebook.com/photo/?fbid=1639097094895879 | date-out-of-range |  |
| 待查 | https://www.facebook.com/permalink.php?story_fbid=pfbid02b8Jyb778jnVi4yyfcEEsZqexvGuLzgeypxR8Bco9UUJgZZSpVtHYW555kWfUfCu3l&id=61574134933376 | possible-duplicate:auto-20261118-f7e6977b |  |
| 待查 | https://www.facebook.com/photo/?fbid=122186354384804497 | judge-needs-check | 只說「額外進行一場大型演出」封神榜，無日期、時間、地點；已知圖片皆為劇照無日期地點 |
| 待查 | https://www.facebook.com/photo/?fbid=122182529360804497 | judge-needs-check | 行程多為農曆8月且無年份，國曆日期（9/15、10/4）皆早於今日 10/29，不新增。 |
| 待查 | https://www.facebook.com/photo/?fbid=1546668374148203 | judge-needs-check | 補助計畫入選名單，只有三週總區間，沒有各團場次日期時間，無法建卡。 |
| 待查 | https://www.facebook.com/photo/?fbid=1680604376765780 | date-out-of-range |  |
| 待查 | https://www.facebook.com/photo/?fbid=122103327177497889 | judge-needs-check | 古都木偶劇團 10/8 桃園蓮華寺場次已過期（距今三週），且發文時間為 null，是否收錄請人工確認。 |
| 待查 | https://www.facebook.com/photo/?fbid=122099118879497889 | judge-needs-check | 古都木偶劇團 10/8 蓮華寺場次已過期，與同系列貼文重複，請人工確認是否補錄。 |
| 待查 | https://www.facebook.com/lanyang.opera/reels_tab | date-out-of-range |  |
| 待查 | https://www.facebook.com/photo/?fbid=1559376062887668 | date-out-of-range |  |
| 待查 | https://www.facebook.com/photo/?fbid=1538038435021431 | judge-needs-check | 行程表貼文只寫 10/26 無年份，發文時間為 null，且連續原文中不含劇團名；同一場次見 1559376062887668。 |
| 待查 | https://www.facebook.com/photo/?fbid=1626553559484654 | judge-needs-check | 布袋戲主題「戲偶互動展」10/24–11/8，屬展覽但含操偶體驗，是否算體驗活動請人工判斷。 |
| 待查 | https://www.facebook.com/photo/?fbid=1614011900738820 | judge-needs-check | FB 無發文時間、正文無年份，且 10/12 已過期，不建卡。 |
| 待查 | https://www.facebook.com/photo/?fbid=1611874497619227 | possible-duplicate:lecture-2026-11-01-tcpt-tech-visual-magic |  |
| 待查 | https://www.opentix.life/event/2090269380048343041 | judge-needs-check | 10 團聯合展演，簡介被截斷，看不出各場劇種與劇團。 |
| 待查 | https://www.opentix.life/program/2088104133013299200 | judge-needs-check | 文化部紀錄只有「偶偶偶劇團」，沒有布袋或掌中證據，不可因名稱有偶就當布袋戲；表上既有卡的劇種需複核。 |
| 待查 | https://www.opentix.life/program/2080173157578416129 | puppet-not-budaixi |  |
| 待查 | https://www.opentix.life/program/2112035354878472193 | puppet-not-budaixi,target-card-not-found |  |
| 待查 | https://www.threads.com/@yuzhongluo/post/De6Mm2DmQ6W | judge-needs-check | 正文與兩張圖（劇照、後台人像）都沒有日期、時間、地點，只是羅裕誴歌劇團海安路萬聖節的宣傳，無法建卡。 |
| 待查 | https://www.threads.com/@yuzhongluo/post/De6Mi7GGRT4 | judge-needs-check | 與另一篇同文同圖，沒有日期、時間、地點，無法建卡。 |
| 待查 | https://www.threads.com/@jing__1017/post/DfAWHhpk3Pm | date-out-of-range,date-not-in-quote |  |
| 待查 | https://www.threads.com/@jing__1017/post/De_9KfvE2gD | time-not-in-quote |  |
| 待查 | https://www.facebook.com/photo/?fbid=122185121900804497 | date-out-of-range,date-not-in-quote |  |
| 待查 | https://www.facebook.com/photo/?fbid=122185121900804497 | date-not-in-quote |  |
| 待查 | https://www.facebook.com/photo/?fbid=122185121900804497 | date-not-in-quote |  |

## 紀錄檔

- 本輪狀態：/Users/eric/aiwork/taiwan-opera-calendar/patrol_state/runs/2026-10-29_0311/state.json
- 巡檢紀錄：patrol_runs/2026-10-29_0311.json（/Users/eric/aiwork/taiwan-opera-calendar）
- 證據：patrol_evidence/2026-10-29_0311/
- 產生時間：2026-10-29T11:00:26+08:00
