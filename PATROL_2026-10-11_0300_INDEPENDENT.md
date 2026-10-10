# 2026-10-11 03:00 獨立巡檢

## 本輪結果

- 實際開始：`2026-10-11T02:57:55+08:00`；時區 `Asia/Taipei`。
- 執行追蹤：[`patrol_runs/2026-10-11_0300.json`](patrol_runs/2026-10-11_0300.json)。21 個動態目標均已嘗試並保存每次時間、方法、公開網址、正文／媒體範圍及失敗原因；初讀後再處理失敗來源。沒有 pending 目標。
- 最終來源覆蓋：`failed`。9 個 Threads 帳號正文未讀，6 個 Facebook 帳號正文未讀；其餘 4 個社群來源只有局部可讀。這不代表沒有新資訊。
- `data/patrol_status.json` 已由 `patrol_progress.py finalize` 按來源狀態產生 `2026-10-11T02:57:55+08:00 / failed`。

## 社群來源核查

- Threads `@joe_huang_k_w`：首頁讀到最近三篇正文（10/9 三場廟會小型演出、10/8 桃園演出後及苗栗竹南 10/30 預告）；海報縮圖未開啟核對，後續貼文也未完整讀取，標記 `partial`。未將圖片內容推測為可新增場次。
- Threads `@h.akito_1996`、`@the_rin.lpm`、`@1013.yr_`、`@xuefeng_lu_`、`@yuzhongluo`、`@taiwaneseopera168`、`@jing__1017`、`@hilang.on.tour`、`@yolin1991`：首次頁面只顯示帳號框架與貼文載入骨架。抽查重開後仍為相同骨架；診斷時確認 Joe 的 Threads 首頁文字可讀。轉用匿名 HTTPS 後，九頁回 HTTP 200 但只取到約 277–279 KB 相似頁面外殼，沒有帳號貼文文字或媒體可核查。各次嘗試均記在本輪 JSON，全部標記 `failed`。
- Facebook `sunhope.fans`、`HsiaoHsiYuan1913`、吳奕萱、`MingHuaYuanTianTaiwaneseOpera`、`mhysun`、`lanyang.opera`：瀏覽器未取得可核查近期貼文正文；匿名 HTTPS 六頁均回 HTTP 400（每頁 1,542 bytes），改道後仍無正文或媒體，標記 `failed`。
- Facebook 繡花園／明華園地字、戲籠出巡、台中木偶劇團：可讀部分精選與貼文文字，未完整瀏覽近 7 日內容或媒體，均 `partial`。繡花園精選有農曆九月戲路及《孫臏兵法》片段，未轉換農曆或據此建卡；戲籠出巡可讀的 10/8 桃園貼文已過期；台中木偶劇團讀到既有 11/7《聖劍風雲三–龍虎兄弟》14:30 卡及最新祈福宣傳短片文字，影片未播放，未發現有足夠證據的新增／異動。
- 共同環境診斷：多個 Threads 帳號同為骨架；跨帳號對照發現 Joe 可讀，匿名請求僅取到通用外殼。Facebook 多頁同為正文不可讀／HTTP 400，但台中木偶劇團等頁可讀部分內容，故僅記錄本輪帳號範圍限制，不泛化成平台整體無內容。

## 文化部與 GitHub Issues

- 文化部官方 `category=all` API 先遇到 Python TLS strict 憑證拒絕、瀏覽器 `ERR_BLOCKED_BY_CLIENT` 及受限 shell DNS 失敗；沒有停用 CA 或主機名稱驗證。改用專案 `updater.fetch_culture_events()` 的 TLS 設定並以核准網路路徑成功讀取 485 筆；專案候選規則在 2026-10-11 起 90 日內抽出 1 筆，與既有 `data/moc_candidates.json` 候選完全相同：三昧堂精工布袋戲展（category 6 展覽），維持待核，不是演出，不新增公開場次。讀取範圍與失敗路徑均逐次寫入 JSON。
- GitHub 全部 Issues 使用 `gh issue list --state all --limit 100` 讀完，共 #1、#2，兩者 open、0 留言；updatedAt 分別 `2026-09-28T19:54:09Z`、`2026-09-28T19:57:36Z`。兩份 body 都是一般演出提報並附 OPENTIX 連結，未見新的狀態或留言異動。此來源 `complete`。

## 公開資料變更與驗收

- 沒有充分證據因社群巡檢新增或修訂演出；文化部候選也未變。推送前發現並 fast-forward 遠端自動更新提交 `f1a1f2e`，該更新依排程清除／重算場次倒數及更新 metadata；已保留，不是本輪來源核實造成的資料修訂。合併後網站資料刷新時間為 `2026-10-10T10:01:32+08:00`，與本輪社群巡檢開始時間分開。
- 本輪已完成 `python3 -m unittest -v`（17 tests PASS）、`node --check assets/app.js`、`git diff --check`；fast-forward 後專案 `validate_schedule` 核對 108 筆必填欄位、日期／endDate、唯一 ID 均 PASS；巡檢狀態與本輪 JSON 一致。頁面程式仍分開載入 metadata 與 patrol status，並顯示巡檢失敗狀態。
- 發布驗收待完成：資料提交 SHA、對應 Actions completed/success、公開狀態 JSON 與驗收收據另補於 [`PATROL_2026-10-11_0300_RECEIPT.md`](PATROL_2026-10-11_0300_RECEIPT.md)。在驗收完成前不宣稱已上線。
