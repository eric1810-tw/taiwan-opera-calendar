# 臺灣戲曲獨立巡檢驗收收據｜2026-10-15

- 巡檢 Run：`patrol_runs/2026-10-15_0300.json`
- 實際巡檢開始：`2026-10-15T07:15:39+08:00`（Asia/Taipei）
- 執行模型名稱／實際推理強度無法從排程執行環境驗證；不宣稱已切換為 Luna High。
- 覆蓋狀態：`failed`（19 partial、1 failed、1 complete、0 pending）。吳奕萱 Facebook 最新貼文正文不可讀；文化部本輪全類別 API 因 DNS 失敗未讀。已發布 failed 狀態不代表來源覆蓋完成。
- 資料 SHA：`d8f9695580da32c3f6249d613c52cc9f72d73d0a`
- GitHub Actions：[Daily Opera Schedule Auto-Updater #38654981372](https://github.com/eric1810-tw/taiwan-opera-calendar/actions/runs/38654981372)；workflow `.github/workflows/daily-update.yml`；head SHA 相符；`completed/success`。
- 公開狀態驗收：`python3 scripts/patrol_progress.py verify` 通過於 `2026-10-15T07:36:12+08:00`。公開 [`patrol_status.json`](https://eric1810-tw.github.io/taiwan-opera-calendar/data/patrol_status.json) 為 `{"startedAt":"2026-10-15T07:15:39+08:00","status":"failed"}`，與本輪 finalized 狀態相同。
- 網站資料刷新：巡檢開始前本地 metadata 為 `2026-10-13T11:18:52+08:00`；推送前合併遠端每日更新 `b9384fd` 後為 `2026-10-14T09:31:49+08:00`。這是獨立資料刷新時間，不是巡檢開始時間。本輪未直接編修 schedule/metadata；合併後 schedule 為95張卡。
- SHA-256（驗收收據提交前）：
  - Run JSON：`3f731f66b47d271a5fb5be6ab136d1b4694018a9daa646eac20f20d663c20e4b`
  - `data/patrol_status.json`：`05cc4eae57c880c9d68915cb222c7f770427b5b74b87013e7961e1d2fdcf6827`
  - `data/schedule.json`：`3174f52f1e6786b26a283ab1233fbbf8be98ca77821248f234b48ebb606fbaba`
  - `data/metadata.json`：`de6c3f2abb98c4632b5cfd13f512eaf01a3f6fccf376609ed79fb1ff50590df0`
- 驗證：17 unittest 通過；`node --check assets/app.js` 通過；`git show --check HEAD` 通過；95 張卡必要欄位、ISO 日期、`endDate` 順序、唯一 ID 與唯一「日期＋場地＋劇團＋劇目」完全相同鍵檢查通過。
- 本地/遠端 `main` 在資料 SHA 推送後相符。驗收收據與已驗證 run JSON 以獨立 `[skip ci]` commit 保存，不會觸發另一輪部署。
- 預存工作區修改 `ISSUES_REVIEW.md`、`PROJECT_HANDOVER.md` 及三個 untracked 檔未 stage、未提交。
