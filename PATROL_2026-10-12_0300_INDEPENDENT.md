# 2026-10-12 03:00 獨立巡檢（failed）

## 結果摘要

- 本輪識別：`patrol_runs/2026-10-12_0300.json`；實際開始 `2026-10-12T02:58:14+08:00`（Asia/Taipei）。
- 動態監看清單共 21 項：Threads 10、Facebook 9、文化部 1、GitHub Issues 1。`summary` 無 pending；`finalize` 依工具規則產生 `data/patrol_status.json` 的 `failed`。
- 覆蓋：2 complete（文化部、Issues）、2 partial（孫翠鳳與戲籠出巡 Facebook）、17 failed（其餘 Threads／Facebook）。`failed` 表示社群關鍵來源正文不可讀；不是「沒有新資訊」。

## 來源讀取與故障

- Threads 十個名單均以 Codex In-app Browser 直接開啟個人頁，確認頁面身份標頭可見，但貼文流均停在「載入中……」骨架，未讀貼文正文、近期範圍、分頁或媒體：`joe_huang_k_w`、`h.akito_1996`、`the_rin.lpm`、`1013.yr_`、`xuefeng_lu_`、`yuzhongluo`、`taiwaneseopera168`、`jing__1017`、`hilang.on.tour`、`yolin1991`。第三個同平台帳號仍相同故障後，另開非監看帳號 `@threads` 作共同環境診斷，也呈現相同貼文骨架。以 web reader 替代讀取 `@joe_huang_k_w` 時回報 URL 不可讀；Threads 覆蓋仍 failed。
- Facebook 九個名單均逐一直接開啟：`sunhope.fans`、`HsiaoHsiYuan1913`、`100063868113954`、`MingHuaYuanTianTaiwaneseOpera`、`61574134933376`、`mhysun`、`61594936681482`、`lanyang.opera`、`Taichungpuppettheater`。前五及後兩個頁面只呈現通用殼或持續載入，沒有可讀近期貼文；`mhysun` 與 `61594936681482` 顯示個人頁結構、相片／貼文連結或外部連結，但正文與圖片內容未能讀取，因此僅列 partial。三個帳號相同空白頁面後已檢查 Facebook 共通環境；web reader 對 `sunhope.fans` 的替代讀取遭節流，沒有取得內容。
- 文化部：先依專案既定 TLS 設定執行 `updater.fetch_culture_events()`，受限網路下兩次請求都因 DNS 失敗；In-app Browser 與 web reader 替代路徑分別回報 `ERR_BLOCKED_BY_CLIENT` 與 URL 不可讀。取得核准網路路徑後重試成功，官方 `category=all` 回傳 98 筆；依專案 90 日日期／關鍵字規則抽取 0 個候選，抽查名稱／日期欄位並比對現有排程。既有 `data/moc_candidates.json` 中的三昧堂待核候選不在本次 payload，故保留候選不刪除、不新增場次。沒有放寬 CA 或主機名稱驗證。
- GitHub Issues：`gh issue list --state all --limit 100` 首次因無網路失敗，遂先以公開 Issues 列表和逐筆頁面讀取。網路路徑恢復後重試 all-state API 成功，確認共 2 項、無下一頁：#2、#1 均 open，updated 分別為 2026-09-28 19:57:36Z、19:54:09Z；兩筆 comments 陣列皆空。逐筆核對回報目標、原因、OPENTIX 來源連結及 activity，沒有新留言或需處理的新回報。

每次監看頁面／替代路徑後均以 `patrol_progress.py record` 寫入本輪 JSON，包含來源、方法、公開網址、範圍、媒體狀態及可見錯誤；attempt `at` 是 record 寫入時間，對應緊接在前的觀察，未聲稱瀏覽器精確載入秒數。完整逐次紀錄以 JSON 為準。

## 資料變更

- 未新增或修改演出卡；社群近期內容未讀，文化部本輪篩選沒有產生演出候選，沒有足夠證據核實社群演出、異動或取消。避免以個別官方公告／連結冒充帳號已完整巡檢。
- 本輪未新增／編修演出卡或候選。推送前 fetch 發現遠端自動更新 `718b898`，正常 merge 保留倒數刷新及到期資料清理；最新 `data/metadata.json` 為 `2026-10-11T09:28:30+08:00`，`data/schedule.json` 為 105 筆。這是網站資料刷新時間，與本輪巡檢開始時間分開。

## 驗收與接續

- 狀態檔已 finalize 為 `2026-10-12T02:58:14+08:00 / failed`。本輪資料 commit `cd6bd23073c94141bbc97a4a30ce1c4db8dabd36` 已推送，推送後確認遠端 `main` 精確相符；Actions run `38166376833` 對應相同 SHA，`Daily Opera Schedule Auto-Updater` 已 `completed/success`。`patrol_progress.py verify` 於 `2026-10-12T03:07:29+08:00` 驗證通過；公開 patrol_status、schedule、metadata JSON 均與該 SHA 的資料相同。收據見 `PATROL_2026-10-12_0300_RECEIPT.md`；最終 run JSON、報告與收據另以 audit-only `[skip ci]` commit 保存，不改公開資料。
- 後續恢復請用 `python3 scripts/patrol_progress.py resume --run patrol_runs/2026-10-12_0300.json`，保留原開始時間並逐項重試未能讀取來源。若社群流仍不可讀，先用其他可用公開路徑，記錄每次嘗試；不可把部分可讀寫成無新資訊。
- 驗證：`python3 -m unittest -v`（17 tests PASS）、`node --check assets/app.js`、`git diff --check`、105 筆 schedule required-fields/schema、日期/endDate、unique ID 與三個本輪 JSON parse 均 PASS。遠端自動刷新後重新驗證；patrol status、metadata、候選均不受本輪場次編輯影響。
- SHA256（整合遠端更新後）：schedule `35d0adb1218e6ba1c43cd3ac500433cd6d08dc1b7354336c1f2fd2e6dcc61355`；metadata `b7b88e788be28d9580dde364f8a0bc321b3f3638773f69f3078b3e64380d5b50`；patrol status `1cf98e34678f7b8a076608c6b9578640379b758c7f166039c527d35242726b65`；本輪 JSON（publication receipt 更新後）見收據。
- 驗收收據記錄資料 SHA、Actions run、公開三 JSON 與 SHA256；本輪社群讀取未完成，請接續 resume 同一輪，不能解讀成沒有新場次。
