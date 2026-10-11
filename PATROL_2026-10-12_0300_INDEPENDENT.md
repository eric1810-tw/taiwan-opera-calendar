# 2026-10-12 03:00 獨立巡檢（failed）

## 結果摘要

- 本輪識別：`patrol_runs/2026-10-12_0300.json`；實際開始 `2026-10-12T02:58:14+08:00`（Asia/Taipei）。
- 動態監看清單共 21 項：Threads 10、Facebook 9、文化部 1、GitHub Issues 1。`summary` 無 pending；`finalize` 依工具規則產生 `data/patrol_status.json` 的 `failed`。
- 覆蓋：1 complete（Issues）、2 partial（孫翠鳳與戲籠出巡 Facebook）、18 failed（其餘社群及文化部）。`failed` 表示多個關鍵來源正文或文化部資料不可讀；不是「沒有新資訊」。

## 來源讀取與故障

- Threads 十個名單均以 Codex In-app Browser 直接開啟個人頁，確認頁面身份標頭可見，但貼文流均停在「載入中……」骨架，未讀貼文正文、近期範圍、分頁或媒體：`joe_huang_k_w`、`h.akito_1996`、`the_rin.lpm`、`1013.yr_`、`xuefeng_lu_`、`yuzhongluo`、`taiwaneseopera168`、`jing__1017`、`hilang.on.tour`、`yolin1991`。第三個同平台帳號仍相同故障後，另開非監看帳號 `@threads` 作共同環境診斷，也呈現相同貼文骨架。以 web reader 替代讀取 `@joe_huang_k_w` 時回報 URL 不可讀；Threads 覆蓋仍 failed。
- Facebook 九個名單均逐一直接開啟：`sunhope.fans`、`HsiaoHsiYuan1913`、`100063868113954`、`MingHuaYuanTianTaiwaneseOpera`、`61574134933376`、`mhysun`、`61594936681482`、`lanyang.opera`、`Taichungpuppettheater`。前五及後兩個頁面只呈現通用殼或持續載入，沒有可讀近期貼文；`mhysun` 與 `61594936681482` 顯示個人頁結構、相片／貼文連結或外部連結，但正文與圖片內容未能讀取，因此僅列 partial。三個帳號相同空白頁面後已檢查 Facebook 共通環境；web reader 對 `sunhope.fans` 的替代讀取遭節流，沒有取得內容。
- 文化部：先依專案既定 TLS 設定執行 `updater.fetch_culture_events()` 讀取官方 `category=all` API；兩次請求都因 DNS 名稱解析失敗，無資料返回。接著分別嘗試 In-app Browser 與 web reader 開啟同一官方端點，分別遇到 `ERR_BLOCKED_BY_CLIENT` 與 URL 不可讀。未抽候選、未作候選／排程去重，保留既有 `data/moc_candidates.json` 不變。沒有放寬 CA 或主機名稱驗證。
- GitHub Issues：`gh issue list --state all --limit 100` 因連不到 `api.github.com` 失敗，隨即改用公開 Issues 列表與逐筆頁面。完整列表顯示 2 項、按更新時間排序，無下一頁：#2、#1 均 open，分別於 2026-09-29 03:57、03:54 +08 更新。逐筆讀取回報目標、原因、OPENTIX 來源連結、狀態及 activity；兩筆均無新留言或後續 activity，沒有收到需要處理的新回報。

每次監看頁面／替代路徑後均以 `patrol_progress.py record` 寫入本輪 JSON，包含來源、方法、公開網址、範圍、媒體狀態及可見錯誤；attempt `at` 是 record 寫入時間，對應緊接在前的觀察，未聲稱瀏覽器精確載入秒數。完整逐次紀錄以 JSON 為準。

## 資料變更

- 未新增或修改演出卡；社群來源未讀、文化部候選未取回，沒有足夠證據核實演出、異動或取消。避免以個別官方公告／連結冒充帳號已完整巡檢。
- 本輪未新增／編修演出卡或候選。推送前 fetch 發現遠端自動更新 `718b898`，正常 merge 保留倒數刷新及到期資料清理；最新 `data/metadata.json` 為 `2026-10-11T09:28:30+08:00`，`data/schedule.json` 為 105 筆。這是網站資料刷新時間，與本輪巡檢開始時間分開。

## 驗收與接續

- 狀態檔已 finalize 為 `2026-10-12T02:58:14+08:00 / failed`。資料 SHA、push、Actions、公開網站及驗收收據尚待另行確認；目前不能稱已上線。
- 後續恢復請用 `python3 scripts/patrol_progress.py resume --run patrol_runs/2026-10-12_0300.json`，保留原開始時間並逐項重試未能讀取來源。若社群流仍不可讀，先用其他可用公開路徑，記錄每次嘗試；不可把部分可讀寫成無新資訊。
- 驗證：`python3 -m unittest -v`（17 tests PASS）、`node --check assets/app.js`、`git diff --check`、105 筆 schedule required-fields/schema、日期/endDate、unique ID 與三個本輪 JSON parse 均 PASS。遠端自動刷新後重新驗證；patrol status、metadata、候選均不受本輪場次編輯影響。
- SHA256（整合遠端更新後）：schedule `35d0adb1218e6ba1c43cd3ac500433cd6d08dc1b7354336c1f2fd2e6dcc61355`；metadata `b7b88e788be28d9580dde364f8a0bc321b3f3638773f69f3078b3e64380d5b50`；patrol status `1cf98e34678f7b8a076608c6b9578640379b758c7f166039c527d35242726b65`；本輪 JSON `ce4c4599ea1877de14eba2d0cce0ebf29dae36dcfc657ab2aed72b005b389678`。
- GitHub Actions／公開 JSON／驗收收據仍待這個資料提交推送後核對；不能以遠端自動更新的部署代替本輪 status 部署驗收。
