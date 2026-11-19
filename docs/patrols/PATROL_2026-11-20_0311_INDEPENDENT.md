# 巡檢報告 2026-11-20_0311（patrol-v2，正式）

## 結論

| 項目 | 結果 |
| --- | --- |
| 執行 | 開始 2026-11-20T03:11:10+08:00；結果 進行中；步驟 preflight:done、collect:done、pack:done、judge:done、check:done、verify:done、review:done、apply:done、publish:done、report:running |
| 來源 | 21 個：完整 3、部分 18、失敗 0、未讀 0 |
| 資料 | 送判讀 215 篇／圖 12 張；變更提案 20、確認一致 20、送查證 17（成立 1、與卡相同 1、查無佐證不收 15）、退回 0、漏處置 0；已過期不收 82、遠期暫存 10 |
| 寫入 | 寫入 1、add_card 拒絕 16、審查未通過 3 |
| 發布 | verified；SHA 2a9de134a5c40fb0927bb26cb2504d701200dd4e；Actions 44601279846 |

## 模型與用量

| 角色 | 模型 | 依據 |
| --- | --- | --- |
| main | claude-sonnet-5-5 | get_session self：effort=medium |
| judge | sonnet | Agent 工具 model 參數；effort=medium |
| verify | opus | Agent 工具 model 參數；effort=medium |
| review | opus | Agent 工具 model 參數；effort=medium |

- 判讀批次 9；送出貼文 215 篇、圖片 12 張、正文約 74246 字
- 略過（已判讀未變動）112 篇；窗口外 27 篇
- 第二次審查：有（20 項）

## 來源

| 來源 | 狀態 | 範圍 | 說明 |
| --- | --- | --- | --- |
| threads:joe_huang_k_w | 部分 | 首屏 4 篇、累積 8 篇；最新 2026-11-19T18:10:09+08:00、最舊 2026-11-12T22:16:50+08:00；捲動 1 次、停止原因 reached-window；圖片下載 10 張 | 不變式通過；證據 /Users/eric/aiwork/taiwan-opera-calendar/patrol_evidence/2026-11-20_0311/threads_joe_huang… |
| threads:h.akito_1996 | 部分 | 首屏 5 篇、累積 14 篇；最新 2026-11-20T03:02:13+08:00、最舊 2026-09-27T00:04:33+08:00；捲動 5 次、停止原因 reached-window；圖片下載 11 張 | 不變式通過；證據 /Users/eric/aiwork/taiwan-opera-calendar/patrol_evidence/2026-11-20_0311/threads_h.akito_1… |
| threads:the_rin.lpm | 部分 | 首屏 4 篇、累積 7 篇；最新 2026-11-19T19:44:49+08:00、最舊 2026-09-26T14:32:03+08:00；捲動 1 次、停止原因 reached-window；圖片下載 31 張 | 不變式通過；證據 /Users/eric/aiwork/taiwan-opera-calendar/patrol_evidence/2026-11-20_0311/threads_the_rin.l… |
| threads:xuefeng_lu_ | 完整 | 7 天窗口讀完（停止原因 reached-window）；窗口內 4 篇皆有處置；圖片 1 張皆已判讀 | 不變式通過、逐篇處置完成 |
| threads:yuzhongluo | 部分 | 首屏 4 篇、累積 13 篇；最新 2026-11-20T00:06:19+08:00、最舊 2026-11-12T23:08:27+08:00；捲動 6 次、停止原因 reached-window；圖片下載 17 張 | 不變式通過；證據 /Users/eric/aiwork/taiwan-opera-calendar/patrol_evidence/2026-11-20_0311/threads_yuzhonglu… |
| threads:taiwaneseopera168 | 部分 | 首屏 4 篇、累積 22 篇；最新 2026-11-19T23:41:16+08:00、最舊 2026-08-16T02:33:12+08:00；捲動 10 次、停止原因 reached-window；圖片下載 19 張 | 不變式通過；證據 /Users/eric/aiwork/taiwan-opera-calendar/patrol_evidence/2026-11-20_0311/threads_taiwanese… |
| threads:jing__1017 | 部分 | 首屏 5 篇、累積 28 篇；最新 2026-11-20T01:09:03+08:00、最舊 2026-10-28T19:50:21+08:00；捲動 11 次、停止原因 reached-window；圖片下載 18 張 | 不變式通過；證據 /Users/eric/aiwork/taiwan-opera-calendar/patrol_evidence/2026-11-20_0311/threads_jing__101… |
| threads:hilang.on.tour | 完整 | 7 天窗口讀完（停止原因 reached-window）；窗口內 0 篇皆有處置；圖片 0 張皆已判讀 | 不變式通過、逐篇處置完成 |
| threads:yolin1991 | 部分 | 首屏 5 篇、累積 10 篇；最新 2026-11-19T18:33:15+08:00、最舊 2026-11-10T06:54:04+08:00；捲動 2 次、停止原因 reached-window；圖片下載 11 張 | 不變式通過；證據 /Users/eric/aiwork/taiwan-opera-calendar/patrol_evidence/2026-11-20_0311/threads_yolin1991… |
| threads:yilan_taiwan | 部分 | 首屏 4 篇、累積 18 篇；最新 2026-11-20T00:33:32+08:00、最舊 2026-11-13T00:56:05+08:00；捲動 9 次、停止原因 reached-window；圖片下載 19 張 | 不變式通過；證據 /Users/eric/aiwork/taiwan-opera-calendar/patrol_evidence/2026-11-20_0311/threads_yilan_tai… |
| facebook:sunhope.fans | 部分 | 首屏 1 篇、累積 20 篇；最新 無、最舊 無；捲動 20 次、停止原因 max-scrolls；圖片下載 36 張 | 不變式通過；證據 /Users/eric/aiwork/taiwan-opera-calendar/patrol_evidence/2026-11-20_0311/facebook_sunhope.… |
| facebook:HsiaoHsiYuan1913 | 部分 | 首屏 1 篇、累積 24 篇；最新 無、最舊 無；捲動 20 次、停止原因 max-scrolls；圖片下載 50 張 | 不變式通過；證據 /Users/eric/aiwork/taiwan-opera-calendar/patrol_evidence/2026-11-20_0311/facebook_HsiaoHsi… |
| facebook:100063868113954 | 部分 | 首屏 1 篇、累積 22 篇；最新 無、最舊 無；捲動 20 次、停止原因 max-scrolls；圖片下載 47 張 | 不變式通過；證據 /Users/eric/aiwork/taiwan-opera-calendar/patrol_evidence/2026-11-20_0311/facebook_10006386… |
| facebook:MingHuaYuanTianTaiwaneseOpera | 部分 | 首屏 1 篇、累積 21 篇；最新 無、最舊 無；捲動 20 次、停止原因 max-scrolls；圖片下載 56 張 | 不變式通過；證據 /Users/eric/aiwork/taiwan-opera-calendar/patrol_evidence/2026-11-20_0311/facebook_MingHuaY… |
| facebook:61574134933376 | 部分 | 首屏 1 篇、累積 18 篇；最新 無、最舊 無；捲動 20 次、停止原因 max-scrolls；圖片下載 46 張 | 不變式通過；證據 /Users/eric/aiwork/taiwan-opera-calendar/patrol_evidence/2026-11-20_0311/facebook_61574134… |
| facebook:mhysun | 部分 | 首屏 1 篇、累積 20 篇；最新 無、最舊 無；捲動 20 次、停止原因 max-scrolls；圖片下載 97 張 | 不變式通過；證據 /Users/eric/aiwork/taiwan-opera-calendar/patrol_evidence/2026-11-20_0311/facebook_mhysun.j… |
| facebook:61594936681482 | 部分 | 首屏 1 篇、累積 7 篇；最新 無、最舊 無；捲動 7 次、停止原因 no-new-after-3；圖片下載 23 張 | 不變式通過；證據 /Users/eric/aiwork/taiwan-opera-calendar/patrol_evidence/2026-11-20_0311/facebook_61594936… |
| facebook:lanyang.opera | 部分 | 首屏 1 篇、累積 22 篇；最新 無、最舊 無；捲動 20 次、停止原因 max-scrolls；圖片下載 37 張 | 不變式通過；證據 /Users/eric/aiwork/taiwan-opera-calendar/patrol_evidence/2026-11-20_0311/facebook_lanyang.… |
| facebook:Taichungpuppettheater | 部分 | 首屏 3 篇、累積 24 篇；最新 無、最舊 無；捲動 20 次、停止原因 max-scrolls；圖片下載 37 張 | 不變式通過；證據 /Users/eric/aiwork/taiwan-opera-calendar/patrol_evidence/2026-11-20_0311/facebook_Taichung… |
| culture | 部分 | total 501、fetchedAt 2026-11-15T10:19:38+08:00、戲曲紀錄 9 筆 | moc_records 已 113 小時未更新 |
| issues | 完整 | 3 筆皆有處置 | 逐筆處置完成 |

- OPENTIX：sitemap 835 個活動、本輪有變 663、抓取 250、戲曲相關且未過期 33、延後 413、錯誤 0

## 卡片變更

| 編號 | 動作 | 來源 | 內容 | 差異 | 審查 | 寫入 |
| --- | --- | --- | --- | --- | --- | --- |
| chg-001 | add | https://www.threads.com/@yuzhongluo/post/Dfy2Iecj_pR | 羅裕誴歌劇團｜《楊排風掛帥》｜大龍峒保安宮庭園廣場｜2026-11-20 正戲 19:00 |  | approve：原文「羅裕誴歌劇團《楊排風掛帥》 時間：115.11.20 [農曆10/12] (五)19:00 地點：大龍峒保安宮庭… | rejected artist-not-in-quote |
| chg-002 | add | https://www.threads.com/@taiwaneseopera168/post/Df1vFr_oF6y | 明華園黃字戲劇團｜《神仙孝子 • 劈山救母》｜台南市⛩️海尾朝皇宮｜2026-11-20 正戲 未公布 |  | needs-check：日期 11/20 與地點海尾朝皇宮有原文與海報佐證（海報另有地址：臺南市安南區海中街101巷10號，可補進 locat… | held  |
| chg-003 | add | https://www.threads.com/@jing__1017/post/Df7IaxPCXZ6 | 烏貓戲出｜《白賊七》粉絲見面會｜浸劇場（高雄市鼓山區裕豐里慶豐街 18 號 2 樓）｜2026-12-19 其他 14:30 |  | approve：原文「日期：2026 年 12 月 19 日（六） 時間：14:30 – 16:30」「地點：浸劇場（高雄市鼓山區裕豐… | rejected title-not-in-quote,artist-not-in-quote |
| chg-004 | add | https://www.threads.com/@jing__1017/post/Df7DKQDk45U | 未公布｜《楊宗保與穆桂英》｜基隆表演藝術中心演藝廳(基隆市信一路181號)｜2026-12-13 正戲 14:30 |  | reject：跟 chg-017 是同一場重複建卡：兩案都寫「《楊宗保與穆桂英》 115/12/13（日）14:30 基隆表演藝術中… | held  |
| chg-005 | add | https://www.threads.com/@yilan_taiwan/post/Df6uUXUH881 | 神童歌劇團｜《醉八仙》｜喜互惠慈安店停車場｜2026-11-21 正戲 17:30 |  | approve：原文「17:30-18:30，我們特別邀請到「神童歌劇團」 現場演出《醉八仙》」「📅 日期｜11/21（六）」「📍 地… | rejected duplicate |
| chg-006 | add | facebook:100063868113954:bd68cce81357 | 台北大龍峒和華樂社｜《周仁獻嫂》｜臺北市大同區保安里哈密街61號（大龍峒保安宮）｜2026-11-23 正戲 19:00 |  | needs-check：日期、時間、地點有原文支持：「台北大龍峒和華樂社-《周仁獻嫂》 演出時間：11/23 晚上7:00 演出住址：臺北市大… | held  |
| chg-007 | add | https://www.facebook.com/photo/?fbid=122315789156250015 | 小金枝歌劇團｜《棄老山傳奇》｜高雄中山堂劇場戶外陽光草坪｜2026-11-27 正戲 19:00 |  | approve：原文「11/27（五）小金枝歌劇團《棄老山傳奇》」「每場次開演時間｜19:00」「演出地點｜高雄中山堂劇場戶外陽光草坪… | rejected badgeType-not-free |
| chg-008 | add | https://www.facebook.com/photo/?fbid=122315789156250015 | 新和興總團｜《秦英掛帥》｜高雄中山堂劇場戶外陽光草坪｜2026-11-28 正戲 19:00 |  | approve：原文「11/28（六）新和興總團《秦英掛帥》」，統一 19:00、高雄中山堂劇場戶外陽光草坪、免費入場；2026/11… | rejected badgeType-not-free |
| chg-009 | add | https://www.facebook.com/photo/?fbid=122315789156250015 | 藝華園戲劇團｜《八仙傳奇－張果老與藍采和》｜高雄中山堂劇場戶外陽光草坪｜2026-11-29 正戲 19:00 |  | approve：原文「11/29（日）藝華園戲劇團《八仙傳奇－張果老與藍采和》」，統一 19:00、同地點、免費；星期一致。 | rejected badgeType-not-free |
| chg-010 | add | https://www.facebook.com/photo/?fbid=122315789156250015 | 新藝芳歌劇團｜《金蟾緣》｜高雄中山堂劇場戶外陽光草坪｜2026-12-03 正戲 19:00 |  | approve：原文「12/03（四）新藝芳歌劇團《金蟾緣》」，統一 19:00、同地點、免費；2026/12/03 是週四，一致。 | rejected badgeType-not-free |
| chg-011 | add | https://www.facebook.com/photo/?fbid=122315789156250015 | 佩儀歌劇團｜《吳漢殺妻》｜高雄中山堂劇場戶外陽光草坪｜2026-12-04 正戲 19:00 |  | approve：原文「12/04（五）佩儀歌劇團《吳漢殺妻》」，統一 19:00、同地點、免費；星期一致。 | rejected badgeType-not-free |
| chg-012 | add | https://www.facebook.com/photo/?fbid=122315789156250015 | 文惜歌仔戲劇團｜《焰火長槍：火帥與玉龍的背影》｜高雄中山堂劇場戶外陽光草坪｜2026-12-05 正戲 19:00 |  | approve：原文「12/05（六）文惜歌仔戲劇團《焰火長槍：火帥與玉龍的背影》」，統一 19:00、同地點、免費；星期一致。 | rejected badgeType-not-free |
| chg-013 | add | https://www.facebook.com/photo/?fbid=122315789156250015 | 繡花園戲劇團｜《姜子牙下山》｜高雄中山堂劇場戶外陽光草坪｜2026-12-06 正戲 19:00 |  | approve：原文「12/06（日）繡花園戲劇團《姜子牙下山》」，統一 19:00、同地點、免費；星期一致。 | rejected badgeType-not-free |
| chg-014 | add | https://www.facebook.com/photo/?fbid=122315789156250015 | 春明歌劇團｜《玉虛戰歌．天命之戰》｜高雄中山堂劇場戶外陽光草坪｜2026-12-11 正戲 19:00 |  | approve：原文「12/11（五）春明歌劇團《玉虛戰歌．天命之戰》」，統一 19:00、同地點、免費；星期一致。 | rejected badgeType-not-free |
| chg-015 | add | https://www.facebook.com/photo/?fbid=122315789156250015 | 水錦歌劇團｜《對面夫妻～韋馱與觀音》｜高雄中山堂劇場戶外陽光草坪｜2026-12-12 正戲 19:00 |  | approve：原文「12/12（六）水錦歌劇團《對面夫妻～韋馱與觀音》」，統一 19:00、同地點、免費；星期一致。 | rejected badgeType-not-free |
| chg-016 | add | https://www.facebook.com/photo/?fbid=122315789156250015 | 明華園星字戲劇團｜《斷案青天－陰錯陽差》｜高雄中山堂劇場戶外陽光草坪｜2026-12-13 正戲 19:00 |  | approve：原文「12/13（日）明華園星字戲劇團《斷案青天－陰錯陽差》」，統一 19:00、同地點、免費；星期一致。 | rejected badgeType-not-free |
| chg-017 | add | https://www.facebook.com/lanyang.opera/reels_tab | 蘭陽戲劇團｜《楊宗保與穆桂英》｜基隆表演藝術中心演藝廳(基隆市信一路181號)｜2026-12-13 正戲 14:30 |  | approve：蘭陽戲劇團官方原文「劇目：《楊宗保與穆桂英》 演出日期： 115/12/13（日）14:30（14:00開放入場） 演… | rejected badgeType-not-free |
| chg-018 | add | https://www.facebook.com/MingHuaYuanTianTaiwaneseOpera/reels_tab | 明華園天字戲劇團｜清雲寺外台演出｜屏東縣鹽埔鄉彭厝村清雲街1號｜2026-11-20 其他 未公布、2026-11-21 其他 未公布 |  | approve：原文「11/20（五）～11/21（六）｜農曆10/12~13 鹽埔清雲寺｜屏東縣鹽埔鄉彭厝村清雲街1號」，海報寫【清… | added  |
| chg-019 | add | https://www.facebook.com/MingHuaYuanTianTaiwaneseOpera/reels_tab | 明華園天字戲劇團｜琉球水仙宮外台演出｜屏東縣琉球鄉本福村中山路223號｜2026-11-20 其他 未公布、2026-11-21 其他 未公布 |  | approve：原文「琉球水仙宮｜屏東縣琉球鄉本福村中山路223號」，日期 11/20～11/21，海報同列【琉球水仙宮】115/11… | rejected duplicate |
| chg-020 | add（查證成立） | http://karensie.blogspot.com/2015/12/1041224.html（原貼文 https://www.opentix.life/event/2080109546140397568） | 一心戲劇團｜《閻王的假期》｜臺北市藝文推廣處城市舞台｜2026-12-05 正戲 14:30、2026-12-06 正戲 14:30 |  | approve：部落格售票彙整（115/11/07 更新）寫「12/05(六)-12/06(日)14:30 一心戲劇團 《閻王的假期》… | rejected badgeType-not-ticket |

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
| https://www.threads.com/@taiwaneseopera168/post/Df1HM9wEdDa | 烏貓戲出｜《白賊七》｜高雄中山堂劇場｜2027-04-17、2027-04-18 |
| https://www.threads.com/@taiwaneseopera168/post/Df1HM9wEdDa | 薪傳歌仔戲劇團｜《封神榜·文王食子》｜高雄中山堂劇場｜2027-04-24、2027-04-25 |

## 紀錄檔

- 本輪狀態：/Users/eric/aiwork/taiwan-opera-calendar/patrol_state/runs/2026-11-20_0311/state.json
- 巡檢紀錄：patrol_runs/2026-11-20_0311.json（/Users/eric/aiwork/taiwan-opera-calendar）
- 證據：patrol_evidence/2026-11-20_0311/
- 產生時間：2026-11-20T03:44:04+08:00
