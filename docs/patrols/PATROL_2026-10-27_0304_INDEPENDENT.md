# 2026-10-27 03:04 臺灣戲曲獨立巡檢與發布驗收報告

- **巡檢識別**：`patrol_runs/2026-10-27_0304.json`
- **開始時間**：`2026-10-27T03:05:03+08:00`
- **最後嘗試**：`2026-10-27T03:16:27+08:00`
- **發布驗收時間**：`2026-10-27T03:20:25+08:00`
- **執行工具**：Antigravity（原生 spawn Microsoft Edge、專用設定檔 `~/.patrol-edge`、Chrome DevTools Protocol (CDP)、文化部開放資料紀錄解析、GitHub CLI）
- **規範依據**：`AGENTS.md`、`PATROL_OPERATIONS.md`

---

## 1. 21 個來源逐一巡檢與存證結果

共巡檢 21 個目標來源，狀態動態計算為：**2 complete、18 partial、1 failed、0 pending**。總狀態依覆蓋率規則忠實判定為 **`failed`**（因 `threads:1013.yr_` 連續重試 4 次後仍為 0 篇貼文 failed）。

| 來源鍵 | 平台／類型 | 狀態 | 擷取篇數 | 最新／最舊貼文時間 | 重試次數 | 登入牆 | 證據檔案 |
|---|---|---|---|---|---|---|---|
| `threads:joe_huang_k_w` | Threads | partial | 13 篇 | 最新 10/25 21:42、最舊 10/15 16:48 | 0 | 否 | `patrol_evidence/2026-10-27_0304/threads_joe_huang_k_w.json` |
| `threads:h.akito_1996` | Threads | partial | 9 篇 | 最新 10/25 23:49、最舊 10/19 15:11 | 0 | 否 | `patrol_evidence/2026-10-27_0304/threads_h.akito_1996.json` |
| `threads:the_rin.lpm` | Threads | partial | 6 篇 | 最新 10/20 20:27、最舊 09/26 14:32 | 0 | 否 | `patrol_evidence/2026-10-27_0304/threads_the_rin.lpm.json` |
| `threads:1013.yr_` | Threads | failed | 0 篇 | 無 | 3 (共4次) | 否 | `patrol_evidence/2026-10-27_0304/threads_1013.yr_.json` |
| `threads:xuefeng_lu_` | Threads | partial | 7 篇 | 最新 10/27 01:06、最舊 10/10 00:03 | 0 | 否 | `patrol_evidence/2026-10-27_0304/threads_xuefeng_lu_.json` |
| `threads:yuzhongluo` | Threads | partial | 8 篇 | 最新 10/22 20:39、最舊 10/19 11:16 | 0 | 否 | `patrol_evidence/2026-10-27_0304/threads_yuzhongluo.json` |
| `threads:taiwaneseopera168` | Threads | partial | 5 篇 | 最新 10/27 01:08、最舊 08/16 02:33 | 0 | 否 | `patrol_evidence/2026-10-27_0304/threads_taiwaneseopera168.json` |
| `threads:jing__1017` | Threads | partial | 10 篇 | 最新 10/22 01:58、最舊 10/19 21:03 | 0 | 否 | `patrol_evidence/2026-10-27_0304/threads_jing__1017.json` |
| `threads:hilang.on.tour` | Threads | partial | 7 篇 | 最新 10/14 11:25、最舊 10/02 11:07 | 0 | 否 | `patrol_evidence/2026-10-27_0304/threads_hilang.on.tour.json` |
| `threads:yolin1991` | Threads | partial | 7 篇 | 最新 10/25 22:39、最舊 10/15 16:29 | 0 | 否 | `patrol_evidence/2026-10-27_0304/threads_yolin1991.json` |
| `facebook:sunhope.fans` | Facebook | partial | 32 篇 | 時間未辨識 32 篇 | 0 | 否 | `patrol_evidence/2026-10-27_0304/facebook_sunhope.fans.json` |
| `facebook:HsiaoHsiYuan1913` | Facebook | partial | 33 篇 | 時間未辨識 33 篇 | 0 | 否 | `patrol_evidence/2026-10-27_0304/facebook_HsiaoHsiYuan1913.json` |
| `facebook:100063868113954` | Facebook | partial | 35 篇 | 時間未辨識 35 篇 | 0 | 否 | `patrol_evidence/2026-10-27_0304/facebook_100063868113954.json` |
| `facebook:MingHuaYuanTianTaiwaneseOpera` | Facebook | partial | 29 篇 | 時間未辨識 29 篇 | 0 | 否 | `patrol_evidence/2026-10-27_0304/facebook_MingHuaYuanTianTaiwaneseOpera.json` |
| `facebook:61574134933376` | Facebook | partial | 26 篇 | 時間未辨識 26 篇 | 0 | 否 | `patrol_evidence/2026-10-27_0304/facebook_61574134933376.json` |
| `facebook:mhysun` | Facebook | partial | 29 篇 | 時間未辨識 29 篇 | 0 | 否 | `patrol_evidence/2026-10-27_0304/facebook_mhysun.json` |
| `facebook:61594936681482` | Facebook | partial | 5 篇 | 時間未辨識 5 篇 | 0 | 否 | `patrol_evidence/2026-10-27_0304/facebook_61594936681482.json` |
| `facebook:lanyang.opera` | Facebook | partial | 33 篇 | 時間未辨識 33 篇 | 0 | 否 | `patrol_evidence/2026-10-27_0304/facebook_lanyang.opera.json` |
| `facebook:Taichungpuppettheater` | Facebook | partial | 32 篇 | 時間未辨識 32 篇 | 0 | 否 | `patrol_evidence/2026-10-27_0304/facebook_Taichungpuppettheater.json` |
| `culture` | 文化部 | complete | 1423 筆 | total=1423，fetchedAt=2026-10-26T08:56:16+08:00，候選 24 筆（15 筆為非演出排除，9 筆演出均已收錄），建卡 0 筆 | 0 | 否 | `data/moc_records.json` |
| `issues` | GitHub | complete | 2 筆 | Issues #1、#2 檢核皆為 open，無新留言，提報演出皆已建卡在表 | 0 | 否 | GitHub REST API |

---

## 2. 提到未來演出之社群貼文逐篇判斷與比對結果

經 `scripts/extract_mentions.py` 自巡檢證據中提取 231 篇演出相關貼文，篩選出涉及未來（2026-10-27 及以後）之貼文逐篇核對 `data/schedule.json` 如下：

### 【已在表且一致】

1. **明華園天字戲劇團 小北城隍廟外台民戲**
   - **來源**：`facebook:100063868113954`（吳奕萱貼文）
   - **比對卡片**：`mhy-tian-2026-10-26-xiaobei`
   - **原文片段**：「接下來的演出行程看這裡 小北城隍廟 時間：10/26-10/27 地點：台南市北區西門路四段70巷17號」
   - **核對結果**：卡片已收錄，日期（2026/10/26–2026/10/27）、地點（臺南市北區西門路四段70巷17號）一致，開演時間貼文未公布。

2. **明華園天字戲劇團 茄萣天府-薛府千歲外台民戲**
   - **來源**：`facebook:100063868113954`（吳奕萱貼文）
   - **比對卡片**：`mhy-tian-2026-10-28-xuefu`
   - **原文片段**：「茄萣天府-薛府千歲 時間：10/28-10/29 地點：高雄市茄萣區莒光路三段167號」
   - **核對結果**：卡片已收錄，日期（2026/10/28–2026/10/29）、地點（高雄市茄萣區莒光路3段167號）一致，開演時間貼文未公布。

3. **台南古都掌中劇團《台灣風雲錄・戰火波瀾》苗栗竹南場**
   - **來源**：`facebook:61594936681482`、`threads:hilang.on.tour`
   - **比對卡片**：`amichen-2026-10-30-zhunan-taiwan-fengyunlu`
   - **原文片段**：「10/30，阿籠邀你到竹南的草地上，看古都用布袋戲演出《台灣風雲錄・戰火波瀾》，一起回望這座島嶼的歷史波瀾。 📍 苗栗竹南運動公園大草坪 📅 2026/10/30（五） 🕔 17:00進場｜18:00開演 主演｜台南古都掌中劇團」
   - **核對結果**：卡片已收錄，日期（2026-10-30）、時間（17:00 開放進場；18:00 正式開演）、地點一致。

4. **秀琴歌劇團《玉石變》新莊保元宮大型公演**
   - **來源**：`threads:the_rin.lpm`
   - **比對卡片**：`sc-2026-11-07-yushibian`
   - **原文片段**：「📅11/07 19：00 🎭戲碼：《玉石變》📍地點：新莊保元宮」
   - **核對結果**：卡片已收錄，日期（2026-11-07）、時間（19:00）、地點完全一致。

5. **秀琴歌劇團《金沙灘》西港慶安宮大型公演**
   - **來源**：`threads:the_rin.lpm`
   - **比對卡片**：`sc-2026-11-15-jinshatan`
   - **原文片段**：「📅11/15 19：00 🎭戲碼：《金沙灘》 📍地點：西港慶安宮」
   - **核對結果**：卡片已收錄，日期（2026-11-15）、時間（19:00）、地點完全一致。

6. **尚和歌仔戲劇團 全新9號作《寒窯之外》（田和越・茶劇場）**
   - **來源**：`facebook:sunhope.fans`
   - **比對卡片**：`sh-2026-11-07-hanyao-zhiwai`
   - **原文片段**：「TEN OR ONE 全新9號作【寒窯之外】 演出日期：11/7（六）、11/8（日） 購票網址： https://www.opentix.life/event/2056288538199531521」
   - **核對結果**：卡片已收錄，日期、地點（高雄市鼓山區美術南一街192號 田和越．茶劇場）與購票網址完全一致。

7. **尚和歌仔戲劇團《驫－馬的心事》（田和越・茶劇場）**
   - **來源**：`facebook:sunhope.fans`
   - **比對卡片**：`sh-2026-12-12-madexinshi-1`、`sh-2026-12-19-madexinshi-2`
   - **原文片段**：「為今年十二月【驫•馬的心事】演出製作一步步努力中！... 12/12（六）－12/13（日）《驫－馬的心事》上集 12/19（六）－12/20（日）《驫－馬的心事》下集」
   - **核對結果**：卡片已依上、下集分別建卡，日期與地點完全一致。

8. **台中木偶劇團 科技布袋戲《聖劍風雲三–龍虎兄弟》**
   - **來源**：`facebook:Taichungpuppettheater`
   - **比對卡片**：`tcpt-2026-11-07-shengjianfengyun-3`
   - **原文片段**：「【台中木偶劇團｜科技布袋戲】《聖劍風雲三–龍虎兄弟》... 11/7（六）歡迎一起進劇場來看戲」
   - **核對結果**：卡片已收錄，日期（2026-11-07）、演出地點（臺中市屯區藝文中心演藝廳）與售票連結完全一致。

9. **明華園戲劇總團 旗艦製作《烏龍天下》（臺北、臺中、高雄巡演）**
   - **來源**：`facebook:mhysun`（孫翠鳳粉專）
   - **比對卡片**：`mhy-flagship-2026-11-20`（臺灣戲曲中心）、`mhy-oolong-tc-2026-12-05`（臺中國家歌劇院）、`mhy-oolong-wv-2026-12-19`（衛武營）
   - **原文片段**：「明華園戲劇總團下半年重頭大戲——《烏龍天下》 今天來到「2026 歌仔戲旗艦展演計畫」記者會...」
   - **核對結果**：三巡迴場次皆已分別建卡在表，售票連結與演出地點完全一致。

10. **繡花園戲劇團《孫臏兵法》臺南柳營場**
    - **來源**：`facebook:61574134933376`
    - **比對卡片**：`auto-20261118-f7e6977b`
    - **原文片段**：「這回，《孫臏兵法》將來到臺南柳營！ 邀請喜愛歌仔戲的朋友們」
    - **核對結果**：卡片已收錄於日程表，演出日期（2026-11-18）與地點完全一致。

---

## 3. 海報未讀（Poster-Only）貼文清單

本次巡檢擷取之貼文中，共有 21 篇含有圖片但正文未列完整演出時間與詳細地址之貼文（依巡檢守則不逕自猜測或建卡，列入海報未讀）：

1. `facebook:100063868113954`（吳奕萱）: `https://www.facebook.com/photo/?fbid=1620804473391808`（中秋節慶賀圖）
2. `facebook:61574134933376`（繡花園）: `https://www.facebook.com/photo/?fbid=122176089698804497`（演後側拍劇照 5 張）
3. `facebook:HsiaoHsiYuan1913`（小西園）: `https://www.facebook.com/photo/?fbid=1457360433057160`（新年祝福圖）
4. `facebook:HsiaoHsiYuan1913`（小西園）: `https://www.facebook.com/photo/?fbid=1380316800761524`（中秋祝福圖 2 張）
5. `facebook:HsiaoHsiYuan1913`（小西園）: `https://www.facebook.com/photo/?fbid=992105692915972`（端午節祝福圖）
6. `facebook:HsiaoHsiYuan1913`（小西園）: `https://www.facebook.com/photo/?fbid=4938090939571505`（節慶祝福圖）
7. `facebook:HsiaoHsiYuan1913`（小西園）: `https://www.facebook.com/photo/?fbid=4359405620773376`（歷史相片回顧）
8. `facebook:HsiaoHsiYuan1913`（小西園）: `https://www.facebook.com/photo/?fbid=4269151523132120`（演出紀錄照）
9. `facebook:HsiaoHsiYuan1913`（小西園）: `https://www.facebook.com/photo/?fbid=3640248446022434`（大稻埕戲苑演後回顧）
10. `facebook:HsiaoHsiYuan1913`（小西園）: `https://www.facebook.com/photo/?fbid=1866124353434861`（戲曲推廣相片）
11. `facebook:MingHuaYuanTianTaiwaneseOpera`（天字團）: `https://www.facebook.com/photo/?fbid=1528865579285729`（農曆八月戲路圖，正文未列明牌）
12. `facebook:Taichungpuppettheater`（台中木偶）: GIF 動圖（戲臺下的另一種精彩）
13. `facebook:Taichungpuppettheater`（台中木偶）: `https://www.facebook.com/100063900765455/videos/pcb.1500362582103753/2087380138522752`（畢業季偶戲影片照片 4 張）
14. `facebook:lanyang.opera`（蘭陽）: 影片縮圖（人才培育計畫推廣）
15. `facebook:lanyang.opera`（蘭陽）: `https://www.facebook.com/photo/?fbid=1447476297410979`（大福補天宮演後劇照）
16. `facebook:lanyang.opera`（蘭陽）: `https://www.facebook.com/photo/?fbid=1447184957440113`（女媧娘娘祝壽劇照）
17. `facebook:lanyang.opera`（蘭陽）: `https://www.facebook.com/photo/?fbid=1444276201064322`（培育計畫宣傳圖）
18. `facebook:lanyang.opera`（蘭陽）: `https://www.facebook.com/photo/?fbid=1411516244340318`（歷史演出照片）
19. `facebook:lanyang.opera`（蘭陽）: `https://www.facebook.com/photo/?fbid=1374526618039281`（劇團彩排照片）
20. `facebook:lanyang.opera`（蘭陽）: `https://www.facebook.com/photo/?fbid=1327118086113468`（公演劇照）
21. `facebook:sunhope.fans`（尚和）: `https://www.facebook.com/photo/?fbid=1716331140498595`（秋冬巡演行程彙整圖；其中 11/29《西遊記之芭蕉密碼》正文無地點，僅圖片載有資訊）

---

## 4. 文化部開放資料逐筆查核結果

- **資料時間**：`fetchedAt=2026-10-26T08:56:16+08:00`（小於 36 小時門檻）
- **總筆數**：1423 筆（大於 500 筆門檻）
- **篩選戲曲紀錄**：共 34 筆紀錄
- **逐筆核對與處置**：
  1. 桃園市土地公文化館常設展-302土地公節日慶典與科儀活動：常設展，非演出，排除。
  2. 2026年1月【雲林布袋戲館-「掌演乾坤」常設展】：常設展，非演出，排除。
  3. 2026年1月【雲林布袋戲館-《傳藝之魂‧黃海岱與戲偶之道》特展】：特展，非演出，排除。
  4. 高雄市皮影戲館常設展：常設展，非演出，排除。
  5. 115年「掌藝薪傳-大師工作坊」（共3筆）：傳藝工作坊，非演出，排除。
  6. 三昧堂精工布袋戲展（共2筆）：偶戲精工展，非演出，排除。
  7. 【掌中戲】五洲勝義閣掌中劇團《濟世降魔傳》：已收錄於表（`wz-2026-10-31`）。
  8. 【掌中戲】新西園掌中劇團《文素臣之大義滅親-殺嫂》：已收錄於表（`moc-20261107-90b0df6d19`）。
  9. 【掌中戲】不貳偶劇《天雷報》：已收錄於表（`moc-20261121-4a31ddab01`）。
  10. 【特展】 「請戲-布袋戲一條街」特展：特展，非演出，排除。
  11. 金鷹歸來：隆興閣掌中武林特展：特展，非演出，排除。
  12. 長義閣掌中劇團「銳劇場」系列 -《我,哪吒》：已收錄於表（`cyg-2026-12-05-nezha`）。
  13. 2026臺南藝術節：李淸照私人劇團感傷動作派《歌仔寶玉講唱》：已收錄於表（`tnaf-2026-11-14-baoyu`）。
  14. 【歌仔戲】元和劇子-鼓震千秋《梁紅玉》：已收錄於表（`yuanhe-2026-10-30`）。
  15. 義興閣掌中劇團《豆花公劇場版－拍斷手骨顛倒勇》：已收錄於表（`yxg-2026-12-05-douhuagong-chiayi`、`yxg-2026-12-19-douhuagong-shulin`）。
  16. 義興閣掌中劇團《四靈國：天祥書之謎》：已收錄於表（`yxg-2026-11-21-silingguo-taipei`、`yxg-2026-12-06-silingguo-chiayi`）。
  17. 2026 NTT遇見巨人—唐美雲歌仔戲團《南都幽靈夜譚》：已收錄於表（`tmy-tc-2026-12-26`）。
  18. 2026歌仔戲旗艦展演補助計畫-明華園總團旗艦製作《烏龍天下》：含展字關鍵字且演出已收錄於表（`mhy-flagship-2026-11-20`）。
  19. 山宛然劇團兒童布袋戲《鷂婆在哪裡？》（4場）：已收錄於表（`moc-20261107-1f034f9eff` 等）。
  20. 2026歌仔戲旗艦展演—唐美雲歌仔戲團《南都幽靈夜譚》：含展字關鍵字且演出已收錄於表（`tmy-flagship-2026-11-27`）。
  21. 2026唐美雲歌仔戲團《南都幽靈夜譚》高雄場（2場）：已收錄於表（`moc-20261212-dff909a239`、`moc-20261213-2bbd4d9c21`）。
  22. 偶偶偶劇團《小狐狸買手套》：已收錄於表（`moc-2088104133013299200-dec93f`）。
  23. 兒童布袋戲《焰王現身：心火山的祕密》：已收錄於表（`child-puppets-2026-10-31`）。
  24. 台中木偶劇團 《聖劍風雲三》：已收錄於表（`tcpt-2026-11-07-shengjianfengyun-3`）。
  25. 拉縴人男聲合唱團《英雄路－布袋戲聲音行旅》：已收錄於表（`tmc-2026-11-22-heros-journey`）。
  26. 登出世界、登入自我！《虛。實─數位與我》插畫創作聯展（共3筆）：插畫聯展，非戲曲演出，排除。
  27. 「戲來就演！」－布袋戲演師們的大挑戰：已收錄於表（`moc-2109890724705943553-033c8f`）。
  28. 2026金鷹閣電視木偶劇團《叱吒風雲－新哪吒》臺中巡演：已收錄於表（`moc-2112035354878472193-f1daf3`）。
  29. 《吟遊詩人的新唸歌——桃園米倉》：已收錄於表（`moc-2110369335028596737-8ddf63`）。
- **結論**：15 筆為非演出排除，其餘 19 筆演出均已完整收錄於日程表，本輪文化部開放資料建卡 0 筆，記為 `complete`。

---

## 5. GitHub Issues 查核結果

- 透過 `gh api repos/eric1810-tw/taiwan-opera-calendar/issues?state=all` 唯讀查詢全數 Issues。
- Issue #1（走戲人《酷麗鳥搞砸了》）與 Issue #2（《龍女流浪記》）均維持 open，comments=0，無任何新建留言或更新。
- 兩筆提報演出先前均已查核 OPENTIX 售票頁並建卡在表（`zx-2026-11-14-kuliniao` 與 `zx-2026-11-15-longnu`），本輪查核無待處理事項，記為 `complete`。

---

## 6. 資料異動與發布驗收

- **新增卡片**：0 筆
- **更新卡片**：0 筆
- **被拒絕提案**：0 筆
- **資料提交 SHA**：[`7f1ef84214c9651754732c944936633c83c1699f`](https://github.com/eric1810-tw/taiwan-opera-calendar/commit/7f1ef84214c9651754732c944936633c83c1699f)
- **GitHub Actions 部署**：
  - Workflow: `Daily Opera Schedule Auto-Updater` (`.github/workflows/daily-update.yml`)
  - Run ID: [`40385748135`](https://github.com/eric1810-tw/taiwan-opera-calendar/actions/runs/40385748135)
  - Head SHA: `7f1ef84214c9651754732c944936633c83c1699f`
  - 狀態: `completed` / `success`
- **公開端點比對（`compare-public`）**：
  - `data/schedule.json` SHA-256: `67dcabf6447bd0d9042fb4383c6818971f7cf12e79f5b58233cba1289d2e79b6` (MATCH: true)
  - `data/patrol_status.json` SHA-256: `fe9354d75d39bc572efc3db66b37adebe614ba72c1b39ad5da6baf26b82fc6bc` (MATCH: true)
  - `data/metadata.json` SHA-256: `8a205b48ba12dd698ad3c6f86765fcaa3182825b4962872c4f1532aeb43e1312` (MATCH: true)
  - 全數 JSON 逐位元相符 (`allMatch: true`)。

---

## 7. 受保護檔案完整性校驗

本工作階段嚴格遵循規範，未更動、未 stage、未刪除下列 6 個受保護檔案：
- `7e551b66ec48c95d  ISSUES_REVIEW.md`
- `f1b2002cdefa74b9  PROJECT_HANDOVER.md`
- `80874b418154dc56  patrol_runs/2026-10-16_0300.json`
- `59259a428dcaffcd  CLAUDE_AUDIT_2026-09-30.md`
- `c2e67dcc180939fd  CLOUDFLARE_HANDOVER.md`
- `459810f13753aa41  CODEX_TASK_REVIEW_FIXES_2026-09-30.md`

---

## 8. 未完成項目與後續交接

1. `threads:1013.yr_` 經原生 Edge 重試 4 次後仍無法擷取貼文（0 篇貼文），判定為 `failed`，待下一輪排程持續追蹤。
2. 海報未讀貼文共有 21 篇（包含尚和 11/29《西遊記之芭蕉密碼》等），因正文未列完整演出時間與詳細地址，需人工檢視圖檔後再行提案建卡。
