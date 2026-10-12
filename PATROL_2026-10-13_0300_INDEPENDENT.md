# 2026-10-13 03:00 獨立巡檢（failed）

## 結果摘要

- 本輪檔案：`patrol_runs/2026-10-13_0300.json`；實際開始 `2026-10-13T03:02:41+08:00`（Asia/Taipei）。動態載入 21 個目標：Threads 10、Facebook 9、文化部 1、Issues 1。
- 覆蓋：19 個社群帳號均為 `partial`，文化部 `failed`，GitHub Issues `complete`，0 pending。`finalize` 依清單規則將 `data/patrol_status.json` 寫為本輪開始時間／`failed`。失敗表示 category=all 文化候選未讀完；社群 partial 也不是「沒有新資訊」。
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

- 本地 `data/moc_candidates.json` 有 1 筆待核候選（三昧堂精工布袋戲展，2027-01-01）。官方 `category=all` API 初次呼叫內部兩次皆 DNS `Errno 8`；web open 回報端點不可存取，瀏覽器直連 API 則 `ERR_BLOCKED_BY_CLIENT`。
- 改看文化部 iCulture 活動列表並以「布袋戲」查詢，僅顯示一頁一般活動摘要，含「逐家逗陣來看歌仔戲」2026/09/05–10/16 等項目；詳情連結打開成錯誤 URL，無法檢視完整來源或確認是否全量搜尋結果。因此沒有 category=all 候選清單、分類與去重證據，目標維持 `failed`；不把舊候選或未完整列表當成 0 筆新候選。

### GitHub Issues

- `gh issue list --state all` 因無法連線 GitHub API；切換到公開 Issues 頁面，分別查 `is:open`、`is:closed`，排序 Updated descending。讀到 #2、#1 均 open，updated 分別為 2026-09-29 03:57、03:54（台北時間）；closed 0。逐頁看完兩筆 Issue 內文及 Activity，均無留言；排除 PR，覆蓋 complete。
- `state:all` 搜尋語法回傳 0 results，已記錄後改用 open／closed 分開查詢；不把該錯誤結果當成無 Issues。

## 資料變更與驗證

- `data/schedule.json`、`data/metadata.json` 均未修改。社群能讀到的活動已過期或與既有場次相符；大寮 10/11–13 與新海報 10/12–13 的差異未見明確取消公告，保留既有卡，不改開始日、劇目、時間或來源可信度。
- `data/patrol_status.json` 僅由 `finalize` 更新為本輪 `startedAt=2026-10-13T03:02:41+08:00`、`status=failed`。網站資料刷新時間仍維持原值，與巡檢時間分開。
- 驗證：`python3 -m unittest -v` 17 tests PASS；`node --check assets/app.js` PASS；`git diff --check` PASS；97 筆場次 schema、唯一 ID、日期與 endDate 檢查 PASS。
- 執行模型未從排程工作階段確認，不宣稱已切換 Luna。現有工作樹原有 `ISSUES_REVIEW.md`、`PROJECT_HANDOVER.md` 修改及三個未追蹤稽核檔全數保留，未加入本輪提交。

## 接續與發布

- 文化部全量候選和 19 個社群帳號近期正文／圖片尚未完整核對；如需續跑，使用 `python3 scripts/patrol_progress.py resume --run patrol_runs/2026-10-13_0300.json` 接續同一輪。隔日另開新輪。
- 巡檢資料 SHA、對應 Actions 狀態、公開狀態檔驗證及驗收收據將在資料提交後另行記錄；未完成前不宣稱已上線。
