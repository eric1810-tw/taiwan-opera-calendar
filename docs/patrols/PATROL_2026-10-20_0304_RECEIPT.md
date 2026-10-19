# 2026-10-20 03:04 巡檢發布驗收收據

- **報告檔案**：[`docs/patrols/PATROL_2026-10-20_0304_INDEPENDENT.md`](./PATROL_2026-10-20_0304_INDEPENDENT.md)
- **巡檢識別**：`patrol_runs/2026-10-20_0304.json`
- **開始時間**：`2026-10-20T03:04:44+08:00`
- **最後嘗試**：`2026-10-20T03:19:24+08:00`
- **驗收完成**：`2026-10-20T03:28:35+08:00`
- **巡檢總結**：共 21 個來源（1 complete、19 partial、1 failed、0 pending）。總狀態正確計算為 `failed`。

## 1. 發布與 CI 驗證收據

- **資料提交 SHA**：[`790763e5bd978b55b7287b5a4dfb4a5e7863380c`](https://github.com/eric1810-tw/taiwan-opera-calendar/commit/790763e5bd978b55b7287b5a4dfb4a5e7863380c)
- **GitHub Actions Run**：[Run ID 39311117711](https://github.com/eric1810-tw/taiwan-opera-calendar/actions/runs/39311117711)
  - 觸發事件：`push`（head_sha: `790763e5bd978b55b7287b5a4dfb4a5e7863380c`）
  - 執行結果：`completed` / `success`
  - Job `update-schedule`: 19s, success
  - Job `deploy`: 9s, success
- **驗證工具執行結果**：
  - 指令：`python3 scripts/patrol_progress.py verify --run patrol_runs/2026-10-20_0304.json --sha 790763e5bd978b55b7287b5a4dfb4a5e7863380c --actions-run 39311117711`
  - 結果：`publication.state = "verified"`

## 2. 公開檔案逐位元一致性核對

| 檔案名稱 | 本地 SHA-256 | 公開網址 SHA-256 | 比對結果 |
|---|---|---|---|
| `schedule.json` | `7941aba066a0cff3d5d329d80a67d4bb763bf37a24dc848891e229254d29175a` | `7941aba066a0cff3d5d329d80a67d4bb763bf37a24dc848891e229254d29175a` | **完全一致** |
| `patrol_status.json` | `a486d2da2c8c0138799e6a2b46098f94a16b04b416e251fd82293918d311b567` | `a486d2da2c8c0138799e6a2b46098f94a16b04b416e251fd82293918d311b567` | **完全一致** |
| `metadata.json` | `6b3cf329b4caff249b52fc45127b200605791124f36a66e29b3e04e485040d1b` | `6b3cf329b4caff249b52fc45127b200605791124f36a66e29b3e04e485040d1b` | **完全一致** |

## 3. 公開網站渲染確認

公開狀態檔 `https://eric1810-tw.github.io/taiwan-opera-calendar/data/patrol_status.json` 已更新至本輪，摘要如下：
```json
{
  "startedAt": "2026-10-20T03:04:44+08:00",
  "lastAttemptAt": "2026-10-20T03:19:24+08:00",
  "status": "failed",
  "counts": {
    "complete": 1,
    "partial": 19,
    "failed": 1,
    "pending": 0,
    "total": 21
  }
}
```
確認無任何未經授權的模型名稱標籤，完全忠實反映 21 個來源的真實巡檢覆蓋成果。
