"""updater.py 的核心資料規則測試；僅使用 Python 標準函式庫。"""

import copy
import json
import tempfile
import unittest
from datetime import date
from pathlib import Path
from unittest.mock import patch

import updater


class UpdaterTests(unittest.TestCase):
    sample = {
        "id": "fixture-event-2026-10-01",
        "date": "2026-10-01",
        "endDate": "2026-10-02",
        "dateFormatted": "2026/10/01–10/02",
        "daysAway": 1,
        "time": "19:00",
        "troupe": "測試劇團",
        "genre": "歌仔戲",
        "artist": "測試演員",
        "title": "固定測試戲",
        "category": "fixture",
        "badgeType": "free",
        "verifyStatus": "community",
        "verifyLabel": "社群公告",
        "location": "高雄市測試場",
        "region": "南部",
        "status": "confirmed",
        "description": "僅供自動化測試，不代表真實演出。",
        "link": "https://example.org/event",
        "tags": ["測試"],
    }

    def test_validate_schedule_accepts_optional_end_date(self):
        event = copy.deepcopy(self.sample)
        event["endDate"] = event["date"]
        self.assertEqual(updater.validate_schedule([event]), [event])

    def test_validate_schedule_accepts_outdoor_badge(self):
        event = copy.deepcopy(self.sample)
        event["badgeType"] = "outdoor"
        self.assertEqual(updater.validate_schedule([event]), [event])

    def test_validate_schedule_rejects_end_date_before_start(self):
        event = copy.deepcopy(self.sample)
        event["endDate"] = "2020-01-01"
        with self.assertRaisesRegex(ValueError, "endDate must not precede date"):
            updater.validate_schedule([event])

    def test_validate_schedule_rejects_invalid_calendar_date(self):
        event = copy.deepcopy(self.sample)
        event["endDate"] = "2026-02-30"
        with self.assertRaisesRegex(ValueError, "endDate is not a valid calendar date"):
            updater.validate_schedule([event])

    def test_update_days_away_removes_expired_and_keeps_ongoing(self):
        expired = copy.deepcopy(self.sample)
        expired.update(id="expired-test", date="2026-09-27", endDate="2026-09-29")
        ongoing = copy.deepcopy(self.sample)
        ongoing.update(id="ongoing-test", date="2026-09-29", endDate="2026-10-02", daysAway=99)
        with patch("builtins.print"):
            result = updater.update_days_away([expired, ongoing], base_date=date(2026, 9, 30))
        self.assertEqual([event["id"] for event in result], ["ongoing-test"])
        self.assertEqual(result[0]["daysAway"], 0)

    def test_infer_region(self):
        self.assertEqual(updater.infer_region("高雄市茄萣區"), "南部")
        self.assertEqual(updater.infer_region("花蓮縣壽豐鄉"), "東部")
        self.assertEqual(updater.infer_region("海外"), "未分類")

    def test_culture_candidates_from_mock_records(self):
        records = [{
            "title": "傳統歌仔戲《測試戲》", "masterUnit": "測試劇團", "category": "戲劇",
            "showInfo": [{"time": "2026/10/11 19:00", "locationName": "高雄市茄萣區金鑾宮"}],
        }]
        candidates = updater.culture_candidates(records, today=date(2026, 9, 30))
        self.assertEqual(len(candidates), 1)
        self.assertEqual(candidates[0]["verifyStatus"], "pending")
        self.assertEqual(candidates[0]["region"], "南部")
        self.assertEqual(candidates[0]["date"], "2026-10-11")

    def test_opentix_program_id(self):
        self.assertEqual(updater.opentix_program_id({"link": "https://www.opentix.life/event/123456"}), "123456")
        self.assertEqual(updater.opentix_program_id({"sourceUrl": "https://www.opentix.life/program/98765"}), "98765")
        self.assertIsNone(updater.opentix_program_id({"link": "https://example.com/event/123"}))

    def test_fetch_latest_updates_succeeds_after_fixture_expiration(self):
        for today in (date(2026, 10, 7), date(2027, 1, 1)):
            with self.subTest(today=today), tempfile.TemporaryDirectory() as temp_dir:
                schedule_path = Path(temp_dir) / "schedule.json"
                metadata_path = Path(temp_dir) / "metadata.json"
                schedule_path.write_text(json.dumps([copy.deepcopy(self.sample)], ensure_ascii=False), encoding="utf-8")
                with patch.object(updater, "DATA_PATH", str(schedule_path)), \
                        patch.object(updater, "METADATA_PATH", str(metadata_path)), \
                        patch.object(updater, "MOC_CANDIDATES_PATH", str(Path(temp_dir) / "moc.json")), \
                        patch.object(updater, "fetch_culture_events", return_value=[]), \
                        patch.object(updater, "taiwan_today", return_value=today), \
                        patch.dict("os.environ", {}, clear=True), \
                        patch("builtins.print"):
                    updater.fetch_latest_updates()
                written = json.loads(schedule_path.read_text(encoding="utf-8"))
                self.assertEqual(written, [])
                self.assertTrue(metadata_path.exists())

    def test_fetch_latest_updates_retains_fixture_on_event_date(self):
        today = date(2026, 10, 1)
        with tempfile.TemporaryDirectory() as temp_dir:
            schedule_path = Path(temp_dir) / "schedule.json"
            metadata_path = Path(temp_dir) / "metadata.json"
            schedule_path.write_text(json.dumps([copy.deepcopy(self.sample)], ensure_ascii=False), encoding="utf-8")
            with patch.object(updater, "DATA_PATH", str(schedule_path)), \
                    patch.object(updater, "METADATA_PATH", str(metadata_path)), \
                    patch.object(updater, "MOC_CANDIDATES_PATH", str(Path(temp_dir) / "moc.json")), \
                    patch.object(updater, "fetch_culture_events", return_value=[]), \
                    patch.object(updater, "taiwan_today", return_value=today), \
                    patch.dict("os.environ", {}, clear=True), \
                    patch("builtins.print"):
                updater.fetch_latest_updates()
            written = json.loads(schedule_path.read_text(encoding="utf-8"))
            self.assertEqual(len(written), 1)
            self.assertEqual(written[0]["id"], self.sample["id"])
            self.assertEqual(written[0]["daysAway"], 0)


if __name__ == "__main__":
    unittest.main()
