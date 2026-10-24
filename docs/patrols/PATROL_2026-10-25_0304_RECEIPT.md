# 2026-10-25 03:04 巡檢發布驗收收據

- **巡檢識別**：`patrol_runs/2026-10-25_0304.json`
- **巡檢開始**：`2026-10-25T03:04:31+08:00`（Asia/Taipei）
- **發布驗收**：`2026-10-25T03:22:55+08:00`（Asia/Taipei）
- **資料提交 SHA**：[`3ec579cefa757553c7c899ae01aa246651f9d7dd`](https://github.com/eric1810-tw/taiwan-opera-calendar/commit/3ec579cefa757553c7c899ae01aa246651f9d7dd)
- **GitHub Actions Run**：[Run ID 40124969910](https://github.com/eric1810-tw/taiwan-opera-calendar/actions/runs/40124969910)（Daily Opera Schedule Auto-Updater / completed / success）
- **詳細報告**：[`docs/patrols/PATROL_2026-10-25_0304_INDEPENDENT.md`](./PATROL_2026-10-25_0304_INDEPENDENT.md)

---

## 1. 來源覆蓋與資料變更總結

- **來源覆蓋總結**：21 個動態監看來源，最終狀態 2 complete、18 partial、1 failed、0 pending；finalized 狀態為 `failed`（`threads:1013.yr_` 重試 4 次後 0 篇）。
- **資料庫卡片變更（本輪共 1 筆新增卡片）**：
  1. `moc-2110369335028596737-8ddf63`：文化部開放資料新增《吟遊詩人的新唸歌——桃園米倉》（2026-12-18 ~ 12-20，米倉劇場，OPENTIX 售票）。

---

## 2. 公開一致性驗收（`compare-public`）

比對本機與公開 GitHub Pages 端點（`https://eric1810-tw.github.io/taiwan-opera-calendar/`）：
- `data/schedule.json` SHA-256: `67c8bea4075232c571a2991cfe55e887c5524189f07a2514fa1fc307a398d05e`（MATCH: true）
- `data/patrol_status.json` SHA-256: `92f95b3daf23620e4617f139e1566f350e5aff564bbda2e9a83c9d7fedd01037`（MATCH: true）
- `data/metadata.json` SHA-256: `9a21057fa8271192e0a61383b85bcd179616998f8e597895eedd481bd541710b`（MATCH: true）

---

## 3. 受保護檔案 SHA-256 前 16 碼檢查

嚴格確認未 stage、未修改、未更動：
- `7e551b66ec48c95d  ISSUES_REVIEW.md`
- `f1b2002cdefa74b9  PROJECT_HANDOVER.md`
- `80874b418154dc56  patrol_runs/2026-10-16_0300.json`
- `59259a428dcaffcd  CLAUDE_AUDIT_2026-09-30.md`
- `c2e67dcc180939fd  CLOUDFLARE_HANDOVER.md`
- `459810f13753aa41  CODEX_TASK_REVIEW_FIXES_2026-09-30.md`
