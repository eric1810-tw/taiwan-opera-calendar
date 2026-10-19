# 臺灣戲曲獨立巡檢｜2026-10-15 03:00 輪次

- Run JSON：`patrol_runs/2026-10-15_0300.json`；Asia/Taipei 實際開始：`2026-10-15T07:15:39+08:00`，不是排程時間。
- 動態目標：21 項（Threads 10、Facebook 9、文化部候選 1、GitHub Issues 1）。結果：19 partial、1 failed、1 complete、0 pending；`data/patrol_status.json` 由工具 finalize 為 `failed`。
- 初始工作區觀察：`main...origin/main [ahead 2]`；既有 `ISSUES_REVIEW.md`、`PROJECT_HANDOVER.md` 修改及三個 untracked 稽核／交接檔保留。本輪資料提交只含 run/report/status，未改 `schedule.json` 或 `metadata.json`。推送前 fetch 發現遠端自動刷新提交 `b9384fd`，以 merge commit `d8f9695` 正常整合；這筆刷新不是巡檢資料修訂。
- 執行模型名稱／實際推理強度無法從排程執行環境驗證；不宣稱已切換為 Luna High。
- 巡檢開始時本地資料刷新時間 `2026-10-13T11:18:52+08:00`；整合遠端自動刷新後，推送狀態的 `data/metadata.json` 為 `2026-10-14T09:31:49+08:00`。兩者均與巡檢開始時間 `2026-10-15T07:15:39+08:00` 分開。本輪未呼叫 updater；遠端更新後 schedule 為95張卡。

## 逐來源讀取範圍與結果

下列範圍、網址、方法、媒體狀態與失敗原因以本輪 JSON 各次 attempt 為準；partial 代表仍有帳號內容、圖片或影片未讀完。`yuzhongluo` 的官方節目頁是單一貼文的場次補核，非額外社群帳號重試。

### `threads:joe_huang_k_w` — partial（1 次記錄）

- Attempt 1 `2026-10-15T07:16:09+08:00`；方法 `profile-browser`；媒體 `unread`；網址：https://www.threads.com/@joe_huang_k_w
  - 範圍：近期首页读到10/13晚一篇完整演出公告及一篇10/14非演出争议贴；其后仍显示载入中，未确认最近7天完整分页
  - 結果／未解項目：演出贴列10/30苗栗竹南運動公園大草坪，17:00進場、18:00開演，古都掌中劇團《台灣風雲錄・戰火波瀾》；海報媒體尚未開啟，帳號後續內容未水合，需保留partial。

### `threads:h.akito_1996` — partial（3 次記錄）

- Attempt 1 `2026-10-15T07:16:16+08:00`；方法 `profile-browser`；媒體 `unread`；網址：https://www.threads.com/@h.akito_1996
  - 範圍：初次開啟個人頁，等候介面後主文欄仍全為載入骨架；未讀到近期貼文與媒體
  - 結果／未解項目：Threads 版面外框可見但帳號主文未水合，初次來源讀取失敗；待完成全名單初次檢查後診斷共同環境並換路徑。

- Attempt 2 `2026-10-15T07:16:43+08:00`；方法 `public-search-browser`；媒體 `unread`；網址：https://www.threads.com/search?q=%E5%B8%83%E8%A2%8B%E6%88%B2
  - 範圍：共通環境診斷：Threads公開搜尋頁僅顯示導覽列，沒有結果正文；未登入提示未出現，搜尋路徑也不能提供可讀公開正文
  - 結果／未解項目：三個帳號先後出現個人頁載入骨架；另外joe_huang_k_w同平台頁曾成功讀到兩篇文字，顯示非全站一致故障。現用公開搜尋頁檢查共通讀取環境仍無結果內容，下一步以個人頁/可用索引替代路徑續查，避免相同reload重試。

- Attempt 3 `2026-10-15T07:22:01+08:00`；方法 `profile-browser-wait-7s`；媒體 `partial`；網址：https://www.threads.com/@h.akito_1996
  - 範圍：第二次嘗試等待7秒後個人頁水合；讀到置頂9/26–27鍘美藝術節心得與一篇個人長文，兩篇均超過最近7天；第1篇多媒體顯示1/4且Video player、其餘內容未檢視，feed底部仍載入中，未完成近期7天/置頂媒體覆蓋
  - 結果／未解項目：已證明初次骨架能延遲水合，並非無內容；目前讀到的場景是已結束的鍘美藝術節，未能判定該帳號近7天是否有新公告。

### `threads:the_rin.lpm` — partial（2 次記錄）

- Attempt 1 `2026-10-15T07:16:24+08:00`；方法 `profile-browser`；媒體 `unread`；網址：https://www.threads.com/@the_rin.lpm
  - 範圍：初次開啟個人頁，主文欄保持載入骨架；未讀到最近7天正文及圖片
  - 結果／未解項目：與上一個Threads來源相同，個人頁未水合；先記錄現象，待全名單初次嘗試完畢後診斷共同環境。

- Attempt 2 `2026-10-15T07:22:34+08:00`；方法 `direct-post-media-browser`；媒體 `partial`；網址：https://www.threads.com/@the_rin.lpm/post/Ddy9Vv8k7IV/media
  - 範圍：第二次等待7秒後讀得9/26釘選宣傳與9/27補發戲路圖；11/7新莊保元宮《玉石變》及11/15西港慶安宮《金沙灘》正文可讀，9/27媒體直連顯示第2/2頁，放大可辨10/11–11/8行程多列；底部仍載入中且第一篇海報與其他貼文/圖片未逐項看完
  - 結果／未解項目：目前可見未來行程已包含於藝師/團隊公開候選，仍需逐筆與正式schedule核對；該帳號自述為非官方宣傳手，貼文不能單獨升為verified。其他直接畫面可辨公告包括11/7新莊保元宮、11/15西港慶安宮；本次只確證原圖含11/7/15文字，未把它當全帳號完成。

### `threads:1013.yr_` — partial（2 次記錄）

- Attempt 1 `2026-10-15T07:16:31+08:00`；方法 `profile-browser`；媒體 `unread`；網址：https://www.threads.com/@1013.yr_
  - 範圍：初次個人頁內容欄全為載入骨架，未取得近期貼文正文或媒體
  - 結果／未解項目：與前兩個Threads帳號同見主文未水合；等待其餘Threads初次讀取後檢查共通環境。

- Attempt 2 `2026-10-15T07:22:51+08:00`；方法 `profile-browser-wait-7s`；媒體 `partial`；網址：https://www.threads.com/@1013.yr_
  - 範圍：第二次等待7秒後讀取到10/12更名通知及回覆、10/10左右《情渡千年》一個月七場演出結束貼文；更名貼文2張圖只顯示1/2，5天前貼文有影片且未播，頁尾仍載入中，近期7天可見三則但帳號媒體和後續feed未完成
  - 結果／未解項目：目前可見內容為個人更名與已結束的春美歌劇團演出，未發現未來場次；因照片、影片及底部feed未讀完，維持partial。

### `threads:xuefeng_lu_` — partial（2 次記錄）

- Attempt 1 `2026-10-15T07:16:53+08:00`；方法 `profile-browser`；媒體 `unread`；網址：https://www.threads.com/@xuefeng_lu_
  - 範圍：初次個人頁只見載入骨架；近期正文與圖片均未取得
  - 結果／未解項目：Threads主文區仍未水合，尚未讀到帳號貼文。

- Attempt 2 `2026-10-15T07:23:10+08:00`；方法 `profile-browser-wait-7s`；媒體 `partial`；網址：https://www.threads.com/@xuefeng_lu_
  - 範圍：第二次等待7秒後，讀到10/13個人轉貼長文2/2、10/10左右「總統讚啦」及6天前笑話；近期7天無顯示戲曲公告；個人轉貼多媒體1/2未讀完，5/6天前的轉貼影片/外部內容未看，feed尚在載入
  - 結果／未解項目：本次可讀近期內容主要為非演出轉貼與個人長文，未取得演出新訊；影片和圖像未全讀，不能標complete。

### `threads:yuzhongluo` — partial（5 次記錄）

- Attempt 1 `2026-10-15T07:16:59+08:00`；方法 `profile-browser`；媒體 `unread`；網址：https://www.threads.com/@yuzhongluo
  - 範圍：初次個人頁主文欄全為載入骨架，沒有近期正文與媒體可讀
  - 結果／未解項目：品牌帳號也未水合，延續前述Threads個人頁讀取失敗現象。

- Attempt 2 `2026-10-15T07:23:34+08:00`；方法 `profile-browser-wait-7s`；媒體 `unread`；網址：https://www.threads.com/@yuzhongluo
  - 範圍：第二次等待7秒後讀到10/14南瀛藝術節10/24（週六）15:00，新營文化中心演藝廳前，八方傳統藝陣創新藝團「八家將+聖王再現」；另讀10/13海外文化交流貼文；新公告海報媒體未完成
  - 結果／未解項目：新活動屬傳統藝陣而非明確戲曲演出，先保留待查，不新增公開戲曲場次。帳號仍有載入中feed。

- Attempt 3 `2026-10-15T07:23:42+08:00`；方法 `direct-post-media-browser`；媒體 `unread`；網址：https://www.threads.com/@yuzhongluo/post/DeeXP_umU6t/media
  - 範圍：對10/14公告開啟原貼文媒體直連，首次快照只有Threads載入標誌，未顯示海報圖文
  - 結果／未解項目：海報仍待有界等待後檢視；這次媒體失敗不可推論公告內容只限已讀文字。

- Attempt 4 `2026-10-15T07:24:08+08:00`；方法 `direct-post-media-wait-7s`；媒體 `partial`；網址：https://www.threads.com/@yuzhongluo/post/DeeXP_umU6t/media
  - 範圍：同一原貼文媒體等待7秒後海報顯示完整；海報確認南瀛藝術節10/24（六）下午3點薪瀛舞台、新營文化中心演藝廳前，八方傳統藝陣創新藝團《八家將+聖王再現》；未在poster辨得任何歌仔戲/布袋戲劇目或售票資訊，頁面仍只有單一貼文，未讀完帳號近期feed
  - 結果／未解項目：海報及文字同列，清楚是傳統藝陣演出，是否屬戲曲網站收錄範圍未核實；先保留線索，不新增正式演出卡。

- Attempt 5 `2026-10-15T07:24:41+08:00`；方法 `official-festival-program-search`；媒體 `not_applicable`；網址：https://nanyingfest.tnc.gov.tw/index.php?id=40&inter=group&lang=zh
  - 範圍：以官方南瀛國際民俗藝術節團隊頁核對藝團性質，明示其表演融合國樂、武術、傳統藝陣；另官方10/24主場節目頁列19:00新營綠都心公園（主場地），不同於貼文所稱15:00新營文化中心前薪瀛舞台；未找到官方secondary-stage 15:00場次逐項表
  - 結果／未解項目：官方頁面不足以證實或否定15:00該場，也確認為民俗藝陣團隊而非標準戲曲團體；原線索留候選，不新增公開戲曲卡。

### `threads:taiwaneseopera168` — partial（2 次記錄）

- Attempt 1 `2026-10-15T07:17:12+08:00`；方法 `profile-browser`；媒體 `unread`；網址：https://www.threads.com/@taiwaneseopera168
  - 範圍：初次個人頁主文欄仍為載入骨架，未取得近期正文/圖片
  - 結果／未解項目：帳號頁的公開導覽已載入，近期貼文未水合，無法判斷是否有演出公告。

- Attempt 2 `2026-10-15T07:25:00+08:00`；方法 `profile-browser-wait-7s`；媒體 `unread`；網址：https://www.threads.com/@taiwaneseopera168
  - 範圍：第二次等待7秒後讀得個人簡介、8/16置頂文化部政策分享與10/14 11小時前演出消息：明華園天字團在屏東鹽埔慈靈宮夜演《林投姊》，吳奕萱演周阿司，貼文附個人FB直播連結；影片未播放、置頂媒體未檢查，底部feed仍載入
  - 結果／未解項目：10/14場次已過；劇團身份、日期、廟名、劇目及演員公告清楚。未將其當未來演出或以貼文取代完整近期帳號/媒體覆蓋。

### `threads:jing__1017` — partial（2 次記錄）

- Attempt 1 `2026-10-15T07:17:19+08:00`；方法 `profile-browser`；媒體 `unread`；網址：https://www.threads.com/@jing__1017
  - 範圍：初次個人頁只顯示載入骨架，未讀近期文字、時間及媒體
  - 結果／未解項目：帳號內容未水合，保留失敗待替代路徑與有界重試。

- Attempt 2 `2026-10-15T07:25:18+08:00`；方法 `profile-browser-wait-7s`；媒體 `partial`；網址：https://www.threads.com/@jing__1017
  - 範圍：第二次等待7秒後讀取10/14兩則貼文及一則跨日公告：10/24 19:00–20:30嘉義市文化公園《戲棚下逐星路》講座（張秀琴、林佳欣）；鴻明歌劇團《戰神花雲》10/17–18 14:30大稻埕戲苑售票資訊及opentix連結；後者角色介紹貼文媒體為1/3，前者海報1/2未讀，底部feed仍載入
  - 結果／未解項目：10/24為講座不是已證實演出；《戰神花雲》為已明確售票的歌仔戲且本週末演出，需比對schedule避免重複；圖片尚未逐項核讀，故partial。

### `threads:hilang.on.tour` — partial（2 次記錄）

- Attempt 1 `2026-10-15T07:17:27+08:00`；方法 `profile-browser`；媒體 `unread`；網址：https://www.threads.com/@hilang.on.tour
  - 範圍：初次品牌個人頁顯示大量載入骨架，無近期文字/圖片內容
  - 結果／未解項目：主文欄未水合；該帳號近期巡演貼文與媒體範圍未能讀取。

- Attempt 2 `2026-10-15T07:25:36+08:00`；方法 `profile-browser-wait-7s`；媒體 `unread`；網址：https://www.threads.com/@hilang.on.tour
  - 範圍：第二次等待7秒後讀到10/14新貼文：10/30苗栗竹南運動公園大草坪，17:00進場/18:00開演，古都掌中劇團《台灣風雲錄・戰火波瀾》，策劃山線百年客家輸出；另讀10/8桃園蓮華寺《三俠五義之鍘龐昱》回顧；兩則貼文海報/照片未打開，feed仍載入中
  - 結果／未解項目：10/30新未來演出，與joe_huang_k_w同一節目公告相符但需要查主辦/售票官方訊息與現有卡，帳號媒體/完整近7天feed仍不完整。

### `threads:yolin1991` — partial（2 次記錄）

- Attempt 1 `2026-10-15T07:17:33+08:00`；方法 `profile-browser`；媒體 `unread`；網址：https://www.threads.com/@yolin1991
  - 範圍：初次個人頁載入骨架未消退，無近期貼文正文或媒體
  - 結果／未解項目：主文feed未水合；待全部初次讀取後改用不同讀取路徑處理。

- Attempt 2 `2026-10-15T07:26:17+08:00`；方法 `profile-browser-wait-7s`；媒體 `unread`；網址：https://www.threads.com/@yolin1991
  - 範圍：第二次等待7秒後讀到10/13新吉義林歌劇團10/17–18雲林四湖丁家九龍元帥演出預告（演出時間待公布）及10/14藝師照片；兩篇附圖未開，feed仍載入中
  - 結果／未解項目：本週末場次待核：原文明示時間待公布，不補猜時間；先與schedule和歌劇團/廟方原始公告對照後再決定是否新增。

### `facebook:sunhope.fans` — partial（2 次記錄）

- Attempt 1 `2026-10-15T07:17:45+08:00`；方法 `page-browser`；媒體 `unread`；網址：https://www.facebook.com/sunhope.fans
  - 範圍：初次開啟 Facebook 公開粉專 URL，頁面只有空白 Facebook 文件，沒有專頁正文、貼文或圖片
  - 結果／未解項目：目前未見可辨識錯誤或登入提示；粉專讀取失敗，待檢查同平台共通環境及替代公開路徑。

- Attempt 2 `2026-10-15T07:27:23+08:00`；方法 `page-browser-wait-7s`；媒體 `partial`；網址：https://www.facebook.com/sunhope.fans
  - 範圍：第二次等待7秒後官方粉專水合；讀取置頂11/7–8《寒窯之外》官方售票與四場資訊、10/14「哪吒伏龍」為酒店邀請不對外開放；另讀4/5/6天前茄萣金鑾宮國慶場、全球首播影片、已額滿《陳世美的三個抉擇》讀者劇場片段；圖片海報未逐張檢視，底部feed仍載入
  - 結果／未解項目：11/7–8及各場時間、售票連結均可讀，應與排程核對；10/14私演與近期已結束場次不作公開卡。頁面延遲水合解釋初次空白，但近期完整feed及圖片仍不足，維持partial。

### `facebook:HsiaoHsiYuan1913` — partial（2 次記錄）

- Attempt 1 `2026-10-15T07:17:52+08:00`；方法 `page-browser`；媒體 `unread`；網址：https://www.facebook.com/HsiaoHsiYuan1913/
  - 範圍：初次粉專載入後只見 Facebook 骨架，沒有近期貼文正文或圖片
  - 結果／未解項目：小西園粉專主文尚未水合，暫列失敗並在全名單初次讀取後檢查共通環境。

- Attempt 2 `2026-10-15T07:28:23+08:00`；方法 `page-browser-wait-7s`；媒體 `unread`；網址：https://www.facebook.com/HsiaoHsiYuan1913/
  - 範圍：公開個人檔案與已載入貼文正文；可見近期貼文未呈現日期，照片描述空白，尚有載入中項目；未能依帳號時間範圍完整覆蓋
  - 結果／未解項目：第二次瀏覽器等待後個人檔案已載入，見一則轉載藝文訊息及空白照片描述；貼文日期與圖片內容不可讀，動態仍載入中；非完整帳號巡檢。

### `facebook:100063868113954` — failed（2 次記錄）

- Attempt 1 `2026-10-15T07:18:01+08:00`；方法 `profile-browser`；媒體 `unread`；網址：https://www.facebook.com/p/%E5%90%B3%E5%A5%95%E8%90%B1-Wu-Yihsuan-100063868113954
  - 範圍：個人專頁、簡介與貼文區標題可讀；貼文區第一個story只有無描述圖片/控件，後續兩區仍載入中，未取得貼文正文與圖片文字
  - 結果／未解項目：確認帳號為吳奕萱本人頁，近期貼文內容與演出公告未讀完整，不能推定沒有新場次。

- Attempt 2 `2026-10-15T07:33:11+08:00`；方法 `page-browser-wait-7s`；媒體 `unread`；網址：https://www.facebook.com/p/%E5%90%B3%E5%A5%95%E8%90%B1-Wu-Yihsuan-100063868113954
  - 範圍：第二次等待7秒後取得吳奕萱個人簡介及12小時前貼文日期；該貼文明示「目前無法查看此內容」，其餘貼文仍在載入中；未取得近期貼文正文或媒體
  - 結果／未解項目：第二次個人頁重讀後，最新12小時貼文顯示目前無法查看此內容，頁面說明可能因分享對象或刪除；未見可讀演出正文/海報，底部feed載入中。因此來源正文不可讀，狀態failed；不可推論無新演出。

### `facebook:MingHuaYuanTianTaiwaneseOpera` — partial（1 次記錄）

- Attempt 1 `2026-10-15T07:18:20+08:00`；方法 `page-browser`；媒體 `unread`；網址：https://www.facebook.com/MingHuaYuanTianTaiwaneseOpera
  - 範圍：讀取個人專頁與兩則近期貼文；3天前貼文全文已展開，內容確認10/10國慶壓軸《旺來神》在屏東圓滿結束；5天前貼文僅讀開頭「今天彰化溪州、明天屏東」，其餘全文未展開；兩則相片/海報皆未逐張讀圖，後續feed仍載入中
  - 結果／未解項目：已取得近期演出回顧與過去行程線索，沒有證據支持未來場次；近期媒體及完整帳號範圍未讀，故partial。

### `facebook:61574134933376` — partial（2 次記錄）

- Attempt 1 `2026-10-15T07:18:58+08:00`；方法 `page-browser`；媒體 `unread`；網址：https://www.facebook.com/profile.php?id=61574134933376
  - 範圍：初次開啟粉專只見 Facebook 骨架及未標籤控制項，沒有頁名、貼文正文或可辨讀媒體
  - 結果／未解項目：匿名頁面主文未水合；未能讀取繡花園／地字近期公告。

- Attempt 2 `2026-10-15T07:28:38+08:00`；方法 `page-browser-wait-7s`；媒體 `partial`；網址：https://www.facebook.com/profile.php?id=61574134933376
  - 範圍：公開粉專資料與已載入貼文正文；只見 21 小時前《孫臏兵法》潮州首演落幕相簿，31 張媒體只呈現少數縮圖；未載完帳號動態
  - 結果／未解項目：第二次等待後載入「繡花園戲劇團x明華園地字戲劇團」頁及最新相簿公告；標示114年度重塑民間劇場外臺歌仔戲2.0《孫臏兵法》（潮州首演）精彩落幕，含31張相片，部分縮圖無描述；此為演後回顧，帳號其餘動態仍載入。

### `facebook:mhysun` — partial（2 次記錄）

- Attempt 1 `2026-10-15T07:19:07+08:00`；方法 `page-browser`；媒體 `unread`；網址：https://www.facebook.com/mhysun
  - 範圍：個人頁與已驗證帳號可辨認；貼文標題下方均為載入骨架，沒有正文或演出媒體
  - 結果／未解項目：無法讀取孫翠鳳近期個人行程，未能將她的個人公告與劇團演出區分；列失敗。

- Attempt 2 `2026-10-15T07:29:00+08:00`；方法 `page-browser-wait-7s`；媒體 `unread`；網址：https://www.facebook.com/mhysun
  - 範圍：公開已載入貼文正文及縮圖；近15小時貼文提到本週末連續三天、三縣市、三齣戲，但正文摺疊、未讀海報；次近貼文含合作宣傳影片與文化部文本外譯消息；動態仍載入中
  - 結果／未解項目：第二次等待後已讀孫翠鳳認證帳號部分公開貼文：最新貼文稱本週末三天三縣市三齣經典戲，細節收於未展開正文及多張未描述海報；另見兩日前演後宣傳影片及 9/28 文化部書籍入選消息，未形成可核的演出場次資料。影音/海報未讀，非完整帳號巡檢。

### `facebook:61594936681482` — partial（2 次記錄）

- Attempt 1 `2026-10-15T07:19:16+08:00`；方法 `page-browser`；媒體 `unread`；網址：https://www.facebook.com/profile.php?id=61594936681482
  - 範圍：初次開啟Facebook粉專URL僅回空白文件，沒有粉專身分、貼文正文或媒體
  - 結果／未解項目：戲籠出巡Facebook頁面未讀到內容；不可用同品牌Threads貼文替代帳號覆蓋。

- Attempt 2 `2026-10-15T07:29:15+08:00`；方法 `page-browser-wait-7s`；媒體 `unread`；網址：https://www.facebook.com/profile.php?id=61594936681482
  - 範圍：公開粉專資料、官網連結與已載入之最新貼文；最新貼文為傳統戲曲文化宣傳，海報僅有文字圖示且未讀；較早貼文載明官網及10/8已結束場次；動態仍載入中
  - 結果／未解項目：第二次等待後載入戲籠出巡粉專。最新20小時貼文倡議留一晚體驗臺灣傳統戲曲，無場次詳情；較早置頂/貼文列官網、10/8桃園蓮華寺《三俠五義之鍘龐昱》19:00扮仙、19:30開演（已過）。未找到10/30竹南活動的粉專公告；底部持續載入，非完整帳號巡檢。

### `facebook:lanyang.opera` — partial（2 次記錄）

- Attempt 1 `2026-10-15T07:19:24+08:00`；方法 `page-browser`；媒體 `unread`；網址：https://www.facebook.com/lanyang.opera/
  - 範圍：初次官方Facebook粉專URL回空白頁面，未讀到近期貼文正文/圖片
  - 結果／未解項目：蘭陽戲劇團帳號內容不可讀，需換受支援公開路徑，不以文化局或官網公告充當帳號覆蓋。

- Attempt 2 `2026-10-15T07:29:32+08:00`；方法 `page-browser-wait-7s`；媒體 `unread`；網址：https://www.facebook.com/lanyang.opera/
  - 範圍：官方粉專最新行程貼文正文讀取；內文列出10/26（一）19:00《錯配姻緣》桃園龜山顯安巖顯應祖師廟、地址及免費觀賞；海報圖像未讀，貼文表示無直播；其餘動態仍載入中
  - 結果／未解項目：第二次等待後讀到官方蘭陽戲劇團10月行程表文字。確認10/26 19:00《錯配姻緣》，桃園市龜山區樂善里樂安街1號顯安巖顯應祖師廟，免費觀賞；未開放直播。海報未檢視、帳號其餘貼文仍載入。

### `facebook:Taichungpuppettheater` — partial（2 次記錄）

- Attempt 1 `2026-10-15T07:19:31+08:00`；方法 `page-browser`；媒體 `unread`；網址：https://www.facebook.com/Taichungpuppettheater/
  - 範圍：初次官方粉專URL只返回空白Facebook文件，沒有貼文正文或媒體可讀
  - 結果／未解項目：台中木偶劇團帳號近期內容未讀。

- Attempt 2 `2026-10-15T07:29:51+08:00`；方法 `page-browser-wait-7s-expanded`；媒體 `partial`；網址：https://www.facebook.com/Taichungpuppettheater/
  - 範圍：公開粉專已載入貼文正文：10/12霧峰祝壽演出《聖劍風雲》及3:30祝壽、6:30演出；10/13左右另有6分15秒影片未播放；其餘貼文仍載入中
  - 結果／未解項目：第二次等待載入後展開官方台中木偶劇團演出公告：10/12（一）臺中市霧峰區林森路433號，15:30祝壽、18:30大型金光武俠布袋戲《聖劍風雲》。演出日期已過；較新影片長6:15未播放，另一張演出公告圖未讀；其餘動態仍載入中。

### `culture` — partial（3 次記錄）

- Attempt 1 `2026-10-15T07:20:29+08:00`；方法 `official-open-data-portal-and-web-search`；媒體 `not_applicable`；網址：https://opendata.culture.tw/frontsite/openData/detail?datasetId=302
  - 範圍：本地moc_candidates.json現有1筆，完整讀取三昧堂精工布袋戲展2027-01-01候選；嘗試文化部官方cloud API category=all遭瀏覽器ERR_BLOCKED_BY_CLIENT，官方開放資料portal僅可讀到資料集metadata/每日更新說明；網搜僅見非官方轉載，未取得本輪完整all-category資料或候選清單
  - 結果／未解項目：依既有候選規則保留三昧堂展覽待人工核實，不把展覽升為正式演出；因未讀全量API及本輪新候選，文化部來源coverage為partial。

- Attempt 2 `2026-10-15T07:30:59+08:00`；方法 `official-updater-api-attempt-1`；媒體 `unread`；網址：https://cloud.culture.tw/frontsite/trans/SearchShowAction.do?method=doFindTypeJ&category=all
  - 範圍：以專案唯讀用戶端請求官方全類別API；首次請求DNS解析失敗，未取得資料
  - 結果／未解項目：第一次 official API 請求回報 nodename nor servname provided；只得到連線解析錯誤，沒有可供檢視的候選或媒體。第二次請求改等待後執行。

- Attempt 3 `2026-10-15T07:31:03+08:00`；方法 `official-updater-api-attempt-2`；媒體 `unread`；網址：https://cloud.culture.tw/frontsite/trans/SearchShowAction.do?method=doFindTypeJ&category=all
  - 範圍：以專案唯讀用戶端第二次請求官方全類別API；再次DNS解析失敗，未取得資料
  - 結果／未解項目：等待2秒後第二次請求仍回報nodename nor servname provided；與第一次相同DNS故障，故停止同路徑重試並保留本地候選待續查。

### `issues` — complete（1 次記錄）

- Attempt 1 `2026-10-15T07:21:37+08:00`；方法 `github-public-browser`；媒體 `not_applicable`；網址：https://github.com/eric1810-tw/taiwan-opera-calendar/issues?q=is%3Aissue+sort%3Aupdated-desc
  - 範圍：以更新時間遞減查看全部Issues（排除PR）；列表顯示2筆open #2/#1，兩則issue正文與Activity區逐一讀取，均無留言/後續活動；另外查is:closed結果0
  - 結果／未解項目：兩則仍open且未更新：#2 OPENTIX 2082042280907173889；#1 OPENTIX 2079784321891332096。沒有新評論或狀態變更。

## 場次比對與資料決定

- `@joe_huang_k_w`、`@hilang.on.tour` 可見的 10/30 竹南古都掌中戲與既有 `amichen-2026-10-30-zhunan-taiwan-fengyunlu` 同場；既有卡保留原策劃／主辦來源，不新增重複卡。
- `@the_rin.lpm` 可見 11/7 新莊保元宮《玉石變》、11/15 西港慶安宮《金沙灘》已由既有卡覆蓋；宣傳帳號自述非官方，未提升可信狀態。
- `@jing__1017` 的 10/17–18 鴻明《戰神花雲》與售票頁資訊已由既有卡覆蓋；10/24《戲棚下逐星路》為講座，不作演出卡。
- `@yolin1991` 提及新吉義林 10/17–18 雲林四湖丁家九龍元帥，原文稱演出時間待公布，其他場次欠詳細地址／劇目對應；保留於本輪待查線索，不補未知欄位或新增正式卡。
- `@yuzhongluo` 10/24「八家將+聖王再現」海報與貼文一致；南瀛官方團隊資料定位為民俗藝陣，另官方主舞台節目時間地點不同，未找到官方薪瀛舞台 15:00 逐項表，故保留待核線索。參考：[南瀛藝術節官方團隊頁](https://nanyingfest.tnc.gov.tw/index.php?id=40&inter=group&lang=zh)。
- `sunhope.fans` 的 11/7–8《寒窯之外》與既有卡相符；10/14《哪吒伏龍》公告明示不對外開放。
- `lanyang.opera` 官方貼文列 10/26 19:00《錯配姻緣》、龜山顯安巖顯應祖師廟、免費且無直播；既有 `lanyang-2026-10-26-guishan-cuoxie-yinyuan` 已涵蓋相同場次，保持 `community`，本輪不重複新增。
- `Taichungpuppettheater` 讀到 10/12《聖劍風雲》已過期；其較新 6:15 影片和其他貼文媒體未播放／讀圖。其他可讀社群公告也未形成足以改動公開表的新資料。
- 全輪未新增或修訂演出卡／候選。巡檢場次比對時（遠端更新合併前）96 張 `schedule.json` 依 ID 及「日期、場地、劇團、劇目」完全相同鍵均無重複；未做模糊相似場次保證。

## 文化部與 GitHub Issues

- 本地候選檔 1 筆：三昧堂精工布袋戲展（2027-01-01）保留待核；官方開放資料集頁可讀到全類別資料集及每日更新說明，但本輪官方 API 受瀏覽器封鎖與 DNS 解析錯誤影響，未取得完整最新清單。官方資料集：[文化部開放資料資料集 302](https://opendata.culture.tw/frontsite/openData/detail?datasetId=302)。Coverage 為 partial，不代表沒有新增候選。
- GitHub Issues 依更新時間由新到舊讀完全部 2 筆 open issues #2、#1 及 Activity／留言，均無新留言或狀態變更；closed 篩選為 0，排除 Pull Requests。#2 線索 OPENTIX 2082042280907173889；#1 線索 OPENTIX 2079784321891332096。

## 驗證與發布

- `python3 -m unittest -v`：17 tests OK。
- `node --check assets/app.js`：通過。
- `git diff --check`：通過。
- 合併遠端更新後 schedule 檢查：95 張卡必填欄位、ISO 日期、`endDate` 不早於開始日、ID 唯一；日期＋場地＋劇團＋劇目完全相同鍵無重複：通過。
- 推送成功：`main` 推至資料 SHA `d8f9695580da32c3f6249d613c52cc9f72d73d0a`。同 SHA `.github/workflows/daily-update.yml` Actions `38654981372` 為 `completed/success`；`patrol_progress.py verify` 於 `2026-10-15T07:36:12+08:00` 核對公開狀態檔等於本輪 `startedAt=2026-10-15T07:15:39+08:00`、`status=failed`。網站狀態已發布；來源覆蓋仍 failed。詳見 `PATROL_2026-10-15_0300_RECEIPT.md`。

## 未完成與接續

- 19 個社群來源：18 partial、1 failed（吳奕萱 Facebook）。初次骨架／空白頁等待 7 秒後，多數可讀到部分正文，但 feed 仍載入、近期覆蓋不足，媒體未全讀；吳奕萱最新貼文明示目前無法查看此內容，未讀得正文。依規程將總狀態維持 failed，不推論無新演出。
- 文化部完整全類別 API 因 DNS 失敗未讀；網路恢復後可用 `resume` 同輪接續，保留原始開始時間與 attempts，再 finalize、發布及驗收。
- 發布驗收需保存資料 SHA，確認同 SHA `.github/workflows/daily-update.yml` 為 `completed/success`，再用 `patrol_progress.py verify` 核對公開 `data/patrol_status.json`；失敗則在 run JSON 保留 blocked 原因。
