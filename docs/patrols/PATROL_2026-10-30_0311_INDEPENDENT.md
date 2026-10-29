# 巡檢報告 2026-10-30_0311（patrol-v2，正式）

## 結論

| 項目 | 結果 |
| --- | --- |
| 執行 | 開始 2026-10-30T03:11:27+08:00；結果 進行中；步驟 preflight:done、collect:done、pack:done、judge:done、check:done、review:done、apply:done、publish:done、report:running |
| 來源 | 21 個：完整 2、部分 18、失敗 1、未讀 0 |
| 資料 | 送判讀 245 篇／圖 22 張；變更提案 4、確認一致 31、待查 54、退回 0、漏處置 0 |
| 寫入 | 寫入 1、add_card 拒絕 1、審查未通過 2 |
| 發布 | verified；SHA 67a3f15d209ffd787b00b0a744380d3b12449399；Actions 40942525671 |

## 模型與用量

| 角色 | 模型 | 依據 |
| --- | --- | --- |
| main | claude-sonnet-5-5 | get_session self：effort=medium |
| judge | sonnet | Agent 工具 model 參數；effort=medium |
| review | opus | Agent 工具 model 參數；effort=high |

- 判讀批次 10；送出貼文 245 篇、圖片 22 張、正文約 74537 字
- 略過（已判讀未變動）102 篇；窗口外 21 篇
- 第二次審查：有（4 項）

## 來源

| 來源 | 狀態 | 範圍 | 說明 |
| --- | --- | --- | --- |
| threads:joe_huang_k_w | 部分 | 首屏 4 篇、累積 9 篇；最新 2026-10-29T17:10:13+08:00、最舊 2026-10-20T21:30:35+08:00；捲動 2 次、停止原因 reached-window；圖片下載 10 張 | 不變式通過；證據 /Users/eric/aiwork/taiwan-opera-calendar/patrol_evidence/2026-10-30_0311/threads_joe_huang… |
| threads:h.akito_1996 | 部分 | 首屏 5 篇、累積 13 篇；最新 2026-10-30T03:03:15+08:00、最舊 2026-09-27T00:04:33+08:00；捲動 4 次、停止原因 reached-window；圖片下載 15 張 | 不變式通過；證據 /Users/eric/aiwork/taiwan-opera-calendar/patrol_evidence/2026-10-30_0311/threads_h.akito_1… |
| threads:the_rin.lpm | 部分 | 首屏 4 篇、累積 5 篇；最新 2026-10-29T19:15:16+08:00、最舊 2026-09-26T14:32:03+08:00；捲動 1 次、停止原因 reached-window；圖片下載 5 張 | 不變式通過；證據 /Users/eric/aiwork/taiwan-opera-calendar/patrol_evidence/2026-10-30_0311/threads_the_rin.l… |
| threads:1013.yr_ | 失敗 | 首屏 0 篇、累積 0 篇；最新 無、最舊 無；捲動 3 次、停止原因 no-new-after-3；圖片下載 0 張 | 問題：first-screen-empty；證據 /Users/eric/aiwork/taiwan-opera-calendar/patrol_evidence/2026-10-30_0311/t… |
| threads:xuefeng_lu_ | 完整 | 7 天窗口讀完（停止原因 reached-window）；窗口內 5 篇皆有處置；圖片 0 張皆已判讀 | 不變式通過、逐篇處置完成 |
| threads:yuzhongluo | 部分 | 首屏 4 篇、累積 35 篇；最新 2026-10-29T17:04:37+08:00、最舊 2026-10-20T12:18:54+08:00；捲動 16 次、停止原因 reached-window；圖片下載 69 張 | 不變式通過；證據 /Users/eric/aiwork/taiwan-opera-calendar/patrol_evidence/2026-10-30_0311/threads_yuzhonglu… |
| threads:taiwaneseopera168 | 部分 | 首屏 5 篇、累積 43 篇；最新 2026-10-29T19:36:43+08:00、最舊 2026-08-16T02:33:12+08:00；捲動 20 次、停止原因 reached-window；圖片下載 34 張 | 不變式通過；證據 /Users/eric/aiwork/taiwan-opera-calendar/patrol_evidence/2026-10-30_0311/threads_taiwanese… |
| threads:jing__1017 | 部分 | 首屏 4 篇、累積 5 篇；最新 2026-10-29T23:18:48+08:00、最舊 2026-10-28T19:50:21+08:00；捲動 4 次、停止原因 no-new-after-3；圖片下載 6 張 | 不變式通過；證據 /Users/eric/aiwork/taiwan-opera-calendar/patrol_evidence/2026-10-30_0311/threads_jing__101… |
| threads:hilang.on.tour | 完整 | 7 天窗口讀完（停止原因 reached-window）；窗口內 0 篇皆有處置；圖片 0 張皆已判讀 | 不變式通過、逐篇處置完成 |
| threads:yolin1991 | 部分 | 首屏 4 篇、累積 6 篇；最新 2026-10-28T18:34:21+08:00、最舊 2026-10-22T11:28:41+08:00；捲動 1 次、停止原因 reached-window；圖片下載 6 張 | 不變式通過；證據 /Users/eric/aiwork/taiwan-opera-calendar/patrol_evidence/2026-10-30_0311/threads_yolin1991… |
| facebook:sunhope.fans | 部分 | 首屏 1 篇、累積 22 篇；最新 無、最舊 無；捲動 20 次、停止原因 max-scrolls；圖片下載 45 張 | 不變式通過；證據 /Users/eric/aiwork/taiwan-opera-calendar/patrol_evidence/2026-10-30_0311/facebook_sunhope.… |
| facebook:HsiaoHsiYuan1913 | 部分 | 首屏 1 篇、累積 24 篇；最新 無、最舊 無；捲動 20 次、停止原因 max-scrolls；圖片下載 50 張 | 不變式通過；證據 /Users/eric/aiwork/taiwan-opera-calendar/patrol_evidence/2026-10-30_0311/facebook_HsiaoHsi… |
| facebook:100063868113954 | 部分 | 首屏 2 篇、累積 20 篇；最新 無、最舊 無；捲動 20 次、停止原因 max-scrolls；圖片下載 47 張 | 不變式通過；證據 /Users/eric/aiwork/taiwan-opera-calendar/patrol_evidence/2026-10-30_0311/facebook_10006386… |
| facebook:MingHuaYuanTianTaiwaneseOpera | 部分 | 首屏 2 篇、累積 22 篇；最新 無、最舊 無；捲動 20 次、停止原因 max-scrolls；圖片下載 48 張 | 不變式通過；證據 /Users/eric/aiwork/taiwan-opera-calendar/patrol_evidence/2026-10-30_0311/facebook_MingHuaY… |
| facebook:61574134933376 | 部分 | 首屏 1 篇、累積 21 篇；最新 無、最舊 無；捲動 20 次、停止原因 max-scrolls；圖片下載 62 張 | 不變式通過；證據 /Users/eric/aiwork/taiwan-opera-calendar/patrol_evidence/2026-10-30_0311/facebook_61574134… |
| facebook:mhysun | 部分 | 首屏 1 篇、累積 19 篇；最新 無、最舊 無；捲動 20 次、停止原因 max-scrolls；圖片下載 79 張 | 不變式通過；證據 /Users/eric/aiwork/taiwan-opera-calendar/patrol_evidence/2026-10-30_0311/facebook_mhysun.j… |
| facebook:61594936681482 | 部分 | 首屏 1 篇、累積 7 篇；最新 無、最舊 無；捲動 7 次、停止原因 no-new-after-3；圖片下載 23 張 | 不變式通過；證據 /Users/eric/aiwork/taiwan-opera-calendar/patrol_evidence/2026-10-30_0311/facebook_61594936… |
| facebook:lanyang.opera | 部分 | 首屏 1 篇、累積 22 篇；最新 無、最舊 無；捲動 20 次、停止原因 max-scrolls；圖片下載 39 張 | 不變式通過；證據 /Users/eric/aiwork/taiwan-opera-calendar/patrol_evidence/2026-10-30_0311/facebook_lanyang.… |
| facebook:Taichungpuppettheater | 部分 | 首屏 3 篇、累積 26 篇；最新 無、最舊 無；捲動 20 次、停止原因 max-scrolls；圖片下載 25 張 | 不變式通過；證據 /Users/eric/aiwork/taiwan-opera-calendar/patrol_evidence/2026-10-30_0311/facebook_Taichung… |
| culture | 部分 | total 1370、fetchedAt 2026-10-29T10:02:34+08:00、戲曲紀錄 30 筆 | 資料新鮮；逐筆處置待判讀後確認 |
| issues | 部分 | state=all 共 3 則（含留言） | 已讀取；處置待判讀後確認 |

- OPENTIX：sitemap 1036 個活動、本輪有變 738、抓取 250、戲曲相關且未過期 25、延後 488、錯誤 0

## 卡片變更

| 編號 | 動作 | 來源 | 內容 | 差異 | 審查 | 寫入 |
| --- | --- | --- | --- | --- | --- | --- |
| chg-001 | change（由「一致」轉） | https://www.threads.com/@the_rin.lpm/post/DfE4HxtE8MM | 秀琴歌劇團｜外台演出｜西港玉勅慶安宮 廟埕｜2026-10-30 扮仙 17:30、2026-10-30 正戲 19:00、2026-10-31 扮仙 17:30、2026-10-31 正戲 19:00 | location：卡 臺南市西港區慶安路32號（慶安宮） → 文 西港玉勅慶安宮 廟埕 | needs-check：日期、時間、劇團都對：原文寫「演出日期：10/30（五)-31日（六）」「下午5：30扮仙、晚上7：00開演」，海報也… | held  |
| chg-002 | change（由「一致」轉） | facebook:61574134933376:5a5635caeeb3 | 繡花園戲劇團｜《孫臏兵法》｜臺南市柳營區 柳營代天院（臺南市柳營區東昇里中山西路一段362號）｜2026-11-18 扮仙 19:00、2026-11-18 正戲 19:30 | time：卡 晚上 7:30 → 文 2026-11-18 扮仙 19:00 | needs-check：內容本身正確：原文寫「演出日期｜2026/11/18（三）」「晚上 7:00｜三仙大會」「晚上 7:30｜正戲開演」，… | held  |
| chg-003 | change（由「一致」轉） | https://www.facebook.com/photo/?fbid=122186687630804497 | 繡花園戲劇團｜《孫臏兵法》｜臺南市柳營區 柳營代天院（臺南市柳營區東昇里中山西路一段362號）｜2026-11-18 扮仙 19:00、2026-11-18 正戲 19:30 | time：卡 晚上 7:30 → 文 2026-11-18 扮仙 19:00 | approve：來源網址 photo/?fbid=122186687630804497 跟卡片的 sourceUrl 相同，是繡花園戲… | rejected no-change-keyword |
| chg-004 | add | https://www.opentix.life/event/2095045191349043200 | 陳錫煌傳統掌中劇團｜大稻埕戲苑「115年駐館團隊專場演出」《三國演義之古城會》｜大稻埕戲苑曲藝場（臺北市 大同區迪化街一段21號8樓）｜2026-11-15 正戲 14:30 |  | approve：OPENTIX 售票頁（event/2095045191349043200，2026-10-28 抓取）寫「場次：20… | added  |

## 待查與退回

| 類別 | 貼文 | 原因 | 說明 |
| --- | --- | --- | --- |
| 待查 | https://www.threads.com/@joe_huang_k_w/post/De84KuwCZYv | time-not-in-quote |  |
| 待查 | https://www.threads.com/@yuzhongluo/post/De8JbMFk2OH | judge-needs-check | 無時間與地點文字，海報僅農曆日期且已過期 |
| 待查 | https://www.threads.com/@yuzhongluo/post/De8JQY1mbpE | judge-needs-check | 無時間，海報僅農曆日期且已過期 |
| 待查 | https://www.threads.com/@yuzhongluo/post/De8JMhjmaBe | judge-needs-check | 無時間，海報僅農曆日期且已過期 |
| 待查 | https://www.threads.com/@yuzhongluo/post/De6Mm2DmQ6W | judge-needs-check | 正文與已知圖片皆無日期時間地點 |
| 待查 | https://www.threads.com/@yuzhongluo/post/De6Mi7GGRT4 | judge-needs-check | 正文與已知圖片皆無日期時間地點 |
| 待查 | https://www.threads.com/@taiwaneseopera168/post/DfE568kCYiY | date-out-of-range |  |
| 待查 | https://www.threads.com/@taiwaneseopera168/post/DfE263nCZIT | date-out-of-range |  |
| 待查 | https://www.threads.com/@taiwaneseopera168/post/DfEkpshkbtZ | date-out-of-range |  |
| 待查 | https://www.threads.com/@taiwaneseopera168/post/DfEdAMwEZOX | judge-needs-check | 10 團 14 夜但各團場次時間表待主辦單位公布，無法逐日對應 |
| 待查 | https://www.threads.com/@jing__1017/post/DfFQnEXic9S | judge-needs-check | 正文只有標籤與時間，無任何內容可判讀 |
| 待查 | https://www.facebook.com/sunhope.fans/reels_tab | time-not-in-quote,date-not-in-quote |  |
| 待查 | https://www.facebook.com/photo/?fbid=1762387365892972 | time-not-in-quote,date-not-in-quote |  |
| 待查 | https://www.facebook.com/photo/?fbid=1760890542709321 | time-not-in-quote,date-not-in-quote |  |
| 待查 | https://www.facebook.com/photo/?fbid=1733072965491079 | judge-needs-check | 只提到 10/31 還有一場繪本活動且已額滿，無時間與地點。 |
| 待查 | https://www.facebook.com/photo/?fbid=1716331140498595 | time-not-in-quote |  |
| 待查 | https://www.facebook.com/photo/?fbid=1716331140498595 | time-not-in-quote |  |
| 待查 | https://www.facebook.com/photo/?fbid=1716331140498595 | time-not-in-quote |  |
| 待查 | https://www.facebook.com/photo/?fbid=1071717901621417 | judge-needs-check | 「10月12日禮拜六」沒有年份、發文時間為 null，且為舊貼文（週六對應 2024 年，早已過期），無法確認年份，不建卡。 |
| 待查 | https://www.facebook.com/photo/?fbid=764328825693661 | judge-needs-check | 7/12 星期三（農曆5/25）無年份、發文時間為 null，且為早已過期的舊貼文，無法確認年份，不建卡。 |
| 待查 | https://www.facebook.com/photo/?fbid=4488203871226883 | judge-needs-check | 「11月27日」無年份、發文時間為 null，內容為疫情期間的舊貼文（已過期），無法確認年份，不建卡。 |
| 待查 | https://www.facebook.com/photo/?fbid=3749542658426345 | judge-needs-check | 只寫「就是明天」，發文時間為 null 無法推算日期，正文也沒有時間地點，且為疫情期間舊貼文。 |
| 待查 | https://www.facebook.com/photo/?fbid=3423966680983946 | judge-needs-check | 只寫「就在這個週日」，發文時間為 null 無法推算日期，無時間地點，且為疫情期間舊貼文。 |
| 待查 | https://www.facebook.com/photo/?fbid=3371704532876828 | judge-needs-check | 「11月優質藝文活動」月曆資訊在圖中，但內容為實名制防疫時期（已過期）舊貼文，發文時間為 null、無年份，不值得看圖建卡。 |
| 待查 | https://www.facebook.com/photo/?fbid=3334478559932759 | judge-needs-check | 11月藝文訊息月曆在圖中，但為疫情期間（已過期）舊貼文，發文時間為 null、無年份，不建卡。 |
| 待查 | https://www.facebook.com/photo/?fbid=2981817195198899 | judge-needs-check | 農曆五月藝文活動資訊在圖中，但為疫情期間（已過期）舊貼文，發文時間為 null、無年份，不建卡。 |
| 待查 | https://www.facebook.com/photo/?fbid=1654012383404350 | date-out-of-range |  |
| 待查 | https://www.facebook.com/photo/?fbid=1653026506836271 | date-out-of-range |  |
| 待查 | https://www.facebook.com/photo/?fbid=1652519793553609 | date-out-of-range |  |
| 待查 | facebook:100063868113954:cd692ac83d13 | date-out-of-range |  |
| 待查 | https://www.facebook.com/photo/?fbid=1650966917042230 | date-out-of-range |  |
| 待查 | https://www.facebook.com/photo/?fbid=1649883867150535 | judge-needs-check | 貼文未寫劇團與劇種，發文時間未知（datetime 為 null），無法確認是否屬歌仔戲／布袋戲 |
| 待查 | https://www.facebook.com/photo/?fbid=1648899747248947 | judge-needs-check | 貼文未寫劇團與劇種，發文時間未知（datetime 為 null），無法確認是否屬歌仔戲／布袋戲 |
| 待查 | https://www.facebook.com/photo/?fbid=1647926894012899 | judge-needs-check | 貼文未寫劇團與劇種，發文時間未知（datetime 為 null），無法確認是否屬歌仔戲／布袋戲 |
| 待查 | https://www.facebook.com/photo/?fbid=1645851590887096 | judge-needs-check | 貼文未寫劇團與劇種，發文時間未知（datetime 為 null），無法確認是否屬歌仔戲／布袋戲 |
| 待查 | https://www.facebook.com/photo/?fbid=1644867644318824 | judge-needs-check | 貼文未寫劇團與劇種，發文時間未知（datetime 為 null），無法確認是否屬歌仔戲／布袋戲 |
| 待查 | https://www.facebook.com/photo/?fbid=1640727488066173 | judge-needs-check | 貼文未寫劇團與劇種，發文時間未知（datetime 為 null），無法確認是否屬歌仔戲／布袋戲 |
| 待查 | https://www.facebook.com/photo/?fbid=1635597898579132 | judge-needs-check | 貼文未寫劇團與劇種，發文時間未知（datetime 為 null），無法確認是否屬歌仔戲／布袋戲 |
| 待查 | https://www.facebook.com/reel/1427405316148301/ | date-out-of-range |  |
| 待查 | https://www.facebook.com/photo/?fbid=1541293428042944 | judge-needs-check | 為已過的永康慈后宮演出時間更正，只有日期地點，無時間，且無對應卡片 |
| 待查 | https://www.facebook.com/photo/?fbid=1534522768720010 | date-out-of-range |  |
| 待查 | https://www.facebook.com/photo/?fbid=122232388448490067 | date-out-of-range |  |
| 待查 | https://www.facebook.com/photo/?fbid=1521960433309577 | judge-needs-check | 中秋貼文用「今天」且無日期時間，發文時間未知，無法推算 |
| 待查 | https://www.facebook.com/photo/?fbid=1515807753924845 | date-out-of-range |  |
| 待查 | https://www.facebook.com/photo/?fbid=1514693090702978 | date-out-of-range |  |
| 待查 | https://www.facebook.com/photo/?fbid=122186354384804497 | judge-needs-check | 預告《封神榜》大型演出，但正文與已知海報紀錄都沒有日期、時間、地點。 |
| 待查 | https://www.facebook.com/photo/?fbid=122185121900804497 | judge-needs-check | 全是農曆日期且無年份，括號內星期與2026年農曆九月對不上（疑為舊行程表重貼），無法確定換算。 |
| 待查 | https://www.facebook.com/photo/?fbid=1546668374148203 | judge-needs-check | 外臺歌仔戲2.0 入選名單與11/27–12/13 高雄中山堂三週區間，沒有各團場次日期時間，無法建卡。 |
| 待查 | https://www.facebook.com/photo/?fbid=1611874497619227 | possible-duplicate:lecture-2026-11-01-tcpt-tech-visual-magic |  |
| 待查 | https://www.opentix.life/event/2090269380048343041 | judge-needs-check | 聯合展演含10團、多場次，簡介被截斷，看不出各場次的劇種與劇團，不猜。 |
| 待查 | https://www.opentix.life/program/2080173157578416129 | puppet-not-budaixi |  |
| 待查 | https://www.opentix.life/program/2112035354878472193 | puppet-not-budaixi |  |
| 待查 | https://www.opentix.life/program/2088104133013299200 | judge-needs-check | 偶偶偶劇團《小狐狸買手套》原文沒有布袋戲證據，既有卡片標布袋戲可能誤收，需人工確認劇種。 |
| 待查 | https://github.com/eric1810-tw/taiwan-opera-calendar/issues/9 | judge-needs-check | 回報只寫「春美」，未寫劇種，內文被截斷且多數場次無時間，需查原貼文確認劇團與劇種。 |

## 紀錄檔

- 本輪狀態：/Users/eric/aiwork/taiwan-opera-calendar/patrol_state/runs/2026-10-30_0311/state.json
- 巡檢紀錄：patrol_runs/2026-10-30_0311.json（/Users/eric/aiwork/taiwan-opera-calendar）
- 證據：patrol_evidence/2026-10-30_0311/
- 產生時間：2026-10-30T03:43:12+08:00
