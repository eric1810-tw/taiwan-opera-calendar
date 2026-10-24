# 回歸案例對照（21 個，★ 請 Eric 抽核）

執行：`python3 -m unittest tests.test_patrol_v2_cases -v`、`node --test tests/test_social_capture.mjs`

| # | 案例（真實出處） | 預期 | 測試 |
|---|---|---|---|
| 1★ | 羅裕誴 De1UV_Ikxkl（10/23 18:14 發，10/23 21:19 與 10/24 03:08 兩輪都漏） | 動態列表假頁面：新讀取器保留首屏 De1UV_Ikxkl／De2R8XSkiWT，模擬頁面確實回收首屏節點；舊輸出被判 known-post-missing | `test_social_capture.mjs`「動態列表…」「不變式：已知貼文不在輸出」；`CaseReader.test_01_old_evidence_lacks_known_posts` |
| 2 | 守門帳號已知貼文從輸出消失 | 來源記 failed，不得回報成功 | `CaseReader.test_01_02_21_…` |
| 3★ | 水門宮：10/23 下午 3:30 扮仙、10/24 下午 5:00 扮仙、改到廟內（10/23 21:14 報告誤列「資訊一致」） | 判讀員說「已在表」也會被程式比出差異 → 轉 change；經 add_card 寫成「10/23 15:30 扮仙、10/24 17:00 扮仙」 | `CaseJudgment.test_03_shuimen_…` |
| 4★ | 新營：舊帖 DeeXP_umU6t「下午3點」對卡片 16:30（10/24 報告誤列一致） | 不得列一致，轉 change 並列出時間差異 | `CaseJudgment.test_04_xinying_…` |
| 5★ | 王福宮 11/6–11/10，11/7 沒有演出 | 顯示「2026/11/06、2026/11/08–2026/11/10（11/7 無演出）」；11/7 有場次就退回 | `CaseJudgment.test_05_wangfu_…` |
| 6★ | 《小狐狸買手套》（OPENTIX 標親子、多元偶戲，10/24 被建成布袋戲） | 標布袋戲會被擋（puppet-not-budaixi）→ 待查；OPENTIX 篩選也不當成戲曲相關 | `CaseJudgment.test_06_…`、`CaseOpentix` |
| 7 | De2R8XSkiWT 03:12 才發，來源 03:08 已讀 | 讀取當下尚未發布的已知貼文不算漏讀 | `test_social_capture.mjs`「案例7」 |
| 8 | 同一天重複觸發 | 第二次直接 done，不重複建輪 | `CaseRunControl.test_08_…` |
| 9 | 鎖還活著時再觸發／鎖失效 | 活鎖擋下；失效鎖接手並記錄 | `CaseRunControl.test_09_…` |
| 10 | 網路失敗（DNS） | fetch 最多 3 次，之後明確失敗 | `CaseRunControl.test_10_…` |
| 11 | Actions 只有別的 SHA 成功／本 SHA 失敗 | 不得 verified | `CasePublish.test_11_…`（兩個） |
| 12 | 公開檔仍舊 | compare-public 不一致 | `CasePublish.test_12_…` |
| 13 | 尚和：正文已列多場日期與劇目（10/23 報告稱「未列明細」） | 每場各自一個事件；漏交代整篇會被抓到 | `CaseJudgment.test_13_14_…` |
| 14 | 茶戲體驗（10/23 被直接判非戲曲） | 「體驗」可收錄 | 同上 |
| 15 | Threads 圖片輪播「1 / 2」 | 不當成 1/2 日期 | `CaseJudgment.test_15_…` |
| 16 | 同一場兩個帳號轉貼 | 一張卡、多來源 | `CaseJudgment.test_16_…` |
| 17 | 同日同地不同劇團 | 不合併 | `CaseJudgment.test_17_…` |
| 18 | 引用的原文不在貼文內 | 退回 quote-not-in-post | `CaseJudgment.test_18_…` |
| 19 | 同一貼文隔天沒變／改字 | 沒變不重送；改字重送 | `CaseCache.test_19_…` |
| 20 | 正式資料夾不在 main（10/23 wip/011 事故）／ff 失敗 | 前置失敗即停止 | `CaseRunControl.test_20_…`（兩個） |
| 21 | 1013.yr_ 連續 0 篇 | failed，不寫「沒有新資訊」 | `CaseReader.test_01_02_21_…` |

另外的防呆測試：海報內容必須有判讀紀錄才可引用、扮仙與正戲分開、禁用 git 指令與逐檔 stage、兩輪看圖。
