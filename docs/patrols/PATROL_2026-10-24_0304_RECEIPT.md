# 2026-10-24 03:04 巡檢發布驗收收據

- **巡檢識別**：`patrol_runs/2026-10-24_0304.json`
- **巡檢開始**：`2026-10-24T03:04:26+08:00`（Asia/Taipei）
- **發布驗收**：`2026-10-24T03:22:32+08:00`（Asia/Taipei）
- **資料提交 SHA**：[`623f9b56f338fde18e65504176dfa841d251e7b5`](https://github.com/eric1810-tw/taiwan-opera-calendar/commit/623f9b56f338fde18e65504176dfa841d251e7b5)
- **GitHub Actions Run**：[Run ID 40010826726](https://github.com/eric1810-tw/taiwan-opera-calendar/actions/runs/40010826726)（Daily Opera Schedule Auto-Updater / completed / success）
- **詳細報告**：[`docs/patrols/PATROL_2026-10-24_0304_INDEPENDENT.md`](./PATROL_2026-10-24_0304_INDEPENDENT.md)

---

## 1. 來源覆蓋與資料變更總結

- **來源覆蓋總結**：21 個動態監看來源，最終狀態 2 complete、18 partial、1 failed、0 pending；finalized 狀態為 `failed`。
- **資料庫卡片變更（本輪共 2 筆新增卡片）**：
  1. `moc-2088104133013299200-dec93f`：文化部開放資料新增《偶偶偶劇團〈小狐狸買手套〉》（2026-12-04 ~ 12-06，臺北市文山劇場）。
  2. `auto-20261024-5717b6a3`：社群新增《新吉義林歌劇團 演出資訊》（2026-10-24，雲林四湖參天宮廣場，時間：未公布）。

---

## 2. 公開一致性驗收（`compare-public`）

比對本機與公開 GitHub Pages 端點（`https://eric1810-tw.github.io/taiwan-opera-calendar/`）：
- `data/schedule.json` SHA-256: `38451186703c092ab9ddbbace5b836032122e9e1a28c01a7f06b2f5c9f71e14f`（MATCH: true）
- `data/patrol_status.json` SHA-256: `43e1863d36b37e487f2133e52dec598d6e76c6fb914ec4dd2f9e569f9b205258`（MATCH: true）
- `data/metadata.json` SHA-256: `950100068bdbe3fe53dfa9c2d0184cd0496a2640b867a1b876f895545d478166`（MATCH: true）

---

## 3. 受保護檔案 SHA-256 前 16 碼檢查

嚴格確認未 stage、未修改、未更動：
- `7e551b66ec48c95d  ISSUES_REVIEW.md`
- `f1b2002cdefa74b9  PROJECT_HANDOVER.md`
- `80874b418154dc56  patrol_runs/2026-10-16_0300.json`
- `59259a428dcaffcd  CLAUDE_AUDIT_2026-09-30.md`
- `c2e67dcc180939fd  CLOUDFLARE_HANDOVER.md`
- `459810f13753aa41  CODEX_TASK_REVIEW_FIXES_2026-09-30.md`
