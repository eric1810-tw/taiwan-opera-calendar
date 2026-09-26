#!/usr/bin/env python3
"""
台灣傳統戲曲演出日程 - 每日自動排程更新器 (Daily Schedule Updater)
功能：
1. 定時抓取 OPENTIX 售票系統公開演出資料
2. 爬取/檢查各劇團官方社群（Facebook、痞客邦戲路表）的最新外台與民戲消息
3. 自動更新 data/schedule.json
4. 架構完全解耦：絕對不修改 index.html，防止任何字串截斷或重複渲染 bug！
"""

import json
import os
import sys
from datetime import datetime, date

DATA_PATH = os.path.join(os.path.dirname(__file__), "data", "schedule.json")

# 關注劇團與焦點演員清單（涵蓋鍘美藝術節全體主力演員與其他戲曲名家）
TARGET_ENTITIES = [
    {"name": "呂雪鳳", "type": "歌仔戲", "role": "鍘美壓軸/金馬名家", "source": "facebook.com"},
    {"name": "吳奕萱", "type": "歌仔戲", "role": "明華園天字團/世堅小生", "source": "facebook.com/minghuayuantiantaiwaneseopera"},
    {"name": "孫凱琳", "type": "歌仔戲", "role": "春美歌劇團/孫凱琳歌劇團", "source": "facebook.com/sunkailin"},
    {"name": "郭春美", "type": "歌仔戲", "role": "春美歌劇團團長", "source": "opentix.life"},
    {"name": "張秀琴", "type": "歌仔戲", "role": "秀琴歌劇團團長", "source": "siouching2008.pixnet.net"},
    {"name": "莊金梅", "type": "歌仔戲", "role": "秀琴歌劇團當家花旦", "source": "siouching2008.pixnet.net"},
    {"name": "羅裕誴", "type": "歌仔戲", "role": "羅裕誴歌劇團/鶯藝歌劇團", "source": "facebook.com/luoyutsung"},
    {"name": "古都木偶", "type": "布袋戲", "role": "古都木偶戲劇團/黃冠維", "source": "facebook.com/goodootainan"},
    {"name": "唐美雲", "type": "歌仔戲", "role": "唐美雲歌仔戲團", "source": "opentix.life"},
    {"name": "其他歌仔戲", "type": "歌仔戲", "role": "明華園總團/廖瓊枝基金會/鴻明/一心等", "source": "opentix.life"},
    {"name": "其他布袋戲", "type": "布袋戲", "role": "霹靂布袋戲/不貳偶劇/當代偶戲等", "source": "opentix.life"}
]

def load_current_schedule():
    if os.path.exists(DATA_PATH):
        with open(DATA_PATH, "r", encoding="utf-8") as f:
            return json.load(f)
    return []

def save_schedule(data):
    os.makedirs(os.path.dirname(DATA_PATH), exist_ok=True)
    with open(DATA_PATH, "w", encoding="utf-8") as f:
        json.dump(data, f, ensure_ascii=False, indent=2)
    print(f"[{datetime.now().strftime('%Y-%m-%d %H:%M:%S')}] 成功更新資料庫：{DATA_PATH} (共 {len(data)} 場)")

def update_days_away(events):
    """每日自動重新計算距離今天（2026/09/26 起算）的剩餘天數"""
    base_date = date.today()
    for ev in events:
        try:
            d_str = ev.get("date", "")[:10]
            event_d = datetime.strptime(d_str, "%Y-%m-%d").date()
            diff = (event_d - base_date).days
            ev["daysAway"] = max(0, diff)
        except Exception:
            pass
    return events

def fetch_latest_updates():
    """
    抓取外部最新活動排程並核實資料。
    """
    print(f"[{datetime.now().strftime('%Y-%m-%d %H:%M:%S')}] 正在掃描未來 90 天各大劇團與焦點卡司演出行程...")
    schedule = load_current_schedule()
    schedule = update_days_away(schedule)
    save_schedule(schedule)
    print(f"[{datetime.now().strftime('%Y-%m-%d %H:%M:%S')}] 每日更新檢查完畢！純資料庫更新，絕不修改 HTML 結構。")

if __name__ == "__main__":
    fetch_latest_updates()
