#!/usr/bin/env python3
"""
台灣傳統戲曲演出日程 - 每日自動排程更新器 (Daily Schedule Updater)
功能：
1. 讀取文化部公開藝文活動 JSON，將待核實戲曲線索存入獨立候選檔
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
THREADS_ACCOUNTS_PATH = os.path.join(os.path.dirname(__file__), "data", "threads_accounts.json")
THREADS_CANDIDATES_PATH = os.path.join(os.path.dirname(__file__), "data", "threads_candidates.json")
MOC_CANDIDATES_PATH = os.path.join(os.path.dirname(__file__), "data", "moc_candidates.json")
THREADS_API_URL = "https://graph.threads.net/v1.0/profile_posts"
API_URL = "https://cloud.culture.tw/frontsite/trans/SearchShowAction.do"
KEYWORDS = ("歌仔戲", "布袋戲", "掌中戲")
TIMEOUT_SECONDS = 60
MAX_ATTEMPTS = 2
REQUIRED_FIELDS = {
    "id", "date", "dateFormatted", "daysAway", "time", "troupe", "genre",
    "artist", "title", "category", "badgeType", "verifyStatus", "verifyLabel",
    "location", "region", "status", "description", "link", "tags",
}
ALLOWED_GENRES = {"歌仔戲", "布袋戲", "音樂劇", "豫劇"}
ALLOWED_VERIFY_STATUS = {"verified", "community", "pending"}
ALLOWED_BADGE_TYPES = {"ticket", "free", "temple", "plan", "outdoor", "broadcast"}
ALLOWED_REGIONS = {"北部", "中部", "南部", "東部", "未分類"}

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
        if not re.fullmatch(r"\d{4}-\d{2}-\d{2}", event["date"]):
            raise ValueError(f"event {index} date must be YYYY-MM-DD")
        datetime.strptime(event["date"], "%Y-%m-%d")
        end_date = event.get("endDate")
        if end_date is not None:
            if not isinstance(end_date, str) or not re.fullmatch(r"\d{4}-\d{2}-\d{2}", end_date):
                raise ValueError(f"event {index} endDate must be YYYY-MM-DD when present")
            try:
                parsed_end_date = datetime.strptime(end_date, "%Y-%m-%d").date()
            except ValueError as error:
                raise ValueError(f"event {index} endDate is not a valid calendar date") from error
            if parsed_end_date < datetime.strptime(event["date"], "%Y-%m-%d").date():
                raise ValueError(f"event {index} endDate must not precede date")
        if event["genre"] not in ALLOWED_GENRES and event["genre"] not in {f"其他{x}" for x in ALLOWED_GENRES}:
            raise ValueError(f"event {index} has invalid genre")
        if event["verifyStatus"] not in ALLOWED_VERIFY_STATUS:
            raise ValueError(f"event {index} has invalid verifyStatus")
        if event["badgeType"] not in ALLOWED_BADGE_TYPES:
            raise ValueError(f"event {index} has invalid badgeType")
        if event["region"] not in ALLOWED_REGIONS:
            raise ValueError(f"event {index} has invalid region")
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


def atomic_write_json(path, data):
    """Write JSON without leaving a partial file if the process is interrupted."""
    directory = os.path.dirname(path)
    fd, temporary_path = tempfile.mkstemp(prefix="threads-", suffix=".json", dir=directory)
    try:
        os.fchmod(fd, 0o644)
        with os.fdopen(fd, "w", encoding="utf-8") as output:
            json.dump(data, output, ensure_ascii=False, indent=2)
            output.write("\n")
            output.flush()
            os.fsync(output.fileno())
        os.replace(temporary_path, path)
    finally:
        if os.path.exists(temporary_path):
            os.unlink(temporary_path)


def fetch_threads_posts(username, access_token):
    """Read a public profile's recent posts through Meta's official Threads API."""
    params = urlencode({
        "username": username,
        "fields": "id,username,text,timestamp,permalink,media_type",
        "limit": 25,
    })
    request = Request(THREADS_API_URL + "?" + params,
                      headers={
                          "User-Agent": "TaiwanOperaCalendar/1.0",
                          "Authorization": f"Bearer {access_token}",
                      })
    with urlopen(request, timeout=30) as response:
        payload = json.loads(response.read().decode("utf-8"))
    if not isinstance(payload, dict) or not isinstance(payload.get("data", []), list):
        raise RuntimeError(f"Threads API returned an unexpected response for @{username}")
    return payload.get("data", [])


THREADS_EVENT_TERMS = ("演出", "表演", "公演", "戲", "戲棚", "廟會", "場次", "開演", "演出時間")


def discover_threads_candidates(access_token):
    """Save event-related source posts for human review; never auto-publish them."""
    with open(THREADS_ACCOUNTS_PATH, "r", encoding="utf-8") as source:
        accounts = json.load(source)
    if not isinstance(accounts, list):
        raise ValueError("Threads account list must be a JSON array")

    try:
        with open(THREADS_CANDIDATES_PATH, "r", encoding="utf-8") as source:
            existing = json.load(source)
    except FileNotFoundError:
        existing = []
    if not isinstance(existing, list):
        raise ValueError("Threads candidate store must be a JSON array")
    by_id = {item.get("postId"): item for item in existing if isinstance(item, dict)}
    failures = []
    successful_accounts = 0
    today = taiwan_today()

    for account in accounts:
        username = account.get("username") if isinstance(account, dict) else None
        if not isinstance(username, str) or not re.fullmatch(r"[A-Za-z0-9._]+", username):
            failures.append(f"invalid account entry: {account!r}")
            continue
        try:
            posts = fetch_threads_posts(username, access_token)
        except (HTTPError, URLError, TimeoutError, OSError, UnicodeError,
                json.JSONDecodeError, RuntimeError) as error:
            failures.append(f"@{username}: {error}")
            continue
        successful_accounts += 1
        for post in posts:
            if not isinstance(post, dict) or not isinstance(post.get("id"), str):
                continue
            text = str(post.get("text") or "").strip()
            if not text or not any(term in text for term in THREADS_EVENT_TERMS):
                continue
            timestamp = str(post.get("timestamp") or "")
            try:
                posted_at = datetime.fromisoformat(timestamp.replace("Z", "+00:00"))
                if posted_at.date() < today - timedelta(days=30):
                    continue
            except ValueError:
                pass
            by_id[post["id"]] = {
                "postId": post["id"],
                "username": username,
                "postedAt": timestamp,
                "permalink": str(post.get("permalink") or f"https://www.threads.com/@{username}"),
                "text": text,
                "reviewStatus": "pending",
                "discoveredAt": datetime.now(ZoneInfo("Asia/Taipei")).isoformat(timespec="seconds"),
            }

    if accounts and not successful_accounts:
        raise RuntimeError("Threads 巡檢全部失敗；候選資料未更新，請確認 API 授權與權限")
    candidates = sorted(by_id.values(), key=lambda item: item.get("postedAt", ""), reverse=True)
    atomic_write_json(THREADS_CANDIDATES_PATH, candidates)
    print(f"Threads 即時巡檢完成：{successful_accounts}/{len(accounts)} 個帳號；候選貼文 {len(candidates)} 筆")
    for failure in failures:
        print(f"Threads 巡檢失敗：{failure}", file=sys.stderr)
    return candidates

def taiwan_today():
    return datetime.now(ZoneInfo("Asia/Taipei")).date()


def update_days_away(events, base_date=None):
    """Recalculate countdown values without silently hiding malformed dates."""
    base_date = base_date or taiwan_today()
    retained = []
    removed_ids = []
    for ev in events:
        event_d = datetime.strptime(ev["date"][:10], "%Y-%m-%d").date()
        end_d = datetime.strptime(ev.get("endDate", ev["date"])[:10], "%Y-%m-%d").date()
        if end_d < base_date:
            removed_ids.append(ev["id"])
            continue
        ev["daysAway"] = max(0, (event_d - base_date).days)
        retained.append(ev)
    if removed_ids:
        print(f"已剔除結束場次 {len(removed_ids)} 筆：{', '.join(removed_ids)}")
    return retained


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
            location_key = str(show.get("locationName") or show.get("location") or record.get("location") or "").strip()
            digest = hashlib.sha256(f"{title}|{event_date.isoformat()}|{location_key}".encode("utf-8")).hexdigest()[:10]
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
    """Refresh candidates and countdowns; never promote discoveries to the public schedule."""
    print(f"[{datetime.now().strftime('%Y-%m-%d %H:%M:%S')}] 正在查詢文化部公開藝文活動資料...")
    schedule = load_current_schedule()
    try:
        discovered = culture_candidates(fetch_culture_events())
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
        candidates = []
        candidate_ids = set()
        for event in discovered:
            program_id = opentix_program_id(event)
            if program_id and program_id in existing_program_ids:
                continue
            event_key = (event["date"][:10], event["title"])
            if event_key in existing_event_keys or event["id"] in candidate_ids:
                continue
            candidates.append(event)
            candidate_ids.add(event["id"])
        atomic_write_json(MOC_CANDIDATES_PATH, candidates)
        print(f"文化部資料源取得 {len(candidates)} 筆未發布、待核實候選")
    except RuntimeError as error:
        raise RuntimeError(f"文化部資料源巡檢失敗，停止發布以免誤更新時間：{error}") from error
    schedule = update_days_away(schedule)
    save_schedule(schedule)
    save_metadata()
    token = os.environ.get("THREADS_ACCESS_TOKEN")
    if token:
        try:
            discover_threads_candidates(token)
        except (OSError, ValueError, RuntimeError, json.JSONDecodeError) as error:
            # Optional social discovery must never block the published schedule.
            print(f"警告：Threads 候選巡檢失敗，保留既有資料：{error}", file=sys.stderr)
    else:
        print("略過 Threads 貼文巡檢：未設定 THREADS_ACCESS_TOKEN", file=sys.stderr)
    print(f"[{datetime.now().strftime('%Y-%m-%d %H:%M:%S')}] 每日更新檢查完畢！純資料庫更新，絕不修改 HTML 結構。")

if __name__ == "__main__":
    try:
        if "--threads-now" in sys.argv:
            token = os.environ.get("THREADS_ACCESS_TOKEN")
            if not token:
                raise RuntimeError("缺少 THREADS_ACCESS_TOKEN；請先在 GitHub Actions secret 設定 Meta Threads API 授權 token")
            discover_threads_candidates(token)
            raise SystemExit(0)
        fetch_latest_updates()
    except (OSError, ValueError, RuntimeError, json.JSONDecodeError) as error:
        print(f"更新失敗，原資料未被覆寫：{error}", file=sys.stderr)
        raise SystemExit(1)
