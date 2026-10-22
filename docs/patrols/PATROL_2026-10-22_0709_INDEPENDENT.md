# 2026-10-22 07:09 臺灣戲曲獨立巡檢與發布驗收報告

- **巡檢識別**：`patrol_runs/2026-10-22_0709.json`
- **開始時間**：`2026-10-22T07:09:15+08:00`
- **最後嘗試**：`2026-10-22T09:34:30+08:00`
- **驗收完成**：`2026-10-22T09:36:48+08:00`
- **執行工具**：Antigravity（原生 spawn 無頭 Microsoft Edge、設定檔 `~/.patrol-edge`、Chrome DevTools Protocol (CDP)、文化部紀錄解析、GitHub CLI）
- **規範依據**：`AGENTS.md`、`PATROL_OPERATIONS.md`

---

## 1. 21 個來源逐一巡檢與存證結果

共巡檢 21 個目標來源，狀態動態計算為：**2 complete、18 partial、1 failed、0 pending**。總狀態依覆蓋率規則忠實判定為 **`failed`**（未達 100% 覆蓋，有 1 個 failed 來源）。

| 來源鍵 | 平台／類型 | 狀態 | 擷取篇數 | 最新／最舊貼文時間 | 重試次數 | 登入牆 | 證據檔案 |
|---|---|---|---|---|---|---|---|
| `threads:joe_huang_k_w` | Threads | partial | 9 篇 | 最新 10/17 20:06、最舊 10/12 17:35 | 0 | 否 | `patrol_evidence/2026-10-22_0709/threads_joe_huang_k_w.json` |
| `threads:h.akito_1996` | Threads | partial | 10 篇 | 最新 10/19 19:06、最舊 10/09 22:13 | 0 | 否 | `patrol_evidence/2026-10-22_0709/threads_h.akito_1996.json` |
| `threads:the_rin.lpm` | Threads | partial | 6 篇 | 最新 10/20 20:27、最舊 09/26 14:32 | 0 | 否 | `patrol_evidence/2026-10-22_0709/threads_the_rin.lpm.json` |
| `threads:1013.yr_` | Threads | failed | 0 篇 | 無 | 3 (共4次) | 否 | `patrol_evidence/2026-10-22_0709/threads_1013.yr_.json` |
| `threads:xuefeng_lu_` | Threads | partial | 7 篇 | 最新 10/20 14:46、最舊 10/08 13:53 | 0 | 否 | `patrol_evidence/2026-10-22_0709/threads_xuefeng_lu_.json` |
| `threads:yuzhongluo` | Threads | partial | 4 篇 | 最新 10/21 13:11、最舊 10/20 12:18 | 0 | 否 | `patrol_evidence/2026-10-22_0709/threads_yuzhongluo.json` |
| `threads:taiwaneseopera168` | Threads | partial | 8 篇 | 最新 10/21 15:00、最舊 10/20 18:06 | 0 | 否 | `patrol_evidence/2026-10-22_0709/threads_taiwaneseopera168.json` |
| `threads:jing__1017` | Threads | partial | 9 篇 | 最新 10/19 01:16、最舊 10/13 23:49 | 0 | 否 | `patrol_evidence/2026-10-22_0709/threads_jing__1017.json` |
| `threads:hilang.on.tour` | Threads | partial | 7 篇 | 最新 10/14 11:25、最舊 10/02 11:07 | 0 | 否 | `patrol_evidence/2026-10-22_0709/threads_hilang.on.tour.json` |
| `threads:yolin1991` | Threads | partial | 7 篇 | 最新 10/21 13:58、最舊 10/10 14:56 | 0 | 否 | `patrol_evidence/2026-10-22_0709/threads_yolin1991.json` |
| `facebook:sunhope.fans` | Facebook | partial | 33 篇 | 時間未辨識 33 篇 | 0 | 否 | `patrol_evidence/2026-10-22_0709/facebook_sunhope.fans.json` |
| `facebook:HsiaoHsiYuan1913` | Facebook | partial | 34 篇 | 時間未辨識 34 篇 | 0 | 否 | `patrol_evidence/2026-10-22_0709/facebook_HsiaoHsiYuan1913.json` |
| `facebook:100063868113954` | Facebook | partial | 34 篇 | 時間未辨識 34 篇 | 0 | 否 | `patrol_evidence/2026-10-22_0709/facebook_100063868113954.json` |
| `facebook:MingHuaYuanTianTaiwaneseOpera` | Facebook | partial | 29 篇 | 時間未辨識 29 篇 | 0 | 否 | `patrol_evidence/2026-10-22_0709/facebook_MingHuaYuanTianTaiwaneseOpera.json` |
| `facebook:61574134933376` | Facebook | partial | 27 篇 | 時間未辨識 27 篇 | 0 | 否 | `patrol_evidence/2026-10-22_0709/facebook_61574134933376.json` |
| `facebook:mhysun` | Facebook | partial | 30 篇 | 時間未辨識 30 篇 | 0 | 否 | `patrol_evidence/2026-10-22_0709/facebook_mhysun.json` |
| `facebook:61594936681482` | Facebook | partial | 6 篇 | 時間未辨識 6 篇 | 0 | 否 | `patrol_evidence/2026-10-22_0709/facebook_61594936681482.json` |
| `facebook:lanyang.opera` | Facebook | partial | 31 篇 | 時間未辨識 31 篇 | 0 | 否 | `patrol_evidence/2026-10-22_0709/facebook_lanyang.opera.json` |
| `facebook:Taichungpuppettheater` | Facebook | partial | 33 篇 | 時間未辨識 33 篇 | 0 | 否 | `patrol_evidence/2026-10-22_0709/facebook_Taichungpuppettheater.json` |
| `culture` | 文化部 | complete | 1531 筆 | 候選 36 筆，不在表 30 筆；建卡 1 筆，其餘 29 筆逐筆審核處置完成 | 0 | 否 | `data/moc_records.json` |
| `issues` | GitHub | complete | 2 筆 | Issues #1、#2 檢核皆為 open，無新留言 | 0 | 否 | GitHub CLI & REST API |

---

## 2. 提到未來演出之貼文逐篇判斷與比對結果

經 `scripts/extract_mentions.py` 自巡檢證據中提取 238 篇演出相關貼文，篩選出涉及未來（2026-10-22 及以後）之貼文，逐篇核對 `data/schedule.json` 如下：

### 【已在表且一致】

1. **明華園天字戲劇團 高雄聖母宮外台**
   - **來源**：`facebook:100063868113954`（吳奕萱粉專）
   - **原文逐字片段**：
     > 「鹿耳門高雄聖母宮 時間：10/22 地點：高雄市三民區中道街43號」
   - **比對狀態**：**已在表且一致**（卡片 ID `mhy-tian-2026-10-22-shengmu`，地點已記載高雄市三民區中道街43號）。

2. **鶯藝歌劇團 台南南廠武英殿外台**
   - **來源**：`threads:yuzhongluo`
   - **原文逐字片段**：
     > 「下一站 農曆9月14、15日~國曆10月23、24日 地點：台南市大智街135號~南廠武英殿 鶯藝歌劇團 安排好戲登場~歡迎來看戲✌️✌️✌️」
   - **比對狀態**：**已在表且一致**（卡片 ID `luo-2026-10-23-wuyingdian`，地址已記載台南市大智街135號）。

3. **台南古都掌中劇團《台灣風雲錄・戰火波瀾》（苗栗竹南場）**
   - **來源**：`threads:joe_huang_k_w`、`threads:hilang.on.tour`、`facebook:61594936681482`
   - **原文逐字片段**：
     > 「10月30日，邀請你來苗栗竹南運動公園大草坪。 帶著家人朋友，一起坐下來，看看臺灣的故事。 ▍《台灣風雲錄・戰火波瀾》 主演｜台南古都掌中劇團 日期｜2026年10月30日（五） 地點｜苗栗竹南運動公園大草坪 進場｜17:00 開演｜18:00 策劃｜山線百年客家輸出・陳翊綾 各位朋友，竹南見。」
   - **比對狀態**：**已在表且一致**（卡片 ID `amichen-2026-10-30-zhunan-taiwan-fengyunlu`）。

4. **秀琴歌劇團 大型公演《玉石變》與《金沙灘》**
   - **來源**：`threads:the_rin.lpm`
   - **原文逐字片段**：
     > 「📅11/07 19：00 🎭戲碼：《玉石變》📍地點：新莊保元宮 ... 📅11/15 19：00 🎭戲碼：《金沙灘》 📍地點：西港慶安宮」
   - **比對狀態**：**已在表且一致**（卡片 ID `sc-2026-11-07-yushibian` 與 `sc-2026-11-15-jinshatan`）。

5. **蘭陽戲劇團《錯配姻緣》**
   - **來源**：`facebook:lanyang.opera`
   - **原文逐字片段**：
     > 「10/26（一）晚上7:00 劇目｜《錯配姻緣》 地點｜桃園顯安巖顯應祖師廟 （桃園市龜山區樂善里樂安街1號） ※免費觀賞」
   - **比對狀態**：**已在表且一致**（卡片 ID `lanyang-2026-10-26-guishan-cuoxie-yinyuan`）。

6. **台中木偶劇團《聖劍風雲三-龍虎兄弟》**
   - **來源**：`facebook:Taichungpuppettheater`
   - **原文逐字片段**：
     > 「日期｜115 / 11 / 7（六） 時間｜14:30 地點｜臺中市屯區藝文中心・實驗劇場」
   - **比對狀態**：**已在表且一致**（卡片 ID `tcpt-2026-11-07-shengjianfengyun-3`）。

7. **明華園戲劇總團《烏龍天下》高雄場**
   - **來源**：`facebook:mhysun`
   - **原文逐字片段**：
     > 「12/19－12/20｜衛武營國家藝術文化中心 10/16 中午12點搶票」
   - **比對狀態**：**已在表且一致**（卡片 ID `mhy-oolong-wv-2026-12-19`）。

8. **尚和歌仔戲劇團【寒窯之外】**
   - **來源**：`facebook:sunhope.fans`
   - **原文逐字片段**：
     > 「演出日期：11/7（六）、11/8（日） OPENTIX 兩廳院售票系統現正熱賣ing」
   - **比對狀態**：**已在表且一致**（卡片 ID `sh-2026-11-07-hanyao-zhiwai`）。

### 【海報未讀 (poster-only) 與線索不足】

- `facebook:HsiaoHsiYuan1913`：貼文為純圖片/海報無內文，列入海報未讀。
- `threads:the_rin.lpm`（`Ddy9Vv8k7IV`）：「先補個劇團新發的戲路表🙌」，貼文僅附戲路表圖片無文字日期地點，列入海報未讀。
- `facebook:61574134933376`（繡花園戲劇團）：貼文提及「我們還有第二場喔！ 繡花園戲劇團《孫臏兵法》 11月18日，台南柳營見！」，未公布具體演出廟宇/場館與開演時間，線索不足不建卡。
- `facebook:Taichungpuppettheater`：貼文提及「11/14（六）戶外演出-《波比大冒險》」，未公布演出地點與時間，線索不足不建卡。
- `threads:the_rin.lpm`（`DejZXiykw3q`）：秀琴歌劇團講座《戲棚下・逐星路》，屬推廣講座非戲曲演出，已於卡片 `lecture-2026-10-24-xipeng-xinglu` 表彰，不另建新卡。
- `facebook:sunhope.fans`：10/24《HOLIDAY 午後沉浸式茶戲體驗》，僅 12 席且已額滿之茶席推廣活動，非公開演出，不建卡。
- `facebook:sunhope.fans`：10/31 岡山圖書館「歌仔繪本演故事」，為圖書館親子繪本活動且已額滿，非正式戲曲演出，不建卡。

### 【新增、更新卡與拒絕提案統計】

- **社群新增卡**：無（0 筆）
- **文化部新增卡**：1 筆
  - **ID**：`moc-2109890724705943553-033c8f`
  - **標題**：《「戲來就演！」－布袋戲演師們的大挑戰》
  - **日期**：2026-12-11～2026-12-12
  - **地點**：輔仁大學外語學院華觀劇場（新北市新莊區營盤里中正路510號 舒德樓1樓）
  - **來源**：文化部開放資料 / OPENTIX兩廳院文化生活
- **更新卡**：無（0 筆）
- **被拒絕之提案**：無（0 筆）

---

## 3. 文化部開放資料比對

- **來源檔案**：`data/moc_records.json`（由 GitHub 更新器產生）
- **抓取時間（fetchedAt）**：`2026-10-21T09:11:17+08:00`（未逾 36 小時門檻）
- **資料總筆數（total）**：1531 筆（達 500 筆新鮮度門檻）
- **篩選候選數**：36 筆
- **不在表 30 筆之逐筆處置與理由**：

1. `「戲來就演！」－布袋戲演師們的大挑戰`：布袋戲售票演出，**成功建卡**（卡片 ID `moc-2109890724705943553-033c8f`）。
2. `桃園市土地公文化館常設展-302土地公節日慶典與科儀活動`：展覽，非演出。
3. `世紀初戀－楊麗花歌仔戲特展`：特展，非演出。
4. `2026年1月【雲林布袋戲館-「掌演乾坤」常設展】`：常設展，非演出。
5. `2026年1月【雲林布袋戲館-《傳藝之魂‧黃海岱與戲偶之道》特展】`：特展，非演出。
6. `高雄市皮影戲館常設展`：常設展，非演出。
7. `115年「掌藝薪傳-大師工作坊」`（類別 19）：研習工作坊，非演出。
8. `115年「掌藝薪傳-大師工作坊」`（類別 200）：研習工作坊，非演出。
9. `115年「掌藝薪傳-大師工作坊」`（類別 4）：研習工作坊，非演出。
10. `三昧堂精工布袋戲展`（2026/01/31）：展覽，非演出。
11. `三昧堂精工布袋戲展`（2027/01/01）：展覽，非演出。
12. `【掌中戲】五洲勝義閣掌中劇團《濟世降魔傳》`：既有卡片已收錄（ID: `wz-2026-10-31`，金光掌中大戲《濟世降魔傳》，2026-10-31 大稻埕戲苑曲藝場）。
13. `【特展】 「請戲-布袋戲一條街」特展`：特展，非演出。
14. `金鷹歸來：隆興閣掌中武林特展`：特展，非演出。
15. `長義閣掌中劇團「銳劇場」系列 -《我,哪吒》`：既有卡片已收錄（ID: `cyg-2026-12-05-nezha`，2026-12-05 ~ 12-06 烏梅劇院）。
16. `【歌仔戲】元和劇子-鼓震千秋《梁紅玉》`：既有卡片已收錄（ID: `yuanhe-2026-10-30`，鼓震千秋《梁紅玉》，2026-10-30 大稻埕戲苑）。
17. `義興閣掌中劇團《豆花公劇場版－拍斷手骨顛倒勇》`：既有卡片已收錄（ID: `yxg-2026-12-05-douhuagong-chiayi`，嘉義場）。
18. `義興閣掌中劇團《四靈國：天祥書之謎》`：既有卡片已收錄（ID: `yxg-2026-11-21-silingguo-taipei`，台北場）。
19. `2026 NTT遇見巨人—唐美雲歌仔戲團《南都幽靈夜譚》`：既有卡片已收錄（ID: `tmy-tc-2026-12-26`，2026 歌仔戲旗艦大展《南都幽靈夜譚》（台中場），2026-12-26 ~ 12-27 臺中國家歌劇院大劇院）。
20. `2026歌仔戲旗艦展演補助計畫-明華園總團旗艦製作《烏龍天下》`：標題含展且既有卡片已收錄（ID: `mhy-flagship-2026-11-20`，台北場）。
21. `2026歌仔戲旗艦展演—唐美雲歌仔戲團《南都幽靈夜譚》`：標題含展且既有卡片已收錄（ID: `tmy-flagship-2026-11-27`，台北場）。
22. `張雅淳×李婉菁《唸歌去天庭：老仙婆的跨界音樂會》`：既有卡片已收錄（ID: `opentix-2026-10-25-niangetwentian-zhangyachun`，2026-10-25 牯嶺街小劇場）。
23. `【2026KIPF】錦飛鳳傀儡戲劇團 《靖姑傳奇》`：既有卡片已收錄（ID: `opentix-2026-10-25-jinfeifeng-jingguchuanqi`，2026-10-25 高雄市皮影戲館3樓劇場）。
24. `【2026KIPF】金鷹閣電視木偶劇團 《西遊記之鬧天宮》`：既有卡片已收錄（ID: `opentix-2026-10-25-jinyingge-naotiangong`，2026-10-25 高雄市岡山文化中心演藝廳）。
25. `偶偶偶劇團《小狐狸買手套》`：現代兒童劇（物件偶/光影），非傳統戲曲（非歌仔戲/布袋戲/皮影戲/傀儡戲），不建卡。
26. `兒童布袋戲《焰王現身：心火山的祕密》`：既有卡片已收錄（ID: `child-puppets-2026-10-31`，2026-10-31 ~ 11-01 水源劇場）。
27. `台中木偶劇團 《聖劍風雲三》`：既有卡片已收錄（ID: `tcpt-2026-11-07-shengjianfengyun-3`，2026-11-07 臺中市屯區藝文中心實驗劇場）。
28. `登出世界、登入自我！《虛。實─數位與我》插畫創作聯展`（類別 6）：插畫展覽，非戲曲演出。
29. `登出世界、登入自我！《虛。實─數位與我》插畫創作聯展`（類別 200）：插畫展覽，非戲曲演出。
30. `登出世界、登入自我！《虛。實─數位與我》插畫創作聯展`（類別 4）：插畫展覽，非戲曲演出。

---

## 4. 發布與公開驗收結果

- **資料提交 SHA**：[`95abd09be1646b08adc8bdeb64f06e3265e0b2b2`](https://github.com/eric1810-tw/taiwan-opera-calendar/commit/95abd09be1646b08adc8bdeb64f06e3265e0b2b2)
- **GitHub Actions Run**：[Run ID 39706630460](https://github.com/eric1810-tw/taiwan-opera-calendar/actions/runs/39706630460)（push / success）
- **公開驗收指令**：`python3 scripts/patrol_progress.py verify --run patrol_runs/2026-10-22_0709.json --sha 95abd09be1646b08adc8bdeb64f06e3265e0b2b2 --actions-run 39706630460`
- **驗收狀態**：`publication.state = "verified"`
- **公開檔案一致性**（`python3 scripts/patrol_progress.py compare-public`）：
  - `data/schedule.json`: `b73c242b7ec3f440ea3057ddae75c9973482cb9692ada9c06f7483d5b2376dd5`（逐位元一致）
  - `data/patrol_status.json`: `229eca45b92d31ec6596cb859935959e4ffc6f3b3c29a066d89f5884cc33f3de`（逐位元一致）
  - `data/metadata.json`: `a14fc180ea06dacf566c1e11aebb09ca84bf60a57dfef6da3295d871ecf60c2d`（逐位元一致）

---

## 5. 未完成項目與後續交接

1. `threads:1013.yr_`：經 4 次有界重試（重新載入、等待 30 秒、等待 60 秒開個人頁）皆擷取 0 篇，記為 `failed`。後續排程輪次可由不同網路路徑接續。
2. 社群圖片：目前全數社群媒體記為 `unread`，維持 `partial` 狀態。
3. 繡花園戲劇團《孫臏兵法》台南柳營場：目前僅有預告「11月18日，台南柳營見！」，後續排程持續關注詳細廟宇或場館與開演時間公布。
