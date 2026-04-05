#!/usr/bin/env python3
"""
update_state.py — Live system state checker.
Writes compact JSON for agent context injection.
Run manually or via cron (every 30 min).

Config: integrations.json (in same directory) or INTEGRATIONS_CONFIG env var.
Output: writes to OUTPUT_PATH env var or config's output_path.
"""
import json
import os
import shutil
import subprocess
import sys
from datetime import datetime, timezone, timedelta
from pathlib import Path

SCRIPT_DIR = Path(__file__).parent
CONFIG_FILE = Path(os.environ.get("INTEGRATIONS_CONFIG",
                                   str(SCRIPT_DIR / "integrations.json")))
DEFAULT_OUTPUT = os.path.expanduser(
    os.environ.get("OUTPUT_PATH", "~/system_state.json"))
TZ_OFFSET = float(os.environ.get("TZ_OFFSET_HOURS", "0"))


def now_iso() -> str:
    tz = timezone(timedelta(hours=TZ_OFFSET)) if TZ_OFFSET else timezone.utc
    return datetime.now(tz).isoformat(timespec="seconds")


def run_check(cmd: str, timeout: int = 15) -> str:
    """Run a shell command, return stdout or error string."""
    try:
        r = subprocess.run(cmd, shell=True, capture_output=True,
                           text=True, timeout=timeout)
        out = r.stdout.strip()
        return out if out else (r.stderr.strip()[:80] or "no output")
    except subprocess.TimeoutExpired:
        return "timeout"
    except Exception as e:
        return f"error: {str(e)[:60]}"


def check_gateway() -> dict:
    """Check OpenClaw gateway status."""
    try:
        r = subprocess.run(["openclaw", "gateway", "status"],
                           capture_output=True, text=True, timeout=10)
        output = r.stdout + r.stderr
        if "running" in output.lower():
            return {"status": "running"}
        elif "stopped" in output.lower() or r.returncode != 0:
            return {"status": "stopped"}
        return {"status": "unknown", "raw": output[:100]}
    except FileNotFoundError:
        return {"status": "openclaw not found"}
    except Exception as e:
        return {"status": f"error: {str(e)[:60]}"}


def check_disk() -> dict:
    """Check disk space on root volume."""
    usage = shutil.disk_usage("/")
    return {
        "free_gb": round(usage.free / (1024**3), 1),
        "used_pct": round((usage.used / usage.total) * 100, 1),
    }


def check_integrations(config: dict) -> dict:
    """Run custom integration probes from config."""
    results = {}
    for integ in config.get("integrations", []):
        name = integ.get("name", "unknown")
        cmd = integ.get("check", "echo unconfigured")
        results[name] = run_check(cmd, timeout=integ.get("timeout", 15))
    return results


def main():
    # Load config
    config = {}
    if CONFIG_FILE.exists():
        with open(CONFIG_FILE) as f:
            config = json.load(f)

    output_path = os.path.expanduser(
        config.get("output_path", DEFAULT_OUTPUT))

    tz_hours = config.get("timezone_offset_hours", TZ_OFFSET)
    if tz_hours:
        global TZ_OFFSET
        TZ_OFFSET = float(tz_hours)

    state = {
        "generated": now_iso(),
        "gateway": check_gateway(),
        "disk": check_disk(),
        "integrations": check_integrations(config),
    }

    # Write output
    os.makedirs(os.path.dirname(output_path) or ".", exist_ok=True)
    with open(output_path, "w") as f:
        json.dump(state, f, indent=2)

    print(f"State written to {output_path}")
    print(json.dumps(state, indent=2))


if __name__ == "__main__":
    main()
