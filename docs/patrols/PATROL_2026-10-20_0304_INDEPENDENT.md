# 2026-10-20 03:04 臺灣戲曲獨立巡檢與發布驗收報告

- **巡檢識別**：`patrol_runs/2026-10-20_0304.json`
- **開始時間**：`2026-10-20T03:04:44+08:00`
- **最後嘗試**：`2026-10-20T03:19:24+08:00`
- **驗收完成**：`2026-10-20T03:28:35+08:00`
- **執行工具**：Antigravity（原生 spawn 無頭 Microsoft Edge、設定檔 `~/.patrol-edge`、Chrome DevTools Protocol (CDP)、文化部原生函式、GitHub CLI）
- **規範依據**：`AGENTS.md`、`PATROL_OPERATIONS.md`

---

## 1. 21 個來源逐一巡檢與存證結果

共巡檢 21 個目標來源，狀態動態計算為：**1 complete、19 partial、1 failed、0 pending**。總狀態依覆蓋率規則忠實判定為 **`failed`**（未達 100% 覆蓋，有 1 個 failed 來源）。

| 來源鍵 | 平台／類型 | 狀態 | 擷取篇數 | 最新／最舊貼文時間 | 重試次數 | 登入牆 | 證據檔案 |
|---|---|---|---|---|---|---|---|
| `threads:joe_huang_k_w` | Threads | partial | 11 篇 | 最新 10/17 18:43、最舊 10/12 12:24 | 0 | 否 | `patrol_evidence/2026-10-20_0304/threads_joe_huang_k_w.json` |
| `threads:h.akito_1996` | Threads | partial | 10 篇 | 最新 10/19 19:06、最舊 09/27 00:04 | 0 | 否 | `patrol_evidence/2026-10-20_0304/threads_h.akito_1996.json` |
| `threads:the_rin.lpm` | Threads | partial | 7 篇 | 最新 10/16 19:11、最舊 09/26 14:32 | 0 | 否 | `patrol_evidence/2026-10-20_0304/threads_the_rin.lpm.json` |
| `threads:1013.yr_` | Threads | failed | 0 篇 | 無 | 3 (共4次) | 否 | `patrol_evidence/2026-10-20_0304/threads_1013.yr_.json` |
| `threads:xuefeng_lu_` | Threads | partial | 8 篇 | 最新 10/17 14:49、最舊 10/03 14:35 | 0 | 否 | `patrol_evidence/2026-10-20_0304/threads_xuefeng_lu_.json` |
| `threads:yuzhongluo` | Threads | partial | 9 篇 | 最新 10/19 11:16、最舊 10/13 01:16 | 0 | 否 | `patrol_evidence/2026-10-20_0304/threads_yuzhongluo.json` |
| `threads:taiwaneseopera168` | Threads | partial | 10 篇 | 最新 10/15 22:26、最舊 10/14 13:09 | 0 | 否 | `patrol_evidence/2026-10-20_0304/threads_taiwaneseopera168.json` |
| `threads:jing__1017` | Threads | partial | 8 篇 | 最新 10/16 00:52、最舊 10/11 22:34 | 0 | 否 | `patrol_evidence/2026-10-20_0304/threads_jing__1017.json` |
| `threads:hilang.on.tour` | Threads | partial | 7 篇 | 最新 10/14 11:25、最舊 10/02 11:07 | 0 | 否 | `patrol_evidence/2026-10-20_0304/threads_hilang.on.tour.json` |
| `threads:yolin1991` | Threads | partial | 7 篇 | 最新 10/19 11:06、最舊 10/09 13:48 | 0 | 否 | `patrol_evidence/2026-10-20_0304/threads_yolin1991.json` |
| `facebook:sunhope.fans` | Facebook | partial | 6 篇 | 時間未辨識 6 篇 | 0 | 否 | `patrol_evidence/2026-10-20_0304/facebook_sunhope.fans.json` |
| `facebook:HsiaoHsiYuan1913` | Facebook | partial | 1 篇 | 時間未辨識 1 篇 | 0 | 否 | `patrol_evidence/2026-10-20_0304/facebook_HsiaoHsiYuan1913.json` |
| `facebook:100063868113954` | Facebook | partial | 12 篇 | 時間未辨識 12 篇 | 0 | 否 | `patrol_evidence/2026-10-20_0304/facebook_100063868113954.json` |
| `facebook:MingHuaYuanTianTaiwaneseOpera` | Facebook | partial | 6 篇 | 時間未辨識 6 篇 | 0 | 否 | `patrol_evidence/2026-10-20_0304/facebook_MingHuaYuanTianTaiwaneseOpera.json` |
| `facebook:61574134933376` | Facebook | partial | 3 篇 | 時間未辨識 3 篇 | 0 | 否 | `patrol_evidence/2026-10-20_0304/facebook_61574134933376.json` |
| `facebook:mhysun` | Facebook | partial | 6 篇 | 時間未辨識 6 篇 | 0 | 否 | `patrol_evidence/2026-10-20_0304/facebook_mhysun.json` |
| `facebook:61594936681482` | Facebook | partial | 1 篇 | 時間未辨識 1 篇 | 0 | 否 | `patrol_evidence/2026-10-20_0304/facebook_61594936681482.json` |
| `facebook:lanyang.opera` | Facebook | partial | 4 篇 | 時間未辨識 4 篇 | 0 | 否 | `patrol_evidence/2026-10-20_0304/facebook_lanyang.opera.json` |
| `facebook:Taichungpuppettheater` | Facebook | partial | 15 篇 | 時間未辨識 15 篇 | 0 | 否 | `patrol_evidence/2026-10-20_0304/facebook_Taichungpuppettheater.json` |
| `culture` | 文化部 | partial | 114 筆 | 候選 3 筆，不在表 3 筆；少於 500 筆門檻，讀取不完整，不可判定無新場次 | 0 | 否 | 原生函式唯讀比對 |
| `issues` | GitHub | complete | 2 筆 | Issues #1、#2 檢核皆為 open，無新留言 | 0 | 否 | GitHub CLI & REST API |

---

## 2. 提到未來演出之貼文逐篇判斷與比對結果

經 `scripts/extract_mentions.py` 自巡檢證據中提取 74 篇演出相關貼文，逐篇核對 `data/schedule.json` 如下：

### 【已在表且一致】

1. **台南古都掌中劇團《台灣風雲錄・戰火波瀾》（苗栗竹南場）**
   - **來源**：`threads:joe_huang_k_w`（https://www.threads.com/@joe_huang_k_w/post/DedaxOSCfHY）、`threads:hilang.on.tour`（https://www.threads.com/@hilang.on.tour/post/DedaYXykx0c）
   - **原文逐字片段**：
     > 「10月30日，邀請你來苗栗竹南運動公園大草坪。 帶著家人朋友，一起坐下來，看看臺灣的故事。 ▍《台灣風雲錄・戰火波瀾》 主演｜台南古都掌中劇團 日期｜2026年10月30日（五） 地點｜苗栗竹南運動公園大草坪 進場｜17:00 開演｜18:00 策劃｜山線百年客家輸出・陳翊綾 各位朋友，竹南見。」
   - **比對狀態**：**已在表且一致**（卡片 ID `amichen-2026-10-30-zhunan-taiwan-fengyunlu`，日期 2026-10-30、時間 17:00 開放進場／18:00 正式開演、地點苗栗縣竹南鎮竹南運動公園）。

2. **明華園天字戲劇團 高雄天保宮外台**
   - **來源**：`facebook:100063868113954`（吳奕萱粉專）
   - **原文逐字片段**：
     > 「天保宮 時間：10/20-10/21 地點：高雄市前鎮區興陽街32巷5號」
   - **比對狀態**：**已在表且一致**（卡片 ID `mhy-tian-2026-10-20-tianbao`，地點已完整記載高雄市前鎮區興陽街32巷5號，貼文未提供開演時間點）。

3. **明華園天字戲劇團 高雄聖母宮外台**
   - **來源**：`facebook:100063868113954`（吳奕萱粉專）
   - **原文逐字片段**：
     > 「鹿耳門高雄聖母宮 時間：10/22 地點：高雄市三民區中道街43號」
   - **比對狀態**：**已在表且一致**（卡片 ID `mhy-tian-2026-10-22-shengmu`，地點已完整記載高雄市三民區中道街43號，貼文未提供開演時間點）。

4. **鶯藝歌劇團 台南南廠武英殿外台**
   - **來源**：`threads:yuzhongluo`（https://www.threads.com/@yuzhongluo/post/DeqRb5qmfdc 等）
   - **原文逐字片段**：
     > 「下一站 農曆9月14、15日~國曆10月23、24日 地點：台南市大智街135號~南廠武英殿 參与母團~鶯藝歌劇團演出 安排好戲登場~歡迎來看戲✌️✌️✌️」
   - **比對狀態**：**已在表且一致**（卡片 ID `luo-2026-10-23-wuyingdian`，地址已具備台南市大智街135號，未列具體劇目與開演時間點）。

5. **秀琴歌劇團 大型公演《玉石變》與《金沙灘》**
   - **來源**：`threads:the_rin.lpm`（https://www.threads.com/@the_rin.lpm/post/DdvZekJE9Mm）
   - **原文逐字片段**：
     > 「📅11/07 19：00 🎭戲碼：《玉石變》📍地點：新莊保元宮 ... 📅11/15 19：00 🎭戲碼：《金沙灘》 📍地點：西港慶安宮」
   - **比對狀態**：**已在表且一致**（卡片 ID `sc-2026-11-07-yushibian` 與 `sc-2026-11-15-jinshatan` 均已完整在庫）。

6. **蘭陽戲劇團《錯配姻緣》**
   - **來源**：`facebook:lanyang.opera`
   - **原文逐字片段**：
     > 「10/26（一）晚上7:00 劇目｜《錯配姻緣》 地點｜桃園顯安巖顯應祖師廟 （桃園市龜山區樂善里樂安街1號） ※免費觀賞」
   - **比對狀態**：**已在表且一致**（卡片 ID `lanyang-2026-10-26-guishan-cuoxie-yinyuan`）。

7. **台中木偶劇團《聖劍風雲三-龍虎兄弟》**
   - **來源**：`facebook:Taichungpuppettheater`
   - **原文逐字片段**：
     > 「日期｜115 / 11 / 7（六） 時間｜14:30 地點｜臺中市屯區藝文中心・實驗劇場」
   - **比對狀態**：**已在表且一致**（卡片 ID `tcpt-2026-11-07-shengjianfengyun-3`）。

8. **明華園戲劇總團《烏龍天下》高雄場**
   - **來源**：`facebook:mhysun`
   - **原文逐字片段**：
     > 「12/19－12/20｜衛武營國家藝術文化中心 10/16 中午12點搶票」
   - **比對狀態**：**已在表且一致**（卡片 ID `mhy-oolong-wv-2026-12-19`）。

9. **尚和歌仔戲劇團【寒窯之外】**
   - **來源**：`facebook:sunhope.fans`
   - **原文逐字片段**：
     > 「演出日期：11/7（六）、11/8（日） OPENTIX 兩廳院售票系統現正熱賣ing」
   - **比對狀態**：**已在表且一致**（卡片 ID `sh-2026-11-07-hanyao-zhiwai`）。

### 【海報未讀 (poster-only) 與線索不足】

- `facebook:HsiaoHsiYuan1913`：貼文為純圖片/海報無內文，列入海報未讀。
- `threads:the_rin.lpm`（`Ddy9Vv8k7IV`）：「先補個劇團新發的戲路表🙌」，貼文僅附戲路表圖片無文字日期地點，列入海報未讀。
- `facebook:Taichungpuppettheater`：貼文提及「11/14（六）戶外演出-《波比大冒險》」，貼文內未公布任何演出地點與時間，線索不足不建卡。
- `threads:the_rin.lpm`（`DejZXiykw3q`）：秀琴歌劇團講座《戲棚下・逐星路》，屬推廣講座非戲曲演出，已於卡片 `lecture-2026-10-24-xipeng-xinglu` 表彰，不另建新卡。

### 【新增、更新卡與拒絕提案統計】

- **新增卡**：無（0 筆）
- **更新卡**：無（0 筆）
- **被拒絕之提案**：無（0 筆，無硬闖或被拒提案）

---

## 3. 文化部開放資料比對

- **呼叫函式**：唯讀匯入 `updater.fetch_culture_events()` 與 `updater.culture_candidates()`。
- **回傳筆數**：總筆數 114 筆（少於 500 筆門檻，依規約記為 `partial`，並記錄「讀取不完整，不可判定無新場次」）。
- **篩選候選**：3 筆。
- **不在表比對與處置**：
  1. `登出世界、登入自我！《虛。實─數位與我》插畫創作聯展`：非戲曲演出（為插畫創作聯展），不建卡。
  2. `登出世界、登入自我！《虛。實─數位與我》插畫創作聯展`（同名場次）：非戲曲演出，不建卡。
  3. `登出世界、登入自我！《虛。實─數位與我》插畫創作聯展`（同名場次）：非戲曲演出，不建卡。

---

## 4. 發布與公開驗收結果

- **資料提交 SHA**：[`790763e5bd978b55b7287b5a4dfb4a5e7863380c`](https://github.com/eric1810-tw/taiwan-opera-calendar/commit/790763e5bd978b55b7287b5a4dfb4a5e7863380c)
- **GitHub Actions Run**：[Run ID 39311117711](https://github.com/eric1810-tw/taiwan-opera-calendar/actions/runs/39311117711)（push / success）
- **公開驗收指令**：`python3 scripts/patrol_progress.py verify --run patrol_runs/2026-10-20_0304.json --sha 790763e5bd978b55b7287b5a4dfb4a5e7863380c --actions-run 39311117711`
- **驗收狀態**：`publication.state = "verified"`
- **公開檔案一致性**（`python3 scripts/patrol_progress.py compare-public`）：
  - `data/schedule.json`: `7941aba066a0cff3d5d329d80a67d4bb763bf37a24dc848891e229254d29175a`（逐位元一致）
  - `data/patrol_status.json`: `a486d2da2c8c0138799e6a2b46098f94a16b04b416e251fd82293918d311b567`（逐位元一致）
  - `data/metadata.json`: `6b3cf329b4caff249b52fc45127b200605791124f36a66e29b3e04e485040d1b`（逐位元一致）

---

## 5. 未完成項目與後續交接

1. `threads:1013.yr_`：經 4 次有界重試（重新載入、等待 30 秒、等待 60 秒開個人頁）皆擷取 0 篇，記為 `failed`。後續排程輪次可由不同網路路徑接續。
2. 社群圖片：目前全數社群媒體記為 `unread`，維持 `partial` 狀態。
3. 文化部 API：本輪回傳筆數 114 筆未達門檻，記為 `partial`，不可判定無新場次，待後續輪次文化部資料源恢復完整筆數時再次檢視。
