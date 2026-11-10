# 巡檢報告 2026-11-11_0311（patrol-v2，正式）

## 結論

| 項目 | 結果 |
| --- | --- |
| 執行 | 開始 2026-11-11T03:11:00+08:00；結果 進行中；步驟 preflight:done、collect:done、pack:done、judge:done、check:done、verify:done、review:done、apply:done、publish:done、report:running |
| 來源 | 20 個：完整 2、部分 18、失敗 0、未讀 0 |
| 資料 | 送判讀 198 篇／圖 6 張；變更提案 10、確認一致 19、送查證 35（成立 1、與卡相同 2、查無佐證不收 34）、退回 0、漏處置 0；已過期不收 74、遠期暫存 4 |
| 寫入 | 寫入 0、add_card 拒絕 10、審查未通過 0 |
| 發布 | verified；SHA f82b3a1aa4e705bed0a2a85147f6815cddc00734；Actions 42887885361 |

## 模型與用量

| 角色 | 模型 | 依據 |
| --- | --- | --- |
| main | claude-sonnet-5-5 | get_session self：effort=medium |
| judge | sonnet | Agent 工具 model 參數；effort=medium |
| verify | opus | Agent 工具 model 參數；effort=medium |
| review | opus | Agent 工具 model 參數；effort=medium |

- 判讀批次 8；送出貼文 198 篇、圖片 6 張、正文約 68483 字
- 略過（已判讀未變動）96 篇；窗口外 22 篇
- 第二次審查：有（10 項）

## 來源

| 來源 | 狀態 | 範圍 | 說明 |
| --- | --- | --- | --- |
| threads:joe_huang_k_w | 部分 | 首屏 4 篇、累積 7 篇；最新 2026-11-08T14:16:48+08:00、最舊 2026-11-03T12:50:20+08:00；捲動 1 次、停止原因 reached-window；圖片下載 13 張 | 不變式通過；證據 /Users/eric/aiwork/taiwan-opera-calendar/patrol_evidence/2026-11-11_0311/threads_joe_huang… |
| threads:h.akito_1996 | 部分 | 首屏 4 篇、累積 6 篇；最新 2026-11-04T17:59:03+08:00、最舊 2026-09-27T00:04:33+08:00；捲動 1 次、停止原因 reached-window；圖片下載 4 張 | 不變式通過；證據 /Users/eric/aiwork/taiwan-opera-calendar/patrol_evidence/2026-11-11_0311/threads_h.akito_1… |
| threads:the_rin.lpm | 部分 | 首屏 4 篇、累積 10 篇；最新 2026-11-10T19:03:41+08:00、最舊 2026-09-26T14:32:03+08:00；捲動 3 次、停止原因 reached-window；圖片下載 15 張 | 不變式通過；證據 /Users/eric/aiwork/taiwan-opera-calendar/patrol_evidence/2026-11-11_0311/threads_the_rin.l… |
| threads:xuefeng_lu_ | 完整 | 7 天窗口讀完（停止原因 reached-window）；窗口內 3 篇皆有處置；圖片 0 張皆已判讀 | 不變式通過、逐篇處置完成 |
| threads:yuzhongluo | 部分 | 首屏 4 篇、累積 16 篇；最新 2026-11-11T00:53:30+08:00、最舊 2026-11-03T14:25:55+08:00；捲動 5 次、停止原因 reached-window；圖片下載 18 張 | 不變式通過；證據 /Users/eric/aiwork/taiwan-opera-calendar/patrol_evidence/2026-11-11_0311/threads_yuzhonglu… |
| threads:taiwaneseopera168 | 部分 | 首屏 5 篇、累積 19 篇；最新 2026-11-11T00:07:22+08:00、最舊 2026-08-16T02:33:12+08:00；捲動 5 次、停止原因 no-new-after-3；圖片下載 24 張 | 不變式通過；證據 /Users/eric/aiwork/taiwan-opera-calendar/patrol_evidence/2026-11-11_0311/threads_taiwanese… |
| threads:jing__1017 | 部分 | 首屏 5 篇、累積 27 篇；最新 2026-11-10T00:51:07+08:00、最舊 2026-10-28T19:50:21+08:00；捲動 10 次、停止原因 reached-window；圖片下載 30 張 | 不變式通過；證據 /Users/eric/aiwork/taiwan-opera-calendar/patrol_evidence/2026-11-11_0311/threads_jing__101… |
| threads:hilang.on.tour | 完整 | 7 天窗口讀完（停止原因 reached-window）；窗口內 0 篇皆有處置；圖片 0 張皆已判讀 | 不變式通過、逐篇處置完成 |
| threads:yolin1991 | 部分 | 首屏 4 篇、累積 8 篇；最新 2026-11-10T06:54:04+08:00、最舊 2026-11-03T21:11:25+08:00；捲動 2 次、停止原因 reached-window；圖片下載 8 張 | 不變式通過；證據 /Users/eric/aiwork/taiwan-opera-calendar/patrol_evidence/2026-11-11_0311/threads_yolin1991… |
| facebook:sunhope.fans | 部分 | 首屏 3 篇、累積 19 篇；最新 無、最舊 無；捲動 20 次、停止原因 max-scrolls；圖片下載 28 張 | 不變式通過；證據 /Users/eric/aiwork/taiwan-opera-calendar/patrol_evidence/2026-11-11_0311/facebook_sunhope.… |
| facebook:HsiaoHsiYuan1913 | 部分 | 首屏 3 篇、累積 23 篇；最新 無、最舊 無；捲動 20 次、停止原因 max-scrolls；圖片下載 38 張 | 不變式通過；證據 /Users/eric/aiwork/taiwan-opera-calendar/patrol_evidence/2026-11-11_0311/facebook_HsiaoHsi… |
| facebook:100063868113954 | 部分 | 首屏 3 篇、累積 21 篇；最新 無、最舊 無；捲動 20 次、停止原因 max-scrolls；圖片下載 48 張 | 不變式通過；證據 /Users/eric/aiwork/taiwan-opera-calendar/patrol_evidence/2026-11-11_0311/facebook_10006386… |
| facebook:MingHuaYuanTianTaiwaneseOpera | 部分 | 首屏 1 篇、累積 23 篇；最新 無、最舊 無；捲動 20 次、停止原因 max-scrolls；圖片下載 61 張 | 不變式通過；證據 /Users/eric/aiwork/taiwan-opera-calendar/patrol_evidence/2026-11-11_0311/facebook_MingHuaY… |
| facebook:61574134933376 | 部分 | 首屏 1 篇、累積 5 篇；最新 無、最舊 無；捲動 4 次、停止原因 no-new-after-3；圖片下載 16 張 | 不變式通過；證據 /Users/eric/aiwork/taiwan-opera-calendar/patrol_evidence/2026-11-11_0311/facebook_61574134… |
| facebook:mhysun | 部分 | 首屏 1 篇、累積 20 篇；最新 無、最舊 無；捲動 20 次、停止原因 max-scrolls；圖片下載 87 張 | 不變式通過；證據 /Users/eric/aiwork/taiwan-opera-calendar/patrol_evidence/2026-11-11_0311/facebook_mhysun.j… |
| facebook:61594936681482 | 部分 | 首屏 1 篇、累積 7 篇；最新 無、最舊 無；捲動 7 次、停止原因 no-new-after-3；圖片下載 23 張 | 不變式通過；證據 /Users/eric/aiwork/taiwan-opera-calendar/patrol_evidence/2026-11-11_0311/facebook_61594936… |
| facebook:lanyang.opera | 部分 | 首屏 1 篇、累積 23 篇；最新 無、最舊 無；捲動 20 次、停止原因 max-scrolls；圖片下載 38 張 | 不變式通過；證據 /Users/eric/aiwork/taiwan-opera-calendar/patrol_evidence/2026-11-11_0311/facebook_lanyang.… |
| facebook:Taichungpuppettheater | 部分 | 首屏 1 篇、累積 25 篇；最新 無、最舊 無；捲動 20 次、停止原因 max-scrolls；圖片下載 42 張 | 不變式通過；證據 /Users/eric/aiwork/taiwan-opera-calendar/patrol_evidence/2026-11-11_0311/facebook_Taichung… |
| culture | 部分 | total 504、fetchedAt 2026-11-08T09:58:57+08:00、戲曲紀錄 9 筆 | moc_records 已 65 小時未更新 |
| issues | 部分 | state=all 共 3 則（含留言） | 已讀取；處置待判讀後確認 |

- OPENTIX：sitemap 827 個活動、本輪有變 625、抓取 250、戲曲相關且未過期 36、延後 375、錯誤 0

## 卡片變更

| 編號 | 動作 | 來源 | 內容 | 差異 | 審查 | 寫入 |
| --- | --- | --- | --- | --- | --- | --- |
| chg-001 | add | https://www.facebook.com/photo/?fbid=122315789156250015 | 小金枝歌劇團｜《棄老山傳奇》｜高雄中山堂劇場戶外陽光草坪｜2026-11-27 正戲 19:00 |  | approve：source.text「11/27（五）小金枝歌劇團《棄老山傳奇》」對得上劇團、劇目、日期（2026-11-27 確為… | rejected badgeType-not-free |
| chg-002 | add | https://www.facebook.com/photo/?fbid=122315789156250015 | 新和興總團｜《秦英掛帥》｜高雄中山堂劇場戶外陽光草坪｜2026-11-28 正戲 19:00 |  | approve：原文「11/28（六）新和興總團《秦英掛帥》」，2026-11-28 為週六，對得上；19:00、地點與免費入場三項都… | rejected badgeType-not-free |
| chg-003 | add | https://www.facebook.com/photo/?fbid=122315789156250015 | 藝華園戲劇團｜《八仙傳奇－張果老與藍采和》｜高雄中山堂劇場戶外陽光草坪｜2026-11-29 正戲 19:00 |  | approve：原文「11/29（日）藝華園戲劇團《八仙傳奇－張果老與藍采和》」，2026-11-29 為週日；劇目全名一致，時間、地… | rejected badgeType-not-free |
| chg-004 | add | https://www.facebook.com/photo/?fbid=122315789156250015 | 新藝芳歌劇團｜《金蟾緣》｜高雄中山堂劇場戶外陽光草坪｜2026-12-03 正戲 19:00 |  | approve：原文「12/03（四）新藝芳歌劇團《金蟾緣》」，2026-12-03 為週四，對得上；時間、地點與免費入場都出自原文共… | rejected badgeType-not-free |
| chg-005 | add | https://www.facebook.com/photo/?fbid=122315789156250015 | 佩儀歌劇團｜《吳漢殺妻》｜高雄中山堂劇場戶外陽光草坪｜2026-12-04 正戲 19:00 |  | approve：原文「12/04（五）佩儀歌劇團《吳漢殺妻》」，2026-12-04 為週五；時間、地點與免費入場都出自原文共用欄。 | rejected badgeType-not-free |
| chg-006 | add | https://www.facebook.com/photo/?fbid=122315789156250015 | 文惜歌仔戲劇團｜《焰火長槍：火帥與玉龍的背影》｜高雄中山堂劇場戶外陽光草坪｜2026-12-05 正戲 19:00 |  | approve：原文「12/05（六）文惜歌仔戲劇團《焰火長槍：火帥與玉龍的背影》」，2026-12-05 為週六；劇團與劇目逐字一致… | rejected badgeType-not-free |
| chg-007 | add | https://www.facebook.com/photo/?fbid=122315789156250015 | 春明歌劇團｜《玉虛戰歌．天命之戰》｜高雄中山堂劇場戶外陽光草坪｜2026-12-11 正戲 19:00 |  | approve：原文「12/11（五）春明歌劇團《玉虛戰歌．天命之戰》」，2026-12-11 為週五；時間、地點與免費入場都出自原文… | rejected badgeType-not-free |
| chg-008 | add | https://www.facebook.com/photo/?fbid=122315789156250015 | 水錦歌劇團｜《對面夫妻～韋馱與觀音》｜高雄中山堂劇場戶外陽光草坪｜2026-12-12 正戲 19:00 |  | approve：原文「12/12（六）水錦歌劇團《對面夫妻～韋馱與觀音》」，2026-12-12 為週六；時間、地點與免費入場都出自原… | rejected badgeType-not-free |
| chg-009 | add | https://www.facebook.com/photo/?fbid=122315789156250015 | 明華園星字戲劇團｜《斷案青天－陰錯陽差》｜高雄中山堂劇場戶外陽光草坪｜2026-12-13 正戲 19:00 |  | approve：原文「12/13（日）明華園星字戲劇團《斷案青天－陰錯陽差》」，2026-12-13 為週日；時間、地點與免費入場都出… | rejected badgeType-not-free |
| chg-010 | add（查證成立） | https://www.opentix.life/event/2090269380048343041（原貼文 https://www.opentix.life/event/2090269380048343041） | 薪傳歌仔戲劇團｜《蒼原孤雁》｜臺灣戲曲中心小表演廳｜2026-11-14 正戲 14:30 |  | approve：OPENTIX 節目頁【小表演廳】段落寫「11/14（六）14:30 薪傳歌仔戲劇團《蒼原孤雁》」，選擇場館一欄列有「… | rejected location-not-in-quote,badgeType-not-ticket |

## 遠期場次（超過 120 天，進入 120 天內自動重驗）

| 貼文 | 內容 |
| --- | --- |
| https://www.facebook.com/photo/?fbid=1560228489482771 | 明華園天字戲劇團｜《重返：愛河戀夢》｜臺灣戲曲中心 大表演廳｜2027-06-05、2027-06-06 |
| https://www.facebook.com/MingHuaYuanTianTaiwaneseOpera/reels_tab | 明華園天字戲劇團｜《重返：愛河戀夢》｜臺灣戲曲中心 大表演廳｜2027-06-05、2027-06-06 |
| https://www.threads.com/@taiwaneseopera168/post/DfWAAt6CT5a | 烏貓戲出｜《白賊七》｜高雄中山堂劇場(高雄市左營區實踐路71號)｜2027-04-17、2027-04-18 |
| https://www.threads.com/@taiwaneseopera168/post/DfWAAt6CT5a | 薪傳歌仔戲劇團｜《封神榜．文王食子》｜高雄中山堂劇場(高雄市左營區實踐路71號)｜2027-04-24、2027-04-25 |

## 紀錄檔

- 本輪狀態：/Users/eric/aiwork/taiwan-opera-calendar/patrol_state/runs/2026-11-11_0311/state.json
- 巡檢紀錄：patrol_runs/2026-11-11_0311.json（/Users/eric/aiwork/taiwan-opera-calendar）
- 證據：patrol_evidence/2026-11-11_0311/
- 產生時間：2026-11-11T03:43:08+08:00
