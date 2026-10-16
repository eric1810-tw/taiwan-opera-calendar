# 2026-10-17 03:00 臺灣戲曲獨立巡檢

- 實際開始：2026-10-17T03:02:16+08:00（Asia/Taipei；排程標稱03:00）。本輪動態目標21項：Threads 10、Facebook 9、文化部候選1、GitHub Issues 1。
- 最終覆蓋：**failed**（17 partial、3 failed、1 complete）。完整逐次時間、方法、網址、正文/媒體範圍、故障原因及候選處置見 [`patrol_runs/2026-10-17_0300.json`](patrol_runs/2026-10-17_0300.json)。Threads `1013.yr_`、Facebook `100063868113954` 與名單所列明華園天字團帳號未能讀取；Issues complete；其餘帳號/文化部均有未讀範圍。未將部分可讀推論成無新資訊。
- 已用 `resume` 查看並恢復 2026-10-16 原輪；原輪無可續讀的新證據，且本輪重試 GitHub DNS 仍失敗。此 resume 清除了前輪 JSON 的 `finalizedAt`、重設 publication 後再記回 blocked；前輪 JSON 在工作區留下未暫存更新，其歷史收據雜湊不再對應該工作檔。隔日另以 `init` 建本輪；網站刷新時間與社群巡檢時間分開。

## 來源覆蓋與處置

- Threads 10帳號均已初讀。9帳號能讀到部分近期正文，但多數 feed、置頂、圖片/影片不完整。`1013.yr_` 個人頁顯示失效；作者搜尋與公開索引皆未提供可讀內容，記錄3次嘗試，保留 failed。其餘 Threads 頁可讀，未見平台共通故障。
- Facebook 9帳號均已初讀。7帳號部分可讀但完整 feed/媒體未讀，2帳號失敗。`100063868113954` 頁面空殼及搜尋無可用內容，記錄2次後保留 failed。名單中的明華園天字團正確網址 `MingHuaYuanTianTaiwaneseOpera` 另行重開仍顯示「目前無法查看此內容」；前兩次嘗試網址拼字不同，故不算目標帳號覆蓋，改列 failed。此前該拼字路徑所見的慈后宮日期資訊只與既有卡相符，不以它作本輪帳號證據或改卡。
- 文化部官方全類別 API：命令列、專案原生 `fetch_culture_events()` 均 DNS 失敗；瀏覽器替代路徑成功載入官方 JSON，但規模過大，本輪未逐筆完成動態候選去重/篩查，保持 partial。本地 [`data/moc_candidates.json`](data/moc_candidates.json) 另行核對只有1筆待核候選「三昧堂精工布袋戲展」，標示2027/1/1、屬展覽，不升格為演出。羅裕誴Threads稱南瀛藝術節10/24內容為八方藝團「八家將＋聖王再現」；[官方藝術節場表](https://nanyingfest.tnc.gov.tw/)同時段列八方藝團及大灣國小客家獅隊，描述不一致，保留待核。
- GitHub Issues 公開頁分別檢查開啟與關閉狀態，讀完#1、#2正文與Activity：2 open、0 closed、無PR混入，無新異動；標 complete。
- 已知古都竹南10/30、尚和11/7–8、秀琴11/7/11/15、小西園10/30/11/1、嘉義10/24講座與其他已讀場次均與既有卡相符。重看小西園官方海報確認11/1主演是「邱鉦富」，更正本輪轉錄字形；正式場次卡原字已正確。
- 台中木偶劇團近期資訊經屯區藝文中心官方活動頁交叉核對：2026/11/1「傳統表演藝術與影視科技的表現形式」講座，時間更新為10:00–12:00，B1藝享空間，名額50，免費報名需100元保證金並於報到後退還；已新增1張 `lecture`、`verified` 推廣講座卡。[官方活動頁](https://www.ttdac.taichung.gov.tw/nc5747528526064455651/ncArticleContent)同日14:00–16:00另有布袋戲手作坊公告，但缺獨立活動頁的完整費用/報名資訊，本輪僅列候選不另建卡。11/7售票演出卡既有，無重複新增。
- `yolin1991` 提及新吉義林歌劇團10/17–18雲林四湖演出，時間未公布，公開查詢未找到可靠同期劇團/廟方佐證；不新增、不猜時間。其他內容不足或有衝突的線索均保留待核。

## 對抗式驗收與發布

- `python3 -m unittest -v`：18 tests passed；`node --check assets/app.js`、`git diff --check`：passed。schedule JSON/schema、日期、`endDate`、唯一 ID 與重複事件鍵檢查通過。
- schedule 由98增為99張，僅新增上述官方戲曲推廣講座卡；`data/metadata.json` 未修改，未改寫網站資料刷新時間。
- 最終資料 commit `f03b44dcd6bf0c4984b6f890cfd29e2ba77dbe45`（schedule 98→99）推送仍因 `Could not resolve host: github.com` 失敗；推送嘗試時本地 `main` ahead 5。公開狀態仍是 `2026-10-15T07:15:39+08:00 / failed`，沒有本輪 matching Actions，也沒有真實 run ID 可執行 `verify`。**本輪未上線**；網路恢復後須 fetch/比較/整合、推送資料 SHA、確認對應 Actions completed/success，再核對公開 JSON。
- 實際排程執行模型未驗證，不聲稱已切換 Luna High。
- 本機原有 `ISSUES_REVIEW.md`、`PROJECT_HANDOVER.md` 修改及3個未追蹤文件均保留；本輪提交只包含本輪明列檔案。
