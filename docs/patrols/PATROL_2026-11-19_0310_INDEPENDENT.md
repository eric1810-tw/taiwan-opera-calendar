# 巡檢報告 2026-11-19_0310（patrol-v2，正式）

## 結論

| 項目 | 結果 |
| --- | --- |
| 執行 | 開始 2026-11-19T03:10:53+08:00；結果 進行中；步驟 preflight:done、collect:done、pack:done、judge:done、check:done、verify:done、review:done、apply:done、publish:done、report:running |
| 來源 | 20 個：完整 3、部分 17、失敗 0、未讀 0 |
| 資料 | 送判讀 193 篇／圖 6 張；變更提案 22、確認一致 18、送查證 14（成立 1、與卡相同 3、查無佐證不收 10）、退回 0、漏處置 0；已過期不收 77、遠期暫存 8 |
| 寫入 | 寫入 2、add_card 拒絕 18、審查未通過 2 |
| 發布 | verified；SHA db55532f4b664aa9bcff9af2fc23e636e5a7a2dd；Actions 44383326317 |

## 模型與用量

| 角色 | 模型 | 依據 |
| --- | --- | --- |
| main | claude-sonnet-5-5 | get_session self：effort=medium |
| judge | sonnet | Agent 工具 model 參數；effort=medium |
| verify | opus | Agent 工具 model 參數；effort=medium |
| review | opus | Agent 工具 model 參數；effort=medium |

- 判讀批次 8；送出貼文 193 篇、圖片 6 張、正文約 66812 字
- 略過（已判讀未變動）93 篇；窗口外 28 篇
- 第二次審查：有（22 項）

## 來源

| 來源 | 狀態 | 範圍 | 說明 |
| --- | --- | --- | --- |
| threads:joe_huang_k_w | 部分 | 首屏 4 篇、累積 10 篇；最新 2026-11-18T11:44:39+08:00、最舊 2026-11-11T14:22:10+08:00；捲動 2 次、停止原因 reached-window；圖片下載 8 張 | 不變式通過；證據 /Users/eric/aiwork/taiwan-opera-calendar/patrol_evidence/2026-11-19_0310/threads_joe_huang… |
| threads:h.akito_1996 | 部分 | 首屏 4 篇、累積 13 篇；最新 2026-11-17T16:50:33+08:00、最舊 2026-09-27T00:04:33+08:00；捲動 4 次、停止原因 reached-window；圖片下載 10 張 | 不變式通過；證據 /Users/eric/aiwork/taiwan-opera-calendar/patrol_evidence/2026-11-19_0310/threads_h.akito_1… |
| threads:the_rin.lpm | 部分 | 首屏 4 篇、累積 8 篇；最新 2026-11-18T19:57:19+08:00、最舊 2026-09-26T14:32:03+08:00；捲動 2 次、停止原因 reached-window；圖片下載 13 張 | 不變式通過；證據 /Users/eric/aiwork/taiwan-opera-calendar/patrol_evidence/2026-11-19_0310/threads_the_rin.l… |
| threads:xuefeng_lu_ | 完整 | 7 天窗口讀完（停止原因 reached-window）；窗口內 3 篇皆有處置；圖片 0 張皆已判讀 | 不變式通過、逐篇處置完成 |
| threads:yuzhongluo | 部分 | 首屏 3 篇、累積 12 篇；最新 2026-11-18T14:22:01+08:00、最舊 2026-11-12T01:15:03+08:00；捲動 5 次、停止原因 reached-window；圖片下載 16 張 | 不變式通過；證據 /Users/eric/aiwork/taiwan-opera-calendar/patrol_evidence/2026-11-19_0310/threads_yuzhonglu… |
| threads:taiwaneseopera168 | 部分 | 首屏 5 篇、累積 10 篇；最新 2026-11-18T21:45:56+08:00、最舊 2026-08-16T02:33:12+08:00；捲動 2 次、停止原因 reached-window；圖片下載 8 張 | 不變式通過；證據 /Users/eric/aiwork/taiwan-opera-calendar/patrol_evidence/2026-11-19_0310/threads_taiwanese… |
| threads:jing__1017 | 部分 | 首屏 4 篇、累積 27 篇；最新 2026-11-18T22:42:33+08:00、最舊 2026-10-28T19:50:21+08:00；捲動 11 次、停止原因 reached-window；圖片下載 18 張 | 不變式通過；證據 /Users/eric/aiwork/taiwan-opera-calendar/patrol_evidence/2026-11-19_0310/threads_jing__101… |
| threads:hilang.on.tour | 完整 | 7 天窗口讀完（停止原因 reached-window）；窗口內 0 篇皆有處置；圖片 0 張皆已判讀 | 不變式通過、逐篇處置完成 |
| threads:yolin1991 | 部分 | 首屏 4 篇、累積 7 篇；最新 2026-11-18T16:11:34+08:00、最舊 2026-11-11T11:21:57+08:00；捲動 1 次、停止原因 reached-window；圖片下載 9 張 | 不變式通過；證據 /Users/eric/aiwork/taiwan-opera-calendar/patrol_evidence/2026-11-19_0310/threads_yolin1991… |
| facebook:sunhope.fans | 部分 | 首屏 1 篇、累積 21 篇；最新 無、最舊 無；捲動 20 次、停止原因 max-scrolls；圖片下載 46 張 | 不變式通過；證據 /Users/eric/aiwork/taiwan-opera-calendar/patrol_evidence/2026-11-19_0310/facebook_sunhope.… |
| facebook:HsiaoHsiYuan1913 | 部分 | 首屏 1 篇、累積 24 篇；最新 無、最舊 無；捲動 20 次、停止原因 max-scrolls；圖片下載 50 張 | 不變式通過；證據 /Users/eric/aiwork/taiwan-opera-calendar/patrol_evidence/2026-11-19_0310/facebook_HsiaoHsi… |
| facebook:100063868113954 | 部分 | 首屏 3 篇、累積 21 篇；最新 無、最舊 無；捲動 20 次、停止原因 max-scrolls；圖片下載 36 張 | 不變式通過；證據 /Users/eric/aiwork/taiwan-opera-calendar/patrol_evidence/2026-11-19_0310/facebook_10006386… |
| facebook:MingHuaYuanTianTaiwaneseOpera | 部分 | 首屏 1 篇、累積 22 篇；最新 無、最舊 無；捲動 20 次、停止原因 max-scrolls；圖片下載 61 張 | 不變式通過；證據 /Users/eric/aiwork/taiwan-opera-calendar/patrol_evidence/2026-11-19_0310/facebook_MingHuaY… |
| facebook:61574134933376 | 部分 | 首屏 3 篇、累積 7 篇；最新 無、最舊 無；捲動 7 次、停止原因 no-new-after-3；圖片下載 8 張 | 不變式通過；證據 /Users/eric/aiwork/taiwan-opera-calendar/patrol_evidence/2026-11-19_0310/facebook_61574134… |
| facebook:mhysun | 部分 | 首屏 1 篇、累積 20 篇；最新 無、最舊 無；捲動 20 次、停止原因 max-scrolls；圖片下載 92 張 | 不變式通過；證據 /Users/eric/aiwork/taiwan-opera-calendar/patrol_evidence/2026-11-19_0310/facebook_mhysun.j… |
| facebook:61594936681482 | 部分 | 首屏 1 篇、累積 7 篇；最新 無、最舊 無；捲動 7 次、停止原因 no-new-after-3；圖片下載 23 張 | 不變式通過；證據 /Users/eric/aiwork/taiwan-opera-calendar/patrol_evidence/2026-11-19_0310/facebook_61594936… |
| facebook:lanyang.opera | 部分 | 首屏 1 篇、累積 22 篇；最新 無、最舊 無；捲動 20 次、停止原因 max-scrolls；圖片下載 38 張 | 不變式通過；證據 /Users/eric/aiwork/taiwan-opera-calendar/patrol_evidence/2026-11-19_0310/facebook_lanyang.… |
| facebook:Taichungpuppettheater | 部分 | 首屏 3 篇、累積 26 篇；最新 無、最舊 無；捲動 20 次、停止原因 max-scrolls；圖片下載 34 張 | 不變式通過；證據 /Users/eric/aiwork/taiwan-opera-calendar/patrol_evidence/2026-11-19_0310/facebook_Taichung… |
| culture | 部分 | total 501、fetchedAt 2026-11-15T10:19:38+08:00、戲曲紀錄 9 筆 | moc_records 已 89 小時未更新 |
| issues | 完整 | 3 筆皆有處置 | 逐筆處置完成 |

- OPENTIX：sitemap 824 個活動、本輪有變 663、抓取 250、戲曲相關且未過期 33、延後 413、錯誤 0

## 卡片變更

| 編號 | 動作 | 來源 | 內容 | 差異 | 審查 | 寫入 |
| --- | --- | --- | --- | --- | --- | --- |
| chg-001 | add | https://www.threads.com/@yuzhongluo/post/Dfy2Iecj_pR | 羅裕誴歌劇團｜《楊排風掛帥》｜大龍峒保安宮庭園廣場｜2026-11-20 正戲 19:00 |  | approve：原文「羅裕誴歌劇團《楊排風掛帥》 時間：115.11.20 [農曆10/12] (五)19:00 地點：大龍峒保安宮庭… | rejected artist-not-in-quote |
| chg-002 | add | https://www.threads.com/@jing__1017/post/Df4vuiMk8nL | 明華園天字戲劇團｜無極慈母宮外台演出｜高雄路竹無極慈母宮｜2026-11-29 扮仙 15:00、2026-11-29 正戲 19:00、2026-11-30 扮仙 15:00、2026-11-30 正戲 19:00、2026-12-01… |  | approve：原文「國曆11月29～12月03日(星期日至四) 共演出5天」「下午3:00辦仙賀壽」「晚上7:00準時開演」，扮仙與… | added  |
| chg-003 | add | https://www.facebook.com/photo/?fbid=122315789156250015 | 小金枝歌劇團｜《棄老山傳奇》｜高雄中山堂劇場戶外陽光草坪｜2026-11-27 正戲 19:00 |  | approve：原文「11/27（五）小金枝歌劇團《棄老山傳奇》」「每場次開演時間｜19:00」「演出地點｜高雄中山堂劇場戶外陽光草坪… | rejected badgeType-not-free |
| chg-004 | add | https://www.facebook.com/photo/?fbid=122315789156250015 | 新和興總團｜《秦英掛帥》｜高雄中山堂劇場戶外陽光草坪｜2026-11-28 正戲 19:00 |  | approve：原文「11/28（六）新和興總團《秦英掛帥》」，共用 19:00 與高雄中山堂戶外陽光草坪、免費入場；2026-11-… | rejected badgeType-not-free |
| chg-005 | add | https://www.facebook.com/photo/?fbid=122315789156250015 | 藝華園戲劇團｜《八仙傳奇－張果老與藍采和》｜高雄中山堂劇場戶外陽光草坪｜2026-11-29 正戲 19:00 |  | approve：原文「11/29（日）藝華園戲劇團《八仙傳奇－張果老與藍采和》」，19:00、高雄中山堂戶外陽光草坪、免費；2026-… | rejected badgeType-not-free |
| chg-006 | add | https://www.facebook.com/photo/?fbid=122315789156250015 | 新藝芳歌劇團｜《金蟾緣》｜高雄中山堂劇場戶外陽光草坪｜2026-12-03 正戲 19:00 |  | approve：原文「12/03（四）新藝芳歌劇團《金蟾緣》」，19:00、高雄中山堂戶外陽光草坪、免費；2026-12-03 為週四… | rejected badgeType-not-free |
| chg-007 | add | https://www.facebook.com/photo/?fbid=122315789156250015 | 佩儀歌劇團｜《吳漢殺妻》｜高雄中山堂劇場戶外陽光草坪｜2026-12-04 正戲 19:00 |  | approve：原文「12/04（五）佩儀歌劇團《吳漢殺妻》」，19:00、高雄中山堂戶外陽光草坪、免費；2026-12-04 為週五… | rejected badgeType-not-free |
| chg-008 | add | https://www.facebook.com/photo/?fbid=122315789156250015 | 文惜歌仔戲劇團｜《焰火長槍：火帥與玉龍的背影》｜高雄中山堂劇場戶外陽光草坪｜2026-12-05 正戲 19:00 |  | approve：原文「12/05（六）文惜歌仔戲劇團《焰火長槍：火帥與玉龍的背影》」，19:00、高雄中山堂戶外陽光草坪、免費；202… | rejected badgeType-not-free |
| chg-009 | add | https://www.facebook.com/photo/?fbid=122315789156250015 | 繡花園戲劇團｜《姜子牙下山》｜高雄中山堂劇場戶外陽光草坪｜2026-12-06 正戲 19:00 |  | approve：原文「12/06（日）繡花園戲劇團《姜子牙下山》」，19:00、高雄中山堂戶外陽光草坪、免費；2026-12-06 為… | rejected badgeType-not-free |
| chg-010 | add | https://www.facebook.com/photo/?fbid=122315789156250015 | 春明歌劇團｜《玉虛戰歌．天命之戰》｜高雄中山堂劇場戶外陽光草坪｜2026-12-11 正戲 19:00 |  | approve：原文「12/11（五）春明歌劇團《玉虛戰歌．天命之戰》」，19:00、高雄中山堂戶外陽光草坪、免費；2026-12-1… | rejected badgeType-not-free |
| chg-011 | add | https://www.facebook.com/photo/?fbid=122315789156250015 | 水錦歌劇團｜《對面夫妻～韋馱與觀音》｜高雄中山堂劇場戶外陽光草坪｜2026-12-12 正戲 19:00 |  | approve：原文「12/12（六）水錦歌劇團《對面夫妻～韋馱與觀音》」，19:00、高雄中山堂戶外陽光草坪、免費；2026-12-… | rejected badgeType-not-free |
| chg-012 | add | https://www.facebook.com/photo/?fbid=122315789156250015 | 明華園星字戲劇團｜《斷案青天－陰錯陽差》｜高雄中山堂劇場戶外陽光草坪｜2026-12-13 正戲 19:00 |  | approve：原文「12/13（日）明華園星字戲劇團《斷案青天－陰錯陽差》」，19:00、高雄中山堂戶外陽光草坪、免費；2026-1… | rejected badgeType-not-free |
| chg-013 | add | https://www.facebook.com/lanyang.opera/reels_tab | 蘭陽戲劇團｜《春草》｜國立臺北科技大學 學生活動中心｜2026-12-10 正戲 14:00 |  | approve：原文「劇目｜《春草》」「日期｜115 年 12 月 10 日（四）」「時間｜14:00 演出（13:30 開放入場）」… | added  |
| chg-014 | add | https://www.threads.com/@yuzhongluo/post/Df32dWaE1iy | 羅裕諒歌劇團｜《楊排風掛帥》｜臺北市大龍峒保安宮｜2026-11-20 正戲 19:00 |  | reject：與 chg-001 為同一場（同為 yuzhongluo 帳號、《楊排風掛帥》11/20 19:00 大龍峒保安宮），… | held  |
| chg-015 | add | https://www.facebook.com/dadaochen2011/posts/pfbid0k6ATPcTLidUcVjHMT7c6m643SjVMZTyhqJRhWr8mnWF6Zo9figpwHGkacBHa1uSxl | 羅裕諒歌劇團｜《楊排風掛帥》｜大龍峒保安宮庭園廣場｜2026-11-20 正戲 19:00 |  | reject：與 chg-001 為同一場（大稻埕戲苑一覽表「11/20(五) 羅裕誴歌劇團《楊排風掛帥》」），重複建卡；troup… | held  |
| chg-016 | add | https://www.facebook.com/dadaochen2011/posts/pfbid0k6ATPcTLidUcVjHMT7c6m643SjVMZTyhqJRhWr8mnWF6Zo9figpwHGkacBHa1uSxl | 小飛霞歌劇團｜《情義—七爺八爺》｜大龍峒保安宮庭園廣場｜2026-11-21 正戲 19:00 |  | approve：一覽表圖片「11/21(六) 小飛霞歌劇團《情義—七爺八爺》」，在「大龍峒保安宮庭園廣場」區塊下；標題「每晚7點好戲開… | rejected badgeType-not-free |
| chg-017 | add | https://www.facebook.com/dadaochen2011/posts/pfbid0k6ATPcTLidUcVjHMT7c6m643SjVMZTyhqJRhWr8mnWF6Zo9figpwHGkacBHa1uSxl | 鴻明歌劇團｜《劈天》｜大龍峒保安宮庭園廣場｜2026-11-22 正戲 19:00 |  | approve：一覽表圖片「11/22(日) 鴻明歌劇團《劈天》」，大龍峒保安宮庭園廣場區塊、19:00、免費入座；2026-11-2… | rejected badgeType-not-free |
| chg-018 | add | https://www.facebook.com/dadaochen2011/posts/pfbid0k6ATPcTLidUcVjHMT7c6m643SjVMZTyhqJRhWr8mnWF6Zo9figpwHGkacBHa1uSxl | 台北市和華樂社｜《周仁獻嫂》｜大龍峒保安宮庭園廣場｜2026-11-23 正戲 19:00 |  | approve：一覽表圖片「11/23(一) 台北市和華樂社《周仁獻嫂》」，大龍峒保安宮庭園廣場區塊、19:00、免費入座；2026-… | rejected badgeType-not-free |
| chg-019 | add | https://www.facebook.com/dadaochen2011/posts/pfbid0k6ATPcTLidUcVjHMT7c6m643SjVMZTyhqJRhWr8mnWF6Zo9figpwHGkacBHa1uSxl | 明華園玄字戲劇團｜《西遊記．大鬧天宮》｜大龍峒保安宮庭園廣場｜2026-11-24 正戲 19:00 |  | approve：一覽表圖片「11/24(二) 明華園玄字戲劇團《西遊記．大鬧天宮》」，大龍峒保安宮庭園廣場區塊、19:00、免費入座；… | rejected badgeType-not-free |
| chg-020 | add | https://www.facebook.com/dadaochen2011/posts/pfbid0k6ATPcTLidUcVjHMT7c6m643SjVMZTyhqJRhWr8mnWF6Zo9figpwHGkacBHa1uSxl | 國立臺灣戲曲學院｜《熱天的戀夢》｜大龍峒保安宮庭園廣場｜2026-11-26 正戲 19:00 |  | approve：一覽表圖片「11/26(四) 國立臺灣戲曲學院《熱天的戀夢》」，大龍峒保安宮庭園廣場區塊、19:00、免費入座；202… | rejected badgeType-not-free |
| chg-021 | add | https://www.facebook.com/dadaochen2011/posts/pfbid0k6ATPcTLidUcVjHMT7c6m643SjVMZTyhqJRhWr8mnWF6Zo9figpwHGkacBHa1uSxl | 葉麗珠三姊妹歌劇團｜《斬鄭英》｜松山車站南側交4廣場｜2026-11-27 正戲 19:00 |  | approve：一覽表圖片「11/27(五) 葉麗珠三姊妹歌劇團《斬鄭英》」，位於「松山車站南側交4廣場」區塊（原文亦寫 11/27–… | rejected badgeType-not-free |
| chg-022 | add（查證成立） | https://www.tw-yishin.com/%e6%bc%94%e5%87%ba%e6%96%b0%e8%a8%8a/2026%e4%b8%80%e5%bf%83%e6%88%b2%e5%8a%87%e5%9c%98%e3%80%8a%e9%96%bb%e7%8e%8b%e7%9a%84%e5%81%87%e6%9c%9f%e3%80%8b/（原貼文 https://www.opentix.life/event/2080109546140397568） | 一心戲劇團｜《閻王的假期》｜臺北市藝文推廣處城市舞台（臺北市松山區八德路三段25號）｜2026-12-05 正戲 14:30、2026-12-06 正戲 14:30 |  | approve：一心戲劇團官網原文「演出時間：2026/12/05(六)14:30 2026/12/06(日)14:30」「票價：30… | rejected location-not-in-quote |

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

- 本輪狀態：/Users/eric/aiwork/taiwan-opera-calendar/patrol_state/runs/2026-11-19_0310/state.json
- 巡檢紀錄：patrol_runs/2026-11-19_0310.json（/Users/eric/aiwork/taiwan-opera-calendar）
- 證據：patrol_evidence/2026-11-19_0310/
- 產生時間：2026-11-19T03:45:02+08:00
