#!/usr/bin/env python3
"""
scripts/extract_mentions.py
從巡檢證據目錄中提取包含演出線索的貼文，輸出為 mentions.json。
純 Python 標準函式庫實作。
"""

import json
import os
import re
import sys
from pathlib import Path

DATE_PATTERNS = [
    re.compile(r'\d{1,2}/\d{1,2}'),
    re.compile(r'\d{1,2}月\d{1,2}日'),
    re.compile(r'農曆'),
    re.compile(r'國曆'),
]

KEYWORDS = [
    '演出', '公演', '戲路', '扮仙', '開演',
    '售票', '索票', '地點', '劇目', '戲碼',
    '日戲', '夜戲'
]

def check_mention(text, images=None):
    """
    檢查一篇貼文是否提及演出線索。
    回傳 matched 類型字串；若不符合則回傳 None。
    """
    if images is None:
        images = []
    
    raw_text = text or ''
    matched_reasons = []

    for dp in DATE_PATTERNS:
        if dp.search(raw_text):
            matched_reasons.append('date')
            break

    for kw in KEYWORDS:
        if kw in raw_text:
            matched_reasons.append('keyword')
            break

    if matched_reasons:
        return '+'.join(matched_reasons)

    # 只有海報檢查：去除空白後少於 40 字，且 images 非空
    clean_text = re.sub(r'\s+', '', raw_text)
    if len(clean_text) < 40 and len(images) > 0:
        return 'poster-only'

    return None

def extract_mentions(evidence_dir):
    """
    掃描 evidence_dir 下的所有 .json 檔案（排除 mentions.json 本身），
    抽取符合條件的貼文，並寫入 mentions.json。
    """
    evidence_path = Path(evidence_dir)
    if not evidence_path.is_dir():
        raise FileNotFoundError(f"證據目錄不存在: {evidence_dir}")

    mentions = []

    # 依檔名排序處理
    json_files = sorted(evidence_path.glob('*.json'))
    for jf in json_files:
        if jf.name == 'mentions.json':
            continue

        try:
            with open(jf, 'r', encoding='utf-8') as f:
                data = json.load(f)
        except Exception:
            continue

        # 取得 source key（通常來自檔名，例如 facebook_lanyang.opera.json -> facebook:lanyang.opera）
        source_key = jf.stem.replace('_', ':', 1)
        posts = data.get('posts', [])
        if not isinstance(posts, list):
            continue

        for post in posts:
            text = post.get('text', '')
            images = post.get('images', [])
            matched = check_mention(text, images)
            if matched:
                mentions.append({
                    'source': source_key,
                    'postUrl': post.get('url', ''),
                    'datetime': post.get('datetime'),
                    'text': text,
                    'images': images,
                    'matched': matched
                })

    out_file = evidence_path / 'mentions.json'
    with open(out_file, 'w', encoding='utf-8') as f:
        json.dump(mentions, f, ensure_ascii=False, indent=2)

    return mentions

def main():
    if len(sys.argv) < 2:
        print("用法: python3 scripts/extract_mentions.py <evidence_dir>", file=sys.stderr)
        sys.exit(1)

    evidence_dir = sys.argv[1]
    res = extract_mentions(evidence_dir)
    print(f"成功提取 {len(res)} 篇演出貼文至 {Path(evidence_dir) / 'mentions.json'}")

if __name__ == '__main__':
    main()
