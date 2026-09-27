# 台灣傳統戲曲演出行事曆｜專案與資料流程交接

更新日期：2026-09-28（Asia/Taipei）

專案：`/Users/eric/aiwork/taiwan-opera-calendar`
用途：供後續 Codex session 接手，先以本文件與實際程式／Git 狀態為準；舊 README 與早期交接文件可能過時。

## 目前狀態摘要

- 靜態網站由 `index.html` 顯示 `data/schedule.json`，頁尾讀取 `data/metadata.json` 顯示資料刷新時間。
- 最近一次已保存的資料時間以 `data/metadata.json` 為準。本次 2026-09-28 更新後 schedule 有 **55 張日曆卡**：`verified` 38、`community` 17；區域北部 26、中部 4、南部 22、東部 2、未分類 1。卡片數不是唯一活動數或演出晚數。
- 卡片來源網域計數（依 `link` 欄位）：文化部 `event.moc.gov.tw` 5、OPENTIX 24、Threads 9、Facebook 4、`siouching2008.pixnet.net` 4、`twoperapf.org.tw` 3，以及 `tw-yishin.com`、`event.culture.tw`、`pili.com.tw`、`shintrun.com`、`npac-ntt.org`、`klpas.klcg.gov.tw` 各 1。連結是卡片來源線索，不代表所有來源都已經有自動擷取器。
- 接手時務必以 `git status --short --branch`、`git log -1`、`git ls-remote origin HEAD` 查證本地／遠端版本；不要依本文件猜測已部署狀態。`CLOUDFLARE_HANDOVER.md` 是先前留下的未追蹤檔案，屬既有使用者工作，請保留。
- 本機 GitHub CLI 曾回報登入 token 無效；但 Git `ls-remote` 在解除工具沙盒網路限制後已可連通。推送和網站部署仍須分別驗證。

## 演出資料來自哪裡

資料是手工整理與自動候選混合，不是由單一資料庫完整生成：

1. **文化部藝文活動 Open Data**：`updater.py` 呼叫 `https://cloud.culture.tw/frontsite/trans/SearchShowAction.do?method=doFindTypeJ&category=all`，依「歌仔戲／布袋戲／掌中戲」等文字篩選、展開 `showInfo` 場次並限未來 90 天。抓到的是候選，程式標成 `verifyStatus: pending`、`⏳ 自動發現・待人工核實`；不能因來自文化部 API 就把每一筆候選宣稱已人工核實。
2. **OPENTIX 官方節目頁與文化部活動詳情頁**：大量已核實卡片來源。人工比對節目、劇團、日期、地點和各場時間後寫入 `data/schedule.json`；同一活動多場應分別列卡或以卡片中的場次描述呈現，新增時會用 OPENTIX program ID、日期與標題等條件去重。
3. **劇團／演員社群公告**：例如使用者提供的羅裕誴歌劇團 Threads 行程、姿蓉歌劇團演出海報及 Facebook／Threads 貼文。由人讀取公告並整理成卡片；有公告但缺演出時間、完整地址或劇目時，應明確保留「未公布／未提供」，不能推測補齊。社群來源狀態 `community` 不等於官方第二來源核實。
4. **主辦單位、場館、劇團官方頁面及政府文化資料**：用作查證或補充詳情；部分項目由官方來源交叉核實後標為 `verified`。
5. **Threads 監控名單**：`data/threads_accounts.json` 放有使用者提供的 13 個 handle，另納入先前提供行程的 `@yuzhongluo`，合計 14 個。這是監控目標清單，不是演出資料來源本身，也不要求替使用者按 Follow。2026-09-28 的瀏覽器巡檢與去重詳見 `THREADS_AUDIT_2026-09-28.md`。

## 時刻表如何產生及更新

### 已運作的既有資料流程

1. `.github/workflows/daily-update.yml` 由 GitHub Actions 於 cron `0 23 * * *` 執行，即台灣時間每天 07:00；另支援 `workflow_dispatch` 手動觸發及 `main` push 事件。
2. job 使用 Python 3.11 執行 `python updater.py`。
3. `updater.py` 讀入現有 schedule，呼叫文化部 API，轉成最多未來 90 天的戲曲候選；依 OPENTIX ID、日期／標題避免與已編輯資料重複。已編輯／已核實資料不應被機器候選覆寫。
4. 重算台灣時區倒數日，驗證必備欄位、日期格式、ID 唯一性、`daysAway` 型態與 tags 格式；以暫存檔、`fsync`、`os.replace` 原子方式更新 `data/schedule.json` 和 `data/metadata.json`。
5. 若 Git 資料有變更，workflow 會 commit/push schedule、metadata，並部署 GitHub Pages artifact。自動 commit message 含 `[skip ci]`；Cloudflare Pages 若採 Git 整合，可能因 skip 標記而不部署自動資料更新，見 `CLOUDFLARE_HANDOVER.md`。

### Threads 監控（瀏覽器已即時巡檢；API 路徑仍待授權）

- Codex 已透過登入的內建瀏覽器讀取名單中 14 個公開帳號的近期可見貼文與圖片，不需 Meta API 授權。本次已從秀琴相關宣傳帳號新增兩場 `community` 卡片，另將未獨立查證的戲路圖與古都木偶團澄清記在 `THREADS_AUDIT_2026-09-28.md`。
- Codex app 已建立有效 heartbeat 排程「臺灣戲曲 Threads 演出巡檢」，設定每日 07:00、19:00 按名單巡檢，僅在新增可發布場次、重要更正、失敗或需使用者處理時通知。排程設定存在 app 個人 automations 中，**不在 Git repo**；是否按台灣時間實際觸發、能否持續讀取登入頁面及寫入／推送，須等首次執行後驗收，不能把「建立成功」當成「長期監控已驗證」。
- 下列官方 Threads API 擷取器是另一條**可選**路徑；缺 token 不會阻止上述瀏覽器巡檢。

- 最近變更新增官方 Threads API 讀取 `/v1.0/profile_posts`，帳號從 `data/threads_accounts.json` 讀入，候選貼文寫入 `data/threads_candidates.json`，按 post ID 去重並保留貼文網址、日期、文字，狀態為待核實。
- 當 workflow secret `THREADS_ACCESS_TOKEN` 存在時，日常 `updater.py` 會呼叫此巡檢；沒有 secret 時只記錄略過。可用 `python3 updater.py --threads-now` 單獨要求立即巡檢，不必等每日 cron。
- **目前還沒有成功的即時批次 API 抓取**：本機未設定 `THREADS_ACCESS_TOKEN`，手動執行 `--threads-now` 因缺 token 停止；`data/threads_candidates.json` 目前是空陣列。需在 Meta Developer 建立／設定 Threads API app、取得包含公開檔案發現權限的授權，並把 token 安全地設成 GitHub repo Actions secret `THREADS_ACCESS_TOKEN`。不要把 token 提交到 Git 或貼在聊天中。
- 本版只讀取每個 profile 最近最多 25 篇，使用文字關鍵字篩選戲曲／演出相關貼文，並保留原文供人工審核；**尚不具備**中文日期／農曆解析、地點抽取、未來日期判斷、跨來源同場次比對、或將 Threads 候選自動合併進 `schedule.json`。避免宣稱它已能自動生成完整演出卡。
- 本輪 offline smoke tests 曾以 mock API 驗證授權標頭、token 不進 URL、候選去重／保存與 pending 狀態；這不是 Meta API 實際連線驗收。

## 有沒有稽核／審核機制？

有**部分技術驗證及資料標籤**，但目前沒有完整、獨立的演出資料審核工作流：

- **技術結構檢查**：`validate_schedule()` 檢查 JSON 結構、必填欄位、日期可解析、ID 不重複、倒數日非負整數與 tags 型別。原子寫入降低更新中斷造成 JSON 損毀的風險。
- **候選去重**：機器候選可按 OPENTIX ID、日期／標題等條件與既有卡比對；只能降低重複，不保證語意上同一活動皆能辨識，也不等同事實核查。
- **來源／狀態標示**：`verified`、`community`、`pending` 對應 UI 標籤。`verified` 表示編輯者曾依來源核對；程式不會重新驗證所有已核實卡片當前是否仍有效或有無改期。
- **人工事實審核**：以官方節目頁、文化部場次、主辦／劇團公告交叉核對日期、時間、地點、劇目與主辦方；需留來源連結和說明。社群公告可作直接來源，但資訊不完整時應保留缺漏並標明來源類型。
- **目前缺少的機制**：沒有 PR 必須經第二人批准的 branch protection 流程、沒有自動逐卡證據快照／稽核日誌、沒有定期重新核對改期取消、沒有獨立模型的強制審核 gate，也沒有 Threads 候選轉正式卡片的審批工具。Schema pass 不能說成「資料絕對正確」。

建議後續正式資料新增採兩階段：先存來源原文與待審候選；人工確認日期、縣市／地點、團名、劇目、場次時間、來源連結、是否重複及取消／異動；再編輯 `schedule.json` 並跑驗收。任何未能從來源明確確認的欄位都標為未公布或待查，不推斷。

## 主要檔案索引

- `index.html`：靜態網站介面與卡片呈現。
- `data/schedule.json`：正式展示的 55 張卡片（以檔案即時計數為準）。
- `data/metadata.json`：頁尾資料時間，Asia/Taipei。
- `updater.py`：文化部候選、schema 驗證、去重、倒數更新、原子寫入，以及尚未實際授權驗收的 Threads 監控程式。
- `.github/workflows/daily-update.yml`：每日／手動更新與 GitHub Pages 部署。
- `data/threads_accounts.json`：14 個 Threads 監控 handle。
- `THREADS_AUDIT_2026-09-28.md`：本次即時瀏覽器巡檢、來源等級、排除與待查線索。
- `data/threads_candidates.json`：Threads 原始貼文候選庫，目前空。
- `CLOUDFLARE_HANDOVER.md`：Cloudflare Pages 遷移專用交接；其中部分摘要數字／commit 可能在其撰寫後過時，需以本檔和最新 repo 驗證。
- `CODEX_HANDOVER_AND_AUDIT_SPEC.md`：較早期審核規格，包含舊專案狀態；作為要求清單參考，不能當作當前程式現況。
- `README.md`：有早期初始化和功能描述，與目前 GitHub Pages 已運作狀態不完全相符。

## 新 Session 接手待辦

1. 先看 `git status --short --branch`、`git diff`，保留本地未提交變更及原有 `CLOUDFLARE_HANDOVER.md`。
2. 建立 Meta Threads API app／授權與 `THREADS_ACCESS_TOKEN` secret；確認 API 對指定公開帳號可讀，勿把 token 寫進 repository。
3. 先驗收 Codex heartbeat 第一次實際觸發時間、14 個帳號的瀏覽器讀取結果與去重。若另取得合法 API 授權，再執行 `python3 updater.py --threads-now`，檢查 14 個帳號成功數、API 部分錯誤和 `data/threads_candidates.json` 原文；目前的 keyword filter 可能漏抓以圖片海報為主或用語未命中的貼文。
4. 手工抽查候選和原始貼文，建立能保留完整來源證據的演出抽取／人工批准步驟；先不要自動將 Threads 候選寫入正式 schedule。
5. 補 parser、重複活動測試、錯誤／token 過期／部分帳號失敗測試與 schema 驗收；檢查當所有帳號失敗時不要把成功狀態或更新時間誤報。
6. 本機 gh authentication 目前 token 無效。由使用者在本機重新登入或修復授權後，才可推送；push 前重新確認 diff，不要提交 secrets。推送後在 GitHub Actions 手動執行一次，確認即時 job 真的成功及候選檔更新。
7. 若網站已遷移到 Cloudflare，另外驗證含 `[skip ci]` 的 bot commit 是否觸發 Pages build，避免只更新 GitHub 資料而線上頁面仍舊資料。

## 驗收時應明確回報

分別報告：已完成程式碼、已執行的離線測試、Meta API 實際成功帳號數、候選貼文數、人工核實數、正式 schedule 的新增／去重／未採納數、Pages 是否已部署，以及尚未核實的欄位。不要用「已自動核實」描述 keyword matching 或 JSON schema validation。
