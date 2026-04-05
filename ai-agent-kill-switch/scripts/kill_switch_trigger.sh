#!/usr/bin/env bash
# kill_switch_trigger.sh — fired when the flag file is created/modified
# (e.g. by launchd WatchPaths or fswatch).
#
# Env vars:
#   KILL_SWITCH_STATE_DIR — default: $HOME/.ai-kill-switch
#   NOTIFY_TARGET         — optional phone/JID (requires openclaw or wacli)
#   NOTIFY_CHANNEL        — default: whatsapp

set -euo pipefail

STATE_DIR="${KILL_SWITCH_STATE_DIR:-$HOME/.ai-kill-switch}"
NOTIFY_TARGET="${NOTIFY_TARGET:-}"
NOTIFY_CHANNEL="${NOTIFY_CHANNEL:-whatsapp}"

LOG="$STATE_DIR/kill-switch.log"
mkdir -p "$STATE_DIR"
echo "[$(date)] kill_switch_trigger fired" >> "$LOG"

MSG="🚨 KILL SWITCH TRIGGERED — all agent automation paused, outbound sends denied."

if [ -n "$NOTIFY_TARGET" ]; then
  if command -v openclaw &>/dev/null; then
    openclaw message send --channel "$NOTIFY_CHANNEL" --target "$NOTIFY_TARGET" --message "$MSG" 2>/dev/null || true
  elif command -v wacli &>/dev/null; then
    wacli send --to "$NOTIFY_TARGET" --message "$MSG" 2>/dev/null || true
  fi
fi

# Pause the OpenClaw gateway if present
if command -v openclaw &>/dev/null; then
  openclaw gateway pause 2>/dev/null || true
  echo "[$(date)] Gateway pause attempted" >> "$LOG"
fi
