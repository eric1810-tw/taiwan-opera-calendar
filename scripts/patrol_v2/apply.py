"""把通過驗證與第二次審查的變更，經 add_card.py 寫入 schedule.json（不直接手改）。"""
import json
import subprocess
import sys
import tempfile
from pathlib import Path

from .common import ROOT, read_json, write_json

ADD_CARD = ROOT / "scripts" / "add_card.py"


def attach_image_readings(evidence_dir, store):
    """把已判讀（legible）的海報紀錄寫進證據檔，讓 add_card 能以「正文＋判讀紀錄」比對原文"""
    for path in Path(evidence_dir).glob("*.json"):
        data = read_json(path)
        if not isinstance(data, dict) or not isinstance(data.get("posts"), list):
            continue
        changed = False
        for post in data["posts"]:
            readings = []
            for m in post.get("media") or []:
                r = store.images.get(m.get("sha256") or "")
                if r and r.get("legible") and r.get("reading"):
                    readings.append({"sha256": m["sha256"], "reading": r["reading"]})
            if readings != post.get("imageReadings", []):
                post["imageReadings"] = readings
                changed = True
        if changed:
            write_json(path, data)


def to_add_card_proposal(change, item_source):
    ev = change["event"]
    proposal = {
        "source": item_source,
        "postKey": change["postKey"],
        "postUrl": change.get("url") or "",
        "quote": ev.get("quote", ""),
    }
    action = change["action"]
    if action == "add":
        proposal.update({
            "troupe": ev.get("troupe", ""),
            "title": ev.get("title", ""),
            "location": ev.get("location", "未公布"),
            "genre": ev.get("genre", "歌仔戲"),
            "artist": ev.get("artist") or "未公布",
            "badgeType": ev.get("badgeType") or ("lecture" if ev.get("eventType") in ("講座", "體驗") else "temple"),
            "sessions": ev.get("sessions"),
        })
        if ev.get("noShowDates"):
            proposal["noShowDates"] = ev["noShowDates"]
    elif action in ("update", "change"):
        fields = {d["field"] for d in change.get("diffs") or []}
        if ev.get("sessions") and ({"time", "date"} & fields or action == "change"):
            proposal["sessions"] = ev["sessions"]
            if ev.get("noShowDates"):
                proposal["noShowDates"] = ev["noShowDates"]
        if "location" in fields and ev.get("location"):
            proposal["location"] = ev["location"]
    return proposal


def run_add_card(args, proposal, work_root, evidence_dir, today):
    work_root = Path(work_root)
    with tempfile.NamedTemporaryFile("w", suffix=".json", delete=False, encoding="utf-8") as f:
        json.dump(proposal, f, ensure_ascii=False)
        proposal_path = f.name
    cmd = [sys.executable, str(ADD_CARD), *args,
           "--schedule", str(work_root / "data/schedule.json"),
           "--review-queue", str(work_root / "data/review_queue.json"),
           "--cancelled", str(work_root / "docs/patrols/cancelled_cards.jsonl"),
           "--facebook-accounts", str(work_root / "data/facebook_accounts.json"),
           "--today", today]
    if "--from-moc" not in args:
        cmd += ["--proposal", proposal_path, "--evidence-dir", str(evidence_dir)]
    else:
        cmd += ["--culture-records", str(work_root / "data/moc_records.json")]
    res = subprocess.run(cmd, capture_output=True, text=True, cwd=ROOT)
    Path(proposal_path).unlink(missing_ok=True)
    try:
        out = json.loads(res.stdout.strip().splitlines()[-1])
    except Exception:
        out = {"result": "error", "reasons": [res.stderr.strip()[-500:] or "add_card 無輸出"]}
    out["exit"] = res.returncode
    return out


def apply_changes(changes, verdicts, work_root, evidence_dir, today, sources_by_key):
    """verdicts：{changeId: 'approve'|'reject'|'needs-check'}；只有 approve 會寫入"""
    results = []
    for change in changes:
        verdict = verdicts.get(change["changeId"], {}).get("verdict", "needs-check")
        if verdict != "approve":
            results.append({"changeId": change["changeId"], "result": "held", "verdict": verdict,
                            "reason": verdicts.get(change["changeId"], {}).get("reason", "")})
            continue
        source = sources_by_key.get(change["postKey"], "")
        action = change["action"]
        if source == "culture" and action == "add":
            out = run_add_card(["--from-moc", change.get("mocTitle") or change["event"].get("title", "")], {}, work_root, evidence_dir, today)
        else:
            proposal = to_add_card_proposal(change, source)
            flag = {"add": [], "update": ["--update", change["event"].get("targetCardId", "")],
                    "change": ["--change", change["event"].get("targetCardId", "")],
                    "cancel": ["--cancel", change["event"].get("targetCardId", "")]}[action]
            out = run_add_card(flag, proposal, work_root, evidence_dir, today)
        results.append({"changeId": change["changeId"], "action": action, **out})
    return results
