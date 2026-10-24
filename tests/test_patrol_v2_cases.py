"""patrol-v2 回歸案例（設計稿 §10 的 21 個案例，取自 2026-10-19～10-24 真實錯誤）。

案例 1、2、7 的讀取器部分在 tests/test_social_capture.mjs（含動態列表的 Edge 實測）；
這裡測 Python 端的判定、驗證、寫入、狀態機與發布防呆。
"""
import json
import subprocess
import sys
import tempfile
import unittest
from datetime import date, datetime, timedelta
from pathlib import Path
from unittest import mock

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "scripts"))
sys.path.insert(0, str(ROOT))

import add_card  # noqa: E402
import patrol  # noqa: E402
import patrol_progress  # noqa: E402
from patrol_v2 import apply as apply_mod  # noqa: E402
from patrol_v2 import evidence, preflight, publish, state  # noqa: E402
from patrol_v2.common import TPE, text_revision  # noqa: E402
from patrol_v2.validate import validate_batch  # noqa: E402

TODAY = date(2026, 10, 23)

SHUIMEN_TEXT = (" 演出時間異動公告 因薔琵來勢洶洶 演出時間調整如下 今天10/23 下午 3:30 開始扮仙 接著連續演出至下午 6:30 左右 "
                "另外，因戲台遭受毀損 演出地點改至廟內進行 請大家留意唷！ 南廠水門宫 時間：10/23-10/24 地點：台南市南區仁南街86號 "
                "10/24 演出時間下午5:00開始扮仙接著演出 顯示較少")
SHUIMEN_URL = "https://www.facebook.com/photo/?fbid=1650076190464636"
SHUIMEN_CARD = {
    "id": "mhy-tian-2026-10-23-shuimen", "date": "2026-10-23", "endDate": "2026-10-24",
    "dateFormatted": "國曆：2026/10/23（五）–2026/10/24（六）", "daysAway": 0,
    "time": "未公布；請洽劇團或廟方", "troupe": "明華園天字戲劇團", "genre": "歌仔戲", "artist": "未公布",
    "title": "水門宮外台｜劇目未公布", "category": "廟口外台", "badgeType": "temple", "verifyStatus": "community",
    "verifyLabel": "📣", "location": "臺南市南區文南里仁南街86號（水門宮）", "region": "南部", "status": "x",
    "description": "x", "link": SHUIMEN_URL, "sourceUrl": SHUIMEN_URL, "tags": ["明華園天字戲劇團"],
}
XINYING_OLD_TEXT = ("yuzhongluo 羅裕誴歌劇團 2026-10-14 南瀛藝術節 10月24日（六）下午3點~薪瀛舞台展演 新營文化中心演藝廳前 "
                    "八方傳統藝陣創新藝團 八家將+聖王再現 44 2 1")
XINYING_CARD = {
    "id": "auto-20261024-84da22bc", "date": "2026-10-24", "dateFormatted": "2026/10/24", "daysAway": 1, "time": "16:30",
    "troupe": "羅裕誴歌劇團", "genre": "歌仔戲", "artist": "未公布", "title": "府城有神・人間有情", "category": "戶外公演",
    "badgeType": "outdoor", "verifyStatus": "community", "verifyLabel": "📣", "location": "新營文化中心演藝廳前「薪瀛舞台」",
    "region": "南部", "status": "x", "description": "x", "link": "https://www.threads.com/@yuzhongluo/post/De1UV_Ikxkl",
    "sourceUrl": "https://www.threads.com/@yuzhongluo/post/De1UV_Ikxkl", "tags": ["羅裕誴歌劇團"],
}
SUNHOPE_TEXT = (" 尚和秋冬開演啦！！！ 外部公演 9/20（日）《紅塵觀音－戶外版》 10/11（日）《正庄・千波之神》 11/29（日）《西遊記之芭蕉密碼》 "
                "田和越・茶劇場 10/24（六）《茶靈系列》下午沉浸式茶戲體驗 11/7（六）－11/8（日）《寒窯之外》 "
                "詳細時間、地點及購票／報名方式，請依圖片資訊為準 #尚和歌仔戲劇團 #歌仔戲")


def item(post_key, text, url="", dt=None, images=None, source=None):
    it = {"postKey": post_key, "source": source or ":".join(post_key.split(":")[:2]), "url": url, "datetime": dt,
          "text": text, "images": images or [], "knownImageReadings": []}
    it["revision"] = text_revision(text, [i["sha256"] for i in images or []])
    return it


def pack_of(*items):
    return {"batch": 1, "items": list(items), "cards": []}


def disp(it, decision, events=(), reason="測試"):
    return {"postKey": it["postKey"], "revision": it["revision"], "decision": decision, "reason": reason, "events": list(events)}


def shuimen_event(action="confirm", sessions=None, location="台南市南區仁南街86號（水門宮廟內）"):
    return {
        "action": action, "targetCardId": SHUIMEN_CARD["id"], "genre": "歌仔戲", "eventType": "演出",
        "troupe": "明華園天字戲劇團", "title": "水門宮外台演出", "location": location,
        "sessions": sessions or [{"date": "2026-10-23", "kind": "扮仙", "time": "15:30"},
                                 {"date": "2026-10-24", "kind": "扮仙", "time": "17:00"}],
        "quote": SHUIMEN_TEXT.strip(), "evidence": [{"field": "sessions[1].time", "quote": "10/24 演出時間下午5:00開始扮仙"}],
    }


class CaseReader(unittest.TestCase):
    def test_01_02_21_social_state_failed_on_invariant_or_zero(self):
        # 案例1／2：守門帳號已知貼文不在輸出 → failed（不得回報成功）
        self.assertEqual(patrol.social_state({"posts": 9, "problems": ["known-post-missing"]}), "failed")
        self.assertEqual(patrol.social_state({"posts": 9, "problems": ["first-screen-lost"]}), "failed")
        # 案例21：1013.yr_ 0 篇 → failed
        self.assertEqual(patrol.social_state({"posts": 0, "problems": []}), "failed")
        self.assertEqual(patrol.social_state({"posts": 9, "problems": []}), "partial")

    def test_01_old_evidence_lacks_known_posts(self):
        data = json.loads((ROOT / "tests/fixtures/patrol_v2/threads_yuzhongluo_2026-10-24_0304.json").read_text(encoding="utf-8"))
        keys = {p["postKey"] for p in data["posts"]}
        watch = json.loads((ROOT / "scripts/patrol_v2/watch.json").read_text(encoding="utf-8"))
        self.assertIn("threads:yuzhongluo:De1UV_Ikxkl", {p["postKey"] for p in watch["threads:yuzhongluo"]})
        self.assertNotIn("threads:yuzhongluo:De1UV_Ikxkl", keys)


class CaseJudgment(unittest.TestCase):
    def test_03_shuimen_two_days_two_times_moved_inside(self):
        it = item("facebook:100063868113954:1650076190464636", SHUIMEN_TEXT, SHUIMEN_URL)
        res = validate_batch(pack_of(it), {"dispositions": [disp(it, "already-listed", [shuimen_event()])]}, [SHUIMEN_CARD], TODAY)
        self.assertEqual(res["confirmed"], [], "有差異不得列為一致")
        self.assertEqual(len(res["accepted"]), 1)
        change = res["accepted"][0]
        self.assertEqual(change["convertedFrom"], "confirm")
        self.assertIn("time", {d["field"] for d in change["diffs"]})
        # 經 add_card 寫入：兩天各自時間、扮仙標示
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            (root / "data").mkdir()
            (root / "docs/patrols").mkdir(parents=True)
            (root / "data/schedule.json").write_text(json.dumps([SHUIMEN_CARD], ensure_ascii=False), encoding="utf-8")
            (root / "data/facebook_accounts.json").write_text("[]", encoding="utf-8")
            edir = root / "ev"
            edir.mkdir()
            (edir / "facebook_100063868113954.json").write_text(json.dumps({"posts": [{"postKey": it["postKey"], "url": SHUIMEN_URL, "text": SHUIMEN_TEXT}]}, ensure_ascii=False), encoding="utf-8")
            change["changeId"] = "chg-001"
            out = apply_mod.apply_changes([change], {"chg-001": {"verdict": "approve"}}, root, edir, "2026-10-23",
                                          {it["postKey"]: "facebook:100063868113954"})
            self.assertEqual(out[0].get("exit"), 0, out)
            card = json.loads((root / "data/schedule.json").read_text(encoding="utf-8"))[0]
            self.assertEqual(card["time"], "10/23 15:30 扮仙、10/24 17:00 扮仙")
            self.assertEqual([s["time"] for s in card["sessions"]], ["15:30", "17:00"])

    def test_04_xinying_old_post_15_vs_card_1630(self):
        it = item("threads:yuzhongluo:DeeXP_umU6t", XINYING_OLD_TEXT, "https://www.threads.com/@yuzhongluo/post/DeeXP_umU6t",
                  "2026-10-14T20:16:54+08:00")
        ev = {"action": "confirm", "targetCardId": XINYING_CARD["id"], "genre": "歌仔戲", "eventType": "演出",
              "troupe": "羅裕誴歌劇團", "title": "南瀛藝術節演出", "location": "新營文化中心演藝廳前",
              "sessions": [{"date": "2026-10-24", "kind": "正戲", "time": "15:00"}], "quote": XINYING_OLD_TEXT}
        res = validate_batch(pack_of(it), {"dispositions": [disp(it, "already-listed", [ev])]}, [XINYING_CARD], TODAY)
        self.assertEqual(res["confirmed"], [])
        self.assertEqual(res["accepted"][0]["action"], "change")
        self.assertEqual(res["accepted"][0]["diffs"][0]["field"], "time")

    def test_05_wangfu_no_show_date(self):
        fields = add_card.format_sessions(
            [{"date": d, "kind": "正戲", "time": "未公布"} for d in ("2026-11-06", "2026-11-08", "2026-11-09", "2026-11-10")],
            ["2026-11-07"])
        self.assertEqual(fields["dateFormatted"], "2026/11/06、2026/11/08–2026/11/10（11/7 無演出）")
        self.assertEqual((fields["date"], fields["endDate"]), ("2026-11-06", "2026-11-10"))
        text = "王福宮 11/6–11/10 演出，11/7 休息無演出 地點：基隆市安樂區湖海路二段192號"
        it = item("facebook:x:1", text)
        ev = {"action": "add", "genre": "歌仔戲", "eventType": "演出", "troupe": "某劇團", "title": "王福宮演出",
              "location": "基隆市安樂區湖海路二段192號", "sessions": [{"date": "2026-11-07", "kind": "正戲", "time": "未公布"}],
              "noShowDates": ["2026-11-07"], "quote": text}
        res = validate_batch(pack_of(it), {"dispositions": [disp(it, "new", [ev])]}, [], TODAY)
        self.assertEqual(res["accepted"], [])
        self.assertIn("session-on-no-show-date", res["needsCheck"][0]["reason"])

    def test_06_little_fox_is_not_budaixi(self):
        text = "節目：偶偶偶劇團《小狐狸買手套》 場次：2026-12-04 19:30｜地點：文山劇場 簡介：親子 多元偶戲"
        it = item("opentix:2088104133013299200", text, "https://www.opentix.life/event/2088104133013299200", source="opentix:2088104133013299200")
        ev = {"action": "add", "genre": "布袋戲", "eventType": "演出", "troupe": "偶偶偶劇團", "title": "《小狐狸買手套》",
              "location": "文山劇場", "sessions": [{"date": "2026-12-04", "kind": "正戲", "time": "19:30"}], "quote": text}
        res = validate_batch(pack_of(it), {"dispositions": [disp(it, "new", [ev])]}, [], TODAY)
        self.assertEqual(res["accepted"], [])
        self.assertIn("puppet-not-budaixi", res["needsCheck"][0]["reason"])

    def test_13_14_sunhope_each_show_and_tea_experience(self):
        it = item("facebook:sunhope.fans:1716331140498595", SUNHOPE_TEXT, "https://www.facebook.com/photo/?fbid=1716331140498595")
        q1 = "11/29（日）《西遊記之芭蕉密碼》"
        q2 = "田和越・茶劇場 10/24（六）《茶靈系列》下午沉浸式茶戲體驗"
        base = {"genre": "歌仔戲", "troupe": "尚和歌仔戲劇團", "badgeType": "plan"}
        events = [
            {**base, "action": "add", "eventType": "演出", "title": "《西遊記之芭蕉密碼》", "location": "未公布",
             "sessions": [{"date": "2026-11-29", "kind": "正戲", "time": "未公布"}], "quote": q1},
            {**base, "action": "add", "eventType": "體驗", "title": "《茶靈系列》", "location": "田和越・茶劇場",
             "sessions": [{"date": "2026-10-24", "kind": "其他", "time": "未公布"}], "quote": q2},
        ]
        res = validate_batch(pack_of(it), {"dispositions": [disp(it, "new", events)]}, [], TODAY)
        self.assertEqual(len(res["accepted"]), 2, res)
        self.assertEqual(res["accepted"][1]["event"]["eventType"], "體驗")
        # 沒交代這篇 → 漏處置
        res2 = validate_batch(pack_of(it), {"dispositions": []}, [], TODAY)
        self.assertEqual(res2["missing"][0]["postKey"], it["postKey"])

    def test_15_threads_pager_is_not_a_date(self):
        text = "歡迎大家先記下時間🙌 我們戲台下相見！ 1 / 2 478 18 25 9"
        it = item("threads:the_rin.lpm:DdvZekJE9Mm", text)
        ev = {"action": "add", "genre": "歌仔戲", "eventType": "演出", "troupe": "x", "title": "戲台演出", "location": "戲台",
              "sessions": [{"date": "2027-01-02", "kind": "正戲", "time": "未公布"}], "quote": text}
        res = validate_batch(pack_of(it), {"dispositions": [disp(it, "new", [ev])]}, [], date(2026, 12, 20))
        self.assertEqual(res["accepted"], [])
        self.assertIn("date-not-in-quote", res["needsCheck"][0]["reason"])

    def test_16_same_show_two_accounts_one_card(self):
        t = "10/30 19:00 某某宮 尚和歌仔戲劇團 演出"
        a, b = item("threads:a:1", t, "https://a"), item("threads:b:2", t, "https://b")
        ev = {"action": "add", "genre": "歌仔戲", "eventType": "演出", "troupe": "尚和歌仔戲劇團", "title": "某某宮演出",
              "location": "某某宮", "sessions": [{"date": "2026-10-30", "kind": "正戲", "time": "19:00"}], "quote": t}
        res = validate_batch(pack_of(a, b), {"dispositions": [disp(a, "new", [ev]), disp(b, "new", [ev])]}, [], TODAY)
        self.assertEqual(len(res["accepted"]), 1)
        self.assertEqual(res["accepted"][0]["alsoSources"], ["https://b"])

    def test_17_same_day_same_place_different_troupe_not_merged(self):
        t = "10/30 19:00 某某宮 新劇團 演出"
        it = item("threads:a:1", t)
        card = {**SHUIMEN_CARD, "id": "c1", "date": "2026-10-30", "troupe": "別的劇團", "location": "某某宮"}
        card.pop("endDate")
        ev = {"action": "add", "genre": "歌仔戲", "eventType": "演出", "troupe": "新劇團", "title": "某某宮演出",
              "location": "某某宮", "sessions": [{"date": "2026-10-30", "kind": "正戲", "time": "19:00"}], "quote": t}
        res = validate_batch(pack_of(it), {"dispositions": [disp(it, "new", [ev])]}, [card], TODAY)
        self.assertEqual(len(res["accepted"]), 1)

    def test_18_fabricated_quote_rejected(self):
        it = item("threads:a:1", "今天天氣很好")
        ev = {"action": "add", "genre": "歌仔戲", "eventType": "演出", "troupe": "x", "title": "x演出", "location": "x",
              "sessions": [{"date": "2026-10-30", "kind": "正戲", "time": "19:00"}], "quote": "10/30 19:00 x 演出"}
        res = validate_batch(pack_of(it), {"dispositions": [disp(it, "new", [ev])]}, [], TODAY)
        self.assertIn("quote-not-in-post", res["rejected"][0]["reason"])

    def test_poster_reading_must_exist_for_image_facts(self):
        img = {"sha256": "a" * 64, "file": "/tmp/x.jpg"}
        it = item("facebook:x:9", "秋季戲路表如圖", images=[img])
        q = "11/2 19:30 某宮 某劇團"
        ev = {"action": "add", "genre": "歌仔戲", "eventType": "演出", "troupe": "某劇團", "title": "某宮演出", "location": "某宮",
              "sessions": [{"date": "2026-11-02", "kind": "正戲", "time": "19:30"}], "quote": q}
        no_reading = validate_batch(pack_of(it), {"dispositions": [disp(it, "new", [ev])]}, [], TODAY)
        self.assertIn("quote-not-in-post", no_reading["rejected"][0]["reason"])
        self.assertEqual(no_reading["needsCheck"][0]["reason"], "image-not-read")
        with_reading = validate_batch(pack_of(it), {"imageReadings": [{"sha256": "a" * 64, "legible": True, "reading": "第1列 " + q}],
                                                    "dispositions": [disp(it, "new", [ev])]}, [], TODAY)
        self.assertEqual(len(with_reading["accepted"]), 1)


class CaseCache(unittest.TestCase):
    def test_19_unchanged_post_not_resent_edit_resent(self):
        with tempfile.TemporaryDirectory() as tmp:
            store = evidence.EvidenceStore(tmp)
            now_dt = datetime(2026, 10, 24, 5, tzinfo=TPE)
            post = {"postKey": "threads:a:1", "text": "10/30 演出", "datetime": "2026-10-23T10:00:00+08:00", "media": []}
            sel, _ = evidence.select_for_judgment([dict(post)], store, now_dt, "r1")
            self.assertEqual(len(sel), 1)
            store.remember_judgment(sel[0]["revision"], post["postKey"], {"decision": "not-event"}, "r1")
            sel2, skipped = evidence.select_for_judgment([dict(post)], store, now_dt, "r2")
            self.assertEqual(sel2, [])
            self.assertEqual(skipped["unchanged-judged"], 1)
            sel3, _ = evidence.select_for_judgment([{**post, "text": "10/30 演出 改至廟內"}], store, now_dt, "r3")
            self.assertEqual(len(sel3), 1)
            self.assertEqual(sel3[0]["changeStatus"], "changed")


class CaseRunControl(unittest.TestCase):
    def test_08_same_day_second_trigger_is_done(self):
        with tempfile.TemporaryDirectory() as tmp:
            st = state.RunState.create("dry-run", tmp)
            state.acquire_lock(st.run_id, tmp)
            st.finish("ok")
            again = state.find_today("dry-run", tmp)
            self.assertTrue(again.data["finished"])
            with self.assertRaises(FileExistsError):
                state.RunState.create("dry-run", tmp, at=datetime.fromisoformat(st.data["startedAt"]))

    def test_09_live_lock_blocks_stale_lock_taken_over(self):
        with tempfile.TemporaryDirectory() as tmp:
            state.acquire_lock("run-a", tmp)
            with self.assertRaises(state.LockBusy):
                state.acquire_lock("run-b", tmp)
            later = datetime.now(TPE) + timedelta(minutes=30)
            previous = state.acquire_lock("run-b", tmp, at=later)
            self.assertEqual(previous["runId"], "run-a")

    def test_10_network_failure_bounded_retry(self):
        calls = []

        def runner(args, cwd=None, check=True):
            calls.append(args)
            raise preflight.PreflightError("Could not resolve host: github.com")
        with self.assertRaises(preflight.PreflightError) as ctx:
            preflight.fetch_with_retry(runner=runner, wait=0)
        self.assertEqual(len(calls), 3)
        self.assertIn("連續失敗", str(ctx.exception))

    def test_20_not_on_main_stops(self):
        def runner(args, cwd=None, check=True):
            return {"rev-parse": "wip/011"}.get(args[0], "")
        with self.assertRaises(preflight.PreflightError) as ctx:
            preflight.check_production(runner=runner)
        self.assertIn("不在 main", str(ctx.exception))

    def test_20_ff_failure_stops(self):
        def runner(args, cwd=None, check=True):
            if args[0] == "merge":
                raise preflight.PreflightError("fatal: Not possible to fast-forward, aborting.")
            return "main" if args[0] == "rev-parse" else ""
        with self.assertRaises(preflight.PreflightError):
            preflight.check_production(runner=runner)


class CasePublish(unittest.TestCase):
    def test_11_actions_other_sha_not_accepted(self):
        api = lambda path: {"workflow_runs": [{"id": 1, "head_sha": "other", "path": publish.WORKFLOW_PATH,  # noqa: E731
                                               "status": "completed", "conclusion": "success"}]}
        with self.assertRaises(publish.PublishError):
            publish.wait_for_actions("abc123", api=api, timeout=0, interval=1, sleep=lambda s: None)

    def test_11_failed_actions_raises(self):
        api = lambda path: {"workflow_runs": [{"id": 2, "head_sha": "abc", "path": publish.WORKFLOW_PATH,  # noqa: E731
                                               "status": "completed", "conclusion": "failure"}]}
        with self.assertRaises(publish.PublishError):
            publish.wait_for_actions("abc", api=api, timeout=0, interval=1, sleep=lambda s: None)

    def test_12_public_files_stale_not_match(self):
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            for rel in patrol_progress.PUBLIC_FILES:
                (root / rel).parent.mkdir(parents=True, exist_ok=True)
                (root / rel).write_text("new", encoding="utf-8")
            res = patrol_progress.compare_public(root=root, fetcher=lambda url: b"old")
            self.assertFalse(res["allMatch"])

    def test_forbidden_git_and_exact_staging(self):
        with self.assertRaises(publish.PublishError):
            publish.git(["add", "."])
        with self.assertRaises(publish.PublishError):
            publish.git(["push", "--force", "origin", "main"])
        with self.assertRaises(publish.PublishError):
            publish.stage_exact(["ISSUES_REVIEW.md"], runner=lambda *a, **k: "")
        outputs = {"add": "", "diff": "data/schedule.json\nsomething_else.md"}
        with self.assertRaises(publish.PublishError):
            publish.stage_exact(["data/schedule.json"], runner=lambda args, cwd=None: outputs[args[0]])


class CaseSessionsFormat(unittest.TestCase):
    def test_banxian_and_main_separate(self):
        f = add_card.format_sessions([{"date": "2026-10-30", "kind": "正戲", "time": "19:30"},
                                      {"date": "2026-10-30", "kind": "扮仙", "time": "19:00"}])
        self.assertEqual(f["time"], "10/30 19:00 扮仙、10/30 19:30 正戲")
        self.assertIsNone(f["endDate"])


if __name__ == "__main__":
    unittest.main()
