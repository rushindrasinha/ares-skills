#!/usr/bin/env bash
# check_flag.sh — source this at the top of any script that does outbound actions.
# Exits 99 if the kill switch flag is present.
#
# Usage:
#   source /path/to/check_flag.sh

STATE_DIR="${KILL_SWITCH_STATE_DIR:-$HOME/.ai-kill-switch}"
FLAG="$STATE_DIR/kill_switch.flag"

if [ -f "$FLAG" ]; then
  echo "🚨 Kill switch active ($FLAG) — aborting." >&2
  exit 99
fi
