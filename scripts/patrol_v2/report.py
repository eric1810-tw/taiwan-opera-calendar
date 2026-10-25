"""每輪報告、收據、影子比對（新系統提案 vs agy 實際變更）。"""
import json
import subprocess
from pathlib import Path

from .common import ROOT, now, read_json, sha256_file

STATE_ZH = {"complete": "完整", "partial": "部分", "failed": "失敗", "pending": "未讀"}


def _rows(table):
    return "\n".join("| " + " | ".join(str(c).replace("|", "／").replace("\n", " ") for c in row) + " |" for row in table)


def _short(text, n=80):
    text = " ".join(str(text or "").split())
    return text if len(text) <= n else text[: n - 1] + "…"


def report_path(st, work_root):
    if st.mode == "production":
        return ROOT / "docs" / "patrols" / f"PATROL_{st.run_id}_INDEPENDENT.md"
    return st.dir / "report.md"


def write_report(st, work_root, progress_run):
    d = st.data
    stats = d.get("stats", {})
    check = read_json(st.dir / "check.json", {}) or {}
    applied = read_json(st.dir / "apply.json", []) or []
    review = read_json(st.dir / "review.json", {}) or {}
    pub = d.get("publication") or {}
    lines = [f"# 巡檢報告 {st.run_id}（patrol-v2，{ {'production': '正式', 'dry-run': '試跑（不推送）', 'shadow': '影子（只出提案）'}[st.mode] }）", ""]
    if d.get("forEric"):
        lines += ["## 需要 Eric 決定", ""] + [f"- {x}" for x in d["forEric"]] + [""]
    counts = (progress_run or {}).get("sources", {})
    n = {k: sum(1 for s in counts.values() if s.get("state") == k) for k in STATE_ZH}
    lines += ["## 結論", "",
              _rows([["項目", "結果"], ["---", "---"],
                     ["執行", f"開始 {d['startedAt']}；結果 {d.get('outcome') or '進行中'}；步驟 " + "、".join(f"{k}:{v.get('status')}" for k, v in d['steps'].items())],
                     ["來源", f"{len(counts)} 個：完整 {n['complete']}、部分 {n['partial']}、失敗 {n['failed']}、未讀 {n['pending']}"],
                     ["資料", f"送判讀 {stats.get('pack', {}).get('posts', 0)} 篇／圖 {stats.get('pack', {}).get('images', 0)} 張；"
                              f"變更提案 {len(check.get('accepted', []))}、確認一致 {len(check.get('confirmed', []))}、待查 {len(check.get('needsCheck', []))}、退回 {len(check.get('rejected', []))}、漏處置 {len(check.get('missing', []))}"],
                     ["寫入", f"寫入 {sum(1 for r in applied if r.get('exit') == 0)}、add_card 拒絕 {sum(1 for r in applied if r.get('exit') not in (0, None))}、審查未通過 {sum(1 for r in applied if r.get('result') == 'held')}"],
                     ["發布", pub.get("state", "本模式不發布" if st.mode != "production" else "未執行")
                              + (f"；SHA {pub.get('sha')}" if pub.get("sha") else "") + (f"；Actions {pub.get('actionsRun')}" if pub.get("actionsRun") else "")
                              + (f"；原因 {pub.get('reason')}" if pub.get("reason") else "")]]), ""]
    models = {**d.get("models", {}), **(read_json(st.dir / "models.json", {}) or {})}
    lines += ["## 模型與用量", "",
              _rows([["角色", "模型", "依據"], ["---", "---", "---"]] +
                    ([[k, v.get("model"), v.get("evidence")] for k, v in models.items()] or [["（未記錄）", "", ""]])), "",
              f"- 判讀批次 {stats.get('pack', {}).get('batches', 0)}；送出貼文 {stats.get('pack', {}).get('posts', 0)} 篇、圖片 {stats.get('pack', {}).get('images', 0)} 張、正文約 {stats.get('pack', {}).get('approxChars', 0)} 字",
              f"- 略過（已判讀未變動）{stats.get('pack', {}).get('skipped', {}).get('unchanged-judged', 0)} 篇；窗口外 {stats.get('pack', {}).get('skipped', {}).get('out-of-window', 0)} 篇",
              f"- 第二次審查：{'有' if review else '無'}（{len(review.get('verdicts', []))} 項）", ""]
    lines += ["## 來源", "", _rows([["來源", "狀態", "範圍", "說明"], ["---", "---", "---", "---"]] +
                                  [[k, STATE_ZH.get(v.get("state"), v.get("state")), _short((v.get("attempts") or [{}])[-1].get("scope"), 120),
                                    _short((v.get("attempts") or [{}])[-1].get("detail"), 100)] for k, v in counts.items()]), ""]
    ot = stats.get("opentix", {})
    lines += [f"- OPENTIX：sitemap {ot.get('sitemapEvents', '?')} 個活動、本輪有變 {ot.get('changed', '?')}、抓取 {ot.get('fetched', '?')}、"
              f"戲曲相關且未過期 {ot.get('related', '?')}、延後 {ot.get('deferred', 0)}、錯誤 {ot.get('errors', ot.get('error', 0))}", ""]
    if check.get("accepted"):
        lines += ["## 卡片變更", "", _rows([["編號", "動作", "來源", "內容", "差異", "審查", "寫入"], ["---"] * 7] + [
            [c["changeId"], c["action"] + ("（由「一致」轉）" if c.get("convertedFrom") else ""), c.get("url") or c["postKey"],
             _short(f"{c['event'].get('troupe')}｜{c['event'].get('title')}｜{c['event'].get('location')}｜" +
                    "、".join(f"{s['date']} {s.get('kind', '')} {s.get('time', '')}" for s in c["event"].get("sessions") or []), 120),
             _short("；".join(f"{x['field']}：卡 {x['card']} → 文 {x['post']}" for x in c.get("diffs") or []), 120),
             next((f"{v['verdict']}：{_short(v.get('reason'), 60)}" for v in review.get("verdicts", []) if v["changeId"] == c["changeId"]), "—"),
             next((f"{r.get('result')} {','.join(r.get('reasons') or [])}" for r in applied if r["changeId"] == c["changeId"]), "—")]
            for c in check["accepted"]]), ""]
    if check.get("needsCheck") or check.get("rejected") or check.get("missing"):
        lines += ["## 待查與退回", "", _rows([["類別", "貼文", "原因", "說明"], ["---"] * 4] +
                                         [["待查", x.get("url") or x["postKey"], x.get("reason"), _short(x.get("detail") or x.get("notes") or "", 100)] for x in check.get("needsCheck", [])] +
                                         [["退回", x.get("url") or x["postKey"], x.get("reason"), ""] for x in check.get("rejected", [])] +
                                         [["漏處置", x["postKey"], x.get("reason"), ""] for x in check.get("missing", [])]), ""]
    if d.get("shadowCompare"):
        lines += [f"影子比對：{d['shadowCompare']}", ""]
    lines += ["## 紀錄檔", "", f"- 本輪狀態：{st.path}", f"- 巡檢紀錄：patrol_runs/{st.run_id}.json（{work_root}）",
              f"- 證據：patrol_evidence/{st.run_id}/", f"- 產生時間：{now()}", ""]
    path = report_path(st, work_root)
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text("\n".join(lines), encoding="utf-8")
    return path


def write_receipt(st):
    pub = st.data.get("publication") or {}
    cmp = pub.get("comparePublic") or {}
    lines = [f"# 發布收據 {st.run_id}（patrol-v2）", "",
             f"- 狀態：{pub.get('state')}", f"- 資料提交 SHA：{pub.get('sha')}",
             f"- Actions：{pub.get('actionsRun')} {pub.get('actionsUrl') or ''}",
             f"- 公開三檔一致：{cmp.get('allMatch')}"]
    for rel, r in (cmp.get("files") or {}).items():
        lines.append(f"  - {rel}：{'一致' if r.get('match') else '不一致'} {r.get('localSha', '')}")
    lines += [f"- 原因：{pub.get('reason')}" if pub.get("reason") else "", f"- 產生時間：{now()}", ""]
    path = ROOT / "docs" / "patrols" / f"PATROL_{st.run_id}_RECEIPT.md"
    path.write_text("\n".join(lines), encoding="utf-8")
    return path


def agy_changes(day, root=ROOT, runner=None):
    """當日 agy 對 schedule.json 的實際變更（只看 origin/main 上非 patrol-v2 的巡檢提交）"""
    def git(args):
        return subprocess.run(["git", *args], cwd=root, capture_output=True, text=True).stdout
    runner = runner or git
    log = runner(["log", "origin/main", f"--since={day}T00:00:00+08:00", "--format=%H\t%s", "--", "data/schedule.json"]).strip().splitlines()
    commits = [l.split("\t", 1) for l in log if "\t" in l]
    commits = [(h, s) for h, s in commits if "patrol" in s and "patrol-v2" not in s or "補正" in s]
    if not commits:
        return {"commits": [], "added": [], "removed": [], "changed": []}
    newest, oldest = commits[0][0], commits[-1][0]

    def load(ref):
        out = runner(["show", f"{ref}:data/schedule.json"])
        try:
            return {c["id"]: c for c in json.loads(out)}
        except Exception:
            return {}
    before, after = load(f"{oldest}^"), load(newest)
    fields = ("date", "endDate", "time", "location", "title", "troupe")
    changed = [{"id": k, "diff": {f: [before[k].get(f), after[k].get(f)] for f in fields if before[k].get(f) != after[k].get(f)}}
               for k in after if k in before and any(before[k].get(f) != after[k].get(f) for f in fields)]
    return {"commits": [s for _, s in commits], "added": [after[k] for k in after if k not in before],
            "removed": [before[k] for k in before if k not in after], "changed": changed}


def shadow_compare(st, root=ROOT):
    check = read_json(st.dir / "check.json", {}) or {}
    agy = agy_changes(st.data["day"], root)
    ours = check.get("accepted", [])
    lines = [f"# 影子比對 {st.run_id}", "", f"agy 當日巡檢提交：{len(agy['commits'])} 筆", ""]
    lines += ["## agy 實際變更", ""]
    confirmed_ids = {x.get("targetCardId") for x in check.get("confirmed", [])}
    touched_ids = {x.get("proposed", {}).get("targetCardId") for x in check.get("needsCheck", []) if isinstance(x.get("proposed"), dict)}
    for c in agy["added"]:
        hit = [o["changeId"] for o in ours if o["action"] == "add" and o["event"].get("troupe") == c.get("troupe")
               and any(s["date"] == c["date"] for s in o["event"].get("sessions") or [])]
        hit += [o["changeId"] for o in ours if o["event"].get("targetCardId") == c["id"]]
        if c["id"] in confirmed_ids:
            hit.append("已在表且逐欄一致（影子在 agy 之後執行，讀到 agy 建好的卡）")
        elif c["id"] in touched_ids:
            hit.append("對到此卡但列待查（見報告）")
        lines.append(f"- 新增 {c['id']}｜{c['date']}｜{c.get('troupe')}｜{c.get('title')}｜{c.get('location')} → 新系統：{'、'.join(hit) or '沒有對應提案'}")
    for c in agy["changed"]:
        hit = [o["changeId"] for o in ours if o["event"].get("targetCardId") == c["id"]]
        lines.append(f"- 修改 {c['id']}：{json.dumps(c['diff'], ensure_ascii=False)} → 新系統：{'、'.join(hit) or '沒有對應提案'}")
    for c in agy["removed"]:
        lines.append(f"- 移除 {c['id']}｜{c['date']}｜{c.get('title')}（可能為過期清理）")
    lines += ["", "## 新系統提案（agy 沒做的）", ""]
    agy_ids = {c["id"] for c in agy["changed"]}
    for o in ours:
        if o["action"] != "add" and o["event"].get("targetCardId") in agy_ids:
            continue
        if o["action"] == "add" and any(c.get("troupe") == o["event"].get("troupe") and any(s["date"] == c["date"] for s in o["event"].get("sessions") or []) for c in agy["added"]):
            continue
        lines.append(f"- {o['changeId']} {o['action']}｜{o.get('url')}｜{o['event'].get('troupe')}｜{o['event'].get('title')}｜"
                     + "、".join(f"{s['date']} {s.get('time')}" for s in o['event'].get('sessions') or [])
                     + (f"｜差異 {json.dumps(o.get('diffs'), ensure_ascii=False)}" if o.get("diffs") else ""))
    lines += ["", f"待查 {len(check.get('needsCheck', []))} 項、退回 {len(check.get('rejected', []))} 項（見報告）", ""]
    path = st.dir / "shadow_compare.md"
    path.write_text("\n".join(lines), encoding="utf-8")
    return path
