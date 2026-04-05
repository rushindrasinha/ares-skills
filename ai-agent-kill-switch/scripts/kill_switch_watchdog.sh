#!/usr/bin/env bash
set -euo pipefail

# Kill switch watchdog
# Scans agent session logs (JSONL) for an ARMED trigger phrase.
# Only triggers when the exact phrase appears. Incremental scan via state file.
#
# Env vars:
#   ARMED_PHRASE      — exact trigger phrase (default: "KILL: AGENT STOP NOW")
#   KILL_SWITCH_STATE_DIR — where state/sentinel files live
#   SESSIONS_DIR      — directory of .jsonl session logs to scan

ARMED_PHRASE="${ARMED_PHRASE:-KILL: AGENT STOP NOW}"
STATE_DIR="${KILL_SWITCH_STATE_DIR:-$HOME/.ai-kill-switch}"
SENTINEL="$STATE_DIR/kill-switch.triggered"
STATE_FILE="$STATE_DIR/kill-switch.watchdog.state.json"
SESSIONS_DIR="${SESSIONS_DIR:-$HOME/.openclaw/agents/main/sessions}"

mkdir -p "$STATE_DIR"

# If already triggered, exit cleanly.
if [ -f "$SENTINEL" ]; then
  echo "TRIGGERED_ALREADY"
  exit 0
fi

export ARMED_PHRASE STATE_FILE SESSIONS_DIR SENTINEL
python3 - <<'PY'
import json, os, glob
from pathlib import Path

armed = os.environ.get('ARMED_PHRASE', '')
state_file = os.environ.get('STATE_FILE', '')
sess_dir = Path(os.environ.get('SESSIONS_DIR', ''))
sentinel = os.environ.get('SENTINEL', '')

if os.path.exists(state_file):
    with open(state_file, 'r', encoding='utf-8') as f:
        state = json.load(f)
else:
    state = {"files": {}}
files_state = state.get('files', {})

triggered = False
for path in glob.glob(str(sess_dir / '*.jsonl')):
    try:
        p = Path(path)
        size = p.stat().st_size
    except FileNotFoundError:
        continue

    last_size = int(files_state.get(path, {}).get('size', 0) or 0)
    if last_size > size:
        last_size = 0  # file rotated

    if size == last_size:
        continue

    with open(path, 'rb') as f:
        f.seek(last_size)
        chunk = f.read()

    text = chunk.decode('utf-8', errors='ignore')
    if armed in text:
        triggered = True

    files_state[path] = {'size': size}

state['files'] = files_state
with open(state_file, 'w', encoding='utf-8') as f:
    json.dump(state, f)

if triggered and sentinel:
    Path(sentinel).touch()

print('TRIGGER' if triggered else 'NO_TRIGGER')
PY
