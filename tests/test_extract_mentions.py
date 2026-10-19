import json
import shutil
import tempfile
import unittest
from pathlib import Path

from scripts.extract_mentions import check_mention, extract_mentions


class TestExtractMentions(unittest.TestCase):
    def setUp(self):
        self.test_dir = tempfile.mkdtemp()

    def tearDown(self):
        shutil.rmtree(self.test_dir, ignore_errors=True)

    def test_case_date(self):
        # 1. 有日期（例如 10/26 或 農曆）
        res1 = check_mention("10/26 大家記得來看")
        self.assertIsNotNone(res1)
        self.assertIn("date", res1)

        res2 = check_mention("農曆九月歡迎來看戲")
        self.assertIsNotNone(res2)
        self.assertIn("date", res2)

    def test_case_keyword(self):
        # 2. 有關鍵字（無日期，但有「扮仙」、「公演」等）
        res = check_mention("今晚於廟前盛大公演，歡慶熱鬧")
        self.assertIsNotNone(res)
        self.assertIn("keyword", res)

    def test_case_poster_only(self):
        # 3. 只有海報（字數小於 40 字，且有圖片，無日期與關鍵字）
        res = check_mention("精采瞬間分享！", images=["https://example.com/poster.jpg"])
        self.assertEqual(res, "poster-only")

    def test_case_neither(self):
        # 4. 都沒有（長文普通生活動態，無關鍵字與日期）
        res = check_mention("今天天氣真好，大家吃了早餐沒？祝大家平安順心每一天。")
        self.assertIsNone(res)

    def test_case_empty_and_integration(self):
        # 5. 空檔或空貼文
        p = Path(self.test_dir)
        # 建立一個空 JSON 檔案
        with open(p / "facebook_empty.json", "w", encoding="utf-8") as f:
            json.dump({"posts": []}, f)

        # 建立一個有符合貼文的檔案
        with open(p / "facebook_troupe.json", "w", encoding="utf-8") as f:
            json.dump({
                "posts": [
                    {"url": "https://example.com/p1", "text": "10/26 晚上7:00 劇目《錯配姻緣》", "images": []},
                    {"url": "https://example.com/p2", "text": "大家早安！", "images": []}
                ]
            }, f)

        mentions = extract_mentions(self.test_dir)
        self.assertEqual(len(mentions), 1)
        self.assertEqual(mentions[0]["postUrl"], "https://example.com/p1")
        self.assertIn("錯配姻緣", mentions[0]["text"])

        # 確認 mentions.json 確實被寫出
        self.assertTrue((p / "mentions.json").is_file())
        with open(p / "mentions.json", "r", encoding="utf-8") as f:
            saved = json.load(f)
            self.assertEqual(len(saved), 1)


if __name__ == '__main__':
    unittest.main()
