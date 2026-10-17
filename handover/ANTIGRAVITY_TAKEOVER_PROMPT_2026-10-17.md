# 可直接貼給 Antigravity 的接手提示詞

**僅使用Antigravity桌面版，不需要啟動agy CLI。任何未確認的功能、設定或選擇先問使用者，不自行推測。**

請先在Antigravity桌面版新增／開啟資料夾：`/Users/eric/aiwork/taiwan-opera-calendar`。本文件分成三階段；先貼第一階段。第二、三階段是接手操作時才使用的明確工作指令，不能因文件存在就自動執行。

## 第一階段：先讀懂、盤點與試讀

將以下整段貼進Antigravity新對話：

```text
我要把「臺灣戲曲情報站」交給Antigravity桌面版維護，後續不再依賴GPT訂閱，也不使用agy CLI作為日常操作入口。任何不確定的事情先問我，不可自行猜測；不要把CLI曾測得的模型或功能當桌面版已確認事實。

我授權你在這個Antigravity對話中讀取這個專案和交接文件，用Antigravity所選模型理解它們；只讀本次工作需要的內容，不讀取或傳送token、cookie、Keychain、登入憑證、.env或其他個人資料。這個階段只做唯讀核對與必要測試，不修改程式／正式資料／規則／排程，不提交／推送、不對外發文或留言。

正式資料夾：/Users/eric/aiwork/taiwan-opera-calendar。
舊的 /Users/eric/.gemini/antigravity/scratch/taiwan-opera-calendar 也是Git repo，但不是現用專案；不要開錯、不要覆蓋或刪除它。

請先任務分級，選最低足夠的實際可用模型。先完整讀：
1. handover/ANTIGRAVITY_HANDOVER_2026-10-17.md
2. handover/ANTIGRAVITY_FEASIBILITY_2026-10-17.md
3. handover/PROJECT_SNAPSHOT_2026-10-17.json
4. PATROL_OPERATIONS.md
5. PATROL_2026-10-17_0300_INDEPENDENT.md
6. PATROL_2026-10-17_0300_RECEIPT.md
7. patrol_runs/2026-10-17_0300.json
再按需要讀原始碼、當前資料與名單。舊PROJECT_HANDOVER與ISSUES_REVIEW含過時排程，不可照抄。

請用真實工具核對：
- cwd、Git HEAD、remote/upstream、staged及unstaged檔名，保留既有使用者修改；不要git add .或清工作區。
- schedule卡片數、verified/community/pending數、endDate數、兩個社群名單數與候選數。
- 最新public status、metadata、資料SHA的matching Actions，以及與目前repo檔案的內容對照。
- 03:00社群代理巡檢與GitHub07:00 updater的不同；resume會清除finalized/publication，不能拿它當查詢。
- 本機實際能執行的模型、terminal、HTTP、本地preview和browser工具。不要只根據官方文件宣稱工具可用。

如工具可用，以只讀公開方式實際測Threads與Facebook各一個名單帳號：讀正文、日期、置頂與附圖，報告哪些成功、哪些媒體／分頁仍未讀。不要登入、Follow、發文、留言、解captcha或匯出cookies；需要初次Chrome偵錯或新權限時具體說明原因與作用範圍。原始貼文直連只能算該貼文，不是整個帳號完整覆蓋。

必要時可執行python3 -m unittest -v、node --check assets/app.js、git diff --check；不要為了檢查直接執行會改正式資料的updater.py，也不要finalize測試輪蓋掉公開status。

輸出繁體中文接手盤點，逐項分已實測／失敗／未驗證，列當前值與交接快照差異、可接手項目、需處理的工具或排程前提，附可重現證據。完成前採質疑者視角檢查是否開錯repo、誤改資料、漏讀來源或把publication verified誤當coverage complete。

不要只回「我已閱讀、可以接手」；請給實際工具結果。不要在這個階段直接建立或啟用每日排程。
```

首次期望值只是2026-10-17快照：HEAD d115a05、96卡、41 verified/55 community、Threads10/FB9、21目標、coverage failed、publication verified。日後有新更新可以不同，需說明證據，不能硬改回快照。

## 第二階段：手動完成一輪正式營運驗收

確認第一階段工具可用、準備正式巡檢時貼以下指令；這段會授權本輪資料與發布，不是第一階段的隱含動作：

```text
請在正式repo手動執行一次臺灣戲曲獨立巡檢，完成到公開驗收和收據。

本次授權：公開資料讀取、依原始證據編輯當輪演出資料、產生巡檢紀錄與狀態、必要測試、只提交及推送本輪明列檔案、查matching Actions、比對公開三JSON及執行verify、推送驗收收據。保留所有原有工作區修改。對外留言／發文、關閉Issue、改全域設定或排程、遷站與DNS不在本輪授權內。

先完整讀PATROL_OPERATIONS.md與交接手冊。先確認沒有其他代理正寫同一輪；新一天init新輪，同日確實要補讀才resume原輪。先完成最新動態名單每個來源的初次嘗試，再處理未完成項。每次嘗試即record，保存時間、方法、公開網址、正文與媒體範圍及失敗原因。

近7天與仍有效置頂／月份戲路、全部Issues狀態／留言／分頁、文化部候選與去重都要交代。初次後最多再試3次；連續2次相同故障先診斷換路徑；3個同平台帳號同故障先查共同環境，但其他來源仍各自嘗試。不將單篇或其他公告冒充整個帳號完整覆蓋。

未知保留未公布，社群仍community，同場保留一張卡及來源。不確定／衝突先候選。summary查漏、finalize產生真實狀態；來源failed可正常發布失敗狀態，不為了好看改complete。

發布先fetch並比較遠端updater提交，安全整合，禁止force push；只stage本輪明列檔案，檢視cached diff。保存完整資料SHA，查該SHA的真實Actions run，待completed/success，再核對公開schedule/metadata/patrol_status原始內容。執行patrol_progress.py verify並另留收據；遇dispatch可能改資料須核實際自動提交與hash。收據／run JSON可用獨立skip-ci稽核提交，但公開資料SHA不改報成稽核提交。

最後如實分列來源覆蓋、資料新增／更正／未採納、push、Actions、公開驗收、未完成範圍及恢復方法。不能只留下本地結果稱上線。完成前以fresh-context合適能力審核者查真實證據，不靠自身敘述背書。
```

## 第三階段：持續每日03:00排程切換

在手動營運驗收完成、你決定正式切換時，再貼：

```text
請提出並準備本專案Antigravity持續每日巡檢排程的具體設定與差異，目標為Asia/Taipei每天03:00、唯一日常社群巡檢。

使用正式repo /Users/eric/aiwork/taiwan-opera-calendar。先確認目前桌面版實際提供的持續排程介面與功能，不能猜按鈕位置、功能名稱或時區；不能用只活在當前conversation的schedule冒充持續排程。若桌面版沒有合適功能，先問我，不自行改用agy CLI、sidecar設定檔、launchd或其他平台。每輪用新對話讀PATROL_OPERATIONS.md和交接文件、動態名單、可恢復JSON；保留初次／重試規則與精確SHA/public驗收。模型選擇須以當前可用列表及實測品質決定，記錄實際模型，不照抄Codex的Luna ID。

先查現有Antigravity排程／規則和Codex Automation 07-00-19-00現況，準備可review的實際檔案／UI差異、projectId、cwd、prompt、權限、next trigger完整日期與UTC offset、模型、通知、停用與回復步驟。先不要變更。全域config只能合併必要項，不能整檔覆蓋。

切換需我確認具體設定後執行：確認原Codex沒有巡檢在跑，再停用原03:00日常排程，最後啟用一個新排程。不要重啟舊threads heartbeat；不要停掉GitHub07:00 updater。正式設定啟用後，驗證下一次實際03:00觸發，App／主機重新啟動或離線／睡眠後行為、單輪互斥與resume方法。前5輪逐輪查漏項、紀錄、恢復、發布與通知品質，外部來源失敗須如實failed／partial。
```

這個分階段設計讓你能先審查接手成果，再進行持續設定變更；不需要重新講一遍所有專案脈絡。
