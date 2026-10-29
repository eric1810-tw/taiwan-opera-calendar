"""2026-10-27／28 兩輪卡住的回歸測試：失敗即停、檔名解析、殘留 index.lock、背景程序、Python 3.11 相容。"""
import io
import os
import sys
import tempfile
import threading
import time
import tokenize
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "scripts"))
sys.path.insert(0, str(ROOT))

import patrol  # noqa: E402
from patrol_v2 import preflight, publish  # noqa: E402
from patrol_v2.common import read_json, write_json  # noqa: E402
from patrol_v2.state import RunState  # noqa: E402


class StepFailureStops(unittest.TestCase):
    """10/27、10/28：發布失敗後 advance 一直重跑同一步，空轉 4～5 小時"""

    def test_failed_step_returns_stopped(self):
        with tempfile.TemporaryDirectory() as tmp:
            st = RunState.create("dry-run", state_dir=tmp)
            calls = []

            def failing(state):
                calls.append(1)
                state.set_step("preflight", "failed", "Actions 123 結論 failure")
                return None

            original = patrol.STEP_FUNCS["preflight"]
            patrol.STEP_FUNCS["preflight"] = failing
            try:
                result = patrol.advance(st)
            finally:
                patrol.STEP_FUNCS["preflight"] = original
            self.assertEqual(result["action"], "stopped")
            self.assertEqual(result["step"], "preflight")
            self.assertEqual(len(calls), 1)


class ChangedPaths(unittest.TestCase):
    """10/28：git status 輸出整段 strip，第一行 " M data/..." 被削成 "M data/..."，檔名少一個字而漏提交"""

    def test_first_entry_with_leading_space(self):
        out = " M data/patrol_status.json\0 M data/schedule.json\0?? patrol_runs/2026-10-28_0311.json\0"
        runner = lambda args, cwd=None, strip=True: out  # noqa: E731
        paths = ["data/schedule.json", "data/patrol_status.json", "patrol_runs/2026-10-28_0311.json", "data/review_queue.json"]
        self.assertEqual(publish.changed_paths(paths, runner=runner),
                         ["data/schedule.json", "data/patrol_status.json", "patrol_runs/2026-10-28_0311.json"])

    def test_git_keeps_leading_space_when_asked(self):
        with tempfile.TemporaryDirectory() as tmp:
            publish.git(["init", "-q"], cwd=tmp)
            Path(tmp, "a.txt").write_text("1")
            publish.git(["add", "a.txt"], cwd=tmp)
            publish.git(["-c", "user.email=t@t", "-c", "user.name=t", "commit", "-qm", "x"], cwd=tmp)
            Path(tmp, "a.txt").write_text("2")
            self.assertEqual(publish.changed_paths(["a.txt", "b.txt"], cwd=tmp), ["a.txt"])


class StaleIndexLock(unittest.TestCase):
    """10/28：上一輪被中斷留下 .git/index.lock，git add 失敗後空轉"""

    def setUp(self):
        self.tmp = tempfile.TemporaryDirectory()
        self.root = Path(self.tmp.name)
        (self.root / ".git").mkdir()
        self.lock = self.root / ".git" / "index.lock"
        self.runner = lambda args, cwd=None, check=True: ".git/index.lock"  # noqa: E731

    def tearDown(self):
        self.tmp.cleanup()

    def test_no_lock(self):
        self.assertIsNone(preflight.clear_stale_index_lock(self.root, self.runner, git_running=lambda: False))

    def test_old_lock_without_git_is_removed(self):
        self.lock.write_text("")
        note = preflight.clear_stale_index_lock(self.root, self.runner, git_running=lambda: False, at=time.time() + 3600)
        self.assertFalse(self.lock.exists())
        self.assertIn("已刪除殘留", note)

    def test_recent_lock_stops(self):
        self.lock.write_text("")
        with self.assertRaises(preflight.PreflightError):
            preflight.clear_stale_index_lock(self.root, self.runner, git_running=lambda: False)
        self.assertTrue(self.lock.exists())

    def test_lock_with_running_git_stops(self):
        self.lock.write_text("")
        with self.assertRaises(preflight.PreflightError):
            preflight.clear_stale_index_lock(self.root, self.runner, git_running=lambda: True, at=time.time() + 3600)
        self.assertTrue(self.lock.exists())


class BackgroundWorker(unittest.TestCase):
    """10/28：讀社群要 20 分鐘，主流程 10 分鐘逾時就把程序砍掉，留下 Edge 與 git 鎖。
    現在耗時步驟交給背景程序，start／next 在時限內一定回來。"""

    def setUp(self):
        self.tmp = tempfile.TemporaryDirectory()
        self.st = RunState.create("dry-run", state_dir=self.tmp.name)
        self.pids = {}

    def tearDown(self):
        self.tmp.cleanup()

    def fake_spawn(self, delay, result):
        def spawn(st):
            pid = 100000 + len(self.pids)
            self.pids[pid] = True

            def work():
                time.sleep(delay)
                info = read_json(patrol.worker_path(st), {}) or {}
                info.update({"status": "finished", "pid": pid, "result": result, "consumed": False})
                write_json(patrol.worker_path(st), info)
                self.pids[pid] = False

            threading.Thread(target=work, daemon=True).start()
            return pid
        return spawn

    def alive(self, pid):
        return self.pids.get(pid, False)

    def test_returns_result_when_worker_finishes_in_time(self):
        result = patrol.drive(self.st, budget=5, spawn=self.fake_spawn(0.1, {"action": "judge"}), alive=self.alive, sleep=lambda s: time.sleep(0.05))
        self.assertEqual(result["action"], "judge")

    def test_slow_worker_returns_continue_within_budget(self):
        spawn = self.fake_spawn(1.0, {"action": "done"})
        started = time.monotonic()
        first = patrol.drive(self.st, budget=0.2, spawn=spawn, alive=self.alive, sleep=lambda s: time.sleep(0.05))
        self.assertLess(time.monotonic() - started, 0.8)
        self.assertEqual(first["action"], "continue")
        self.assertEqual(len(self.pids), 1)
        second = patrol.drive(self.st, budget=5, spawn=spawn, alive=self.alive, sleep=lambda s: time.sleep(0.05))
        self.assertEqual(second["action"], "done")
        self.assertEqual(len(self.pids), 1, "還在跑的背景程序不能重開第二個")

    def test_result_is_consumed_once(self):
        spawn = self.fake_spawn(0.05, {"action": "review"})
        patrol.drive(self.st, budget=5, spawn=spawn, alive=self.alive, sleep=lambda s: time.sleep(0.02))
        nxt = patrol.drive(self.st, budget=0.3, spawn=self.fake_spawn(0.05, {"action": "done"}), alive=self.alive, sleep=lambda s: time.sleep(0.02))
        self.assertEqual(nxt["action"], "done", "用過的結果不能再回傳一次，要開新的背景程序往下做")

    def test_worker_finishing_between_read_and_alive_check(self):
        """10/29：背景程序在「讀狀態檔」與「查程序還在不在」之間寫完結果並結束，主流程誤回 continue"""
        def alive(pid):
            info = read_json(patrol.worker_path(self.st), {}) or {}
            if info.get("status") == "running":
                info.update({"status": "finished", "result": {"action": "judge"}, "consumed": False})
                write_json(patrol.worker_path(self.st), info)
            return False

        result = patrol.drive(self.st, budget=5, spawn=lambda st: 123456, alive=alive, sleep=lambda s: None)
        self.assertEqual(result["action"], "judge")

    def test_dead_worker_is_restarted(self):
        write_json(patrol.worker_path(self.st), {"status": "running", "pid": 999999, "restarts": 0})
        result = patrol.drive(self.st, budget=5, spawn=self.fake_spawn(0.05, {"action": "done"}), alive=self.alive, sleep=lambda s: time.sleep(0.02))
        self.assertEqual(result["action"], "done")
        self.assertEqual((read_json(patrol.worker_path(self.st)) or {}).get("restarts"), 1)


def py311_violations(source):
    """Python 3.12 才允許的 f-string：大括號內再用同一種引號（Actions 用 3.11 會 SyntaxError）"""
    if not hasattr(tokenize, "FSTRING_START"):
        return []
    found = []
    stack = []
    for tok in tokenize.generate_tokens(io.StringIO(source).readline):
        if tok.type == tokenize.FSTRING_START:
            quote = tok.string.lstrip("fFrRbBuU")
            if stack and (quote == stack[-1] or quote[0] == stack[-1][0] and len(stack[-1]) == 1):
                found.append(tok.start[0])
            stack.append(quote)
        elif tok.type == tokenize.FSTRING_END:
            stack.pop()
        elif tok.type == tokenize.STRING and stack:
            quote = tok.string.lstrip("fFrRbBuU")[:3]
            quote = quote if quote in ('"""', "'''") else quote[0]
            outer = stack[-1]
            if quote == outer or (len(outer) == 1 and quote[0] == outer):
                found.append(tok.start[0])
    return found


@unittest.skipUnless(hasattr(tokenize, "FSTRING_START"), "需 Python 3.12 以上的 tokenize 才能檢查")
class Python311Compat(unittest.TestCase):
    """10/27：report.py 的 f"{len(agy["commits"])}" 在本機 3.14 正常、Actions 3.11 語法錯誤"""

    def test_detector_catches_the_incident(self):
        self.assertEqual(py311_violations('x = f"agy {len(agy["commits"])} 筆"\n'), [1])
        self.assertEqual(py311_violations("x = f\"agy {len(agy['commits'])} 筆\"\n"), [])

    def test_all_python_files(self):
        problems = []
        for path in sorted(list((ROOT / "scripts").rglob("*.py")) + list((ROOT / "tests").glob("*.py"))):
            if ".bak" in path.name:
                continue
            for line in py311_violations(path.read_text(encoding="utf-8")):
                problems.append(f"{path.relative_to(ROOT)}:{line}")
        self.assertEqual(problems, [], "這些 f-string 在 GitHub Actions 的 Python 3.11 會語法錯誤")


if __name__ == "__main__":
    unittest.main()
