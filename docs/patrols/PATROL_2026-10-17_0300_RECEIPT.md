# 2026-10-17 巡檢發布驗收收據

- 巡檢開始：2026-10-17T03:02:16+08:00（Asia/Taipei）
- coverage：failed（17 partial、3 failed、1 complete）；動態目標21項。
- 最終資料 commit：`f03b44dcd6bf0c4984b6f890cfd29e2ba77dbe45`（Add verified 2026-11-01 opera lecture）。資料 commit 推送嘗試時本地 `main` ahead 5；03:17:49 最後一次 push 前 HEAD 為 `3d5a2ff`、當時 ahead 6，`git push origin main` 因 `Could not resolve host: github.com` 失敗。`df258e4` 及其後續收尾提交在該次失敗嘗試後才建立；`git fetch origin main` 此前亦因同一 DNS 故障失敗。
- schedule SHA-256：`a847f1ac24883c4e458e0531e59a847bcaa6cd21091647376b8272f1b6f4ddfa`（98→99，新增1張官方核實講座卡）
- metadata SHA-256：`9ea3e07f20a1a6f3e31f52a572d2d34d16f0ee95f2427a1dbd640f80ad2efd35`（未修改）
- patrol_status SHA-256：`2514309cb1e51b361d134bc2ddf62bc539ee418936fbfd845975b18a99a8bd5e`
- 本輪 JSON SHA-256：`2442f40ff095f89916b3ce61f6dfd207c67730fdaa49458a940c1528574f14d8`（publication.state=`blocked`；目標資料 SHA 為上述 commit）。
- 驗證：`python3 -m unittest -v` 18/18 passed；`node --check assets/app.js`、`git diff --check` passed；schedule JSON/schema、日期、endDate、唯一 ID 與重複事件鍵檢查 passed。
- GitHub：目前無本輪 matching Actions run，無真實 run id 可傳給 `verify`。公開 `data/patrol_status.json` 實讀仍為 `2026-10-15T07:15:39+08:00 / failed`。本輪未上線。網路恢復後先 fetch 並核對遠端祖先/差異，再安全整合與推送；若 push workflow 因 skip 指令未啟動，對最新 main SHA 用 `workflow_dispatch` 觸發 `.github/workflows/daily-update.yml`。`workflow_dispatch` 會執行 updater，可能改 schedule/metadata 並產生自動提交；須核該次實際資料樹與公開 schedule/metadata 雜湊。以 workflow 的實際 `head_sha` 和 matching run id 執行 `verify`，僅當 Actions completed/success 且公開 status 符合本輪才記 verified；另記任何 updater 自動提交的資料 SHA。
- 前一輪 2026-10-16 因 resume 留下的 JSON 修改保持未暫存；所有原有工作區修改及未追蹤文件均保留。
- 2026-10-17 20:49 resume 重查：`git fetch origin main` 仍 DNS 失敗。GitHub 網頁觀察遠端main `e063c0b`（parent `ae0a92b`，其parent為本地舊追蹤基底 `58a989b`）；遠端在共同基底 `58a989b` 之後多兩個自動更新提交；本地亦有11個巡檢/收尾提交在該基底之後，因此兩邊已分歧。Actions #106 `38988749015` 為scheduled、head `ae0a92b`、completed/success；它不是本輪資料SHA的 matching Actions，不能代替 verify。最新公開 `patrol_status.json` 仍 `2026-10-15T07:15:39+08:00 / failed`。本次未推送，沒有改遠端資料；DNS恢復後須 fetch/比較兩個updater提交與本輪變更，再整合並驗收。
- 收據更新時間：2026-10-17T20:49:21+08:00（Asia/Taipei）。


## 最終續跑驗收（2026-10-17T21:15:54+08:00 Asia/Taipei）

- 沙箱診斷：一般受限命令執行環境無 DNS resolver 設定且 DNS 查詢失敗；提升權限唯讀測試解析、HTTPS、`git ls-remote`、`git fetch` 全部成功，確認為命令沙箱網路隔離，不是電腦整體斷網。
- 遠端整合：在 fetch 並比較 `ae0a92b`、`e063c0b` 兩筆 updater 提交後，以 `b33144e129c91a6aec5c6baaac78d33113519f0a` 整合並成功推送；無 force push。保留最新 metadata 刷新時間與 daysAway、三筆 updater 過期剔除、巡檢新增／更正；schedule 共96筆。
- matching Actions：[39035784418](https://github.com/eric1810-tw/taiwan-opera-calendar/actions/runs/39035784418)，event=push，head SHA=`b33144e129c91a6aec5c6baaac78d33113519f0a`，completed/success。`patrol_progress.py verify` 成功，publication=`verified`。
- 最終本地與公開 SHA-256 完全一致：
  - `data/schedule.json`: `bcecb6bae0840985a50514f3caa57578c6be36c3097b4d0371657ed5f3a78ffc`
  - `data/metadata.json`: `997d55acc5e86468c7d5b0b6f2f15c13ac7762e6e2af3f8084b602e1974a47cd`
  - `data/patrol_status.json`: `2514309cb1e51b361d134bc2ddf62bc539ee418936fbfd845975b18a99a8bd5e`
- coverage=`failed`（17 partial、3 failed、1 complete）；公開狀態正確反映失敗，未宣稱來源覆蓋成功。網站資料刷新時間為 10/17 08:57:55+08:00，社群巡檢開始為 10/17 03:02:16+08:00。
- 本輪 JSON（含續跑根因與驗收紀錄）SHA-256：`f0974d805eabac470d4fe497b50d56c4b2dca64479c985c229aaa0ac8ff2e5af`。
