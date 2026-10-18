"""Failure cases that must never produce a false patrol/publication success."""
import copy
import subprocess
import sys
import tempfile
import unittest
from pathlib import Path
from unittest.mock import patch

from scripts import patrol_progress as patrol


class PatrolProgressTests(unittest.TestCase):
    def setUp(self):
        self.run = {"startedAt": "2026-10-08T03:00:00+08:00", "sources": {},
                    "publication": {"state": "pending"}, "finalizedAt": None}
        patrol.sync(self.run, {"threads:test": "https://example.org"})

    def test_pending_or_new_target_fails_coverage(self):
        self.assertEqual(patrol.coverage(self.run, ["threads:test"]), "failed")
        self.assertEqual(patrol.coverage(self.run, ["threads:new"]), "failed")

    def test_incomplete_media_cannot_be_complete(self):
        with self.assertRaises(ValueError):
            patrol.record(self.run, "threads:test", "complete", "browser", "url", "today", "unread", "text only")

    def test_partial_is_not_complete_and_attempts_survive_retry(self):
        patrol.record(self.run, "threads:test", "failed", "browser", "url", "", "unread", "loading")
        patrol.record(self.run, "threads:test", "partial", "post", "url", "one post", "partial", "other posts unavailable")
        self.assertEqual(patrol.coverage(self.run, ["threads:test"]), "partial")
        self.assertEqual(len(self.run["sources"]["threads:test"]["attempts"]), 2)

    def test_new_reading_invalidates_published_receipt(self):
        self.run["publication"] = {"state": "verified"}
        patrol.record(self.run, "threads:test", "complete", "browser", "url", "date range", "complete", "posts and posters checked")
        self.assertEqual(self.run["publication"]["state"], "pending")
        self.assertIsNone(self.run["finalizedAt"])

    def test_resume_preserves_evidence_and_adds_new_target_as_pending(self):
        patrol.record(self.run, "threads:test", "complete", "browser", "url", "date range", "complete", "checked")
        started = self.run["startedAt"]
        patrol.sync(self.run, {"threads:test": "url", "facebook:new": "new-url"})
        self.assertEqual(self.run["startedAt"], started)
        self.assertEqual(len(self.run["sources"]["threads:test"]["attempts"]), 1)
        self.assertEqual(patrol.coverage(self.run, self.run["activeTargets"]), "failed")

    def publication_fixture(self):
        run = copy.deepcopy(self.run)
        run["finalizedAt"] = "2026-10-08T03:10:00+08:00"
        expected = {
            "startedAt": run["startedAt"],
            "lastAttemptAt": run["startedAt"],
            "status": "failed",
            "counts": {"complete": 0, "partial": 0, "failed": 0, "pending": 1, "total": 1}
        }
        action = {"path": ".github/workflows/daily-update.yml", "head_sha": "sha",
                  "status": "completed", "conclusion": "success"}
        return run, expected, action

    def test_wrong_sha_running_action_or_stale_public_status_rejected(self):
        for defect in ("sha", "running", "public", "workflow"):
            with self.subTest(defect=defect), tempfile.TemporaryDirectory() as tmp, \
                    patch.object(patrol, "targets", return_value={"threads:test": "url"}):
                run, expected, action = self.publication_fixture()
                path = Path(tmp) / "status.json"
                patrol.write(path, expected)
                live = dict(expected)
                if defect == "sha":
                    action["head_sha"] = "wrong"
                elif defect == "running":
                    action["status"] = "in_progress"
                elif defect == "workflow":
                    action["path"] = ".github/workflows/unrelated.yml"
                else:
                    live["startedAt"] = "2026-10-07T03:00:00+08:00"
                responses = iter([action, live])
                with self.assertRaises(ValueError):
                    patrol.verify(run, "sha", "123", path,
                                  fetcher=lambda url: next(responses),
                                  git_reader=lambda sha, rel: expected)

    def test_failed_patrol_can_have_successfully_published_status(self):
        with tempfile.TemporaryDirectory() as tmp, \
                patch.object(patrol, "targets", return_value={"threads:test": "url"}):
            run, expected, action = self.publication_fixture()
            path = Path(tmp) / "status.json"
            patrol.write(path, expected)
            responses = iter([action, expected])
            patrol.verify(run, "sha", "123", path,
                          fetcher=lambda url: next(responses),
                          git_reader=lambda sha, rel: expected)
            self.assertEqual(run["publication"]["state"], "verified")
            self.assertEqual(run["publication"]["publicStatus"]["status"], "failed")

    # --- B 段新增測試 ---

    def test_last_attempt_at_equals_max_at_independent_of_finalize_time(self):
        """1. lastAttemptAt 等於 attempts 中 at 的最大值，與 finalize 時間無關。"""
        with tempfile.TemporaryDirectory() as tmp:
            status_path = Path(tmp) / "status.json"
            targets_dict = {"threads:test": "url"}
            self.run["sources"]["threads:test"]["attempts"] = [
                {"at": "2026-10-18T03:05:00+08:00", "method": "m", "url": "u", "state": "partial", "scope": "s", "media": "partial", "detail": "d1"},
                {"at": "2026-10-18T03:41:07+08:00", "method": "m", "url": "u", "state": "partial", "scope": "s", "media": "partial", "detail": "d2"},
                {"at": "2026-10-18T03:10:00+08:00", "method": "m", "url": "u", "state": "partial", "scope": "s", "media": "partial", "detail": "d3"},
            ]
            self.run["sources"]["threads:test"]["state"] = "partial"
            with patch.object(patrol, "now", return_value="2026-10-18T08:31:00+08:00"):
                status_data = patrol.finalize(self.run, status_path=status_path, current=targets_dict)
            self.assertEqual(status_data["lastAttemptAt"], "2026-10-18T03:41:07+08:00")
            self.assertNotEqual(status_data["lastAttemptAt"], "2026-10-18T08:31:00+08:00")
            self.assertNotIn("completedAt", status_data)
            self.assertNotIn("completedAt", self.run)

    def test_finalize_without_model_omits_model(self):
        """2. 未帶 --model → 狀態檔沒有 model。"""
        with tempfile.TemporaryDirectory() as tmp:
            status_path = Path(tmp) / "status.json"
            status_data = patrol.finalize(self.run, status_path=status_path, model=None, current={"threads:test": "url"})
            self.assertNotIn("model", status_data)
            self.assertNotIn("modelEvidence", status_data)
            on_disk = patrol.read(status_path)
            self.assertNotIn("model", on_disk)

    def test_finalize_with_model_only_no_evidence_records_claimed_and_warns(self):
        """3. 只帶 --model、沒有證據 → 不報錯，狀態檔沒有 model，run 有 modelClaimed。"""
        with tempfile.TemporaryDirectory() as tmp:
            status_path = Path(tmp) / "status.json"
            # Should not raise
            status_data = patrol.finalize(self.run, status_path=status_path, model="Gemini Pro", model_evidence=None, current={"threads:test": "url"})
            self.assertNotIn("model", status_data)
            self.assertNotIn("modelEvidence", status_data)
            self.assertEqual(self.run.get("modelClaimed"), "Gemini Pro")
            self.assertNotIn("model", self.run)
            on_disk = patrol.read(status_path)
            self.assertNotIn("model", on_disk)

    def test_finalize_with_model_and_evidence_records_both(self):
        """4. --model 與 --model-evidence 都有 → 狀態檔有 model 與 modelEvidence。"""
        with tempfile.TemporaryDirectory() as tmp:
            status_path = Path(tmp) / "status.json"
            status_data = patrol.finalize(self.run, status_path=status_path,
                                          model="Gemini 3.8",
                                          model_evidence="Menu screenshot in patrol_runs/...",
                                          current={"threads:test": "url"})
            self.assertEqual(status_data["model"], "Gemini 3.8")
            self.assertEqual(status_data["modelEvidence"], "Menu screenshot in patrol_runs/...")
            self.assertEqual(self.run["model"], "Gemini 3.8")
            self.assertEqual(self.run["modelEvidence"], "Menu screenshot in patrol_runs/...")
            on_disk = patrol.read(status_path)
            self.assertEqual(on_disk["model"], "Gemini 3.8")
            self.assertEqual(on_disk["modelEvidence"], "Menu screenshot in patrol_runs/...")

    def test_verified_run_refinalize_requires_reason(self):
        """5. 已 verified 的 run 再 finalize → 拒絕；帶 --refinalize-reason → 舊 publication 進入 publicationHistory。"""
        with tempfile.TemporaryDirectory() as tmp:
            status_path = Path(tmp) / "status.json"
            targets_dict = {"threads:test": "url"}
            self.run["publication"] = {"state": "verified", "sha": "commit-123"}
            # Without reason -> rejected
            with self.assertRaises(ValueError):
                patrol.finalize(self.run, status_path=status_path, current=targets_dict)
            with self.assertRaises(ValueError):
                patrol.finalize(self.run, status_path=status_path, refinalize_reason="   ", current=targets_dict)

            # With reason -> accepted
            status_data = patrol.finalize(self.run, status_path=status_path,
                                          refinalize_reason="Re-verifying due to frontend fix",
                                          current=targets_dict)
            self.assertIn("publicationHistory", self.run)
            self.assertEqual(len(self.run["publicationHistory"]), 1)
            self.assertEqual(self.run["publicationHistory"][0]["publication"]["sha"], "commit-123")
            self.assertEqual(self.run["publicationHistory"][0]["reason"], "Re-verifying due to frontend fix")
            self.assertEqual(self.run["publication"]["state"], "pending")

    def test_verify_fails_when_status_file_tampered(self):
        """6. 狀態檔的 lastAttemptAt、counts、model、status 任一被竄改 → verify 失敗。"""
        with tempfile.TemporaryDirectory() as tmp, \
                patch.object(patrol, "targets", return_value={"threads:test": "url"}):
            run, expected, action = self.publication_fixture()
            run["sources"]["threads:test"]["state"] = "failed"
            status_path = Path(tmp) / "status.json"

            for tampered_key in ("lastAttemptAt", "counts", "status"):
                with self.subTest(tampered_key=tampered_key):
                    bad_status = copy.deepcopy(expected)
                    if tampered_key == "lastAttemptAt":
                        bad_status["lastAttemptAt"] = "2026-01-01T00:00:00+08:00"
                    elif tampered_key == "counts":
                        bad_status["counts"] = {"complete": 1, "partial": 0, "failed": 0, "pending": 0, "total": 1}
                    elif tampered_key == "status":
                        bad_status["status"] = "complete"

                    patrol.write(status_path, bad_status)
                    with self.assertRaises(ValueError):
                        patrol.verify(run, "sha", "123", status_path,
                                      fetcher=lambda u: action,
                                      git_reader=lambda s, r: expected)

    def test_verify_fails_when_git_status_mismatches_expected(self):
        """7. 注入的 git 讀取結果與期望值不符 → verify 失敗。"""
        with tempfile.TemporaryDirectory() as tmp, \
                patch.object(patrol, "targets", return_value={"threads:test": "url"}):
            run, expected, action = self.publication_fixture()
            status_path = Path(tmp) / "status.json"
            patrol.write(status_path, expected)

            # Git reader returns mismatched content
            git_mismatched = copy.deepcopy(expected)
            git_mismatched["status"] = "complete"

            with self.assertRaises(ValueError):
                patrol.verify(run, "sha", "123", status_path,
                              fetcher=lambda u: action,
                              git_reader=lambda s, r: git_mismatched)

            # Git reader fails / throws
            def failing_git_reader(s, r):
                raise RuntimeError("Git object not found")

            with self.assertRaises(ValueError):
                patrol.verify(run, "sha", "123", status_path,
                              fetcher=lambda u: action,
                              git_reader=failing_git_reader)

    def test_counts_sum_to_total_and_pending_or_failed_leads_to_failed_status(self):
        """8. counts 加總等於 total；只要有 pending 或 failed → status 為 failed。"""
        run = {
            "startedAt": "2026-10-18T03:00:00+08:00",
            "sources": {
                "t1": {"state": "complete"},
                "t2": {"state": "partial"},
                "t3": {"state": "failed"},
                "t4": {"state": "pending"}
            }
        }
        current = ["t1", "t2", "t3", "t4"]
        counts = patrol.get_counts(run, current)
        self.assertEqual(counts["complete"], 1)
        self.assertEqual(counts["partial"], 1)
        self.assertEqual(counts["failed"], 1)
        self.assertEqual(counts["pending"], 1)
        self.assertEqual(counts["total"], 4)
        self.assertEqual(counts["complete"] + counts["partial"] + counts["failed"] + counts["pending"], counts["total"])
        self.assertEqual(patrol.coverage(run, current), "failed")

        # Only partial and complete -> partial
        run_partial = {"sources": {"t1": {"state": "complete"}, "t2": {"state": "partial"}}}
        self.assertEqual(patrol.coverage(run_partial, ["t1", "t2"]), "partial")

        # Only complete -> complete
        run_complete = {"sources": {"t1": {"state": "complete"}, "t2": {"state": "complete"}}}
        self.assertEqual(patrol.coverage(run_complete, ["t1", "t2"]), "complete")

    # --- 002 指令新增：resume 防護與 publicationHistory 測試 ---

    def test_resume_verified_run_without_reason_rejected_and_file_not_modified(self):
        """verified 的 run 不帶 --reason 就 resume → 拒絕，且 run 檔未被改動。"""
        import hashlib
        with tempfile.TemporaryDirectory() as tmp:
            run_file = Path(tmp) / "fake_run.json"
            data = {
                "version": 1,
                "startedAt": "2026-10-18T03:00:00+08:00",
                "resumedAt": [],
                "sources": {"threads:test": {"state": "complete"}},
                "finalizedAt": "2026-10-18T03:30:00+08:00",
                "publication": {
                    "state": "verified",
                    "sha": "abc1234",
                    "actionsRun": "999",
                    "verifiedAt": "2026-10-18T03:35:00+08:00"
                }
            }
            patrol.write(run_file, data)
            sha_before = hashlib.sha256(run_file.read_bytes()).hexdigest()

            # Python API test
            with self.assertRaises(ValueError):
                patrol.resume(data, current={"threads:test": "url"})
            with self.assertRaises(ValueError):
                patrol.resume(data, reason="   ", current={"threads:test": "url"})

            # CLI test: should exit with code 2 and not modify file
            res = subprocess.run(
                [sys.executable, str(patrol.ROOT / "scripts/patrol_progress.py"), "resume", "--run", str(run_file)],
                capture_output=True,
                text=True
            )
            self.assertEqual(res.returncode, 2)
            self.assertIn("必須提供 --reason", res.stderr)

            sha_after = hashlib.sha256(run_file.read_bytes()).hexdigest()
            self.assertEqual(sha_before, sha_after)

    def test_resume_verified_run_with_reason_preserves_publication_history(self):
        """帶 --reason → 歷史中保存舊 publication。"""
        targets_dict = {"threads:test": "url"}
        self.run["publication"] = {
            "state": "verified",
            "sha": "commit-verified-777",
            "actionsRun": "888",
            "verifiedAt": "2026-10-18T03:35:00+08:00"
        }
        self.run["finalizedAt"] = "2026-10-18T03:30:00+08:00"

        patrol.resume(self.run, reason="Adding late discovered opera troupe", current=targets_dict)

        self.assertIn("publicationHistory", self.run)
        self.assertEqual(len(self.run["publicationHistory"]), 1)
        history_entry = self.run["publicationHistory"][0]
        self.assertEqual(history_entry["publication"]["sha"], "commit-verified-777")
        self.assertEqual(history_entry["reason"], "Adding late discovered opera troupe")
        self.assertIn("at", history_entry)
        self.assertEqual(self.run["publication"], {"state": "pending"})
        self.assertIsNone(self.run["finalizedAt"])
        self.assertEqual(len(self.run["resumedAt"]), 1)

    def test_resume_non_verified_run_with_content_archives_to_history(self):
        """非 verified 但 publication 有內容（如 blocked）的 resume → 保存進 publicationHistory。"""
        targets_dict = {"threads:test": "url"}
        self.run["publication"] = {
            "state": "blocked",
            "sha": "bad-sha-000",
            "actionsRun": "111",
            "reason": "Actions run failed"
        }
        patrol.resume(self.run, reason=None, current=targets_dict)

        self.assertIn("publicationHistory", self.run)
        self.assertEqual(len(self.run["publicationHistory"]), 1)
        self.assertEqual(self.run["publicationHistory"][0]["publication"]["state"], "blocked")
        self.assertEqual(self.run["publication"], {"state": "pending"})

    def test_resume_non_verified_run_bare_pending_executes_normally(self):
        """非 verified 的 resume（初始 pending 狀態）→ 照常執行，不產生多餘歷史。"""
        targets_dict = {"threads:test": "url"}
        self.run["publication"] = {"state": "pending"}
        self.run["finalizedAt"] = None

        patrol.resume(self.run, current=targets_dict)

        self.assertNotIn("publicationHistory", self.run)
        self.assertEqual(self.run["publication"], {"state": "pending"})
        self.assertEqual(len(self.run["resumedAt"]), 1)


if __name__ == "__main__":
    unittest.main()

