# patrol-v2 切換清單（**等 Eric 批准才執行**）

前提：新舊測試全過、真實資料 dry-run 完成、並行 2–3 晚的影子比對已交 Eric 看過。

## 切換時段

選一天 **05:00–06:30**（agy 03:00 那輪已結束、07:00 Actions 更新器還沒跑）。開始前確認：
- `~/.gemini/antigravity/sidecar_data/daily-opera-patrol/logs/sidecar.log` 當天那輪已結束，`patrol_runs/` 當天的 run 已有 `finalizedAt`。
- 正式資料夾 `git status --short` 只有既存的保留檔與未追蹤檔（6 保留檔 hash 與基準一致）。

## 步驟

1. **備份**
   - `cp ~/.gemini/config/sidecars/daily-opera-patrol/sidecar.json ~/.gemini/config/sidecars/daily-opera-patrol/sidecar.json.bak-YYMMDD`
   - 記錄正式資料夾 `git rev-parse HEAD`（回復用）。
2. **合併**：在 GitHub 開 PR `claude/claude-patrol-rebuild-f0faa6` → `main`，Eric 核准後 merge（不 force、不改歷史）。正式資料夾 `git fetch origin main && git merge --ff-only origin/main`。
3. **驗證合併後的正式資料夾**：`python3 -m unittest -v`、`node --test tests/*.mjs`、`python3 scripts/patrol.py status`。
4. **停用 agy sidecar**：依 Antigravity 官方方式停用 `daily-opera-patrol`（不刪除；sidecar.json 已備份）。確認 sidecar.log 沒有新的排程時間。
5. **建立正式排程**：Claude 桌面版排程任務 `daily-opera-patrol-v2`，`0 3 * * *`，prompt 用 `docs/patrol-v2/SCHEDULED_PROMPT.md`（`{ROOT}`=正式資料夾、`{MODE}`=production），SKILL.md frontmatter 加 `model: sonnet`。
6. **Claude 桌面版加入登入項目**：系統設定 → 一般 → 登入項目 → 加入 Claude（Eric 自己操作；App 沒開時排程會在下次開啟補跑）。
7. **第一次正式執行**：當天手動按「立即執行」一次，或等隔天 03:00；確認報告、收據、同 SHA Actions、公開三檔一致。
8. **刪除影子任務**（若有）。

## 回復方法

1. 停用（不刪）`daily-opera-patrol-v2` 排程任務。
2. 還原 `sidecar.json.bak-YYMMDD` → `sidecar.json`，依 Antigravity 方式重新啟用 sidecar。
3. 程式：新系統的檔案都是新增的（`scripts/patrol.py`、`scripts/patrol_v2/`），agy 用的 `social_reader.mjs` 沒改；`add_card.py` 的改動向下相容（舊用法測試全過）。若仍要退回，用 `git revert <merge commit>` 開 PR，不 reset。
4. 資料：新系統寫入的卡片照常保留；若某張卡有誤，用 add_card 的 change／cancel 修正，不整檔回滾，以免蓋掉之後的新公告。
5. 新系統的本機狀態 `patrol_state/` 不影響 agy，可保留。
