"""新巡檢後端共用工具：路徑、時間、原子寫入、雜湊。"""
import hashlib
import re
import json
import os
import tempfile
from datetime import datetime, time as dtime
from pathlib import Path
from zoneinfo import ZoneInfo

TPE = ZoneInfo("Asia/Taipei")
ROOT = Path(__file__).resolve().parents[2]
STATE_DIR = ROOT / "patrol_state"
EVIDENCE_DIR = ROOT / "patrol_evidence"
RULES_VERSION = "v2-2026-10-24"
EDGE_PROFILE = Path.home() / ".patrol-edge"

PROTECTED_FILES = (
    "ISSUES_REVIEW.md",
    "PROJECT_HANDOVER.md",
    "patrol_runs/2026-10-16_0300.json",
    "CLAUDE_AUDIT_2026-09-30.md",
    "CLOUDFLARE_HANDOVER.md",
    "CODEX_TASK_REVIEW_FIXES_2026-09-30.md",
)

# agy 在正式資料夾 03:00 巡檢；非正式模式在此時段不得開 ~/.patrol-edge
AGY_WINDOW = (dtime(2, 30), dtime(4, 30))


def now_dt():
    return datetime.now(TPE)


def now():
    return now_dt().isoformat(timespec="seconds")


def today_str(at=None):
    return (at or now_dt()).date().isoformat()


def in_agy_window(at=None):
    t = (at or now_dt()).timetz().replace(tzinfo=None)
    return AGY_WINDOW[0] <= t < AGY_WINDOW[1]


def read_json(path, default=None):
    path = Path(path)
    if not path.exists():
        return default
    return json.loads(path.read_text(encoding="utf-8"))


def write_json(path, value):
    path = Path(path)
    path.parent.mkdir(parents=True, exist_ok=True)
    fd, temp = tempfile.mkstemp(prefix=".tmp-", suffix=".json", dir=path.parent)
    try:
        with os.fdopen(fd, "w", encoding="utf-8") as stream:
            json.dump(value, stream, ensure_ascii=False, indent=2)
            stream.write("\n")
            stream.flush()
            os.fsync(stream.fileno())
        os.replace(temp, path)
    finally:
        if os.path.exists(temp):
            os.unlink(temp)


def append_jsonl(path, value):
    path = Path(path)
    path.parent.mkdir(parents=True, exist_ok=True)
    with open(path, "a", encoding="utf-8") as stream:
        stream.write(json.dumps(value, ensure_ascii=False) + "\n")
        stream.flush()
        os.fsync(stream.fileno())


def read_jsonl(path):
    path = Path(path)
    if not path.exists():
        return []
    rows = []
    for line in path.read_text(encoding="utf-8").splitlines():
        line = line.strip()
        if line:
            rows.append(json.loads(line))
    return rows


def sha256_bytes(data):
    return hashlib.sha256(data).hexdigest()


def sha256_file(path):
    return sha256_bytes(Path(path).read_bytes())


def normalize_text(text):
    return " ".join(str(text or "").split())


_RELATIVE = re.compile(r"(?<![\d/:])\d{1,3}\s*(?:秒|分鐘|分钟|小時|小时|天|週|周|個月|个月)(?:前)?")
_TRAILING_COUNTS = re.compile(r"(?:\s+\d{1,7})+\s*$")
_UI_WORDS = re.compile(r"顯示較少|顯示更多|查看更多|查看翻譯|See more|See translation")


def revision_text(text):
    """版本比對用的正文：去掉「5天」「3小時」等相對時間、結尾讚數留言數、介面字，避免同一篇每天都被當成有變動"""
    t = _UI_WORDS.sub(" ", str(text or ""))
    t = _RELATIVE.sub(" ", t)
    t = normalize_text(t)
    return _TRAILING_COUNTS.sub("", t)


def text_revision(text, image_hashes=()):
    body = revision_text(text) + "\n" + "\n".join(sorted(image_hashes))
    return "sha256:" + sha256_bytes(body.encode("utf-8"))
