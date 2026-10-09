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
