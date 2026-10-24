"""驗證判讀子代理的提案。程式能檢查的一律由程式檢查，不信任模型自稱「一致」。

結果分三類：
- accepted：可進入第二次審查與寫入的卡片變更
- needsCheck：證據不足、衝突、跨帳號異動等，保留待查並列入報告
- rejected：格式或引用錯誤（例如引用的原文不在貼文內）
"""
import re
import sys
from datetime import date, timedelta

from .common import ROOT, normalize_text

sys.path.insert(0, str(ROOT / "scripts"))
import add_card  # noqa: E402

DECISIONS = {"new", "update", "change", "cancel", "already-listed", "out-of-scope", "not-event", "needs-check", "needs-images"}
ACTIONS = {"add", "update", "change", "cancel", "confirm"}
GENRES = {"歌仔戲", "布袋戲"}
EVENT_TYPES = {"演出", "講座", "體驗"}
KINDS = {"扮仙", "正戲", "其他"}
PAGER = re.compile(r"(?<![\d/])(?<!/ )(\d{1,2})\s+/\s+(\d{1,2})(?![\d/])(?!\s*/)")
TIME_RE = re.compile(r"^(?:[01]?\d|2[0-3]):[0-5]\d$")


def strip_pager(text):
    """Threads 圖片輪播的「1 / 2」「2 / 2」不是日期（頁碼一定是前數 ≤ 後數 ≤ 20）"""
    return PAGER.sub(lambda m: " " if int(m.group(1)) <= int(m.group(2)) <= 20 else m.group(0), text)


def corpus_for(item, readings):
    parts = [item.get("text", "")]
    for img in (item.get("images") or []) + (item.get("knownImageReadings") or []):
        r = readings.get(img["sha256"]) or ({"legible": True, "reading": img.get("reading")} if img.get("reading") else None)
        if r and r.get("legible") and r.get("reading"):
            parts.append(r["reading"])
    return normalize_text(" ".join(parts))


def main_location(loc):
    return re.sub(r"（[^）]*）|\([^)]*\)", "", loc or "").strip()


def norm_place(text):
    t = (text or "").replace("臺", "台").replace("巖", "岩").replace("嚴", "岩")
    return re.sub(r"[\s　()（）「」『』、，,・·\-–—:：。]", "", t)


def subseq_coverage(short, long):
    """short 的字依序出現在 long 裡的比例（容許地址、廳名、錯字等小差異）"""
    i = hit = 0
    for ch in short:
        j = long.find(ch, i)
        if j >= 0:
            hit += 1
            i = j + 1
    return hit / len(short) if short else 0.0


def place_parts(text):
    """「地址（場館）」拆成 [整串, 地址, 場館]，兩邊寫法前後顛倒也能比"""
    text = text or ""
    parts = [text, main_location(text)] + re.findall(r"[（(]([^）)]*)[）)]", text)
    return [p for p in parts if len(norm_place(p)) >= 4]


def same_place(a, b):
    na, nb = norm_place(a), norm_place(b)
    if not na or not nb:
        return False
    for pa in place_parts(a):
        for pb in place_parts(b):
            if _same(norm_place(pa), norm_place(pb)):
                return True
    return _same(na, nb)


def _same(na, nb):
    if not na or not nb:
        return False
    if na in nb or nb in na:
        return True
    short, long = (na, nb) if len(na) <= len(nb) else (nb, na)
    return subseq_coverage(short, long) >= 0.8


def card_dates(card):
    start = add_card.parse_date(card["date"])
    end = add_card.parse_date(card.get("endDate", card["date"]))
    no_show = set(card.get("noShowDates") or [])
    if card.get("sessions"):
        return sorted({s["date"] for s in card["sessions"]})
    out, d = [], start
    while d <= end:
        if d.isoformat() not in no_show:
            out.append(d.isoformat())
        d += timedelta(days=1)
    return out


def diff_against_card(event, card):
    """逐欄比對貼文所述與卡片；回傳差異清單（空＝真的一致）"""
    diffs = []
    sessions = event.get("sessions") or []
    post_dates = sorted({s["date"] for s in sessions})
    cdates = card_dates(card)
    if post_dates and not set(post_dates) <= set(cdates):
        diffs.append({"field": "date", "card": card.get("dateFormatted") or card["date"], "post": "、".join(post_dates)})
    card_time = str(card.get("time", ""))
    card_time_unknown = any(k in card_time for k in add_card.UNSPECIFIED_KEYWORDS) and not re.search(r"\d{1,2}[:：]\d{2}", card_time)
    for s in sessions:
        t = s.get("time", "未公布")
        if TIME_RE.match(t):
            if not add_card.match_time_in_quote(t, card_time.replace("：", ":")) and t not in card_time:
                diffs.append({"field": "time", "card": card_time, "post": f"{s['date']} {s.get('kind', '正戲')} {t}",
                              "fill": card_time_unknown})
    loc = event.get("location")
    if loc and not any(k in loc for k in add_card.UNSPECIFIED_KEYWORDS):
        card_loc = card.get("location") or ""
        if any(k in card_loc for k in add_card.UNSPECIFIED_KEYWORDS) or not main_location(card_loc):
            diffs.append({"field": "location", "card": card_loc, "post": loc, "fill": True})
        elif not same_place(loc, card_loc):
            diffs.append({"field": "location", "card": card_loc, "post": loc})
    return diffs


def check_sessions(event, quote, today, action, now_hm=None):
    reasons = []
    sessions = event.get("sessions")
    if not isinstance(sessions, list) or not sessions:
        return ["sessions-missing"]
    seen = set()
    q = strip_pager(quote)
    no_show = set(event.get("noShowDates") or [])
    for s in sessions:
        try:
            d = add_card.parse_date(s.get("date", ""))
        except Exception:
            reasons.append("invalid-date-format")
            continue
        if action != "cancel" and not (today <= d <= today + timedelta(days=120)):
            reasons.append("date-out-of-range")
        if action in ("add", "update") and now_hm and d == today and TIME_RE.match(s.get("time", "")) and s["time"].zfill(5) < now_hm:
            reasons.append("already-past")
        if not add_card.match_date_in_quote(d, q):
            reasons.append("date-not-in-quote")
        kind = s.get("kind", "正戲")
        if kind not in KINDS:
            reasons.append("session-kind-invalid")
        t = s.get("time", "未公布")
        if not (TIME_RE.match(t) or t == "未公布"):
            reasons.append("time-format")
        elif TIME_RE.match(t) and not add_card.match_time_in_quote(t, quote):
            reasons.append("time-not-in-quote")
        if (s.get("date"), kind, t) in seen:
            reasons.append("duplicate-session")
        seen.add((s.get("date"), kind, t))
        if s.get("date") in no_show:
            reasons.append("session-on-no-show-date")
    return reasons


def validate_batch(pack, proposals, schedule, today=None, now_hm=None):
    """now_hm：本輪讀取時間（HH:MM），當天已演完的場次不新建"""
    today = today or date.today()
    cards = {c["id"]: c for c in schedule}
    readings = {r["sha256"]: r for r in proposals.get("imageReadings") or [] if r.get("sha256")}
    items = {it["postKey"]: it for it in pack["items"]}
    result = {"accepted": [], "confirmed": [], "needsCheck": [], "rejected": [], "dispositions": [], "missing": [],
              "imageRequests": [], "imageReadings": readings}

    # 每張送審圖片都要有判讀紀錄（看不清也要寫 legible=false）
    for it in pack["items"]:
        for img in it.get("images") or []:
            if img["sha256"] not in readings:
                result["needsCheck"].append({"postKey": it["postKey"], "reason": "image-not-read", "sha256": img["sha256"]})
            elif not readings[img["sha256"]].get("legible"):
                result["needsCheck"].append({"postKey": it["postKey"], "reason": "image-illegible", "sha256": img["sha256"],
                                             "notes": readings[img["sha256"]].get("notes", "")})

    by_key = {}
    for d in proposals.get("dispositions") or []:
        by_key.setdefault(d.get("postKey"), []).append(d)
    for key, it in items.items():
        ds = by_key.get(key) or []
        if len(ds) != 1 or ds[0].get("revision") != it["revision"]:
            result["missing"].append({"postKey": key, "reason": "missing-or-duplicate-disposition" if len(ds) != 1 else "revision-mismatch"})
            continue
        d = ds[0]
        if d.get("decision") not in DECISIONS:
            result["rejected"].append({"postKey": key, "reason": "decision-invalid", "decision": d.get("decision")})
            continue
        if d["decision"] == "needs-images":
            if it.get("imageCount") or it.get("images"):
                result["imageRequests"].append(key)
            else:
                result["rejected"].append({"postKey": key, "reason": "needs-images-but-no-images"})
            continue
        result["dispositions"].append(d)
        corpus = corpus_for(it, readings)
        social = key.startswith(("threads:", "facebook:"))
        if d["decision"] == "needs-check":
            result["needsCheck"].append({"postKey": key, "url": it.get("url"), "reason": "judge-needs-check", "detail": d.get("reason")})
        for n, ev in enumerate(d.get("events") or []):
            ref = {"postKey": key, "url": it.get("url"), "event": n, "revision": it["revision"]}
            action = ev.get("action")
            if action not in ACTIONS:
                result["rejected"].append({**ref, "reason": "action-invalid"})
                continue
            quote = normalize_text(ev.get("quote", ""))
            reasons = []
            if not quote or quote not in corpus:
                reasons.append("quote-not-in-post")
            for evid in ev.get("evidence") or []:
                if normalize_text(evid.get("quote", "")) not in corpus:
                    reasons.append(f"evidence-not-in-post:{evid.get('field')}")
            if ev.get("genre") not in GENRES:
                reasons.append("genre-out-of-scope")
            if ev.get("eventType", "演出") not in EVENT_TYPES:
                reasons.append("eventType-invalid")
            if ev.get("genre") == "布袋戲" and re.search(r"偶", corpus) and not re.search(r"布袋|掌中|金光", corpus):
                reasons.append("puppet-not-budaixi")
            if action in ("update", "change", "cancel", "confirm"):
                if ev.get("targetCardId") not in cards:
                    reasons.append("target-card-not-found")
            if action != "cancel" or ev.get("sessions"):
                reasons.extend(check_sessions(ev, quote, today, action, now_hm))
            if reasons:
                bucket = "rejected" if any(r.startswith(("quote-not", "evidence-not", "action", "time-format", "invalid-date")) for r in reasons) else "needsCheck"
                result[bucket].append({**ref, "reason": ",".join(dict.fromkeys(reasons)), "proposed": ev})
                continue
            if action == "confirm":
                diffs = diff_against_card(ev, cards[ev["targetCardId"]])
                if diffs:
                    # 程式比對出差異：不得當成一致；只是補未公布欄位→update，否則→change，都交第二次審查
                    new_action = "update" if all(x.get("fill") for x in diffs) else "change"
                    result["accepted"].append({**ref, "action": new_action, "event": ev, "diffs": diffs, "convertedFrom": "confirm"})
                else:
                    result["confirmed"].append({**ref, "targetCardId": ev["targetCardId"]})
                continue
            if action == "add":
                dup = find_duplicate(ev, schedule)
                if dup:
                    result["needsCheck"].append({**ref, "reason": f"possible-duplicate:{dup}", "proposed": ev})
                    continue
            if action in ("change", "cancel") and social:
                target = cards[ev["targetCardId"]]
                if add_card.extract_account_id(target.get("sourceUrl") or target.get("link", "")) != add_card.extract_account_id(it.get("url", "")):
                    result["needsCheck"].append({**ref, "reason": "different-account-change", "proposed": ev, "targetCardId": ev["targetCardId"]})
                    continue
            diffs = diff_against_card(ev, cards[ev["targetCardId"]]) if action in ("update", "change") else []
            result["accepted"].append({**ref, "action": action, "event": ev, "diffs": diffs})
    dedupe_within_run(result)
    return result


def find_duplicate(event, schedule):
    """同日＋同地＋同劇團才算同場；同日同地不同劇團不合併"""
    dates = {s["date"] for s in event.get("sessions") or []}
    for card in schedule:
        if not (dates & set(card_dates(card))):
            continue
        place = same_place(event.get("location"), card.get("location"))
        same_troupe = norm_place(event.get("troupe")) == norm_place(card.get("troupe")) or same_place(event.get("troupe"), card.get("troupe"))
        titles = re.findall(r"《(.*?)》", event.get("title", "")) or [event.get("title", "")]
        same_title = any(t and norm_place(t) and norm_place(t) in norm_place(card.get("title", "")) for t in titles)
        # 同日＋同地＋（同團或同劇目）；或同日＋同團＋同劇目（地點寫法差很多時，例如「演藝廳戶外廣場大舞台」對「薪瀛舞台」）
        if (place and (same_troupe or same_title)) or (same_troupe and same_title):
            return card["id"]
    return None


def dedupe_within_run(result):
    """同一輪兩個帳號轉貼同一場：保留第一個，其餘轉為補充來源"""
    seen = {}
    kept = []
    for change in result["accepted"]:
        ev = change["event"]
        if change["action"] != "add":
            key = (change["action"], ev.get("targetCardId"))
            if key in seen:
                seen[key].setdefault("alsoSources", []).append(change["url"])
                continue
            seen[key] = change
            kept.append(change)
            continue
        key = (ev.get("troupe"), main_location(ev.get("location")), tuple(sorted(s["date"] for s in ev.get("sessions") or [])))
        if key in seen:
            seen[key].setdefault("alsoSources", []).append(change["url"])
            continue
        seen[key] = change
        kept.append(change)
    result["accepted"] = kept
