# 2026-10-10 獨立巡檢發布驗收收據

- 巡檢開始（Asia/Taipei）：2026-10-10T02:56:34+08:00
- 資料提交 SHA：`5b290c871128207bd161bae882ea449afebf699c`
- 推送：成功，`origin/main` 已包含該提交；期間先 fetch 並整合遠端每日更新提交 `83b175cac348cfca4511dfff5d58062e64082d44`，未 force-push。
- SHA 對應 Actions：[`37979681070`](https://github.com/eric1810-tw/taiwan-opera-calendar/actions/runs/37979681070)，workflow `.github/workflows/daily-update.yml`，head SHA 相同，`completed/success`（update-schedule 與 deploy jobs 均 success）。
- 狀態檔驗收：`python3 scripts/patrol_progress.py verify --run patrol_runs/2026-10-10_0300.json --sha 5b290c871128207bd161bae882ea449afebf699c --actions-run 37979681070` 成功；公開 [`data/patrol_status.json`](https://eric1810-tw.github.io/taiwan-opera-calendar/data/patrol_status.json) 回傳 `{"startedAt":"2026-10-10T02:56:34+08:00","status":"failed"}`，與本輪 finalize 一致。公開狀態 failed 反映文化部來源不可讀與社群部分覆蓋，並非發布失敗。
- 排程資料驗收：公開 [`data/schedule.json`](https://eric1810-tw.github.io/taiwan-opera-calendar/data/schedule.json) 共 111 筆，與本地 `data/schedule.json` 位元組相同；核對 `mh-2026-10-10` 及 `lanyang-2026-10-26-guishan-cuoxie-yinyuan` 的 link/sourceUrl/verifyStatus 均與預期相符。
- SHA-256：`data/schedule.json` = `06ba5d68c95f1c3030744bf27f0aa64ea19ddca67196b827f7faa33470f471d1`；`data/patrol_status.json` = `677d5f4531037074ac31737e0a093ff82b7016208f7bae2c2026d7b2319a5d2d`。公開兩檔雜湊與本地一致。
- 驗收時間：2026-10-10T03:23:43+08:00 執行 `verify` 成功；隨後公開 schedule 與 status 檔位元組比對相同。
- 網站資料刷新時間：`data/metadata.json` 的 `lastUpdated` 為 `2026-10-09T10:41:36+08:00`；與本輪巡檢開始時間分開保存。
- 本地測試：17/17 unittest PASS；`node --check assets/app.js` PASS；`git diff --check` PASS；排程 schema/日期/唯一 ID/目標來源檢查 PASS。
- 覆蓋限制：文化部當期端點三次讀取失敗；19 個 Threads/Facebook 來源因近 7 日內容或媒體範圍未完整讀取而維持 partial。詳見 [PATROL_2026-10-10_0300_INDEPENDENT.md](PATROL_2026-10-10_0300_INDEPENDENT.md)。

## 重試後覆蓋狀態驗收

- 重試：恢復 `patrol_runs/2026-10-10_0300.json`；Culture API 以 curl 成功讀取完整 1,622 筆，候選篩選 34 筆、核對 9 個 OPENTIX 頁面，演出均已由現有卡片覆蓋；另重讀新吉 Threads 及繡花園／明華園地字 Facebook 近期貼文。Culture 由 failed 恢復為 complete，社群仍 partial，因此總狀態由 failed 改為 partial。
- 新狀態資料 SHA：`16adf82328be58dc3456bd3c9a079ea6cdde74b4`，已推送至 `origin/main`。排程 JSON 未變更；SHA 是包含本輪 run JSON、報告及 `data/patrol_status.json=partial` 的資料提交。
- 對應 [Actions run 38005309417](https://github.com/eric1810-tw/taiwan-opera-calendar/actions/runs/38005309417)：head SHA 相同，`.github/workflows/daily-update.yml` `completed/success`。
- 07:39:20+08:00 再次執行 `patrol_progress.py verify` 成功；公開狀態 `{"startedAt":"2026-10-10T02:56:34+08:00","status":"partial"}` 與 finalize 一致。
- 公開 schedule 仍為 111 筆並與本地位元組相同，SHA-256 `06ba5d68c95f1c3030744bf27f0aa64ea19ddca67196b827f7faa33470f471d1`；公開及本地 `data/patrol_status.json` SHA-256 均為 `5703c039335d2bfacc690d9140c25bd3cd0f6c1983dfbb7e376582d0b0f98303`。metadata lastUpdated 仍為 `2026-10-09T10:41:36+08:00`，未與巡檢時間混用。
- 本輪測試仍為 17/17 unittest、JS syntax、diff check 與 111 筆排程檢查全部 PASS。來源覆蓋 partial 代表社群讀取不完整，不是無新資訊或發布失敗。
