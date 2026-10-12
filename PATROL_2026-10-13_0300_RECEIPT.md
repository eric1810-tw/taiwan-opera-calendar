# 2026-10-13 03:00 巡檢發布驗收收據

- 巡檢範圍：21 個動態目標。最終來源覆蓋為 19 partial（Threads 10、Facebook 9）、文化部 failed、Issues complete；公開巡檢狀態 `failed`。資料覆蓋結果與部署狀態分開判定。
- 巡檢開始：`2026-10-13T03:02:41+08:00`。本輪 JSON：`patrol_runs/2026-10-13_0300.json`；每次操作時間由 JSON 的 attempt `at` 記錄。初次草稿中的部分自由文字時間已移除，保留工具自動產生的精確時間欄位。
- 資料提交 SHA：`c5b66e437661ecc54450fd08d5fbb1a3fd8b8e39`，推送至 `main`。此 SHA 對應 [GitHub Actions run 38297227559](https://github.com/eric1810-tw/taiwan-opera-calendar/actions/runs/38297227559)，workflow `.github/workflows/daily-update.yml`，`completed/success`；`update-schedule` 與 Pages `deploy` 皆成功。
- `python3 scripts/patrol_progress.py verify --run patrol_runs/2026-10-13_0300.json --sha c5b66e437661ecc54450fd08d5fbb1a3fd8b8e39 --actions-run 38297227559` 於 `2026-10-13T03:23:16+08:00` 成功。公開 [`patrol_status.json`](https://eric1810-tw.github.io/taiwan-opera-calendar/data/patrol_status.json) 回傳 `{"startedAt":"2026-10-13T03:02:41+08:00","status":"failed"}`，與本輪狀態一致。
- 公開資料未改動場次或 metadata；`schedule.json` 97 筆 SHA256：`f2029bc1eff74e7e3c29e3987fc905bcbfa248432eb6678bdbafc2921b911647`；`metadata.json` SHA256：`6e3b182fe2b8bfe7083fd4f18d3f6502e26ea08cbbce3268eda2b5e306ab3e0b`；`patrol_status.json` SHA256：`6c03b175ce68012e570d303c092304576dbbb452a476023698c8376c4f9ee72c`。
- 最終已驗收的本輪 JSON SHA256：`d16922225b84ca1426cf1f56ee2e589f27214c6395e6ec479539eac55f1521af`。
- 本地檢查：17 個 unittest PASS；`node --check assets/app.js`、`git diff --check`、97 筆 schedule schema／唯一 ID／日期／endDate 檢查皆 PASS。
- 收據及 verify 更新後的巡檢 JSON 將以獨立 `[skip ci]` 稽核提交保存，避免不必要地再觸發部署。當前待續項目是 culture category=all API 及 19 個社群帳號的未完整正文／媒體；需以 `resume --run patrol_runs/2026-10-13_0300.json` 接續，不可把 partial 寫成無新資訊。
