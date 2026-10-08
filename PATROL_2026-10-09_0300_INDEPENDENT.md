# 臺灣戲曲獨立巡檢｜2026-10-09 03:00（Asia/Taipei）

## 結果

- 巡檢輪次：`patrol_runs/2026-10-09_0300.json`
- 實際開始：2026-10-09T03:01:24+08:00
- 覆蓋狀態：`failed`。20 個動態目標均有結果；1 個 Facebook 關鍵帳號不可讀，Threads／Facebook 其餘 17 個來源僅部分可讀；MOC 與 Issues 完成核對。
- 昨日續跑檢查：工作樹內沒有 2026-10-08 的 `patrol_runs/*.json` 可恢復；因此依規程新建本輪，未把昨日讀取列入今日覆蓋。
- 模型：本次執行環境未提供可核驗的實際模型／推理強度；沒有宣稱已切換至 Luna High。

## 來源讀取與恢復

- Threads：10 個帳號均完成初次帳號頁讀取及一次載入等待後重試；頁面未完整載入近 7 天所有內容，且部分照片、長文或續載未逐項檢查，故皆記 `partial`。羅裕誴最新文直接重開媒體並等待圖片載入，看到光音寺牌樓，未見劇目、時間或詳細地址。
- Facebook：8 個目標均完成初次讀取及一次等待後重試。7 個可讀帳號留 `partial`，因完整帳號續載／所有媒體未讀完；吳奕萱帳號的近期項目顯示「目前無法查看此內容」，另試 posts 頁得到「連結可能損壞或網頁已移除」，留 `failed`。其餘 Facebook 頁可開啟，未見平台共同故障。初次讀取的失敗紀錄於約 03:11 補登，原始嘗試秒數無法還原；JSON 的 `at` 為補登時間，細節已註明，並未偽作原始秒數。
- 文化部：Web 工具與 shell `curl` 連續兩次無法讀 API（工具拒絕 URL；`curl` DNS exit 6）。依規程改用核准的唯讀 Python 網路讀官方 `category=all` API，取得 109 筆；以 `updater.culture_candidates(..., today=2026-10-09)` 篩選近 90 日為 0 筆，並比對既有候選，無新增候選。
- GitHub Issues：Web 工具及 shell `curl` 連續兩次無法讀 API（`api.github.com` DNS exit 6）；改用核准唯讀 Python API，`state=all`、`sort=updated`、`per_page=100` 共 2 筆，並在瀏覽器讀 #2、#1 正文及留言。兩者均 open、留言數為 0；更新時間分別為 #2 `2026-09-28T19:57:36Z`、#1 `2026-09-28T19:54:09Z`。

## 資料核對與變更

- 新吉歌劇團東河宮：依 yolin1991 10/8 貼文及海報補上 10/10 14:30 扮仙、扮仙後午戲、19:00 晚戲與東河宮；劇目仍未公布，維持 `community`。新貼文連結列為詳情，舊貼文保留於 `relatedSourceUrls`。
- 羅文君歌劇團：依羅裕誴 10/8 貼文與光音寺牌樓照片補上「南投縣中寮鄉光音寺」；劇目、時間及詳細地址維持未公布，維持 `community`。
- 尚和 10/11：詳情連結改為劇團最新公告，文化部仍保留為 `sourceUrl` 與 `verified` 依據；核對內容與原卡相符。
- 明華園天字團 10/10：詳情連結改為最新官方貼文；基金會原公告保留為來源並提供原卡演出結束時間。最新貼文確認16:00免費藝文活動及19:00演出；維持原驗證狀態。
- 繡花園／明華園地字：將官方 Facebook 農曆九月行程作為 10/10 至 10/31 八張對應演出卡的最新官方來源；香港天文台日曆及舊 Threads 來源保留於 `relatedSourceUrls`，驗證狀態仍為 `community`。11/4 卡未更新，因該貼文末段截斷，無法讀到對應場次細節。
- 其他讀到的節目與現有卡片重複（尚和、小西園、明華園天字、溪州、秀琴、蘭陽等），沒有重複新增；公視播映表辨識為電視播映，未誤列現場演出。
- 網站資料刷新時間未變更。巡檢開始時間獨立寫入 `data/patrol_status.json`。

## 驗收

- `python3 -m unittest -v`：17 項通過。
- `node --check assets/app.js`：通過。
- `git diff --check`：通過。
- 另以 `updater.validate_schedule` 驗證 113 張卡；日期可解析、ID 無重複、必填欄位及 URL 有效格式檢查通過；確認 `index.html` 載入 `assets/app.js` 且前端讀取 `./data/schedule.json`；社群來源驗證等級未提升；巡檢狀態與來源覆蓋計算均為 `failed`。
- 最終資料 SHA256：`data/schedule.json` `76711b28dd9279f296dd15e38d635a728ddeef62f53dc7715463f61995663d0a`；`data/metadata.json` `c0dd13f63e010d0d11e85353e3a44b75d90fa18b1ae362eb0e677f34e71c6e3e`（未變）；`data/patrol_status.json` `a2c783f1a087420ad8bff0a91673af3052a7bb8e54dccd9a00aeddc41e0883e3`。
- 推送、對應 Actions `completed/success`、公開網站狀態檔比對：待資料提交後驗證；在核對完成前不宣稱已上線。

## 接續事項

1. 對吳奕萱 Facebook 公開頁改用可讀替代路徑或於下輪重試；不可把不可讀判作無新資訊。
2. 恢復 Threads／Facebook 近七天完整續載與未讀媒體核查，再決定是否能把覆蓋狀態從 `failed` 改為其他狀態；不得手動覆寫。
3. 推送本輪明列檔案後，等待相同資料 SHA 的 Actions 完成，執行 `patrol_progress.py verify` 核對公開狀態檔；若失敗，記錄原始錯誤及續跑方法。
