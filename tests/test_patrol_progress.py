"""Failure cases that must never produce a false patrol/publication success."""
import copy
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
        expected = {"startedAt": run["startedAt"], "status": "failed"}
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
                    patrol.verify(run, "sha", "123", path, fetcher=lambda url: next(responses))

    def test_failed_patrol_can_have_successfully_published_status(self):
        with tempfile.TemporaryDirectory() as tmp, \
                patch.object(patrol, "targets", return_value={"threads:test": "url"}):
            run, expected, action = self.publication_fixture()
            path = Path(tmp) / "status.json"
            patrol.write(path, expected)
            responses = iter([action, expected])
            patrol.verify(run, "sha", "123", path, fetcher=lambda url: next(responses))
            self.assertEqual(run["publication"]["state"], "verified")
            self.assertEqual(run["publication"]["publicStatus"]["status"], "failed")


if __name__ == "__main__":
    unittest.main()
