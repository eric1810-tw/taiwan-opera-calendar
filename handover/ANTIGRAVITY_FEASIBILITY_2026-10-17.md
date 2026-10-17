# Antigravity 接手可行性評估

評估日期：2026-10-17，Asia/Taipei。評估範圍是接手現有臺灣戲曲情報站的維護、來源審核、巡檢與發布。這不是以重寫網站來替代交接，也不是已完成新平台上線驗收。

> 使用者執行偏好已確認：**只由Antigravity桌面版接手，不以agy CLI作為使用者入口**。所有未確認事項須先問使用者；桌面版功能不得由CLI測試結果推定。

## 1. 結論與判定程度

**Antigravity具備接手這個專案所需的基本工具能力，網站和GitHub更新流程也沒有GPT訂閱依賴。一般程式／資料維護可以移交；每日03:00無人值守社群巡檢則需要重新建立排程、授權與瀏覽器環境，經實測後才可稱完整接手。**

目前證據不足以說「已經100%取代且每天一定讀完所有來源」。缺的是新平台的真實執行與營運驗收，不是靜態網站需要OpenAI。即使留在Codex，近期也只有部分社群內容可讀；換平台不會自動解除Meta登入牆、媒體限制或來源矛盾。

本次完成了源碼與流程盤點、live網站／GitHub核對、已安裝Antigravity與CLI的版本確認、真實可用模型清單查詢。**沒有執行Antigravity專案代理、瀏覽器、排程或部署試跑。**

## 2. 實際已取得的證據

|證據|實讀結果|能證明／不能證明|
|---|---|---|
|網站原始碼與updater|靜態HTML/CSS/JS、Python標準函式庫、GitHub Actions/Pages|可移植；沒有OpenAI推論API的runtime需求|
|本機App|`/Applications/Antigravity.app`，2.23.1|已安裝；不證明每項官方新功能都在目前介面可用|
|CLI|`/Users/eric/.local/bin/agy`，1.3.2，help成功|程式可執行；不是模型推論已成功|
|`agy models`|沙箱外exit0，真實取得模型列表|服務可取得可用模型；不證明額度、browser、所有工具已驗收|
|模型清單|原始ID：`gemini-3.8-flash-high/medium/low`（三個）、`claude-sonnet-4-6`、`claude-opus-4-6-thinking`、`gpt-oss-120b-medium`|僅歷史CLI可見選項；不從ID補推理模式，不證明桌面版選項／額度／推論已測，也不保證未來相同|
|GitHub與Pages|main=`d115a05…`；資料SHA=`b33144e…`的Actions成功；公開三JSON和本地一致|現有平台已發布；不是由Antigravity發布成功|
|GitHub CLI|在可連網環境登入exit0；Git push本回合成功|可沿用本機既有授權前提；新代理仍需工具權限|
|專案代理唯讀試跑|自動核准審查拒絕，未啟動|不能把計畫當成完成，亦沒有模型實際讀本地專案的結果|

試跑原訂讀取repo文件及資料；自動審查認為目前授權未明確涵蓋向外部Gemini傳送本地專案內容而拒絕。後續官方FAQ亦明示consumer方案不支援把`agy`包在第三方coding agent內使用。因此本交接採**讓使用者直接在Antigravity桌面版啟動**，不由Codex包裝它作後端。

## 3. 按工作項目評估

|工作|可行性|接手所需條件與驗收|
|---|---|---|
|讀／改HTML、JS、CSS、Python|高|正確開現用repo，遵守使用者既有修改，做diff／測試|
|編輯schedule與來源連結|高，但需專業判斷|逐欄原公告證據、未知保留、community、不重複、異動審查|
|本地preview與測試|高|終端、Python/Node和localhost權限；真實跑過，不能只寫測試會通過|
|Git提交、整合遠端、push|高，授權條件式|現有Git憑證可用，代理需正式命令／網路授權；安全處理updater分歧|
|Actions／公開JSON驗收|高|讀GitHub API/Pages，精確SHA與run、原始檔雜湊、verify|
|文化部候選分類|工具上可行，需實測完整性|讀全API、解析showInfo、去重；截斷回應不能當全部已讀|
|Threads文字巡檢|條件式|正確帳號、實際日期＋正文、置頂、分頁；工具與平台限制照實留證|
|Facebook海報與影片|條件式，風險較高|browser可讀媒體，逐張核對；登入牆／灰圖不能推定沒消息|
|Issues全狀態巡檢|高|state=all、分頁、排PR、正文／留言與活動；對外留言需另有授權|
|03:00持續巡檢|官方有對應機制，本機桌面介面未驗證|先確認桌面持續排程入口、工作路徑／時區／模型／權限和實際跨日觸發；功能不明先問，不自行安裝sidecar或改用CLI|
|中斷後resume|專案工具可沿用|理解resume清除finalized/publication；不覆寫原證據，先保留JSON|
|無人值守遇權限／額度／睡眠|未驗證|錯誤通知、保留進度、補跑、單輪鎖、重啟後持續；官方功能名稱不等於SLA|
|完整繼承Codex聊天／個人排程|不能直接假設|需用本文件／repo紀錄轉成規則；舊排程要另外切換，cookies不轉移|
|改用Cloudflare|與換代理無必然關係|目前不是必要工作；另行帳戶、域名、bot提交觸發和部署驗收|

評估中的「高」是工作適配性，不是實測通過率；沒有用沒有根據的百分比替代缺失證據。

## 4. 產品能力查證與適用邊界

Google官方將App、CLI與IDE分開。App／CLI有[Chrome browser command](https://antigravity.google/docs/commands/browser/)，IDE的瀏覽器機制另述；本機目前的瀏覽器連接、Google Chrome、首次偵錯授權與社群可讀性都需原生環境實測。不能假設既有Edge／Codex登入會直接繼承。

[Rules文件](https://antigravity.google/docs/rules/)提供持續專案指令的載入方式，因此可以把本專案約束變成可攜規則；但本repo尚無實體AGENTS.md，聊天規則並不會自動搬移。

[Schedule文件](https://antigravity.google/docs/commands/schedule)區分conversation計時與持續Automation；本專案應評估[持續sidecar](https://antigravity.google/docs/sidecars)。其定義可跨session保存，並不等於機器關機仍會執行。03:00的scheduler時區、App重啟、睡眠前後和補跑行為尚需確認；本機桌面版實際排程入口也未確認，必須向使用者釐清，不自行安裝sidecar。

[Permissions文件](https://antigravity.google/docs/permissions)說明它也有命令沙箱與網路／瀏覽器權限。從Codex移出不保證完全不會再遇到「瀏覽器能上網、終端網路受限」。應在Antigravity中依允許範圍解決，不全域關閉權限控制。

官方[FAQ](https://antigravity.google/docs/faq/)只說代理執行時防止睡眠，並非已睡眠機器的喚醒保證；同頁也限制consumer方案把CLI包進第三方代理。使用者可直接使用原生Antigravity來接手。

## 5. 訂閱、額度與費用

停止GPT訂閱，**不會因而停掉已部署的GitHub Pages、GitHub repo或既有GitHub Actions資料更新器**。它們有自己的帳戶、服務條件與權限。這不是保證這些外部服務永不變更，而是現有架構沒有把GPT訂閱作為網站runtime的前提。

原03:00 Codex代理巡檢不能被視為訂閱結束後仍有保證的執行資源，需切換到Antigravity的可用額度。Google帳戶方案、模型和配額與GPT分開；官方[方案說明](https://antigravity.google/blog/changes-to-antigravity-plans/)也會變動。本次沒有讀你的帳務／剩餘額度，不主張免費額度一定足夠，不建議先為本專案購買昂貴方案。

先用可見的Flash做固定清單／進度紀錄與簡單維護，對重大來源衝突或資料發布改用足夠模型審核；保留實際耗用與完成紀錄。前5輪再依實際讀取量、失敗重試、模型和耗用判斷是否需要其他方案。模型可用列表不能換算成一個未量測的每月金額。

## 6. 建議採用的接手方式

1. **先保持現站與GitHub流程，直接打開目前repo。** 開新framework／重建資料庫會增加搬移風險，沒有必要。
2. **原生Antigravity直接接手。** 不透過Codex持續呼叫Antigravity CLI；GPT到期後也無須維持這種轉接。
3. **先建立可讀的工作知識，再試跑。** 使用詳細手冊、snapshot與首次提示詞，完成正確路徑、數量、最新發布和未提交修改的核對。
4. **一次手動巡檢與發布。** 真正測讀社群正文／媒體、進度JSON、原文查證、測試、push、matching Actions和公開資料；外部失敗能正確保存也是驗收項。
5. **最後切03:00持續排程。** 停用舊Codex每日排程後只啟一個新排程；前5輪逐輪檢查，GitHub07:00 updater維持獨立。

初次讀檔與瀏覽器試跑應直接由你在Antigravity貼上附檔提示詞開始。這能同時確立你對新平台讀取專案的授權，也遵循原生使用方式。

## 7. 哪些條件會阻止「完整接手」

|阻礙|處置|
|---|---|
|本機App其實沒有所需持續排程介面|查明桌面版實際能力後詢問使用者，不能自行改用CLI或其他排程；不能只用conversation timer充數|
|模型／工具一直停在需人工批准|只授予已同意任務必要且有限的範圍，做無人值守測試；不能先宣稱全自動|
|社群持續不可讀|照實failed／partial、換合法公開途徑核特定場；不保證換模型能解除來源限制|
|工作區指向舊scratch|立即停止寫入並核對現用repo；舊獨有提交另審，不直接merge整份舊站|
|額度不足|記實際耗用，縮減重複上下文／無效重試，必要時改可用模型或由使用者決定方案|
|主機／App不在觸發時可用|保持舊結果可公開辨識、明確通知及恢復方法；若需常駐主機要另規劃，不聲稱本地排程=雲端服務|
|資料可推送但公開狀態舊|依精確SHA、Actions、public三JSON拆查，未過不稱上線|

## 8. 正式接手的通過條件

以詳細手冊第17節清單驗收。最少需：一輪真實手動流程、一次matching SHA發布、一次真實03:00持續觸發、一次同輪恢復證據、排程重啟／補跑及權限行為確認，再觀察前5輪無靜默漏項。

這裡「完整」指所有工作責任都有接手者、必要工具及可恢復流程；**不要求把來源不可讀硬改為complete**。如果Antigravity能保留正確failed狀態、證據、通知和已驗收發布，它可以是合格營運結果；如果只說讀完但沒正文／媒體證據，即使終端命令都成功也不合格。

## 9. 本次已完成與仍待做

已完成：交接手冊、現況證據、來源／未完項清單、啟動提示詞、搬遷及驗收計畫、官方功能查證、本機版本與模型清單、live repo與公開資料核對。

待使用者直接在Antigravity進行：模型真實推論與專案讀取、瀏覽器／海報試讀、規則實際載入、完整巡檢／發布試跑、持續排程建立與時區／每次觸發確認、前5輪品質觀察。本次沒有改網站程式、正式資料、舊排程或Antigravity全域設定。
