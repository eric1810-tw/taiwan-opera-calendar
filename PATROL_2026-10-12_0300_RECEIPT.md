# 2026-10-12 03:00 巡檢發布驗收收據

- 巡檢進度：`patrol_runs/2026-10-12_0300.json`，實際開始 `2026-10-12T02:58:14+08:00`；重試同一輪後 latest final status 仍為 `failed`：2 complete、4 partial、15 failed、0 pending。文化部及全部 Issues 完成；15 個社群目標仍 failed，這是內容覆蓋結果，部署本身另行驗收。
- 資料提交 SHA：`cd6bd23073c94141bbc97a4a30ce1c4db8dabd36`；已推送，`origin/main` 指向同一 SHA。此提交正常整合遠端 auto-update `718b898`，未 force-push。
- Workflow：`.github/workflows/daily-update.yml`，Actions run [38166376833](https://github.com/eric1810-tw/taiwan-opera-calendar/actions/runs/38166376833)，head SHA 完全相同，狀態 `completed/success`。workflow push 路徑執行 17 項測試、組合 Pages 檔案並部署。
- 初次 `patrol_progress.py verify` 通過時間：`2026-10-12T03:07:29+08:00`。重試後 06:47:08 及第二次 resume 後 `2026-10-12T09:56:56+08:00`，均對相同資料 SHA 與 Actions run 執行 verify 成功；公開狀態仍是 `2026-10-12T02:58:14+08:00 / failed`，schedule、metadata 與原資料 SHA 的內容一致。重試只改變本輪 JSON 的來源證據，不改網站資料檔。
- 公開 JSON 對照該資料 SHA 的 `git show`：`patrol_status.json` HTTP 200、完全相同；`schedule.json` HTTP 200、105 筆、完全相同；`metadata.json` HTTP 200、完全相同，刷新時間 `2026-10-11T09:28:30+08:00`。
- 本地驗證：`python3 -m unittest -v` 17 tests PASS；`node --check assets/app.js` PASS；`git diff --check` PASS；schedule schema、日期/endDate、105 筆唯一 ID 與 JSON parse PASS。

## SHA256

- `data/schedule.json`: `35d0adb1218e6ba1c43cd3ac500433cd6d08dc1b7354336c1f2fd2e6dcc61355`
- `data/metadata.json`: `b7b88e788be28d9580dde364f8a0bc321b3f3638773f69f3078b3e64380d5b50`
- `data/patrol_status.json`: `1cf98e34678f7b8a076608c6b9578640379b758c7f166039c527d35242726b65`
- `patrol_runs/2026-10-12_0300.json`（完成本次重試並 publication verified）：`55f43f86dbe059f9d3772551ae87703476fc7dbb32540347769d63de6ba26df8`。

## 恢復

第一次重試 06:41–06:45，第二次恢復 09:55–09:56 Asia/Taipei：Threads 10 帳號均重試後仍是載入骨架；Facebook 尚和、蘭陽讀到一則精選公告但近期動態流／媒體不完整，其餘原 failed 頁仍無可讀正文。尚和《寒窯之外》11/7–8已由 OPENTIX 卡涵蓋，蘭陽《錯配姻緣》10/26已在排程，未因局部讀取修改卡片。第二次恢復另測 Threads 公開索引與匿名 HTTPS、Facebook 公開索引／替代 reader／匿名 HTTPS，分別得到空搜尋、通用Threads殼、Facebook暫時限制／HTTP 400；未讀取到任何原 failed 帳號正文。其餘 15 個 failed 的正文未讀不代表無新資訊。續跑時用 `python3 scripts/patrol_progress.py resume --run patrol_runs/2026-10-12_0300.json`，先切換可用公開讀取路徑，再逐項記錄每次結果。舊 heartbeat `threads` 維持停用。
