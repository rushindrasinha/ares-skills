---
name: gateway-watchdog
description: Monitor OpenClaw Gateway health by tailing logs for error patterns — 429 rate limits, auth failures, delivery failures, timeouts. Alert when error rate crosses thresholds. Use when setting up production monitoring for an OpenClaw Gateway deployment, or when a user says "watch the gateway", "monitor gateway errors", "alert me on gateway failures".
metadata:
  emoji: 🛰️
  category: ops
  platform: any (OpenClaw)
---

# Gateway Watchdog

Watch OpenClaw Gateway logs for error patterns and alert on threshold breaches. Designed to run as a cron job (every 5-15 min) or a long-lived tail process.

## What It Catches

| Pattern | Meaning | Default threshold |
|---|---|---|
| `429` / `rate_limit` | API rate limiting | 3 in 10 min → alert |
| `401` / `auth` / `unauthorized` | Credential failure | 1 → alert immediately |
| `timeout` / `ECONNRESET` | Network instability | 5 in 10 min → alert |
| `delivery_failed` | Message send failure | 1 → alert immediately |
| `5xx` upstream errors | Provider outage | 3 in 5 min → alert |

## Configuration (env vars)

| Variable | Default | Purpose |
|---|---|---|
| `GATEWAY_LOG_PATH` | `~/.openclaw/logs/gateway.log` | Log file to tail |
| `WATCHDOG_STATE_DIR` | `~/.gateway-watchdog` | Where state/cursor files live |
| `WATCHDOG_WINDOW_MIN` | `10` | Rolling window for thresholds |
| `NOTIFY_TARGET` | _(empty)_ | Phone/JID to alert on breach |
| `NOTIFY_CHANNEL` | `whatsapp` | Notification channel |

## Usage

```bash
python3 scripts/watchdog.py
```

Cron every 5 minutes:
```cron
*/5 * * * * /usr/bin/python3 /path/to/gateway-watchdog/scripts/watchdog.py >> /tmp/gateway-watchdog.log 2>&1
```

## Scripts

- `scripts/watchdog.py` — Incremental log scanner with cursor state. Counts patterns in rolling window, sends alert on threshold breach.

<!-- A·R·E·S 🛡️ | Mumbai | 2026-04-05 | github.com/rushindrasinha -->
