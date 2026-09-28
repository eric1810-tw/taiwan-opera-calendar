# 演出資訊回報：GitHub Issues 巡檢與處理

回報入口會開啟此儲存庫的 [Issues](https://github.com/eric1810-tw/taiwan-opera-calendar/issues)。訪客必須登入 GitHub 並在 GitHub 按「Submit new issue」；網站本身不接收或儲存表單。切勿將「開啟預填頁」當作「已送出」。

## 巡檢範圍

現有「臺灣戲曲 Threads 與 Issues 巡檢」排程每天台北時間 07:00、19:00，同時查看本儲存庫所有新建或更新的 Issues（包含留言、重新開啟與關閉；排除 Pull Requests）。以 GitHub 公開頁面或 `GET /repos/eric1810-tw/taiwan-opera-calendar/issues?state=all&sort=updated&per_page=100` 唯讀取得，必要時翻頁；API 不通時改用瀏覽器，不得把巡檢失敗當作沒有回報。記錄 issue 編號、網址、`updated_at`、審核結果與處理版本，避免漏看或重複處理。未變更時可保持安靜。

## 處理順序

1. 先讀回報及後續留言，核對 `data/schedule.json` 的日期、場地、劇團、劇目與來源；比對是否同場或已更正，保留回報原文與連結。
2. 查原始公告及最新的劇團、主辦、場館、文化部或售票頁；區分已證實、僅社群線索、矛盾與無法核實。取消、延期及時間／地點異動不得僅靠匿名回報直接改正式資料。
3. 有足夠證據才修正 `data/schedule.json`，保留來源與核實狀態，驗證 JSON/schema、去重、日期及頁面呈現；推送後驗證 GitHub Actions 和公開網站資料。若推送、登入或網路失敗，保留本地結果並明示未上線。
4. 能在 GitHub 回覆時，附上查證來源、處理結果及已部署版本；無法核實時標為待查並說明缺哪些證據，不要捏造。需要帳號權限或使用者決策時通知使用者。只有確認問題已處理且網站已更新後，才將 Issue 標記完成。

## 初始基線

- 2026-09-28：公開 GitHub API `state=all` 查詢回傳空陣列；當時沒有可見的 Issue。這只是當次快照，不代表日後無人回報。
