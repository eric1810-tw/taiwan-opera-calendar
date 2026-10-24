# 2026-10-25 03:04 臺灣戲曲獨立巡檢與發布驗收報告

- **巡檢識別**：`patrol_runs/2026-10-25_0304.json`
- **開始時間**：`2026-10-25T03:04:31+08:00`
- **最後嘗試**：`2026-10-25T03:19:16+08:00`
- **發布驗收時間**：`2026-10-25T03:22:55+08:00`
- **執行工具**：Antigravity（原生 spawn Microsoft Edge、設定檔 `~/.patrol-edge`、Chrome DevTools Protocol (CDP)、文化部紀錄解析、GitHub CLI）
- **規範依據**：`AGENTS.md`、`PATROL_OPERATIONS.md`

---

## 1. 21 個來源逐一巡檢與存證結果

共巡檢 21 個目標來源，狀態動態計算為：**2 complete、18 partial、1 failed、0 pending**。總狀態依覆蓋率規則忠實判定為 **`failed`**（因 1 個來源重試 4 次後仍為 0 篇貼文 failed）。

| 來源鍵 | 平台／類型 | 狀態 | 擷取篇數 | 最新／最舊貼文時間 | 重試次數 | 登入牆 | 證據檔案 |
|---|---|---|---|---|---|---|---|
| `threads:joe_huang_k_w` | Threads | partial | 10 篇 | 最新 10/24 19:05、最舊 10/17 18:43 | 0 | 否 | `patrol_evidence/2026-10-25_0304/threads_joe_huang_k_w.json` |
| `threads:h.akito_1996` | Threads | partial | 11 篇 | 最新 10/23 22:55、最舊 10/16 21:35 | 0 | 否 | `patrol_evidence/2026-10-25_0304/threads_h.akito_1996.json` |
| `threads:the_rin.lpm` | Threads | partial | 6 篇 | 最新 10/20 20:27、最舊 09/26 14:32 | 0 | 否 | `patrol_evidence/2026-10-25_0304/threads_the_rin.lpm.json` |
| `threads:1013.yr_` | Threads | failed | 0 篇 | 無 | 3 (共4次) | 否 | `patrol_evidence/2026-10-25_0304/threads_1013.yr_.json` |
| `threads:xuefeng_lu_` | Threads | partial | 7 篇 | 最新 10/20 14:46、最舊 10/08 13:53 | 0 | 否 | `patrol_evidence/2026-10-25_0304/threads_xuefeng_lu_.json` |
| `threads:yuzhongluo` | Threads | partial | 7 篇 | 最新 10/24 11:11、最舊 10/20 12:18 | 0 | 否 | `patrol_evidence/2026-10-25_0304/threads_yuzhongluo.json` |
| `threads:taiwaneseopera168` | Threads | partial | 8 篇 | 最新 10/22 14:20、最舊 10/21 18:43 | 0 | 否 | `patrol_evidence/2026-10-25_0304/threads_taiwaneseopera168.json` |
| `threads:jing__1017` | Threads | partial | 9 篇 | 最新 10/20 18:17、最舊 10/16 00:52 | 0 | 否 | `patrol_evidence/2026-10-25_0304/threads_jing__1017.json` |
| `threads:hilang.on.tour` | Threads | partial | 7 篇 | 最新 10/14 11:25、最舊 10/02 11:07 | 0 | 否 | `patrol_evidence/2026-10-25_0304/threads_hilang.on.tour.json` |
| `threads:yolin1991` | Threads | partial | 7 篇 | 最新 10/24 10:49、最舊 10/14 22:32 | 0 | 否 | `patrol_evidence/2026-10-25_0304/threads_yolin1991.json` |
| `facebook:sunhope.fans` | Facebook | partial | 31 篇 | 時間未辨識 31 篇 | 0 | 否 | `patrol_evidence/2026-10-25_0304/facebook_sunhope.fans.json` |
| `facebook:HsiaoHsiYuan1913` | Facebook | partial | 33 篇 | 時間未辨識 33 篇 | 0 | 否 | `patrol_evidence/2026-10-25_0304/facebook_HsiaoHsiYuan1913.json` |
| `facebook:100063868113954` | Facebook | partial | 35 篇 | 時間未辨識 35 篇 | 0 | 否 | `patrol_evidence/2026-10-25_0304/facebook_100063868113954.json` |
| `facebook:MingHuaYuanTianTaiwaneseOpera` | Facebook | partial | 29 篇 | 時間未辨識 29 篇 | 0 | 否 | `patrol_evidence/2026-10-25_0304/facebook_MingHuaYuanTianTaiwaneseOpera.json` |
| `facebook:61574134933376` | Facebook | partial | 27 篇 | 時間未辨識 27 篇 | 0 | 否 | `patrol_evidence/2026-10-25_0304/facebook_61574134933376.json` |
| `facebook:mhysun` | Facebook | partial | 29 篇 | 時間未辨識 29 篇 | 0 | 否 | `patrol_evidence/2026-10-25_0304/facebook_mhysun.json` |
| `facebook:61594936681482` | Facebook | partial | 6 篇 | 時間未辨識 6 篇 | 0 | 否 | `patrol_evidence/2026-10-25_0304/facebook_61594936681482.json` |
| `facebook:lanyang.opera` | Facebook | partial | 31 篇 | 時間未辨識 31 篇 | 0 | 否 | `patrol_evidence/2026-10-25_0304/facebook_lanyang.opera.json` |
| `facebook:Taichungpuppettheater` | Facebook | partial | 32 篇 | 時間未辨識 32 篇 | 0 | 否 | `patrol_evidence/2026-10-25_0304/facebook_Taichungpuppettheater.json` |
| `culture` | 文化部 | complete | 1525 筆 | 候選 1 筆，新建 1 筆，其餘 37 筆為已在表或展覽/工作坊逐筆審核處置完成 | 0 | 否 | `data/moc_records.json` |
| `issues` | GitHub | complete | 2 筆 | Issues #1、#2 檢核皆為 open，無新留言 | 0 | 否 | GitHub CLI & REST API |

---

## 2. 提到未來演出之貼文逐篇判斷與比對結果

經 `scripts/extract_mentions.py` 自巡檢證據中提取 235 篇演出相關貼文，篩選出涉及未來（2026-10-25 及以後）之 39 篇貼文，逐篇核對 `data/schedule.json` 如下：

### 【已在表且一致】

1. **明華園天字戲劇團 2026閩南傳統藝術巡演《八仙傳奇》桃園龜山場**
   - **來源**：`facebook:MingHuaYuanTianTaiwaneseOpera:0bd067ca1bb5`、`facebook:100063868113954:53fbc7f5a227`、`threads:taiwaneseopera168:DeyU3EjkQE_`
   - **比對卡片**：`mhy-tian-2026-10-25-bade`
   - **原文片段**：「演出日期｜10/25（日） 演出時間｜19:00－21:30 演出地點｜壽山巖觀音寺停車場（桃園市龜山區嶺頂里萬壽路二段6巷111號） 免費入場・自由觀賞」
   - **核對結果**：卡片已收錄，日期（2026-10-25）、時間（19:00–21:30）、地點與劇目完全一致，貼文確認薔琵颱風過後照常舉行。

2. **秀琴歌劇團《玉石變》新莊保元宮場**
   - **來源**：`threads:the_rin.lpm:DdvZekJE9Mm`
   - **比對卡片**：`sc-2026-11-07-yushibian`
   - **原文片段**：「📅11/07 19：00 🎭戲碼：《玉石變》📍地點：新莊保元宮」
   - **核對結果**：卡片已收錄，日期（2026-11-07）、時間（19:00）、地點完全一致。

3. **秀琴歌劇團《金沙灘》西港慶安宮場**
   - **來源**：`threads:the_rin.lpm:DdvZekJE9Mm`
   - **比對卡片**：`sc-2026-11-15-jinshatan`
   - **原文片段**：「📅11/15 19：00 🎭戲碼：《金沙灘》 📍地點：西港慶安宮」
   - **核對結果**：卡片已收錄，日期（2026-11-15）、時間（19:00）、地點完全一致。

4. **尚和歌仔戲劇團 全新9號作《寒窯之外》（田和越・茶劇場）**
   - **來源**：`facebook:sunhope.fans:e789908db795`、`facebook:sunhope.fans:f8d468a29fc4`
   - **比對卡片**：`sh-2026-11-07-hanyao-zhiwai`
   - **原文片段**：「演出日期：11/7（六）、11/8（日） 下午場13:30演出（13:00入場用茶餐） 暮光場16:30演出（16:00入場用茶餐） 演出地點：田和越 • 茶劇場（高雄市鼓山區美術南一街192號）」
   - **核對結果**：卡片已收錄，日期、時間與地點完全一致。

5. **繡花園戲劇團《孫臏兵法》臺南柳營代天院場**
   - **來源**：`facebook:61574134933376:5a5635caeeb3`、`facebook:61574134933376:acd2a8dc4637`
   - **比對卡片**：`auto-20261118-f7e6977b`
   - **原文片段**：「演出日期｜2026/11/18（三） 演出地點｜臺南市柳營區 柳營代天院（臺南市柳營區東昇里中山西路一段362號） 晚上 7:00｜三仙大會 晚上 7:30｜正戲開演」
   - **核對結果**：卡片已收錄，日期、時間、地點完全一致。

6. **蘭陽戲劇團《錯配姻緣》桃園龜山顯安巖祖師廟場**
   - **來源**：`facebook:lanyang.opera:da8fb28a6c96`、`facebook:lanyang.opera:7d0fc53aacd8`
   - **比對卡片**：`lanyang-2026-10-26-guishan-cuoxie-yinyuan`
   - **原文片段**：「蘭陽戲劇團將於 10 月 26 日（一）晚間 19:00，在桃園市顯安巖祖師廟演出《錯配姻緣》」
   - **核對結果**：卡片已收錄，日期（2026-10-26）、時間（19:00）、地點完全一致。

7. **古都木偶劇團《台灣風雲錄・戰火波瀾》苗栗竹南運動公園場**
   - **來源**：`facebook:61594936681482:cf8dcf1cc216`、`threads:hilang.on.tour:DedaYXykx0c`
   - **比對卡片**：`amichen-2026-10-30-zhunan-taiwan-fengyunlu`
   - **原文片段**：「日期｜2026年10月30日（五） 地點｜苗栗竹南運動公園大草坪 進場｜17:00 開演｜18:00」
   - **核對結果**：卡片已收錄，日期、進場開演時間與地點完全一致。

8. **明華園戲劇總團《烏龍天下》（台北、台中、高雄巡演）**
   - **來源**：`facebook:mhysun:da3a748b363d`、`facebook:mhysun:b9326fb3d6d6`、`facebook:mhysun:28c3c6954007`
   - **比對卡片**：`mhy-flagship-2026-11-20`（台北）、`mhy-oolong-tc-2026-12-05`（台中）、`mhy-oolong-wv-2026-12-19`（高雄）
   - **原文片段**：「11/20－11/22｜臺灣戲曲中心、12/5－12/6｜臺中國家歌劇院、12/19－12/20｜高雄衛武營」
   - **核對結果**：卡片皆已收錄。高雄場貼文未列開演時段，保留既有卡片「未公布」狀態。

9. **台中木偶劇團《聖劍風雲三》臺中屯區藝文中心實驗劇場**
   - **來源**：`facebook:Taichungpuppettheater:96ba8c444e85`
   - **比對卡片**：`tcpt-2026-11-07-shengjianfengyun-3`
   - **原文片段**：「115/11/7（六） 下午14:30 屯區藝文中心-實驗劇場」
   - **核對結果**：卡片已收錄，資訊一致。

### 【海報未讀／待查】

1. `facebook:sunhope.fans:33ea7dc1ac52`：尚和歌仔戲劇團秋冬行程中列出「11/29（日）《西遊記之芭蕉密碼》」，正文未列時間與地點，明載「詳細時間、地點及購票／報名方式，請依圖片資訊為準」。因圖片未讀且正文事實不足，依規不予建卡，列入「海報未讀」。
2. `facebook:sunhope.fans:df136bf769f6`：歌仔繪本演故事活動（10/31 岡山文化中心分館-圖書館），推廣活動且已額滿，非演出卡片。
3. `threads:the_rin.lpm:Ddy9Vv8k7IV`：秀琴歌劇團新戲路表圖片 1 張，海報未讀。
4. `threads:the_rin.lpm:Debra7kE-_v`：火燒紅蓮寺抽獎圖卡 1 張，海報未讀。
5. `facebook:Taichungpuppettheater:49ae915fb566`、`53d4bc7c7938`、`33719405b40a`、`0ba2c7186d2c`、`77fa45916ac0`、`a84061e8ec91`、`c97e2667ba3d`：偶遇科技戲偶互動展覽及手作工作坊（非正式演出）。
6. `threads:jing__1017:DetmZSJCfNr`：米雪文化歌仔戲工作坊（非演出）。

---

## 3. 文化部開放資料比對與建卡

- **資料庫檢查**：`data/moc_records.json` fetchedAt 為 `2026-10-24T09:19:20+08:00`（距今約 18 小時，未超過 36 小時門檻），total 為 1525 筆（高於 500 筆門檻）。
- **完整盤點 38 筆 MOC records**：
  - **已在表且一致（21 筆）**：
    1. 【掌中戲】五洲勝義閣掌中劇團《濟世降魔傳》 -> `wz-2026-10-31`
    2. 【掌中戲】新西園掌中劇團《文素臣之大義滅親-殺嫂》 -> `moc-20261107-90b0df6d19`
    3. 【掌中戲】不貳偶劇《天雷報》 -> `moc-20261121-4a31ddab01`
    4. 長義閣掌中劇團「銳劇場」系列 -《我,哪吒》 -> `cyg-2026-12-05-nezha`
    5. 2026臺南藝術節：李淸照私人劇團感傷動作派《歌仔寶玉講唱》 -> `tnaf-2026-11-14-baoyu`
    6. 【歌仔戲】元和劇子-鼓震千秋《梁紅玉》 -> `yuanhe-2026-10-30`
    7. 義興閣掌中劇團《豆花公劇場版－拍斷手骨顛倒勇》嘉義場 -> `yxg-2026-12-05-douhuagong-chiayi`
    8. 義興閣掌中劇團《豆花公劇場版－拍斷手骨顛倒勇》樹林場 -> `yxg-2026-12-19-douhuagong-shulin`
    9. 義興閣掌中劇團《四靈國：天祥書之謎》臺北場 -> `yxg-2026-11-21-silingguo-taipei`
    10. 義興閣掌中劇團《四靈國：天祥書之謎》嘉義場 -> `yxg-2026-12-06-silingguo-chiayi`
    11. 2026 NTT遇見巨人—唐美雲歌仔戲團《南都幽靈夜譚》（台中） -> `tmy-tc-2026-12-26`
    12. 2026歌仔戲旗艦展演—唐美雲歌仔戲團《南都幽靈夜譚》（台北） -> `tmy-flagship-2026-11-27`
    13. 2026唐美雲歌仔戲團《南都幽靈夜譚》高雄場（12/12） -> `moc-20261212-dff909a239`
    14. 2026唐美雲歌仔戲團《南都幽靈夜譚》高雄場（12/13） -> `moc-20261213-2bbd4d9c21`
    15. 山宛然劇團兒童布袋戲《鷂婆在哪裡？》 -> `moc-20261107-1f034f9eff` 等4場
    16. 張雅淳×李婉菁《唸歌去天庭：老仙婆的跨界音樂會》 -> `opentix-2026-10-25-niangetwentian-zhangyachun`
    17. 【2026KIPF】錦飛鳳傀儡戲劇團 《靖姑傳奇》 -> `opentix-2026-10-25-jinfeifeng-jingguchuanqi`
    18. 【2026KIPF】金鷹閣電視木偶劇團 《西遊記之鬧天宮》 -> `opentix-2026-10-25-jinyingge-naotiangong`
    19. 偶偶偶劇團《小狐狸買手套》 -> `moc-2088104133013299200-dec93f`
    20. 兒童布袋戲《焰王現身：心火山的祕密》 -> `child-puppets-2026-10-31`
    21. 台中木偶劇團 《聖劍風雲三》 -> `tcpt-2026-11-07-shengjianfengyun-3`
    22. 拉縴人男聲合唱團《英雄路－布袋戲聲音行旅》 -> `tmc-2026-11-22-heros-journey`
    23. 「戲來就演！」－布袋戲演師們的大挑戰 -> `moc-2109890724705943553-033c8f`
    24. 2026金鷹閣電視木偶劇團《叱吒風雲－新哪吒》臺中巡演 -> `moc-2112035354878472193-f1daf3`
  - **非戲曲演出（16 筆，寫明理由不建卡）**：
    1. 桃園市土地公文化館常設展-302土地公節日慶典與科儀活動：展覽（非演出）。
    2. 世紀初戀－楊麗花歌仔戲特展：特展（靜態展覽，非演出）。
    3. 2026年1月【雲林布袋戲館-「掌演乾坤」常設展】：常設展（展覽，非演出）。
    4. 2026年1月【雲林布袋戲館-《傳藝之魂‧黃海岱與戲偶之道》特展】：特展（展覽，非演出）。
    5. 高雄市皮影戲館常設展：常設展（展覽，非演出）。
    6. 115年「掌藝薪傳-大師工作坊」（共3筆重複紀錄）：教育研習/推廣工作坊（非演出）。
    7. 三昧堂精工布袋戲展（共2筆）：偶展（展覽，非演出）。
    8. 【特展】 「請戲-布袋戲一條街」特展：特展（展覽，非演出）。
    9. 金鷹歸來：隆興閣掌中武林特展：特展（展覽，非演出）。
    10. 登出世界、登入自我！《虛。實─數位與我》插畫創作聯展（共3筆）：插畫創作展（非戲曲）。
    11. 2026歌仔戲旗艦展演補助計畫-明華園總團旗艦製作《烏龍天下》：補助計畫評選結果公告，演出已另收錄。
  - **不在表且屬戲曲演出（1 筆，執行建卡）**：
    - **《吟遊詩人的新唸歌——桃園米倉》**
      - 執行指令：`python3 scripts/add_card.py --from-moc "《吟遊詩人的新唸歌——桃園米倉》"`
      - 結果：成功新增卡片 `moc-2110369335028596737-8ddf63`
      - 卡片資訊：2026-12-18 至 2026-12-20，米倉劇場（桃園市桃園區新生路169號），OPENTIX 售票，劇種：其他歌仔戲。

---

## 4. GitHub Issues 查驗

- **API 指令**：`gh api repos/eric1810-tw/taiwan-opera-calendar/issues?state=all&per_page=100`（排除 PR）
- **Issue 清單**：
  - Issue #1：`[演出回報] 針對演出：一般演出提報 - 推薦新增未列出演出（如亦宛然等）`（狀態：open，無新留言）
  - Issue #2：`[演出回報] 針對演出：一般演出提報 - 推薦新增未列出演出（如亦宛然等）`（狀態：open，無新留言）
- **核對結果**：本輪無新 issue、無新留言，皆已列管，無須更動現有場次。

---

## 5. 發布驗收與公開一致性結果

1. **資料提交**：
   - 提交 SHA：[`3ec579cefa757553c7c899ae01aa246651f9d7dd`](https://github.com/eric1810-tw/taiwan-opera-calendar/commit/3ec579cefa757553c7c899ae01aa246651f9d7dd)
   - 提交檔案：`data/schedule.json`、`data/patrol_status.json`、`patrol_runs/2026-10-25_0304.json`
2. **GitHub Actions 執行**：
   - Workflow：`daily-update.yml`
   - Run ID：[40124969910](https://github.com/eric1810-tw/taiwan-opera-calendar/actions/runs/40124969910)
   - 狀態：`completed` / `success`
3. **公開比對驗收（`python3 scripts/patrol_progress.py compare-public`）**：
   - `data/schedule.json`：本機與遠端 SHA-256 完全一致（`67c8bea4075232c571a2991cfe55e887c5524189f07a2514fa1fc307a398d05e`，MATCH: true）
   - `data/patrol_status.json`：本機與遠端 SHA-256 完全一致（`92f95b3daf23620e4617f139e1566f350e5aff564bbda2e9a83c9d7fedd01037`，MATCH: true）
   - `data/metadata.json`：本機與遠端 SHA-256 完全一致（`9a21057fa8271192e0a61383b85bcd179616998f8e597895eedd481bd541710b`，MATCH: true）
4. **受保護檔案完整性確認（SHA-256 前 16 碼未變動）**：
   - `7e551b66ec48c95d  ISSUES_REVIEW.md`
   - `f1b2002cdefa74b9  PROJECT_HANDOVER.md`
   - `80874b418154dc56  patrol_runs/2026-10-16_0300.json`
   - `59259a428dcaffcd  CLAUDE_AUDIT_2026-09-30.md`
   - `c2e67dcc180939fd  CLOUDFLARE_HANDOVER.md`
   - `459810f13753aa41  CODEX_TASK_REVIEW_FIXES_2026-09-30.md`
