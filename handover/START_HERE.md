# Antigravity 接手套件入口

建立於2026-10-17（Asia/Taipei）。這套文件用於讓Antigravity直接接手現有臺灣戲曲情報站。

## 檔案

1. [完整工作交接說明書](ANTIGRAVITY_HANDOVER_2026-10-17.md)：架構、當前狀態、資料規則、全部名單、每日流程、恢復、部署、技術債和驗收。
2. [接手可行性評估](ANTIGRAVITY_FEASIBILITY_2026-10-17.md)：能接手什麼、已實測什麼、仍需驗收什麼、訂閱與工具界線。
3. [直接貼給Antigravity的提示詞](ANTIGRAVITY_TAKEOVER_PROMPT_2026-10-17.md)：唯讀接手、正式手動巡檢、持續排程切換三階段。
4. [現況證據JSON](PROJECT_SNAPSHOT_2026-10-17.json)：repo與公開狀態、完整名單、每來源未完項、原工作區檔案雜湊、舊排程prompt及本機工具證據。
5. [交接文件驗收紀錄](HANDOVER_ACCEPTANCE_2026-10-17.md)：本次核對項目、獨立審核範圍、原工作區保留證據與未驗證事項。
6. [每日巡檢與GitHub逐輪核對](PATROL_GITHUB_AUDIT_2026-10-17.md)：哪些紀錄已上傳、哪些有部署證據，以及10/15歷史收據被後續恢復清除的問題；[機器證據](PATROL_GITHUB_AUDIT_2026-10-17.json)。

## 開始方法

**執行方式：Antigravity桌面版；不以agy CLI接手。未確認事項先詢問使用者。**

在Antigravity桌面版開啟 `/Users/eric/aiwork/taiwan-opera-calendar`，把提示詞第一階段貼進新對話。請不要開 `/Users/eric/.gemini/antigravity/scratch/taiwan-opera-calendar` 的舊repo。

目前正式網站：[GitHub Pages](https://eric1810-tw.github.io/taiwan-opera-calendar/)。停止GPT訂閱不會因而關閉現站或GitHub updater；03:00代理巡檢需另外在新平台驗收並切換。

這套件是交接文件，不是完整repo備份，ZIP也只包含handover文件。新電腦／另一環境需保留現有repo、未提交修改和使用者文件；純Git clone不會帶走未追蹤／未提交內容。文件可能含本機路徑及操作脈絡，對外分享前自行決定範圍；沒有token或cookie。

使用者已於2026-10-17授權嚴格審核、修正後將本套件提交與推送。若從GitHub main讀到本檔，表示這個版本已進入該repo；本機檔案是否與遠端相同仍需核對。文件沒有停用原排程或建立新排程。日期、卡數、模型與狀態都是快照，接手應重查。

## GitHub使用方式

本專案已使用[GitHub repo](https://github.com/eric1810-tw/taiwan-opera-calendar)，main分支經GitHub Actions部署至GitHub Pages。現有本機資料夾已設定origin，不必為改用桌面版再重新clone。GitHub只會取得已commit並成功push的內容；不會自動同步每次本機存檔。交接套件發布後，從包含本套件的main版本clone可取得handover；其餘既有未提交／未追蹤使用者檔案仍不會隨clone帶走。

03:00巡檢原本就要求推送當輪紀錄與狀態，再驗收Actions及公開網站。實際歷史曾有受阻與延後補推，不能說每天03:00都準時完成發布；也不能因新文件當時未提交，就推定每日巡檢都沒有上傳。詳見逐輪核對表。
