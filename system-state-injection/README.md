# 🔬 System State Injection

Inject live system reality into agent context so the agent answers status questions from facts, not stale memory.

---

## The problem it solves

Autonomous agents drift when they answer operational questions from memory:
- “Is WhatsApp linked?”
- “Is the gateway healthy?”
- “Did auth expire?”

The fix is simple: write live state to a compact JSON file on a schedule, then force the agent to read it before answering.

This skill packages that pattern.

## Core pattern

**cron → JSON → session-open read rule → better answers**

That one loop eliminates an entire class of stale-recall failures.

## What it checks

Typical checks include:
- gateway status
- disk space
- active sessions
- integration health probes
- custom command-based or file-based checks

The exact checks are configurable.

## Why this skill matters

This is not just a monitoring script.
It is a behavior-control pattern.

Once live state is injected into the agent context, the agent becomes much more reliable at answering:
- what’s up
- what’s broken
- what’s expired
- what needs attention right now

## Typical workflow

1. cron runs `update_state.py`
2. the script probes local services and integrations
3. it writes a compact `system_state.json`
4. your agent is instructed to read that file before answering status questions

## Setup

Use [`SKILL.md`](./SKILL.md) for:
- config schema
- integration examples
- cron wiring
- output structure
- agent prompt rule

## Good fits

Use this if you run:
- OpenClaw with multiple integrations
- a personal ops stack
- long-lived assistant sessions
- any workflow where stale status answers create trust damage

## Limitations

- only as good as the checks you configure
- does not replace full observability
- needs discipline: the agent must actually read the generated state file

## File structure

```text
system-state-injection/
├── README.md
├── SKILL.md
└── scripts/
```

## Related skills

- [gateway-watchdog](../gateway-watchdog/)
- [weekly-reality-capture](../weekly-reality-capture/)

---

Built for OpenClaw workflows. Read [`SKILL.md`](./SKILL.md) before rollout.
