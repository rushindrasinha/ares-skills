#!/usr/bin/env bash
set -euo pipefail

# AI Agent Kill Switch — emergency stop
# Purpose: halt automation + prevent outbound sends.
# Safe to run multiple times (idempotent).
#
# Config via env vars:
#   KILL_SWITCH_STATE_DIR  — where state/log files live (default: $HOME/.ai-kill-switch)
#   KILL_SWITCH_LOGGER_PATTERN — pattern passed to pkill (optional, e.g. "scripts/my_logger.js")

STATE_DIR="${KILL_SWITCH_STATE_DIR:-$HOME/.ai-kill-switch}"
LOGGER_PATTERN="${KILL_SWITCH_LOGGER_PATTERN:-}"

mkdir -p "$STATE_DIR"
TS=$(date -u +"%Y-%m-%dT%H:%M:%SZ")
echo "$TS kill_switch invoked" >> "$STATE_DIR/kill-switch.log"

# 1) Create the sentinel flag — any script sourcing check_flag.sh will bail on this
touch "$STATE_DIR/kill_switch.flag"

# 2) Kill the passive logger if configured
if [ -n "$LOGGER_PATTERN" ]; then
  pkill -f "$LOGGER_PATTERN" 2>/dev/null || true
fi

# 3) Pause OpenClaw gateway if installed
if command -v openclaw >/dev/null 2>&1; then
  openclaw gateway pause 2>/dev/null || true
fi

# 4) Write send-policy deny marker (agents can read this and refuse to send)
cat > "$STATE_DIR/send-policy.deny.json" <<'JSON'
{
  "sendPolicy": {
    "default": "deny",
    "rules": [
      {"action":"deny","match":{"channel":"*"}}
    ]
  }
}
JSON

echo "$TS kill_switch completed" >> "$STATE_DIR/kill-switch.log"
echo "Kill switch ACTIVE. Clear with: rm \"$STATE_DIR/kill_switch.flag\""
