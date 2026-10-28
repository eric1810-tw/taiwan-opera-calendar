#!/usr/bin/env python3
"""每日巡檢單一入口（新後端）。

    python3 scripts/patrol.py start [--mode production|dry-run|shadow]
    python3 scripts/patrol.py next --run <runId>
    python3 scripts/patrol.py models --run <runId> --role main --model <模型> --evidence <來源>
    python3 scripts/patrol.py status [--run <runId>]
    python3 scripts/patrol.py close --run <runId> --reason <原因>

`start`／`next` 都會印出一行 JSON，告訴排程工作階段下一步：
  {"action": "judge", ...}   派判讀子代理（Sonnet／medium）寫出指定的 proposals 檔
  {"action": "review", ...}  派質疑者子代理（Opus／high）寫出 review.json
  {"action": "continue"}     背景程序還在跑（或步驟間銜接），再跑一次 next；每次 start／next 最多約 4 分鐘就回來
  {"action": "done", ...}    本輪結束（含今日已完成而直接結束）
  {"action": "stopped", ...} 前置失敗或其他無法續行的狀況，原因已寫進報告
模型不得自行改 schedule.json 或執行 git；寫入與發布都只由本程式進行。
"""
import argparse
import json
import os
import signal
import subprocess
import sys
import threading
import time
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
sys.path.insert(0, str(Path(__file__).resolve().parents[1]))

import patrol_progress as progress  # noqa: E402
from patrol_v2 import apply as apply_mod  # noqa: E402
from patrol_v2 import evidence as ev_mod  # noqa: E402
from patrol_v2 import preflight, publish, report, sources  # noqa: E402
from patrol_v2.common import (EVIDENCE_DIR, ROOT, STATE_DIR, in_agy_window, now, now_dt,  # noqa: E402
                              read_json, write_json)
from patrol_v2.state import LockBusy, RunState, acquire_lock, find_today, heartbeat, missed_days  # noqa: E402
from patrol_v2.validate import validate_batch  # noqa: E402

CAPTURE = ROOT / "scripts" / "patrol_v2" / "social_capture.mjs"
WATCH = ROOT / "scripts" / "patrol_v2" / "watch.json"
JUDGE_PROMPT = "docs/patrol-v2/JUDGE_PROMPT.md"
REVIEW_PROMPT = "docs/patrol-v2/REVIEW_PROMPT.md"
CAPTURE_TIMEOUT = 40 * 60  # 社群擷取整體上限（秒）；正常約 20 分鐘


def emit(obj):
    print(json.dumps(obj, ensure_ascii=False))
    return 0


# --- 共用 ---

def work_root(st):
    return Path(st.data["workRoot"]) if st.data.get("workRoot") else ROOT


def progress_path(st):
    return work_root(st) / "patrol_runs" / f"{st.run_id}.json"


def evidence_dir(st):
    return EVIDENCE_DIR / st.run_id


def load_progress(st):
    return progress.read(progress_path(st))


def record(st, key, state, method, url, scope, media, detail):
    path = progress_path(st)
    run = progress.read(path)
    progress.record(run, key, state, method, url, scope, media, detail)
    progress.write(path, run)


def today(st):
    return st.data["day"]


# --- 步驟 ---

def step_preflight(st):
    try:
        if st.mode == "production":
            info = preflight.check_production(ROOT)
            st.data["workRoot"] = str(ROOT)
        else:
            sandbox = st.dir / "sandbox"
            info = preflight.build_sandbox(sandbox, ROOT)
            st.data["workRoot"] = str(sandbox)
    except preflight.PreflightError as error:
        st.set_step("preflight", "failed", str(error))
        st.ask_eric(f"前置檢查失敗，本輪沒有巡檢：{error}")
        return stop(st, "preflight-failed", str(error))
    st.data["preflight"] = info
    if info.get("indexLock"):
        st.log(info["indexLock"])
    st.save()
    st.set_step("preflight", "done")
    return None


def build_social_sources(targets):
    watch = read_json(WATCH, {}) or {}
    result = []
    for key, url in targets.items():
        if key.startswith("threads:"):
            result.append({"key": key, "kind": "threads", "handle": key.split(":", 1)[1], "url": url, "knownPosts": watch.get(key, [])})
        elif key.startswith("facebook:"):
            result.append({"key": key, "kind": "facebook", "handle": key.split(":", 1)[1], "url": url, "knownPosts": watch.get(key, [])})
    return result


def social_state(event):
    if event.get("error") or event.get("loginWall") or not event.get("posts"):
        return "failed"
    if set(event.get("problems") or []) & {"first-screen-lost", "known-post-missing", "first-screen-empty"}:
        return "failed"
    return "partial"


def run_capture(st, social_sources, edir):
    sources_file = st.dir / "social_sources.json"
    write_json(sources_file, social_sources)
    cmd = ["node", str(CAPTURE), "--sources", str(sources_file), "--out", str(edir), "--media", str(STATE_DIR / "media")]
    # 自成一個程序群組：逾時或本程序被結束時，連同 node 開的 Edge 一起收掉
    proc = subprocess.Popen(cmd, cwd=ROOT, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True,
                            start_new_session=True)
    expired = threading.Event()
    watchdog = threading.Timer(CAPTURE_TIMEOUT, lambda: (expired.set(), kill_group(proc)))
    watchdog.daemon = True
    watchdog.start()
    try:
        summaries = read_capture(st, proc, social_sources)
    finally:
        watchdog.cancel()
        if proc.poll() is None:
            kill_group(proc)
    err = proc.stderr.read()
    for s in social_sources:
        if s["key"] not in summaries:
            reason = f"超過 {CAPTURE_TIMEOUT // 60} 分鐘上限，已強制結束" if expired.is_set() else f"讀取器結束碼 {proc.returncode}"
            record(st, s["key"], "failed", "social-capture-v2", s["url"], "讀取器未回報此來源", "unread",
                   f"{reason}：{err.strip()[-300:] or '無錯誤訊息'}")
    return summaries, proc.returncode, err


def kill_group(proc, grace=5):
    try:
        os.killpg(proc.pid, signal.SIGTERM)
    except (ProcessLookupError, PermissionError):
        return
    try:
        proc.wait(timeout=grace)
    except subprocess.TimeoutExpired:
        try:
            os.killpg(proc.pid, signal.SIGKILL)
        except (ProcessLookupError, PermissionError):
            pass
        proc.wait()


def read_capture(st, proc, social_sources):
    summaries = {}
    for line in proc.stdout:
        line = line.strip()
        if not line.startswith("{"):
            continue
        event = json.loads(line)
        key = event["source"]
        url = next((s["url"] for s in social_sources if s["key"] == key), "")
        if event["type"] == "attempt":
            record(st, key, "failed", "social-capture-v2", event.get("url") or url,
                   f"第 {event['attempt']} 次嘗試：{event.get('posts', 0)} 篇；登入牆＝{'是' if event.get('loginWall') else '否'}；停止原因 {event.get('stopReason')}",
                   "unread", f"失敗：{event.get('error') or '、'.join(event.get('problems') or []) or '0 篇'}；換路徑重試")
            continue
        summaries[key] = event
        state = social_state(event)
        scope = (f"首屏 {event['firstScreen']} 篇、累積 {event['posts']} 篇；最新 {event.get('newestPostAt') or '無'}、最舊 {event.get('oldestPostAt') or '無'}；"
                 f"捲動 {event['scrolls']} 次、停止原因 {event.get('stopReason')}；圖片下載 {event.get('images', 0)} 張")
        detail = "不變式通過" if not event.get("problems") else "問題：" + "、".join(event["problems"])
        record(st, key, state, "social-capture-v2", url, scope, "unread", f"{detail}；證據 {event['path']}")
        heartbeat(st.run_id)
    proc.wait()
    return summaries


def write_items_evidence(edir, name, items):
    write_json(edir / f"{name}.json", {"posts": [{k: v for k, v in it.items() if k != "changedThisRun"} for it in items]})


def step_collect(st):
    root = work_root(st)
    targets = progress.targets(root)
    ppath = progress_path(st)
    if not ppath.exists():
        run = {"version": 1, "startedAt": st.data["startedAt"], "resumedAt": [], "sources": {},
               "finalizedAt": None, "publication": {"state": "pending"}, "engine": "patrol-v2"}
        progress.sync(run, targets)
        progress.write(ppath, run)
    else:
        run = progress.read(ppath)
        progress.resume(run, reason="patrol-v2 恢復續跑", current=targets)
        progress.write(ppath, run)
    edir = evidence_dir(st)
    edir.mkdir(parents=True, exist_ok=True)
    stats = st.data.setdefault("stats", {})

    # 1. 社群（Edge＋~/.patrol-edge）
    social = build_social_sources(targets)
    if st.mode != "production" and in_agy_window():
        st.set_step("collect", "failed", "02:30–04:30 為 agy 巡檢時段，非正式模式不開 ~/.patrol-edge")
        return stop(st, "agy-window", "非正式模式在 02:30–04:30 不讀社群")
    summaries, code, err = run_capture(st, social, edir)
    stats["social"] = {"sources": len(social), "reported": len(summaries), "exit": code,
                       "posts": sum(e.get("posts", 0) for e in summaries.values()),
                       "images": sum(e.get("images", 0) for e in summaries.values()),
                       "failed": [k for k, e in summaries.items() if social_state(e) == "failed"]}
    items = []
    for key, event in summaries.items():
        data = read_json(event["path"], {}) or {}
        for post in data.get("posts", []):
            post["source"] = key
            items.append(post)

    # 2. OPENTIX（含兩廳院節目）
    try:
        ot_items, ot_stats = sources.collect_opentix(STATE_DIR / "opentix_cache.json", today=today(st))
        write_items_evidence(edir, "opentix", ot_items)
        for it in ot_items:
            write_items_evidence(edir, it["source"].replace(":", "_"), [it])
        items.extend(ot_items)
        stats["opentix"] = ot_stats
    except Exception as error:
        stats["opentix"] = {"error": str(error)}
        st.ask_eric(f"OPENTIX 讀取失敗：{error}")

    # 3. 文化部
    import updater
    moc_items, moc_stats = sources.collect_moc(root / "data/moc_records.json", now_dt(), updater.is_culture_record_keyword_matched)
    write_items_evidence(edir, "culture", moc_items)
    items.extend(moc_items)
    stats["culture"] = moc_stats
    record(st, "culture", "partial", "moc-records", "data/moc_records.json",
           f"total {moc_stats['total']}、fetchedAt {moc_stats['fetchedAt']}、戲曲紀錄 {len(moc_items)} 筆",
           "not_applicable", "；".join(moc_stats["problems"]) or "資料新鮮；逐筆處置待判讀後確認")

    # 4. GitHub Issues
    issues_key = "issues"
    try:
        is_items, is_stats = sources.collect_issues()
        write_items_evidence(edir, "issues", is_items)
        items.extend(is_items)
        stats["issues"] = is_stats
        record(st, issues_key, "partial", "gh-api", targets[issues_key], f"state=all 共 {len(is_items)} 則（含留言）",
               "not_applicable", "已讀取；處置待判讀後確認")
    except Exception as error:
        stats["issues"] = {"error": str(error)}
        record(st, issues_key, "failed", "gh-api", targets[issues_key], "無法讀取", "not_applicable", str(error)[:300])

    unique = {}
    for it in items:
        unique.setdefault(it["postKey"], it)
    items = list(unique.values())
    write_json(st.dir / "items.json", items)
    st.save()
    st.set_step("collect", "done")
    return None


def step_pack(st):
    items = read_json(st.dir / "items.json", [])
    store = ev_mod.EvidenceStore()
    schedule = read_json(work_root(st) / "data/schedule.json", [])
    force = set()
    for key, posts in (read_json(WATCH, {}) or {}).items():
        force.update(p["postKey"] for p in posts if p.get("forceJudge"))
    selected, skipped = ev_mod.select_for_judgment(items, store, now_dt(), st.run_id, force)
    store.save()
    write_json(st.dir / "selected.json", selected)
    packs = ev_mod.build_batches(selected, schedule, store)
    jdir = st.dir / "judge"
    jdir.mkdir(exist_ok=True)
    batches = []
    for pack in packs:
        path = jdir / f"batch_{pack['batch']:02d}.json"
        write_json(path, pack)
        batches.append({"batch": pack["batch"], "round": 1, "pack": str(path), "output": str(jdir / f"proposals_{pack['batch']:02d}.json"),
                        "posts": len(pack["items"]), "images": 0, "imagesAvailable": sum(i["imageCount"] for i in pack["items"])})
    st.data["judgeBatches"] = batches
    st.data["stats"]["pack"] = {**ev_mod.pack_stats(packs), "skipped": skipped, "totalItems": len(items)}
    st.save()
    st.set_step("pack", "done")
    if not batches:
        st.set_step("judge", "skipped", "沒有新的或有變動的內容")
    return None


def step_judge(st):
    pending = [b for b in st.data.get("judgeBatches", []) if not Path(b["output"]).exists()]
    if pending:
        st.set_step("judge", "waiting")
        return {"action": "judge", "runId": st.run_id, "promptFile": JUDGE_PROMPT,
                "agent": {"model": "sonnet", "effort": "medium"}, "batches": pending}
    st.set_step("judge", "done")
    return None


def step_check(st):
    schedule = read_json(work_root(st) / "data/schedule.json", [])
    store = ev_mod.EvidenceStore()
    merged = {"accepted": [], "confirmed": [], "needsCheck": [], "rejected": [], "missing": []}
    disposed = set()
    from datetime import date as _date
    day = _date.fromisoformat(today(st))
    batches = st.data.get("judgeBatches", [])
    round2_keys = {i["postKey"] for b in batches if b.get("round") == 2 for i in read_json(b["pack"])["items"]}
    image_requests = []
    for b in batches:
        pack = read_json(b["pack"])
        proposals = read_json(b["output"], {}) or {}
        if b.get("round", 1) == 1 and round2_keys:
            # 第二輪看過圖的貼文，以第二輪的處置為準
            pack = {**pack, "items": [i for i in pack["items"] if i["postKey"] not in round2_keys]}
        res = validate_batch(pack, proposals, schedule, day, st.data["startedAt"][11:16])
        image_requests.extend(res["imageRequests"])
        items = {i["postKey"]: i for i in pack["items"]}
        for sha, reading in res["imageReadings"].items():
            store.remember_image(sha, reading, st.run_id)
        # 有被拒或待查事件的貼文不記為「已判讀」，下輪（仍在窗口內）會再送
        unsettled = {m["postKey"] for m in res["missing"] + res["rejected"] + res["needsCheck"]}
        for d in res["dispositions"]:
            if d["postKey"] in unsettled:
                continue
            store.remember_judgment(items[d["postKey"]]["revision"], d["postKey"], d, st.run_id)
            disposed.add(d["postKey"])
        for k in merged:
            merged[k].extend(res.get(k, []))
    store.save()
    if image_requests and not round2_keys:
        # 第二輪：只把判讀員指定要看圖的貼文連同圖片送出
        wanted = set(image_requests)
        selected = [i for i in read_json(st.dir / "selected.json", []) if i["postKey"] in wanted]
        for it in selected:
            it["pendingImages"] = [m["sha256"] for m in ev_mod.unique_media(it) if not store.image_done(m["sha256"])]
        packs = ev_mod.build_batches(selected, schedule, store, with_images=True, start=len(batches) + 1, round_no=2)
        jdir = st.dir / "judge"
        for pack in packs:
            path = jdir / f"batch_{pack['batch']:02d}.json"
            write_json(path, pack)
            batches.append({"batch": pack["batch"], "round": 2, "pack": str(path),
                            "output": str(jdir / f"proposals_{pack['batch']:02d}.json"),
                            "posts": len(pack["items"]), "images": sum(len(i["images"]) for i in pack["items"])})
        st.data["judgeBatches"] = batches
        st.data["stats"]["pack"]["round2"] = ev_mod.pack_stats(packs)
        st.data["stats"]["pack"]["images"] = st.data["stats"]["pack"].get("images", 0) + ev_mod.pack_stats(packs)["images"]
        st.save()
        st.set_step("judge", "pending", "第二輪：看圖")
        st.set_step("check", "pending", "等第二輪看圖結果")
        return None
    for n, change in enumerate(merged["accepted"], 1):
        change["changeId"] = f"chg-{n:03d}"
    items = read_json(st.dir / "items.json", [])
    moc_titles = {i["postKey"]: i.get("mocTitle") for i in items if i.get("mocTitle")}
    for change in merged["accepted"]:
        if change["postKey"] in moc_titles:
            change["mocTitle"] = moc_titles[change["postKey"]]
    write_json(st.dir / "check.json", merged)
    st.data["stats"]["check"] = {k: len(v) for k, v in merged.items()}
    if merged["missing"]:
        st.ask_eric(f"判讀有 {len(merged['missing'])} 篇沒有逐篇處置，已列待查（見報告）")
    upgrade_coverage(st, items, store)
    st.save()
    st.set_step("check", "done")
    if st.mode != "shadow" and not merged["accepted"]:
        st.set_step("review", "skipped", "沒有新增／修改／取消卡片")
    return None


def upgrade_coverage(st, items, store):
    """社群來源達到「7 天窗口讀完、不變式通過、窗口內每篇有處置、圖片都看清楚」才升為 complete"""
    edir = evidence_dir(st)
    judged_rev = lambda it: store.judged(ev_mod.EvidenceStore.revision_of(it))  # noqa: E731
    by_source = {}
    for it in items:
        by_source.setdefault(it.get("source"), []).append(it)
    run = load_progress(st)
    for key, info in run["sources"].items():
        if not key.startswith(("threads:", "facebook:")) or info.get("state") != "partial":
            continue
        data = read_json(edir / f"{key.replace(':', '_')}.json", {}) or {}
        window = [p for p in by_source.get(key, []) if ev_mod.in_window(p, now_dt())]
        images = [m for p in window for m in p.get("media") or []]
        ok = (data.get("stopReason") == "reached-window" and data.get("invariants", {}).get("ok")
              and all(judged_rev(p) for p in window)
              and all(m.get("sha256") and store.image_done(m["sha256"]) for m in images))
        if ok:
            record(st, key, "complete", "social-capture-v2", info["url"],
                   f"7 天窗口讀完（停止原因 reached-window）；窗口內 {len(window)} 篇皆有處置；圖片 {len(images)} 張皆已判讀",
                   "complete" if images else "not_applicable", "不變式通過、逐篇處置完成")
    for key, prefix in (("culture", "culture:"), ("issues", "issues:")):
        src = [i for i in items if i["postKey"].startswith(prefix)]
        stats = st.data["stats"].get(key, {})
        if key == "culture" and stats.get("problems"):
            continue
        if run["sources"].get(key, {}).get("state") == "partial" and all(judged_rev(i) for i in src):
            record(st, key, "complete", "patrol-v2", run["sources"][key]["url"], f"{len(src)} 筆皆有處置",
                   "not_applicable", "逐筆處置完成")


def step_review(st):
    check = read_json(st.dir / "check.json", {})
    if not check.get("accepted"):
        st.set_step("review", "skipped", "沒有卡片變更")
        return None
    out = st.dir / "review.json"
    if out.exists():
        st.set_step("review", "done")
        return None
    items = {i["postKey"]: i for i in read_json(st.dir / "items.json", [])}
    cards = {c["id"]: c for c in read_json(work_root(st) / "data/schedule.json", [])}
    store = ev_mod.EvidenceStore()
    pack = {"runId": st.run_id, "changes": []}
    for c in check["accepted"]:
        it = items.get(c["postKey"], {})
        pack["changes"].append({
            "changeId": c["changeId"], "action": c["action"], "convertedFrom": c.get("convertedFrom"),
            "proposed": c["event"], "diffs": c.get("diffs"),
            "currentCard": cards.get(c["event"].get("targetCardId")),
            "source": {"postKey": c["postKey"], "url": c.get("url"), "datetime": it.get("datetime"), "text": it.get("text"),
                       "images": [{"sha256": m["sha256"], "file": m["file"], "reading": store.images.get(m["sha256"], {}).get("reading")}
                                  for m in it.get("media") or [] if m.get("sha256")]},
            "alsoSources": c.get("alsoSources", []),
        })
    write_json(st.dir / "review_pack.json", pack)
    st.set_step("review", "waiting")
    return {"action": "review", "runId": st.run_id, "promptFile": REVIEW_PROMPT,
            "agent": {"model": "opus", "effort": "high"}, "pack": str(st.dir / "review_pack.json"), "output": str(out),
            "changes": len(pack["changes"])}


def step_apply(st):
    root = work_root(st)
    if st.mode == "production":
        try:
            preflight.check_production(ROOT)
        except preflight.PreflightError as error:
            st.set_step("apply", "failed", str(error))
            st.ask_eric(f"寫入前重新同步失敗，本輪不寫入：{error}")
            return stop(st, "apply-sync-failed", str(error))
    check = read_json(st.dir / "check.json", {})
    review = read_json(st.dir / "review.json", {}) or {}
    verdicts = {v["changeId"]: v for v in review.get("verdicts", [])}
    store = ev_mod.EvidenceStore()
    apply_mod.attach_image_readings(evidence_dir(st), store)
    items = read_json(st.dir / "items.json", [])
    sources_by_key = {i["postKey"]: i.get("source", "") for i in items}
    results = apply_mod.apply_changes(check.get("accepted", []), verdicts, root, evidence_dir(st), today(st), sources_by_key)
    write_json(st.dir / "apply.json", results)
    st.data["stats"]["apply"] = {"written": sum(1 for r in results if r.get("exit") == 0),
                                 "rejectedByAddCard": sum(1 for r in results if r.get("exit") not in (0, None)),
                                 "held": sum(1 for r in results if r.get("result") == "held")}
    run = load_progress(st)
    progress.finalize(run, status_path=root / "data/patrol_status.json", current=progress.targets(root))
    progress.write(progress_path(st), run)
    st.save()
    st.set_step("apply", "done")
    return None


def step_publish(st):
    paths = ["data/schedule.json", "data/patrol_status.json", f"patrol_runs/{st.run_id}.json",
             "data/review_queue.json", "docs/patrols/cancelled_cards.jsonl"]
    to_stage = publish.changed_paths(paths)
    try:
        sha = None if not to_stage else publish.commit_and_push(to_stage, f"chore(patrol): {st.run_id} 巡檢紀錄與場次更新（patrol-v2）")
        if not sha and st.data.get("publication", {}).get("sha"):
            sha = st.data["publication"]["sha"]  # 先前已提交推送：沿用該 SHA 續驗證
        st.data["publication"] = {"sha": sha, "staged": to_stage}
        st.save()
        if not sha:
            raise publish.PublishError("沒有可提交的變更")
        action = publish.wait_for_actions(sha)
        run = load_progress(st)
        progress.verify(run, sha, str(action["id"]), ROOT / "data/patrol_status.json")
        progress.write(progress_path(st), run)
        cmp = progress.compare_public(ROOT)
        st.data["publication"].update({"actionsRun": action["id"], "actionsUrl": action.get("html_url"), "comparePublic": cmp})
        if not cmp["allMatch"]:
            raise publish.PublishError("公開三檔與本機不一致")
        st.data["publication"]["state"] = "verified"
    except (publish.PublishError, ValueError, OSError) as error:
        st.data.setdefault("publication", {}).update({"state": "blocked", "reason": str(error)})
        st.ask_eric(f"發布未完成：{error}")
        st.save()
        st.set_step("publish", "failed", str(error))
        return None
    st.save()
    st.set_step("publish", "done")
    return None


def step_compare(st):
    out = report.shadow_compare(st, ROOT)
    st.data["shadowCompare"] = str(out)
    st.save()
    st.set_step("compare", "done")
    return None


def step_report(st):
    path = report.write_report(st, work_root(st), load_progress(st) if progress_path(st).exists() else None)
    st.data["report"] = str(path)
    st.save()
    if st.mode == "production":
        try:
            receipt = report.write_receipt(st)
            sha = publish.commit_and_push([str(path.relative_to(ROOT)), str(receipt.relative_to(ROOT))],
                                          f"docs(patrol): {st.run_id} 巡檢報告與驗收收據（patrol-v2） [skip ci]")
            st.data["reportCommit"] = sha
        except publish.PublishError as error:
            st.ask_eric(f"報告提交失敗：{error}")
    st.set_step("report", "done")
    outcome = "ok" if not st.data["forEric"] else "needs-eric"
    st.finish(outcome)
    return {"action": "done", "runId": st.run_id, "outcome": outcome, "report": str(path), "forEric": st.data["forEric"],
            "shadowCompare": st.data.get("shadowCompare")}


def stop(st, outcome, reason):
    for name, info in st.data["steps"].items():
        if info.get("status") == "pending" and name != "report":
            info["status"] = "skipped"
    st.save()
    path = report.write_report(st, work_root(st), load_progress(st) if progress_path(st).exists() else None)
    st.data["report"] = str(path)
    st.set_step("report", "done")
    st.finish(outcome)
    return {"action": "stopped", "runId": st.run_id, "outcome": outcome, "reason": reason, "report": str(path)}


STEP_FUNCS = {"preflight": step_preflight, "collect": step_collect, "pack": step_pack, "judge": step_judge,
              "check": step_check, "review": step_review, "apply": step_apply, "publish": step_publish,
              "compare": step_compare, "report": step_report}


def advance(st):
    while True:
        if st.data.get("finished"):
            return {"action": "done", "runId": st.run_id, "outcome": st.data.get("outcome"), "report": st.data.get("report")}
        name = st.next_step()
        if name is None:
            return step_report(st)
        heartbeat(st.run_id)
        st.set_step(name, "running")
        try:
            result = STEP_FUNCS[name](st)
        except Exception as error:  # 未預期錯誤：記錄後停止，下次 start 可恢復
            st.set_step(name, "failed", f"{type(error).__name__}: {error}")
            st.log("step-error", step=name, error=str(error))
            return {"action": "stopped", "runId": st.run_id, "outcome": "step-error", "step": name, "reason": str(error),
                    "hint": "修正後再跑 python3 scripts/patrol.py start 會從此步驟續跑"}
        if result is not None:
            return result
        if st.data["steps"].get(name, {}).get("status") == "failed":
            return {"action": "stopped", "runId": st.run_id, "outcome": "step-failed", "step": name,
                    "reason": st.data["steps"][name].get("detail") or "步驟失敗", "forEric": list(st.data["forEric"])}


# --- 背景程序：耗時的步驟（讀社群約 20 分鐘、等 Actions）不在 start／next 裡同步跑 ---
# start／next 最多等 WORKER_BUDGET 秒就回來；主流程被中斷或逾時，背景程序照樣跑完。

WORKER_BUDGET = 240
MAX_WORKER_RESTARTS = 3


def worker_path(st):
    return st.dir / "worker.json"


def pid_alive(pid):
    if not pid:
        return False
    try:
        os.kill(pid, 0)
        return True
    except ProcessLookupError:
        return False
    except PermissionError:
        return True


def spawn_worker(st):
    log = open(st.dir / "worker.log", "a", encoding="utf-8")
    proc = subprocess.Popen([sys.executable, str(Path(__file__).resolve()), "_worker", "--run", st.run_id],
                            cwd=ROOT, stdin=subprocess.DEVNULL, stdout=log, stderr=log, start_new_session=True)
    return proc.pid


def take_result(path, info):
    info["consumed"] = True
    write_json(path, info)
    return info["result"]


def drive(st, budget=WORKER_BUDGET, spawn=spawn_worker, alive=pid_alive, sleep=time.sleep, clock=time.monotonic):
    path = worker_path(st)
    info = read_json(path, {}) or {}
    if info.get("status") == "finished" and not info.get("consumed"):
        return take_result(path, info)
    restarts = info.get("restarts", 0)
    if info.get("status") in ("running", "starting") and not alive(info.get("pid")):
        restarts += 1
        st = RunState(st.run_id, st.state_dir)
        st.log("背景程序中斷，重新啟動", pid=info.get("pid"), restarts=restarts)
        if restarts > MAX_WORKER_RESTARTS:
            st.ask_eric(f"背景程序連續中斷 {restarts} 次，本輪停止")
            result = stop(st, "worker-died", f"背景程序連續中斷 {restarts} 次")
            write_json(path, {"status": "finished", "result": result, "consumed": True, "restarts": restarts})
            return result
        info = {}
    if info.get("status") not in ("running", "starting"):
        write_json(path, {"status": "starting", "pid": None, "restarts": restarts, "startedAt": now()})
        pid = spawn(st)
        current = read_json(path, {}) or {}
        if current.get("status") == "starting":
            current.update({"status": "running", "pid": pid})
            write_json(path, current)
    deadline = clock() + budget
    while True:
        info = read_json(path, {}) or {}
        if info.get("status") == "finished" and not info.get("consumed"):
            return take_result(path, info)
        if clock() >= deadline or not alive(info.get("pid")):
            break
        sleep(2)
    st = RunState(st.run_id, st.state_dir)
    running = next((k for k, v in st.data["steps"].items() if v.get("status") == "running"), None)
    return {"action": "continue", "runId": st.run_id, "waiting": running,
            "note": "背景程序仍在執行，請再跑一次 next；不要結束任何程序"}


def notify(st, result):
    """這台 Mac 的系統通知（排程工作階段沒有連 Remote Control，手機推播送不出去）"""
    if result.get("action") == "stopped":
        text = f"【要處理】巡檢停止：{str(result.get('reason') or result.get('outcome'))[:80]}"
    else:
        asks = len(result.get("forEric") or [])
        text = f"巡檢完成（{result.get('outcome')}）" + (f"，{asks} 件要你看" if asks else "")
    script = f"display notification {json.dumps(text, ensure_ascii=False)} with title \"臺灣戲曲巡檢 {st.run_id}\""
    try:
        subprocess.run(["osascript", "-e", script], capture_output=True, timeout=15)
    except (OSError, subprocess.TimeoutExpired):
        pass


def cmd_worker(args):
    st = RunState(args.run)
    stop_beat = threading.Event()

    def beat():
        while not stop_beat.wait(60):
            heartbeat(st.run_id)

    threading.Thread(target=beat, daemon=True).start()
    try:
        acquire_lock(st.run_id)
        result = advance(st)
    except LockBusy as error:
        result = {"action": "stopped", "outcome": "reentry-blocked", "reason": str(error)}
    except Exception as error:  # advance 內已處理步驟錯誤；這裡只接住意外
        result = {"action": "stopped", "runId": st.run_id, "outcome": "worker-error", "reason": f"{type(error).__name__}: {error}"}
    finally:
        stop_beat.set()
    path = worker_path(st)
    info = read_json(path, {}) or {}
    info.update({"status": "finished", "pid": os.getpid(), "result": result, "finishedAt": now(), "consumed": False})
    write_json(path, info)
    if result.get("action") in ("done", "stopped") and st.mode == "production":
        notify(st, result)
    return 0


def cmd_close(args):
    st = RunState(args.run)
    if not st.data:
        return emit({"action": "stopped", "reason": f"找不到本輪 {args.run}"})
    if st.data.get("finished"):
        return emit({"ok": False, "reason": f"{args.run} 已結案（{st.data.get('outcome')}）"})
    if pid_alive((read_json(worker_path(st), {}) or {}).get("pid")) and (read_json(worker_path(st), {}) or {}).get("status") == "running":
        return emit({"ok": False, "reason": "背景程序仍在執行，不能結案"})
    st.data["closedReason"] = args.reason
    st.log("人工結案", reason=args.reason)
    st.finish("abandoned")
    return emit({"ok": True, "runId": st.run_id, "outcome": "abandoned", "reason": args.reason})


def cmd_start(args):
    existing = find_today(args.mode)
    if existing and existing.data.get("finished") and not args.force_new:
        return emit({"action": "done", "runId": existing.run_id, "outcome": existing.data.get("outcome"),
                     "report": existing.data.get("report"), "note": "今日已完成，不重複執行"})
    if existing and not existing.data.get("finished"):
        st = existing
    else:
        missed = missed_days(args.mode)
        st = RunState.create(args.mode)
        for text in missed:
            st.ask_eric(f"前幾天的巡檢沒有完成：{text}")
    try:
        previous = acquire_lock(st.run_id)
    except LockBusy as error:
        return emit({"action": "stopped", "outcome": "reentry-blocked", "reason": str(error)})
    if previous:
        st.log("接手失效的鎖", previous=previous)
    return emit(drive(st))


def cmd_next(args):
    st = RunState(args.run)
    if not st.data:
        return emit({"action": "stopped", "reason": f"找不到本輪 {args.run}"})
    try:
        acquire_lock(st.run_id)
    except LockBusy as error:
        return emit({"action": "stopped", "outcome": "reentry-blocked", "reason": str(error)})
    return emit(drive(st))


def cmd_models(args):
    # 另存 models.json：start 可能還在跑（讀社群要十幾分鐘），共用 state.json 會被它存檔時蓋掉
    st = RunState(args.run)
    path = st.dir / "models.json"
    models = read_json(path, {}) or {}
    models[args.role] = {"model": args.model, "evidence": args.evidence, "at": now()}
    write_json(path, models)
    return emit({"ok": True, "models": models})


def cmd_status(args):
    st = RunState(args.run) if args.run else find_today(args.mode)
    if not st or not st.data:
        return emit({"run": None})
    return emit({"runId": st.run_id, "mode": st.mode, "finished": st.data["finished"], "outcome": st.data.get("outcome"),
                 "steps": {k: v.get("status") for k, v in st.data["steps"].items()}, "stats": st.data.get("stats"),
                 "worker": {k: v for k, v in (read_json(worker_path(st), {}) or {}).items() if k != "result"}})


def main(argv=None):
    parser = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    sub = parser.add_subparsers(dest="command", required=True)
    p = sub.add_parser("start")
    p.add_argument("--mode", choices=("production", "dry-run", "shadow"), default="production")
    p.add_argument("--force-new", action="store_true", help="今日已完成仍開新一輪（只供測試）")
    p = sub.add_parser("next")
    p.add_argument("--run", required=True)
    p = sub.add_parser("models")
    p.add_argument("--run", required=True)
    p.add_argument("--role", required=True, choices=("main", "judge", "review"))
    p.add_argument("--model", required=True)
    p.add_argument("--evidence", required=True)
    p = sub.add_parser("close", help="人工結案一輪沒跑完的巡檢（標為 abandoned）")
    p.add_argument("--run", required=True)
    p.add_argument("--reason", required=True)
    p = sub.add_parser("_worker", help="內部用：背景執行步驟")
    p.add_argument("--run", required=True)
    p = sub.add_parser("status")
    p.add_argument("--run")
    p.add_argument("--mode", choices=("production", "dry-run", "shadow"), default="production")
    args = parser.parse_args(argv)
    return {"start": cmd_start, "next": cmd_next, "models": cmd_models, "status": cmd_status,
            "close": cmd_close, "_worker": cmd_worker}[args.command](args)


if __name__ == "__main__":
    sys.exit(main())
