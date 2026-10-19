# 2026-10-18 17:25 臺灣戲曲獨立巡檢

- 實際開始：2026-10-18T17:38:53+08:00（Asia/Taipei）。本輪動態目標21項：Threads 10、Facebook 9、文化部候選1、GitHub Issues 1。
- 最終覆蓋：**failed**（1 complete、19 partial、1 failed）。完整逐次時間、方法、網址、正文/媒體範圍、故障原因及候選處置見 [`patrol_runs/2026-10-18_1725.json`](patrol_runs/2026-10-18_1725.json)。
  - Threads `1013.yr_` 個人頁重定向至登入畫面，無法讀取個人檔案正文或動態，保留 failed。
  - GitHub Issues complete（2 open、0 closed，#1 與 #2 均已審核建檔，無新回報）。
  - 其餘 19 個目標（Threads 9、Facebook 9、文化部 1）均有部分可讀，但受限於未開啟所有相簿海報或未完成逐筆人工核查，照實記錄 partial。未將部分可讀推論成無新資訊。
- 工作區既有未暫存與未追蹤檔案（`ISSUES_REVIEW.md`、`PROJECT_HANDOVER.md`、`patrol_runs/2026-10-16_0300.json`、`CLAUDE_AUDIT_2026-09-30.md`、`CLOUDFLARE_HANDOVER.md`、`CODEX_TASK_REVIEW_FIXES_2026-09-30.md`）全程保留，嚴格禁止 `git add .`。

## 來源覆蓋與處置

- Threads 10 帳號均已巡檢（透過獨立設定檔無頭 Edge 載入）：
  - `joe_huang_k_w`：讀取約 3,361 字元，載入團長工作短文與女兒探班動態，未見新演出公告；部分海報圖片未展開，標 partial。
  - `h.akito_1996`：讀取約 2,686 字元，成功載入置頂 2026-09-26 鍘美藝術節心得長文，無未來新檔期；近 7 天未全讀，標 partial。
  - `the_rin.lpm`：讀取約 2,250 字元，置頂 2026-09-26 預告秀琴《玉石變》與《金沙灘》（均已在表）；後續 feed 未全讀，標 partial。
  - `1013.yr_`：頁面載入直接重定向至登入畫面（Threads•登錄），無法取得使用者檔案與貼文，標 failed。
  - `xuefeng_lu_`：讀取約 1,163 字元，多為時事與公益轉貼，無新戲曲演出檔期；影片與圖媒未逐一開啟，標 partial。
  - `yuzhongluo`：讀取約 586 字元，載入團長動態與鍘美藝術節貼文；圖媒未全開，標 partial。
  - `taiwaneseopera168`：讀取約 2,497 字元，載入歌仔出少年賞戲筆記與明華園相關動態；圖媒未逐一開啟，標 partial。
  - `jing__1017`：讀取約 921 字元，置頂 10/24 嘉義市文化公園戲棚下逐星路講座已在表；圖媒未逐一開啟，標 partial。
  - `hilang.on.tour`：讀取約 1,603 字元，載入戲籠出巡演出理念與竹南運動公園公演公告（已在表）；圖片未全部展開，標 partial。
  - `yolin1991`：讀取約 665 字元，載入劇團幫手生活短文，未見新演出檔期；照片未逐一開啟，標 partial。

- Facebook 9 帳號均已巡檢（透過無頭 Edge 載入）：
  - `sunhope.fans`（尚和歌仔戲劇團）：讀取約 505 字元，專頁置頂與簡介正常載入；未全讀近 7 日 feed 與戲路表，標 partial。
  - `HsiaoHsiYuan1913`（小西園掌中劇團）：讀取約 250 字元，粉專頁首與藝文訊息正常載入，10/30 與 11/1 演出已在表；標 partial。
  - `100063868113954`（吳奕萱 Wu-Yihsuan）：讀取約 404 字元，載入粉專頁首自介與演出歷練短文，無新正式檔期；標 partial。
  - `MingHuaYuanTianTaiwaneseOpera`（明華園天字戲劇團）：讀取約 434 字元，粉專頁首自介正常載入，近期演出公告與現有卡相符；標 partial。
  - `61574134933376`（繡花園戲劇團x明華園地字戲劇團）：讀取約 460 字元，載入粉專自介與潮州演出相簿，無未來新演出公告；標 partial。
  - `mhysun`（孫翠鳳）：讀取約 263 字元，粉專頁首自介正常載入；高雄等演出均已在表，標 partial。
  - `61594936681482`（戲籠出巡｜臺灣傳統戲曲巡演）：讀取約 417 字元，置頂與巡演消息正常載入，與現有竹南卡相符；標 partial。
  - `lanyang.opera`（蘭陽戲劇團）：讀取約 322 字元，精選 10/26 龜山顯安巖《錯配姻緣》演出與現有卡相符；標 partial。
  - `Taichungpuppettheater`（台中木偶劇團）：讀取約 405 字元，精選 11/7《聖劍風雲三》及 11/1 布袋戲科技講座均在表；標 partial。

- 文化部全類別 Open Data API：
  - 成功連線官方端點（`SearchShowAction.do?method=doFindTypeJ&category=all`）載入 1,480 筆活動；依關鍵字篩選出未來 90 天戲曲候選共 29 筆。因尚未逐筆人工核實售票海報，保留於候選清單，標 partial。

- GitHub Issues：
  - 透過 `gh issue list --state all` 唯讀審視全儲存庫全部 Issues，排除 Pull Requests。
  - 目前維持 2 筆 open、0 筆 closed：#1、#2 之走戲人節目均已建檔入表（`zx-2026-11-14-kuliniao`、`zx-2026-11-15-longnu`），無新未處理回報；標 complete。

## 本輪資料與驗收

- 場次維持 98 張，無新增或更動。
- 單元測試：`python3 -m unittest -v` 18 項全數通過；`node --check assets/app.js` 與 `git diff --check` 通過。
- 資料 commit：`597da80276e9780bcc954f36a139552b89695574`。
- GitHub Actions daily-update run：`39116572530` 成功（completed/success）。
- 規程驗收：`python3 scripts/patrol_progress.py verify --run patrol_runs/2026-10-18_1725.json --sha 597da80276e9780bcc954f36a139552b89695574 --actions-run 39116572530` 成功驗收（`publication.state="verified"`）。
- 6 個受保護檔案 SHA-256 全程完好一致。
