---
name: ai-agent-kill-switch
description: Phrase-triggered emergency stop system for AI agents. Instantly halts all agent automation when a trigger phrase is detected in session logs, or via manual flag. Use when setting up a safety kill switch, emergency stop, or pause-all-automation mechanism for autonomous agents. Survives restarts via LaunchAgent watchdog.
metadata:
  emoji: 🛑
  category: safety
  platform: macOS, Linux
---

# AI Agent Kill Switch

Hard stop for autonomous agents. Trigger phrase or manual flag → all outbound halts. Designed to be impossible to accidentally bypass.

## Architecture

```
┌─────────────┐     ┌──────────────┐     ┌─────────────┐
│ Trigger     │ ──▶ │ Flag file    │ ──▶ │ Any agent   │
│ (phrase or  │     │ (sentinel)   │     │ script bails│
│ manual)     │     │              │     │ on source   │
└─────────────┘     └──────────────┘     └─────────────┘
       │
       ▼
┌──────────────────┐
│ Watchdog scans   │
│ session JSONL    │  ← LaunchAgent, cron, or fswatch
│ for armed phrase │
└──────────────────┘
```

## Components

| Script | Role |
|---|---|
| `scripts/kill_switch.sh` | Activate the kill switch (creates flag, pauses gateway) |
| `scripts/kill_switch_watchdog.sh` | Scans session logs for the armed phrase |
| `scripts/kill_switch_trigger.sh` | Runs when flag appears (notifications, gateway pause) |
| `scripts/check_flag.sh` | Source this at top of any agent script to auto-abort |

## Quick Start

### 1. Activate manually
```bash
bash scripts/kill_switch.sh
```

### 2. Clear the flag
```bash
rm "${KILL_SWITCH_STATE_DIR:-$HOME/.ai-kill-switch}/kill_switch.flag"
```

### 3. Protect any script
At the top of any script that makes outbound calls:
```bash
#!/usr/bin/env bash
source /path/to/ai-agent-kill-switch/scripts/check_flag.sh
# ... your code runs only if flag absent
```

## Phrase-Based Trigger (watchdog)

The watchdog scans agent session JSONL files for an exact armed phrase. When detected, it creates the sentinel flag.

```bash
export ARMED_PHRASE="KILL: AGENT STOP NOW"
export SESSIONS_DIR="$HOME/.openclaw/agents/main/sessions"
bash scripts/kill_switch_watchdog.sh
```

Run via cron every minute:
```cron
* * * * * /path/to/scripts/kill_switch_watchdog.sh >> /tmp/watchdog.log 2>&1
```

Or via launchd (macOS) — create `~/Library/LaunchAgents/ai.kill-switch.watchdog.plist` with `StartInterval=60`.

## Configuration (env vars)

| Variable | Default | Purpose |
|---|---|---|
| `KILL_SWITCH_STATE_DIR` | `$HOME/.ai-kill-switch` | Where flag/log/state live |
| `KILL_SWITCH_LOGGER_PATTERN` | _(none)_ | `pkill -f` pattern to terminate on trigger |
| `ARMED_PHRASE` | `KILL: AGENT STOP NOW` | Watchdog trigger phrase |
| `SESSIONS_DIR` | `$HOME/.openclaw/agents/main/sessions` | JSONL logs to scan |
| `NOTIFY_TARGET` | _(empty)_ | Phone/JID to alert on trigger |
| `NOTIFY_CHANNEL` | `whatsapp` | Notification channel |

## Why Phrase-Based?

Typing a short kill phrase anywhere the agent is listening (WhatsApp, Twitch chat, a shell session) instantly halts it. No UI, no password, no latency. Designed for the moment you realize something is wrong and you want it *stopped now*.

Choose an armed phrase that:
- Is unlikely to appear naturally in conversation
- Contains a distinctive marker like `KILL:` or `STOP-NOW:`
- You can type reliably under stress

## Full Setup

See `references/setup.md` (if present) for LaunchAgent plist and recovery procedures.

<!-- A·R·E·S 🛡️ | Mumbai | 2026-04-05 | github.com/rushindrasinha -->
