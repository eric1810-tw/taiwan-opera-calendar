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

只有新核實場次、重要更正、需處理的 Issue、巡檢失敗、狀態發布失敗或需使用者決策時通知；沒有可行動變更且狀態成功發布時可保持安靜。`partial` 不是「無新演出」。

## 同場來源整合與詳情連結

- 同一節目被不同帳號先後分享時，依日期、場地、劇團及劇目辨識同場並合併，保留舊公告於 `relatedSourceUrls`。
- 每次核對也重新比較卡片右下方的 `link`：以劇團官方消息為優先，選擇該場最新有效、資訊完整的公告；主辦方提供更新或更完整的場次專頁、交通、直播及異動資訊時，核對後可改連該專頁。不得永久固定最早發現的轉貼。
- 不是只看發布時間：新轉貼不能凌駕官方，無關場次或較新但內容較少的貼文不取代有效詳情。若官方消息互相衝突，先核對異動、標明差異，證據不足保留待查。
- `link` 是讀者詳情入口；`sourceUrl` 是核實依據，可不同。更新詳情連結不代表提升來源可信度，`verifyStatus` 仍依實際證據分類。

## 後續變更與搬遷驗收

- 加巡檢帳號：更新相應的 `data/*_accounts.json`，確認公開帳號網址可讀，下一輪排程會自動讀新清單；不必改排程文字。
- 改網站：在新工作階段指定本專案及此文件，按需求修改、測試、推送並核對公開頁。單次改站不取代每日巡檢。
- 舊 heartbeat 只有在新獨立排程**實際執行**、留下狀態與巡檢紀錄，且推送和公開站已核實後才能停用。單純建好排程不算搬遷完成；若驗收未過，保留舊排程運作，避免巡檢中斷。
