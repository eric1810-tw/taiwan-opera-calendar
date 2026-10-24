"""非社群來源：OPENTIX（sitemap＋活動頁 JSON-LD）、文化部（moc_records.json）、GitHub Issues。

都不開瀏覽器、不需登入。回傳的 item 會寫成與社群相同格式的證據檔（posts[]），
讓 add_card 能用同一套「原文必須在證據內」的規則驗證。
"""
import html
import json
import re
import subprocess
import time
import urllib.request
import xml.etree.ElementTree as ET
from datetime import datetime, timedelta

from .common import ROOT, normalize_text, read_json, sha256_bytes, write_json

UA = "TaiwanOperaCalendar-patrol/2.0 (+https://eric1810-tw.github.io/taiwan-opera-calendar/)"
OPENTIX_SITEMAP = "https://www.opentix.life/otWebSitemap.xml"
OPERA_KEYWORDS = ("歌仔戲", "歌仔", "布袋戲", "掌中戲", "掌中劇", "金光", "野台戲", "外台戲", "薪傳獎", "戲曲")
REPO = "eric1810-tw/taiwan-opera-calendar"


def http_get(url, timeout=30, retries=2):
    last = None
    for attempt in range(retries + 1):
        try:
            request = urllib.request.Request(url, headers={"User-Agent": UA})
            with urllib.request.urlopen(request, timeout=timeout) as response:
                return response.read()
        except Exception as error:  # 網路錯誤一律重試，最後拋出
            last = error
            if attempt < retries:
                time.sleep(3 * (attempt + 1))
    raise RuntimeError(f"讀取失敗 {url}：{last}")


# --- OPENTIX ---

def parse_sitemap(xml_bytes):
    ns = {"s": "http://www.sitemaps.org/schemas/sitemap/0.9"}
    root = ET.fromstring(xml_bytes)
    result = {}
    for url in root.findall("s:url", ns):
        loc = (url.findtext("s:loc", default="", namespaces=ns) or "").strip()
        m = re.match(r"https://www\.opentix\.life/event/(\d+)$", loc)
        if m:
            result[m.group(1)] = (url.findtext("s:lastmod", default="", namespaces=ns) or "").strip()
    return result


def parse_event_page(page_html):
    """取活動頁所有 schema.org Event；回傳 {name, description, organizers, sessions:[{start,end,place,address}]}"""
    events = []
    for block in re.findall(r'<script[^>]*type="application/ld\+json"[^>]*>(.*?)</script>', page_html, re.S):
        try:
            data = json.loads(block)
        except Exception:
            continue
        for item in data if isinstance(data, list) else [data]:
            if isinstance(item, dict) and item.get("@type") == "Event":
                events.append(item)
    if not events:
        return None
    first = events[0]
    sessions = []
    for ev in events:
        loc = ev.get("location") or {}
        addr = loc.get("address") or {}
        sessions.append({
            "start": ev.get("startDate"),
            "end": ev.get("endDate"),
            "place": loc.get("name"),
            "address": " ".join(x for x in (addr.get("addressLocality"), addr.get("streetAddress")) if x),
            "status": ev.get("eventStatus"),
        })
    organizers = [o.get("name") for o in (first.get("organizer") or []) if isinstance(o, dict) and o.get("name")]
    offers = first.get("offers") or {}
    prices = [offers.get(k) for k in ("lowPrice", "highPrice", "price") if isinstance(offers, dict) and offers.get(k) not in (None, "")]
    return {
        "prices": prices,
        "name": html.unescape(first.get("name") or ""),
        "description": html.unescape(re.sub(r"&nbsp;|\s+", " ", first.get("description") or "")).strip(),
        "organizers": organizers,
        "sessions": sessions,
    }


def opentix_text(info):
    """把 JSON-LD 攤平成可引用的正文（add_card 以此比對原文）"""
    lines = [f"節目：{info['name']}", f"主辦：{'、'.join(info['organizers']) or '未列'}", "售票：OPENTIX 售票頁"]
    if info.get("prices"):
        lines.append("票價：" + "～".join(f"{p}元" for p in dict.fromkeys(info["prices"])))
    for s in info["sessions"]:
        start = (s.get("start") or "").replace("T", " ")[:16]
        lines.append(f"場次：{start}｜地點：{s.get('place') or '未列'}（{s.get('address') or '未列'}）")
    lines.append(f"簡介：{info['description']}")
    return "\n".join(lines)


def is_opera_related(info):
    text = f"{info.get('name', '')} {info.get('description', '')} {' '.join(info.get('organizers', []))}"
    return any(k in text for k in OPERA_KEYWORDS)


def collect_opentix(cache_path, fetch=http_get, max_pages=250, delay=0.4, today=None):
    """只抓 lastmod 有變的活動頁；回傳 (items, stats)。cache：{eventId: {lastmod, related, info}}"""
    cache = read_json(cache_path, {}) or {}
    sitemap = parse_sitemap(fetch(OPENTIX_SITEMAP))
    changed = [eid for eid, lastmod in sitemap.items() if cache.get(eid, {}).get("lastmod") != lastmod]
    stats = {"sitemapEvents": len(sitemap), "changed": len(changed), "fetched": 0, "errors": 0, "related": 0, "deferred": 0}
    for eid in changed[:max_pages]:
        try:
            info = parse_event_page(fetch(f"https://www.opentix.life/event/{eid}").decode("utf-8", "replace"))
            stats["fetched"] += 1
        except Exception:
            stats["errors"] += 1
            continue
        cache[eid] = {"lastmod": sitemap[eid], "related": bool(info and is_opera_related(info)), "info": info if info and is_opera_related(info) else None}
        if stats["fetched"] % 50 == 0:
            write_json(cache_path, cache)  # 中途存檔，中斷後不必重抓
        time.sleep(delay)
    stats["deferred"] = max(0, len(changed) - max_pages)
    write_json(cache_path, cache)
    today = today or datetime.now().date().isoformat()
    items = []
    for eid, entry in cache.items():
        info = entry.get("info")
        if not entry.get("related") or not info:
            continue
        if not any((s.get("start") or "")[:10] >= today for s in info["sessions"]):
            continue
        stats["related"] += 1
        text = opentix_text(info)
        items.append({
            "source": f"opentix:{eid}",
            "postKey": f"opentix:{eid}",
            "url": f"https://www.opentix.life/event/{eid}",
            "datetime": entry.get("lastmod"),
            "text": text,
            "images": [],
            "changedThisRun": eid in changed,
        })
    return items, stats


# --- 文化部 ---

def collect_moc(records_path, now_dt, keyword_filter=None):
    data = read_json(records_path, {}) or {}
    records = data.get("records", []) if isinstance(data, dict) else []
    fetched_at = data.get("fetchedAt") if isinstance(data, dict) else None
    problems = []
    try:
        age = now_dt - datetime.fromisoformat(fetched_at)
        if age > timedelta(hours=36):
            problems.append(f"moc_records 已 {int(age.total_seconds() // 3600)} 小時未更新")
    except Exception:
        problems.append("moc_records 沒有有效 fetchedAt")
    total = data.get("total") if isinstance(data, dict) else None
    if not isinstance(total, int) or total < 500:
        problems.append(f"文化部總筆數 {total} 低於 500 門檻")
    items = []
    for r in records:
        if keyword_filter and not keyword_filter(r):
            continue
        shows = r.get("showInfo") or []
        lines = [f"活動：{r.get('title', '')}", f"主辦：{r.get('masterUnit') or r.get('showUnit') or '未列'}"]
        for s in shows[:20]:
            lines.append(f"場次：{s.get('time', '')}｜{s.get('locationName', '')}（{s.get('location', '')}）")
        lines.append(f"說明：{normalize_text(r.get('descriptionFilterHtml'))[:1500]}")
        text = "\n".join(lines)
        uid = r.get("UID") or sha256_bytes(r.get("title", "").encode())[:16]
        items.append({
            "source": "culture",
            "postKey": f"culture:{uid}",
            "url": r.get("sourceWebPromote") or r.get("webSales") or "https://cloud.culture.tw/",
            "datetime": r.get("editModifyDate"),
            "text": text,
            "images": [],
            "mocTitle": r.get("title", ""),
        })
    return items, {"fetchedAt": fetched_at, "total": total, "records": len(records), "problems": problems}


# --- GitHub Issues ---

def gh_json(args):
    result = subprocess.run(["gh", "api", *args], capture_output=True, text=True, timeout=60)
    if result.returncode != 0:
        raise RuntimeError(result.stderr.strip() or "gh api 失敗")
    return json.loads(result.stdout or "null")


def collect_issues(runner=gh_json):
    issues = runner([f"repos/{REPO}/issues?state=all&per_page=100&sort=updated&direction=desc"])
    items = []
    for issue in issues or []:
        if "pull_request" in issue:
            continue
        comments = []
        if issue.get("comments"):
            comments = runner([f"repos/{REPO}/issues/{issue['number']}/comments?per_page=100"]) or []
        body = [f"Issue #{issue['number']}（{issue.get('state')}）：{issue.get('title', '')}", normalize_text(issue.get("body"))]
        for c in comments:
            body.append(f"留言 {c.get('created_at', '')}：{normalize_text(c.get('body'))}")
        items.append({
            "source": "issues",
            "postKey": f"issues:{issue['number']}",
            "url": issue.get("html_url"),
            "datetime": issue.get("updated_at"),
            "text": "\n".join(body)[:6000],
            "images": [],
        })
    return items, {"issues": len(items)}
