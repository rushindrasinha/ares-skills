---
name: weekly-reality-capture
description: Auto-generate a reality-first weekly log from daily memory logs, git history, and agent state. Uses Claude to synthesize what actually happened — not a strategic filter, not a curated narrative. Supports backfill by week number. Use when a user says "weekly recap", "what happened this week", "weekly capture", or "reality check".
metadata:
  emoji: 📸
  category: memory
  platform: any (requires Anthropic API key)
---

# Weekly Reality Capture

Synthesize a reality-first weekly log from multiple data sources. The key insight: most weekly reviews optimize for narrative. This one optimizes for truth.

## Data Sources

| Source | What it captures |
|---|---|
| Daily memory logs | What the agent did/discussed each day |
| Git log | What code actually changed |
| Agent session state | Open threads, pending follow-ups |
| Open threads JSON | Carried-over work items |

## Usage

```bash
# Current week
python3 scripts/capture.py

# Specific week
python3 scripts/capture.py --week 2026-W14

# Dry run (print synthesis prompt, don't call Claude)
python3 scripts/capture.py --dry-run
```

## Configuration (env vars)

| Variable | Default | Purpose |
|---|---|---|
| `ANTHROPIC_API_KEY` | _(required)_ | Claude API key for synthesis |
| `CAPTURE_MODEL` | `claude-sonnet-4-5-20250514` | Model for synthesis |
| `MEMORY_DIR` | `~/agent-workspace/memory` | Daily log directory (`YYYY-MM-DD.md` files) |
| `WEEKLY_DIR` | `~/agent-workspace/weekly` | Output directory for weekly captures |
| `REPO_DIR` | `~/agent-workspace` | Git repo to pull log from |
| `SESSION_STATE_PATH` | _(optional)_ | Path to `session_state.json` |
| `OPEN_THREADS_PATH` | _(optional)_ | Path to `open_threads.json` |

## Output Format

Each weekly capture produces `YYYY-WNN.md`:

```markdown
# Week 14 — 2026-03-31 to 2026-04-06

## What Actually Happened
- ...

## Decisions Made
- ...

## Unresolved / Carried Over
- ...

## Patterns Noticed
- ...
```

## Why "Reality-First"?

Most automated weekly summaries read like press releases — they highlight wins and bury problems. This tool is designed to report what *actually happened*, including:
- Threads that stalled without resolution
- Promises made but not delivered
- Work that was started then abandoned
- Time spent on ops vs. creative work

The synthesis prompt explicitly instructs Claude to resist narrative smoothing.

## Cron Setup

Run Sunday night to capture the full week:

```cron
0 23 * * 0 /usr/bin/python3 /path/to/weekly-reality-capture/scripts/capture.py >> /tmp/weekly-capture.log 2>&1
```

## Scripts

- `scripts/capture.py` — Main script. Collects data, builds synthesis prompt, calls Claude, writes output.

<!-- A·R·E·S 🛡️ | Mumbai | 2026-04-05 | github.com/rushindrasinha -->
