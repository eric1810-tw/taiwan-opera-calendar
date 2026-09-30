#!/usr/bin/env python3
"""從 dateFormatted 可明確解析的日期清單遷移選填 endDate。"""

import json
import re
import sys
import argparse
from datetime import date
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
SCHEDULE = ROOT / "data" / "schedule.json"
TOKEN = re.compile(r"(?:(20\d{2})\s*[/年.-]\s*)?(\d{1,2})\s*[/月.-]\s*(\d{1,2})")


def parsed_dates(event):
    text = event["dateFormatted"].split("(原公告", 1)[0].split("（原公告", 1)[0]
    matches = list(TOKEN.finditer(text))
    start = date.fromisoformat(event["date"])
    dates = []
    previous = None
    for match in matches:
        year = int(match.group(1)) if match.group(1) else (previous.year if previous else start.year)
        month, day = int(match.group(2)), int(match.group(3))
        if previous and not match.group(1) and (year, month) < (previous.year, previous.month):
            year += 1
        try:
            current = date(year, month, day)
        except ValueError:
            return None, f"日期無效：{match.group(0)}"
        dates.append(current)
        previous = current
    if len(dates) < 2:
        return None, "無法由 dateFormatted 判定多日日期"
    if dates[0] != start:
        return None, f"dateFormatted 首日 {dates[0]} 與 date {start} 不一致"
    if any(right < left for left, right in zip(dates, dates[1:])):
        return None, "日期順序不明確"
    return dates[-1], None


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--apply", action="store_true", help="寫入 schedule.json")
    parser.add_argument("--base-date", default=date.today().isoformat(), help="清除已結束場次時使用的基準日期")
    parser.add_argument("--report", help="將相同遷移清單另存為 Markdown")
    args = parser.parse_args()
    today = date.fromisoformat(args.base_date)
    events = json.loads(SCHEDULE.read_text(encoding="utf-8"))
    additions, uncertain = [], []
    for event in events:
        end_date, reason = parsed_dates(event)
        if reason:
            # 單日資料預期沒有 endDate；僅列出明顯像區間但解析失敗的項目。
            if re.search(r"[–—~～至]", event["dateFormatted"]):
                uncertain.append((event["id"], event["dateFormatted"], reason))
            continue
        iso = end_date.isoformat()
        if event.get("endDate") != iso:
            additions.append((event["id"], event.get("endDate"), iso))
            event["endDate"] = iso
    expired = [event["id"] for event in events if date.fromisoformat(event.get("endDate", event["date"])) < today]
    retained = [event for event in events if event["id"] not in set(expired)]
    lines = ["新增 endDate（id | 舊值 | 新值）"]
    for row in additions:
        lines.append(" | ".join(str(value or "（無）") for value in row))
    lines.append(f"\n無法判定：{len(uncertain)} 筆")
    for row in uncertain:
        lines.append(" | ".join(row))
    lines.append(f"\n依基準日 {today} 移除已結束場次：{', '.join(expired) if expired else '無'}")
    if args.apply:
        SCHEDULE.write_text(json.dumps(retained, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
        lines.append(f"已寫入 {SCHEDULE.relative_to(ROOT)}；保留 {len(retained)} 筆")
    else:
        lines.append("預覽模式；加 --apply 才會寫入。")
    output = "\n".join(lines)
    print(output)
    if args.report:
        report = ROOT / args.report
        report.write_text("# 場次結束日遷移清單\n\n" + output + "\n", encoding="utf-8")


if __name__ == "__main__":
    main()
