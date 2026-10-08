# 臺灣戲曲網站巡檢交接與操作

本文件是排程和新工作階段的操作入口；即時狀態以檔案及公開網站為準，不沿用文件中舊的場次數。時區一律為 Asia/Taipei。

## 工作分界

- 獨立 Codex 排程每日 03:00（Asia/Taipei，每天一次） 巡檢公開 Threads、Facebook、文化部候選及 GitHub Issues，經來源核對才編修正式場次。每輪留下巡檢紀錄與 `data/patrol_status.json`，並嘗試推送、驗證公開站。
- GitHub Actions `.github/workflows/daily-update.yml` 呼叫 `updater.py`，處理候選、倒數、metadata、過期場次及部署。它不是社群貼文語意審核員；不得將自動候選當成已核實演出。
- `data/schedule.json` 是公開場次；`data/metadata.json` 是網站資料刷新時間；`data/patrol_status.json` 是社群巡檢開始時間及完成程度。三者不可混稱。

## 每輪巡檢

1. 記錄實際開始時間（含 `+08:00`）。從 `data/threads_accounts.json`、`data/facebook_accounts.json` 動態讀取完整監看名單，查看近期公開貼文及圖片戲路表；檢視 `data/moc_candidates.json`。帳號無須按 Follow，也不依賴 Meta token。無法讀取或只能讀一部分時，記下實際範圍，不可推斷「沒有新資訊」。
2. 抽取今天、明天及未來演出的日期、時間、劇團、劇目、場地與原始連結。與 `data/schedule.json` 依日期、場地、劇團及劇目核對重複；查原始劇團、主辦、售票及文化部公告，並查異動或取消。未核實的保留候選或稽核紀錄，不當確定場次發布。社群原始公告依 `community` 分類，不因它是劇團貼文就改標 `verified`；同場保留一張卡及所有來源連結。
3. 巡檢儲存庫 [全部 Issues](https://github.com/eric1810-tw/taiwan-opera-calendar/issues?q=is%3Aissue+sort%3Aupdated-desc)（新建、留言、重開、關閉），按更新時間排序，必要時翻頁，排除 Pull Requests。API 不通改用公開瀏覽器；仍不可讀就記失敗。收到回報先查原始公告及現有場次，依 `ISSUES_REVIEW.md` 留證據與處理結果。
4. 記錄本輪來源、比對、未解線索及失敗範圍；可參考最近 `PATROL_*.md`、`THREADS_AUDIT_*.md`、`SOURCE_AUDIT_2026-09-28.md`。更新 `data/patrol_status.json` 的 `startedAt` 和 `status`：所有目標近期公開內容及 Issues 均讀完才用 `complete`；任一來源部分可讀、圖片不清或範圍不足用 `partial`；關鍵來源無法讀或巡檢未完成用 `failed`。不為更新時間捏造場次。
5. 只在證據足夠時改 `data/schedule.json`；執行 `python3 -m unittest -v`、`node --check assets/app.js`、`git diff --check`，檢查 schema、日期、去重及頁面。僅提交本輪檔案，保留其他人的工作區修改。每輪把巡檢紀錄與狀態檔推送；確認 GitHub Actions 結果、[公開站狀態檔](https://eric1810-tw.github.io/taiwan-opera-calendar/data/patrol_status.json) 的時間與狀態。推送或部署不通則保留本地並明示未上線。

## 執行與恢復規則（2026-10-08 起）

日常排程維持 Luna，先用 High 試行；前 5 輪逐輪檢查漏項、恢復步驟及發布驗收。模型不能保證外部頁面可讀。遇到來源衝突先保留候選；若流程仍反覆漏步驟，整理同一批輸入、工具結果及差異後，再評估改用 Sol 處理該段判斷。不要宣稱已自動切換模型。

### 1. 開始即建立可續跑清單

- 先保存 `git status --short` 與 staged 檔案清單，辨識既有修改；不可 `git add .`。一次只執行一輪，避免兩輪覆寫 `patrol_status.json`。
- 執行 `python3 scripts/patrol_progress.py init --run patrol_runs/<本輪識別>.json`。工具照實記錄開始時間，動態建立 Threads、Facebook、文化部、Issues 的全部目標。使用新檔名，不回填排程時間。
- 每個目標都須留下結果。先走完全部目標的初次讀取，再處理未完成項目；單一頁面失敗不能讓其他目標停擺。
- 中斷後以 `resume --run <原檔>` 接續同一輪，工具保留原開始時間與歷次嘗試，另記恢復時間並同步新名單。隔日建立新輪，不把前一天的成功結果算入今天覆蓋。

### 2. 記錄讀取證據與範圍

每次操作後使用 `record` 存檔。成功也必須記錄日期範圍、貼文範圍、圖片核對結果及來源網址；首頁帳號名稱、貼文容器、搜尋摘要或單篇可讀不等於近期內容已讀完。預設讀取最近 7 天，另核對仍有效的置頂／月份戲路公告；遇到分頁或更早公告包含未來演出時繼續追查。圖片不存在才能使用 `not_applicable`，並在 detail 說明；圖片打不開屬未讀。

```sh
python3 scripts/patrol_progress.py record --run <原檔> \
  --source threads:joe_huang_k_w --state partial --method profile-browser \
  --url https://www.threads.com/@joe_huang_k_w \
  --scope '最近7天只讀到一篇；其他貼文仍載入中' --media unread \
  --detail '正文局部可讀，海報無法開啟；尚未完成帳號覆蓋'
```

`--source` 的鍵以 `summary --run <原檔>` 列出的完整清單為準。讀不到正文用 `failed`；正文或媒體局部可讀用 `partial`；全部範圍讀完才用 `complete`。文化部須記錄候選讀取、分類／去重與比對範圍；Issues 須記錄全部狀態、更新順序、分頁與留言核查。

### 3. 有界重試與替代路徑

- 初次失敗先記可見現象：載入骨架、登入提示、HTTP／DNS 錯誤、工具封鎖、媒體打不開或原因未知。區分「工具不支援」與「來源沒有內容」。
- 初次嘗試後最多再試 3 次，每次記錄實際時間、方法、網址及結果。可先等待頁面完成再重新讀取；連續 2 次完全相同就切換方法，不把四次相同 reload 當成恢復方案。
- 可行路徑依序檢查：原頁正文與媒體 → 既有原始貼文／媒體直連 → 已確認可用的其他瀏覽器或讀取工具。瀏覽器未接通／工具不支援時記錄並選其他可用路徑，不反覆呼叫同一失敗介面。
- 3 個同平台帳號出現相同失敗時，先診斷共通環境（其他公開頁是否可讀、登入提示、工具封鎖或網路）；整理共同故障證據，再繼續其他平台及候選／Issues。其餘帳號仍需初次嘗試，不能以共同故障推定全部結果。
- 劇團、主辦、政府或售票公告可補核對特定場次，但不可充當 Facebook／Threads 整個帳號讀完的證據。搜尋摘要只能作線索。
- 首輪處理以 45 分鐘為軟上限；剩餘範圍照實記 failed／partial，保存進度並完成可做的核對及狀態發布。必要時在同一工作階段接續恢復；不另建日常 heartbeat，也不自動製造無限重試排程。

### 4. 覆蓋狀態由清單計算

執行 `summary --run <原檔>` 檢查剩餘目標，再以 `finalize --run <原檔>` 寫入公開狀態檔。工具規則：任一目標 pending／failed → `failed`；全數均有結果但至少一項 partial → `partial`；全部 complete → `complete`。不得手改狀態以掩蓋未完成。

工具只檢查記錄完整性，不能替代實際閱讀。報告需附本輪 JSON 路徑，逐項列出已讀範圍、未解線索及失敗原因。當輪有充分證據的場次仍可依既有規則發布；網站 metadata 不因狀態發布而刷新。

### 5. 提交與部署另行驗收

- 測試與 schema／去重檢查通過後，只 stage 本輪明列檔案（包括本輪 JSON），檢視 cached diff 再提交。推送受阻時先分辨 DNS、授權、權限與遠端分歧；使用已授權可用路徑。遠端分歧先 fetch、比較並整合，保留既有修改，不 force-push。
- 保存資料提交 SHA，查找該 SHA 對應的 `.github/workflows/daily-update.yml` Actions run。按狀態變化等待，單次等待不超過 60 秒；不得將其他 SHA 的成功代替本次。
- 執行 `python3 scripts/patrol_progress.py verify --run <原檔> --sha <完整SHA> --actions-run <run-id>`。工具確認該 workflow、SHA、`completed/success`，再比對公開網站狀態檔。失敗時留存 `publication=blocked` 與原因；有必要可用公開瀏覽器核對，將可重現證據寫入報告，工具未成功須如實說明。
- 提交驗收收據及報告可用獨立 `[skip ci]` 提交，僅包含稽核文件，不改公開資料；保留被驗收的資料 SHA，避免收據引發無限部署。推送收據也要確認結果。
- 通知須分別交代「來源覆蓋」、「已核對資料變更」、「推送」、「Actions」、「公開狀態」，列出未完成目標與可接續步驟。原始錯誤或帳號讀取失敗不准被寫成「沒有新資訊」。

只有新核實場次、重要更正、需處理的 Issue、巡檢失敗、狀態發布失敗或需使用者決策時通知；沒有可行動變更且狀態成功發布時可保持安靜。`partial` 不是「無新演出」。

## 同場來源整合與詳情連結

- 同一節目被不同帳號先後分享時，依日期、場地、劇團及劇目辨識同場並合併，保留舊公告於 `relatedSourceUrls`。
- 每次核對也重新比較卡片右下方的 `link`：以劇團官方消息為優先，選擇該場最新有效、資訊完整的公告；主辦方提供更新或更完整的場次專頁、交通、直播及異動資訊時，核對後可改連該專頁。不得永久固定最早發現的轉貼。
- 不是只看發布時間：新轉貼不能凌駕官方，無關場次或較新但內容較少的貼文不取代有效詳情。若官方消息互相衝突，先核對異動、標明差異，證據不足保留待查。
- `link` 是讀者詳情入口；`sourceUrl` 是核實依據，可不同。更新詳情連結不代表提升來源可信度，`verifyStatus` 仍依實際證據分類。

## 後續變更與搬遷驗收

- 加巡檢帳號：更新相應的 `data/*_accounts.json`，確認公開帳號網址可讀，下一輪排程會自動讀新清單；不必改排程文字。
- 改網站：在新工作階段指定本專案及此文件，按需求修改、測試、推送並核對公開頁。單次改站不取代每日巡檢。
- 舊 heartbeat `threads` 已停用，不要重啟；每日 03:00 獨立排程為唯一日常巡檢。來源或部署驗收失敗時按上述恢復規則續跑並通知，不以重啟舊排程處理。
