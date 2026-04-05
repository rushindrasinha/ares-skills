#!/usr/bin/env python3
"""
watchdog.py — OpenClaw Gateway log watchdog.

Tails the gateway log incrementally (via byte cursor), counts error patterns
in a rolling time window, and sends an alert on threshold breach.

Configure via environment variables — see README/SKILL.md.
"""
import json
import os
import re
import subprocess
import sys
import time
from datetime import datetime, timezone, timedelta
from pathlib import Path

# ── Config ────────────────────────────────────────────────────────────────
LOG_PATH   = Path(os.path.expanduser(
    os.environ.get("GATEWAY_LOG_PATH", "~/.openclaw/logs/gateway.log")))
STATE_DIR  = Path(os.path.expanduser(
    os.environ.get("WATCHDOG_STATE_DIR", "~/.gateway-watchdog")))
WINDOW_MIN = int(os.environ.get("WATCHDOG_WINDOW_MIN", "10"))
NOTIFY_TARGET  = os.environ.get("NOTIFY_TARGET", "")
NOTIFY_CHANNEL = os.environ.get("NOTIFY_CHANNEL", "whatsapp")

STATE_DIR.mkdir(parents=True, exist_ok=True)
STATE_FILE  = STATE_DIR / "state.json"
EVENTS_FILE = STATE_DIR / "events.jsonl"

# ── Patterns + thresholds ────────────────────────────────────────────────
PATTERNS = {
    "rate_limit":     {"regex": re.compile(r"\b429\b|rate.?limit", re.I), "threshold": 3, "window_min": 10},
    "auth_failure":   {"regex": re.compile(r"\b401\b|unauthorized|auth.?fail", re.I), "threshold": 1, "window_min": 10},
    "timeout":        {"regex": re.compile(r"timeout|ECONNRESET|ETIMEDOUT", re.I), "threshold": 5, "window_min": 10},
    "delivery_fail":  {"regex": re.compile(r"delivery[_ ]?fail", re.I), "threshold": 1, "window_min": 10},
    "upstream_5xx":   {"regex": re.compile(r"\b5\d\d\b"), "threshold": 3, "window_min": 5},
}

def load_state() -> dict:
    if STATE_FILE.exists():
        try:
            return json.loads(STATE_FILE.read_text())
        except Exception:
            pass
    return {"cursor": 0, "last_alert_ts": {}}

def save_state(state: dict) -> None:
    STATE_FILE.write_text(json.dumps(state, indent=2))

def notify(msg: str) -> None:
    print(msg)
    if not NOTIFY_TARGET:
        return
    try:
        subprocess.run(
            ["openclaw", "message", "send",
             "--channel", NOTIFY_CHANNEL,
             "--target", NOTIFY_TARGET,
             "--message", msg],
            capture_output=True, timeout=30
        )
    except Exception as e:
        print(f"notify failed: {e}", file=sys.stderr)

def append_event(kind: str, line: str) -> None:
    with EVENTS_FILE.open("a") as f:
        f.write(json.dumps({
            "ts": datetime.now(timezone.utc).isoformat(),
            "kind": kind,
            "line": line.strip()[:500],
        }) + "\n")

def recent_count(kind: str, window_min: int) -> int:
    if not EVENTS_FILE.exists():
        return 0
    cutoff = datetime.now(timezone.utc) - timedelta(minutes=window_min)
    count = 0
    with EVENTS_FILE.open() as f:
        for line in f:
            try:
                evt = json.loads(line)
                if evt["kind"] != kind:
                    continue
                if datetime.fromisoformat(evt["ts"]) >= cutoff:
                    count += 1
            except Exception:
                pass
    return count

def main() -> int:
    if not LOG_PATH.exists():
        print(f"log not found: {LOG_PATH}", file=sys.stderr)
        return 1

    state = load_state()
    cursor = int(state.get("cursor", 0))
    size = LOG_PATH.stat().st_size
    if cursor > size:
        cursor = 0  # rotated

    with LOG_PATH.open("rb") as f:
        f.seek(cursor)
        chunk = f.read().decode("utf-8", errors="ignore")
    state["cursor"] = size

    for line in chunk.splitlines():
        for kind, cfg in PATTERNS.items():
            if cfg["regex"].search(line):
                append_event(kind, line)

    for kind, cfg in PATTERNS.items():
        count = recent_count(kind, cfg["window_min"])
        if count >= cfg["threshold"]:
            last = state.get("last_alert_ts", {}).get(kind, 0)
            if time.time() - last > 600:  # 10-min cooldown per kind
                notify(f"🛰️ Gateway watchdog: *{kind}* = {count} in last {cfg['window_min']}min (threshold {cfg['threshold']})")
                state.setdefault("last_alert_ts", {})[kind] = time.time()

    save_state(state)
    return 0

if __name__ == "__main__":
    sys.exit(main())
