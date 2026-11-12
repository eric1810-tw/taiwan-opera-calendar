# 巡檢報告 2026-11-13_0311（patrol-v2，正式）

## 結論

| 項目 | 結果 |
| --- | --- |
| 執行 | 開始 2026-11-13T03:11:35+08:00；結果 進行中；步驟 preflight:done、collect:done、pack:done、judge:done、check:done、verify:done、review:done、apply:done、publish:done、report:running |
| 來源 | 20 個：完整 4、部分 16、失敗 0、未讀 0 |
| 資料 | 送判讀 189 篇／圖 5 張；變更提案 12、確認一致 21、送查證 65（成立 1、與卡相同 5、查無佐證不收 61）、退回 0、漏處置 0；已過期不收 72、遠期暫存 5 |
| 寫入 | 寫入 0、add_card 拒絕 11、審查未通過 1 |
| 發布 | verified；SHA 57c107112b951db3b378d6ffd480439aa99577f3；Actions 43293294280 |

## 模型與用量

| 角色 | 模型 | 依據 |
| --- | --- | --- |
| main | claude-sonnet-5-5 | get_session self：effort=medium |
| judge | sonnet | Agent 工具 model 參數；effort=medium |
| verify | opus | Agent 工具 model 參數；effort=medium |
| review | opus | Agent 工具 model 參數；effort=medium |

- 判讀批次 8；送出貼文 189 篇、圖片 5 張、正文約 64715 字
- 略過（已判讀未變動）89 篇；窗口外 38 篇
- 第二次審查：有（12 項）

## 來源

| 來源 | 狀態 | 範圍 | 說明 |
| --- | --- | --- | --- |
| threads:joe_huang_k_w | 部分 | 首屏 5 篇、累積 11 篇；最新 2026-11-12T22:33:24+08:00、最舊 2026-11-03T21:56:59+08:00；捲動 2 次、停止原因 reached-window；圖片下載 15 張 | 不變式通過；證據 /Users/eric/aiwork/taiwan-opera-calendar/patrol_evidence/2026-11-13_0311/threads_joe_huang… |
| threads:h.akito_1996 | 完整 | 7 天窗口讀完（停止原因 reached-window）；窗口內 0 篇皆有處置；圖片 0 張皆已判讀 | 不變式通過、逐篇處置完成 |
| threads:the_rin.lpm | 部分 | 首屏 4 篇、累積 10 篇；最新 2026-11-12T19:18:17+08:00、最舊 2026-09-26T14:32:03+08:00；捲動 3 次、停止原因 reached-window；圖片下載 15 張 | 不變式通過；證據 /Users/eric/aiwork/taiwan-opera-calendar/patrol_evidence/2026-11-13_0311/threads_the_rin.l… |
| threads:xuefeng_lu_ | 完整 | 7 天窗口讀完（停止原因 reached-window）；窗口內 2 篇皆有處置；圖片 0 張皆已判讀 | 不變式通過、逐篇處置完成 |
| threads:yuzhongluo | 部分 | 首屏 4 篇、累積 25 篇；最新 2026-11-12T23:08:27+08:00、最舊 2026-10-28T01:03:35+08:00；捲動 5 次、停止原因 reached-window；圖片下載 29 張 | 不變式通過；證據 /Users/eric/aiwork/taiwan-opera-calendar/patrol_evidence/2026-11-13_0311/threads_yuzhonglu… |
| threads:taiwaneseopera168 | 部分 | 首屏 3 篇、累積 14 篇；最新 2026-11-12T23:39:53+08:00、最舊 2026-08-16T02:33:12+08:00；捲動 6 次、停止原因 no-new-after-3；圖片下載 23 張 | 不變式通過；證據 /Users/eric/aiwork/taiwan-opera-calendar/patrol_evidence/2026-11-13_0311/threads_taiwanese… |
| threads:jing__1017 | 部分 | 首屏 4 篇、累積 17 篇；最新 2026-11-12T23:20:51+08:00、最舊 2026-10-28T19:50:21+08:00；捲動 6 次、停止原因 reached-window；圖片下載 30 張 | 不變式通過；證據 /Users/eric/aiwork/taiwan-opera-calendar/patrol_evidence/2026-11-13_0311/threads_jing__101… |
| threads:hilang.on.tour | 完整 | 7 天窗口讀完（停止原因 reached-window）；窗口內 0 篇皆有處置；圖片 0 張皆已判讀 | 不變式通過、逐篇處置完成 |
| threads:yolin1991 | 部分 | 首屏 4 篇、累積 8 篇；最新 2026-11-12T23:41:50+08:00、最舊 2026-11-05T16:28:03+08:00；捲動 2 次、停止原因 reached-window；圖片下載 8 張 | 不變式通過；證據 /Users/eric/aiwork/taiwan-opera-calendar/patrol_evidence/2026-11-13_0311/threads_yolin1991… |
| facebook:sunhope.fans | 部分 | 首屏 3 篇、累積 20 篇；最新 無、最舊 無；捲動 20 次、停止原因 max-scrolls；圖片下載 26 張 | 不變式通過；證據 /Users/eric/aiwork/taiwan-opera-calendar/patrol_evidence/2026-11-13_0311/facebook_sunhope.… |
| facebook:HsiaoHsiYuan1913 | 部分 | 首屏 1 篇、累積 24 篇；最新 無、最舊 無；捲動 20 次、停止原因 max-scrolls；圖片下載 50 張 | 不變式通過；證據 /Users/eric/aiwork/taiwan-opera-calendar/patrol_evidence/2026-11-13_0311/facebook_HsiaoHsi… |
| facebook:100063868113954 | 部分 | 首屏 3 篇、累積 20 篇；最新 無、最舊 無；捲動 20 次、停止原因 max-scrolls；圖片下載 39 張 | 不變式通過；證據 /Users/eric/aiwork/taiwan-opera-calendar/patrol_evidence/2026-11-13_0311/facebook_10006386… |
| facebook:MingHuaYuanTianTaiwaneseOpera | 部分 | 首屏 1 篇、累積 21 篇；最新 無、最舊 無；捲動 20 次、停止原因 max-scrolls；圖片下載 55 張 | 不變式通過；證據 /Users/eric/aiwork/taiwan-opera-calendar/patrol_evidence/2026-11-13_0311/facebook_MingHuaY… |
| facebook:61574134933376 | 部分 | 首屏 1 篇、累積 5 篇；最新 無、最舊 無；捲動 4 次、停止原因 no-new-after-3；圖片下載 16 張 | 不變式通過；證據 /Users/eric/aiwork/taiwan-opera-calendar/patrol_evidence/2026-11-13_0311/facebook_61574134… |
| facebook:mhysun | 部分 | 首屏 1 篇、累積 20 篇；最新 無、最舊 無；捲動 20 次、停止原因 max-scrolls；圖片下載 87 張 | 不變式通過；證據 /Users/eric/aiwork/taiwan-opera-calendar/patrol_evidence/2026-11-13_0311/facebook_mhysun.j… |
| facebook:61594936681482 | 部分 | 首屏 1 篇、累積 7 篇；最新 無、最舊 無；捲動 7 次、停止原因 no-new-after-3；圖片下載 23 張 | 不變式通過；證據 /Users/eric/aiwork/taiwan-opera-calendar/patrol_evidence/2026-11-13_0311/facebook_61594936… |
| facebook:lanyang.opera | 部分 | 首屏 1 篇、累積 23 篇；最新 無、最舊 無；捲動 20 次、停止原因 max-scrolls；圖片下載 38 張 | 不變式通過；證據 /Users/eric/aiwork/taiwan-opera-calendar/patrol_evidence/2026-11-13_0311/facebook_lanyang.… |
| facebook:Taichungpuppettheater | 部分 | 首屏 1 篇、累積 25 篇；最新 無、最舊 無；捲動 20 次、停止原因 max-scrolls；圖片下載 42 張 | 不變式通過；證據 /Users/eric/aiwork/taiwan-opera-calendar/patrol_evidence/2026-11-13_0311/facebook_Taichung… |
| culture | 部分 | total 504、fetchedAt 2026-11-08T09:58:57+08:00、戲曲紀錄 9 筆 | moc_records 已 113 小時未更新 |
| issues | 完整 | 3 筆皆有處置 | 逐筆處置完成 |

- OPENTIX：sitemap 828 個活動、本輪有變 633、抓取 250、戲曲相關且未過期 36、延後 383、錯誤 0

## 卡片變更

| 編號 | 動作 | 來源 | 內容 | 差異 | 審查 | 寫入 |
| --- | --- | --- | --- | --- | --- | --- |
| chg-001 | add | https://www.facebook.com/photo/?fbid=1670847141720874 | 明華園天字戲劇團｜清雲寺外台演出｜屏東縣鹽埔鄉彭厝村青雲街1號｜2026-11-20 正戲 未公布、2026-11-21 正戲 未公布 |  | approve：日期與地點出自 source.text「清雲寺 時間：11/20-11/21 地點：屏東縣鹽埔鄉彭厝村青雲街1號」；海… | rejected artist-not-in-quote |
| chg-002 | add | https://www.facebook.com/photo/?fbid=1562267689278851 | 明華園天字戲劇團｜東隆宮外台演出｜國曆11/09 澎湖縣馬公市石泉里33號【朱王廟】 時間未標示；明華園天字戲劇團 國曆11/10 澎湖縣馬公市石泉里33號【朱王廟】 時間未標示；明華園天字戲劇團 國曆11/10 高雄市前鎮區康定路365… |  | reject：location 欄位錯誤：把整張戲路表 reading（11/09 朱王廟起至 12/08 東隆宮共數十筆）整串塞進… | held  |
| chg-003 | add | https://www.facebook.com/photo/?fbid=122315789156250015 | 小金枝歌劇團｜《棄老山傳奇》｜高雄中山堂劇場戶外陽光草坪｜2026-11-27 正戲 19:00 |  | approve：source.text「11/27（五）小金枝歌劇團《棄老山傳奇》」「每場次開演時間｜19:00」「演出地點｜高雄中山… | rejected badgeType-not-free |
| chg-004 | add | https://www.facebook.com/photo/?fbid=122315789156250015 | 新和興總團｜《秦英掛帥》｜高雄中山堂劇場戶外陽光草坪｜2026-11-28 正戲 19:00 |  | approve：source.text「11/28（六）新和興總團《秦英掛帥》」，時間 19:00、地點中山堂戶外陽光草坪、免費皆出自… | rejected badgeType-not-free |
| chg-005 | add | https://www.facebook.com/photo/?fbid=122315789156250015 | 藝華園戲劇團｜《八仙傳奇－張果老與藍采和》｜高雄中山堂劇場戶外陽光草坪｜2026-11-29 正戲 19:00 |  | approve：source.text「11/29（日）藝華園戲劇團《八仙傳奇－張果老與藍采和》」，時間、地點、免費皆有原文；11/2… | rejected badgeType-not-free |
| chg-006 | add | https://www.facebook.com/photo/?fbid=122315789156250015 | 新藝芳歌劇團｜《金蟾緣》｜高雄中山堂劇場戶外陽光草坪｜2026-12-03 正戲 19:00 |  | approve：source.text「12/03（四）新藝芳歌劇團《金蟾緣》」，時間 19:00、地點、免費有原文；12/03 為週… | rejected badgeType-not-free |
| chg-007 | add | https://www.facebook.com/photo/?fbid=122315789156250015 | 佩儀歌劇團｜《吳漢殺妻》｜高雄中山堂劇場戶外陽光草坪｜2026-12-04 正戲 19:00 |  | approve：source.text「12/04（五）佩儀歌劇團《吳漢殺妻》」，時間、地點、免費有原文；12/04 為週五，正確。 | rejected badgeType-not-free |
| chg-008 | add | https://www.facebook.com/photo/?fbid=122315789156250015 | 文惜歌仔戲劇團｜《焰火長槍：火帥與玉龍的背影》｜高雄中山堂劇場戶外陽光草坪｜2026-12-05 正戲 19:00 |  | approve：source.text「12/05（六）文惜歌仔戲劇團《焰火長槍：火帥與玉龍的背影》」，時間、地點、免費有原文；12/… | rejected badgeType-not-free |
| chg-009 | add | https://www.facebook.com/photo/?fbid=122315789156250015 | 春明歌劇團｜《玉虛戰歌．天命之戰》｜高雄中山堂劇場戶外陽光草坪｜2026-12-11 正戲 19:00 |  | approve：source.text「12/11（五）春明歌劇團《玉虛戰歌．天命之戰》」，時間、地點、免費有原文；12/11 為週五… | rejected badgeType-not-free |
| chg-010 | add | https://www.facebook.com/photo/?fbid=122315789156250015 | 水錦歌劇團｜《對面夫妻～韋馱與觀音》｜高雄中山堂劇場戶外陽光草坪｜2026-12-12 正戲 19:00 |  | approve：source.text「12/12（六）水錦歌劇團《對面夫妻～韋馱與觀音》」，時間、地點、免費有原文；12/12 為週… | rejected badgeType-not-free |
| chg-011 | add | https://www.facebook.com/photo/?fbid=122315789156250015 | 明華園星字戲劇團｜《斷案青天－陰錯陽差》｜高雄中山堂劇場戶外陽光草坪｜2026-12-13 正戲 19:00 |  | approve：source.text「12/13（日）明華園星字戲劇團《斷案青天－陰錯陽差》」，時間、地點、免費有原文；12/13 … | rejected badgeType-not-free |
| chg-012 | add（查證成立） | https://www.opentix.life/event/2090269380048343041（原貼文 https://www.opentix.life/event/2090269380048343041） | 薪傳歌仔戲劇團｜《蒼原孤雁》（戲釀青春──2026駐團演訓育成聯合展演）｜臺灣戲曲中心小表演廳（臺北市士林區文林路751號）｜2026-11-14 正戲 14:30 |  | approve：OPENTIX 頁面原文【小表演廳】「11/14（六）14:30 薪傳歌仔戲劇團《蒼原孤雁》」，場館地址「臺北市士林區… | rejected location-not-in-quote,title-not-in-quote,badgeType-not-ticket |

## 遠期場次（超過 120 天，進入 120 天內自動重驗）

| 貼文 | 內容 |
| --- | --- |
| https://www.facebook.com/photo/?fbid=1560228489482771 | 明華園天字戲劇團｜《重返：愛河戀夢》｜臺灣戲曲中心 大表演廳｜2027-06-05、2027-06-06 |
| https://www.facebook.com/MingHuaYuanTianTaiwaneseOpera/reels_tab | 明華園天字戲劇團｜《重返：愛河戀夢》｜臺灣戲曲中心 大表演廳｜2027-06-05、2027-06-06 |
| https://www.threads.com/@taiwaneseopera168/post/DfWAAt6CT5a | 烏貓戲出｜《白賊七》｜高雄中山堂劇場(高雄市左營區實踐路71號)｜2027-04-17、2027-04-18 |
| https://www.threads.com/@taiwaneseopera168/post/DfWAAt6CT5a | 薪傳歌仔戲劇團｜《封神榜．文王食子》｜高雄中山堂劇場(高雄市左營區實踐路71號)｜2027-04-24、2027-04-25 |
| https://www.threads.com/@taiwaneseopera168/post/DfWAAt6CT5a | 燕玲戲劇團｜《韓信設窖安軍心》｜高雄中山堂劇場(高雄市左營區實踐路71號)｜2027-03-20、2027-03-21 |

## 紀錄檔

- 本輪狀態：/Users/eric/aiwork/taiwan-opera-calendar/patrol_state/runs/2026-11-13_0311/state.json
- 巡檢紀錄：patrol_runs/2026-11-13_0311.json（/Users/eric/aiwork/taiwan-opera-calendar）
- 證據：patrol_evidence/2026-11-13_0311/
- 產生時間：2026-11-13T03:45:16+08:00
