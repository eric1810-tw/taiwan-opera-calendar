#!/usr/bin/env python3
"""
台灣傳統戲曲演出日程 - 每日自動排程更新器 (Daily Schedule Updater)
功能：
1. 讀取文化部公開藝文活動 JSON，產生待人工核實的戲曲候選
2. 重新計算台灣時區日期與倒數天數
3. 驗證結構後以原子方式更新 data/schedule.json
4. 絕不修改 index.html
"""

import json
import hashlib
import os
import re
import sys
import tempfile
import time
from datetime import date, datetime, timedelta
from zoneinfo import ZoneInfo
from urllib.error import HTTPError, URLError
from urllib.parse import urlencode
from urllib.request import Request, urlopen

DATA_PATH = os.path.join(os.path.dirname(__file__), "data", "schedule.json")
METADATA_PATH = os.path.join(os.path.dirname(__file__), "data", "metadata.json")
API_URL = "https://cloud.culture.tw/frontsite/trans/SearchShowAction.do"
KEYWORDS = ("歌仔戲", "布袋戲", "掌中戲")
TIMEOUT_SECONDS = 60
MAX_ATTEMPTS = 2
REQUIRED_FIELDS = {
    "id", "date", "dateFormatted", "daysAway", "time", "troupe", "genre",
    "artist", "title", "category", "badgeType", "verifyStatus", "verifyLabel",
    "location", "region", "status", "description", "link", "tags",
}

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

def validate_schedule(data):
    if not isinstance(data, list):
        raise ValueError("schedule root must be a JSON array")
    seen = set()
    for index, event in enumerate(data):
        if not isinstance(event, dict):
            raise ValueError(f"event {index} must be an object")
        missing = REQUIRED_FIELDS - event.keys()
        if missing:
            raise ValueError(f"event {index} missing required fields: {sorted(missing)}")
        if not all(isinstance(event[key], str) and event[key].strip() for key in
                   ("id", "date", "title", "troupe", "genre", "location", "link")):
            raise ValueError(f"event {index} has an empty or invalid required string")
        if event["id"] in seen:
            raise ValueError(f"duplicate event id: {event['id']}")
        seen.add(event["id"])
        datetime.strptime(event["date"][:10], "%Y-%m-%d")
        if not isinstance(event["daysAway"], int) or event["daysAway"] < 0:
            raise ValueError(f"event {index} daysAway must be a non-negative integer")
        if not isinstance(event["tags"], list) or not all(isinstance(tag, str) for tag in event["tags"]):
            raise ValueError(f"event {index} tags must be an array of strings")
    return data


def load_current_schedule():
    with open(DATA_PATH, "r", encoding="utf-8") as source:
        return validate_schedule(json.load(source))

def save_schedule(data):
    validate_schedule(data)
    directory = os.path.dirname(DATA_PATH)
    original_mode = os.stat(DATA_PATH).st_mode & 0o777
    fd, temporary_path = tempfile.mkstemp(prefix="schedule-", suffix=".json", dir=directory)
    try:
        os.fchmod(fd, original_mode)
        with os.fdopen(fd, "w", encoding="utf-8") as output:
            json.dump(data, output, ensure_ascii=False, indent=2)
            output.write("\n")
            output.flush()
            os.fsync(output.fileno())
        os.replace(temporary_path, DATA_PATH)
    finally:
        if os.path.exists(temporary_path):
            os.unlink(temporary_path)
    print(f"[{datetime.now().strftime('%Y-%m-%d %H:%M:%S')}] 成功更新資料庫：{DATA_PATH} (共 {len(data)} 筆節目卡片)")


def save_metadata():
    """Atomically record when the schedule was most recently refreshed."""
    directory = os.path.dirname(METADATA_PATH)
    fd, temporary_path = tempfile.mkstemp(prefix="metadata-", suffix=".json", dir=directory)
    try:
        os.fchmod(fd, 0o644)
        with os.fdopen(fd, "w", encoding="utf-8") as output:
            json.dump({
                "lastUpdated": datetime.now(ZoneInfo("Asia/Taipei")).isoformat(timespec="seconds"),
                "timezone": "Asia/Taipei",
            }, output, ensure_ascii=False, indent=2)
            output.write("\n")
            output.flush()
            os.fsync(output.fileno())
        os.replace(temporary_path, METADATA_PATH)
    finally:
        if os.path.exists(temporary_path):
            os.unlink(temporary_path)
    print(f"資料更新時間已寫入：{METADATA_PATH}")

def taiwan_today():
    return datetime.now(ZoneInfo("Asia/Taipei")).date()


def update_days_away(events, base_date=None):
    """Recalculate countdown values without silently hiding malformed dates."""
    base_date = base_date or taiwan_today()
    for ev in events:
        event_d = datetime.strptime(ev["date"][:10], "%Y-%m-%d").date()
        ev["daysAway"] = max(0, (event_d - base_date).days)
    return events


def opentix_program_id(event):
    """Return the numeric OPENTIX event/program ID from either URL form."""
    for key in ("link", "sourceUrl"):
        value = event.get(key, "")
        if isinstance(value, str):
            match = re.search(r"opentix\.life/(?:event|program)/(\d+)", value)
            if match:
                return match.group(1)
    return None


def remove_duplicate_candidates(events):
    """Drop machine candidates already represented by a curated OPENTIX card."""
    curated_ids = {
        program_id for event in events
        if event.get("verifyStatus") != "pending"
        for program_id in (opentix_program_id(event),)
        if program_id
    }
    return [
        event for event in events
        if not (
            event.get("verifyStatus") == "pending"
            and opentix_program_id(event) in curated_ids
        )
    ]


def infer_region(location):
    """Map an explicit Taiwan city/county name to the site's region filters."""
    text = str(location or "")
    regions = {
        "北部": ("基隆", "臺北", "台北", "新北", "桃園", "新竹", "宜蘭"),
        "中部": ("苗栗", "臺中", "台中", "彰化", "南投", "雲林"),
        "南部": ("嘉義", "臺南", "台南", "高雄", "屏東", "澎湖"),
        "東部": ("花蓮", "臺東", "台東"),
    }
    matches = [region for region, place_names in regions.items()
               if any(place in text for place in place_names)]
    return matches[0] if len(matches) == 1 else "未分類"


def fetch_culture_events():
    """Fetch the Ministry of Culture's documented all-category JSON feed."""
    request = Request(
        f"{API_URL}?{urlencode({'method': 'doFindTypeJ', 'category': 'all'})}",
        headers={"User-Agent": "TaiwanOperaCalendar/1.0 (public cultural events)"},
    )
    last_error = None
    for attempt in range(MAX_ATTEMPTS):
        try:
            # The official endpoint's certificate chain omits a Subject Key
            # Identifier and is rejected by OpenSSL 3.6 strict mode. Keep CA
            # and hostname checks enabled; relax only X509_STRICT for this URL.
            import ssl
            context = ssl.create_default_context()
            if hasattr(ssl, "VERIFY_X509_STRICT"):
                context.verify_flags &= ~ssl.VERIFY_X509_STRICT
            with urlopen(request, timeout=TIMEOUT_SECONDS, context=context) as response:
                payload = json.loads(response.read().decode("utf-8"))
            if not isinstance(payload, list):
                raise RuntimeError("Culture API returned a non-array payload; check its method/schema")
            return payload
        except RuntimeError:
            raise
        except (HTTPError, URLError, TimeoutError, OSError, UnicodeError, json.JSONDecodeError) as error:
            last_error = error
            if attempt + 1 < MAX_ATTEMPTS:
                time.sleep(2 ** attempt)
    raise RuntimeError(f"Culture API unavailable after {MAX_ATTEMPTS} attempts: {last_error}")


def culture_candidates(records, today=None):
    """Create clearly unverified review candidates; never promote source data to verified."""
    today = today or taiwan_today()
    end_date = today + timedelta(days=90)
    candidates = []
    for record in records:
        if not isinstance(record, dict):
            continue
        title = str(record.get("title", "")).strip()
        unit_names = " ".join(
            record.get(key, "") for key in ("masterUnit", "otherUnit")
            if isinstance(record.get(key), str)
        )
        category_text = " ".join(
            record.get(key, "") for key in ("category", "showUnit", "subUnit")
            if isinstance(record.get(key), str)
        )
        explicit_genre_text = f"{title} {unit_names} {category_text}"
        if not title or not any(keyword in explicit_genre_text for keyword in KEYWORDS) or "演員" in title:
            continue
        explicit_genre_text = f"{title} {unit_names}"
        if not title or not any(keyword in explicit_genre_text for keyword in KEYWORDS) or "演員" in title:
            continue
        show_info = record.get("showInfo")
        shows = show_info if isinstance(show_info, list) and show_info else [{}]
        for show in shows:
            if not isinstance(show, dict):
                continue
            raw_date = str(show.get("time", record.get("startDate", "")))[:10]
            try:
                event_date = datetime.strptime(raw_date, "%Y/%m/%d").date() if "/" in raw_date else datetime.strptime(raw_date, "%Y-%m-%d").date()
            except ValueError:
                continue
            if not today <= event_date <= end_date:
                continue
            genre = "布袋戲" if any(word in explicit_genre_text for word in ("布袋戲", "掌中戲")) else "歌仔戲"
            digest = hashlib.sha256(f"{title}|{event_date.isoformat()}".encode("utf-8")).hexdigest()[:10]
            event_id = f"moc-{event_date:%Y%m%d}-{digest}"
            raw_link = show.get("webSales") or record.get("sourceWebPromote") or "https://cloud.culture.tw/"
            candidates.append({
                "id": event_id, "date": event_date.isoformat(),
                "dateFormatted": event_date.strftime("%Y/%m/%d"), "daysAway": 0,
                "time": str(show.get("time") or "時間請查官方公告"),
                "troupe": next((record[key].strip() for key in ("masterUnit", "otherUnit")
                                if isinstance(record.get(key), str) and record[key].strip()), "文化部開放資料候選"),
                "genre": genre, "artist": "待查官方公告", "title": title,
                "category": "文化部 Open Data 候選（待人工核實）", "badgeType": "plan",
                "verifyStatus": "pending", "verifyLabel": "⏳ 自動發現・待人工核實",
                "location": str(show.get("locationName") or show.get("location") or record.get("location") or "地點請查官方公告"),
                "region": infer_region(" ".join(
                    str(value) for value in
                    (show.get("locationName"), show.get("location"), record.get("location"))
                    if value
                )),
                "status": "待人工核實", "description": "由文化部公開資料關鍵字找到；發布前請人工核對劇種、主辦單位、日期與場地。",
                "link": str(raw_link),
                "linkLabel": "來源資訊（待核實）", "sourceUrl": str(raw_link),
                "tags": ["自動發現候選", genre],
            })
    return candidates

def fetch_latest_updates():
    """
    抓取外部最新活動排程並核實資料。
    """
    print(f"[{datetime.now().strftime('%Y-%m-%d %H:%M:%S')}] 正在查詢文化部公開藝文活動資料...")
    schedule = load_current_schedule()
    schedule = remove_duplicate_candidates(schedule)
    try:
        discovered = culture_candidates(fetch_culture_events())
        existing_by_id = {event["id"]: event for event in schedule}
        existing_event_keys = {
            (event["date"][:10], event["title"])
            for event in schedule
        }
        existing_program_ids = {
            program_id for event in schedule
            if event.get("verifyStatus") != "pending"
            for program_id in (opentix_program_id(event),)
            if program_id
        }
        new_events = []
        for event in discovered:
            program_id = opentix_program_id(event)
            if program_id and program_id in existing_program_ids:
                continue
            event_key = (event["date"][:10], event["title"])
            if event_key not in existing_event_keys:
                new_events.append(event)
                existing_event_keys.add(event_key)
                if program_id:
                    existing_program_ids.add(program_id)
            elif event["id"] in existing_by_id and existing_by_id[event["id"]].get("verifyStatus") == "pending":
                # Refresh only machine-generated candidates. Human-verified
                # entries and their editorial fields are never overwritten.
                existing_by_id[event["id"]].update(event)
        schedule.extend(new_events)
        print(f"文化部資料源新增 {len(new_events)} 筆待人工核實候選")
    except RuntimeError as error:
        # Keep existing checked-in data and still refresh countdowns on a source outage.
        print(f"警告：{error}", file=sys.stderr)
    schedule = update_days_away(schedule)
    save_schedule(schedule)
    save_metadata()
    print(f"[{datetime.now().strftime('%Y-%m-%d %H:%M:%S')}] 每日更新檢查完畢！純資料庫更新，絕不修改 HTML 結構。")

if __name__ == "__main__":
    try:
        fetch_latest_updates()
    except (OSError, ValueError, json.JSONDecodeError) as error:
        print(f"更新失敗，原資料未被覆寫：{error}", file=sys.stderr)
        raise SystemExit(1)
