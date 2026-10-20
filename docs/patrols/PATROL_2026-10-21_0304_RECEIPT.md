# 2026-10-21 03:04 巡檢發布驗收收據

- **報告檔案**：[`docs/patrols/PATROL_2026-10-21_0304_INDEPENDENT.md`](./PATROL_2026-10-21_0304_INDEPENDENT.md)
- **巡檢識別**：`patrol_runs/2026-10-21_0304.json`
- **開始時間**：`2026-10-21T03:04:40+08:00`
- **最後嘗試**：`2026-10-21T03:16:22+08:00`
- **驗收完成**：`2026-10-21T03:19:40+08:00`
- **巡檢總結**：共 21 個來源（2 complete、18 partial、1 failed、0 pending）。總狀態正確計算為 `failed`。

## 1. 發布與 CI 驗證收據

- **資料提交 SHA**：[`c3b7bcfd588b09b3d943db0b178b289d11699f86`](https://github.com/eric1810-tw/taiwan-opera-calendar/commit/c3b7bcfd588b09b3d943db0b178b289d11699f86)
- **GitHub Actions Run**：[Run ID 39482406699](https://github.com/eric1810-tw/taiwan-opera-calendar/actions/runs/39482406699)
  - 觸發事件：`push`（head_sha: `c3b7bcfd588b09b3d943db0b178b289d11699f86`）
  - 執行結果：`completed` / `success`
  - Job `update-schedule`: 7s, success
  - Job `deploy`: 11s, success
- **驗證工具執行結果**：
  - 指令：`python3 scripts/patrol_progress.py verify --run patrol_runs/2026-10-21_0304.json --sha c3b7bcfd588b09b3d943db0b178b289d11699f86 --actions-run 39482406699`
  - 結果：`publication.state = "verified"`

## 2. 公開檔案逐位元一致性核對

| 檔案名稱 | 本地 SHA-256 | 公開網址 SHA-256 | 比對結果 |
|---|---|---|---|
| `schedule.json` | `b05299d001de93e43632cdaf3480e6fd8a318fdd267eb4b474aced3f2eb70f7f` | `b05299d001de93e43632cdaf3480e6fd8a318fdd267eb4b474aced3f2eb70f7f` | **完全一致** |
| `patrol_status.json` | `ed4e9341dc4aab24c546c576ddbcca3749af18c9a326a44d107249c0b53b0b1a` | `ed4e9341dc4aab24c546c576ddbcca3749af18c9a326a44d107249c0b53b0b1a` | **完全一致** |
| `metadata.json` | `e2dde36ff97339222b4b53e1b674c91f7281196f72edb85c1f775c549f231ff4` | `e2dde36ff97339222b4b53e1b674c91f7281196f72edb85c1f775c549f231ff4` | **完全一致** |

## 3. 公開網站渲染確認

公開狀態檔 `https://eric1810-tw.github.io/taiwan-opera-calendar/data/patrol_status.json` 已更新至本輪，摘要如下：
```json
{
  "startedAt": "2026-10-21T03:04:40+08:00",
  "lastAttemptAt": "2026-10-21T03:16:22+08:00",
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
