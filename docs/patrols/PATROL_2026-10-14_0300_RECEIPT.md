# 2026-10-14 03:00 巡檢驗收收據（發布受阻）

- 本輪啟動時間：`2026-10-14T03:05:15+08:00`（Asia/Taipei）。21 個動態來源最後狀態：10 Threads failed、Facebook 1 failed／8 partial、culture partial、Issues complete、0 pending；finalized `failed`。failed/partial 是資料覆蓋結果，與部署狀態分開。
- 報告：[`PATROL_2026-10-14_0300_INDEPENDENT.md`](./PATROL_2026-10-14_0300_INDEPENDENT.md)。本輪證據：[`patrol_runs/2026-10-14_0300.json`](patrol_runs/2026-10-14_0300.json)。公開排程與 metadata 未因本輪更新。
- 驗收：`python3 -m unittest -v` 17 tests PASS；`node --check assets/app.js` PASS；`git diff --check` PASS；96 筆演出必要欄位、唯一 ID、ISO 日期及 endDate 順序檢查 PASS。
- 本地資料提交：`9c9efc9195f55e29d18ebf564c89024b03e98c66`（`Record 2026-10-14 independent patrol`），只納入本輪 JSON、`data/patrol_status.json` 與巡檢報告。工作樹其他既有修改／未追蹤檔案未納入。
- 遠端驗收受阻：`git fetch origin main` 與 `git push origin main` 均回報 `fatal: unable to access 'https://github.com/eric1810-tw/taiwan-opera-calendar.git/': Could not resolve host: github.com`。推送失敗當下本機 `main` ahead 1；其後只增加本地收據提交，現為 ahead 2；`origin/main` 未更新。沒有這個 SHA 的 Actions run，因此無法確認 `.github/workflows/daily-update.yml` `completed/success`；也沒有執行或宣稱通過公開狀態 verify。公開巡檢狀態仍未證實為本輪內容；不能稱已上線。
- `patrol_runs/2026-10-14_0300.json` 的 `publication` 已記 `blocked`，包含本地 SHA、DNS 故障、時間與恢復步驟。網路恢復後，接續同一輪：先 `git fetch origin main`；檢查並正常整合遠端新提交（保留既有工作樹修改），再推送包含本輪狀態檔的提交；等待同一 SHA 的 daily-update Actions 完成成功，取得真實 run ID，再執行：

  ```sh
  python3 scripts/patrol_progress.py verify --run patrol_runs/2026-10-14_0300.json --sha <完整部署SHA> --actions-run <真實Actions-run-ID>
  ```

  成功後將更新本輪 JSON 的 verified 收據，再 stage 本輪明列檔案並提交 `[skip ci]` 稽核收據；不得以假 run ID 或舊公開狀態替代驗收。

## SHA256

- `data/schedule.json`: `6640702ab0f9500327dd923a9d19ccbee6367936be140f0d4d3cbfada1cf6371`
- `data/metadata.json`: `1557c7f2c058e52e1e7ed6242c4e828032428f5b5146f976fb89d9f43357e1f2`
- `data/patrol_status.json`: `257ba0693b0b24f52984a2cd2765da1c56da65653e8f34b29e37b9759b87a516`
- `patrol_runs/2026-10-14_0300.json`（publication blocked）: `2d1cff9623bcecbff23dc1169e9788badfbd8efe15d867c71efa6663922d774c`

截至 `2026-10-14T03:23:12+08:00`，本輪網站資料刷新時間仍是 `2026-10-13T11:18:52+08:00`，與巡檢啟動時間分開保存。
