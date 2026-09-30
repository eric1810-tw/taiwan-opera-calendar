# 台灣傳統戲曲演出行事曆（Taiwan Opera Calendar）
# Codex 系統審核與初步修訂工作交接規格書（Handover & Audit Specification）

> **交接文件版本**：v1.2.0  
> **交接日期**：2026-09-26  
> **專案儲存庫**：[https://github.com/eric1810-tw/taiwan-opera-calendar](https://github.com/eric1810-tw/taiwan-opera-calendar)  
> **線上即時展示**：[https://eric1810-tw.github.io/taiwan-opera-calendar/](https://eric1810-tw.github.io/taiwan-opera-calendar/)  
> **本地工作目錄**：`/Users/eric/.gemini/antigravity/scratch/taiwan-opera-calendar`  

---

## 壹、專案背景與業務目標

本專案旨在提供全國最即時、完整且經過核實的**台灣傳統戲曲（歌仔戲、布袋戲）未來 90 天（2026 年 10 月至 12 月底）演出行事曆**。

### 核心關注團隊與焦點卡司
1. **歌仔戲焦點名家**：
   * **吳奕萱**（明華園天字戲劇團新生代當家小生，在鍘美藝術節壓軸跨刀飾演「周阿司」爆紅）
   * **呂雪鳳**（金馬獎最佳女配角、歌仔戲資深名旦名丑，唱活戲即興泰斗）
   * **孫凱琳**（傳藝金曲獎最佳青年演員，春美歌劇團／孫凱琳歌劇團主演與導演）
   * **郭春美**（春美歌劇團團長、國寶天王小生）
   * **張秀琴 & 莊金梅**（秀琴歌劇團「歌仔戲皇帝」與「苦旦天后」）
   * **羅裕誴**（羅裕誴歌劇團／四代傳承鶯藝歌劇團團長，文武兼備小生）
   * **唐美雲**（唐美雲歌仔戲團創辦人、國家文藝獎得主）
   * **明華園家族**（包含明華園戲劇總團之孫翠鳳旗艦大戲、明華園天字戲劇團等）
2. **布袋戲焦點名家**：
   * **古都木偶戲劇團**（黃冠維團長領銜，鍘美藝術節首日以《包公斬駙馬》引爆話題）
   * **亦宛然掌中劇團**（人間國寶李天祿傳承，台北大稻埕曲藝場 10/17 等售票公演）
   * **霹靂國際多媒體**（布袋戲音樂盛會、經典偶尊跨界公演）
   * **不貳偶劇**（傳藝金獎郭建甫當代掌中大戲《戲頭 2》）
   * **五洲勝義閣掌中劇團**（五洲派傳統金光布袋戲）
3. **其他國家級與優秀團隊**：
   * 財團法人廖瓊枝歌仔戲文教基金會、薪傳歌仔戲劇團、一心戲劇團、鴻明歌劇團等。

---

## 貳、目前技術架構與檔案清單

系統採用輕量化、免伺服器（Serverless）架構，結合 **靜態前台（JAMstack）+ Python 自動排程腳本 + GitHub Actions CI/CD + GitHub Pages 免費代管**。

```
taiwan-opera-calendar/
├── .github/
│   └── workflows/
│       └── daily-update.yml       # 每天台灣時間 07:00 (UTC 23:00) 自動更新並部署
├── data/
│   └── schedule.json              # 結構化演出資料庫 (唯一真相來源 Single Source of Truth)
├── index.html                     # Mobile-First 響應式單頁應用 (UI 展示與動態 fetch)
├── updater.py                     # 每日排程更新、天數計算與資料核實腳本
├── README.md                      # 專案公開說明文件
└── CODEX_HANDOVER_AND_AUDIT_SPEC.md # 本份 Codex 審核與工作交接規格書
```

### 各模組實作現況：
1. **`index.html`**：
   * **版面設計**：以手機優先（Mobile-First，最佳化視寬 375px ~ 430px），雙側設有原創純 CSS 戲院絳紅天鵝絨帷幔（仿傳統戲台深紅視覺，絕無版權侵權疑慮）。
   * **主題系統**：內建 3 款即時切換主題：
     1. `crimson-classic`：經典戲台絳紅金殿（預設・鍘美紅海報色系・象牙宣紙底）
     2. `purple-regal`：新古典宮廷絳紫金繡（夜間高對比・大劇院 VIP 包廂感）
     3. `literati-ink`：典雅文人宣紙墨金（素雅水墨留白・文青展冊風格）
   * **動態加載**：透過 `fetch('./data/schedule.json')` 於用戶端動態渲染，**完全與後端字串操作解耦**。
2. **`data/schedule.json`**：
   * 目前收錄 22 場未來 90 天完整核實演出，包含：
     * `id`, `date`, `dateFormatted`, `daysAway`（剩餘天數）, `time`
     * `troupe`（劇團）, `genre`（類別）, `artist`（主演卡司）, `title`（劇碼）
     * `category`（性質）, `badgeType`（ticket/free/temple/plan）
     * `verifyStatus`（verified/community/pending）, `verifyLabel`
     * `location`, `region`, `status`, `description`
     * `link`（官方購票/詳情直達）, `tags`
3. **`updater.py`**：
   * 專職資料層邏輯，自動計算相對於今日的 `daysAway` 倒數天數。
   * **架構鐵律**：僅對 `data/schedule.json` 進行讀寫，**嚴禁修改或字串覆寫 `index.html`**（徹底防堵過去字串截斷導致網頁重複貼上的重大 Bug）。
4. **`.github/workflows/daily-update.yml`**：
   * 排程：`cron: '0 23 * * *'`（台灣時間每天早上 07:00）。
   * 權限：`contents: write`, `pages: write`, `id-token: write`。
   * 步驟：Checkout -> Python 3.11 -> Run updater.py -> Git commit & push (若有異動) -> Deploy to GitHub Pages。

---

## 參、已確認之重要業務約束（Critical Business Constraints）

**Codex 在審核與修訂時，必須絕對遵守以下規則，切勿任意更動：**

1. ⚠️ **快速篩選按鈕順序必須嚴格保持**：
   按鈕在手機端採 **3 行對齊排列（每行 4 顆，共 12 顆）**，次序不可打亂：
   ```
   [全部]       [🎭 古都木偶]  [⚔️ 羅裕誴]    [✨ 孫凱琳]
   [🤣 吳奕萱]   [👑 呂雪鳳]   [🌸 春美]      [🏮 秀琴]
   [👑 唐美雲]   [⭐ 明華園]   [🎪 其他歌仔]  [🪵 其他布袋]
   ```
2. ⚠️ **搜尋輸入框已依需求廢除**：
   搜尋框佔用手機垂直空間且操作繁瑣，已全數以 3 行快速標籤取代，**不可將搜尋框加回**。
3. ⚠️ **嚴禁出現「蹭熱度」的宣傳字眼**：
   頂部大標題必須保持大氣中立之 **「台灣傳統戲曲演出行事曆」**，不得在 Header 或標章處標記「🏮 鍘美藝術節後續・戲曲文藝復興」等字樣，以維持公信力並避免公關風險。
4. ⚠️ **審核機制提示列必須維持在版面下方**：
   「資料核實機制」與「回報或推薦場次」區塊必須維持在卡片流下方近 Footer 處，不得放回頂端佔用手機首屏高度。
5. ⚠️ **雙來源審核標章機制（Verification Badges）**：
   * `🛡️ 官方認證`（verified）：來自兩廳院 OPENTIX、文化部、文化局官方售票或正式公告。
   * `📣 官方粉專動態`（community）：來自劇團官方 Facebook 粉絲團、痞客邦戲路。
   * `⏳ 籌劃洽詢中`（pending）：主辦場地洽談中，標註提醒留意官方異動。

---

## 肆、交接給 Codex 之審核與修訂任務清單（Action Items for Codex）

請 Codex 針對以下四個面向進行深度審核（Code Review & Quality Audit），並進行初步修訂：

### 任務一：資料完整性與自動排程抓取邏輯強化（Data Integrity & Scraper Robustness）
* [ ] **缺失檢查**：
  * 目前已補入 10/17 亦宛然《續小五義之朝天嶺》，請進一步核實全國各縣市文化中心（如衛武營、大東文化藝術中心、台南文化中心）於 2026/10 ～ 2026/12 是否有其他漏列的立案劇團公演。
* [ ] **`updater.py` 增強**：
  * 目前腳本僅做本地日期與倒數天數計算，需實作具備容錯處理（Exception Handling、Retry、Timeout）的外部爬蟲模組，對接：
    1. OPENTIX 公開搜尋 API（檢索「歌仔戲」、「布袋戲」關鍵字）。
    2. 文化部全國藝文活動資訊整合平台（Open Data JSON API）。
  * 引入資料模型驗證（如標準 JSON Schema 驗證），確保抓取資料寫入 `data/schedule.json` 前必備欄位齊全，防止髒資料破壞前端渲染。

### 任務二：Mobile-First 前端使用者體驗與極端視窗審核（UI/UX Audit）
* [ ] **安全區域相容（iOS Notch / Home Indicator）**：
  * 審核 `viewport-fit=cover` 與 `padding-bottom: env(safe-area-inset-bottom)` 設定，確保 iPhone 與全面屏 Android 底部 Footer 及按鈕不會被虛擬按鍵或黑條遮擋。
* [ ] **按鈕在極窄小螢幕（如 320px、360px）之自適應表現**：
  * 審核 3 行 4 列按鈕在小螢幕上是否有文字溢出或文字折行問題。建議文字使用 `truncate` 或於極小螢幕微調字級（`text-[10px]`）。
* [ ] **主題切換記憶（Local Storage Persistence）**：
  * 目前點選主題切換按鈕後，刷新網頁會回到預設。請實作 `localStorage.setItem('opera-theme', themeName)`，讓使用者選取的主題風格能夠被長期記住。

### 任務三：離線降級與異常處理審核（Fault Tolerance & Offline Fallback）
* [ ] **Fetch 異常降級機制**：
  * 當用戶處於飛航模式、網路斷線，或直接於本地以 `file://` 協議雙擊開啟 `index.html` 時，`fetch('./data/schedule.json')` 會拋出網路或 CORS 錯誤。
  * 請審核並補強降級方案：若 Fetch 失敗，自動啟用內置快取的備用資料或顯示優雅的離線重試（Offline Retry）畫面。

### 任務四：CI/CD 與自動化部署維護（GitHub Actions Audit）
* [ ] **Node.js 執行期棄用警告處理**：
  * GitHub Actions 日誌中出現 `Node.js 20 is deprecated... forced to run on Node.js 24` 與 `ubuntu-latest migration` 提示。
  * 請更新 `.github/workflows/daily-update.yml` 中的 action 版本（如 `actions/checkout@v4`, `actions/setup-python@v5`, `actions/deploy-pages@v4`），確保符合 2026/2027 年長久穩定運行的 CI 標準。

---

## 伍、驗收標準（Acceptance Criteria）

Codex 在完成審核與修訂後，交付成果須滿足以下條件：

1. **功能無損**：
   * 12 顆快篩按鈕功能運作精確無誤，順序保持一致。
   * 點選「明華園」可正確篩選天字團與總團；點選「其他布袋」可正確列出亦宛然、霹靂、不貳偶劇、五洲勝義閣等。
2. **零重複渲染**：
   * 頁面自頂端至底部僅有單一完整介面，無任何重複拼接現象。
3. **通過本機與線上部署測試**：
   * 執行 `python3 updater.py` 退出碼為 `0`。
   * 程式碼推送到 `main` 分支後，GitHub Actions 流程（`update-schedule` 與 `deploy`）均亮綠燈。
   * 線上網址 [https://eric1810-tw.github.io/taiwan-opera-calendar/](https://eric1810-tw.github.io/taiwan-opera-calendar/) 載入流暢無報錯。

---

## 陸、快速啟動與開發指令指引

```bash
# 1. 進入專案目錄
cd /Users/eric/.gemini/antigravity/scratch/taiwan-opera-calendar

# 2. 檢視最新代碼與提交紀錄
git status
git log -n 5 --oneline

# 3. 測試執行更新腳本
python3 updater.py

# 4. 本地啟動預覽測試
python3 -m http.server 8000
# 瀏覽器訪問 http://localhost:8000

# 5. 提交與推送
git add .
git commit -m "refactor(codex): 完成系統架構審核與初步修訂"
git push origin main

# 6. 觸發 GitHub Actions 部署並監控
gh workflow run "Daily Opera Schedule Auto-Updater"
gh run list --workflow="daily-update.yml" -n 1
```

---
*規格書完畢，請 Codex 遵照此指引進行逐項審核、修訂與驗證。*
