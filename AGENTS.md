# 臺灣戲曲情報站：代理人作業守則 (AGENTS.md)

1. **環境與語言**：工作目錄為 `/Users/eric/aiwork/taiwan-opera-calendar`；時區一律為 `Asia/Taipei`（時間標記帶 `+08:00`）；所有思考、回答、回報一律使用**臺灣繁體中文（zh-TW）**。
2. **6 個受保護檔案（嚴禁更動）**：`ISSUES_REVIEW.md`、`PROJECT_HANDOVER.md`、`patrol_runs/2026-10-16_0300.json`、`CLAUDE_AUDIT_2026-09-30.md`、`CLOUDFLARE_HANDOVER.md`、`CODEX_TASK_REVIEW_FIXES_2026-09-30.md`。嚴禁 stage、修改、移動或刪除。
3. **禁用 Git 指令**：嚴禁 `git add .`、`git add -A`、`git reset --hard`、`git stash`、`git push --force`、`git clean`。提交時一律逐檔指定。
4. **事實查核與建卡底線**：卡片事實欄位（日期、時間、場館、地址、票價、主演）必須有官方原文逐字片段為證；未知欄位寫「未公布」或「請查官方公告」；社群來源一律標註 community；自動候選不得自動發布為正式卡片。
5. **即時記錄與重試規範**：每次讀完來源必須**立即**執行 `record`，嚴禁事後批次補寫；失敗時最多重試 3 次，每次必須切換讀取路徑（重新載入→原帖直連→未登入模式），且每次嘗試皆須記錄。
6. **誠實標示模型**：不可宣稱未經驗證之模型名稱；finalize 巡檢輪時不帶 `--model`（模型由外層驗證或留空）。
7. **上線驗收標準**：資料提交必須推送至 `origin/main`；對應 HEAD SHA 的 GitHub Actions 必須執行成功（success）；公開 3 個 JSON（`schedule.json`、`patrol_status.json`、`metadata.json`）必須與本機逐位元一致。
8. **標準規程優先**：開始任何巡檢作業前，必須完整閱讀並嚴格遵守 `PATROL_OPERATIONS.md`。
