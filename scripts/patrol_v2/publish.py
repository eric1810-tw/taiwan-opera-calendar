"""發布：逐檔 stage → commit → push → 等「該 SHA」的 Actions 成功 → compare-public 三檔一致。

禁用：git add . / -A、reset --hard、stash、push --force、clean。
"""
import json
import subprocess
import time
from pathlib import Path

from .common import PROTECTED_FILES, ROOT

REPO = "eric1810-tw/taiwan-opera-calendar"
WORKFLOW_PATH = ".github/workflows/daily-update.yml"
FORBIDDEN = ({"add", "."}, {"add", "-A"}, {"reset", "--hard"}, {"stash"}, {"push", "--force"}, {"clean"})


class PublishError(Exception):
    pass


def git(args, cwd=ROOT, check=True, strip=True):
    lowered = set(args)
    for bad in FORBIDDEN:
        if bad <= lowered:
            raise PublishError(f"禁用的 git 指令：{' '.join(args)}")
    res = subprocess.run(["git", *args], cwd=cwd, capture_output=True, text=True)
    if check and res.returncode != 0:
        raise PublishError(f"git {' '.join(args)} 失敗：{(res.stderr or res.stdout).strip()}")
    return res.stdout.strip() if strip else res.stdout


def changed_paths(paths, cwd=ROOT, runner=git):
    """paths 中有變動（含未追蹤）的檔案。用 -z 且不去頭尾空白：狀態碼開頭的空白（" M"）不能被削掉"""
    out = runner(["status", "--porcelain", "-z", "--untracked-files=all", "--", *paths], cwd=cwd, strip=False)
    found = [entry[3:] for entry in out.split("\0") if len(entry) > 3]
    return [p for p in paths if p in found]


def stage_exact(paths, cwd=ROOT, runner=git):
    for rel in paths:
        if rel in PROTECTED_FILES:
            raise PublishError(f"不得提交保留檔：{rel}")
    runner(["add", "--", *paths], cwd=cwd)
    staged = set(filter(None, runner(["diff", "--cached", "--name-only"], cwd=cwd).splitlines()))
    extra = staged - set(paths)
    if extra:
        raise PublishError(f"暫存區有本輪以外的檔案：{sorted(extra)}")
    return sorted(staged)


def commit_and_push(paths, message, cwd=ROOT, runner=git):
    staged = stage_exact(paths, cwd, runner)
    if not staged:
        return None
    runner(["commit", "-m", message], cwd=cwd)
    sha = runner(["rev-parse", "HEAD"], cwd=cwd)
    try:
        runner(["push", "origin", "HEAD:main"], cwd=cwd)
    except PublishError as first:
        # 遠端前進：fetch 後 merge 一次（正式資料夾有既存未提交的保留檔，rebase 會被擋）；衝突就放棄並停止
        runner(["fetch", "origin", "main"], cwd=cwd)
        try:
            runner(["merge", "--no-edit", "origin/main"], cwd=cwd)
        except PublishError as conflict:
            runner(["merge", "--abort"], cwd=cwd, check=False)
            raise PublishError(f"push 被拒且與遠端合併衝突，已放棄合併：{conflict}")
        sha = runner(["rev-parse", "HEAD"], cwd=cwd)
        try:
            runner(["push", "origin", "HEAD:main"], cwd=cwd)
        except PublishError as second:
            raise PublishError(f"push 兩次失敗：{first}；{second}")
    return sha


def gh_api(path):
    res = subprocess.run(["gh", "api", path], capture_output=True, text=True, timeout=60)
    if res.returncode != 0:
        raise PublishError(res.stderr.strip() or "gh api 失敗")
    return json.loads(res.stdout)


def find_actions_run(sha, api=gh_api):
    data = api(f"repos/{REPO}/actions/runs?head_sha={sha}&per_page=20")
    runs = [r for r in data.get("workflow_runs", []) if r.get("head_sha") == sha and r.get("path") == WORKFLOW_PATH]
    return runs[0] if runs else None


def wait_for_actions(sha, api=gh_api, timeout=1200, interval=30, sleep=time.sleep):
    """只接受 head_sha＝本次 SHA 的 run；其他 SHA 的成功一律不算"""
    waited = 0
    while waited <= timeout:
        run = find_actions_run(sha, api)
        if run and run.get("status") == "completed":
            if run.get("conclusion") != "success":
                raise PublishError(f"Actions {run.get('id')} 結論 {run.get('conclusion')}")
            return run
        sleep(interval)
        waited += interval
    raise PublishError(f"等待 {timeout} 秒仍沒有 SHA {sha[:12]} 的完成紀錄")
