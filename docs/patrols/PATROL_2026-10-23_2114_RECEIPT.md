# 2026-10-23 21:14 巡檢發布驗收收據

- **巡檢識別**：`patrol_runs/2026-10-23_2114.json`
- **巡檢開始**：`2026-10-23T21:15:11+08:00`（Asia/Taipei）
- **發布驗收時間**：`2026-10-23T21:35:21+08:00`（Asia/Taipei）
- **資料提交 SHA**：[`af38779ad5a4c4481c3c7522cfee517417ef09ac`](https://github.com/eric1810-tw/taiwan-opera-calendar/commit/af38779ad5a4c4481c3c7522cfee517417ef09ac)
- **GitHub Actions Run**：[Run ID 39962234913](https://github.com/eric1810-tw/taiwan-opera-calendar/actions/runs/39962234913)（Daily Opera Calendar Update / completed / success）
- **驗收狀態**：`publication.state = "verified"`
- **詳細報告**：[`docs/patrols/PATROL_2026-10-23_2114_INDEPENDENT.md`](./PATROL_2026-10-23_2114_INDEPENDENT.md)

---

## 1. 來源覆蓋與資料變更

- **來源覆蓋總結**：21 個動態監看來源，最終狀態 2 complete、18 partial、1 failed、0 pending；finalized 為 `failed`。
- **資料庫卡片變更**：
  1. `moc-2112035354878472193-f1daf3`：文化部新增《2026金鷹閣電視木偶劇團〈叱吒風雲－新哪吒〉臺中巡演》（2026-11-21 ~ 11-22，臺中市葫蘆墩文化中心演奏廳）。
  2. `auto-20261118-f7e6977b`：社群新增《繡花園戲劇團〈孫臏兵法〉》（2026-11-18，臺南市柳營區東昇里中山西路一段362號 柳營代天院）。

---

## 2. 公開一致性驗收（`compare-public`）

比對本機與公開 GitHub Pages 端點（`https://eric1810-tw.github.io/taiwan-opera-calendar/`）：
- `data/schedule.json` SHA-256: `68a24fab5c3883ab2cbfc3210e910bd946966f0558ef6897e64b0deb2841dfe1`（MATCH: true）
- `data/patrol_status.json` SHA-256: `3733c847fec86d84fbb2648e7764e1f7250be68a608bb4cef617bd68b23c58f5`（MATCH: true）
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
