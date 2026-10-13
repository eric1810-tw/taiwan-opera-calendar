# 2026-10-13 03:00 獨立巡檢（恢復後 partial）

## 結果摘要

- 本輪檔案：`patrol_runs/2026-10-13_0300.json`；實際開始 `2026-10-13T03:02:41+08:00`（Asia/Taipei）。動態載入 21 個目標：Threads 10、Facebook 9、文化部 1、Issues 1。
- 覆蓋：19 個社群帳號均為 `partial`，文化部及 GitHub Issues `complete`，0 pending。初次 finalize 為 `failed`；22:34 恢復文化部全量資料後再次 finalize，`data/patrol_status.json` 為本輪開始時間／`partial`。社群 partial 不是「沒有新資訊」。
- 瀏覽器頁面讀取後均即時 `record`。JSON 保留每次操作時間、方法、公開 URL、可讀範圍、媒體狀態及故障原因；其 `at` 為 record 寫入時刻，detail 記錄緊接觀察與等待情形。

## 來源與結果

### Threads

- 十個名單均已逐一初讀。初始頁多呈載入骨架；對 7 個初讀失敗帳號採用延遲 6 秒後再讀，最終十個帳號都讀到部分正文：`joe_huang_k_w`、`h.akito_1996`、`the_rin.lpm`、`1013.yr_`、`xuefeng_lu_`、`yuzhongluo`、`taiwaneseopera168`、`jing__1017`、`hilang.on.tour`、`yolin1991`。以未列入清單的 `@threads` 控制頁診斷時，等待 6 秒後可讀 2–4 天前貼文，顯示登入／平台頁面可水合，但個別監看頁水合時間不同。
- 仍全部標 `partial`：每頁只顯示部分近期貼文，底部尚有載入中內容；多則含圖片或影片未逐項核對。未以單篇貼文、置頂文或搜尋摘要當成完整帳號覆蓋。
- 讀到的場次線索都保守處理。`the_rin.lpm` 9/26 貼文提及秀琴 11/7《玉石變》及 11/15《金沙灘》，兩筆已在排程；`yuzhongluo` 海報列大寮鳳山寺聖王堂 10/12–13，舊官方月戲路列同地 10/11–13。兩份官方資料沒有明確取消或更改起始日的說明，既有場次已在排程，因此保留原卡及未知劇目／時間，不臆造更正。其他可讀貼文多為回顧、個人近況或非演出公告。

### Facebook

- 九個名單均已逐一初讀：`sunhope.fans`、`HsiaoHsiYuan1913`、`100063868113954`、`MingHuaYuanTianTaiwaneseOpera`、`61574134933376`、`mhysun`、`61594936681482`、`lanyang.opera`、`Taichungpuppettheater`。最後全部 `partial`，因近期動態流未讀完整、仍有載入骨架，且多張公告圖片／影片不全；不得把精選或單篇當整個帳號讀完。
- 可讀的主要線索：尚和兩天前貼文是 10/11 已結束的茄萣金鑾宮《正庄·千波之神2.0》，精選 11/7–8《寒窯之外》已在排程；蘭陽精選 10/26《錯配姻緣》已在排程；天字頁最近貼文是國慶演出結束；地字頁農曆九月戲路含嘉義王靈宮《周公法鬥桃花女》，既有排程已列 11/4–8；孫翠鳳頁讀到 13 小時前傳說教育影片；戲籠出巡記錄 10/8 桃園蓮華寺古都木偶戲，場次已過；台中木偶公告為 10/12 霧峰祝壽演出，巡檢開始時已過。
- 小西園公告展開後說明 2026 下半年索票戲路，但場次表在圖片；點開後 photo viewer 顯示灰屏，日期、劇目、場地仍不可讀。尚和一張公告圖片點開也顯示灰屏；此媒體故障已逐筆記錄，不能據此判定沒有場次。

### 文化部候選

- 初次官方 `category=all` API 兩次 DNS 失敗，公開 web 路徑也不可讀；恢復時改以專案 `fetch_culture_events()` 所用 TLS 設定讀取官方 JSON（保留 CA 與 hostname 驗證，僅為憑證缺少 Subject Key Identifier 放寬 X509 strict）。HTTP 200，完整讀到 1,578 筆。
- 依專案分類函式，以 2026-10-13 至 2027-01-11 的 90 日範圍篩出 32 筆戲曲場次；用 OPENTIX 活動 ID 與日期區間，對照 97 張正式卡及候選檔。31 筆已有對應正式卡；另 1 筆三昧堂精工布袋戲展（2027-01-01）是原有待核候選，未找到獨立原公告，繼續保留 pending。9 個新候選所連 OPENTIX 節目頁均抽核名稱、場次、場地及劇團，均已在正式表且無需改動。
- 本輪沒有新增或改期依據，`data/moc_candidates.json`、`data/schedule.json` 均未修改；文化部來源恢復為 `complete`，未把待核候選算作已驗證演出。
### GitHub Issues

- `gh issue list --state all` 因無法連線 GitHub API；切換到公開 Issues 頁面，分別查 `is:open`、`is:closed`，排序 Updated descending。讀到 #2、#1 均 open，updated 分別為 2026-09-29 03:57、03:54（台北時間）；closed 0。逐頁看完兩筆 Issue 內文及 Activity，均無留言；排除 PR，覆蓋 complete。
- `state:all` 搜尋語法回傳 0 results，已記錄後改用 open／closed 分開查詢；不把該錯誤結果當成無 Issues。

## 資料變更與驗證

- `data/schedule.json`、`data/metadata.json` 均未修改。社群能讀到的活動已過期或與既有場次相符；大寮 10/11–13 與新海報 10/12–13 的差異未見明確取消公告，保留既有卡，不改開始日、劇目、時間或來源可信度。
- `data/patrol_status.json` 經恢復後 `finalize` 更新為本輪 `startedAt=2026-10-13T03:02:41+08:00`、`status=partial`。網站資料刷新時間仍維持原值，與巡檢時間分開。
- 驗證：`python3 -m unittest -v` 17 tests PASS；`node --check assets/app.js` PASS；`git diff --check` PASS；97 筆場次 schema、唯一 ID、日期與 endDate 檢查 PASS。
- 執行模型未從排程工作階段確認，不宣稱已切換 Luna。現有工作樹原有 `ISSUES_REVIEW.md`、`PROJECT_HANDOVER.md` 修改及三個未追蹤稽核檔全數保留，未加入本輪提交。

## 接續與發布

- 恢復於 `2026-10-13T22:27:35+08:00` 開始；新增 Threads `the_rin.lpm`、`joe_huang_k_w`、`1013.yr_` 與 Facebook `HsiaoHsiYuan1913` 的逐筆記錄。19 個社群帳號仍全為 partial：上述4個已做恢復嘗試，另外15個沿用先前讀取證據；feed 分頁尾端或媒體仍不可完整讀取。需要繼續時，用 `python3 scripts/patrol_progress.py resume --run patrol_runs/2026-10-13_0300.json` 接續同一輪，僅在取得實際可讀範圍時更新狀態。隔日另開新輪。
- 初次資料部署 SHA `c5b66e437661ecc54450fd08d5fbb1a3fd8b8e39`／Actions [38297227559](https://github.com/eric1810-tw/taiwan-opera-calendar/actions/runs/38297227559) 已在 03:23 `completed/success` 並驗證當時公開 `failed` 狀態。恢復後的新 `partial` 狀態仍待推送及重新驗證；未完成前不宣稱恢復狀態已上線。
- 本輪 JSON SHA256：`d16922225b84ca1426cf1f56ee2e589f27214c6395e6ec479539eac55f1521af`。`data/schedule.json` 97 筆 SHA256 `f2029bc1eff74e7e3c29e3987fc905bcbfa248432eb6678bdbafc2921b911647`；`data/metadata.json` SHA256 `6e3b182fe2b8bfe7083fd4f18d3f6502e26ea08cbbce3268eda2b5e306ab3e0b`；`data/patrol_status.json` SHA256 `6c03b175ce68012e570d303c092304576dbbb452a476023698c8376c4f9ee72c`。
- 恢復後完整 Actions／公開狀態與 SHA256 驗收收據將追加至 [`PATROL_2026-10-13_0300_RECEIPT.md`](PATROL_2026-10-13_0300_RECEIPT.md)。
