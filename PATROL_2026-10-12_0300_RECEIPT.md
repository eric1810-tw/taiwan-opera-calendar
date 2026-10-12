# 2026-10-12 03:00 巡檢發布驗收收據

- 巡檢進度：`patrol_runs/2026-10-12_0300.json`，實際開始 `2026-10-12T02:58:14+08:00`；重試同一輪後 latest final status 為 `failed`：2 complete、5 partial、14 failed、0 pending。文化部及全部 Issues 完成；14 個社群目標仍 failed，這是內容覆蓋結果，部署本身另行驗收。
- 資料提交 SHA：`cd6bd23073c94141bbc97a4a30ce1c4db8dabd36`；已推送，`origin/main` 指向同一 SHA。此提交正常整合遠端 auto-update `718b898`，未 force-push。
- Workflow：`.github/workflows/daily-update.yml`，Actions run [38166376833](https://github.com/eric1810-tw/taiwan-opera-calendar/actions/runs/38166376833)，head SHA 完全相同，狀態 `completed/success`。workflow push 路徑執行 17 項測試、組合 Pages 檔案並部署。
- 初次 `patrol_progress.py verify` 通過時間：`2026-10-12T03:07:29+08:00`。重試後 06:47:08、09:56:56 及本次延後載入診斷後 `2026-10-12T10:02:34+08:00`，均對相同資料 SHA 與 Actions run 執行 verify 成功；公開狀態仍是 `2026-10-12T02:58:14+08:00 / failed`，schedule、metadata 與原資料 SHA 的內容一致。重試只改變本輪 JSON 的來源證據，不改網站資料檔。
- 巡檢 SHA `cd6bd23073c94141bbc97a4a30ce1c4db8dabd36` 的驗收當時，公開三 JSON 與該 SHA 相同：status failed、schedule 105 筆、metadata 更新時間 `2026-10-11T09:28:30+08:00`。本次收尾期間遠端另有自動刷新 `aa82f06`（`[skip ci]`，沒有對應 Actions run）；正常 merge 後，於 10:05 對目前網站三 JSON 重新 GET，皆 HTTP 200 且逐位元組 SHA 與最新本地檔一致：patrol_status `1cf98e34678f7b8a076608c6b9578640379b758c7f166039c527d35242726b65`，schedule 97 筆／`f2029bc1eff74e7e3c29e3987fc905bcbfa248432eb6678bdbafc2921b911647`，metadata `6e3b182fe2b8bfe7083fd4f18d3f6502e26ea08cbbce3268eda2b5e306ab3e0b`（更新時間 `2026-10-12T09:59:30+08:00`）。因此公開網站目前狀態已核對，但不把缺少 Actions 的 auto-refresh 說成 Actions 驗收成功。
- 本地驗證：`python3 -m unittest -v` 17 tests PASS；`node --check assets/app.js` PASS；`git diff --check` PASS；schedule schema、日期/endDate、105 筆唯一 ID 與 JSON parse PASS。

## SHA256

- `data/schedule.json`: `35d0adb1218e6ba1c43cd3ac500433cd6d08dc1b7354336c1f2fd2e6dcc61355`
- `data/metadata.json`: `b7b88e788be28d9580dde364f8a0bc321b3f3638773f69f3078b3e64380d5b50`
- `data/patrol_status.json`: `1cf98e34678f7b8a076608c6b9578640379b758c7f166039c527d35242726b65`
- `patrol_runs/2026-10-12_0300.json`（延後載入診斷後、publication verified）：`a5377bce70149d36d19af9bf413badf52a7867d0b4fac7fb91a59154cb516202`。

## 恢復

第一次重試 06:41–06:45，第二次恢復 09:55–09:56 Asia/Taipei。10:02 延後再取 `@the_rin.lpm` 無障礙樹後，實讀 9/26 與 9/27 兩則正文；底部仍載入中，媒體未全讀，該帳號改為 partial。這確認先前立即取得頁面骨架至少是部分 Threads 失敗的原因，巡檢重試應等內容載入後再判讀。Facebook 尚和、蘭陽讀到一則精選公告但近期動態流／媒體不完整，其餘原 failed 頁仍無可讀正文。尚和《寒窯之外》11/7–8已由 OPENTIX 卡涵蓋，蘭陽《錯配姻緣》10/26已在排程，未因局部讀取修改卡片。第二次恢復另測 Threads 公開索引與匿名 HTTPS、Facebook 公開索引／替代 reader／匿名 HTTPS，分別得到空搜尋、通用Threads殼、Facebook暫時限制／HTTP 400；未讀取到任何原 failed 帳號正文。其餘 14 個 failed 的正文未讀不代表無新資訊。續跑時用 `python3 scripts/patrol_progress.py resume --run patrol_runs/2026-10-12_0300.json`，先切換可用公開讀取路徑，再逐項記錄每次結果。舊 heartbeat `threads` 維持停用。
