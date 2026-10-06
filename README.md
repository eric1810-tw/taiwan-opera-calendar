# 臺灣戲曲情報站

整理各地歌仔戲、布袋戲及其他戲曲演出消息，逐場標示日期、地點與來源狀態，陪你找下一場戲。資料以官方公告、售票頁及劇團／主辦單位公開資訊為準；社群線索未經交叉核實時不標為官方核實。

## 專案內容

- `index.html`、`assets/app.js`、`assets/app.css`：靜態前端。卡片由瀏覽器載入 `data/schedule.json`，並在臺灣日期過濾已結束場次。
- `data/schedule.json`：目前公開的場次資料；`endDate` 是多日活動的最後一場日期（不表示起訖日之間每天都有演出），單日活動可省略。
- `data/metadata.json`：最近一次成功刷新排程資料的時間，不代表每場演出都在該時間重新核實。
- `updater.py`：讀取文化部公開活動資料作候選、重新計算倒數並清除已結束場次；候選資料不會自動升格為已核實場次。
- `data/threads_accounts.json`、候選資料檔：來源巡檢設定與待人工核對線索。候選內容不包含在 GitHub Pages 網站 artifact 中。
- `tests/`：Python 標準函式庫 `unittest` 測試。

目前資料與快速篩選涵蓋古都木偶、羅裕誴、孫凱琳／春美、吳奕萱／明華、呂雪鳳、秀琴、唐美雲及其他歌仔戲／布袋戲；頁面以未來 90 天為主要資訊窗口。資料可能有公告延遲或異動，請以各場次來源公告為準。

## 本機預覽與測試

需使用 HTTP 伺服器才能讀取 JSON：

```bash
python3 -m http.server 8000
```

瀏覽器開啟 <http://localhost:8000/>。執行測試：

```bash
python3 -m unittest -v
```

## 重新編譯前端 CSS

Tailwind CSS 3.4.17 CLI 用於開發時編譯；已編譯的 `assets/app.css` 提交至版本庫，Actions 不需建置 CSS。需要 Node.js/npm，於專案根目錄執行：

```bash
npm exec --yes --package=tailwindcss@3.4.17 -- tailwindcss -i assets/input.css -o assets/app.css --minify
```

編譯設定在 `tailwind.config.cjs`，掃描 `index.html` 與 `assets/app.js`（含卡片模板中的 utility classes）。

## 自動更新與發布

`.github/workflows/daily-update.yml` 每日依 GitHub Actions 排程嘗試更新資料，並支援手動觸發。排程執行時間以 workflow 的 UTC cron 為準；失敗、外部來源不可用或無資料異動時，不能視作已更新。workflow 先執行單元測試，再跑 updater，最後只將 `index.html`、`assets/` 前端必要檔案及 `data/schedule.json`、`data/metadata.json` 組成 `_site/` 發布至 GitHub Pages。

GitHub Pages 請在 repository Settings → Pages 選擇 GitHub Actions 作為發布來源。若另以 Cloudflare Pages 直接連接 Git repository，需在 Cloudflare 設定正確 build/output 範圍；本 workflow 的 `_site/` 白名單不會限制 Cloudflare 對 repo 原始碼的存取，也不會替 Cloudflare 設定做任何變更。
