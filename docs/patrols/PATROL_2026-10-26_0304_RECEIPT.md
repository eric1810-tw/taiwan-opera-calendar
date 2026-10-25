# 2026-10-26 03:04 巡檢發布驗收收據

- **巡檢識別**：`patrol_runs/2026-10-26_0304.json`
- **巡檢開始**：`2026-10-26T03:04:26+08:00`（Asia/Taipei）
- **發布驗收**：`2026-10-26T03:20:48+08:00`（Asia/Taipei）
- **資料提交 SHA**：[`d11a6f5c5fea7ccb85388fac23168cf2b4450bbd`](https://github.com/eric1810-tw/taiwan-opera-calendar/commit/d11a6f5c5fea7ccb85388fac23168cf2b4450bbd)
- **GitHub Actions Run**：[Run ID 40225534171](https://github.com/eric1810-tw/taiwan-opera-calendar/actions/runs/40225534171)（Daily Opera Schedule Auto-Updater / push / completed / success）
- **詳細報告**：[`docs/patrols/PATROL_2026-10-26_0304_INDEPENDENT.md`](./PATROL_2026-10-26_0304_INDEPENDENT.md)

---

## 1. 來源覆蓋與資料變更總結

- **來源覆蓋總結**：21 個動態監看來源，最終狀態 2 complete、18 partial、1 failed、0 pending；finalized 狀態依規則判定為 `failed`（`threads:1013.yr_` 重試 4 次後 0 篇）。
- **資料庫卡片變更（本輪共 0 筆新增卡片、0 筆更新）**：
  - 社群與文化部提及之未來演出均已建卡在表，無缺漏或需異動事項。

---

## 2. 公開一致性驗收（`compare-public`）

比對本機與公開 GitHub Pages 端點（`https://eric1810-tw.github.io/taiwan-opera-calendar/`）：
- `data/schedule.json` SHA-256: `dcc939f031723041695b17d58930e8afd3066f5f32e439a1764d437ad94c164b`（MATCH: true）
- `data/patrol_status.json` SHA-256: `3b95b1eb988fb94cf508bb97201fe92b651411d22d69778d81eda4a0c4661aad`（MATCH: true）
- `data/metadata.json` SHA-256: `64d42b6991f3504a5bad627c4fcdd2c781338fe5e41d9e1b798ee626e056d02b`（MATCH: true）

---

## 3. 受保護檔案 SHA-256 前 16 碼檢查

嚴格確認未 stage、未修改、未更動：
- `7e551b66ec48c95d  ISSUES_REVIEW.md`
- `f1b2002cdefa74b9  PROJECT_HANDOVER.md`
- `80874b418154dc56  patrol_runs/2026-10-16_0300.json`
- `59259a428dcaffcd  CLAUDE_AUDIT_2026-09-30.md`
- `c2e67dcc180939fd  CLOUDFLARE_HANDOVER.md`
- `459810f13753aa41  CODEX_TASK_REVIEW_FIXES_2026-09-30.md`
