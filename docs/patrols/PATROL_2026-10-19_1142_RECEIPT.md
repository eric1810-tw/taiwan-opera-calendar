# 2026-10-19 11:42 巡檢發布驗收收據

- **報告檔案**：[`docs/patrols/PATROL_2026-10-19_1142_INDEPENDENT.md`](./PATROL_2026-10-19_1142_INDEPENDENT.md)
- **巡檢識別**：`patrol_runs/2026-10-19_1142.json`
- **開始時間**：`2026-10-19T11:42:45+08:00`
- **最後嘗試**：`2026-10-19T11:48:45+08:00`
- **驗收完成**：`2026-10-19T11:52:09+08:00`
- **巡檢總結**：共 21 個來源（1 complete、20 partial、0 failed、0 pending）。總狀態正確計算為 `partial`。

## 1. 發布與 CI 驗證收據

- **資料提交 SHA**：[`c7871a164f1a0c3cd3c7eadd0ed4877346d6d55e`](https://github.com/eric1810-tw/taiwan-opera-calendar/commit/c7871a164f1a0c3cd3c7eadd0ed4877346d6d55e)
- **GitHub Actions Run**：[Run ID 39196599326](https://github.com/eric1810-tw/taiwan-opera-calendar/actions/runs/39196599326)
  - 觸發事件：`push`（head_sha: `c7871a164f1a0c3cd3c7eadd0ed4877346d6d55e`）
  - 執行結果：`completed` / `success`
  - Job `update-schedule`: 7s, success
  - Job `deploy`: 9s, success
- **驗證工具執行結果**：
  - 指令：`python3 scripts/patrol_progress.py verify --run patrol_runs/2026-10-19_1142.json --sha c7871a164f1a0c3cd3c7eadd0ed4877346d6d55e --actions-run 39196599326`
  - 結果：`publication.state = "verified"`

## 2. 公開檔案逐位元一致性核對

| 檔案名稱 | 本地 SHA-256 | 公開網址 SHA-256 | 比對結果 |
|---|---|---|---|
| `schedule.json` | `50c3573a068d1c9af205d4abfcf1f69f2832cdcafa93b6007af668207c194a65` | `50c3573a068d1c9af205d4abfcf1f69f2832cdcafa93b6007af668207c194a65` | **完全一致** |
| `patrol_status.json` | `cef5b8dcd53866367199d3cb81a44c074c7c98c442e25bc7ac169b3b5f76c344` | `cef5b8dcd53866367199d3cb81a44c074c7c98c442e25bc7ac169b3b5f76c344` | **完全一致** |
| `metadata.json` | `6b3cf329b4caff249b52fc45127b200605791124f36a66e29b3e04e485040d1b` | `6b3cf329b4caff249b52fc45127b200605791124f36a66e29b3e04e485040d1b` | **完全一致** |

## 3. 公開網站渲染確認

以無頭 Microsoft Edge 瀏覽器載入公開首頁 `https://eric1810-tw.github.io/taiwan-opera-calendar/`，狀態列顯示文字確認如下：
```text
社群資訊最近巡檢：2026/10/19 11:48（21 個來源：1 完整・20 部分・0 失敗）
```
上方文字確認無任何未經授權的模型名稱標籤，完全忠實反映 21 個來源的真實巡檢覆蓋成果。

---

## 4. 2026-10-19 13:30 覆查更正收據

- **更正資料提交 SHA**：[`bd3c53832c00944db7e096178d814f87de7e554a`](https://github.com/eric1810-tw/taiwan-opera-calendar/commit/bd3c53832c00944db7e096178d814f87de7e554a)
- **GitHub Actions Run**：[Run ID 39204882361](https://github.com/eric1810-tw/taiwan-opera-calendar/actions/runs/39204882361)（push / success）
- **公開驗收指令**：`python3 scripts/patrol_progress.py verify --run patrol_runs/2026-10-19_1142.json --sha bd3c53832c00944db7e096178d814f87de7e554a --actions-run 39204882361`
- **驗收結果**：`publication.state = "verified"`
- **更正後公開顯示**：
```text
社群資訊最近巡檢：2026/10/19 13:28（21 個來源：1 完整・1 部分・19 失敗）
```

