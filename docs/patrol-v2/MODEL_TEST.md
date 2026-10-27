# 排程任務模型設定實測（2026-10-24 23:19）

測試任務 `patrol-v2-model-test`（只能手動執行，測完刪除），以 `mcp__ccd_session_mgmt__get_session` 讀系統回報值，不靠模型自稱。

| 次 | SKILL.md frontmatter | 系統回報 model | 系統回報 effort | 工作目錄 |
|---|---|---|---|---|
| 1 | `model: sonnet`、`effort: low` | `claude-sonnet-5-5` | `medium` | `/Users/eric/aiwork/taiwan-opera-calendar` |
| 2（對照） | 只有 `effort: low` | `claude-opus-5-5` | `medium` | 同上 |

結論：
- **`model: sonnet` 有效**（拿掉就回到預設 Opus）。
- **`effort: low` 沒有效果**，兩次都是 medium。排程工作階段也不能改自己的 effort（App 規定只能由別的工作階段改）。所以每日主流程實際會是 **Sonnet 5.5／medium**，不是規格要的 low。主流程只跑 patrol.py 與派子代理，用量主要在子代理，影響有限；若要 low，只能等 App 支援或另想辦法。
- 排程工作階段的工作目錄是**正式資料夾**（不是 worktree），所以 prompt 一律寫絕對路徑。專案權限清單 `.claude/settings.json` 要在合併到 main 後才會對排程生效。
- 任務建立時沿用本工作階段的 Auto 模式（App 回報），第 1 次執行沒有跳出權限確認。
- 第 1 次執行內容：`pwd` 與 `patrol.py status --mode dry-run`（輸出 `{"run": null}`），無寫入。
