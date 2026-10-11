# 2026-10-12 03:00 巡檢發布驗收收據

- 巡檢進度：`patrol_runs/2026-10-12_0300.json`，實際開始 `2026-10-12T02:58:14+08:00`；final status `failed`（Threads/Facebook 覆蓋不足），文化部及全部 Issues 完成。這是內容覆蓋結果，部署本身已成功。
- 資料提交 SHA：`cd6bd23073c94141bbc97a4a30ce1c4db8dabd36`；已推送，`origin/main` 指向同一 SHA。此提交正常整合遠端 auto-update `718b898`，未 force-push。
- Workflow：`.github/workflows/daily-update.yml`，Actions run [38166376833](https://github.com/eric1810-tw/taiwan-opera-calendar/actions/runs/38166376833)，head SHA 完全相同，狀態 `completed/success`。workflow push 路徑執行 17 項測試、組合 Pages 檔案並部署。
- `patrol_progress.py verify` 通過時間：`2026-10-12T03:07:29+08:00`；公開狀態 `2026-10-12T02:58:14+08:00 / failed` 與本輪一致。
- 公開 JSON 對照該資料 SHA 的 `git show`：`patrol_status.json` HTTP 200、完全相同；`schedule.json` HTTP 200、105 筆、完全相同；`metadata.json` HTTP 200、完全相同，刷新時間 `2026-10-11T09:28:30+08:00`。
- 本地驗證：`python3 -m unittest -v` 17 tests PASS；`node --check assets/app.js` PASS；`git diff --check` PASS；schedule schema、日期/endDate、105 筆唯一 ID 與 JSON parse PASS。

## SHA256

- `data/schedule.json`: `35d0adb1218e6ba1c43cd3ac500433cd6d08dc1b7354336c1f2fd2e6dcc61355`
- `data/metadata.json`: `b7b88e788be28d9580dde364f8a0bc321b3f3638773f69f3078b3e64380d5b50`
- `data/patrol_status.json`: `1cf98e34678f7b8a076608c6b9578640379b758c7f166039c527d35242726b65`
- `patrol_runs/2026-10-12_0300.json`（publication verified 後）: `5dae849d007a05ee8e7cbbe05a63f4494cf5fad402dc008fffdfff084eda8a63`

## 恢復

社群貼文正文未讀完，不代表無新資訊。續跑時使用 `python3 scripts/patrol_progress.py resume --run patrol_runs/2026-10-12_0300.json`，先換可用公開讀取路徑，再逐項記錄每次結果。舊 heartbeat `threads` 維持停用。
