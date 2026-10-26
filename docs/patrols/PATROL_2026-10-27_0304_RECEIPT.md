# 2026-10-27 03:04 巡檢發布驗收收據

- **巡檢識別**：`patrol_runs/2026-10-27_0304.json`
- **巡檢開始**：`2026-10-27T03:05:03+08:00`（Asia/Taipei）
- **發布驗收**：`2026-10-27T03:20:25+08:00`（Asia/Taipei）
- **資料提交 SHA**：[`7f1ef84214c9651754732c944936633c83c1699f`](https://github.com/eric1810-tw/taiwan-opera-calendar/commit/7f1ef84214c9651754732c944936633c83c1699f)
- **GitHub Actions Run**：[Run ID 40385748135](https://github.com/eric1810-tw/taiwan-opera-calendar/actions/runs/40385748135)（Daily Opera Schedule Auto-Updater / push / completed / success）
- **詳細報告**：[`docs/patrols/PATROL_2026-10-27_0304_INDEPENDENT.md`](./PATROL_2026-10-27_0304_INDEPENDENT.md)

---

## 1. 來源覆蓋與資料變更總結

- **來源覆蓋總結**：21 個動態監看來源，最終狀態 2 complete、18 partial、1 failed、0 pending；finalized 狀態依規則判定為 `failed`（`threads:1013.yr_` 重試 4 次後 0 篇）。
- **資料庫卡片變更（本輪共 0 筆新增卡片、0 筆更新）**：
  - 社群與文化部提及之未來演出均已建卡在表，無缺漏或需異動事項。

---

## 2. 公開一致性驗收（`compare-public`）

比對本機與公開 GitHub Pages 端點（`https://eric1810-tw.github.io/taiwan-opera-calendar/`）：
- `data/schedule.json` SHA-256: `67dcabf6447bd0d9042fb4383c6818971f7cf12e79f5b58233cba1289d2e79b6`（MATCH: true）
- `data/patrol_status.json` SHA-256: `fe9354d75d39bc572efc3db66b37adebe614ba72c1b39ad5da6baf26b82fc6bc`（MATCH: true）
- `data/metadata.json` SHA-256: `8a205b48ba12dd698ad3c6f86765fcaa3182825b4962872c4f1532aeb43e1312`（MATCH: true）

---

## 3. 受保護檔案 SHA-256 前 16 碼檢查

嚴格確認未 stage、未修改、未更動：
- `7e551b66ec48c95d  ISSUES_REVIEW.md`
- `f1b2002cdefa74b9  PROJECT_HANDOVER.md`
- `80874b418154dc56  patrol_runs/2026-10-16_0300.json`
- `59259a428dcaffcd  CLAUDE_AUDIT_2026-09-30.md`
- `c2e67dcc180939fd  CLOUDFLARE_HANDOVER.md`
- `459810f13753aa41  CODEX_TASK_REVIEW_FIXES_2026-09-30.md`
