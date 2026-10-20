#!/usr/bin/env python3
"""
tests/test_add_card.py - 測試 scripts/add_card.py 的 13 個嚴格檢查案例
"""

import json
import os
import subprocess
import sys
import tempfile
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
ADD_CARD_SCRIPT = ROOT / "scripts" / "add_card.py"


class TestAddCard(unittest.TestCase):
    def setUp(self):
        self.temp_dir = tempfile.TemporaryDirectory()
        self.base_dir = Path(self.temp_dir.name)
        self.schedule_path = self.base_dir / "schedule.json"
        self.review_queue_path = self.base_dir / "review_queue.json"
        self.cancelled_path = self.base_dir / "cancelled_cards.jsonl"
        self.fb_accounts_path = self.base_dir / "facebook_accounts.json"
        self.evidence_dir = self.base_dir / "evidence"
        self.evidence_dir.mkdir(parents=True, exist_ok=True)

        self.fb_accounts = [
            {"handle": "MingHuaYuanTianTaiwaneseOpera", "name": "明華園天字戲劇團", "url": "https://www.facebook.com/MingHuaYuanTianTaiwaneseOpera"}
        ]
        self.fb_accounts_path.write_text(json.dumps(self.fb_accounts, ensure_ascii=False), encoding="utf-8")

        # 初始卡片（含 luo-2026-10-23-wuyingdian 與其他卡片）
        self.initial_schedule = [
            {
                "id": "luo-2026-10-23-wuyingdian",
                "date": "2026-10-23",
                "endDate": "2026-10-24",
                "dateFormatted": "2026/10/23–2026/10/24",
                "daysAway": 4,
                "time": "未公布；請洽劇團或廟方",
                "troupe": "鶯藝歌劇團",
                "genre": "歌仔戲",
                "artist": "鶯藝歌劇團",
                "title": "農曆九月戲路｜台南南廠武英殿",
                "category": "廟會民俗演出",
                "badgeType": "temple",
                "verifyStatus": "community",
                "verifyLabel": "📣 羅裕誴歌劇團 Threads 行程公告",
                "location": "臺南市南廠武英殿（詳細地址未列）",
                "region": "南部",
                "status": "劇團行程公告列 10/23–10/24；演出時間未列",
                "description": "原說明",
                "link": "https://www.threads.com/@yuzhongluo/post/DeqRSuNGRfu",
                "sourceUrl": "https://www.threads.com/@yuzhongluo/post/DeqRSuNGRfu",
                "tags": ["鶯藝歌劇團"]
            }
        ]
        self.schedule_path.write_text(json.dumps(self.initial_schedule, ensure_ascii=False), encoding="utf-8")

    def tearDown(self):
        self.temp_dir.cleanup()

    def run_cmd(self, extra_args):
        cmd = [
            sys.executable,
            str(ADD_CARD_SCRIPT),
            "--schedule", str(self.schedule_path),
            "--review-queue", str(self.review_queue_path),
            "--cancelled", str(self.cancelled_path),
            "--facebook-accounts", str(self.fb_accounts_path),
            "--today", "2026-10-19",
        ] + extra_args
        proc = subprocess.run(cmd, capture_output=True, text=True)
        try:
            out_json = json.loads(proc.stdout.strip())
        except Exception:
            out_json = {"stdout": proc.stdout, "stderr": proc.stderr}
        return proc.returncode, out_json

    def test_01_update_wuyingdian_address_pass(self):
        """1. 鶯藝補地址：對既有卡 luo-2026-10-23-wuyingdian 執行 --update，location 改成「台南市大智街135號（南廠武英殿）」→ 通過（原值含「未列」）"""
        evidence_file = self.evidence_dir / "threads_yuzhongluo.json"
        text = "下一站 農曆9月14、15日~國曆10月23、24日 地點：台南市大智街135號~南廠武英殿 鶯藝歌劇團 安排好戲登場~歡迎來看戲"
        post_url = "https://www.threads.com/@yuzhongluo/post/DeqRSuNGRfu"
        evidence_file.write_text(json.dumps({
            "source": "threads:yuzhongluo",
            "posts": [{"permalink": post_url, "datetime": "2026-10-15T12:00:00+08:00", "text": text}]
        }, ensure_ascii=False), encoding="utf-8")

        proposal_file = self.base_dir / "prop01.json"
        proposal_file.write_text(json.dumps({
            "source": "threads:yuzhongluo",
            "postUrl": post_url,
            "quote": "地點：台南市大智街135號~南廠武英殿",
            "location": "台南市大智街135號（南廠武英殿）"
        }, ensure_ascii=False), encoding="utf-8")

        code, out = self.run_cmd(["--update", "luo-2026-10-23-wuyingdian", "--proposal", str(proposal_file), "--evidence-dir", str(self.evidence_dir)])
        self.assertEqual(code, 0)
        self.assertEqual(out.get("result"), "updated")

        # 檢查 schedule 內的卡片確實更新，且原 sourceUrl 移到 relatedSourceUrls
        cards = json.loads(self.schedule_path.read_text(encoding="utf-8"))
        updated_card = next(c for c in cards if c["id"] == "luo-2026-10-23-wuyingdian")
        self.assertEqual(updated_card["location"], "台南市大智街135號（南廠武英殿）")
        self.assertIn("relatedSourceUrls", updated_card)

    def test_02_fake_location_rejected(self):
        """2. 編造地點：提案 location 為「臺南文化中心 原生劇場」，但 quote 裡沒有 → 拒絕，原因含 location"""
        post_url = "https://www.threads.com/@someone/post/1"
        self.evidence_dir.joinpath("threads_someone.json").write_text(json.dumps({
            "posts": [{"permalink": post_url, "datetime": "2026-10-19T10:00:00+08:00", "text": "10月25日 演出在歸仁文化中心"}]
        }, ensure_ascii=False), encoding="utf-8")

        prop_file = self.base_dir / "prop.json"
        prop_file.write_text(json.dumps({
            "source": "threads:someone",
            "postUrl": post_url,
            "quote": "10月25日 演出在歸仁文化中心",
            "date": "2026-10-25",
            "troupe": "明華園天字戲劇團",
            "title": "歸仁公演戲路",
            "location": "臺南文化中心 原生劇場",
            "time": "未公布",
            "badgeType": "temple"
        }, ensure_ascii=False), encoding="utf-8")

        code, out = self.run_cmd(["--proposal", str(prop_file), "--evidence-dir", str(self.evidence_dir)])
        self.assertNotEqual(code, 0)
        self.assertEqual(out.get("result"), "rejected")
        self.assertTrue(any("location" in r for r in out.get("reasons", [])))

    def test_03_fake_time_rejected(self):
        """3. 編造時間：time 為「14:30」，但 quote 只寫 15:00 → 拒絕"""
        post_url = "https://www.threads.com/@someone/post/1"
        self.evidence_dir.joinpath("threads_someone.json").write_text(json.dumps({
            "posts": [{"permalink": post_url, "datetime": "2026-10-19T10:00:00+08:00", "text": "10月25日 15:00 歸仁文化中心 明華園天字戲劇團"}]
        }, ensure_ascii=False), encoding="utf-8")

        prop_file = self.base_dir / "prop.json"
        prop_file.write_text(json.dumps({
            "source": "threads:someone",
            "postUrl": post_url,
            "quote": "10月25日 15:00 歸仁文化中心 明華園天字戲劇團",
            "date": "2026-10-25",
            "troupe": "明華園天字戲劇團",
            "title": "歸仁戲路",
            "location": "歸仁文化中心",
            "time": "14:30",
            "badgeType": "temple"
        }, ensure_ascii=False), encoding="utf-8")

        code, out = self.run_cmd(["--proposal", str(prop_file), "--evidence-dir", str(self.evidence_dir)])
        self.assertNotEqual(code, 0)
        self.assertEqual(out.get("result"), "rejected")
        self.assertTrue(any("time" in r for r in out.get("reasons", [])))

    def test_04_lunar_only_rejected(self):
        """4. 只有農曆：quote 只寫「農曆9月14日」→ 拒絕 lunar-only"""
        post_url = "https://www.threads.com/@someone/post/1"
        self.evidence_dir.joinpath("threads_someone.json").write_text(json.dumps({
            "posts": [{"permalink": post_url, "datetime": "2026-10-19T10:00:00+08:00", "text": "農曆9月14日 歸仁文化中心 明華園天字戲劇團"}]
        }, ensure_ascii=False), encoding="utf-8")

        prop_file = self.base_dir / "prop.json"
        prop_file.write_text(json.dumps({
            "source": "threads:someone",
            "postUrl": post_url,
            "quote": "農曆9月14日 歸仁文化中心 明華園天字戲劇團",
            "date": "2026-10-23",
            "troupe": "明華園天字戲劇團",
            "title": "歸仁戲路",
            "location": "歸仁文化中心",
            "time": "未公布",
            "badgeType": "temple"
        }, ensure_ascii=False), encoding="utf-8")

        code, out = self.run_cmd(["--proposal", str(prop_file), "--evidence-dir", str(self.evidence_dir)])
        self.assertNotEqual(code, 0)
        self.assertEqual(out.get("result"), "rejected")
        self.assertIn("lunar-only", out.get("reasons", []))

    def test_05_quote_not_in_evidence_rejected(self):
        """5. quote 不在證據裡 → 拒絕"""
        post_url = "https://www.threads.com/@someone/post/1"
        self.evidence_dir.joinpath("threads_someone.json").write_text(json.dumps({
            "posts": [{"permalink": post_url, "datetime": "2026-10-19T10:00:00+08:00", "text": "今天天氣很好"}]
        }, ensure_ascii=False), encoding="utf-8")

        prop_file = self.base_dir / "prop.json"
        prop_file.write_text(json.dumps({
            "source": "threads:someone",
            "postUrl": post_url,
            "quote": "10月25日 歸仁文化中心 明華園天字戲劇團",
            "date": "2026-10-25",
            "troupe": "明華園天字戲劇團",
            "title": "歸仁戲路",
            "location": "歸仁文化中心",
            "time": "未公布",
            "badgeType": "temple"
        }, ensure_ascii=False), encoding="utf-8")

        code, out = self.run_cmd(["--proposal", str(prop_file), "--evidence-dir", str(self.evidence_dir)])
        self.assertNotEqual(code, 0)
        self.assertEqual(out.get("result"), "rejected")
        self.assertIn("quote-not-in-post", out.get("reasons", []))

    def test_06_duplicate_rejected(self):
        """6. 重複：同日、同劇團的新提案 → 不新增"""
        post_url = "https://www.threads.com/@someone/post/1"
        self.evidence_dir.joinpath("threads_someone.json").write_text(json.dumps({
            "posts": [{"permalink": post_url, "datetime": "2026-10-19T10:00:00+08:00", "text": "10月23日 南廠武英殿 鶯藝歌劇團 精彩好戲"}]
        }, ensure_ascii=False), encoding="utf-8")

        prop_file = self.base_dir / "prop.json"
        prop_file.write_text(json.dumps({
            "source": "threads:someone",
            "postUrl": post_url,
            "quote": "10月23日 南廠武英殿 鶯藝歌劇團",
            "date": "2026-10-23",
            "troupe": "鶯藝歌劇團",
            "title": "農曆九月戲路",
            "location": "南廠武英殿",
            "time": "未公布",
            "badgeType": "temple"
        }, ensure_ascii=False), encoding="utf-8")

        code, out = self.run_cmd(["--proposal", str(prop_file), "--evidence-dir", str(self.evidence_dir)])
        self.assertNotEqual(code, 0)
        self.assertEqual(out.get("result"), "rejected")
        self.assertIn("duplicate", out.get("reasons", []))

    def test_07_from_moc_pass(self):
        """7. --from-moc 用 mock 紀錄（《我,哪吒》的 showInfo：華山1914文創園區東3B館 烏梅劇院／臺北市中正區八德路一段1號／2026/12/05 15:00、12/06 15:00）→ 產出的卡片 location、time、date、endDate 與紀錄完全一致"""
        mock_records = [
            {
                "title": "《我,哪吒》",
                "masterUnit": "偶戲團",
                "webSales": "https://www.opentix.life/event/12345678",
                "showInfo": [
                    {"time": "2026/12/05 15:00", "location": "臺北市中正區八德路一段1號", "locationName": "華山1914文創園區東3B館 烏梅劇院"},
                    {"time": "2026/12/06 15:00", "location": "臺北市中正區八德路一段1號", "locationName": "華山1914文創園區東3B館 烏梅劇院"}
                ]
            }
        ]
        rec_file = self.base_dir / "moc_mock.json"
        rec_file.write_text(json.dumps(mock_records, ensure_ascii=False), encoding="utf-8")

        code, out = self.run_cmd(["--from-moc", "《我,哪吒》", "--culture-records", str(rec_file)])
        self.assertEqual(code, 0)
        self.assertEqual(out.get("result"), "added")

        cards = json.loads(self.schedule_path.read_text(encoding="utf-8"))
        card = next(c for c in cards if c["title"] == "《我,哪吒》")
        self.assertEqual(card["location"], "華山1914文創園區東3B館 烏梅劇院（臺北市中正區八德路一段1號）")
        self.assertEqual(card["date"], "2026-12-05")
        self.assertEqual(card["endDate"], "2026-12-06")
        self.assertEqual(card["time"], "15:00")

    def test_08_from_moc_exhibition_rejected(self):
        """8. --from-moc 標題含「展」→ 拒絕 not-performance"""
        mock_records = [
            {
                "title": "傳統偶戲特展",
                "showInfo": [{"time": "2026/11/01 10:00", "locationName": "某展覽館"}]
            }
        ]
        rec_file = self.base_dir / "moc_mock.json"
        rec_file.write_text(json.dumps(mock_records, ensure_ascii=False), encoding="utf-8")

        code, out = self.run_cmd(["--from-moc", "傳統偶戲特展", "--culture-records", str(rec_file)])
        self.assertNotEqual(code, 0)
        self.assertEqual(out.get("result"), "rejected")
        self.assertIn("not-performance", out.get("reasons", []))

    def test_09_fake_artist_rejected(self):
        """9. 編造主演：artist 為「孫翠鳳」，但 quote 沒有這三個字 → 拒絕"""
        post_url = "https://www.threads.com/@someone/post/1"
        self.evidence_dir.joinpath("threads_someone.json").write_text(json.dumps({
            "posts": [{"permalink": post_url, "datetime": "2026-10-19T10:00:00+08:00", "text": "10月25日 歸仁文化中心 明華園天字戲劇團 精彩好戲"}]
        }, ensure_ascii=False), encoding="utf-8")

        prop_file = self.base_dir / "prop.json"
        prop_file.write_text(json.dumps({
            "source": "threads:someone",
            "postUrl": post_url,
            "quote": "10月25日 歸仁文化中心 明華園天字戲劇團",
            "date": "2026-10-25",
            "troupe": "明華園天字戲劇團",
            "artist": "孫翠鳳",
            "title": "歸仁戲路",
            "location": "歸仁文化中心",
            "time": "未公布",
            "badgeType": "temple"
        }, ensure_ascii=False), encoding="utf-8")

        code, out = self.run_cmd(["--proposal", str(prop_file), "--evidence-dir", str(self.evidence_dir)])
        self.assertNotEqual(code, 0)
        self.assertEqual(out.get("result"), "rejected")
        self.assertTrue(any("artist" in r for r in out.get("reasons", [])))

    def test_10_badge_type_free_without_keyword_rejected(self):
        """10. badgeType 為 free，但 quote 沒有「免費」→ 拒絕"""
        post_url = "https://www.threads.com/@someone/post/1"
        self.evidence_dir.joinpath("threads_someone.json").write_text(json.dumps({
            "posts": [{"permalink": post_url, "datetime": "2026-10-19T10:00:00+08:00", "text": "10月25日 歸仁文化中心 明華園天字戲劇團 歡迎來看戲"}]
        }, ensure_ascii=False), encoding="utf-8")

        prop_file = self.base_dir / "prop.json"
        prop_file.write_text(json.dumps({
            "source": "threads:someone",
            "postUrl": post_url,
            "quote": "10月25日 歸仁文化中心 明華園天字戲劇團",
            "date": "2026-10-25",
            "troupe": "明華園天字戲劇團",
            "title": "歸仁戲路",
            "location": "歸仁文化中心",
            "time": "未公布",
            "badgeType": "free"
        }, ensure_ascii=False), encoding="utf-8")

        code, out = self.run_cmd(["--proposal", str(prop_file), "--evidence-dir", str(self.evidence_dir)])
        self.assertNotEqual(code, 0)
        self.assertEqual(out.get("result"), "rejected")
        self.assertTrue(any("badgeType" in r for r in out.get("reasons", [])))

    def test_11_from_moc_multiple_venues(self):
        """11. --from-moc mock 一筆有 3 個場館的紀錄（唐美雲《南都幽靈夜譚》的型態）→ 產出 3 張卡，各自的場館與日期正確"""
        mock_records = [
            {
                "title": "唐美雲《南都幽靈夜譚》",
                "masterUnit": "唐美雲歌仔戲團",
                "webSales": "https://www.opentix.life/event/9999",
                "showInfo": [
                    {"time": "2026/11/10 19:30", "location": "台北市中山南路21-1號", "locationName": "國家戲劇院"},
                    {"time": "2026/11/20 19:30", "location": "台中市西屯區惠來路二段101號", "locationName": "台中國家歌劇院大劇院"},
                    {"time": "2026/11/30 19:30", "location": "高雄市鳳山區三多一路1號", "locationName": "衛武營國家藝術文化中心歌劇院"}
                ]
            }
        ]
        rec_file = self.base_dir / "moc_mock.json"
        rec_file.write_text(json.dumps(mock_records, ensure_ascii=False), encoding="utf-8")

        code, out = self.run_cmd(["--from-moc", "唐美雲《南都幽靈夜譚》", "--culture-records", str(rec_file)])
        self.assertEqual(code, 0)
        self.assertEqual(out.get("result"), "added")
        self.assertEqual(out.get("count"), 3)

        cards = json.loads(self.schedule_path.read_text(encoding="utf-8"))
        moc_cards = [c for c in cards if "南都幽靈夜譚" in c["title"]]
        self.assertEqual(len(moc_cards), 3)
        venues = {c["location"] for c in moc_cards}
        self.assertTrue(any("國家戲劇院" in v for v in venues))
        self.assertTrue(any("台中國家歌劇院" in v for v in venues))
        self.assertTrue(any("衛武營" in v for v in venues))

    def test_12_change_event(self):
        """12. --change：同帳號、含「異動」、新時間出現在 quote → 通過，description 留下舊值；不同帳號 → 拒絕"""
        post_url_same = "https://www.threads.com/@yuzhongluo/post/DeqRSuNGRfu"
        post_url_diff = "https://www.threads.com/@otheruser/post/2"

        self.evidence_dir.joinpath("threads_otheruser.json").write_text(json.dumps({
            "posts": [
                {"permalink": post_url_diff, "datetime": "2026-10-18T10:00:00+08:00", "text": "南廠武英殿演出時間異動為 19:30 開演"}
            ]
        }, ensure_ascii=False), encoding="utf-8")
        self.evidence_dir.joinpath("threads_yuzhongluo.json").write_text(json.dumps({
            "posts": [
                {"permalink": post_url_same, "datetime": "2026-10-18T10:00:00+08:00", "text": "南廠武英殿演出時間異動為 19:30 開演"}
            ]
        }, ensure_ascii=False), encoding="utf-8")

        # 不同帳號測試
        prop_diff = self.base_dir / "prop_diff.json"
        prop_diff.write_text(json.dumps({
            "source": "threads:otheruser",
            "postUrl": post_url_diff,
            "quote": "南廠武英殿演出時間異動為 19:30 開演",
            "time": "19:30"
        }, ensure_ascii=False), encoding="utf-8")

        code, out = self.run_cmd(["--change", "luo-2026-10-23-wuyingdian", "--proposal", str(prop_diff), "--evidence-dir", str(self.evidence_dir)])
        self.assertNotEqual(code, 0)
        self.assertIn("different-account", out.get("reasons", []))

        # 同帳號測試
        prop_same = self.base_dir / "prop_same.json"
        prop_same.write_text(json.dumps({
            "source": "threads:yuzhongluo",
            "postUrl": post_url_same,
            "quote": "南廠武英殿演出時間異動為 19:30 開演",
            "time": "19:30"
        }, ensure_ascii=False), encoding="utf-8")

        code, out = self.run_cmd(["--change", "luo-2026-10-23-wuyingdian", "--proposal", str(prop_same), "--evidence-dir", str(self.evidence_dir)])
        self.assertEqual(code, 0)
        self.assertEqual(out.get("result"), "changed")

        cards = json.loads(self.schedule_path.read_text(encoding="utf-8"))
        card = next(c for c in cards if c["id"] == "luo-2026-10-23-wuyingdian")
        self.assertEqual(card["time"], "19:30")
        self.assertIn("異動公告更正", card["description"])

    def test_13_cancel_event(self):
        """13. --cancel：同帳號、含「取消」與該卡日期 → 卡片被移除，並寫入 cancelled_cards.jsonl；quote 不含「取消」→ 拒絕"""
        post_url_no_keyword = "https://www.threads.com/@yuzhongluo/post/cancel1"
        post_url_cancel = "https://www.threads.com/@yuzhongluo/post/cancel2"

        self.evidence_dir.joinpath("threads_yuzhongluo.json").write_text(json.dumps({
            "posts": [
                {"permalink": post_url_no_keyword, "datetime": "2026-10-18T10:00:00+08:00", "text": "10/23 武英殿因雨暫停"},
                {"permalink": post_url_cancel, "datetime": "2026-10-18T10:00:00+08:00", "text": "10/23 南廠武英殿演出因故取消，請大家見諒"}
            ]
        }, ensure_ascii=False), encoding="utf-8")

        # quote 不含取消關鍵字測試
        prop_no_kw = self.base_dir / "prop_no_kw.json"
        prop_no_kw.write_text(json.dumps({
            "source": "threads:yuzhongluo",
            "postUrl": post_url_no_keyword,
            "quote": "10/23 武英殿因雨暫停"
        }, ensure_ascii=False), encoding="utf-8")

        code, out = self.run_cmd(["--cancel", "luo-2026-10-23-wuyingdian", "--proposal", str(prop_no_kw), "--evidence-dir", str(self.evidence_dir)])
        self.assertNotEqual(code, 0)
        self.assertIn("no-cancel-keyword", out.get("reasons", []))

        # 含取消關鍵字與卡片日期
        prop_ok = self.base_dir / "prop_ok.json"
        prop_ok.write_text(json.dumps({
            "source": "threads:yuzhongluo",
            "postUrl": post_url_cancel,
            "quote": "10/23 南廠武英殿演出因故取消，請大家見諒"
        }, ensure_ascii=False), encoding="utf-8")

        code, out = self.run_cmd(["--cancel", "luo-2026-10-23-wuyingdian", "--proposal", str(prop_ok), "--evidence-dir", str(self.evidence_dir)])
        self.assertEqual(code, 0)
        self.assertEqual(out.get("result"), "cancelled")

        cards = json.loads(self.schedule_path.read_text(encoding="utf-8"))
        self.assertFalse(any(c["id"] == "luo-2026-10-23-wuyingdian" for c in cards))
        self.assertTrue(self.cancelled_path.exists())
        cancelled_content = self.cancelled_path.read_text(encoding="utf-8")
        self.assertIn("luo-2026-10-23-wuyingdian", cancelled_content)

    def test_14_scoped_source_and_postkey_lookup(self):
        """14. 兩個不同 source 的證據檔，都有一篇 url 為 photo 的貼文；以 postKey 提案時，必須找到正確 source 的那一篇"""
        from scripts.add_card import load_post_from_evidence

        post_a = {"postKey": "facebook:sourceA:hashA", "url": "https://www.facebook.com/photo/", "text": "A 的貼文"}
        post_b = {"postKey": "facebook:sourceB:hashB", "url": "https://www.facebook.com/photo/", "text": "B 的貼文"}

        (self.evidence_dir / "facebook_sourceA.json").write_text(json.dumps({"posts": [post_a]}, ensure_ascii=False), encoding="utf-8")
        (self.evidence_dir / "facebook_sourceB.json").write_text(json.dumps({"posts": [post_b]}, ensure_ascii=False), encoding="utf-8")

        found_a = load_post_from_evidence(self.evidence_dir, source="facebook:sourceA", post_key="facebook:sourceA:hashA")
        self.assertIsNotNone(found_a)
        self.assertEqual(found_a["text"], "A 的貼文")

        found_b = load_post_from_evidence(self.evidence_dir, source="facebook:sourceB", post_key="facebook:sourceB:hashB")
        self.assertIsNotNone(found_b)
        self.assertEqual(found_b["text"], "B 的貼文")

        # 若在 sourceA 找 post_key_B 應回傳 None
        wrong = load_post_from_evidence(self.evidence_dir, source="facebook:sourceA", post_key="facebook:sourceB:hashB")
        self.assertIsNone(wrong)

    def test_15_lanyang_real_fixture_pass(self):
        """15. 用蘭陽真實原文當 fixture，提案 date=2026-10-26、time=19:00、location 桃園顯安巖，--today 2026-10-20 → 通過"""
        lanyang_text = (
            "10/26（一）晚上7:00\n"
            "劇目｜《錯配姻緣》\n"
            "地點｜桃園顯安巖顯應祖師廟\n"
            "（桃園市龜山區樂善里樂安街1號）\n"
            "※免費觀賞\n"
            "以上場次均無直播"
        )
        post_key = "facebook:lanyang.opera:a732ac4abaa5"
        (self.evidence_dir / "facebook_lanyang.opera.json").write_text(json.dumps({
            "posts": [{
                "postKey": post_key,
                "url": "",
                "text": lanyang_text,
                "datetime": "2026-10-18T10:00:00+08:00"
            }]
        }, ensure_ascii=False), encoding="utf-8")

        # 更新 fb_accounts
        accounts = json.loads(self.fb_accounts_path.read_text(encoding="utf-8"))
        accounts.append({"handle": "lanyang.opera", "name": "蘭陽戲劇團", "url": "https://www.facebook.com/lanyang.opera/"})
        self.fb_accounts_path.write_text(json.dumps(accounts, ensure_ascii=False), encoding="utf-8")

        prop_file = self.base_dir / "prop_lanyang.json"
        prop_file.write_text(json.dumps({
            "source": "facebook:lanyang.opera",
            "postKey": post_key,
            "date": "2026-10-26",
            "time": "19:00",
            "location": "桃園市龜山區樂善里樂安街1號（桃園顯安巖顯應祖師廟）",
            "troupe": "蘭陽戲劇團",
            "title": "錯配姻緣",
            "badgeType": "free",
            "quote": "10/26（一）晚上7:00\n劇目｜《錯配姻緣》\n地點｜桃園顯安巖顯應祖師廟\n（桃園市龜山區樂善里樂安街1號）\n※免費觀賞"
        }, ensure_ascii=False), encoding="utf-8")

        code, out = self.run_cmd(["--proposal", str(prop_file), "--evidence-dir", str(self.evidence_dir), "--today", "2026-10-20"])
        self.assertEqual(code, 0, f"Expected 0 but got {code}, out: {out}")
        self.assertEqual(out.get("result"), "added")

        cards = json.loads(self.schedule_path.read_text(encoding="utf-8"))
        added_card = next(c for c in cards if c["title"] == "錯配姻緣")
        self.assertEqual(added_card["date"], "2026-10-26")
        self.assertEqual(added_card["time"], "19:00")
        self.assertEqual(added_card["badgeType"], "free")
        # 貼文無 url 時自動替換為粉專首頁
        self.assertEqual(added_card["link"], "https://www.facebook.com/lanyang.opera/")

    def test_16_lanyang_wrong_source_rejected_post_not_found(self):
        """16. 同樣的蘭陽提案，但 source 寫成 facebook:mhysun → 拒絕 post-not-found"""
        lanyang_text = (
            "10/26（一）晚上7:00\n"
            "劇目｜《錯配姻緣》\n"
            "地點｜桃園顯安巖顯應祖師廟\n"
            "（桃園市龜山區樂善里樂安街1號）\n"
            "※免費觀賞\n"
            "以上場次均無直播"
        )
        post_key = "facebook:lanyang.opera:a732ac4abaa5"
        (self.evidence_dir / "facebook_lanyang.opera.json").write_text(json.dumps({
            "posts": [{
                "postKey": post_key,
                "url": "",
                "text": lanyang_text
            }]
        }, ensure_ascii=False), encoding="utf-8")

        prop_file = self.base_dir / "prop_lanyang_wrong.json"
        prop_file.write_text(json.dumps({
            "source": "facebook:mhysun",
            "postKey": post_key,
            "date": "2026-10-26",
            "time": "19:00",
            "location": "桃園市龜山區樂善里樂安街1號（桃園顯安巖顯應祖師廟）",
            "troupe": "蘭陽戲劇團",
            "title": "錯配姻緣",
            "badgeType": "free",
            "quote": "10/26（一）晚上7:00\n劇目｜《錯配姻緣》\n地點｜桃園顯安巖顯應祖師廟\n（桃園市龜山區樂善里樂安街1號）\n※免費觀賞"
        }, ensure_ascii=False), encoding="utf-8")

        code, out = self.run_cmd(["--proposal", str(prop_file), "--evidence-dir", str(self.evidence_dir), "--today", "2026-10-20"])
        self.assertNotEqual(code, 0)
        self.assertIn("post-not-found", out.get("reasons", []))

    def test_17_moc_records_stale_rejected(self):
        """17. moc_records 過期（> 36 小時）時，--from-moc 拒絕 moc-records-stale"""
        stale_file = self.base_dir / "moc_stale.json"
        stale_file.write_text(json.dumps({
            "fetchedAt": "2026-10-18T10:00:00+08:00",
            "total": 1400,
            "records": [{"title": "某某歌仔戲公演"}]
        }, ensure_ascii=False), encoding="utf-8")

        code, out = self.run_cmd(["--from-moc", "某某歌仔戲公演", "--culture-records", str(stale_file), "--today", "2026-10-20"])
        self.assertNotEqual(code, 0)
        self.assertIn("moc-records-stale", out.get("reasons", []))

    def test_18_fresh_moc_records_adds_card(self):
        """18. 新鮮的 moc_records → 能依標題建卡，事實欄位全部來自紀錄"""
        from datetime import datetime, timezone, timedelta
        now_iso = datetime.now(timezone(timedelta(hours=8))).isoformat(timespec="seconds")
        fresh_file = self.base_dir / "moc_fresh.json"
        fresh_record = {
            "title": "金鷹閣電視木偶劇團《西遊記之鬧天宮》",
            "masterUnit": "金鷹閣電視木偶劇團",
            "startDate": "2026/10/25",
            "webSales": "https://www.opentix.life/program/2090773654423490561",
            "showInfo": [{
                "time": "2026/10/25 16:00",
                "location": "高雄市岡山區岡山南路43號",
                "locationName": "高雄市岡山文化中心演藝廳",
                "price": "300,500"
            }]
        }
        fresh_file.write_text(json.dumps({
            "fetchedAt": now_iso,
            "total": 1474,
            "records": [fresh_record]
        }, ensure_ascii=False), encoding="utf-8")

        code, out = self.run_cmd(["--from-moc", "金鷹閣電視木偶劇團《西遊記之鬧天宮》", "--culture-records", str(fresh_file), "--today", "2026-10-20"])
        self.assertEqual(code, 0, f"Expected 0, out: {out}")
        self.assertEqual(out.get("result"), "added")

        cards = json.loads(self.schedule_path.read_text(encoding="utf-8"))
        added = next(c for c in cards if "鬧天宮" in c["title"])
        self.assertEqual(added["date"], "2026-10-25")
        self.assertEqual(added["time"], "16:00")
        self.assertEqual(added["troupe"], "金鷹閣電視木偶劇團")
        self.assertIn("高雄市岡山文化中心演藝廳", added["location"])


if __name__ == "__main__":
    unittest.main()
