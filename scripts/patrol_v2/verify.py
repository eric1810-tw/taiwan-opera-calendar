"""查證：判讀後還不能確定的項目（舊稱「待查」），交給質疑者找第二來源佐證。

質疑者只能交「佐證網址＋逐字引文＋事件」；程式自己重抓網址、把頁面當成一篇新來源，
用跟判讀一樣的 validate_batch 檢查（引文逐字在頁面上、日期時間在引文內、劇種、重複卡…）。
過了才變成變更提案，照常送審查與 add_card；查不到或過不了的只計數，不列清單。
"""
import hashlib
import html
import re
import ssl
import urllib.request
from urllib.parse import urlparse

from .common import text_revision
from .validate import dedupe_within_run, validate_batch

BATCH_SIZE = 8
SOCIAL_HOSTS = ("facebook.com", "fb.com", "fb.watch", "threads.com", "threads.net", "instagram.com")
UA = "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/130 Safari/537.36"


def is_social(url):
    host = (urlparse(url).hostname or "").lower()
    return any(host == h or host.endswith("." + h) for h in SOCIAL_HOSTS)


def html_to_text(raw):
    raw = re.sub(r"(?is)<(script|style|noscript)[^>]*>.*?</\1>", " ", raw)
    raw = re.sub(r"(?s)<[^>]+>", " ", raw)
    return re.sub(r"\s+", " ", html.unescape(raw)).strip()


def _ssl_context():
    # 照常驗憑證；只關掉 Python 3.13+ 的 X509 嚴格模式（不少政府網站憑證缺 Subject Key Identifier 會被擋）
    ctx = ssl.create_default_context()
    ctx.verify_flags &= ~getattr(ssl, "VERIFY_X509_STRICT", 0)
    return ctx


def fetch_page_text(url, timeout=20):
    req = urllib.request.Request(url, headers={"User-Agent": UA, "Accept-Language": "zh-TW,zh;q=0.9"})
    with urllib.request.urlopen(req, timeout=timeout, context=_ssl_context()) as res:
        charset = res.headers.get_content_charset() or "utf-8"
        return html_to_text(res.read(3_000_000).decode(charset, errors="replace"))


def build_batches(candidates, items, cards, image_reading):
    """candidates：check.json 的 needsCheck；image_reading(sha) 回傳已存的海報判讀"""
    rows = []
    for n, c in enumerate(candidates, 1):
        it = items.get(c["postKey"], {})
        proposed = c.get("proposed") if isinstance(c.get("proposed"), dict) else None
        target = (proposed or {}).get("targetCardId") or c.get("targetCardId")
        rows.append({
            "verifyId": f"v-{n:03d}", "postKey": c["postKey"], "url": c.get("url") or it.get("url"),
            "whyUnsure": c.get("reason"), "judgeNote": c.get("detail") or c.get("notes"),
            "proposed": proposed, "currentCard": cards.get(target) if target else None,
            "source": {"datetime": it.get("datetime"), "text": it.get("text"),
                       "imageReadings": [r for r in (image_reading(m["sha256"]) for m in it.get("media") or [] if m.get("sha256")) if r]},
        })
    return [rows[i:i + BATCH_SIZE] for i in range(0, len(rows), BATCH_SIZE)]


def corroboration_item(url, text):
    key = "verify:" + hashlib.sha256(url.encode()).hexdigest()[:12]
    return {"postKey": key, "source": "verify", "url": url, "datetime": None, "text": text,
            "images": [], "knownImageReadings": [], "revision": text_revision(text, [])}


def process(verdicts, candidates_by_id, schedule, today, fetch=None):
    """回傳 {"accepted": 變更提案, "confirmed": 佐證顯示卡片本來就對, "unverified": 查無佐證, "items": 新增的佐證來源}"""
    out = {"accepted": [], "confirmed": [], "unverified": [], "items": []}
    fetch = fetch or fetch_page_text
    pages = {}
    answered = set()
    for v in verdicts:
        vid = v.get("verifyId")
        cand = candidates_by_id.get(vid)
        if not cand or vid in answered:
            continue
        answered.add(vid)
        base = {"verifyId": vid, "postKey": cand["postKey"], "url": cand.get("url"), "whyUnsure": cand.get("whyUnsure")}
        if v.get("result") != "confirmed":
            out["unverified"].append({**base, "reason": "no-corroboration", "detail": v.get("reason")})
            continue
        corr = v.get("corroboration") or {}
        url = corr.get("url") or ""
        # 一個佐證頁面可以列多場（events）；每場可有自己的 quote，沒寫就用 corroboration.quote
        events = v.get("events") if isinstance(v.get("events"), list) else ([v["event"]] if isinstance(v.get("event"), dict) else [])
        events = [e for e in events if isinstance(e, dict)]
        if not url.startswith(("http://", "https://")) or is_social(url):
            out["unverified"].append({**base, "reason": "corroboration-url-not-fetchable", "detail": url})
            continue
        if not events:
            out["unverified"].append({**base, "reason": "event-missing"})
            continue
        if url not in pages:
            try:
                pages[url] = fetch(url)
            except Exception as error:  # 抓不到就算沒查到
                pages[url] = None
                out["unverified"].append({**base, "reason": "corroboration-fetch-failed", "detail": f"{url}：{error}"})
                continue
        if pages[url] is None:
            out["unverified"].append({**base, "reason": "corroboration-fetch-failed", "detail": url})
            continue
        item = corroboration_item(url, pages[url])
        events = [{**e, "quote": e.get("quote") or corr.get("quote", "")} for e in events]
        res = validate_batch({"items": [item]}, {"dispositions": [{"postKey": item["postKey"], "revision": item["revision"],
                                                                     "decision": "new", "events": events}]}, schedule, today)
        for change in res["accepted"]:
            out["accepted"].append({**change, "verifiedFrom": {"verifyId": vid, "postKey": cand["postKey"], "url": cand.get("url")}})
        if res["accepted"] and item["postKey"] not in {i["postKey"] for i in out["items"]}:
            out["items"].append(item)
        for c in res["confirmed"]:
            out["confirmed"].append({**base, "targetCardId": c["targetCardId"], "detail": url})
        failed = [x for k in ("needsCheck", "rejected", "expired", "farFuture") for x in res[k]]
        if failed:
            why = ",".join(dict.fromkeys(filter(None, (x.get("reason") for x in failed))))
            out["unverified"].append({**base, "reason": "corroboration-failed-check", "detail": f"{url}：{len(failed)} 場未過（{why}）"})
    # 兩則待查講同一場（例如兩個帳號轉貼）：同一張卡只改一次，其餘當補充來源
    merged = {"accepted": out["accepted"]}
    dedupe_within_run(merged)
    out["accepted"] = merged["accepted"]
    for vid, cand in candidates_by_id.items():
        if vid not in answered:
            out["unverified"].append({"verifyId": vid, "postKey": cand["postKey"], "url": cand.get("url"),
                                      "whyUnsure": cand.get("whyUnsure"), "reason": "verifier-no-answer"})
    return out
