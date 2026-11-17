# 巡檢報告 2026-11-18_0311（patrol-v2，正式）

## 結論

| 項目 | 結果 |
| --- | --- |
| 執行 | 開始 2026-11-18T03:11:11+08:00；結果 進行中；步驟 preflight:done、collect:done、pack:done、judge:done、check:done、verify:done、review:done、apply:done、publish:done、report:running |
| 來源 | 20 個：完整 3、部分 17、失敗 0、未讀 0 |
| 資料 | 送判讀 196 篇／圖 3 張；變更提案 5、確認一致 24、送查證 47（成立 2、與卡相同 1、查無佐證不收 45）、退回 0、漏處置 0；已過期不收 80、遠期暫存 8 |
| 寫入 | 寫入 0、add_card 拒絕 3、審查未通過 2 |
| 發布 | verified；SHA 3783bfd283e4cf9ed947448d31a7297d58b9a960；Actions 44161360658 |

## 模型與用量

| 角色 | 模型 | 依據 |
| --- | --- | --- |
| main | claude-sonnet-5-5 | get_session self：effort=medium |
| judge | sonnet | Agent 工具 model 參數；effort=medium |
| verify | opus | Agent 工具 model 參數；effort=medium |
| review | opus | Agent 工具 model 參數；effort=medium |

- 判讀批次 8；送出貼文 196 篇、圖片 3 張、正文約 67051 字
- 略過（已判讀未變動）104 篇；窗口外 29 篇
- 第二次審查：有（5 項）

## 來源

| 來源 | 狀態 | 範圍 | 說明 |
| --- | --- | --- | --- |
| threads:joe_huang_k_w | 部分 | 首屏 4 篇、累積 12 篇；最新 2026-11-17T20:53:55+08:00、最舊 2026-11-07T16:49:05+08:00；捲動 3 次、停止原因 reached-window；圖片下載 16 張 | 不變式通過；證據 /Users/eric/aiwork/taiwan-opera-calendar/patrol_evidence/2026-11-18_0311/threads_joe_huang… |
| threads:h.akito_1996 | 部分 | 首屏 4 篇、累積 13 篇；最新 2026-11-17T16:50:33+08:00、最舊 2026-09-27T00:04:33+08:00；捲動 4 次、停止原因 reached-window；圖片下載 10 張 | 不變式通過；證據 /Users/eric/aiwork/taiwan-opera-calendar/patrol_evidence/2026-11-18_0311/threads_h.akito_1… |
| threads:the_rin.lpm | 部分 | 首屏 4 篇、累積 6 篇；最新 2026-11-16T19:23:08+08:00、最舊 2026-09-26T14:32:03+08:00；捲動 1 次、停止原因 reached-window；圖片下載 11 張 | 不變式通過；證據 /Users/eric/aiwork/taiwan-opera-calendar/patrol_evidence/2026-11-18_0311/threads_the_rin.l… |
| threads:xuefeng_lu_ | 完整 | 7 天窗口讀完（停止原因 reached-window）；窗口內 3 篇皆有處置；圖片 0 張皆已判讀 | 不變式通過、逐篇處置完成 |
| threads:yuzhongluo | 部分 | 首屏 4 篇、累積 17 篇；最新 2026-11-17T05:31:05+08:00、最舊 2026-11-11T00:38:21+08:00；捲動 8 次、停止原因 reached-window；圖片下載 22 張 | 不變式通過；證據 /Users/eric/aiwork/taiwan-opera-calendar/patrol_evidence/2026-11-18_0311/threads_yuzhonglu… |
| threads:taiwaneseopera168 | 部分 | 首屏 7 篇、累積 11 篇；最新 2026-11-17T20:29:54+08:00、最舊 2026-08-16T02:33:12+08:00；捲動 3 次、停止原因 reached-window；圖片下載 11 張 | 不變式通過；證據 /Users/eric/aiwork/taiwan-opera-calendar/patrol_evidence/2026-11-18_0311/threads_taiwanese… |
| threads:jing__1017 | 部分 | 首屏 6 篇、累積 30 篇；最新 2026-11-18T00:12:41+08:00、最舊 2026-10-28T19:50:21+08:00；捲動 11 次、停止原因 reached-window；圖片下載 37 張 | 不變式通過；證據 /Users/eric/aiwork/taiwan-opera-calendar/patrol_evidence/2026-11-18_0311/threads_jing__101… |
| threads:hilang.on.tour | 完整 | 7 天窗口讀完（停止原因 reached-window）；窗口內 0 篇皆有處置；圖片 0 張皆已判讀 | 不變式通過、逐篇處置完成 |
| threads:yolin1991 | 部分 | 首屏 4 篇、累積 6 篇；最新 2026-11-16T13:26:48+08:00、最舊 2026-11-10T06:54:04+08:00；捲動 1 次、停止原因 reached-window；圖片下載 6 張 | 不變式通過；證據 /Users/eric/aiwork/taiwan-opera-calendar/patrol_evidence/2026-11-18_0311/threads_yolin1991… |
| facebook:sunhope.fans | 部分 | 首屏 1 篇、累積 20 篇；最新 無、最舊 無；捲動 20 次、停止原因 max-scrolls；圖片下載 41 張 | 不變式通過；證據 /Users/eric/aiwork/taiwan-opera-calendar/patrol_evidence/2026-11-18_0311/facebook_sunhope.… |
| facebook:HsiaoHsiYuan1913 | 部分 | 首屏 1 篇、累積 24 篇；最新 無、最舊 無；捲動 20 次、停止原因 max-scrolls；圖片下載 50 張 | 不變式通過；證據 /Users/eric/aiwork/taiwan-opera-calendar/patrol_evidence/2026-11-18_0311/facebook_HsiaoHsi… |
| facebook:100063868113954 | 部分 | 首屏 4 篇、累積 21 篇；最新 無、最舊 無；捲動 20 次、停止原因 max-scrolls；圖片下載 44 張 | 不變式通過；證據 /Users/eric/aiwork/taiwan-opera-calendar/patrol_evidence/2026-11-18_0311/facebook_10006386… |
| facebook:MingHuaYuanTianTaiwaneseOpera | 部分 | 首屏 1 篇、累積 21 篇；最新 無、最舊 無；捲動 20 次、停止原因 max-scrolls；圖片下載 55 張 | 不變式通過；證據 /Users/eric/aiwork/taiwan-opera-calendar/patrol_evidence/2026-11-18_0311/facebook_MingHuaY… |
| facebook:61574134933376 | 部分 | 首屏 3 篇、累積 17 篇；最新 無、最舊 無；捲動 20 次、停止原因 max-scrolls；圖片下載 31 張 | 不變式通過；證據 /Users/eric/aiwork/taiwan-opera-calendar/patrol_evidence/2026-11-18_0311/facebook_61574134… |
| facebook:mhysun | 部分 | 首屏 1 篇、累積 20 篇；最新 無、最舊 無；捲動 20 次、停止原因 max-scrolls；圖片下載 92 張 | 不變式通過；證據 /Users/eric/aiwork/taiwan-opera-calendar/patrol_evidence/2026-11-18_0311/facebook_mhysun.j… |
| facebook:61594936681482 | 部分 | 首屏 1 篇、累積 7 篇；最新 無、最舊 無；捲動 7 次、停止原因 no-new-after-3；圖片下載 23 張 | 不變式通過；證據 /Users/eric/aiwork/taiwan-opera-calendar/patrol_evidence/2026-11-18_0311/facebook_61594936… |
| facebook:lanyang.opera | 部分 | 首屏 3 篇、累積 21 篇；最新 無、最舊 無；捲動 20 次、停止原因 max-scrolls；圖片下載 25 張 | 不變式通過；證據 /Users/eric/aiwork/taiwan-opera-calendar/patrol_evidence/2026-11-18_0311/facebook_lanyang.… |
| facebook:Taichungpuppettheater | 部分 | 首屏 3 篇、累積 26 篇；最新 無、最舊 無；捲動 20 次、停止原因 max-scrolls；圖片下載 34 張 | 不變式通過；證據 /Users/eric/aiwork/taiwan-opera-calendar/patrol_evidence/2026-11-18_0311/facebook_Taichung… |
| culture | 部分 | total 501、fetchedAt 2026-11-15T10:19:38+08:00、戲曲紀錄 9 筆 | moc_records 已 65 小時未更新 |
| issues | 完整 | 3 筆皆有處置 | 逐筆處置完成 |

- OPENTIX：sitemap 819 個活動、本輪有變 646、抓取 250、戲曲相關且未過期 33、延後 396、錯誤 0

## 卡片變更

| 編號 | 動作 | 來源 | 內容 | 差異 | 審查 | 寫入 |
| --- | --- | --- | --- | --- | --- | --- |
| chg-001 | add | https://www.threads.com/@yuzhongluo/post/Dfy2Iecj_pR | 羅裕誴歌劇團｜《楊排風掛帥》｜大龍峒保安宮庭園廣場｜2026-11-20 正戲 19:00 |  | approve：日期時間「115.11.20 (五)19:00」、地點「大龍峒保安宮庭園廣場」、劇團、劇目《楊排風掛帥》、主演「羅文惜… | rejected artist-not-in-quote |
| chg-002 | add | https://www.threads.com/@taiwaneseopera168/post/Df1vFr_oF6y | 明華園黃字戲劇團｜《神仙孝子 • 劈山救母》｜台南市安平開台天后宮｜2026-11-19 正戲 19:00 |  | approve：原文寫「2026/11/19(四)19:00大戲開鑼 台南市安平開台天后宮」，海報也印「國曆11/19(農曆10/11… | rejected location-not-in-quote |
| chg-003 | add | https://www.threads.com/@taiwaneseopera168/post/Df1vFr_oF6y | 明華園黃字戲劇團｜《神仙孝子 • 劈山救母》｜台南市海尾朝皇宮｜2026-11-20 正戲 未公布 |  | needs-check：日期 11/20 與地點「台南市海尾朝皇宮」有原文和海報兩邊佐證，但這天原文只寫「民戲」。劇目《神仙孝子•劈山救母》在… | held  |
| chg-004 | update（查證成立） | https://web.ncku.edu.tw/p/406-1000-299280,r4153.php?Lang=zh-tw（原貼文 https://www.facebook.com/MingHuaYuanTianTaiwaneseOpera/reels_tab） | 明華園天字戲劇團｜《喜脈緣》｜成大校園｜2026-11-24 正戲 19:00 |  | needs-check：diffs 是空的，但提案和 currentCard 其實有兩處不同：(1) artist 從「未公布」改成「陳昭香」… | held  |
| chg-005 | add（查證成立） | https://www.tw-yishin.com/%e6%bc%94%e5%87%ba%e6%96%b0%e8%a8%8a/2026%e4%b8%80%e5%bf%83%e6%88%b2%e5%8a%87%e5%9c%98%e3%80%8a%e9%96%bb%e7%8e%8b%e7%9a%84%e5%81%87%e6%9c%9f%e3%80%8b/（原貼文 https://www.opentix.life/event/2080109546140397568） | 一心戲劇團｜《閻王的假期》｜城市舞台｜2026-12-05 正戲 14:30、2026-12-06 正戲 14:30 |  | approve：官網原文寫「演出時間：2026/12/05(六)14:30 2026/12/06(日)14:30」與「地點：城市舞台」… | rejected artist-not-in-quote |

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

- 本輪狀態：/Users/eric/aiwork/taiwan-opera-calendar/patrol_state/runs/2026-11-18_0311/state.json
- 巡檢紀錄：patrol_runs/2026-11-18_0311.json（/Users/eric/aiwork/taiwan-opera-calendar）
- 證據：patrol_evidence/2026-11-18_0311/
- 產生時間：2026-11-18T03:42:55+08:00
