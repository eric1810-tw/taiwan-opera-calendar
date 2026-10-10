# 2026-10-11 03:00 獨立巡檢發布驗收收據

驗收時間：`2026-10-11T03:04:39+08:00`（Asia/Taipei）。

## 覆蓋結果

本輪實際開始 `2026-10-11T02:57:55+08:00`，共 21 個來源：2 complete（文化部、GitHub Issues）、4 partial（1 Threads、3 Facebook）、15 failed（9 Threads、6 Facebook）、0 pending。總狀態由 `patrol_progress.py finalize` 正確算為 `failed`；未讀帳號均未被當成沒有新資訊。細節與每次嘗試見 [`PATROL_2026-10-11_0300_INDEPENDENT.md`](PATROL_2026-10-11_0300_INDEPENDENT.md) 及 [`patrol_runs/2026-10-11_0300.json`](patrol_runs/2026-10-11_0300.json)。

本輪沒有因來源新增或修訂場次；遠端 `f1a1f2e` 的自動倒數／過期更新已 fast-forward 保留。網站刷新時間 `2026-10-10T10:01:32+08:00`，巡檢開始 `2026-10-11T02:57:55+08:00`。

## 執行紀錄限制

首輪社群頁面導航及文化部多路徑診斷先批次操作、再批次寫入 progress JSON。對應的 `at` 是紀錄寫入時間，不能證明每一個操作的精確發生時間；Web API 兩次拒絕也合併成一筆。因此，本輪沒有完全遵守「每次嘗試立即 record」，逐次時間證據有缺口。這不改變來源狀態或已發布 `failed` 判定；下輪需在每個操作後立即記錄再繼續。

## 推送與 Actions

- 巡檢資料提交 SHA：`4e86509fc9cb1474b6289f4ec053359042fa0c3a`；推送後 `origin/main` 精確相同。
- Actions：[38078301761](https://github.com/eric1810-tw/taiwan-opera-calendar/actions/runs/38078301761)，workflow `.github/workflows/daily-update.yml`，push event，`headSha` 完全相符，`completed/success`。
- `update-schedule` 及 `deploy` 兩個 job 均 success，GitHub Pages deploy step success。
- `python3 scripts/patrol_progress.py verify --run patrol_runs/2026-10-11_0300.json --sha 4e86509fc9cb1474b6289f4ec053359042fa0c3a --actions-run 38078301761` 成功；run JSON publication=`verified`。

## 公開輸出核對

以下均以 cache-busting 讀取 Pages 公開 JSON，並逐物件比對本地檔案：

- [`公開巡檢狀態 JSON`](https://eric1810-tw.github.io/taiwan-opera-calendar/data/patrol_status.json)：與本輪完全一致，`2026-10-11T02:57:55+08:00 / failed`。
- [`公開場次 JSON`](https://eric1810-tw.github.io/taiwan-opera-calendar/data/schedule.json)：108 筆，與本地完全一致。
- [`公開網站 metadata`](https://eric1810-tw.github.io/taiwan-opera-calendar/data/metadata.json)：`lastUpdated=2026-10-10T10:01:32+08:00`，與本地完全一致。
- [`公開網站首頁`](https://eric1810-tw.github.io/taiwan-opera-calendar/) 已實讀頁尾：資料刷新時間 `2026/10/10 10:01`；社群巡檢開始時間 `2026/10/11 02:57`，標示「巡檢未完成」。兩個時間欄分開顯示。

## SHA256 與檢查

- `data/patrol_status.json`: `d6c80f1056ddbb8451f334ae76565c64c28042e687c09e9671c7cf0bd023fae1`
- `data/schedule.json`: `8d5acc7d6a9e3f4ffeedd835ee3baf8dc20b1f7127afe06e3ea18e18fdebb05e`
- `data/metadata.json`: `a02bfeb53ca4e83c1942797446e01e3f48c4bf17c8692315b604f01d400b63ae`
- `python3 -m unittest -v`: 17 tests PASS。
- `node --check assets/app.js`: PASS。
- `git diff --check`: PASS。
- `updater.validate_schedule`: 108 筆必要欄位、日期／endDate、唯一 ID PASS。

結論：**本輪 `failed` 狀態已成功推送並發布；社群來源覆蓋仍未完成。**
