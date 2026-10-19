# 臺灣戲曲網站巡檢交接與操作

本文件是排程和新工作階段的操作入口；即時狀態以檔案及公開網站為準，不沿用文件中舊的場次數。時區一律為 Asia/Taipei（時間戳記帶 `+08:00`）。

## 工作分界

- 獨立 Antigravity sidecar 排程 `daily-opera-patrol` 每日 03:00（Asia/Taipei，每天一次）巡檢公開 Threads、Facebook、文化部候選及 GitHub Issues，經來源核對才編修正式場次。每輪留下巡檢紀錄與 `data/patrol_status.json`，並嘗試推送、驗證公開站。
- GitHub Actions `.github/workflows/daily-update.yml` 呼叫 `updater.py`，處理候選、倒數、metadata、過期場次及部署。它不是社群貼文語意審核員；不得將自動候選當成已核實演出。
- `data/schedule.json` 是公開場次；`data/metadata.json` 是網站資料刷新時間；`data/patrol_status.json` 是社群巡檢最新嘗試時間、覆蓋數量及完成程度。三者不可混稱。

## 每輪巡檢

1. 記錄實際開始時間（含 `+08:00`）。從 `data/threads_accounts.json`、`data/facebook_accounts.json` 動態讀取完整監看名單，使用巡檢專用瀏覽器設定檔查看近期公開貼文及圖片戲路表；檢視文化部開放資料。無法讀取或只能讀一部分時，記下實際範圍，不可推斷「沒有新資訊」。
2. 抽取今天、明天及未來演出的日期、時間、劇團、劇目、場地與原始連結。與 `data/schedule.json` 依日期、場地、劇團及劇目核對重複；查原始劇團、主辦、售票及文化部公告，並查異動或取消。未核實的保留候選或稽核紀錄，不當確定場次發布。社群原始公告依 `community` 分類，不因它是劇團貼文就改標 `verified`；同場保留一張卡及所有來源連結。
3. 巡檢儲存庫 [全部 Issues](https://github.com/eric1810-tw/taiwan-opera-calendar/issues?q=is%3Aissue+sort%3Aupdated-desc)（新建、留言、重開、關閉），按更新時間排序，排除 Pull Requests。API 不通改用公開瀏覽器；仍不可讀就記失敗。收到回報先查原始公告及現有場次，依 `ISSUES_REVIEW.md` 留證據與處理結果。
4. 記錄本輪來源、比對、未解線索及失敗範圍。巡檢報告與發布收據統一存放於 `docs/patrols/` 目錄。更新 `data/patrol_status.json`：動態計算 `lastAttemptAt`（attempts 最大時間）與 `counts`（包含 complete、partial、failed、pending 與 total）。所有目標近期公開內容及 Issues 均讀完才用 `complete`；任一來源部分可讀、圖片不清或範圍不足用 `partial`；關鍵來源無法讀或巡檢未完成用 `failed`。不為更新時間捏造場次。
5. 只在證據足夠時改 `data/schedule.json`；執行 `python3 -m unittest -v`、`node --check assets/app.js`、`git diff --check`，檢查 schema、日期、去重及頁面。僅提交本輪檔案，保留其他人的工作區修改。每輪把巡檢紀錄與狀態檔推送；確認 GitHub Actions 結果、[公開站狀態檔](https://eric1810-tw.github.io/taiwan-opera-calendar/data/patrol_status.json) 的時間與狀態。推送或部署不通則保留本地並明示未上線。

## 執行與恢復規則（2026-10-19 起）

日常排程由 Antigravity sidecar `daily-opera-patrol` 執行。模型標示遵循「未驗證不標示」原則：未提供 `--model-evidence` 時不宣稱任何模型名稱，finalize 時不帶 `--model` 參數。

### 1. 開始即建立可續跑清單

- 先保存 `git status --short` 與 staged 檔案清單，辨識既有修改；嚴格禁用 `git add .`。一次只執行一輪，避免兩輪覆寫 `patrol_status.json`。
- 執行 `python3 scripts/patrol_progress.py init --run patrol_runs/<本輪識別>.json`。工具照實記錄開始時間，動態建立 Threads、Facebook、文化部、Issues 的全部目標。使用實際開始時間的檔名（如 `YYYY-MM-DD_HHMM.json`），不回填排程時間。
- 每個目標都須留下結果。先走完全部目標的初次讀取，再處理未完成項目；單一頁面失敗不能讓其他目標停擺。
- 中斷後以 `resume --run <原檔>` 接續同一輪。**已 verified 的 run 必須帶 `--reason` 說明原因方可 resume**，工具保留原開始時間與歷次嘗試，將舊發布資訊封存至 `publicationHistory`，另記恢復時間並同步新名單。

### 2. 記錄讀取證據與範圍

每次操作後使用 `record` 存檔。成功也必須記錄日期範圍、貼文範圍、圖片核對結果及來源網址；首頁帳號名稱、貼文容器、搜尋摘要或單篇可讀不等於近期內容已讀完。預設讀取最近 7 天，另核對仍有效的置頂／月份戲路公告；遇到分頁或更早公告包含未來演出時繼續追查。圖片不存在才能使用 `not_applicable`，並在 detail 說明；圖片打不開屬未讀。

```sh
python3 scripts/patrol_progress.py record --run <原檔> \
  --source threads:joe_huang_k_w --state partial --method profile-browser \
  --url https://www.threads.com/@joe_huang_k_w \
  --scope '最近7天只讀到一篇；其他貼文仍載入中' --media unread \
  --detail '正文局部可讀，海報無法開啟；尚未完成帳號覆蓋'
```

- `--source` 的鍵以 `summary --run <原檔>` 列出的完整清單為準。讀不到正文用 `failed`；正文或媒體局部可讀用 `partial`；全部範圍讀完才用 `complete`。
- **巡檢專用瀏覽器設定檔與社群讀取（CDP）**：
  - 獨立設定檔目錄一律為 `--user-data-dir=/Users/eric/.patrol-edge`（舊目錄 `~/.patrol-browser-profile` 保留不動不刪除）。
  - 嚴禁使用 `puppeteer.launch()`、`playwright`，只能用 `child_process.spawn` 直接啟動 Edge，啟動參數固定為：`--headless=new`、`--remote-debugging-port=<port>`、`--user-data-dir=/Users/eric/.patrol-edge`、`--lang=zh-TW`、`--no-first-run`、`--no-default-browser-check`、`--window-size=1280,2000`、`about:blank`。
  - 嚴禁使用 `--use-mock-keychain`、`--password-store=basic`、`--no-sandbox`、`--disable-setuid-sandbox`，禁止修改 User-Agent。
  - 執行 `node scripts/social_reader.mjs --run <原檔> --out patrol_evidence/<本輪>/` 逐來源擷取貼文並即時 `record`，狀態由純函式判定（永遠不判 `complete`，有貼文記 `partial`，0 篇記 `failed`）。嚴禁讀取或輸出 cookie、密碼、資料檔；登入態以頁面實際有無登入牆為準。

- **文化部開放資料原生函式**：使用 `python3 -c "import updater; ..."` 匯入 `updater.fetch_culture_events()` 與 `updater.culture_candidates()` 唯讀執行，不執行 updater 主流程、不覆寫檔案。若回傳筆數小於 500 筆門檻（`MIN_CULTURE_RECORDS`），記為 `partial`，並註明「讀取不完整，不可判定無新場次」。候選須與 `data/schedule.json` 比對，列出不在表內者。
- **GitHub Issues**：使用 `gh api` 讀取 `state=all` 的全部 issues 與留言（排除 PR）。

### 3. 有界重試與替代路徑

- 初次失敗先記可見現象：載入骨架、登入提示、HTTP／DNS 錯誤、工具封鎖、媒體打不開或原因未知。區分「工具不支援」與「來源沒有內容」。
- 初次嘗試後最多再試 3 次，每次記錄實際時間、方法、網址及結果。連續失敗時必須更換路徑（重新載入→原帖直連→未登入模式），每次嘗試均須立即 `record`。
- 首輪處理以 45 分鐘為軟上限；剩餘範圍照實記 failed／partial，保存進度並完成可做的核對及狀態發布。

### 4. 覆蓋狀態由清單計算

- 執行 `summary --run <原檔>` 檢查剩餘目標，再以 `finalize --run <原檔>` 寫入公開狀態檔。不帶 `--model` 參數。**已 verified 的 run 若需重新 finalize，必須提供 `--refinalize-reason` 說明原因**，舊發布記錄會妥善保存於 `publicationHistory`。
- 工具規則：動態計算 `lastAttemptAt`（attempts 最大時間）與 `counts`。任一目標 pending／failed → `failed`；全數均有結果但至少一項 partial → `partial`；全部 complete → `complete`。不得手改狀態以掩蓋未完成。
- 工具只檢查記錄完整性，不能替代實際閱讀。報告需附本輪 JSON 路徑，逐項列出已讀範圍、未解線索及失敗原因。當輪有充分證據的場次仍可依既有規則發布；網站 metadata 不因狀態發布而刷新。

### 5. 提交與部署另行驗收

- 測試與 schema／去重檢查通過後，只 stage 本輪明列檔案（包括本輪 JSON、`data/patrol_status.json` 及修改之 `data/schedule.json`），檢視 cached diff 再提交。推送受阻時先分辨 DNS、授權、權限與遠端分歧；使用已授權可用路徑。遠端分歧先 fetch、比較並整合，保留既有修改，不 force-push。
- 保存資料提交 SHA，查找該 SHA 對應的 `.github/workflows/daily-update.yml` Actions run。按狀態變化等待，單次等待不超過 60 秒；不得將其他 SHA 的成功代替本次。
- 執行 `python3 scripts/patrol_progress.py verify --run <原檔> --sha <完整SHA> --actions-run <run-id>`。工具確認該 workflow、SHA、`completed/success`，再比對公開網站狀態檔。失敗時留存 `publication=blocked` 與原因。
- 提交驗收收據及報告至 `docs/patrols/PATROL_YYYY-MM-DD_HHMM_INDEPENDENT.md` 與 `docs/patrols/PATROL_YYYY-MM-DD_HHMM_RECEIPT.md`，使用獨立 `[skip ci]` 提交，僅包含稽核文件，不改公開資料；保留被驗收的資料 SHA，避免收據引發無限部署。推送收據也要確認結果。
- 通知須分別交代「來源覆蓋」、「已核對資料變更」、「推送」、「Actions」、「公開狀態」，列出未完成目標與可接續步驟。原始錯誤或帳號讀取失敗不准被寫成「沒有新資訊」。

只有新核實場次、重要更正、需處理的 Issue、巡檢失敗、狀態發布失敗或需使用者決策時通知；沒有可行動變更且狀態成功發布時可保持安靜。`partial` 不是「無新演出」。

## 同場來源整合與詳情連結

- 同一節目被不同帳號先後分享時，依日期、場地、劇團及劇目辨識同場並合併，保留舊公告於 `relatedSourceUrls`。
- 每次核對也重新比較卡片右下方的 `link`：以劇團官方消息為優先，選擇該場最新有效、資訊完整的公告；主辦方提供更新或更完整的場次專頁、交通、直播及異動資訊時，核對後可改連該專頁。不得永久固定最早發現的轉貼。
- 不是只看發布時間：新轉貼不能凌駕官方，無關場次或較新但內容較少的貼文不取代有效詳情。若官方消息互相衝突，先核對異動、標明差異，證據不足保留待查。
- `link` 是讀者詳情入口；`sourceUrl` 是核實依據，可不同。更新詳情連結不代表提升來源可信度，`verifyStatus` 仍依實際證據分類。

## 後續變更與排程維護

- 加巡檢帳號：更新相應的 `data/*_accounts.json`，確認公開帳號網址可讀，下一輪排程會自動讀新清單；不必改排程文字。
- 改網站：在新工作階段指定本專案及此文件，按需求修改、測試、推送並核對公開頁。單次改站不取代每日巡檢。
- 舊排程已全數清理；每日 03:00 Antigravity sidecar `daily-opera-patrol` 為唯一日常巡檢。來源或部署驗收失敗時按上述恢復規則續跑並通知，不以重啟舊排程處理。
