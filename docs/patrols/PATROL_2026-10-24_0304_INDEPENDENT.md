# 2026-10-24 03:04 臺灣戲曲獨立巡檢與發布驗收報告

- **巡檢識別**：`patrol_runs/2026-10-24_0304.json`
- **開始時間**：`2026-10-24T03:04:26+08:00`
- **最後嘗試**：`2026-10-24T03:17:47+08:00`
- **發布驗收時間**：`2026-10-24T03:22:32+08:00`
- **執行工具**：Antigravity（原生 spawn Microsoft Edge、設定檔 `~/.patrol-edge`、Chrome DevTools Protocol (CDP)、文化部紀錄解析、GitHub CLI）
- **規範依據**：`AGENTS.md`、`PATROL_OPERATIONS.md`

---

## 1. 21 個來源逐一巡檢與存證結果

共巡檢 21 個目標來源，狀態動態計算為：**2 complete、18 partial、1 failed、0 pending**。總狀態依覆蓋率規則忠實判定為 **`failed`**（未達 100% 覆蓋，1 個來源連續失敗）。

| 來源鍵 | 平台／類型 | 狀態 | 擷取篇數 | 最新／最舊貼文時間 | 重試次數 | 登入牆 | 證據檔案 |
|---|---|---|---|---|---|---|---|
| `threads:joe_huang_k_w` | Threads | partial | 10 篇 | 最新 10/20 00:35、最舊 10/13 15:11 | 0 | 否 | `patrol_evidence/2026-10-24_0304/threads_joe_huang_k_w.json` |
| `threads:h.akito_1996` | Threads | partial | 10 篇 | 最新 10/23 15:11、最舊 10/16 16:26 | 0 | 否 | `patrol_evidence/2026-10-24_0304/threads_h.akito_1996.json` |
| `threads:the_rin.lpm` | Threads | partial | 6 篇 | 最新 10/20 20:27、最舊 09/26 14:32 | 0 | 否 | `patrol_evidence/2026-10-24_0304/threads_the_rin.lpm.json` |
| `threads:1013.yr_` | Threads | failed | 0 篇 | 無 | 3 (共4次) | 否 | `patrol_evidence/2026-10-24_0304/threads_1013.yr_.json` |
| `threads:xuefeng_lu_` | Threads | partial | 4 篇 | 最新 10/20 14:46、最舊 10/10 00:03 | 0 | 否 | `patrol_evidence/2026-10-24_0304/threads_xuefeng_lu_.json` |
| `threads:yuzhongluo` | Threads | partial | 9 篇 | 最新 10/19 11:15、最舊 10/11 17:50 | 0 | 否 | `patrol_evidence/2026-10-24_0304/threads_yuzhongluo.json` |
| `threads:taiwaneseopera168` | Threads | partial | 9 篇 | 最新 10/22 18:42、最舊 10/22 14:11 | 0 | 否 | `patrol_evidence/2026-10-24_0304/threads_taiwaneseopera168.json` |
| `threads:jing__1017` | Threads | partial | 6 篇 | 最新 10/20 18:17、最舊 10/16 21:49 | 0 | 否 | `patrol_evidence/2026-10-24_0304/threads_jing__1017.json` |
| `threads:hilang.on.tour` | Threads | partial | 7 篇 | 最新 10/14 11:25、最舊 10/02 11:07 | 0 | 否 | `patrol_evidence/2026-10-24_0304/threads_hilang.on.tour.json` |
| `threads:yolin1991` | Threads | partial | 7 篇 | 最新 10/22 11:28、最舊 10/13 21:15 | 0 | 否 | `patrol_evidence/2026-10-24_0304/threads_yolin1991.json` |
| `facebook:sunhope.fans` | Facebook | partial | 32 篇 | 時間未辨識 32 篇 | 0 | 否 | `patrol_evidence/2026-10-24_0304/facebook_sunhope.fans.json` |
| `facebook:HsiaoHsiYuan1913` | Facebook | partial | 34 篇 | 時間未辨識 34 篇 | 0 | 否 | `patrol_evidence/2026-10-24_0304/facebook_HsiaoHsiYuan1913.json` |
| `facebook:100063868113954` | Facebook | partial | 35 篇 | 時間未辨識 35 篇 | 0 | 否 | `patrol_evidence/2026-10-24_0304/facebook_100063868113954.json` |
| `facebook:MingHuaYuanTianTaiwaneseOpera` | Facebook | partial | 29 篇 | 時間未辨識 29 篇 | 0 | 否 | `patrol_evidence/2026-10-24_0304/facebook_MingHuaYuanTianTaiwaneseOpera.json` |
| `facebook:61574134933376` | Facebook | partial | 26 篇 | 時間未辨識 26 篇 | 0 | 否 | `patrol_evidence/2026-10-24_0304/facebook_61574134933376.json` |
| `facebook:mhysun` | Facebook | partial | 31 篇 | 時間未辨識 31 篇 | 0 | 否 | `patrol_evidence/2026-10-24_0304/facebook_mhysun.json` |
| `facebook:61594936681482` | Facebook | partial | 6 篇 | 時間未辨識 6 篇 | 0 | 否 | `patrol_evidence/2026-10-24_0304/facebook_61594936681482.json` |
| `facebook:lanyang.opera` | Facebook | partial | 31 篇 | 時間未辨識 31 篇 | 0 | 否 | `patrol_evidence/2026-10-24_0304/facebook_lanyang.opera.json` |
| `facebook:Taichungpuppettheater` | Facebook | partial | 32 篇 | 時間未辨識 32 篇 | 0 | 否 | `patrol_evidence/2026-10-24_0304/facebook_Taichungpuppettheater.json` |
| `culture` | 文化部 | complete | 1534 筆 | 候選 17 筆，新建 1 筆，重複 1 筆，其餘 15 筆為展覽/工作坊逐筆審核處置完成 | 0 | 否 | `data/moc_records.json` |
| `issues` | GitHub | complete | 2 筆 | Issues #1、#2 檢核皆為 open，無新留言 | 0 | 否 | GitHub CLI & REST API |

---

## 2. 提到未來演出之貼文逐篇判斷與比對結果

經 `scripts/extract_mentions.py` 自巡檢證據中提取 237 篇演出相關貼文，篩選出涉及未來（2026-10-24 及以後）之 41 篇貼文，逐篇核對 `data/schedule.json` 如下：

### 【新建卡片】（共 1 筆社群卡片）

1. **新吉義林歌劇團 雲林四湖參天宮廣場 外台公演**
   - **來源**：`threads:yolin1991:DeyBKTzGgA6`
   - **卡片 ID**：`auto-20261024-5717b6a3`
   - **原文逐字片段**：
     > 「📌新吉義林歌劇團 演出資訊 📣 🗓️演出日期：10月24（六） ⏰演出時間：待公布 📍演出地點：雲林四湖參天宮廣場」
   - **新增事實**：日期 2026-10-24、時間 未公布、地點 雲林四湖參天宮廣場、劇團 新吉義林歌劇團、劇名 新吉義林歌劇團 演出資訊、性質 廟會民俗演出。

### 【已在表且一致】

1. **明華園天字戲劇團 2026閩南傳統藝術巡演《八仙傳奇》桃園龜山場**
   - **來源**：`facebook:MingHuaYuanTianTaiwaneseOpera:0bd067ca1bb5`、`facebook:100063868113954:8d15194b76c6`、`threads:taiwaneseopera168:DeyU3EjkQE_`
   - **比對卡片**：`mhy-tian-2026-10-25-bade`
   - **原文片段**：「外台公演｜2026 閩南傳統藝術巡演 演出時間｜ 10/25（日）晚上 7:00 演出戲碼｜八仙傳奇-張果老與藍采和 演出地點｜ 壽山嚴觀音寺停車場（桃園市龜山區嶺頂里萬壽路二段6巷111號）」
   - **核對結果**：卡片已收錄，日期（2026-10-25）、時間（19:00–21:30）、地點與劇目完全一致。

2. **明華園天字戲劇團 臺南南廠水門宮外台演出**
   - **來源**：`facebook:100063868113954:40e6571de221`、`facebook:100063868113954:8d15194b76c6`
   - **比對卡片**：`mhy-tian-2026-10-23-shuimen`
   - **原文片段**：「明天 10/24 演出時間公告 下午 5:00 開始扮仙 扮仙結束後，接著正式演出 演出地點一樣在廟內進行 南廠水門宫 時間：10/24 地點：台南市南區仁南街86號」
   - **核對結果**：卡片已收錄，日期（2026-10-23 至 2026-10-24）、時間（10/23 下午 3:30、10/24 下午 5:00）、地點（臺南市南區仁南街86號 水門宮）完全一致。

3. **繡花園戲劇團《孫臏兵法》臺南柳營代天院場**
   - **來源**：`facebook:61574134933376:5a5635caeeb3`
   - **比對卡片**：`auto-20261118-f7e6977b`
   - **原文片段**：「這回，《孫臏兵法》將來到臺南柳營！新營五間厝大豐宮 ◎慶讚 柳營代天院｜柳營王醮《敬王爺‧看大戲》」
   - **核對結果**：卡片已收錄，日期（2026-11-18）、時間（晚上 7:30）、地點與劇名完全一致。

4. **尚和歌仔戲劇團《HOLIDAY 午後沉浸式茶戲體驗》（田和越・茶劇場）**
   - **來源**：`facebook:sunhope.fans:4163f0e2fd02`
   - **比對卡片**：`auto-20261024-f7a76b26`
   - **原文片段**：「10/24（六）《HOLIDAY 午後沉浸式茶戲體驗》下午 2:00－3:30 田和越茶劇場」
   - **核對結果**：卡片已收錄，日期、時間與地點完全一致。

5. **羅裕誴歌劇團《府城有神・人間有情》（南瀛國際民俗藝術節 薪瀛舞台）**
   - **來源**：`threads:yuzhongluo:DeeXP_umU6t`
   - **比對卡片**：`auto-20261024-84da22bc`
   - **原文片段**：「10月24日（六）下午3點~薪瀛舞台展演 新營文化中心演藝廳前」
   - **核對結果**：卡片已收錄，資訊一致。

6. **秀琴歌劇團《玉石變》新莊保元宮場**
   - **來源**：`threads:the_rin.lpm:DdvZekJE9Mm`
   - **比對卡片**：`sc-2026-11-07-yushibian`
   - **原文片段**：「📅11/07 19：00 🎭戲碼：《玉石變》📍地點：新莊保元宮」
   - **核對結果**：卡片已收錄，資訊一致。

7. **秀琴歌劇團《金沙灘》西港慶安宮場**
   - **來源**：`threads:the_rin.lpm:DdvZekJE9Mm`
   - **比對卡片**：`sc-2026-11-15-jinshatan`
   - **原文片段**：「📅11/15 19：00 🎭戲碼：《金沙灘》 📍地點：西港慶安宮」
   - **核對結果**：卡片已收錄，資訊一致。

8. **蘭陽戲劇團《錯配姻緣》桃園顯安巖祖師廟場**
   - **來源**：`facebook:lanyang.opera:da8fb28a6c96`
   - **比對卡片**：`lanyang-2026-10-26-guishan-cuoxie-yinyuan`
   - **原文片段**：「蘭陽戲劇團將於 10 月 26 日（一）晚間 19:00，在桃園市顯安巖祖師廟演出《錯配姻緣》」
   - **核對結果**：卡片已收錄，資訊一致。

9. **台中木偶劇團《聖劍風雲三》臺中屯區藝文中心實驗劇場**
   - **來源**：`facebook:Taichungpuppettheater:9711d0738c28`、`96ba8c444e85`、`4bd70383e575`、`b769ce927a9d`
   - **比對卡片**：`tcpt-2026-11-07-shengjianfengyun-3`
   - **原文片段**：「115/11/7（六） 下午14:30 屯區藝文中心-實驗劇場」
   - **核對結果**：卡片已收錄，資訊一致。

10. **明華園戲劇總團《烏龍天下》**
    - **來源**：`facebook:mhysun:da3a748b363d`、`b9326fb3d6d6`、`28c3c6954007`
    - **比對卡片**：`mhy-flagship-2026-11-20`、`mhy-oolong-wv-2026-12-19`
    - **核對結果**：卡片已收錄，資訊一致。

11. **古都木偶劇團《台灣風雲錄・戰火波瀾》苗栗竹南場**
    - **來源**：`facebook:61594936681482:cf8dcf1cc216`、`threads:hilang.on.tour:DedaYXykx0c`、`threads:joe_huang_k_w:DedaxOSCfHY`
    - **比對卡片**：`amichen-2026-10-30-zhunan-taiwan-fengyunlu`
    - **核對結果**：卡片已收錄，資訊一致。

### 【海報未讀】（共 11 篇）

以下貼文僅附海報圖片或文字簡略註明「詳見海報／如圖／戲路表」，正文未完整刊載演出事實，依規範不予建卡，列入「海報未讀」：
1. `facebook:100063868113954:2227207e47f9`（吳奕萱：2026農曆9月戲路表，海報圖1張）
2. `facebook:61574134933376:423d70d71578`（繡花園：《陷空山一日旅》新版海報公開，海報圖1張）
3. `facebook:lanyang.opera:dab2c68c5d6b`（蘭陽戲劇團：9月演出預告海報圖1張）
4. `facebook:lanyang.opera:37173532d886`（蘭陽戲劇團：新秀登臺培育計畫主視覺海報圖1張）
5. `facebook:lanyang.opera:8e41528ff262`（蘭陽戲劇團：8月演出預告海報圖1張）
6. `facebook:lanyang.opera:76be96c50423`（蘭陽戲劇團：7月演出預告海報圖1張）
7. `facebook:mhysun:b3b5d3c6be16`（明華園總團：父親節圖卡5張）
8. `facebook:sunhope.fans:911fb6535995`（尚和歌仔戲劇團：《魔法柑仔店》活動海報圖1張）
9. `facebook:sunhope.fans:538f996cd917`（尚和歌仔戲劇團：小尚報馬仔圖卡1張）
10. `threads:the_rin.lpm:Ddy9Vv8k7IV`（秀琴歌劇團：劇團新戲路表圖片1張）
11. `threads:the_rin.lpm:Debra7kE-_v`（火燒紅蓮寺抽獎圖卡1張）

### 【非演出／未在表公告處理】

1. `threads:taiwaneseopera168:DeyVW8TkZpQ`、`DeyelRfEc3E`：
   - 內容：明華園戲劇總團原訂 10/24(六) 桃園中壢天德宮《薛丁山傳奇》因薔琵颱風延期舉辦。
   - 核對：原表無中壢天德宮場次，無須執行 `--cancel` 或修改。
2. `facebook:61574134933376:e37d22e6be54`：傳藝中心「重塑民間劇場」補助審查結果，非演出。
3. `threads:jing__1017:DetmZSJCfNr`：米雪文化 10 月歌仔戲《頭飾手作梳妝＆戲曲卡拉OK》工作坊，非演出。
4. `threads:the_rin.lpm:DejZXiykw3q`：秀琴歌劇團《戲棚下・逐星路》講座，非演出。
5. `facebook:Taichungpuppettheater:53d4bc7c7938`、`33719405b40a`、`0ba2c7186d2c`、`77fa45916ac0`、`a84061e8ec91`、`c97e2667ba3d`：偶遇科技戲偶互動展與講座活動，非演出。
6. `facebook:sunhope.fans:df136bf769f6`：歌仔繪本演故事推廣活動，非演出。

---

## 3. 文化部開放資料比對

- **來源檔案**：`data/moc_records.json`（由 GitHub 更新器產生）
- **抓取時間（fetchedAt）**：`2026-10-23T09:08:19+08:00`（距今約 18 小時，未逾 36 小時門檻）
- **資料總筆數（total）**：1534 筆（達 500 筆新鮮度門檻）
- **符合關鍵字紀錄數**：37 筆
- **在表筆數**：20 筆
- **不在表候選數**：17 筆
- **不在表 17 筆逐筆審核處置與理由**：

1. `偶偶偶劇團《小狐狸買手套》`：偶劇演出（2026/12/04–12/06 臺北市文山劇場），執行 `python3 scripts/add_card.py --from-moc "偶偶偶劇團《小狐狸買手套》"`，**成功建卡**（卡片 ID `moc-2088104133013299200-dec93f`）。
2. `台中木偶劇團 《聖劍風雲三》`：布袋戲演出，執行 `python3 scripts/add_card.py --from-moc "台中木偶劇團 《聖劍風雲三》"`，因同日期（2026-11-07）同場館（臺中市屯區藝文中心實驗劇場）已有既有卡片 `tcpt-2026-11-07-shengjianfengyun-3`，依規則被 add_card.py 拒絕（`duplicate-or-no-valid-shows`），視為已在表。
3. `桃園市土地公文化館常設展-302土地公節日慶典與科儀活動`：常設展覽，非演出（含「展」字，不予建卡）。
4. `世紀初戀－楊麗花歌仔戲特展`：特展，非演出（含「展」字，不予建卡）。
5. `2026年1月【雲林布袋戲館-「掌演乾坤」常設展】`：常設展，非演出（含「展」字，不予建卡）。
6. `2026年1月【雲林布袋戲館-《傳藝之魂‧黃海岱與戲偶之道》特展】`：特展，非演出（含「展」字，不予建卡）。
7. `高雄市皮影戲館常設展`：常設展，非演出（含「展」字，不予建卡）。
8. `115年「掌藝薪傳-大師工作坊」`（第 1 筆）：工作坊，非演出（含「工作坊」字，不予建卡）。
9. `115年「掌藝薪傳-大師工作坊」`（第 2 筆）：工作坊，非演出（含「工作坊」字，不予建卡）。
10. `115年「掌藝薪傳-大師工作坊」`（第 3 筆）：工作坊，非演出（含「工作坊」字，不予建卡）。
11. `三昧堂精工布袋戲展`（第 1 筆）：展覽，非演出（含「展」字，不予建卡）。
12. `三昧堂精工布袋戲展`（第 2 筆）：展覽，非演出（含「展」字，不予建卡）。
13. `【特展】 「請戲-布袋戲一條街」特展`：特展，非演出（含「展」字，不予建卡）。
14. `金鷹歸來：隆興閣掌中武林特展`：特展，非演出（含「展」字，不予建卡）。
15. `登出世界、登入自我！《虛。實─數位與我》插畫創作聯展`（第 1 筆）：插畫聯展，非演出（含「展」字，不予建卡）。
16. `登出世界、登入自我！《虛。實─數位與我》插畫創作聯展`（第 2 筆）：插畫聯展，非演出（含「展」字，不予建卡）。
17. `登出世界、登入自我！《虛。實─數位與我》插畫創作聯展`（第 3 筆）：插畫聯展，非演出（含「展」字，不予建卡）。

---

## 4. GitHub Issues 巡檢

- **讀取指令**：`gh api "repos/eric1810-tw/taiwan-opera-calendar/issues?state=all&sort=updated&direction=desc"`
- **檢核結果**：儲存庫共有 2 筆 Issues（Issue #1、#2），皆於 2026-09-28 建立，狀態均為 `open`，留言數為 0。
- **異動與處置**：本輪巡檢無新建 Issue、無重開或關閉、無新留言。

---

## 5. 發布驗收與公開一致性比對

- **資料提交 SHA**：[`623f9b56f338fde18e65504176dfa841d251e7b5`](https://github.com/eric1810-tw/taiwan-opera-calendar/commit/623f9b56f338fde18e65504176dfa841d251e7b5)
- **GitHub Actions 執行**：[Daily Opera Schedule Auto-Updater Run 40010826726](https://github.com/eric1810-tw/taiwan-opera-calendar/actions/runs/40010826726)
  - 狀態：`completed` / `success`
- **發布驗收（`patrol_progress.py verify`）**：狀態轉為 `verified`。
- **公開站逐位元比對（`compare-public`）**：`allMatch: true`
  - `data/schedule.json`：`38451186703c092ab9ddbbace5b836032122e9e1a28c01a7f06b2f5c9f71e14f`（MATCH）
  - `data/patrol_status.json`：`43e1863d36b37e487f2133e52dec598d6e76c6fb914ec4dd2f9e569f9b205258`（MATCH）
  - `data/metadata.json`：`950100068bdbe3fe53dfa9c2d0184cd0496a2640b867a1b876f895545d478166`（MATCH）

---

## 6. 未完成項目與後續交接

1. `threads:1013.yr_` 本輪重試 4 次皆回傳 0 篇貼文（非登入牆），依覆蓋率規則忠實判定為 `failed`。後續巡檢輪應持續追蹤該帳號之可讀性。
2. 11 篇「海報未讀」貼文包含劇團戲路表與活動宣傳圖卡，待後續具備圖片解析能力或官方發布文字版演出資訊時再行收錄。
