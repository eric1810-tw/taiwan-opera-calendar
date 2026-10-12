# 2026-10-12 03:00 獨立巡檢（failed）

## 結果摘要

- 本輪識別：`patrol_runs/2026-10-12_0300.json`；實際開始 `2026-10-12T02:58:14+08:00`（Asia/Taipei）。
- 動態監看清單共 21 項：Threads 10、Facebook 9、文化部 1、GitHub Issues 1。`summary` 無 pending；`finalize` 依工具規則產生 `data/patrol_status.json` 的 `failed`。
- 初次巡檢覆蓋：2 complete（文化部、Issues）、2 partial（孫翠鳳與戲籠出巡 Facebook）、17 failed（其餘 Threads／Facebook）。使用者要求重試後，於 06:41–06:45 Asia/Taipei 恢復同一輪並逐頁重試原失敗目標；06:48 後為 2 complete、4 partial、15 failed；10:02 延後載入診斷後為 2 complete、5 partial、14 failed、0 pending。`failed` 表示仍有關鍵社群來源正文不可讀；不是「沒有新資訊」。

## 來源讀取與故障

- Threads 十個名單均以 Codex In-app Browser 直接開啟個人頁，首次快照確認頁面身份標頭可見，但貼文流停在「載入中……」骨架：`joe_huang_k_w`、`h.akito_1996`、`the_rin.lpm`、`1013.yr_`、`xuefeng_lu_`、`yuzhongluo`、`taiwaneseopera168`、`jing__1017`、`hilang.on.tour`、`yolin1991`。第三個同平台帳號仍相同故障後，另開非監看帳號 `@threads` 作共同環境診斷，也呈現相同貼文骨架。以 web reader 替代讀取 `@joe_huang_k_w` 時回報 URL 不可讀；Threads 覆蓋仍 failed。10:02 對 `the_rin.lpm` 做延後無障礙樹檢查後讀到 9/26、9/27 兩則歌仔戲公告正文，但底部仍載入中、媒體未全核，故此帳號由 failed 改為 partial；其餘九個帳號的貼文正文仍未讀。
- Facebook 九個名單均逐一直接開啟：`sunhope.fans`、`HsiaoHsiYuan1913`、`100063868113954`、`MingHuaYuanTianTaiwaneseOpera`、`61574134933376`、`mhysun`、`61594936681482`、`lanyang.opera`、`Taichungpuppettheater`。初次巡檢的七個失敗目標均在重試時再度逐頁檢查：`sunhope.fans` 與 `lanyang.opera` 恢復讀到一則精選文字，升為 partial；尚和文字提到 11/7–8《寒窯之外》，已由 OPENTIX verified 場次卡涵蓋；蘭陽文字提到 10/26《錯配姻緣》，與既有卡相符。蘭陽原始貼文直連標題吻合，但貼文彈層仍載入中，沒有讀到完整正文／發布時間／海報。`HsiaoHsiYuan1913`、`100063868113954`、`MingHuaYuanTianTaiwaneseOpera`、`61574134933376`、`Taichungpuppettheater` 仍無貼文正文，維持 failed。原本 partial 的 `mhysun` 與 `61594936681482` 未冒充完整讀取，維持 partial。Threads 名單 10 個皆重試；Joe 已達第四次總嘗試，其餘九個為第二次總嘗試，仍全部載入骨架。重試時改走可用的 Codex In-app Browser；Edge 瀏覽器綁定不可用，Edge app 擷取逾時。替代路徑與每次結果逐筆記入 JSON。這些直接公告只供場次核對，不代表帳號已讀完。
- 文化部：先依專案既定 TLS 設定執行 `updater.fetch_culture_events()`，受限網路下兩次請求都因 DNS 失敗；In-app Browser 與 web reader 替代路徑分別回報 `ERR_BLOCKED_BY_CLIENT` 與 URL 不可讀。取得核准網路路徑後重試成功，官方 `category=all` 回傳 98 筆；依專案 90 日日期／關鍵字規則抽取 0 個候選，抽查名稱／日期欄位並比對現有排程。既有 `data/moc_candidates.json` 中的三昧堂待核候選不在本次 payload，故保留候選不刪除、不新增場次。沒有放寬 CA 或主機名稱驗證。
- GitHub Issues：`gh issue list --state all --limit 100` 首次因無網路失敗，遂先以公開 Issues 列表和逐筆頁面讀取。網路路徑恢復後重試 all-state API 成功，確認共 2 項、無下一頁：#2、#1 均 open，updated 分別為 2026-09-28 19:57:36Z、19:54:09Z；兩筆 comments 陣列皆空。逐筆核對回報目標、原因、OPENTIX 來源連結及 activity，沒有新留言或需處理的新回報。

每次監看頁面／替代路徑後均以 `patrol_progress.py record` 寫入本輪 JSON，包含來源、方法、公開網址、範圍、媒體狀態及可見錯誤；attempt `at` 是 record 寫入時間，對應緊接在前的觀察，未聲稱瀏覽器精確載入秒數。完整逐次紀錄以 JSON 為準。

## 資料變更

- 未新增或修改演出卡；社群近期內容未讀，文化部本輪篩選沒有產生演出候選，沒有足夠證據核實社群演出、異動或取消。避免以個別官方公告／連結冒充帳號已完整巡檢。
- 本輪及重試均未新增／編修演出卡或候選。重試兩則公告對應的 11/7–8 尚和 OPENTIX 節目及蘭陽 10/26 場次均已在排程，未見需修正的欄位；蘭陽單篇貼文頁仍不完整，故不改詳情連結。推送前 fetch 發現遠端自動更新 `718b898`，正常 merge 保留倒數刷新及到期資料清理；最新 `data/metadata.json` 為 `2026-10-11T09:28:30+08:00`，`data/schedule.json` 為 105 筆。這是網站資料刷新時間，與本輪巡檢開始時間分開。

## 驗收與接續

- `finalize` 依 14 個 failed 目標產生 `2026-10-12T02:58:14+08:00 / failed`。重試新增了來源證據，所以之前的發布收據先由工具作廢；資料檔內容與已發布的 failed 狀態相同，並以原資料 commit `cd6bd23073c94141bbc97a4a30ce1c4db8dabd36`、Actions run `38166376833` 重新執行 `verify`。06:47:08 首次重試驗收後，使用者再要求 resume；09:56–09:57 又以 `resume` 接續同一輪。改用公開搜尋索引查 `@yuzhongluo`、`@yolin1991` 皆無結果；匿名 HTTPS 直讀 Threads `@yuzhongluo` HTTP 200 但只有通用殼／載入提示；Facebook Hsiao 頁的替代 reader 顯示 temporary block、索引結果不相關；吳奕萱索引亦未命中目標帳號；地字 Facebook 匿名 HTTPS 回 HTTP 400。以上各次均記入 JSON；09:57 時為 2 complete、4 partial、15 failed。10:02 對 `the_rin.lpm` 等待頁面載入後，確實讀到兩則正文，因此確認此前至少部分失敗由過早擷取載入骨架造成；這也揭露重試流程未落實等待水合的既有成功方法。Facebook 另有替代 reader 明示 temporary block、匿名 HTTP 400 等獨立存取限制，不能將所有故障歸為同一原因。診斷後為 2 complete、5 partial、14 failed；該 Threads 帳號改為 partial，其餘社群目標仍未完整讀取。10:02:34 以原資料 SHA／Actions 重新 `verify` 成功，公開狀態仍是本輪 failed。收尾時合併遠端自動刷新 `aa82f06`（無 Actions run）；10:05 直接重讀公開三 JSON，與最新本地 status、97 筆 schedule、metadata 逐位元組一致，並保留「auto-refresh 未經 Actions」的區別。
- 後續若來源恢復，使用 `python3 scripts/patrol_progress.py resume --run patrol_runs/2026-10-12_0300.json` 接續同一輪。仍失敗來源為 9 個 Threads 和 5 個 Facebook：`HsiaoHsiYuan1913`、`100063868113954`、`MingHuaYuanTianTaiwaneseOpera`、`61574134933376`、`Taichungpuppettheater`。其餘九個仍失敗的 Threads 來源仍未讀到貼文正文；Edge 綁定不可用，建議先恢復其他可用瀏覽器／讀取路徑，再逐項記錄，不以單篇連結替代帳號覆蓋。
- 本次重試後驗證：`python3 -m unittest -v`（17 tests PASS）、`node --check assets/app.js`、`git diff --check`、105 筆 schedule required-fields/schema、日期/endDate、unique ID 與 JSON parse 均 PASS。`data/schedule.json` 與 `data/metadata.json` 未變。
- SHA256（整合遠端更新後）：schedule `35d0adb1218e6ba1c43cd3ac500433cd6d08dc1b7354336c1f2fd2e6dcc61355`；metadata `b7b88e788be28d9580dde364f8a0bc321b3f3638773f69f3078b3e64380d5b50`；patrol status `1cf98e34678f7b8a076608c6b9578640379b758c7f166039c527d35242726b65`；本輪 JSON（publication receipt 更新後）見收據。
- 驗收收據記錄資料 SHA、Actions run、公開三 JSON 與 SHA256；本輪社群讀取未完成，不代表沒有新場次；Threads 即時快照過早是已驗證的流程問題，Facebook 同時存在公開讀取限制。
