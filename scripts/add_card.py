#!/usr/bin/env python3
"""
scripts/add_card.py - 傳統戲曲日程守護建卡程式

用法：
1. 社群貼文提案建卡：
   python3 scripts/add_card.py --proposal <提案.json> --evidence-dir <目錄>
2. 補充既有卡片（僅限補齊未列/未公布/待確認欄位）：
   python3 scripts/add_card.py --update <卡片id> --proposal <提案.json> --evidence-dir <目錄>
3. 異動既有卡片（同帳號且具異動公告）：
   python3 scripts/add_card.py --change <卡片id> --proposal <提案.json> --evidence-dir <目錄>
4. 取消既有卡片（同帳號且具取消公告）：
   python3 scripts/add_card.py --cancel <卡片id> --proposal <提案.json> --evidence-dir <目錄>
5. 文化部開放資料建卡：
   python3 scripts/add_card.py --from-moc "<活動標題>"
"""

import argparse
import hashlib
import json
import os
import re
import sys
import tempfile
from datetime import date, datetime, timedelta
from pathlib import Path
from zoneinfo import ZoneInfo

# 從 updater 匯入標準驗證與區域判定函式
ROOT_DIR = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT_DIR))
from updater import validate_schedule, infer_region, opentix_program_id

DEFAULT_SCHEDULE_PATH = ROOT_DIR / "data" / "schedule.json"
DEFAULT_REVIEW_QUEUE_PATH = ROOT_DIR / "data" / "review_queue.json"
DEFAULT_CANCELLED_PATH = ROOT_DIR / "docs" / "patrols" / "cancelled_cards.jsonl"
DEFAULT_FB_ACCOUNTS_PATH = ROOT_DIR / "data" / "facebook_accounts.json"
DEFAULT_MOC_RECORDS_PATH = ROOT_DIR / "data" / "moc_records.json"

UNSPECIFIED_KEYWORDS = ("未公布", "未列", "待確認", "時間請查官方公告", "地點請查官方公告", "待查官方公告")


def normalize_whitespace(text: str) -> str:
    """將所有空白（含換行、全形空白、tab）正規化為單一空格並去除首尾空白"""
    if not text:
        return ""
    return re.sub(r"[\s\u3000]+", " ", str(text)).strip()


def extract_account_id(url: str) -> str:
    """自 Threads 或 Facebook 網址萃取帳號識別碼"""
    if not url:
        return ""
    url = str(url).strip()
    threads_match = re.search(r"threads\.(?:net|com)/@([A-Za-z0-9._]+)", url)
    if threads_match:
        return threads_match.group(1).lower()
    fb_match = re.search(r"facebook\.com/([^/?#]+)", url)
    if fb_match:
        cand = fb_match.group(1).lower()
        if cand not in ("profile.php", "permalink.php", "story.php", "groups"):
            return cand
        id_match = re.search(r"[?&]id=(\d+)", url)
        if id_match:
            return id_match.group(1)
    return url.lower()


def parse_date(date_str: str) -> date:
    return datetime.strptime(date_str[:10], "%Y-%m-%d").date()


def match_date_in_quote(target_date: date, quote: str, end_date: date = None) -> bool:
    """
    檢查 quote 中是否有對應 target_date（與 end_date，如有）的月份與日期。
    接受 M/D、M月D日、M／D 三種寫法（數字可有前導 0）。
    亦支援同月連寫：如 10月23、24日、10/23-24、10/23~24 等。
    """
    q = quote

    def has_single_date(d: date) -> bool:
        m, day = d.month, d.day
        # 單獨月日匹配
        patterns = [
            rf"(?<!\d){m}\s*[/／]\s*0?{day}(?!\d)",
            rf"(?<!\d)0{m}\s*[/／]\s*0?{day}(?!\d)",
            rf"(?<!\d){m}\s*月\s*0?{day}\s*日?",
            rf"(?<!\d)0{m}\s*月\s*0?{day}\s*日?",
        ]
        if any(re.search(pat, q) for pat in patterns):
            return True
        # 連寫形式：例如 10月23、24日 或 10/23-24 或 10/23、24
        # 尋找同一月份後續的一串數字
        month_seq_patterns = [
            rf"(?<!\d){m}\s*月\s*([0-9\s、，,~～\-至到/／]+)(?:日)?",
            rf"(?<!\d)0{m}\s*月\s*([0-9\s、，,~～\-至到/／]+)(?:日)?",
            rf"(?<!\d){m}\s*[/／]\s*([0-9\s、，,~～\-至到/／]+)",
        ]
        for pat in month_seq_patterns:
            for match in re.finditer(pat, q):
                seq = match.group(1)
                # 從 seq 中提取所有純數字
                days_in_seq = [int(n) for n in re.findall(r"\b\d{1,2}\b", seq)]
                if day in days_in_seq:
                    return True
        return False

    if not has_single_date(target_date):
        return False

    if end_date and end_date != target_date:
        if not has_single_date(end_date):
            return False

    return True


def match_time_in_quote(time_str: str, quote: str) -> bool:
    """
    time 不是未公布時，其中每個 H:MM 或 HH:MM 都必須出現在 quote 裡。
    全形冒號視為半形，「晚上7:00」「晚上7點」與「19:00」視為相同。
    """
    if any(k in time_str for k in UNSPECIFIED_KEYWORDS):
        return True

    # 原文常見「下午 3:30」中間有空白；候選字串都不含空白，比對前一律去掉空白
    norm_quote = re.sub(r"[\s\u3000]+", "", quote.replace("：", ":"))
    times = re.findall(r"\b\d{1,2}:\d{2}\b", time_str.replace("：", ":"))
    if not times:
        # 如果不是具體 H:MM 格式，檢查整個字串是否在 quote 內
        return time_str in quote

    for t in times:
        h, m = [int(x) for x in t.split(":")]
        candidates = [
            f"{h}:{m:02d}",
            f"{h:02d}:{m:02d}",
        ]
        # 12 小時制轉換
        if h >= 12:
            h12 = h - 12 if h > 12 else 12
            candidates.extend([
                f"晚上{h12}:{m:02d}",
                f"晚間{h12}:{m:02d}",
                f"下午{h12}:{m:02d}",
                f"夜戲{h12}:{m:02d}",
                f"夜場{h12}:{m:02d}",
            ])
            if m == 0:
                candidates.extend([
                    f"晚上{h12}點",
                    f"晚間{h12}點",
                    f"下午{h12}點",
                    f"夜戲{h12}點",
                    f"夜場{h12}點",
                    f"{h}點整",
                    f"{h}點",
                ])
            elif m == 30:
                candidates.extend([
                    f"晚上{h12}點半",
                    f"晚間{h12}點半",
                    f"下午{h12}點半",
                    f"夜戲{h12}點半",
                ])
        else:
            candidates.extend([
                f"上午{h}:{m:02d}",
                f"早上{h}:{m:02d}",
                f"早戲{h}:{m:02d}",
                f"日戲{h}:{m:02d}",
            ])
            if m == 0:
                candidates.extend([
                    f"上午{h}點",
                    f"早上{h}點",
                    f"日戲{h}點",
                    f"{h}點整",
                    f"{h}點",
                ])
            elif m == 30:
                candidates.extend([
                    f"上午{h}點半",
                    f"早上{h}點半",
                    f"日戲{h}點半",
                ])

        if not any(cand in norm_quote for cand in candidates):
            return False

    return True


def match_location_in_quote(location: str, quote: str) -> bool:
    """location 去掉括號內文字後，主體字串必須是 quote 的子字串"""
    main_loc = re.sub(r"（[^）]*）|\([^)]*\)", "", location).strip()
    return main_loc in quote


def load_post_from_evidence(evidence_dir: Path, source: str = "", post_key: str = "", post_url: str = ""):
    """自 evidence_dir 尋找指定 postKey 或 post_url 的貼文物件。
    只在檔名對應到提案 source 的證據檔尋找（例如 facebook:lanyang.opera -> facebook_lanyang.opera.json）。
    postKey 優先於 post_url。找不到則回傳 None。
    """
    if not source and post_key:
        parts = post_key.split(":")
        if len(parts) >= 3:
            source = f"{parts[0]}:{parts[1]}"

    if not source:
        return None

    expected_filename = f"{source.replace(':', '_')}.json"
    target_file = evidence_dir / expected_filename
    if not target_file.exists():
        return None

    try:
        data = json.loads(target_file.read_text(encoding="utf-8"))
    except Exception:
        return None

    posts = data.get("posts", [])
    if not isinstance(posts, list):
        return None

    # 1. postKey 優先
    if post_key:
        for item in posts:
            if item.get("postKey") == post_key:
                return item
        return None

    # 2. postUrl 相容
    if post_url:
        norm_post_url = post_url.strip().rstrip("/")
        for item in posts:
            item_url = str(item.get("permalink") or item.get("postUrl") or item.get("url") or item.get("link") or "").strip().rstrip("/")
            if item_url == norm_post_url or item_url.split("?")[0] == norm_post_url.split("?")[0]:
                return item

    return None


def post_corpus(post: dict) -> str:
    """貼文正文＋本輪已存檔的海報判讀紀錄（imageReadings），作為原文比對範圍"""
    parts = [post.get("text", "") or ""]
    for reading in post.get("imageReadings") or []:
        if isinstance(reading, dict) and reading.get("sha256") and reading.get("reading"):
            parts.append(str(reading["reading"]))
    return normalize_whitespace(" ".join(parts))


def validate_sessions(sessions, no_show_dates, quote: str):
    """sessions：每筆一個日期、時間與種類（扮仙／正戲／其他）；noShowDates 不可有場次"""
    reasons = []
    if not isinstance(sessions, list) or not sessions:
        return ["sessions-invalid"]
    seen = set()
    for item in sessions:
        if not isinstance(item, dict):
            reasons.append("sessions-invalid")
            continue
        try:
            d = parse_date(item.get("date", ""))
        except Exception:
            reasons.append("invalid-date-format")
            continue
        if not match_date_in_quote(d, quote):
            reasons.append("date-not-in-quote")
        if item.get("kind", "正戲") not in ("扮仙", "正戲", "其他"):
            reasons.append("session-kind-invalid")
        if not match_time_in_quote(item.get("time", "未公布"), quote):
            reasons.append("time-not-in-quote")
        key = (item.get("date"), item.get("kind", "正戲"))
        if key in seen:
            reasons.append("duplicate-session")
        seen.add(key)
    session_dates = {item.get("date") for item in sessions if isinstance(item, dict)}
    for d in no_show_dates or []:
        if d in session_dates:
            reasons.append("session-on-no-show-date")
    return sorted(set(reasons), key=reasons.index)


def format_sessions(sessions, no_show_dates=None):
    """由 sessions 產生網站既有欄位：date、endDate、time、dateFormatted"""
    ordered = sorted(sessions, key=lambda s: (s["date"], 0 if s.get("kind") == "扮仙" else 1))
    dates = sorted({s["date"] for s in ordered})
    time_parts = []
    for item in ordered:
        md = f"{int(item['date'][5:7])}/{int(item['date'][8:10])}"
        t = item.get("time", "未公布")
        if any(k in t for k in UNSPECIFIED_KEYWORDS):
            t = "時間未公布"
        kind = item.get("kind", "正戲")
        # 時間後留空白：match_time_in_quote 以 \b 擷取 H:MM，緊接中文字會抓不到
        time_parts.append(f"{md} {t} {kind}" if kind != "其他" else f"{md} {t}")
    runs = []
    for d in dates:
        cur = parse_date(d)
        if runs and (cur - parse_date(runs[-1][-1])).days == 1:
            runs[-1].append(d)
        else:
            runs.append([d])
    labels = [r[0].replace("-", "/") if len(r) == 1 else f"{r[0].replace('-', '/')}–{r[-1].replace('-', '/')}" for r in runs]
    date_formatted = "、".join(labels)
    if no_show_dates:
        skipped = "、".join(f"{int(d[5:7])}/{int(d[8:10])}" for d in sorted(no_show_dates))
        date_formatted += f"（{skipped} 無演出）"
    return {
        "date": dates[0],
        "endDate": dates[-1] if dates[-1] != dates[0] else None,
        "time": "、".join(time_parts),
        "dateFormatted": date_formatted,
    }


def atomic_save_json(path: Path, data):
    path.parent.mkdir(parents=True, exist_ok=True)
    fd, temp_path = tempfile.mkstemp(prefix="card-", suffix=".json", dir=path.parent)
    try:
        with os.fdopen(fd, "w", encoding="utf-8") as stream:
            json.dump(data, stream, ensure_ascii=False, indent=2)
            stream.write("\n")
            stream.flush()
            os.fsync(stream.fileno())
        os.replace(temp_path, path)
    finally:
        if os.path.exists(temp_path):
            os.unlink(temp_path)


def append_to_review_queue(review_queue_path: Path, proposal: dict, reasons: list):
    """附加失敗提案至 review_queue.json（依 postKey 去重，舊格式依 postUrl 去重，fromMoc 依標題去重）"""
    queue = []
    if review_queue_path.exists():
        try:
            queue = json.loads(review_queue_path.read_text(encoding="utf-8"))
            if not isinstance(queue, list):
                queue = []
        except Exception:
            queue = []

    post_key = proposal.get("postKey", "")
    post_url = proposal.get("postUrl", "")
    entry = {
        "postKey": post_key,
        "postUrl": post_url,
        "proposal": proposal,
        "reasons": reasons,
        "rejectedAt": datetime.now(ZoneInfo("Asia/Taipei")).isoformat(timespec="seconds"),
    }
    # 去重
    def is_same(item):
        if post_key and item.get("postKey") == post_key:
            return True
        if not post_key and post_url and item.get("postUrl") == post_url:
            return True
        if proposal.get("fromMoc") and item.get("proposal", {}).get("fromMoc") == proposal.get("fromMoc"):
            return True
        return False

    new_queue = [item for item in queue if not is_same(item)]
    new_queue.append(entry)
    atomic_save_json(review_queue_path, new_queue)


def append_to_cancelled_file(cancelled_path: Path, card: dict, quote: str, post_url: str):
    cancelled_path.parent.mkdir(parents=True, exist_ok=True)
    entry = {
        "card": card,
        "quote": quote,
        "postUrl": post_url,
        "cancelledAt": datetime.now(ZoneInfo("Asia/Taipei")).isoformat(timespec="seconds"),
    }
    with open(cancelled_path, "a", encoding="utf-8") as f:
        f.write(json.dumps(entry, ensure_ascii=False) + "\n")


def apply_sessions_to_proposal(proposal: dict):
    """有 sessions 時，date／endDate／time／dateFormatted 一律由 sessions 產生，不採用提案自填值"""
    sessions = proposal.get("sessions")
    if not sessions or not isinstance(sessions, list):
        return
    try:
        fields = format_sessions(sessions, proposal.get("noShowDates"))
    except Exception:
        return
    proposal["date"] = fields["date"]
    if fields["endDate"]:
        proposal["endDate"] = fields["endDate"]
    else:
        proposal.pop("endDate", None)
    proposal["time"] = fields["time"]
    proposal["dateFormatted"] = fields["dateFormatted"]


def validate_proposal_common(proposal: dict, post: dict, schedule: list, today: date, fb_accounts: list, check_duplicate: bool = True):
    reasons = []
    quote = proposal.get("quote", "")

    # 1. postUrl 與 quote 檢查（比對範圍＝正文＋已存檔海報判讀）
    norm_quote = normalize_whitespace(quote)
    norm_text = post_corpus(post)
    if not norm_quote or norm_quote not in norm_text:
        reasons.append("quote-not-in-post")

    # 1a. 多場次（sessions）：逐筆檢查日期、時間、種類與無演出日
    if "sessions" in proposal:
        reasons.extend(validate_sessions(proposal["sessions"], proposal.get("noShowDates"), norm_quote))

    # 2. 日期檢查
    date_str = proposal.get("date", "")
    end_date_str = proposal.get("endDate")
    try:
        target_date = parse_date(date_str)
        target_end_date = parse_date(end_date_str) if end_date_str else None
    except Exception:
        reasons.append("invalid-date-format")
        target_date = None
        target_end_date = None

    if target_date:
        if not match_date_in_quote(target_date, norm_quote, target_end_date):
            if re.search(r"農曆|陰曆", norm_quote):
                reasons.append("lunar-only")
            else:
                reasons.append("date-not-in-quote")

        # 3. 日期範圍檢查（今天到今天＋120 天）
        if not (today <= target_date <= today + timedelta(days=120)):
            reasons.append("date-out-of-range")

    # 4. 時間檢查
    time_str = proposal.get("time", "未公布")
    if not match_time_in_quote(time_str, norm_quote):
        reasons.append("time-not-in-quote")

    # 5. 地點檢查
    location = proposal.get("location", "")
    if not location or not match_location_in_quote(location, norm_quote):
        reasons.append("location-not-in-quote")

    # 6. 劇團檢查
    troupe = proposal.get("troupe", "")
    fb_names = {acc.get("name") for acc in fb_accounts if isinstance(acc, dict) and acc.get("name")}
    if not (troupe in norm_quote or troupe in fb_names):
        reasons.append("troupe-not-in-quote")

    # 7. 劇名檢查
    title = proposal.get("title", "")
    title_matches = re.findall(r"《(.*?)》", title)
    for m in title_matches:
        if m not in norm_quote:
            reasons.append("title-not-in-quote")
            break
    if "title-not-in-quote" not in reasons:
        # title 需為 quote 子字串，或為描述性寫法
        is_descriptive = "戲路" in title or "公演" in title or "演出" in title
        if not (title in norm_quote or is_descriptive):
            reasons.append("title-not-in-quote")

    # 7a. 主演檢查
    artist = proposal.get("artist", "未公布")
    if not (artist in norm_quote or artist == troupe or any(k in artist for k in UNSPECIFIED_KEYWORDS)):
        reasons.append("artist-not-in-quote")

    # 7b. 類型檢查
    badge_type = proposal.get("badgeType", "temple")
    if badge_type == "free":
        if "免費" not in norm_quote:
            reasons.append("badgeType-not-free")
    elif badge_type == "ticket":
        if not any(k in norm_quote for k in ("售票", "購票", "票價", "元")):
            reasons.append("badgeType-not-ticket")
    elif badge_type not in ("temple", "plan", "outdoor", "broadcast", "lecture"):
        reasons.append("badgeType-invalid")

    # 8. 重複檢查
    if check_duplicate and target_date:
        main_loc = re.sub(r"（[^）]*）|\([^)]*\)", "", location).strip()
        prop_start = target_date
        prop_end = target_end_date or target_date
        for card in schedule:
            try:
                card_start = parse_date(card["date"])
                card_end = parse_date(card.get("endDate", card["date"]))
            except Exception:
                continue
            # 區間重疊
            if not (card_end < prop_start or card_start > prop_end):
                card_loc = card.get("location", "")
                card_main_loc = re.sub(r"（[^）]*）|\([^)]*\)", "", card_loc).strip()
                if (card.get("troupe") == troupe or
                    card_loc == location or
                    (main_loc and main_loc in card_loc) or
                    (card_main_loc and card_main_loc in location)):
                    reasons.append("duplicate")
                    break

    return reasons


def handle_proposal(args, today: date):
    proposal_path = Path(args.proposal)
    evidence_dir = Path(args.evidence_dir)
    schedule_path = Path(args.schedule)
    review_queue_path = Path(args.review_queue)
    fb_accounts_path = Path(args.facebook_accounts)

    proposal = json.loads(proposal_path.read_text(encoding="utf-8"))
    fb_accounts = json.loads(fb_accounts_path.read_text(encoding="utf-8")) if fb_accounts_path.exists() else []
    schedule = json.loads(schedule_path.read_text(encoding="utf-8")) if schedule_path.exists() else []

    source_id = proposal.get("source", "")
    post_key = proposal.get("postKey", "")
    post_url = proposal.get("postUrl", "")
    post = load_post_from_evidence(evidence_dir, source=source_id, post_key=post_key, post_url=post_url)
    if not post:
        reasons = ["post-not-found"]
        append_to_review_queue(review_queue_path, proposal, reasons)
        out = {"result": "rejected", "id": None, "reasons": reasons}
        print(json.dumps(out, ensure_ascii=False))
        return 1

    apply_sessions_to_proposal(proposal)
    reasons = validate_proposal_common(proposal, post, schedule, today, fb_accounts, check_duplicate=True)
    if reasons:
        append_to_review_queue(review_queue_path, proposal, reasons)
        out = {"result": "rejected", "id": None, "reasons": reasons}
        print(json.dumps(out, ensure_ascii=False))
        return 1

    # 通過檢查，程式自動組裝卡片欄位
    date_str = proposal["date"]
    end_date_str = proposal.get("endDate")
    troupe = proposal["troupe"]
    title = proposal["title"]
    location = proposal["location"]
    badge_type = proposal.get("badgeType", "temple")

    # 9. 程式自動填入欄位
    digest = hashlib.sha256(f"{date_str}_{troupe}_{title}_{location}".encode("utf-8")).hexdigest()[:8]
    card_id = f"auto-{date_str.replace('-', '')}-{digest}"

    if proposal.get("dateFormatted"):
        date_formatted = proposal["dateFormatted"]
    elif end_date_str and end_date_str != date_str:
        date_formatted = f"{date_str.replace('-', '/')}–{end_date_str.replace('-', '/')}"
    else:
        date_formatted = date_str.replace("-", "/")

    days_away = max(0, (parse_date(date_str) - today).days)
    region = infer_region(location)

    category_map = {
        "temple": "廟會民俗演出",
        "ticket": "售票演出",
        "free": "免費索票/戶外演出",
        "outdoor": "戶外公演",
        "plan": "預定演出",
        "lecture": "講座／體驗",
    }
    category = category_map.get(badge_type, "廟會民俗演出")

    source_id = proposal.get("source", "")
    if ":" in source_id:
        kind, sname = source_id.split(":", 1)
        source_label = f"@{sname}" if kind == "threads" else sname
    else:
        source_label = source_id or troupe

    post_date_raw = str(post.get("datetime") or "")[:10]
    post_date_label = post_date_raw if post_date_raw else "近期"
    quote_clip = proposal.get("quote", "")[:200]
    description = f"依 {source_label} {post_date_label} 公告：「{quote_clip}」"
    status = "依社群公告；未列事項請洽劇團或廟方"

    post_actual_url = post.get("url") or post_url
    if not post_actual_url:
        if source_id.startswith("facebook:"):
            fb_handle = source_id.replace("facebook:", "")
            matched_fb = next((acc.get("url") for acc in fb_accounts if acc.get("handle") == fb_handle), None)
            post_actual_url = matched_fb if matched_fb else f"https://www.facebook.com/{fb_handle}"
        elif source_id.startswith("threads:"):
            th_handle = source_id.replace("threads:", "")
            post_actual_url = f"https://www.threads.com/@{th_handle}"
        else:
            post_actual_url = ""

    card = {
        "id": card_id,
        "date": date_str,
        "dateFormatted": date_formatted,
        "daysAway": days_away,
        "time": proposal.get("time", "未公布"),
        "troupe": troupe,
        "genre": proposal.get("genre", "歌仔戲"),
        "artist": proposal.get("artist", "未公布"),
        "title": title,
        "category": category,
        "badgeType": badge_type,
        "verifyStatus": "community",
        "verifyLabel": "📣 社群公告（程式比對原文）",
        "location": location,
        "region": region,
        "status": status,
        "description": description,
        "link": post_actual_url,
        "sourceUrl": post_actual_url,
        "tags": [troupe],
    }
    if end_date_str:
        card["endDate"] = end_date_str
    if source_id.startswith("opentix:"):
        # 售票頁屬官方來源；只證明頁面實際列出的欄位
        card["verifyStatus"] = "verified"
        card["verifyLabel"] = "🎫 OPENTIX 售票頁（程式比對頁面資料）"
        card["description"] = f"依 OPENTIX 售票頁：「{quote_clip}」"
        card["status"] = "依售票頁資料；未列事項請查售票頁"
    if proposal.get("sessions"):
        card["sessions"] = proposal["sessions"]
        if proposal.get("noShowDates"):
            card["noShowDates"] = sorted(proposal["noShowDates"])

    schedule.append(card)
    # 重新計算 daysAway 並排序
    validate_schedule(schedule)
    atomic_save_json(schedule_path, schedule)

    out = {"result": "added", "id": card_id, "reasons": []}
    print(json.dumps(out, ensure_ascii=False))
    return 0


def handle_update(args, today: date):
    target_id = args.update
    proposal_path = Path(args.proposal)
    evidence_dir = Path(args.evidence_dir)
    schedule_path = Path(args.schedule)
    review_queue_path = Path(args.review_queue)

    proposal = json.loads(proposal_path.read_text(encoding="utf-8"))
    schedule = json.loads(schedule_path.read_text(encoding="utf-8")) if schedule_path.exists() else []

    target_card = next((c for c in schedule if c["id"] == target_id), None)
    if not target_card:
        reasons = ["card-not-found"]
        append_to_review_queue(review_queue_path, proposal, reasons)
        print(json.dumps({"result": "rejected", "id": target_id, "reasons": reasons}, ensure_ascii=False))
        return 1

    source = proposal.get("source", "")
    post_key = proposal.get("postKey", "")
    post_url = proposal.get("postUrl", "")
    post = load_post_from_evidence(evidence_dir, source=source, post_key=post_key, post_url=post_url)
    if not post:
        reasons = ["post-not-found"]
        append_to_review_queue(review_queue_path, proposal, reasons)
        print(json.dumps({"result": "rejected", "id": target_id, "reasons": reasons}, ensure_ascii=False))
        return 1

    reasons = []
    norm_quote = normalize_whitespace(proposal.get("quote", ""))
    norm_text = post_corpus(post)

    # 1. quote 必須在 post text 內
    if not norm_quote or norm_quote not in norm_text:
        reasons.append("quote-not-in-post")

    # 4. time 比對
    new_time = proposal.get("time")
    if new_time and not match_time_in_quote(new_time, norm_quote):
        reasons.append("time-not-in-quote")

    # 5. location 比對
    new_loc = proposal.get("location")
    if new_loc and not match_location_in_quote(new_loc, norm_quote):
        reasons.append("location-not-in-quote")

    if "sessions" in proposal:
        apply_sessions_to_proposal(proposal)
        reasons.extend(validate_sessions(proposal["sessions"], proposal.get("noShowDates"), norm_quote))
        for field in ("date", "endDate"):
            if proposal.get(field) and proposal[field] != target_card.get(field, target_card["date"] if field == "endDate" else None):
                reasons.append("sessions-change-dates")
                break

    # 檢查是否試圖覆寫已有明確值的欄位
    for field in ("location", "time", "artist", "troupe", "title"):
        if field in proposal and proposal[field] is not None:
            old_val = str(target_card.get(field, ""))
            proposed_val = str(proposal[field])
            # 如果新值不同於舊值
            if proposed_val != old_val:
                # 只有當舊值包含「未公布」「未列」「待確認」等字眼時才允許更新
                if not any(k in old_val for k in UNSPECIFIED_KEYWORDS):
                    reasons.append("would-overwrite")
                    break

    if reasons:
        append_to_review_queue(review_queue_path, proposal, reasons)
        print(json.dumps({"result": "rejected", "id": target_id, "reasons": reasons}, ensure_ascii=False))
        return 1

    # 通過，更新欄位
    for field in ("location", "time", "artist", "troupe", "title"):
        if field in proposal and proposal[field] is not None:
            old_val = str(target_card.get(field, ""))
            if any(k in old_val for k in UNSPECIFIED_KEYWORDS):
                target_card[field] = proposal[field]
                if field == "location":
                    target_card["region"] = infer_region(proposal[field])

    if proposal.get("sessions") and any(k in str(target_card.get("time", "")) for k in UNSPECIFIED_KEYWORDS + (proposal["time"],)):
        target_card["sessions"] = proposal["sessions"]
        target_card["time"] = proposal["time"]
        target_card["dateFormatted"] = proposal.get("dateFormatted", target_card.get("dateFormatted"))

    # 原 sourceUrl 移到 relatedSourceUrls
    old_source = target_card.get("sourceUrl")
    if "relatedSourceUrls" not in target_card:
        target_card["relatedSourceUrls"] = []
    if old_source and old_source not in target_card["relatedSourceUrls"]:
        target_card["relatedSourceUrls"].append(old_source)
    target_card["sourceUrl"] = post_url

    validate_schedule(schedule)
    atomic_save_json(schedule_path, schedule)
    print(json.dumps({"result": "updated", "id": target_id, "reasons": []}, ensure_ascii=False))
    return 0


def handle_change(args, today: date):
    target_id = args.change
    proposal_path = Path(args.proposal)
    evidence_dir = Path(args.evidence_dir)
    schedule_path = Path(args.schedule)
    review_queue_path = Path(args.review_queue)
    fb_accounts_path = Path(args.facebook_accounts)

    proposal = json.loads(proposal_path.read_text(encoding="utf-8"))
    schedule = json.loads(schedule_path.read_text(encoding="utf-8")) if schedule_path.exists() else []
    fb_accounts = json.loads(fb_accounts_path.read_text(encoding="utf-8")) if fb_accounts_path.exists() else []

    target_card = next((c for c in schedule if c["id"] == target_id), None)
    if not target_card:
        reasons = ["card-not-found"]
        append_to_review_queue(review_queue_path, proposal, reasons)
        print(json.dumps({"result": "rejected", "id": target_id, "reasons": reasons}, ensure_ascii=False))
        return 1

    source = proposal.get("source", "")
    post_key = proposal.get("postKey", "")
    post_url = proposal.get("postUrl", "")
    post = load_post_from_evidence(evidence_dir, source=source, post_key=post_key, post_url=post_url)
    if not post:
        reasons = ["post-not-found"]
        append_to_review_queue(review_queue_path, proposal, reasons)
        print(json.dumps({"result": "rejected", "id": target_id, "reasons": reasons}, ensure_ascii=False))
        return 1

    reasons = []
    # 1. 同帳號檢查
    card_source = target_card.get("sourceUrl") or target_card.get("link", "")
    if extract_account_id(card_source) != extract_account_id(post_url):
        reasons.append("different-account")

    norm_quote = normalize_whitespace(proposal.get("quote", ""))
    norm_text = post_corpus(post)

    # 2. quote 必須含「異動」「更正」「更改」「延期」「改期」「改至」「改在」之一
    if not any(k in norm_quote for k in ("異動", "更正", "更改", "延期", "改期", "改至", "改在")):
        reasons.append("no-change-keyword")

    if "sessions" in proposal:
        apply_sessions_to_proposal(proposal)
        reasons.extend(validate_sessions(proposal["sessions"], proposal.get("noShowDates"), norm_quote))

    # 3. quote 在 post text 內
    if not norm_quote or norm_quote not in norm_text:
        reasons.append("quote-not-in-post")

    # 新值比對
    old_summary_parts = []
    if "date" in proposal and proposal["date"] != target_card["date"]:
        try:
            d = parse_date(proposal["date"])
            if not match_date_in_quote(d, norm_quote):
                reasons.append("date-not-in-quote")
            old_summary_parts.append(f"舊日期：{target_card['date']}")
        except Exception:
            reasons.append("invalid-date-format")

    if "time" in proposal and proposal["time"] != target_card.get("time"):
        if not match_time_in_quote(proposal["time"], norm_quote):
            reasons.append("time-not-in-quote")
        old_summary_parts.append(f"舊時間：{target_card.get('time')}")

    if "location" in proposal and proposal["location"] != target_card.get("location"):
        if not match_location_in_quote(proposal["location"], norm_quote):
            reasons.append("location-not-in-quote")
        old_summary_parts.append(f"舊地點：{target_card.get('location')}")

    if reasons:
        append_to_review_queue(review_queue_path, proposal, reasons)
        print(json.dumps({"result": "rejected", "id": target_id, "reasons": reasons}, ensure_ascii=False))
        return 1

    # 通過，更新值並在 description 留下舊值
    if "date" in proposal:
        target_card["date"] = proposal["date"]
        target_card["daysAway"] = max(0, (parse_date(proposal["date"]) - today).days)
        target_card["dateFormatted"] = proposal.get("dateFormatted") or proposal["date"].replace("-", "/")
    if proposal.get("sessions"):
        target_card["sessions"] = proposal["sessions"]
        if proposal.get("endDate"):
            target_card["endDate"] = proposal["endDate"]
        else:
            target_card.pop("endDate", None)
        if proposal.get("noShowDates"):
            target_card["noShowDates"] = sorted(proposal["noShowDates"])
    if "time" in proposal:
        target_card["time"] = proposal["time"]
    if "location" in proposal:
        target_card["location"] = proposal["location"]
        target_card["region"] = infer_region(proposal["location"])

    change_date_str = str(post.get("datetime") or today.isoformat())[:10]
    old_details = "／".join(old_summary_parts) if old_summary_parts else "原公告內容"
    target_card["description"] = (
        target_card.get("description", "").rstrip()
        + f"（原公告：{old_details}，{change_date_str} 依同帳號異動公告更正）"
    )

    validate_schedule(schedule)
    atomic_save_json(schedule_path, schedule)
    print(json.dumps({"result": "changed", "id": target_id, "reasons": []}, ensure_ascii=False))
    return 0


def handle_cancel(args, today: date):
    target_id = args.cancel
    proposal_path = Path(args.proposal)
    evidence_dir = Path(args.evidence_dir)
    schedule_path = Path(args.schedule)
    review_queue_path = Path(args.review_queue)
    cancelled_path = Path(args.cancelled)

    proposal = json.loads(proposal_path.read_text(encoding="utf-8"))
    schedule = json.loads(schedule_path.read_text(encoding="utf-8")) if schedule_path.exists() else []

    target_card = next((c for c in schedule if c["id"] == target_id), None)
    if not target_card:
        reasons = ["card-not-found"]
        append_to_review_queue(review_queue_path, proposal, reasons)
        print(json.dumps({"result": "rejected", "id": target_id, "reasons": reasons}, ensure_ascii=False))
        return 1

    source = proposal.get("source", "")
    post_key = proposal.get("postKey", "")
    post_url = proposal.get("postUrl", "")
    post = load_post_from_evidence(evidence_dir, source=source, post_key=post_key, post_url=post_url)
    if not post:
        reasons = ["post-not-found"]
        append_to_review_queue(review_queue_path, proposal, reasons)
        print(json.dumps({"result": "rejected", "id": target_id, "reasons": reasons}, ensure_ascii=False))
        return 1

    reasons = []
    # 1. 同帳號檢查
    card_source = target_card.get("sourceUrl") or target_card.get("link", "")
    if extract_account_id(card_source) != extract_account_id(post_url):
        reasons.append("different-account")

    norm_quote = normalize_whitespace(proposal.get("quote", ""))
    norm_text = post_corpus(post)

    if not norm_quote or norm_quote not in norm_text:
        reasons.append("quote-not-in-post")

    # 2. quote 必須含「取消」「停演」「暫停演出」之一
    if not any(k in norm_quote for k in ("取消", "停演", "暫停演出")):
        reasons.append("no-cancel-keyword")

    # 必須包含該卡的日期
    try:
        card_d = parse_date(target_card["date"])
        if not match_date_in_quote(card_d, norm_quote):
            reasons.append("date-not-in-quote")
    except Exception:
        reasons.append("card-date-invalid")

    if reasons:
        append_to_review_queue(review_queue_path, proposal, reasons)
        print(json.dumps({"result": "rejected", "id": target_id, "reasons": reasons}, ensure_ascii=False))
        return 1

    # 通過，從 schedule 移除，並 append 到 cancelled_cards.jsonl
    schedule = [c for c in schedule if c["id"] != target_id]
    append_to_cancelled_file(cancelled_path, target_card, proposal.get("quote", ""), post_url)
    validate_schedule(schedule)
    atomic_save_json(schedule_path, schedule)

    print(json.dumps({"result": "cancelled", "id": target_id, "reasons": []}, ensure_ascii=False))
    return 0


def handle_from_moc(args, today: date):
    title_query = args.from_moc.strip()
    schedule_path = Path(args.schedule)
    review_queue_path = Path(args.review_queue)

    # 排除關鍵字檢查
    if any(k in title_query for k in ("展", "講座", "工作坊", "研習", "徵選", "課程")):
        reasons = ["not-performance"]
        proposal = {"fromMoc": title_query}
        append_to_review_queue(review_queue_path, proposal, reasons)
        print(json.dumps({"result": "rejected", "id": None, "reasons": reasons}, ensure_ascii=False))
        return 1

    # 讀取文化部資料
    culture_path = Path(args.culture_records) if args.culture_records else DEFAULT_MOC_RECORDS_PATH
    if not culture_path.exists():
        reasons = ["moc-records-stale"]
        proposal = {"fromMoc": title_query}
        append_to_review_queue(review_queue_path, proposal, reasons)
        print(json.dumps({"result": "rejected", "id": None, "reasons": reasons}, ensure_ascii=False))
        return 1

    try:
        raw_payload = json.loads(culture_path.read_text(encoding="utf-8"))
    except Exception:
        reasons = ["moc-records-stale"]
        append_to_review_queue(review_queue_path, {"fromMoc": title_query}, reasons)
        print(json.dumps({"result": "rejected", "id": None, "reasons": reasons}, ensure_ascii=False))
        return 1

    if isinstance(raw_payload, dict):
        fetched_at_str = raw_payload.get("fetchedAt")
        if fetched_at_str:
            try:
                f_dt = datetime.fromisoformat(fetched_at_str)
                now_dt = datetime.now(ZoneInfo("Asia/Taipei"))
                if f_dt.tzinfo is None:
                    f_dt = f_dt.replace(tzinfo=ZoneInfo("Asia/Taipei"))
                if (now_dt - f_dt).total_seconds() > 36 * 3600:
                    reasons = ["moc-records-stale"]
                    append_to_review_queue(review_queue_path, {"fromMoc": title_query}, reasons)
                    print(json.dumps({"result": "rejected", "id": None, "reasons": reasons}, ensure_ascii=False))
                    return 1
            except Exception:
                pass
        records = raw_payload.get("records", [])
    elif isinstance(raw_payload, list):
        records = raw_payload
    else:
        records = []

    # 尋找匹配紀錄
    target_record = None
    for r in records:
        if isinstance(r, dict) and (r.get("title", "").strip() == title_query or title_query in r.get("title", "")):
            target_record = r
            break

    if not target_record:
        reasons = ["moc-record-not-found"]
        append_to_review_queue(review_queue_path, {"fromMoc": title_query}, reasons)
        print(json.dumps({"result": "rejected", "id": None, "reasons": reasons}, ensure_ascii=False))
        return 1

    record_title = target_record.get("title", "").strip()
    if any(k in record_title for k in ("展", "講座", "工作坊", "研習", "徵選", "課程")):
        reasons = ["not-performance"]
        append_to_review_queue(review_queue_path, {"fromMoc": title_query}, reasons)
        print(json.dumps({"result": "rejected", "id": None, "reasons": reasons}, ensure_ascii=False))
        return 1

    schedule = json.loads(schedule_path.read_text(encoding="utf-8")) if schedule_path.exists() else []

    # 依 locationName 分組
    raw_shows = target_record.get("showInfo")
    shows = raw_shows if isinstance(raw_shows, list) and raw_shows else [{}]

    venues = {}
    for s in shows:
        vname = s.get("locationName") or s.get("location") or "文化部活動場地"
        venues.setdefault(vname, []).append(s)

    created_ids = []
    # 推導劇種
    troupe = next((target_record[k].strip() for k in ("masterUnit", "otherUnit", "showUnit")
                   if isinstance(target_record.get(k), str) and target_record[k].strip()), "文化部演出團隊")
    desc_full = f"{record_title} {troupe} {target_record.get('descriptionFilterHtml', '')}"
    if any(w in desc_full for w in ("布袋", "掌中", "偶戲", "偶劇", "傀儡")):
        genre = "布袋戲"
    elif any(w in desc_full for w in ("唸歌", "跨界", "音樂會")):
        genre = "其他歌仔戲"
    else:
        genre = "歌仔戲"

    for venue_name, vshows in venues.items():
        # 計算此場館所有場次的日期
        show_dates = []
        show_times = []
        price_val = None
        for s in vshows:
            raw_time_str = str(s.get("time") or target_record.get("startDate", ""))
            # 格式可能為 2026/12/05 15:00 或 2026-12-05
            clean_date_match = re.search(r"(\d{4}[-/]\d{1,2}[-/]\d{1,2})", raw_time_str)
            if clean_date_match:
                d_str = clean_date_match.group(1).replace("/", "-")
                try:
                    show_dates.append(parse_date(d_str))
                except Exception:
                    pass
            time_part_match = re.search(r"\d{1,2}:\d{2}", raw_time_str)
            if time_part_match:
                show_times.append(time_part_match.group(0))
            if not price_val and s.get("price"):
                price_val = s.get("price")

        if not show_dates:
            continue

        min_d = min(show_dates)
        max_d = max(show_dates)
        card_date = min_d.isoformat()
        card_end_date = max_d.isoformat() if max_d > min_d else None

        # 時間整理
        unique_times = sorted(set(show_times))
        if len(unique_times) == 1:
            card_time = unique_times[0]
        elif len(vshows) > 1 and all(s.get("time") for s in vshows):
            # 若每場都有完整時間，列出場次時間
            card_time = "、".join(str(s.get("time")) for s in vshows)
        else:
            card_time = "、".join(unique_times) if unique_times else "時間請查官方公告"

        # 地點：locationName 加括號內的 location
        addr = next((s.get("location") for s in vshows if s.get("location") and s.get("location") != venue_name), None)
        full_location = f"{venue_name}（{addr}）" if addr else venue_name

        # link
        link = (
            next((s.get("webSales") for s in vshows if s.get("webSales")), None)
            or target_record.get("webSales")
            or target_record.get("sourceWebPromote")
            or "https://cloud.culture.tw/"
        )

        # ID 計算：moc-<OPENTIX編號或標題雜湊>-<場館雜湊>
        opt_id = None
        opt_match = re.search(r"opentix\.life/(?:event|program)/(\d+)", link)
        if opt_match:
            opt_id = opt_match.group(1)
        base_hash = opt_id if opt_id else hashlib.sha256(record_title.encode("utf-8")).hexdigest()[:8]
        venue_hash = hashlib.sha256(venue_name.encode("utf-8")).hexdigest()[:6]
        card_id = f"moc-{base_hash}-{venue_hash}"

        # 重複檢查（第 8 條：同日期區間＋同場館，並比對 OPENTIX 編號）
        is_dup = False
        card_start = min_d
        card_end = max_d
        for exist_card in schedule:
            try:
                e_start = parse_date(exist_card["date"])
                e_end = parse_date(exist_card.get("endDate", exist_card["date"]))
            except Exception:
                continue
            # OPENTIX ID 相同
            e_opt = opentix_program_id(exist_card)
            if opt_id and e_opt and opt_id == e_opt:
                # 若同場館則重複
                if venue_name in exist_card.get("location", ""):
                    is_dup = True
                    break
            # 同日期區間重疊且同場館
            if not (e_end < card_start or e_start > card_end):
                if venue_name in exist_card.get("location", ""):
                    is_dup = True
                    break

        if is_dup:
            continue

        shows_summary = "、".join(str(s.get("time") or "") for s in vshows if s.get("time"))
        description = f"文化部開放資料：{record_title}；{venue_name}；{shows_summary if shows_summary else card_date}"
        status_text = f"票價：{price_val}" if price_val else "文化部開放資料"

        date_formatted = f"{card_date.replace('-', '/')}–{card_end_date.replace('-', '/')}" if card_end_date else card_date.replace("-", "/")
        days_away = max(0, (min_d - today).days)

        new_card = {
            "id": card_id,
            "date": card_date,
            "dateFormatted": date_formatted,
            "daysAway": days_away,
            "time": card_time,
            "troupe": troupe,
            "genre": genre,
            "artist": troupe,
            "title": record_title,
            "category": "售票演出",
            "badgeType": "ticket",
            "verifyStatus": "verified",
            "verifyLabel": "🛡️ 文化部開放資料",
            "location": full_location,
            "region": infer_region(full_location),
            "status": status_text,
            "description": description,
            "link": link,
            "sourceUrl": link,
            "tags": [troupe, genre],
        }
        if card_end_date:
            new_card["endDate"] = card_end_date

        schedule.append(new_card)
        created_ids.append(card_id)

    if created_ids:
        validate_schedule(schedule)
        atomic_save_json(schedule_path, schedule)
        print(json.dumps({"result": "added", "ids": created_ids, "count": len(created_ids), "reasons": []}, ensure_ascii=False))
        return 0
    else:
        reasons = ["duplicate-or-no-valid-shows"]
        print(json.dumps({"result": "rejected", "id": None, "reasons": reasons}, ensure_ascii=False))
        return 1


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--proposal", help="提案 JSON 檔案路徑")
    parser.add_argument("--evidence-dir", help="巡檢證據目錄")
    parser.add_argument("--update", help="更新既有卡片 ID")
    parser.add_argument("--change", help="異動既有卡片 ID")
    parser.add_argument("--cancel", help="取消既有卡片 ID")
    parser.add_argument("--from-moc", help="依文化部活動標題建卡")
    parser.add_argument("--culture-records", help="測試或離線用文化部紀錄 JSON 檔案")
    parser.add_argument("--schedule", default=str(DEFAULT_SCHEDULE_PATH), help="schedule.json 路徑")
    parser.add_argument("--review-queue", default=str(DEFAULT_REVIEW_QUEUE_PATH), help="review_queue.json 路徑")
    parser.add_argument("--cancelled", default=str(DEFAULT_CANCELLED_PATH), help="cancelled_cards.jsonl 路徑")
    parser.add_argument("--facebook-accounts", default=str(DEFAULT_FB_ACCOUNTS_PATH), help="facebook_accounts.json 路徑")
    parser.add_argument("--today", help="覆寫今日日期 YYYY-MM-DD（測試用）")

    args = parser.parse_args()

    today = parse_date(args.today) if args.today else datetime.now(ZoneInfo("Asia/Taipei")).date()

    if args.from_moc:
        sys.exit(handle_from_moc(args, today))
    elif args.update:
        if not args.proposal or not args.evidence_dir:
            parser.error("--update 必須同時指定 --proposal 與 --evidence-dir")
        sys.exit(handle_update(args, today))
    elif args.change:
        if not args.proposal or not args.evidence_dir:
            parser.error("--change 必須同時指定 --proposal 與 --evidence-dir")
        sys.exit(handle_change(args, today))
    elif args.cancel:
        if not args.proposal or not args.evidence_dir:
            parser.error("--cancel 必須同時指定 --proposal 與 --evidence-dir")
        sys.exit(handle_cancel(args, today))
    elif args.proposal:
        if not args.evidence_dir:
            parser.error("提案建卡必須同時指定 --evidence-dir")
        sys.exit(handle_proposal(args, today))
    else:
        parser.print_help()
        sys.exit(1)


if __name__ == "__main__":
    main()
