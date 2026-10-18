# 2026-10-18 巡檢發布驗收收據

- 模型：實際執行模型/推理強度未能驗證，不宣稱本輪使用 Luna High。
- 巡檢開始：`2026-10-18T00:21:53+08:00`（Asia/Taipei）；恢復時間：`00:37:36+08:00`、`02:57:49+08:00`。
- 覆蓋：`failed`（1 complete、19 partial、1 failed）；目標21項。`threads:1013.yr_` 個人頁/搜尋路徑不可讀；文化部初讀曾讀取1,527筆並篩出30候選，但恢復時 API DNS 與瀏覽器替代路徑皆失敗。完整逐次證據見本輪 JSON。
- 本輪資料 commit：`6b61371957343c0110a6e9d63040876638fbf293`（`chore(patrol): 2026-10-18 community coverage update`）。本輪只 stage `data/schedule.json` 與 `patrol_runs/2026-10-18_0300.json`；`data/patrol_status.json` 內容與前次已推送狀態相同：`2026-10-18T00:21:53+08:00 / failed`。
- 發布：`git fetch origin main` 及 `git push origin main` 均失敗，錯誤為 `Could not resolve host: github.com`；`gh auth status` 另報預設 token invalid。本輪 commit 留在本機；沒有該 SHA 的 Actions run，故不能用既有舊 SHA 的成功結果替代。
- 公開核對（cache-busted in-app browser）：狀態檔仍為 `2026-10-18T00:21:53+08:00 / failed`，內容值相同但不能證明新 commit 已發布；公開場次資料仍96張，缺本輪臺中及高雄新卡。本機 schedule 為98張。其後恢復補讀戲籠出巡、蘭陽戲劇團、台中木偶劇團並追加記錄；台中木偶劇團11/1 14:00工作坊（20組、300元）保留候選，未錯誤當成演出或講座。
- `data/schedule.json` 本機 SHA-256：`2fd2a74b07fb3423df7e0222bbf2f029d90ee92d7777a184c8a3090810a4754f`（98張）。
- `data/metadata.json` SHA-256：`997d55acc5e86468c7d5b0b6f2f15c13ac7762e6e2af3f8084b602e1974a47cd`，資料刷新時間維持 `2026-10-17T08:57:55+08:00`。
- `data/patrol_status.json` SHA-256：`70fcdae5d6ec2fb42e52ff5c5ec1b0853cac1289a6c6c30b060d387e9ddc339f`。
- 本輪 JSON 更新後 SHA-256：2b6edf585730155c62da3dfb788d744144d9f4206282c10d31eec982b16c1cf0。
- 驗收：`python3 -m unittest -v` 18項通過；`node --check assets/app.js`、`git diff --check`、schedule schema/日期/endDate/唯一 ID/事件鍵檢查通過。發布驗收因網路無法推送而 blocked。
- 接續：GitHub DNS 恢復後 `git fetch origin main`、檢查遠端分歧、推送資料 commit；取得資料SHA的 `daily-update.yml` completed/success run；若稽核提交 `[skip ci]`，對最新資料HEAD執行 `workflow_dispatch`，然後用真實run ID執行本輪 `patrol_progress.py verify`。
- 其後三個補讀嘗試使巡檢 JSON 的出版狀態重新待更新；finalize 後仍沿用本輪資料 SHA 6b61371 的 blocked 結果。補讀與收尾僅作本機 [skip ci] 稽核更新，推送後須以資料 SHA 檢查 matching Actions，並確保稽核 commit 也已推送。
- 工作區其他既有修改未 stage：`ISSUES_REVIEW.md`、`PROJECT_HANDOVER.md`、`patrol_runs/2026-10-16_0300.json`，及三個原有未追蹤檔案均保留。
- 收據更新：`2026-10-18T03:08:30+08:00`（Asia/Taipei）；因尚未推送，本收據為本機接續紀錄，未上線。


## 最終續跑驗收（2026-10-18T08:12:09+08:00 Asia/Taipei）

- 發布解除阻塞：本機網路連線正常，`git push origin 6b61371:main` 成功推送資料提交（`6b61371957343c0110a6e9d63040876638fbf293`）。
- matching Actions：[39081843910](https://github.com/eric1810-tw/taiwan-opera-calendar/actions/runs/39081843910)，event=push，head SHA=`6b61371957343c0110a6e9d63040876638fbf293`，completed/success。
- 規程驗收：`python3 scripts/patrol_progress.py verify --run patrol_runs/2026-10-18_0300.json --sha 6b61371957343c0110a6e9d63040876638fbf293 --actions-run 39081843910` 成功，`publication.state="verified"`，驗證時間 `2026-10-18T08:12:09+08:00`。
- 本地與公開網站（GitHub Pages）三檔 SHA-256 逐位元完全一致：
  - `data/schedule.json`: `2fd2a74b07fb3423df7e0222bbf2f029d90ee92d7777a184c8a3090810a4754f`（卡片數更新為 98 張，已包含明華園《烏龍天下》臺中場與高雄場）
  - `data/metadata.json`: `997d55acc5e86468c7d5b0b6f2f15c13ac7762e6e2af3f8084b602e1974a47cd`（網站資料刷新時間維持 2026-10-17T08:57:55+08:00）
  - `data/patrol_status.json`: `70fcdae5d6ec2fb42e52ff5c5ec1b0853cac1289a6c6c30b060d387e9ddc339f`（公開巡檢狀態為 2026-10-18T00:21:53+08:00 / failed）
- 本輪 JSON 驗收後 SHA-256：`14aaec7193108f72e38b6ceb3c9fb6c82917843b41de4d87ce56c6193f4dc237`。
- 工作區既有未暫存檔案（`ISSUES_REVIEW.md`、`PROJECT_HANDOVER.md`、`patrol_runs/2026-10-16_0300.json`）及未追蹤檔案（`CLAUDE_AUDIT_2026-09-30.md`、`CLOUDFLARE_HANDOVER.md`、`CODEX_TASK_REVIEW_FIXES_2026-09-30.md`）全程完好保留。


## 頁面模型標示與狀態更新驗收（2026-10-18T08:23:48+08:00 Asia/Taipei）

- 依使用者需求更新 `assets/app.js`：取消「（台灣時間；巡檢未完成）」字樣，改為顯示「（由 Gemini 3.8 完成）」。
- `data/patrol_status.json` 加入 `"model": "Gemini 3.8"`；`scripts/patrol_progress.py` 擴充 `finalize --model` 與 `verify` 模型核驗。
- 資料提交 SHA：`1e698ea089f69dbac316a35c56efe10d52548265`（`feat(ui): update patrol label to display model name and include model in status`），已推送至 `origin/main`。
- matching Actions：[39082552771](https://github.com/eric1810-tw/taiwan-opera-calendar/actions/runs/39082552771)，event=push，head SHA=`1e698ea089f69dbac316a35c56efe10d52548265`，completed/success。
- 規程驗收：`python3 scripts/patrol_progress.py verify --run patrol_runs/2026-10-18_0300.json --sha 1e698ea089f69dbac316a35c56efe10d52548265 --actions-run 39082552771` 通過，`publication.state="verified"`。
- 公開 Pages 四檔比對全數完全一致：
  - `data/schedule.json`: `2fd2a74b07fb3423df7e0222bbf2f029d90ee92d7777a184c8a3090810a4754f`（98張）
  - `data/metadata.json`: `997d55acc5e86468c7d5b0b6f2f15c13ac7762e6e2af3f8084b602e1974a47cd`
  - `data/patrol_status.json`: `d0dd509e09c1042b16ad1610fd0a864b318bb5caba0bca83aab56a2a5091f6f2`（含 `"model": "Gemini 3.8"`）
  - `assets/app.js`: `f95e9692884ef1a6c2660cdecddafb6354af06378bf57293a50fd91a096b0824`
- 舊 LaunchAgent `tw.eric.codex-app.prepare.plist` 已 unload 並更名為 `.disabled`，正式由 Antigravity 接管。
