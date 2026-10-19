# Threads 監看清單調整

- 執行時間：2026-10-05T09:36:34+08:00（Asia/Taipei）。中複雜度：明確清單修改與近期資訊價值判讀。
- 使用者指定新增 hilang.on.tour；指定移除 emily19911212、rouhesper_ch0706、liu_0130__、sn_kiter。16−4+1＝13帳號；Facebook仍6帳號，合計19。保留其他帳號及原順序，新帳號加在末尾。
- 已即時讀 https://www.threads.com/@hilang.on.tour 載入後首頁，頁名「戲籠出巡｜臺灣傳統戲曲巡演」。實讀首則 https://www.threads.com/@hilang.on.tour/post/Dd-e4j4E8y4 及續文：古都木偶《三俠五義之鍘龐昱》2026/10/8桃園蓮華寺、19:00扮仙／19:30正戲。此場已有卡，不新增場次。本次只確認帳號可讀與有實際演出預告，未完整巡檢歷史、多圖、留言。
- 評估依據為PATROL_2026-10-03_1900_INDEPENDENT.md、PATROL_2026-10-04_0700_INDEPENDENT.md、PATROL_2026-10-05_0700_INDEPENDENT.md的實讀紀錄；今天07:01首頁範圍：h.akito_1996為9/27鍘美回顧及續文；whidu1124為9/27創作回顧及2025/8舊文；su._1023為9/28生活與9/21–22回顧；c910303為9/27貓、9/25中秋、9/21回顧。這4個是可精簡候選，未經使用者指示不移除。
- 不能從近期回顧推論「從未發表演出資訊」。1013.yr_近期也多回顧，但原為演員工作帳號；xuefeng_lu_及taiwaneseopera168近期多媒體／文化／觀後感，外連未全部讀，不宣稱沒有資訊。
- 高直接資訊價值的保留來源：joe_huang_k_w、hilang.on.tour有巡演日期與時間；the_rin.lpm有未來戲路；wu.yi0722、yuzhongluo有個人行程／異動但需判讀；jing__1017有密集場次線索及原來源連結。
- 對抗式驗收：JSON解析、帳號唯一性、差集合及數量檢查PASS，證明只移除指定4個且只增加1個。既有schedule、metadata及patrol_status均未改，不冒充完整巡檢。僅提交本清單與日誌；既有2 modified／3 untracked他人檔案保留。不改排程，下一輪依PATROL_OPERATIONS.md動態讀清單。

## 推送驗收

首次push因遠端每日資料提交14fbe3af2af974494674987eff08717d47c722a5而拒絕；唯讀檢視確認只改schedule／metadata，合併後逐位元確認兩檔與origin/main一致，未回推舊資料。監看調整提交297cae4c4ded99fc30d054447a15e9104dd1c973、整合提交de01fcf2c30bcecab11c118203a0d0f28cd3d830已推送，ls-remote與本地SHA一致；JSON再次確認13帳號及精確指定增刪。均為[skip ci]，清單不在公開站發布白名單，本次不觸發無關網站部署；下一輪實際執行尚未發生。

## 使用者第二次精簡

2026-10-05T09:42:08+08:00：使用者明確保留h.akito_1996，移除whidu1124、su._1023、c910303。本次只調整巡檢清單，未操作Threads平台追蹤按鈕。JSON解析、唯一性、精確差集合及保留帳號驗收PASS；13→10 Threads，Facebook仍6，共16。演出資料及巡檢狀態不改；其他工作區修改保留。

## 移除吳奕萱及改為每日03:00

- 設定核對時間：2026-10-05T09:45:11+08:00。使用者要求移除wu.yi0722及每日巡檢改03:00一次；清單10→9，Facebook仍6，共15。此為監看清單移除，未操作Threads平台追蹤。
- 使用排程管理工具更新既有id=07-00-19-00，保留cron、ACTIVE、project/local、gpt-6.1-sol/medium、原巡檢要求及舊heartbeat不重啟條款，名稱改「臺灣戲曲獨立巡檢（每日03:00）」，每日03:00，prompt明列Asia/Taipei且每日一次。工具回傳Updated且ACTIVE；重新讀automation.toml，name/prompt/rrule及保留欄位均與要求一致。
- PATROL_OPERATIONS.md同步改每日03:00，保留其餘要求；GitHub Actions的07:00網站自動資料刷新是另一個工作，未修改。
- 對抗式驗收：JSON解析及精確差集合PASS，確認只移除wu.yi0722且h.akito_1996保留；schedule/metadata/patrol_status未因本次設定更新而刷新，舊巡檢日誌維持歷史時間。僅提交清單、操作文件及本日誌，其他工作區修改保留。
- 依目前Asia/Taipei日期時間，新設定的下一個時段為2026-10-06 03:00；尚未發生，不能稱新時間已實際觸發。

## 新增戲籠出巡Facebook

2026-10-05T14:32:38+08:00：使用者指定https://www.facebook.com/profile.php?id=61594936681482。本次瀏覽器實讀載入後首頁，頁名「戲籠出巡｜臺灣傳統戲曲巡演」，自介列巡演消息、劇目介紹、演出紀錄，並连至sites.google.com/view/hilang-re/及Instagram hilang.on.tour；近期可見官網上線貼文。確認帳號可讀及身份後加入清單，原6筆逐筆保留、handle唯一性與JSON檢查PASS。Threads仍9，Facebook6→7，共16。本次未全讀貼文／圖片，不新增場次、不刷新巡檢時間；下一輪每日03:00動態讀取，不改排程。僅提交清單及本日誌，其他修改保留。
