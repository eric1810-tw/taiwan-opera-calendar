# 2026-10-22 07:09 巡檢發布驗收收據

- **報告檔案**：[`docs/patrols/PATROL_2026-10-22_0709_INDEPENDENT.md`](./PATROL_2026-10-22_0709_INDEPENDENT.md)
- **巡檢識別**：`patrol_runs/2026-10-22_0709.json`
- **開始時間**：`2026-10-22T07:09:15+08:00`
- **最後嘗試**：`2026-10-22T09:34:30+08:00`
- **驗收完成**：`2026-10-22T09:36:48+08:00`
- **巡檢總結**：共 21 個來源（2 complete、18 partial、1 failed、0 pending）。總狀態正確計算為 `failed`。

## 1. 發布與 CI 驗證收據

- **資料提交 SHA**：[`95abd09be1646b08adc8bdeb64f06e3265e0b2b2`](https://github.com/eric1810-tw/taiwan-opera-calendar/commit/95abd09be1646b08adc8bdeb64f06e3265e0b2b2)
- **GitHub Actions Run**：[Run ID 39706630460](https://github.com/eric1810-tw/taiwan-opera-calendar/actions/runs/39706630460)
  - 觸發事件：`push`（head_sha: `95abd09be1646b08adc8bdeb64f06e3265e0b2b2`）
  - 執行結果：`completed` / `success`
  - Job `update-schedule`: 8s, success
  - Job `deploy`: 9s, success
- **驗證工具執行結果**：
  - 指令：`python3 scripts/patrol_progress.py verify --run patrol_runs/2026-10-22_0709.json --sha 95abd09be1646b08adc8bdeb64f06e3265e0b2b2 --actions-run 39706630460`
  - 結果：`publication.state = "verified"`

## 2. 公開檔案逐位元一致性核對

| 檔案名稱 | 本地 SHA-256 | 公開網址 SHA-256 | 比對結果 |
|---|---|---|---|
| `schedule.json` | `b73c242b7ec3f440ea3057ddae75c9973482cb9692ada9c06f7483d5b2376dd5` | `b73c242b7ec3f440ea3057ddae75c9973482cb9692ada9c06f7483d5b2376dd5` | **完全一致** |
| `patrol_status.json` | `229eca45b92d31ec6596cb859935959e4ffc6f3b3c29a066d89f5884cc33f3de` | `229eca45b92d31ec6596cb859935959e4ffc6f3b3c29a066d89f5884cc33f3de` | **完全一致** |
| `metadata.json` | `a14fc180ea06dacf566c1e11aebb09ca84bf60a57dfef6da3295d871ecf60c2d` | `a14fc180ea06dacf566c1e11aebb09ca84bf60a57dfef6da3295d871ecf60c2d` | **完全一致** |

## 3. 公開網站渲染確認

公開狀態檔 `https://eric1810-tw.github.io/taiwan-opera-calendar/data/patrol_status.json` 已更新至本輪，摘要如下：
```json
{
  "startedAt": "2026-10-22T07:09:15+08:00",
  "lastAttemptAt": "2026-10-22T09:34:30+08:00",
  "status": "failed",
  "counts": {
    "complete": 2,
    "partial": 18,
    "failed": 1,
    "pending": 0,
    "total": 21
  }
}
```
確認無任何未經授權的模型名稱標籤，完全忠實反映 21 個來源的真實巡檢覆蓋成果。
