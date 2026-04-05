#!/usr/bin/env python3
"""
capture.py — Reality-first weekly log generator.

Collects daily logs + git history + agent state, then uses Claude
to synthesize a structured weekly capture that prioritizes truth over narrative.

Usage:
    python3 capture.py [--week 2026-WNN] [--dry-run]

Env vars:
    ANTHROPIC_API_KEY  — required
    CAPTURE_MODEL      — default: claude-sonnet-4-5-20250514
    MEMORY_DIR         — daily logs (YYYY-MM-DD.md files)
    WEEKLY_DIR         — output directory
    REPO_DIR           — git repo for log
    SESSION_STATE_PATH — optional session state JSON
    OPEN_THREADS_PATH  — optional open threads JSON
"""
import argparse
import json
import os
import subprocess
import sys
from datetime import datetime, timedelta
from pathlib import Path

try:
    import anthropic
except ImportError:
    print("pip install anthropic", file=sys.stderr)
    sys.exit(1)

# ── Config ────────────────────────────────────────────────────────────────
MEMORY_DIR    = Path(os.path.expanduser(os.environ.get("MEMORY_DIR", "~/agent-workspace/memory")))
WEEKLY_DIR    = Path(os.path.expanduser(os.environ.get("WEEKLY_DIR", "~/agent-workspace/weekly")))
REPO_DIR      = Path(os.path.expanduser(os.environ.get("REPO_DIR", "~/agent-workspace")))
SESSION_STATE = os.environ.get("SESSION_STATE_PATH", "")
OPEN_THREADS  = os.environ.get("OPEN_THREADS_PATH", "")
MODEL         = os.environ.get("CAPTURE_MODEL", "claude-sonnet-4-5-20250514")


def current_week_label() -> str:
    today = datetime.now()
    year, week, _ = today.isocalendar()
    return f"{year}-W{week:02d}"


def week_date_range(label: str):
    year, week = label.split("-W")
    monday = datetime.fromisocalendar(int(year), int(week), 1)
    sunday = monday + timedelta(days=6)
    return monday, sunday


def dates_in_week(label: str) -> list[str]:
    monday, sunday = week_date_range(label)
    dates = []
    current = monday
    while current <= sunday:
        dates.append(current.strftime("%Y-%m-%d"))
        current += timedelta(days=1)
    return dates


def collect_daily_logs(week_label: str) -> str:
    dates = dates_in_week(week_label)
    collected = []
    for date in dates:
        p = MEMORY_DIR / f"{date}.md"
        if p.exists():
            content = p.read_text(encoding="utf-8").strip()
            if content:
                collected.append(f"### {date}\n{content}")
        for aux in MEMORY_DIR.glob(f"{date}-*.md"):
            content = aux.read_text(encoding="utf-8").strip()
            if content:
                collected.append(f"### {aux.stem}\n{content}")
    return "\n\n".join(collected) if collected else "(no daily logs found)"


def collect_git_log(week_label: str) -> str:
    monday, sunday = week_date_range(week_label)
    since = monday.strftime("%Y-%m-%d")
    until = (sunday + timedelta(days=1)).strftime("%Y-%m-%d")
    try:
        r = subprocess.run(
            ["git", "log", "--oneline", "--since", since, "--until", until],
            capture_output=True, text=True, timeout=15, cwd=str(REPO_DIR)
        )
        return r.stdout.strip() or "(no commits)"
    except Exception:
        return "(git log unavailable)"


def collect_state_files() -> str:
    parts = []
    for path_str, label in [(SESSION_STATE, "Session State"), (OPEN_THREADS, "Open Threads")]:
        if path_str:
            p = Path(os.path.expanduser(path_str))
            if p.exists():
                parts.append(f"### {label}\n```json\n{p.read_text()[:3000]}\n```")
    return "\n\n".join(parts) if parts else ""


def synthesize(week_label: str, daily: str, git: str, state: str, dry_run: bool) -> str:
    monday, sunday = week_date_range(week_label)
    prompt = f"""You are generating a REALITY-FIRST weekly capture for {week_label} ({monday.strftime('%Y-%m-%d')} to {sunday.strftime('%Y-%m-%d')}).

Your job is to report what ACTUALLY happened — not a curated highlight reel. Include:
- Work that stalled or was abandoned
- Promises made but not delivered
- Patterns (positive or negative)
- Decisions actually taken vs deferred

Structure your output as:
# Week {week_label.split('-W')[1]} — {monday.strftime('%Y-%m-%d')} to {sunday.strftime('%Y-%m-%d')}

## What Actually Happened
(Day-by-day or thematic, whichever is clearer)

## Decisions Made
(Concrete decisions, not intentions)

## Unresolved / Carried Over
(Threads that didn't close)

## Patterns Noticed
(Recurring behaviors, good or bad)

---

## Data Sources

### Daily Logs
{daily[:8000]}

### Git Log
{git[:2000]}

{state}
"""

    if dry_run:
        print("=== DRY RUN — SYNTHESIS PROMPT ===")
        print(prompt[:3000])
        return ""

    client = anthropic.Anthropic()
    resp = client.messages.create(
        model=MODEL,
        max_tokens=4096,
        messages=[{"role": "user", "content": prompt}],
    )
    return resp.content[0].text


def main():
    parser = argparse.ArgumentParser(description="Weekly reality capture")
    parser.add_argument("--week", default=current_week_label(), help="Week label (YYYY-WNN)")
    parser.add_argument("--dry-run", action="store_true", help="Print prompt without calling Claude")
    args = parser.parse_args()

    daily = collect_daily_logs(args.week)
    git = collect_git_log(args.week)
    state = collect_state_files()

    output = synthesize(args.week, daily, git, state, args.dry_run)
    if not output:
        return

    WEEKLY_DIR.mkdir(parents=True, exist_ok=True)
    out_file = WEEKLY_DIR / f"{args.week}.md"
    out_file.write_text(output)
    print(f"Written: {out_file}")


if __name__ == "__main__":
    main()
