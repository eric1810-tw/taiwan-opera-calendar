# 巡檢報告 2026-11-22_0311（patrol-v2，正式）

## 需要 Eric 決定

- 前幾天的巡檢沒有完成：2026-11-21：輪次 2026-11-21_0311 沒有跑完

## 結論

| 項目 | 結果 |
| --- | --- |
| 執行 | 開始 2026-11-22T03:11:05+08:00；結果 進行中；步驟 preflight:done、collect:done、pack:done、judge:done、check:done、verify:done、review:done、apply:done、publish:done、report:running |
| 來源 | 21 個：完整 6、部分 13、失敗 2、未讀 0 |
| 資料 | 送判讀 60 篇／圖 42 張；變更提案 4、確認一致 12、送查證 18（成立 2、與卡相同 1、查無佐證不收 15）、退回 0、漏處置 0；已過期不收 9、遠期暫存 8 |
| 寫入 | 寫入 1、add_card 拒絕 2、審查未通過 1 |
| 發布 | verified；SHA 6324b16d088fbc8b005c457b7b1a8a8311725e84；Actions 44942108620 |

## 模型與用量

| 角色 | 模型 | 依據 |
| --- | --- | --- |
| main | claude-sonnet-5-5 | get_session self：effort=medium |
| judge | sonnet | Agent 工具 model 參數；effort=medium |
| verify | opus | Agent 工具 model 參數；effort=medium |
| review | opus | Agent 工具 model 參數；effort=medium |

- 判讀批次 3；送出貼文 60 篇、圖片 42 張、正文約 13696 字
- 略過（已判讀未變動）27 篇；窗口外 27 篇
- 第二次審查：有（4 項）

## 來源

| 來源 | 狀態 | 範圍 | 說明 |
| --- | --- | --- | --- |
| threads:joe_huang_k_w | 部分 | 首屏 4 篇、累積 16 篇；最新 2026-11-21T00:14:15+08:00、最舊 2026-11-06T18:32:27+08:00；捲動 1 次、停止原因 reached-window；圖片下載 23 張 | 不變式通過；證據 /Users/eric/aiwork/taiwan-opera-calendar/patrol_evidence/2026-11-22_0311/threads_joe_huang… |
| threads:h.akito_1996 | 部分 | 首屏 7 篇、累積 7 篇；最新 2026-11-21T23:54:12+08:00、最舊 2026-09-27T00:04:33+08:00；捲動 3 次、停止原因 no-new-after-3；圖片下載 3 張 | 不變式通過；證據 /Users/eric/aiwork/taiwan-opera-calendar/patrol_evidence/2026-11-22_0311/threads_h.akito_1… |
| threads:the_rin.lpm | 部分 | 首屏 5 篇、累積 5 篇；最新 2026-11-20T19:39:32+08:00、最舊 2026-10-01T22:31:26+08:00；捲動 3 次、停止原因 no-new-after-3；圖片下載 26 張 | 不變式通過；證據 /Users/eric/aiwork/taiwan-opera-calendar/patrol_evidence/2026-11-22_0311/threads_the_rin.l… |
| threads:xuefeng_lu_ | 完整 | 7 天窗口讀完（停止原因 reached-window）；窗口內 2 篇皆有處置；圖片 1 張皆已判讀 | 不變式通過、逐篇處置完成 |
| threads:yuzhongluo | 部分 | 首屏 4 篇、累積 4 篇；最新 2026-11-22T02:45:14+08:00、最舊 2026-11-21T14:22:35+08:00；捲動 3 次、停止原因 no-new-after-3；圖片下載 8 張 | 不變式通過；證據 /Users/eric/aiwork/taiwan-opera-calendar/patrol_evidence/2026-11-22_0311/threads_yuzhonglu… |
| threads:taiwaneseopera168 | 部分 | 首屏 3 篇、累積 4 篇；最新 2026-11-21T20:12:52+08:00、最舊 2026-08-16T02:33:12+08:00；捲動 4 次、停止原因 no-new-after-3；圖片下載 0 張 | 不變式通過；證據 /Users/eric/aiwork/taiwan-opera-calendar/patrol_evidence/2026-11-22_0311/threads_taiwanese… |
| threads:jing__1017 | 部分 | 首屏 6 篇、累積 6 篇；最新 2026-11-21T21:18:50+08:00、最舊 2026-10-28T19:50:21+08:00；捲動 3 次、停止原因 no-new-after-3；圖片下載 7 張 | 不變式通過；證據 /Users/eric/aiwork/taiwan-opera-calendar/patrol_evidence/2026-11-22_0311/threads_jing__101… |
| threads:hilang.on.tour | 完整 | 7 天窗口讀完（停止原因 reached-window）；窗口內 0 篇皆有處置；圖片 0 張皆已判讀 | 不變式通過、逐篇處置完成 |
| threads:yolin1991 | 部分 | 首屏 6 篇、累積 6 篇；最新 2026-11-21T11:27:15+08:00、最舊 2026-11-18T10:38:29+08:00；捲動 3 次、停止原因 no-new-after-3；圖片下載 6 張 | 不變式通過；證據 /Users/eric/aiwork/taiwan-opera-calendar/patrol_evidence/2026-11-22_0311/threads_yolin1991… |
| threads:yilan_taiwan | 部分 | 首屏 4 篇、累積 4 篇；最新 2026-11-20T19:29:01+08:00、最舊 2026-11-20T16:13:04+08:00；捲動 3 次、停止原因 no-new-after-3；圖片下載 4 張 | 不變式通過；證據 /Users/eric/aiwork/taiwan-opera-calendar/patrol_evidence/2026-11-22_0311/threads_yilan_tai… |
| facebook:sunhope.fans | 失敗 | 首屏 0 篇、累積 0 篇；最新 無、最舊 無；捲動 3 次、停止原因 no-new-after-3；圖片下載 0 張 | 不變式通過；證據 /Users/eric/aiwork/taiwan-opera-calendar/patrol_evidence/2026-11-22_0311/facebook_sunhope.… |
| facebook:HsiaoHsiYuan1913 | 完整 | 7 天窗口讀完（停止原因 reached-window）；窗口內 0 篇皆有處置；圖片 0 張皆已判讀 | 不變式通過、逐篇處置完成 |
| facebook:100063868113954 | 部分 | 首屏 1 篇、累積 1 篇；最新 無、最舊 無；捲動 3 次、停止原因 no-new-after-3；圖片下載 12 張 | 不變式通過；證據 /Users/eric/aiwork/taiwan-opera-calendar/patrol_evidence/2026-11-22_0311/facebook_10006386… |
| facebook:MingHuaYuanTianTaiwaneseOpera | 部分 | 首屏 1 篇、累積 1 篇；最新 無、最舊 無；捲動 3 次、停止原因 no-new-after-3；圖片下載 12 張 | 不變式通過；證據 /Users/eric/aiwork/taiwan-opera-calendar/patrol_evidence/2026-11-22_0311/facebook_MingHuaY… |
| facebook:61574134933376 | 失敗 | 首屏 0 篇、累積 0 篇；最新 無、最舊 無；捲動 3 次、停止原因 no-new-after-3；圖片下載 0 張 | 不變式通過；證據 /Users/eric/aiwork/taiwan-opera-calendar/patrol_evidence/2026-11-22_0311/facebook_61574134… |
| facebook:mhysun | 部分 | 首屏 1 篇、累積 1 篇；最新 無、最舊 無；捲動 3 次、停止原因 no-new-after-3；圖片下載 13 張 | 不變式通過；證據 /Users/eric/aiwork/taiwan-opera-calendar/patrol_evidence/2026-11-22_0311/facebook_mhysun.j… |
| facebook:61594936681482 | 完整 | 7 天窗口讀完（停止原因 reached-window）；窗口內 0 篇皆有處置；圖片 0 張皆已判讀 | 不變式通過、逐篇處置完成 |
| facebook:lanyang.opera | 部分 | 首屏 1 篇、累積 1 篇；最新 無、最舊 無；捲動 3 次、停止原因 no-new-after-3；圖片下載 12 張 | 不變式通過；證據 /Users/eric/aiwork/taiwan-opera-calendar/patrol_evidence/2026-11-22_0311/facebook_lanyang.… |
| facebook:Taichungpuppettheater | 部分 | 首屏 1 篇、累積 1 篇；最新 無、最舊 無；捲動 3 次、停止原因 no-new-after-3；圖片下載 16 張 | 不變式通過；證據 /Users/eric/aiwork/taiwan-opera-calendar/patrol_evidence/2026-11-22_0311/facebook_Taichung… |
| culture | 完整 | 9 筆皆有處置 | 逐筆處置完成 |
| issues | 完整 | 3 筆皆有處置 | 逐筆處置完成 |

- OPENTIX：sitemap 843 個活動、本輪有變 668、抓取 250、戲曲相關且未過期 35、延後 418、錯誤 0

## 卡片變更

| 編號 | 動作 | 來源 | 內容 | 差異 | 審查 | 寫入 |
| --- | --- | --- | --- | --- | --- | --- |
| chg-001 | add | https://www.opentix.life/event/2110252942473105409 | 三昧堂創意木偶團隊｜2026偶樂迴響布袋戲音樂劇音樂會｜嘉義縣表演藝術中心實驗劇場（嘉義縣 民雄鄉建國路二段265號）｜2026-12-13 正戲 14:00 |  | approve：OPENTIX 原文「場次：2026-12-13 14:00｜地點：嘉義縣表演藝術中心實驗劇場（嘉義縣 民雄鄉建國路二… | added  |
| chg-002 | add | https://www.facebook.com/lanyang.opera/reels_tab | 蘭陽戲劇團｜《楊宗保與穆桂英》｜基隆表演藝術中心 演藝廳｜2026-12-13 正戲 14:30 |  | needs-check：內容本身正確：海報 363c82… 看得到「蘭陽戲劇團《楊宗保與穆桂英》12/13 (Sun.) 14:30 基隆表演… | held  |
| chg-003 | add（查證成立） | https://udn.com/news/story/7266/9893679（原貼文 https://www.opentix.life/event/2080109546140397568） | 一心戲劇團｜《閻王的假期》｜台北市藝文推廣處城市舞台｜2026-12-05 正戲 未公布、2026-12-06 正戲 未公布 |  | approve：聯合報 2026-11-21 20:44 的報導原文「『一心戲劇團』將於12月5日、12月6日於台北市藝文推廣處城市舞… | rejected badgeType-not-ticket |
| chg-004 | add（查證成立） | https://klpas.klcg.gov.tw/News_Photo_Content.aspx?n=8045&s=19143（原貼文 https://www.facebook.com/lanyang.opera/reels_tab） | 蘭陽戲劇團｜《楊宗保與穆桂英》｜基隆表演藝術中心演藝廳｜2026-12-13 正戲 14:30 |  | approve：基隆市表演藝術網（更新日期 115-11-19）原文「辦理日期時間(起) 115-12-13 14:30」「活動地點 … | rejected title-not-in-quote,artist-not-in-quote |

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

- 本輪狀態：/Users/eric/aiwork/taiwan-opera-calendar/patrol_state/runs/2026-11-22_0311/state.json
- 巡檢紀錄：patrol_runs/2026-11-22_0311.json（/Users/eric/aiwork/taiwan-opera-calendar）
- 證據：patrol_evidence/2026-11-22_0311/
- 產生時間：2026-11-22T03:40:41+08:00
