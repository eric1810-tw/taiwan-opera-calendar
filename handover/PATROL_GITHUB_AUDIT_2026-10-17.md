# 每日巡檢是否已進入GitHub：逐輪證據核對

核對日期：2026-10-17，Asia/Taipei。範圍是repo內現存10/9～10/17九輪機器進度，不宣稱更早全部歷史皆完成驗收。重新fetch的遠端main為`d115a052095ed4bcdc0a32a1deada7671fb36796`；這是本次交接文件提交前基線。API／公開三JSON重查時間及輸出節錄存於[機器證據](PATROL_GITHUB_AUDIT_2026-10-17.json)。

## 使用GitHub不代表每次本機存檔自動上傳

流程是：代理在本機讀來源與修改檔案 → commit保存一批變更 → push送至GitHub repo → Actions部署白名單資料至Pages → 核對公開資料及保存收據。每一步都可能未執行或失敗。

因此「專案使用GitHub」與「剛新建的交接文件當時尚未commit/push」可以同時成立。03:00巡檢的既有規程本來就要求每輪推送紀錄、本輪JSON與狀態檔，但歷史上確有推送受阻、延後補推及收據狀態被後續操作清除，不能宣稱每天03:00都已準時且完整發布。

## 目前遠端保存與歷史驗收

下列九輪JSON、巡檢報告及收據均已存在重新fetch的遠端main。表中「成功」指發布證據，不表示社群全部讀完；資料仍可能failed或partial。

|輪次|遠端JSON目前publication|發布證據與限制|
|---|---|---|
|10/9|verified|資料`ffb104a`，Actions `37830259024`；本次API確認同SHA completed/success；歷史JSON留有公開status驗收|
|10/10|verified|資料`16adf82`，Actions `38005309417`；同SHA completed/success；歷史驗收時間07:39，不能稱03:00準時發布|
|10/11|verified|資料`4e86509`，Actions `38078301761`；同SHA completed/success；歷史JSON留有公開status驗收|
|10/12|verified|資料`cd6bd23`，Actions `38166376833`；同SHA completed/success；歷史驗收時間10:02|
|10/13|verified|資料`a764929`，Actions `38415095773`；同SHA completed/success；歷史驗收時間22:39|
|10/14|blocked|資料`9c9efc9`及紀錄現已在遠端歷史；本次按該SHA查Actions為0筆，缺該輪獨立部署／公開驗收證據|
|10/15|pending|原資料`d8f9695`、Actions `38654981372`同SHA completed/success；原收據和Git歷史證實曾verified，後來跨日操作清除欄位，詳下一節|
|10/16|blocked|資料`553041c`及紀錄現已在遠端歷史；本次按該SHA查Actions為0筆，缺該輪獨立部署／公開驗收證據；本機JSON另有既存未提交修改|
|10/17|verified|整合資料`b33144e`、Actions `39035784418`同SHA completed/success；本次重新取得公開三JSON，與本機及已發布資料一致|

舊輪的公開URL現在已被10/17覆蓋，無法用今天的網站重演每一舊輪的當時HTTP回應。本次對舊輪確認的是「Git中的歷史收據＋目前仍可查的matching Actions」，不稱舊輪公開內容已於今天逐一重播驗證。

## 10/15為何有成功收據，JSON卻pending

1. `a127580`保存的10/15 JSON含`publication.state=verified`、資料SHA `d8f9695580da32c3f6249d613c52cc9f72d73d0a`、Actions `38654981372`、驗收時間`2026-10-15T07:36:12+08:00`。本次再次查Actions仍為同SHA、同workflow、completed/success。
2. `553041c`的diff顯示：10/16 `03:04:48+08:00`恢復10/15舊輪，新增一筆吳奕萱來源讀取，finalizedAt改為10/16 `03:17:44+08:00`，原verified區塊被替換成pending。
3. 這是跨日恢復及重新finalize舊輪的歷史操作偏離，不能用它示範日常流程，也不能把pending解讀為10/15從未發布。

本次交接發布只修改handover，不覆寫歷史JSON／收據，也不把它直接改回verified：現在的JSON已含後續來源修改，並不是原驗收版本。完整原版本仍可從Git取得。正確交接方式是保留此對照及原提交，新增一天使用init新輪；不得為修補舊收據把現站status倒退。日後如要修復歷史紀錄結構，需另做明確範圍的變更與驗證，不能刪掉這段歷史。

可重現的唯讀命令：

```sh
git show a127580:patrol_runs/2026-10-15_0300.json
git show 553041c -- patrol_runs/2026-10-15_0300.json
git show origin/main:PATROL_2026-10-15_0300_RECEIPT.md
gh api repos/eric1810-tw/taiwan-opera-calendar/actions/runs/38654981372
```

## 現在公開網站的確定狀態

公開schedule／metadata／patrol_status三檔原始SHA-256均與本機一致；網站資料部署SHA是`b33144e129c91a6aec5c6baaac78d33113519f0a`。公開status為`startedAt=2026-10-17T03:02:16+08:00`、`status=failed`。metadata刷新時間為`2026-10-17T08:57:55+08:00`。

這代表10/17巡檢結果已發布，且誠實顯示來源未完整讀完。先前Git命令受限沙箱的DNS失敗與主機能上網並不矛盾；獲准主機路徑已成功fetch／push／HTTP。不能再沿用「電腦整體斷網」或「token失效」作未經重查的原因。

本次handover文件使用文件專用提交；它們不在Pages artifact白名單，成功推到repo不代表更換網站演出資料或啟用Antigravity排程。
