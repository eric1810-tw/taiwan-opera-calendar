# 巡檢報告 2026-11-25_0311（patrol-v2，正式）

## 結論

| 項目 | 結果 |
| --- | --- |
| 執行 | 開始 2026-11-25T03:11:09+08:00；結果 進行中；步驟 preflight:done、collect:done、pack:done、judge:done、check:done、verify:done、review:done、apply:done、publish:done、report:running |
| 來源 | 21 個：完整 6、部分 15、失敗 0、未讀 0 |
| 資料 | 送判讀 70 篇／圖 4 張；變更提案 5、確認一致 13、送查證 12（成立 2、與卡相同 0、查無佐證不收 10）、退回 0、漏處置 0；已過期不收 10、遠期暫存 31 |
| 寫入 | 寫入 2、add_card 拒絕 1、審查未通過 2 |
| 發布 | verified；SHA 524bb4e53cf0092d50617402d115b6b135274037；Actions 45470768300 |

## 模型與用量

| 角色 | 模型 | 依據 |
| --- | --- | --- |
| main | claude-sonnet-5-5 | get_session self：effort=medium |
| judge | sonnet | Agent 工具 model 參數；effort=medium |
| verify | opus | Agent 工具 model 參數；effort=medium |
| review | opus | Agent 工具 model 參數；effort=medium |

- 判讀批次 3；送出貼文 70 篇、圖片 4 張、正文約 13898 字
- 略過（已判讀未變動）48 篇；窗口外 76 篇
- 第二次審查：有（5 項）

## 來源

| 來源 | 狀態 | 範圍 | 說明 |
| --- | --- | --- | --- |
| threads:joe_huang_k_w | 部分 | 首屏 4 篇、累積 16 篇；最新 2026-11-23T00:01:53+08:00、最舊 2026-11-07T16:49:05+08:00；捲動 1 次、停止原因 reached-window；圖片下載 24 張 | 不變式通過；證據 /Users/eric/aiwork/taiwan-opera-calendar/patrol_evidence/2026-11-25_0311/threads_joe_huang… |
| threads:h.akito_1996 | 部分 | 首屏 8 篇、累積 8 篇；最新 2026-11-24T15:32:35+08:00、最舊 2026-09-27T00:04:33+08:00；捲動 3 次、停止原因 no-new-after-3；圖片下載 16 張 | 不變式通過；證據 /Users/eric/aiwork/taiwan-opera-calendar/patrol_evidence/2026-11-25_0311/threads_h.akito_1… |
| threads:the_rin.lpm | 部分 | 首屏 5 篇、累積 5 篇；最新 2026-11-24T19:29:45+08:00、最舊 2026-10-01T22:31:26+08:00；捲動 3 次、停止原因 no-new-after-3；圖片下載 15 張 | 不變式通過；證據 /Users/eric/aiwork/taiwan-opera-calendar/patrol_evidence/2026-11-25_0311/threads_the_rin.l… |
| threads:xuefeng_lu_ | 完整 | 7 天窗口讀完（停止原因 reached-window）；窗口內 2 篇皆有處置；圖片 1 張皆已判讀 | 不變式通過、逐篇處置完成 |
| threads:yuzhongluo | 部分 | 首屏 4 篇、累積 4 篇；最新 2026-11-24T07:21:33+08:00、最舊 2026-11-24T02:32:23+08:00；捲動 3 次、停止原因 no-new-after-3；圖片下載 4 張 | 不變式通過；證據 /Users/eric/aiwork/taiwan-opera-calendar/patrol_evidence/2026-11-25_0311/threads_yuzhonglu… |
| threads:taiwaneseopera168 | 部分 | 首屏 5 篇、累積 5 篇；最新 2026-11-24T22:34:19+08:00、最舊 2026-08-16T02:33:12+08:00；捲動 3 次、停止原因 no-new-after-3；圖片下載 3 張 | 不變式通過；證據 /Users/eric/aiwork/taiwan-opera-calendar/patrol_evidence/2026-11-25_0311/threads_taiwanese… |
| threads:jing__1017 | 部分 | 首屏 7 篇、累積 7 篇；最新 2026-11-24T23:31:44+08:00、最舊 2026-10-28T19:50:21+08:00；捲動 3 次、停止原因 no-new-after-3；圖片下載 8 張 | 不變式通過；證據 /Users/eric/aiwork/taiwan-opera-calendar/patrol_evidence/2026-11-25_0311/threads_jing__101… |
| threads:hilang.on.tour | 完整 | 7 天窗口讀完（停止原因 reached-window）；窗口內 0 篇皆有處置；圖片 0 張皆已判讀 | 不變式通過、逐篇處置完成 |
| threads:yolin1991 | 部分 | 首屏 5 篇、累積 5 篇；最新 2026-11-23T21:38:13+08:00、最舊 2026-11-21T11:25:14+08:00；捲動 3 次、停止原因 no-new-after-3；圖片下載 4 張 | 不變式通過；證據 /Users/eric/aiwork/taiwan-opera-calendar/patrol_evidence/2026-11-25_0311/threads_yolin1991… |
| threads:yilan_taiwan | 部分 | 首屏 4 篇、累積 4 篇；最新 2026-11-22T11:14:10+08:00、最舊 2026-11-20T16:13:13+08:00；捲動 3 次、停止原因 no-new-after-3；圖片下載 6 張 | 不變式通過；證據 /Users/eric/aiwork/taiwan-opera-calendar/patrol_evidence/2026-11-25_0311/threads_yilan_tai… |
| facebook:sunhope.fans | 部分 | 首屏 1 篇、累積 9 篇；最新 2026-11-24T03:12:39+08:00、最舊 2026-11-03T19:16:00+08:00；捲動 1 次、停止原因 reached-window；圖片下載 29 張 | 不變式通過；證據 /Users/eric/aiwork/taiwan-opera-calendar/patrol_evidence/2026-11-25_0311/facebook_sunhope.… |
| facebook:HsiaoHsiYuan1913 | 部分 | 首屏 3 篇、累積 11 篇；最新 2026-05-07T12:00:00+08:00、最舊 2026-05-07T12:00:00+08:00；捲動 1 次、停止原因 reached-window；圖片下載 18 張 | 不變式通過；證據 /Users/eric/aiwork/taiwan-opera-calendar/patrol_evidence/2026-11-25_0311/facebook_HsiaoHsi… |
| facebook:100063868113954 | 部分 | 首屏 2 篇、累積 13 篇；最新 2026-11-23T03:13:00+08:00、最舊 2026-11-06T19:57:00+08:00；捲動 2 次、停止原因 reached-window；圖片下載 17 張 | 不變式通過；證據 /Users/eric/aiwork/taiwan-opera-calendar/patrol_evidence/2026-11-25_0311/facebook_10006386… |
| facebook:MingHuaYuanTianTaiwaneseOpera | 完整 | 7 天窗口讀完（停止原因 reached-window）；窗口內 4 篇皆有處置；圖片 3 張皆已判讀 | 不變式通過、逐篇處置完成 |
| facebook:61574134933376 | 部分 | 首屏 3 篇、累積 8 篇；最新 2026-11-23T03:13:24+08:00、最舊 2026-10-23T12:00:00+08:00；捲動 1 次、停止原因 reached-window；圖片下載 11 張 | 不變式通過；證據 /Users/eric/aiwork/taiwan-opera-calendar/patrol_evidence/2026-11-25_0311/facebook_61574134… |
| facebook:mhysun | 部分 | 首屏 3 篇、累積 11 篇；最新 2026-11-23T03:13:34+08:00、最舊 2026-10-31T23:10:00+08:00；捲動 1 次、停止原因 reached-window；圖片下載 50 張 | 不變式通過；證據 /Users/eric/aiwork/taiwan-opera-calendar/patrol_evidence/2026-11-25_0311/facebook_mhysun.j… |
| facebook:61594936681482 | 完整 | 7 天窗口讀完（停止原因 reached-window）；窗口內 0 篇皆有處置；圖片 0 張皆已判讀 | 不變式通過、逐篇處置完成 |
| facebook:lanyang.opera | 部分 | 首屏 3 篇、累積 11 篇；最新 2026-11-24T03:13:55+08:00、最舊 2026-09-22T12:00:00+08:00；捲動 1 次、停止原因 reached-window；圖片下載 15 張 | 不變式通過；證據 /Users/eric/aiwork/taiwan-opera-calendar/patrol_evidence/2026-11-25_0311/facebook_lanyang.… |
| facebook:Taichungpuppettheater | 完整 | 7 天窗口讀完（停止原因 reached-window）；窗口內 1 篇皆有處置；圖片 5 張皆已判讀 | 不變式通過、逐篇處置完成 |
| culture | 部分 | total 503、fetchedAt 2026-11-22T10:46:46+08:00、戲曲紀錄 9 筆 | moc_records 已 64 小時未更新 |
| issues | 完整 | 3 筆皆有處置 | 逐筆處置完成 |

- OPENTIX：sitemap 814 個活動、本輪有變 638、抓取 250、戲曲相關且未過期 30、延後 388、錯誤 0

## 卡片變更

| 編號 | 動作 | 來源 | 內容 | 差異 | 審查 | 寫入 |
| --- | --- | --- | --- | --- | --- | --- |
| chg-001 | add | https://www.threads.com/@yuzhongluo/post/DgGjHE2j9ob | 文惜歌仔戲劇團｜《焰火長槍：火帥與玉龍的背影》｜左營中山堂｜2026-12-05 正戲 未公布 |  | approve：troupe、title、date、location 皆出自 source.text「文惜歌仔戲劇團 為妳精心呈現~~… | added  |
| chg-002 | add | https://www.threads.com/@yuzhongluo/post/DgGgrdpD5Ff | 陳昭瑋歌劇團｜威靈堂外台演出｜小琉球井仔口威靈堂 屏東縣琉球鄉南福村忠孝路32號｜2026-11-25 扮仙 14:30、2026-11-25 正戲 19:00、2026-11-26 扮仙 14:30、2026-11-26 正戲 19:00 |  | needs-check：日期、時間、地點經目視海報確認無誤：11/25-26 連演2日（農曆10月17至18日），「午戲 14:30開演(扮仙… | held  |
| chg-003 | add | https://www.threads.com/@yolin1991/post/DgEWdsTGi0g | 新吉義林歌劇團｜鹽水外台演出｜鹽水｜2026-11-26 正戲 未公布、2026-11-27 正戲 未公布 |  | approve：source.text「11/26（四）.11/27（五） 新吉義林歌劇團在鹽水演出2天」與 sessions 兩天、… | added  |
| chg-004 | change（查證成立） | https://kinotw.com/show/moc-6aaacec826b324165c32e41c-dba40c9c（原貼文 https://www.opentix.life/event/2099337927309197313） | 烏貓戲出｜《燈殼樓的委託-小戲蟲拜先生》｜大稻埕戲苑曲藝場（臺北市大同區迪化街一段21號8樓）｜2026-11-28 正戲 11:00、2026-11-28 正戲 14:30、2026-11-29 正戲 11:00、2026-12-12 … |  | reject：proposed.sessions 只有 7 筆，少了 2026-11-29 14:30 正戲。原文明寫「未來場次 8… | held  |
| chg-005 | add（查證成立） | https://www.tw-yishin.com/%E6%BC%94%E5%87%BA%E6%96%B0%E8%A8%8A/2026%E4%B8%80%E5%BF%83%E6%88%B2%E5%8A%87%E5%9C%98%E3%80%8A%E9%96%BB%E7%8E%8B%E7%9A%84%E5%81%87%E6%9C%9F%E3%80%8B/（原貼文 https://www.opentix.life/event/2080109546140397568） | 一心戲劇團｜《閻王的假期》｜臺北市藝文推廣處城市舞台（臺北市松山區八德路三段25號）｜2026-12-05 正戲 14:30、2026-12-06 正戲 14:30 |  | approve：劇團官網原文「2026一心戲劇團《閻王的假期》◎ 演出時間：2026/12/05(六)14:30 2026/12/06… | rejected location-not-in-quote,artist-not-in-quote |

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
| https://www.threads.com/@yuzhongluo/post/DgGCMHkEl8q | 薪傳歌仔戲劇團｜《陳世美-反奸》開鑼式｜保安宮庭園（台北市大同區哈密街61號）｜2027-04-11 |
| https://www.threads.com/@yuzhongluo/post/DgGCMHkEl8q | 春明歌劇團｜《五毒亂唐-大聖降魔》｜保安宮庭園（台北市大同區哈密街61號）｜2027-04-12 |
| https://www.threads.com/@yuzhongluo/post/DgGCMHkEl8q | 羅裕誴歌劇團｜《滄海神醫》｜保安宮庭園（台北市大同區哈密街61號）｜2027-04-13 |
| https://www.threads.com/@yuzhongluo/post/DgGCMHkEl8q | 秀琴歌劇團｜《林投姐》｜保安宮庭園（台北市大同區哈密街61號）｜2027-04-14 |
| https://www.threads.com/@yuzhongluo/post/DgGCMHkEl8q | 秀琴歌劇團｜《盤絲洞》｜保安宮庭園（台北市大同區哈密街61號）｜2027-04-15 |
| https://www.threads.com/@yuzhongluo/post/DgGCMHkEl8q | 孫凱琳歌劇團｜恨鎖天倫夢｜保安宮庭園（台北市大同區哈密街61號）｜2027-04-16 |
| https://www.threads.com/@yuzhongluo/post/DgGCMHkEl8q | 孫凱琳歌劇團｜情渡千年｜保安宮庭園（台北市大同區哈密街61號）｜2027-04-17 |
| https://www.threads.com/@yuzhongluo/post/DgGCMHkEl8q | 民安歌劇團｜包公審烏盆｜保安宮庭園（台北市大同區哈密街61號）｜2027-04-18 |
| https://www.threads.com/@yuzhongluo/post/DgGCMHkEl8q | 鴻明歌劇團｜一文錢｜保安宮庭園（台北市大同區哈密街61號）｜2027-04-19 |
| https://www.threads.com/@yuzhongluo/post/DgGCMHkEl8q | 國立臺灣戲曲學院歌仔戲學系高職部｜《魚美人》｜保安宮庭園（台北市大同區哈密街61號）｜2027-04-21 |
| https://www.threads.com/@yuzhongluo/post/DgGCMHkEl8q | 國立臺灣戲曲學院歌仔戲學系學院部｜《鐵面情》｜保安宮庭園（台北市大同區哈密街61號）｜2027-04-22 |
| https://www.threads.com/@yuzhongluo/post/DgGCMHkEl8q | 小金枝歌劇團｜一念恩仇｜保安宮庭園（台北市大同區哈密街61號）｜2027-04-23 |
| https://www.threads.com/@yuzhongluo/post/DgGCMHkEl8q | 唐美雲歌仔戲團青年團｜哪吒傳｜保安宮庭園（台北市大同區哈密街61號）｜2027-04-24 |
| https://www.threads.com/@yuzhongluo/post/DgGCMHkEl8q | 明華園玄字戲劇團｜三打白骨精｜保安宮庭園（台北市大同區哈密街61號）｜2027-04-26 |
| https://www.threads.com/@yuzhongluo/post/DgGCMHkEl8q | 蘭陽戲劇團｜福氣臨門｜保安宮庭園（台北市大同區哈密街61號）｜2027-04-28 |
| https://www.threads.com/@yuzhongluo/post/DgGCMHkEl8q | 保安宮杏壇歌仔戲社｜宋宮秘史｜保安宮庭園（台北市大同區哈密街61號）｜2027-04-29 |
| https://www.threads.com/@yuzhongluo/post/DgGCMHkEl8q | 臺北市永樂國小歌仔戲劇團｜義女情｜保安宮庭園（台北市大同區哈密街61號）｜2027-04-30 |
| https://www.threads.com/@yuzhongluo/post/DgGCMHkEl8q | 文惜歌仔戲劇團｜《龍鳳餅》｜保安宮庭園（台北市大同區哈密街61號）｜2027-05-01 |
| https://www.threads.com/@yuzhongluo/post/DgGCMHkEl8q | 陳麗香歌仔戲團｜雙遊庵｜保安宮庭園（台北市大同區哈密街61號）｜2027-05-02 |
| https://www.threads.com/@yuzhongluo/post/DgGCMHkEl8q | 一心戲劇團｜《刺客列傳魚腸劍》｜保安宮庭園（台北市大同區哈密街61號）｜2027-05-03 |
| https://www.threads.com/@yuzhongluo/post/DgGCMHkEl8q | 李靜芳歌仔戲團｜穆桂英破洪州(祭祀公業吳家記酬神戲)｜保安宮庭園（台北市大同區哈密街61號）｜2027-05-04 |
| https://www.threads.com/@yuzhongluo/post/DgGCBBfD3VQ | 羅裕誴歌劇團｜《滄海神醫》｜保安宮庭園（台北市大同區哈密街61號）｜2027-04-13 |
| https://www.threads.com/@yuzhongluo/post/DgGCBBfD3VQ | 文惜歌仔戲劇團｜《龍鳳餅》｜保安宮庭園（台北市大同區哈密街61號）｜2027-05-01 |

## 紀錄檔

- 本輪狀態：/Users/eric/aiwork/taiwan-opera-calendar/patrol_state/runs/2026-11-25_0311/state.json
- 巡檢紀錄：patrol_runs/2026-11-25_0311.json（/Users/eric/aiwork/taiwan-opera-calendar）
- 證據：patrol_evidence/2026-11-25_0311/
- 產生時間：2026-11-25T03:30:38+08:00
