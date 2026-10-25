"""本輪狀態機：步驟紀錄、跨程序鎖（心跳）、防重入、恢復點。

每個 patrol.py 子命令都是短命程序，所以鎖不綁 pid，而是綁 runId＋心跳時間。
"""
import os
from datetime import datetime, timedelta
from pathlib import Path

from .common import STATE_DIR, now, now_dt, read_json, today_str, write_json

STEPS_BY_MODE = {
    "production": ["preflight", "collect", "pack", "judge", "check", "review", "apply", "publish", "report"],
    "dry-run": ["preflight", "collect", "pack", "judge", "check", "review", "apply", "report"],
    "shadow": ["preflight", "collect", "pack", "judge", "check", "compare", "report"],
}
LOCK_STALE = timedelta(minutes=15)


class LockBusy(Exception):
    pass


def runs_dir(state_dir=STATE_DIR):
    return Path(state_dir) / "runs"


def run_dir(run_id, state_dir=STATE_DIR):
    return runs_dir(state_dir) / run_id


def lock_path(state_dir=STATE_DIR):
    return Path(state_dir) / "lock.json"


def day_index_path(day, mode, state_dir=STATE_DIR):
    return Path(state_dir) / "days" / f"{day}_{mode}.json"


def _parse(ts):
    try:
        return datetime.fromisoformat(ts)
    except Exception:
        return None


def lock_status(state_dir=STATE_DIR, at=None):
    data = read_json(lock_path(state_dir))
    if not data:
        return None
    beat = _parse(data.get("heartbeatAt", ""))
    data["stale"] = beat is None or ((at or now_dt()) - beat) > LOCK_STALE
    return data


def acquire_lock(run_id, state_dir=STATE_DIR, at=None):
    """取得鎖；同一 runId 可重入。其他 runId 的活鎖 → LockBusy；失效鎖 → 接手並回傳舊鎖內容。"""
    path = lock_path(state_dir)
    path.parent.mkdir(parents=True, exist_ok=True)
    payload = {"runId": run_id, "acquiredAt": now(), "heartbeatAt": now(), "pid": os.getpid()}
    try:
        fd = os.open(path, os.O_CREAT | os.O_EXCL | os.O_WRONLY, 0o644)
        os.close(fd)
        write_json(path, payload)
        return None
    except FileExistsError:
        pass
    current = lock_status(state_dir, at)
    if current and current.get("runId") == run_id:
        heartbeat(run_id, state_dir)
        return None
    if current and not current["stale"]:
        raise LockBusy(f"另一輪 {current.get('runId')} 仍在執行（心跳 {current.get('heartbeatAt')}）")
    write_json(path, payload)
    return current


def heartbeat(run_id, state_dir=STATE_DIR):
    path = lock_path(state_dir)
    data = read_json(path)
    if data and data.get("runId") == run_id:
        data["heartbeatAt"] = now()
        write_json(path, data)


def release_lock(run_id, state_dir=STATE_DIR):
    path = lock_path(state_dir)
    data = read_json(path)
    if data and data.get("runId") == run_id:
        path.unlink(missing_ok=True)


class RunState:
    def __init__(self, run_id, state_dir=STATE_DIR):
        self.run_id = run_id
        self.state_dir = Path(state_dir)
        self.dir = run_dir(run_id, state_dir)
        self.path = self.dir / "state.json"
        self.data = read_json(self.path) or {}

    @classmethod
    def create(cls, mode, state_dir=STATE_DIR, at=None, work_root=None):
        at = at or now_dt()
        run_id = at.strftime("%Y-%m-%d_%H%M") + ("" if mode == "production" else f"_{mode}")
        state = cls(run_id, state_dir)
        if state.data:
            raise FileExistsError(f"本輪 {run_id} 已存在")
        state.data = {
            "version": 2,
            "runId": run_id,
            "mode": mode,
            "day": today_str(at),
            "startedAt": at.isoformat(timespec="seconds"),
            "workRoot": str(work_root) if work_root else None,
            "steps": {name: {"status": "pending"} for name in STEPS_BY_MODE[mode]},
            "finished": False,
            "outcome": None,
            "stats": {},
            "models": {},
            "forEric": [],
            "events": [],
        }
        state.save()
        write_json(day_index_path(state.data["day"], mode, state_dir), {"runId": run_id, "finished": False})
        return state

    @property
    def mode(self):
        return self.data["mode"]

    def save(self):
        write_json(self.path, self.data)

    def log(self, message, **extra):
        self.data.setdefault("events", []).append({"at": now(), "message": message, **extra})
        self.save()

    def step(self, name):
        return self.data["steps"].get(name)

    def set_step(self, name, status, detail=None, **extra):
        entry = self.data["steps"].setdefault(name, {})
        entry.update({"status": status, "at": now(), **extra})
        if detail is not None:
            entry["detail"] = detail
        self.save()
        heartbeat(self.run_id, self.state_dir)

    def next_step(self):
        for name in STEPS_BY_MODE[self.mode]:
            status = self.data["steps"].get(name, {}).get("status")
            if status not in ("done", "skipped"):
                return name
        return None

    def ask_eric(self, text):
        if text not in self.data["forEric"]:
            self.data["forEric"].append(text)
            self.save()

    def finish(self, outcome):
        self.data["finished"] = True
        self.data["outcome"] = outcome
        self.data["finishedAt"] = now()
        self.save()
        write_json(day_index_path(self.data["day"], self.mode, self.state_dir),
                   {"runId": self.run_id, "finished": True, "outcome": outcome})
        release_lock(self.run_id, self.state_dir)


def missed_days(mode, state_dir=STATE_DIR, at=None, lookback=3):
    """往前檢查 lookback 天：沒有輪次或沒跑完的日子（第一次執行之前的日子不算）"""
    at = at or now_dt()
    days_dir = Path(state_dir) / "days"
    known = sorted(p.name.split("_")[0] for p in days_dir.glob(f"*_{mode}.json")) if days_dir.exists() else []
    if not known:
        return []
    first = known[0]
    missed = []
    for i in range(1, lookback + 1):
        day = (at - timedelta(days=i)).date().isoformat()
        if day < first:
            break
        index = read_json(day_index_path(day, mode, state_dir))
        if not index:
            missed.append(f"{day}：沒有執行紀錄（漏跑）")
        elif not index.get("finished"):
            missed.append(f"{day}：輪次 {index.get('runId')} 沒有跑完")
    return missed


def find_today(mode, state_dir=STATE_DIR, at=None):
    """今日（台北）同模式的輪次；沒有回傳 None。"""
    index = read_json(day_index_path(today_str(at), mode, state_dir))
    if not index:
        return None
    return RunState(index["runId"], state_dir)
