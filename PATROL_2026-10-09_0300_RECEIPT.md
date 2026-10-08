# 巡檢發布驗收收據｜2026-10-09 03:00 Asia/Taipei

- 資料提交：`ffb104a1cc23aa446776a454a3aa169a07450d4a`（`main`，已推送）。
- 本輪巡檢開始：`2026-10-09T03:01:24+08:00`；公開結果 `failed`，原因為吳奕萱 Facebook 項目不可讀、其他 Threads／Facebook 帳號只部分讀取。
- 對應 workflow：`.github/workflows/daily-update.yml`。
- GitHub Actions：run `37830259024`，`completed/success`，head SHA 與資料提交完全相同。
  - https://github.com/eric1810-tw/taiwan-opera-calendar/actions/runs/37830259024
- 公開狀態核驗：`python3 scripts/patrol_progress.py verify --run patrol_runs/2026-10-09_0300.json --sha ffb104a1cc23aa446776a454a3aa169a07450d4a --actions-run 37830259024` 成功。
- 公開狀態 URL：https://eric1810-tw.github.io/taiwan-opera-calendar/data/patrol_status.json
- 核驗時間：`2026-10-09T03:13:52+08:00`。公開 JSON 與當輪計算相同：`{"startedAt":"2026-10-09T03:01:24+08:00","status":"failed"}`。
- SHA256：`data/schedule.json` `76711b28dd9279f296dd15e38d635a728ddeef62f53dc7715463f61995663d0a`；`data/metadata.json` `c0dd13f63e010d0d11e85353e3a44b75d90fa18b1ae362eb0e677f34e71c6e3e`（未變）；`data/patrol_status.json` `a2c783f1a087420ad8bff0a91673af3052a7bb8e54dccd9a00aeddc41e0883e3`。
- 17 項 unittest、`node --check assets/app.js`、`git diff --check` 及 113 張場次卡 schema／日期／ID／頁面載入檢查均通過。
- 資料發布成功與來源覆蓋狀態分開：網站已發布本輪 `failed` 狀態，並不代表所有社群帳號已讀完。
