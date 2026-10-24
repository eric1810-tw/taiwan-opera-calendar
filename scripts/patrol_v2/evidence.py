"""貼文版本、圖片快取、判讀快取，以及「只送新內容」的判讀包。

- 貼文版本＝正規化正文＋已下載圖片 sha256 的雜湊。版本判讀過就沿用，不重送。
- 圖片以內容 sha256 存放；判讀成功（legible）才算看過，看不清的下輪再送。
- 規則版本（RULES_VERSION）升級時，所有判讀快取失效。
"""
from datetime import datetime, timedelta
from pathlib import Path

from .common import RULES_VERSION, STATE_DIR, now, read_json, text_revision, write_json

POSTS_INDEX = "posts_index.json"
JUDGMENTS = "judgments.json"
IMAGE_READINGS = "image_readings.json"


class EvidenceStore:
    def __init__(self, state_dir=STATE_DIR):
        self.dir = Path(state_dir)
        self.posts = read_json(self.dir / POSTS_INDEX, {}) or {}
        self.judgments = read_json(self.dir / JUDGMENTS, {}) or {}
        self.images = read_json(self.dir / IMAGE_READINGS, {}) or {}

    def save(self):
        write_json(self.dir / POSTS_INDEX, self.posts)
        write_json(self.dir / JUDGMENTS, self.judgments)
        write_json(self.dir / IMAGE_READINGS, self.images)

    @staticmethod
    def revision_of(post):
        hashes = [m["sha256"] for m in post.get("media") or [] if m.get("sha256")]
        return text_revision(post.get("text", ""), hashes)

    def observe(self, post, run_id):
        """登記本輪看到的貼文；回傳 'new'／'changed'／'unchanged'。"""
        rev = self.revision_of(post)
        post["revision"] = rev
        entry = self.posts.get(post["postKey"])
        if entry is None:
            self.posts[post["postKey"]] = {"revisions": [{"revision": rev, "firstSeenAt": now(), "runId": run_id}],
                                           "url": post.get("url"), "datetime": post.get("datetime"), "lastSeenRun": run_id}
            return "new"
        entry["lastSeenRun"] = run_id
        if entry["revisions"][-1]["revision"] != rev:
            entry["revisions"].append({"revision": rev, "firstSeenAt": now(), "runId": run_id})
            return "changed"
        return "unchanged"

    def judged(self, revision):
        j = self.judgments.get(revision)
        return bool(j and j.get("rulesVersion") == RULES_VERSION)

    def image_done(self, sha):
        r = self.images.get(sha)
        return bool(r and r.get("legible") and r.get("rulesVersion") == RULES_VERSION)

    def remember_judgment(self, revision, post_key, disposition, run_id):
        self.judgments[revision] = {"postKey": post_key, "decision": disposition.get("decision"),
                                    "reason": disposition.get("reason"), "runId": run_id,
                                    "judgedAt": now(), "rulesVersion": RULES_VERSION}

    def remember_image(self, sha, reading, run_id):
        self.images[sha] = {"legible": bool(reading.get("legible")), "reading": reading.get("reading", ""),
                            "notes": reading.get("notes", ""), "runId": run_id, "readAt": now(),
                            "rulesVersion": RULES_VERSION}


def in_window(post, now_dt, days=7):
    """發文時間在窗口內，或時間不明（FB 常見）→ 需要看。"""
    dt = post.get("datetime")
    if not dt:
        return True
    try:
        return datetime.fromisoformat(str(dt).replace("Z", "+00:00")) >= now_dt - timedelta(days=days)
    except ValueError:
        return True


def compact_card(card):
    keys = ("id", "date", "endDate", "time", "troupe", "title", "genre", "location", "verifyStatus", "sourceUrl", "link")
    return {k: card[k] for k in keys if k in card}


def select_for_judgment(items, store, now_dt, run_id, force_keys=()):
    """回傳 (要送判讀的 items, 略過統計)。items 需已含 media（社群）或空 images。"""
    selected, skipped = [], {"unchanged-judged": 0, "out-of-window": 0}
    for item in items:
        status = store.observe(item, run_id)
        item["changeStatus"] = status
        pending_images = [m["sha256"] for m in item.get("media") or [] if m.get("sha256") and not store.image_done(m["sha256"])]
        item["pendingImages"] = pending_images
        if item["postKey"] in force_keys:
            selected.append(item)
            continue
        if not item["postKey"].startswith(("issues:", "opentix:", "culture:")) and not in_window(item, now_dt):
            skipped["out-of-window"] += 1
            continue
        if store.judged(item["revision"]) and not pending_images and not item.get("changedThisRun"):
            skipped["unchanged-judged"] += 1
            continue
        selected.append(item)
    return selected, skipped


def build_batches(selected, schedule, store=None, max_posts=25, max_images=12):
    """切批：每批最多 25 篇或 12 張圖，避免單次子代理過大。"""
    batches, cur, cur_images = [], [], 0
    for item in selected:
        n_img = len(item.get("pendingImages") or [])
        if cur and (len(cur) >= max_posts or cur_images + n_img > max_images):
            batches.append(cur)
            cur, cur_images = [], 0
        cur.append(item)
        cur_images += n_img
    if cur:
        batches.append(cur)
    cards = [compact_card(c) for c in schedule]
    packs = []
    for i, batch in enumerate(batches, 1):
        packs.append({
            "batch": i,
            "rulesVersion": RULES_VERSION,
            "cards": cards,
            "items": [{
                "postKey": it["postKey"], "revision": it["revision"], "source": it.get("source"),
                "url": it.get("url"), "datetime": it.get("datetime"), "changeStatus": it.get("changeStatus"),
                "text": it.get("text", ""),
                "images": [{"sha256": m["sha256"], "file": m["file"]} for m in it.get("media") or []
                           if m.get("sha256") and m["sha256"] in (it.get("pendingImages") or [])],
                "knownImageReadings": [{"sha256": m["sha256"], "reading": (store.images.get(m["sha256"], {}) if store else {}).get("reading", "")}
                                       for m in it.get("media") or []
                                       if m.get("sha256") and m["sha256"] not in (it.get("pendingImages") or [])],
            } for it in batch],
        })
    return packs


def pack_stats(packs):
    posts = sum(len(p["items"]) for p in packs)
    images = sum(len(i["images"]) for p in packs for i in p["items"])
    chars = sum(len(i["text"]) for p in packs for i in p["items"])
    return {"batches": len(packs), "posts": posts, "images": images, "approxChars": chars}
