# 巡檢報告 2026-11-23_0311（patrol-v2，正式）

## 需要 Eric 決定

- 前幾天的巡檢沒有完成：2026-11-21：輪次 2026-11-21_0311 沒有跑完

## 結論

| 項目 | 結果 |
| --- | --- |
| 執行 | 開始 2026-11-23T03:11:08+08:00；結果 進行中；步驟 preflight:done、collect:done、pack:done、judge:done、check:done、verify:done、review:done、apply:done、publish:done、report:running |
| 來源 | 21 個：完整 8、部分 13、失敗 0、未讀 0 |
| 資料 | 送判讀 83 篇／圖 38 張；變更提案 8、確認一致 19、送查證 19（成立 2、與卡相同 4、查無佐證不收 13）、退回 0、漏處置 0；已過期不收 18、遠期暫存 8 |
| 寫入 | 寫入 1、add_card 拒絕 5、審查未通過 2 |
| 發布 | verified；SHA b32ae16f4b635ac64db76173a01dc34bb5297c9a；Actions 45061191123 |

## 模型與用量

| 角色 | 模型 | 依據 |
| --- | --- | --- |
| main | claude-sonnet-5-5 | get_session self：effort=medium |
| judge | sonnet | Agent 工具 model 參數；effort=medium |
| verify | opus | Agent 工具 model 參數；effort=medium |
| review | opus | Agent 工具 model 參數；effort=medium |

- 判讀批次 4；送出貼文 83 篇、圖片 38 張、正文約 13517 字
- 略過（已判讀未變動）28 篇；窗口外 63 篇
- 第二次審查：有（8 項）

## 來源

| 來源 | 狀態 | 範圍 | 說明 |
| --- | --- | --- | --- |
| threads:joe_huang_k_w | 部分 | 首屏 4 篇、累積 16 篇；最新 2026-11-23T00:01:53+08:00、最舊 2026-11-07T16:49:05+08:00；捲動 1 次、停止原因 reached-window；圖片下載 24 張 | 不變式通過；證據 /Users/eric/aiwork/taiwan-opera-calendar/patrol_evidence/2026-11-23_0311/threads_joe_huang… |
| threads:h.akito_1996 | 部分 | 首屏 7 篇、累積 7 篇；最新 2026-11-22T14:24:52+08:00、最舊 2026-09-27T00:04:33+08:00；捲動 3 次、停止原因 no-new-after-3；圖片下載 14 張 | 不變式通過；證據 /Users/eric/aiwork/taiwan-opera-calendar/patrol_evidence/2026-11-23_0311/threads_h.akito_1… |
| threads:the_rin.lpm | 部分 | 首屏 5 篇、累積 5 篇；最新 2026-11-22T18:49:22+08:00、最舊 2026-10-01T22:31:26+08:00；捲動 3 次、停止原因 no-new-after-3；圖片下載 18 張 | 不變式通過；證據 /Users/eric/aiwork/taiwan-opera-calendar/patrol_evidence/2026-11-23_0311/threads_the_rin.l… |
| threads:xuefeng_lu_ | 完整 | 7 天窗口讀完（停止原因 reached-window）；窗口內 2 篇皆有處置；圖片 1 張皆已判讀 | 不變式通過、逐篇處置完成 |
| threads:yuzhongluo | 部分 | 首屏 4 篇、累積 4 篇；最新 2026-11-22T23:08:25+08:00、最舊 2026-11-21T14:56:41+08:00；捲動 3 次、停止原因 no-new-after-3；圖片下載 4 張 | 不變式通過；證據 /Users/eric/aiwork/taiwan-opera-calendar/patrol_evidence/2026-11-23_0311/threads_yuzhonglu… |
| threads:taiwaneseopera168 | 部分 | 首屏 4 篇、累積 4 篇；最新 2026-11-22T23:39:22+08:00、最舊 2026-08-16T02:33:12+08:00；捲動 3 次、停止原因 no-new-after-3；圖片下載 1 張 | 不變式通過；證據 /Users/eric/aiwork/taiwan-opera-calendar/patrol_evidence/2026-11-23_0311/threads_taiwanese… |
| threads:jing__1017 | 部分 | 首屏 5 篇、累積 5 篇；最新 2026-11-22T22:35:12+08:00、最舊 2026-10-28T19:50:21+08:00；捲動 3 次、停止原因 no-new-after-3；圖片下載 5 張 | 不變式通過；證據 /Users/eric/aiwork/taiwan-opera-calendar/patrol_evidence/2026-11-23_0311/threads_jing__101… |
| threads:hilang.on.tour | 完整 | 7 天窗口讀完（停止原因 reached-window）；窗口內 0 篇皆有處置；圖片 0 張皆已判讀 | 不變式通過、逐篇處置完成 |
| threads:yolin1991 | 部分 | 首屏 5 篇、累積 5 篇；最新 2026-11-22T14:35:35+08:00、最舊 2026-11-18T16:11:34+08:00；捲動 3 次、停止原因 no-new-after-3；圖片下載 6 張 | 不變式通過；證據 /Users/eric/aiwork/taiwan-opera-calendar/patrol_evidence/2026-11-23_0311/threads_yolin1991… |
| threads:yilan_taiwan | 部分 | 首屏 4 篇、累積 4 篇；最新 2026-11-22T11:14:10+08:00、最舊 2026-11-20T16:13:13+08:00；捲動 3 次、停止原因 no-new-after-3；圖片下載 6 張 | 不變式通過；證據 /Users/eric/aiwork/taiwan-opera-calendar/patrol_evidence/2026-11-23_0311/threads_yilan_tai… |
| facebook:sunhope.fans | 部分 | 首屏 1 篇、累積 9 篇；最新 2026-11-20T03:12:36+08:00、最舊 2026-11-02T19:36:00+08:00；捲動 1 次、停止原因 reached-window；圖片下載 29 張 | 不變式通過；證據 /Users/eric/aiwork/taiwan-opera-calendar/patrol_evidence/2026-11-23_0311/facebook_sunhope.… |
| facebook:HsiaoHsiYuan1913 | 部分 | 首屏 3 篇、累積 11 篇；最新 2026-05-07T12:00:00+08:00、最舊 2026-05-07T12:00:00+08:00；捲動 1 次、停止原因 reached-window；圖片下載 18 張 | 不變式通過；證據 /Users/eric/aiwork/taiwan-opera-calendar/patrol_evidence/2026-11-23_0311/facebook_HsiaoHsi… |
| facebook:100063868113954 | 部分 | 首屏 3 篇、累積 8 篇；最新 2026-11-22T03:12:58+08:00、最舊 2026-11-11T07:29:00+08:00；捲動 2 次、停止原因 reached-window；圖片下載 9 張 | 不變式通過；證據 /Users/eric/aiwork/taiwan-opera-calendar/patrol_evidence/2026-11-23_0311/facebook_10006386… |
| facebook:MingHuaYuanTianTaiwaneseOpera | 完整 | 7 天窗口讀完（停止原因 reached-window）；窗口內 3 篇皆有處置；圖片 2 張皆已判讀 | 不變式通過、逐篇處置完成 |
| facebook:61574134933376 | 部分 | 首屏 3 篇、累積 8 篇；最新 2026-11-19T03:13:22+08:00、最舊 2026-10-23T12:00:00+08:00；捲動 1 次、停止原因 reached-window；圖片下載 11 張 | 不變式通過；證據 /Users/eric/aiwork/taiwan-opera-calendar/patrol_evidence/2026-11-23_0311/facebook_61574134… |
| facebook:mhysun | 部分 | 首屏 3 篇、累積 11 篇；最新 2026-11-21T03:13:32+08:00、最舊 2026-10-31T23:10:00+08:00；捲動 1 次、停止原因 reached-window；圖片下載 50 張 | 不變式通過；證據 /Users/eric/aiwork/taiwan-opera-calendar/patrol_evidence/2026-11-23_0311/facebook_mhysun.j… |
| facebook:61594936681482 | 完整 | 7 天窗口讀完（停止原因 reached-window）；窗口內 0 篇皆有處置；圖片 0 張皆已判讀 | 不變式通過、逐篇處置完成 |
| facebook:lanyang.opera | 完整 | 7 天窗口讀完（停止原因 reached-window）；窗口內 3 篇皆有處置；圖片 3 張皆已判讀 | 不變式通過、逐篇處置完成 |
| facebook:Taichungpuppettheater | 完整 | 7 天窗口讀完（停止原因 reached-window）；窗口內 1 篇皆有處置；圖片 5 張皆已判讀 | 不變式通過、逐篇處置完成 |
| culture | 完整 | 9 筆皆有處置 | 逐筆處置完成 |
| issues | 完整 | 3 筆皆有處置 | 逐筆處置完成 |

- OPENTIX：sitemap 801 個活動、本輪有變 628、抓取 250、戲曲相關且未過期 29、延後 378、錯誤 0

## 卡片變更

| 編號 | 動作 | 來源 | 內容 | 差異 | 審查 | 寫入 |
| --- | --- | --- | --- | --- | --- | --- |
| chg-001 | add | https://www.facebook.com/dadaochen2011/posts/pfbid035yrs3sdbyzzLWJV1WbpfxqYc2j1HxfZ5RCVMus3Ky58MWkAHYvXnQuXJcSRzN9dWl | 台北市和華樂社｜《周仁獻嫂》｜大龍峒保安宮庭園廣場｜2026-11-23 正戲 19:00 |  | approve：海報圖（3633c9be…jpg）大龍峒保安宮庭園廣場表列「11/23(一) 台北市和華樂社《周仁獻嫂》全程直播」，標… | rejected badgeType-not-free |
| chg-002 | add | https://www.facebook.com/dadaochen2011/posts/pfbid035yrs3sdbyzzLWJV1WbpfxqYc2j1HxfZ5RCVMus3Ky58MWkAHYvXnQuXJcSRzN9dWl | 明華園玄字戲劇團｜《西遊記．大鬧天宮》｜大龍峒保安宮庭園廣場｜2026-11-24 正戲 19:00 |  | approve：海報表列「11/24(二) 明華園玄字戲劇團《西遊記．大鬧天宮》」，地點在大龍峒保安宮庭園廣場區塊，時間依標頭「每晚7… | rejected badgeType-not-free |
| chg-003 | add | https://www.facebook.com/dadaochen2011/posts/pfbid035yrs3sdbyzzLWJV1WbpfxqYc2j1HxfZ5RCVMus3Ky58MWkAHYvXnQuXJcSRzN9dWl | 國立臺灣戲曲學院｜《熱天的戀夢》｜大龍峒保安宮庭園廣場｜2026-11-26 正戲 19:00 |  | approve：海報表列「11/26(四) 國立臺灣戲曲學院《熱天的戀夢》」，屬大龍峒保安宮庭園廣場區塊，19:00、免費入座；歌仔戲… | rejected badgeType-not-free |
| chg-004 | add | https://www.facebook.com/dadaochen2011/posts/pfbid035yrs3sdbyzzLWJV1WbpfxqYc2j1HxfZ5RCVMus3Ky58MWkAHYvXnQuXJcSRzN9dWl | 葉麗珠三姊妹歌劇團｜《斬鄭英》｜松山車站南側交4廣場｜2026-11-27 正戲 19:00 |  | approve：海報松山車站南側交4廣場區塊列「11/27(五) 葉麗珠三姊妹歌劇團《斬鄭英》全程直播」，地點正確（未誤套大龍峒），1… | rejected badgeType-not-free |
| chg-005 | add | https://www.facebook.com/lanyang.opera/posts/pfbid02fzCMQWgdc9UYpsqU7MCcjupqHxRhoLJLiBJjJSKSohNZfwX5uy94jLcoKVAqtADFl | 蘭陽戲劇團｜《楊宗保與穆桂英》｜基隆表演藝術中心 演藝廳（基隆市中正區信一路181號）｜2026-12-13 正戲 14:30 |  | approve：海報（363c82c6…jpg）明載「蘭陽戲劇團《楊宗保與穆桂英》12/13 (Sun.) 14:30 基隆表演藝術中… | added  |
| chg-006 | add | https://www.facebook.com/permalink.php?story_fbid=pfbid02cL7LZhMCsfpRLDx7pngAZWEQgPaVi8asfoJp22XrN55YbYPh2KJYUVCrfQ7895qhl&id=100063868113954 | 台北大龍峒和華樂社｜周仁獻嫂｜臺北市大同區保安里哈密街61號（大龍峒保安宮）｜2026-11-23 正戲 19:00 |  | reject：與 chg-001 為同一場演出：海報（d699114e…jpg）「11/23 晚上7:00 演出劇團 台北大龍峒和華… | held  |
| chg-007 | add（查證成立） | http://karensie.blogspot.com/2015/12/1041224.html（原貼文 https://www.opentix.life/event/2080109546140397568） | 一心戲劇團｜《閻王的假期》｜臺北市藝文推廣處城市舞台｜2026-12-05 正戲 14:30、2026-12-06 正戲 14:30 |  | approve：阿K部落格「歌仔戲相關售票資訊(115/11/21更)」（2026年11月21日發文，網址路徑雖為 2015 但內容為… | rejected badgeType-not-ticket |
| chg-008 | add（查證成立） | http://karensie.blogspot.com/2015/12/1041224.html（原貼文 https://www.opentix.life/event/2112431894778032129） | 奇巧劇團｜《鞍馬天狗》十週年慶生派對｜臺南文創園區 漂丿白鷺live house｜2026-12-06 正戲 15:00、2026-12-06 正戲 19:00 |  | needs-check：日期時間地點出自部落格原文「12/06(日)15:00&19:00奇巧劇團《鞍馬天狗》十週年慶生派對 KURAMA T… | held  |

## 遠期場次（超過 120 天，進入 120 天內自動重驗）

| 貼文 | 內容 |
| --- | --- |
| https://www.facebook.com/photo/?fbid=1560228489482771 | 明華園天字戲劇團｜《重返：愛河戀夢》｜臺灣戲曲中心 大表演廳｜2027-06-05、2027-06-06 |
| https://www.facebook.com/MingHuaYuanTianTaiwaneseOpera/reels_tab | 明華園天字戲劇團｜《重返：愛河戀夢》｜臺灣戲曲中心 大表演廳｜2027-06-05、2027-06-06 |
| https://www.threads.com/@taiwaneseopera168/post/DfWAAt6CT5a | 烏貓戲出｜《白賊七》｜高雄中山堂劇場(高雄市左營區實踐路71號)｜2027-04-17、2027-04-18 |
| https://www.threads.com/@taiwaneseopera168/post/DfWAAt6CT5a | 薪傳歌仔戲劇團｜《封神榜．文王食子》｜高雄中山堂劇場(高雄市左營區實踐路71號)｜2027-04-24、2027-04-25 |
| https://www.threads.com/@jing__1017/post/DfzIPO8E6F0 | 烏貓戲出｜《白賊七》｜高雄中山堂劇場｜2027-04-17、2027-04-18 |
| https://www.threads.com/@jing__1017/post/DfzIPO8E6F0 | 薪傳歌仔戲劇團｜《封神榜·文王食子》｜高雄中山堂劇場｜2027-04-24、2027-04-25 |
| https://www.threads.com/@taiwaneseopera168/post/Df1HM9wEdDa | 烏貓戲出｜《白賊七》｜高雄中山堂劇場｜2027-04-17、2027-04-18 |
| https://www.threads.com/@taiwaneseopera168/post/Df1HM9wEdDa | 薪傳歌仔戲劇團｜《封神榜·文王食子》｜高雄中山堂劇場｜2027-04-24、2027-04-25 |

## 紀錄檔

- 本輪狀態：/Users/eric/aiwork/taiwan-opera-calendar/patrol_state/runs/2026-11-23_0311/state.json
- 巡檢紀錄：patrol_runs/2026-11-23_0311.json（/Users/eric/aiwork/taiwan-opera-calendar）
- 證據：patrol_evidence/2026-11-23_0311/
- 產生時間：2026-11-23T03:32:05+08:00
