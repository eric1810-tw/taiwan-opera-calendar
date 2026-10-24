"""前置檢查：正式模式必須在 main 且 fetch＋ff-only 成功；其他模式建立沙盒資料。"""
import subprocess
import time
from pathlib import Path

from .common import PROTECTED_FILES, ROOT, sha256_file

SANDBOX_FILES = (
    "data/schedule.json",
    "data/metadata.json",
    "data/patrol_status.json",
    "data/threads_accounts.json",
    "data/facebook_accounts.json",
    "data/moc_records.json",
    "data/review_queue.json",
)


class PreflightError(Exception):
    pass


def git(args, cwd=ROOT, check=True):
    result = subprocess.run(["git", *args], cwd=cwd, capture_output=True, text=True)
    if check and result.returncode != 0:
        raise PreflightError(f"git {' '.join(args)} 失敗：{(result.stderr or result.stdout).strip()}")
    return result.stdout.strip()


def fetch_with_retry(cwd=ROOT, runner=git, attempts=3, wait=10):
    errors = []
    for i in range(attempts):
        try:
            runner(["fetch", "origin", "main"], cwd=cwd)
            return errors
        except PreflightError as error:
            errors.append(str(error))
            if i < attempts - 1:
                time.sleep(wait)
    raise PreflightError("fetch 連續失敗：" + "；".join(errors))


def protected_hashes(root=ROOT):
    result = {}
    for rel in PROTECTED_FILES:
        path = Path(root) / rel
        result[rel] = sha256_file(path)[:16] if path.exists() else None
    return result


def check_production(root=ROOT, runner=git):
    branch = runner(["rev-parse", "--abbrev-ref", "HEAD"], cwd=root)
    if branch != "main":
        raise PreflightError(f"正式資料夾不在 main（目前 {branch}），停止巡檢")
    staged = runner(["diff", "--cached", "--name-only"], cwd=root)
    if staged:
        raise PreflightError(f"正式資料夾已有 staged 檔案，停止以免混入提交：{staged}")
    retries = fetch_with_retry(root, runner)
    runner(["merge", "--ff-only", "origin/main"], cwd=root)
    head = runner(["rev-parse", "HEAD"], cwd=root)
    return {"branch": branch, "head": head, "fetchRetries": retries, "protected": protected_hashes(root)}


def build_sandbox(sandbox, root=ROOT, runner=git):
    """非正式模式：從 origin/main 取出當天真實資料，所有寫入只到沙盒。"""
    retries = fetch_with_retry(root, runner)
    head = runner(["rev-parse", "origin/main"], cwd=root)
    sandbox = Path(sandbox)
    for rel in SANDBOX_FILES:
        target = sandbox / rel
        target.parent.mkdir(parents=True, exist_ok=True)
        content = runner(["show", f"origin/main:{rel}"], cwd=root, check=False)
        target.write_text((content + "\n") if content else "[]\n", encoding="utf-8")
    (sandbox / "patrol_runs").mkdir(exist_ok=True)
    (sandbox / "docs" / "patrols").mkdir(parents=True, exist_ok=True)
    return {"originMain": head, "fetchRetries": retries, "sandbox": str(sandbox), "protected": protected_hashes(root)}
