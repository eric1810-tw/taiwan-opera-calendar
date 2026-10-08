"""Persist patrol coverage; never fetch social posts or infer event facts."""
import argparse
import json
import tempfile
import urllib.request
from datetime import datetime
from pathlib import Path
from zoneinfo import ZoneInfo

ROOT = Path(__file__).resolve().parents[1]
REPO = "eric1810-tw/taiwan-opera-calendar"
PUBLIC = f"https://eric1810-tw.github.io/taiwan-opera-calendar/data/patrol_status.json"


def now():
    return datetime.now(ZoneInfo("Asia/Taipei")).isoformat(timespec="seconds")


def read(path):
    return json.loads(Path(path).read_text(encoding="utf-8"))


def write(path, value):
    path = Path(path)
    path.parent.mkdir(parents=True, exist_ok=True)
    with tempfile.NamedTemporaryFile(mode="w", encoding="utf-8", dir=path.parent,
                                     delete=False) as stream:
        temporary = Path(stream.name)
        json.dump(value, stream, ensure_ascii=False, indent=2)
        stream.write("\n")
    temporary.replace(path)


def targets(root=ROOT):
    result = {}
    for account in read(root / "data/threads_accounts.json"):
        handle = account["username"]
        result[f"threads:{handle}"] = f"https://www.threads.com/@{handle}"
    for account in read(root / "data/facebook_accounts.json"):
        result[f"facebook:{account['handle']}"] = account["url"]
    result["culture"] = "data/moc_candidates.json"
    result["issues"] = f"https://github.com/{REPO}/issues?q=is%3Aissue+sort%3Aupdated-desc"
    return result


def sync(run, current):
    run["activeTargets"] = list(current)
    for key, url in current.items():
        run["sources"].setdefault(key, {"url": url, "state": "pending", "attempts": []})


def coverage(run, current):
    # A new account added after init cannot silently disappear from coverage.
    states = [run["sources"].get(key, {}).get("state", "pending") for key in current]
    if not states or any(state not in ("complete", "partial") for state in states):
        return "failed"
    return "partial" if "partial" in states else "complete"


def record(run, key, state, method, url, scope, media, detail):
    if key not in run["activeTargets"]:
        raise ValueError("來源不在本輪清單；先 resume 同步監看清單")
    if not detail.strip():
        raise ValueError("必須記錄可讀範圍或失敗原因")
    if state == "complete" and (not scope.strip() or media not in ("complete", "not_applicable")):
        raise ValueError("complete 必須提供讀取範圍，且媒體已核對或有理由不適用")
    source = run["sources"][key]
    source["attempts"].append({"at": now(), "method": method, "url": url,
                               "state": state, "scope": scope, "media": media,
                               "detail": detail})
    source["state"] = state
    # Any new reading invalidates the previously published coverage receipt.
    run["finalizedAt"] = None
    run["publication"] = {"state": "pending"}


def fetch(url):
    request = urllib.request.Request(url, headers={"User-Agent": "opera-patrol-verifier"})
    with urllib.request.urlopen(request, timeout=20) as response:
        return json.load(response)


def verify(run, sha, actions_run, status_path, fetcher=fetch):
    expected = {"startedAt": run["startedAt"], "status": coverage(run, targets())}
    if not run.get("finalizedAt") or read(status_path) != expected:
        raise ValueError("請先 finalize；本輪狀態必須與狀態檔一致")
    action = fetcher(f"https://api.github.com/repos/{REPO}/actions/runs/{actions_run}")
    if not isinstance(action, dict):
        raise ValueError("Actions 回應格式無法核對")
    if (action.get("path") != ".github/workflows/daily-update.yml"
            or action.get("head_sha") != sha or action.get("status") != "completed"
            or action.get("conclusion") != "success"):
        raise ValueError("Actions 尚未 completed/success 或 SHA 不符")
    live = fetcher(f"{PUBLIC}?patrol={datetime.now().timestamp()}")
    if live != expected:
        raise ValueError("公開網站巡檢狀態與本輪不符")
    run["publication"] = {"state": "verified", "sha": sha, "actionsRun": actions_run,
                          "actionsUrl": action.get("html_url"), "publicUrl": PUBLIC,
                          "verifiedAt": now(), "publicStatus": live}


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    sub = parser.add_subparsers(dest="command", required=True)
    for command in ("init", "resume", "record", "summary", "finalize", "verify"):
        child = sub.add_parser(command)
        child.add_argument("--run", type=Path, required=True)
        if command == "record":
            child.add_argument("--source", required=True)
            child.add_argument("--state", choices=("complete", "partial", "failed"), required=True)
            child.add_argument("--method", required=True)
            child.add_argument("--url", required=True)
            child.add_argument("--scope", default="")
            child.add_argument("--media", choices=("complete", "partial", "unread", "not_applicable"), required=True)
            child.add_argument("--detail", required=True)
        if command == "verify":
            child.add_argument("--sha", required=True)
            child.add_argument("--actions-run", required=True)
    args = parser.parse_args()
    if args.command == "init":
        if args.run.exists():
            parser.error("本輪檔案已存在；使用 resume，不覆蓋證據")
        run = {"version": 1, "startedAt": now(), "resumedAt": [], "sources": {},
               "finalizedAt": None, "publication": {"state": "pending"}}
        sync(run, targets())
    else:
        run = read(args.run)
    if args.command == "resume":
        sync(run, targets())
        run["resumedAt"].append(now())
        run["finalizedAt"] = None
        run["publication"] = {"state": "pending"}
    if args.command == "record":
        record(run, args.source, args.state, args.method, args.url, args.scope, args.media, args.detail)
    if args.command == "finalize":
        write(ROOT / "data/patrol_status.json", {"startedAt": run["startedAt"], "status": coverage(run, targets())})
        run["finalizedAt"] = now()
        run["publication"] = {"state": "pending"}
    if args.command == "verify":
        try:
            verify(run, args.sha, args.actions_run, ROOT / "data/patrol_status.json")
        except (ValueError, OSError) as error:
            run["publication"] = {"state": "blocked", "sha": args.sha,
                                  "actionsRun": args.actions_run, "at": now(), "reason": str(error)}
            write(args.run, run)
            parser.exit(1, f"發布未驗證：{error}\n")
    if args.command != "summary":
        write(args.run, run)
    current = targets()
    print(json.dumps({"startedAt": run["startedAt"], "status": coverage(run, current),
                      "sources": {key: run["sources"].get(key, {}).get("state", "pending") for key in current},
                      "publication": run["publication"]}, ensure_ascii=False, indent=2))


if __name__ == "__main__":
    main()
