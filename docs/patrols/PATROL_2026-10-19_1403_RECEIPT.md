# 2026-10-19 14:03 巡檢發布驗收收據

- **報告檔案**：[`docs/patrols/PATROL_2026-10-19_1403_INDEPENDENT.md`](./PATROL_2026-10-19_1403_INDEPENDENT.md)
- **巡檢識別**：`patrol_runs/2026-10-19_1403.json`
- **開始時間**：`2026-10-19T14:04:25+08:00`
- **最後嘗試**：`2026-10-19T14:18:53+08:00`
- **驗收完成**：`2026-10-19T14:21:55+08:00`
- **巡檢總結**：共 21 個來源（2 complete、17 partial、2 failed、0 pending）。總狀態正確計算為 `failed`。

## 1. 發布與 CI 驗證收據

- **資料提交 SHA**：[`893046bd90d94e9de05555ffa896588d63b7ce2b`](https://github.com/eric1810-tw/taiwan-opera-calendar/commit/893046bd90d94e9de05555ffa896588d63b7ce2b)
- **GitHub Actions Run**：[Run ID 39209357537](https://github.com/eric1810-tw/taiwan-opera-calendar/actions/runs/39209357537)
  - 觸發事件：`push`（head_sha: `893046bd90d94e9de05555ffa896588d63b7ce2b`）
  - 執行結果：`completed` / `success`
  - Job `update-schedule`: 7s, success
  - Job `deploy`: 10s, success
- **驗證工具執行結果**：
  - 指令：`python3 scripts/patrol_progress.py verify --run patrol_runs/2026-10-19_1403.json --sha 893046bd90d94e9de05555ffa896588d63b7ce2b --actions-run 39209357537`
  - 結果：`publication.state = "verified"`

## 2. 公開檔案逐位元一致性核對

| 檔案名稱 | 本地 SHA-256 | 公開網址 SHA-256 | 比對結果 |
|---|---|---|---|
| `schedule.json` | `973e0c034945da9b5f58c734dc386d34e6f4aa4b61132dd0e2f5ff57a2fb6e98` | `973e0c034945da9b5f58c734dc386d34e6f4aa4b61132dd0e2f5ff57a2fb6e98` | **完全一致** |
| `patrol_status.json` | `86127be5154316d3e33b6680a6c0c2738682054ff8e7bfa511a54728fce89fb7` | `86127be5154316d3e33b6680a6c0c2738682054ff8e7bfa511a54728fce89fb7` | **完全一致** |
| `metadata.json` | `6b3cf329b4caff249b52fc45127b200605791124f36a66e29b3e04e485040d1b` | `6b3cf329b4caff249b52fc45127b200605791124f36a66e29b3e04e485040d1b` | **完全一致** |

## 3. 公開網站渲染確認

以無頭 Microsoft Edge 瀏覽器載入公開首頁 `https://eric1810-tw.github.io/taiwan-opera-calendar/`，狀態列顯示文字確認如下：
```text
社群資訊最近巡檢：2026/10/19 14:18（21 個來源：2 完整・17 部分・2 失敗）
```
上方文字確認無任何未經授權的模型名稱標籤，完全忠實反映 21 個來源的真實巡檢覆蓋成果。
