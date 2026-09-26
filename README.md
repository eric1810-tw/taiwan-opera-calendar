# 台灣傳統戲曲演出行事曆（鍘美藝術節後續追劇指南）

> 追蹤古都木偶、羅裕誴、孫凱琳、春美歌劇團、秀琴歌劇團、明華園天字團、吳奕萱、唐美雲歌仔戲團未來一個月的精彩演出！

## 專案結構
- `index.html`：現代化、響應式戲曲行事曆互動網頁（支援劇團/演員標籤篩選、區域過濾、關鍵字即時搜尋、官方售票與粉專連結）。
- `data/schedule.json`：結構化演出資料庫。
- `updater.py`：每日定時更新爬蟲與資料同步腳本。
- `.github/workflows/daily-update.yml`：GitHub Actions 每日排程自動部署工作流。

## 如何直接開啟預覽
在 Mac 終端機執行：
```bash
open index.html
```
或使用任何靜態伺服器（例如 `python -m http.server 8000`）。

## 如何啟用「每天自動更新」發布成免費公開網站
1. 在 GitHub 上建立一個新的 Public 儲存庫（例如 `taiwan-opera-calendar`）。
2. 將本資料夾推送到 GitHub：
   ```bash
   git init
   git add .
   git commit -m "feat: 初版台灣傳統戲曲行事曆"
   git branch -M main
   git remote add origin https://github.com/<你的帳號>/taiwan-opera-calendar.git
   git push -u origin main
   ```
3. 到 GitHub 專案的 **Settings** -> **Pages**，將 Build and deployment 的 Source 設定為 **GitHub Actions**。
4. 完成！系統每天台灣時間上午 7:00 會自動運行 `updater.py` 檢查更新、提交最新資料並重新發布網站。
