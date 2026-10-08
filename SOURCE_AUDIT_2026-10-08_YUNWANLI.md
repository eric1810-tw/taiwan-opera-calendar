# 《雲萬里》單則來源核對｜2026-10-08

本次為使用者提供單則 Threads 線索的定點核查，不是完整社群巡檢，不更新 `patrol_status.json`。資料刷新 metadata 保留遠端每日更新結果。

## 來源與替代讀取

- 線索：https://www.threads.com/@suiianinn/post/DeO59vdEmTS 。一般 web reader 無法讀取，改用內建瀏覽器成功讀到主文。主文為歌仔戲與祖母的回憶，場次資訊在附圖。
- 原頁媒體按鈕的 AX click 遇到 shadow-root 錯誤；直接開啟頁面已列出的 `/media` 連結，成功查看原海報：https://www.threads.com/@suiianinn/post/DeO59vdEmTS/media 。未重複盲試相同 click。
- 海報標示「2026聲浪藝術節」、明華園黃字戲劇團《雲萬里》、10/10（六）14:30、恆春文化中心劇場館、東門路1巷18號、票價300元、65歲以上100元。
- 找到並實讀 OPENTIX 官方頁：https://www.opentix.life/event/2073017191612608513 。web reader 未呈現動態場次，內建瀏覽器顯示唯一場次為2026/10/10（六）14:30，場館為恆春文化中心劇場館表演廳，地址屏東縣恆春鎮東門路1巷18號1樓，本場次同步錄影。
- 官方頁另列主演翁妙嬅、陳子豪、晨翎，演出全長100分鐘無中場休息，建議7歲以上，65歲以上100元且入場須出示身分證件。未操作訂票，不推定剩餘票券。

## 比對與結果

- 編修前 fetch 並 fast-forward 整合遠端 `12c6f74` 每日更新，保留其 metadata `2026-10-08T10:23:47+08:00` 和原場次。
- 依官方節目ID、2026/10/10、劇團、劇目及恆春場館核查，既有公開表無同場，新增一張 `mhy-huang-2026-10-10-yunwanli-hengchun`。
- `verified` 依官方 OPENTIX 日期、時間、場館及節目資訊，不因 Threads 分享者身分而升級。卡片詳情與核實來源採 OPENTIX；原 Threads 與海報頁保留為 relatedSourceUrls。
- 帳號清單不變；本次單則核查未宣稱已完成日常巡檢。

## 驗收

- 提交前17項單元測試、JavaScript 語法、schema、去重及 diff 檢查通過；移除新增卡後資料與遠端整合後的原表完全相同。僅本來源紀錄和 schedule.json 屬此次提交範圍。
- 部署完成與公開 JSON 核對結果於發布後留下驗收收據；未核對前不宣稱已上線。

## 發布驗收收據

- 驗收時間：2026-10-08T22:53:52+08:00。
- 資料提交：`3e4e442affcf7fff929ddc538648b0516ab4fa5f`。
- [Actions 37796129958](https://github.com/eric1810-tw/taiwan-opera-calendar/actions/runs/37796129958) 已 completed/success。
- 公開 schedule.json 中只有一張本場卡，所有欄位與本地核對一致。
- 公開 patrol_status.json 仍為2026-10-08T07:44:15+08:00、failed，與本地一致；沒有把此定點查核誤當整輪巡檢成功。
