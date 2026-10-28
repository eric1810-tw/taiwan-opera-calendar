# 巡檢報告 2026-10-28_0311（patrol-v2，正式）

## 需要 Eric 決定

- 前幾天的巡檢沒有完成：2026-10-27：輪次 2026-10-27_1544 沒有跑完

## 結論

| 項目 | 結果 |
| --- | --- |
| 執行 | 開始 2026-10-28T03:11:50+08:00；結果 進行中；步驟 preflight:done、collect:done、pack:done、judge:done、check:done、review:done、apply:done、publish:done、report:running |
| 來源 | 21 個：完整 1、部分 1、失敗 19、未讀 0 |
| 資料 | 送判讀 24 篇／圖 0 張；變更提案 2、確認一致 18、待查 5、退回 0、漏處置 0 |
| 寫入 | 寫入 2、add_card 拒絕 0、審查未通過 0 |
| 發布 | verified；SHA 8802522728e2d861f18864f1366f5a923bfa7691；Actions 40622828847 |

## 模型與用量

| 角色 | 模型 | 依據 |
| --- | --- | --- |
| main | claude-sonnet-5-5 | get_session self：effort=medium |
| judge | sonnet | Agent 工具 model 參數；effort=medium |
| review | opus | Agent 工具 model 參數；effort=high |

- 判讀批次 1；送出貼文 24 篇、圖片 0 張、正文約 7040 字
- 略過（已判讀未變動）25 篇；窗口外 0 篇
- 第二次審查：有（2 項）

## 來源

| 來源 | 狀態 | 範圍 | 說明 |
| --- | --- | --- | --- |
| threads:joe_huang_k_w | 失敗 | 讀取器未回報此來源 | 讀取器結束碼 1：eric/aiwork/taiwan-opera-calendar/scripts/patrol_v2/social_capture.mjs:156:11) at async ru… |
| threads:h.akito_1996 | 失敗 | 讀取器未回報此來源 | 讀取器結束碼 1：eric/aiwork/taiwan-opera-calendar/scripts/patrol_v2/social_capture.mjs:156:11) at async ru… |
| threads:the_rin.lpm | 失敗 | 讀取器未回報此來源 | 讀取器結束碼 1：eric/aiwork/taiwan-opera-calendar/scripts/patrol_v2/social_capture.mjs:156:11) at async ru… |
| threads:1013.yr_ | 失敗 | 讀取器未回報此來源 | 讀取器結束碼 1：eric/aiwork/taiwan-opera-calendar/scripts/patrol_v2/social_capture.mjs:156:11) at async ru… |
| threads:xuefeng_lu_ | 失敗 | 讀取器未回報此來源 | 讀取器結束碼 1：eric/aiwork/taiwan-opera-calendar/scripts/patrol_v2/social_capture.mjs:156:11) at async ru… |
| threads:yuzhongluo | 失敗 | 讀取器未回報此來源 | 讀取器結束碼 1：eric/aiwork/taiwan-opera-calendar/scripts/patrol_v2/social_capture.mjs:156:11) at async ru… |
| threads:taiwaneseopera168 | 失敗 | 讀取器未回報此來源 | 讀取器結束碼 1：eric/aiwork/taiwan-opera-calendar/scripts/patrol_v2/social_capture.mjs:156:11) at async ru… |
| threads:jing__1017 | 失敗 | 讀取器未回報此來源 | 讀取器結束碼 1：eric/aiwork/taiwan-opera-calendar/scripts/patrol_v2/social_capture.mjs:156:11) at async ru… |
| threads:hilang.on.tour | 失敗 | 讀取器未回報此來源 | 讀取器結束碼 1：eric/aiwork/taiwan-opera-calendar/scripts/patrol_v2/social_capture.mjs:156:11) at async ru… |
| threads:yolin1991 | 失敗 | 讀取器未回報此來源 | 讀取器結束碼 1：eric/aiwork/taiwan-opera-calendar/scripts/patrol_v2/social_capture.mjs:156:11) at async ru… |
| facebook:sunhope.fans | 失敗 | 讀取器未回報此來源 | 讀取器結束碼 1：eric/aiwork/taiwan-opera-calendar/scripts/patrol_v2/social_capture.mjs:156:11) at async ru… |
| facebook:HsiaoHsiYuan1913 | 失敗 | 讀取器未回報此來源 | 讀取器結束碼 1：eric/aiwork/taiwan-opera-calendar/scripts/patrol_v2/social_capture.mjs:156:11) at async ru… |
| facebook:100063868113954 | 失敗 | 讀取器未回報此來源 | 讀取器結束碼 1：eric/aiwork/taiwan-opera-calendar/scripts/patrol_v2/social_capture.mjs:156:11) at async ru… |
| facebook:MingHuaYuanTianTaiwaneseOpera | 失敗 | 讀取器未回報此來源 | 讀取器結束碼 1：eric/aiwork/taiwan-opera-calendar/scripts/patrol_v2/social_capture.mjs:156:11) at async ru… |
| facebook:61574134933376 | 失敗 | 讀取器未回報此來源 | 讀取器結束碼 1：eric/aiwork/taiwan-opera-calendar/scripts/patrol_v2/social_capture.mjs:156:11) at async ru… |
| facebook:mhysun | 失敗 | 讀取器未回報此來源 | 讀取器結束碼 1：eric/aiwork/taiwan-opera-calendar/scripts/patrol_v2/social_capture.mjs:156:11) at async ru… |
| facebook:61594936681482 | 失敗 | 讀取器未回報此來源 | 讀取器結束碼 1：eric/aiwork/taiwan-opera-calendar/scripts/patrol_v2/social_capture.mjs:156:11) at async ru… |
| facebook:lanyang.opera | 失敗 | 讀取器未回報此來源 | 讀取器結束碼 1：eric/aiwork/taiwan-opera-calendar/scripts/patrol_v2/social_capture.mjs:156:11) at async ru… |
| facebook:Taichungpuppettheater | 失敗 | 讀取器未回報此來源 | 讀取器結束碼 1：eric/aiwork/taiwan-opera-calendar/scripts/patrol_v2/social_capture.mjs:156:11) at async ru… |
| culture | 部分 | total 1363、fetchedAt 2026-10-27T09:46:26+08:00、戲曲紀錄 30 筆 | 資料新鮮；逐筆處置待判讀後確認 |
| issues | 完整 | 2 筆皆有處置 | 逐筆處置完成 |

- OPENTIX：sitemap 1038 個活動、本輪有變 838、抓取 250、戲曲相關且未過期 17、延後 588、錯誤 0

## 卡片變更

| 編號 | 動作 | 來源 | 內容 | 差異 | 審查 | 寫入 |
| --- | --- | --- | --- | --- | --- | --- |
| chg-001 | add | https://www.opentix.life/event/2101875447018987520 | 長義閣掌中劇團｜《乘上鸚鵡的記憶飛翔》｜新嘉義座（嘉義市 西區中山路616號O棟2樓）｜2026-11-06 正戲 19:30 |  | approve：source.text（OPENTIX 節目頁）明列「節目：《乘上鸚鵡的記憶飛翔》」「主辦：長義閣掌中劇團」「場次：2… | added  |
| chg-002 | add | https://www.opentix.life/event/2083498970180161537 | 光興閣掌中劇團｜《鬼谷第貳部》｜彰化縣文化局員林演藝廳小劇場（彰化縣 員林市員林大道二段99號）｜2026-11-07 正戲 19:00、2026-11-08 正戲 14:30 |  | approve：source.text（OPENTIX）明列「節目：《鬼谷第貳部》」「主辦：光興閣掌中劇團」，兩個場次「2026-11… | added  |

## 待查與退回

| 類別 | 貼文 | 原因 | 說明 |
| --- | --- | --- | --- |
| 待查 | https://www.opentix.life/event/2090269380048343041 | judge-needs-check | 十團聯合育成展演，文字未見劇種與劇目，無法判定是否含歌仔戲／布袋戲 |
| 待查 | https://www.opentix.life/event/2095800553720586241 | judge-needs-check | 兒童劇團作品，僅稱保留歌仔戲唱腔，劇種是否屬歌仔戲需人工確認 |
| 待查 | https://www.opentix.life/program/2088104133013299200 | judge-needs-check | 文字未寫布袋戲，偶偶偶劇團不能憑名稱判定為布袋戲；表上卡片劇種需人工確認 |
| 待查 | https://www.opentix.life/program/2080173157578416129 | puppet-not-budaixi |  |
| 待查 | https://www.opentix.life/program/2112035354878472193 | puppet-not-budaixi |  |

## 紀錄檔

- 本輪狀態：/Users/eric/aiwork/taiwan-opera-calendar/patrol_state/runs/2026-10-28_0311/state.json
- 巡檢紀錄：patrol_runs/2026-10-28_0311.json（/Users/eric/aiwork/taiwan-opera-calendar）
- 證據：patrol_evidence/2026-10-28_0311/
- 產生時間：2026-10-28T10:46:19+08:00
