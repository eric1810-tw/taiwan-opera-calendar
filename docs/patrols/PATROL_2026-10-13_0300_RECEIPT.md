# 2026-10-13 03:00 巡檢發布驗收收據

- 巡檢範圍：21 個動態目標。恢復後最終覆蓋為 19 partial（Threads 10、Facebook 9）、文化部 complete、Issues complete；公開巡檢狀態 `partial`。資料覆蓋結果與部署狀態分開判定。
- 巡檢開始：`2026-10-13T03:02:41+08:00`。本輪 JSON：`patrol_runs/2026-10-13_0300.json`；每次操作時間由 JSON 的 attempt `at` 記錄。初次草稿中的部分自由文字時間已移除，保留工具自動產生的精確時間欄位。
- 初次發布資料提交 SHA：`c5b66e437661ecc54450fd08d5fbb1a3fd8b8e39`，推送至 `main`。此 SHA 對應 [GitHub Actions run 38297227559](https://github.com/eric1810-tw/taiwan-opera-calendar/actions/runs/38297227559)，workflow `.github/workflows/daily-update.yml`，`completed/success`；`update-schedule` 與 Pages `deploy` 皆成功。
- 初次 `verify` 於 `2026-10-13T03:23:16+08:00` 成功；當時公開狀態為 `failed`。同日恢復後已重新 finalize、部署並在下方記錄最終 `partial` 驗證。
- 初次資料提交時，公開場次與 metadata 未因巡檢改動；`schedule.json` 97 筆 SHA256：`f2029bc1eff74e7e3c29e3987fc905bcbfa248432eb6678bdbafc2921b911647`；`metadata.json` SHA256：`6e3b182fe2b8bfe7083fd4f18d3f6502e26ea08cbbce3268eda2b5e306ab3e0b`；`patrol_status.json` SHA256：`6c03b175ce68012e570d303c092304576dbbb452a476023698c8376c4f9ee72c`。
- 初次驗收時本輪 JSON SHA256：`d16922225b84ca1426cf1f56ee2e589f27214c6395e6ec479539eac55f1521af`；恢復後最終 SHA 見下方。
- 初次本地檢查：17 個 unittest PASS；`node --check assets/app.js`、`git diff --check`、當時 97 張 schedule schema／唯一 ID／日期／endDate 檢查皆 PASS。恢復後 96 張版本再次通過，記於下方。
- 初次收據保存時的待續項目為 culture API 與社群內容；恢復後 culture 已 complete，19 個社群帳號仍 partial。最終 verify 更新的巡檢 JSON 與本收據會以獨立 `[skip ci]` 稽核提交保存。


## 恢復後驗收（2026-10-13 22:39 Asia/Taipei）

- 以同一 JSON `resume`，保留原開始時間。Culture API 已恢復讀取：HTTP 200、1,578 筆；90日內 32 筆戲曲場次，31 筆對應既有正式卡，三昧堂 2027-01-01 候選保留 pending。社群來源未全部恢復完整，19 個帳號仍 partial；恢復期間新增逐筆記錄於本輪 JSON。
- 恢復後狀態 `partial`。資料部署 SHA `a76492999fe17e5871baa3156092a2df3cb00d34` 對應 [Actions 38415095773](https://github.com/eric1810-tw/taiwan-opera-calendar/actions/runs/38415095773)，`completed/success`；update-schedule 測試與 Pages deploy 成功。
- `patrol_progress.py verify` 於 `2026-10-13T22:39:15+08:00` 成功；公開狀態回傳 `startedAt=2026-10-13T03:02:41+08:00`、`status=partial`。
- 已合併遠端每日自動更新 `6c914d2`：已過期 10/10 九天堂卡移除，排程 97→96 張，metadata 更新至 `2026-10-13T11:18:52+08:00`。本輪無新增場次。
- SHA256：schedule `6640702ab0f9500327dd923a9d19ccbee6367936be140f0d4d3cbfada1cf6371`；metadata `1557c7f2c058e52e1e7ed6242c4e828032428f5b5146f976fb89d9f43357e1f2`；patrol_status `1f31c0305e14451823be92db14c165389f2109a55e8501c07cd62725d567a1e1`；本輪 JSON `c0e65e255a7091723a8e25f33efbca94098a317b6042f8166e92ca40c5f28c9d`。
- 恢復後 17 tests、JS syntax、git diff check 與 96 張排程 schema/date/endDate/unique ID 檢查均通過。
