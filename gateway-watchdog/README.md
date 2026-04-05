# 🛰️ Gateway Watchdog

Monitor OpenClaw Gateway health by watching for the failure patterns that actually matter: auth problems, timeouts, delivery failures, and rate-limit bursts.

---

## What this skill is for

Gateways do not usually fail in dramatic ways first.
They fail quietly:
- more 429s
- more auth errors
- more delivery misses
- more “it sort of works” drift

This skill is for catching that early.

## What it watches

Depending on configuration, the watchdog can flag:
- authentication failures
- timeout spikes
- rate-limit bursts
- delivery issues
- suspicious error-rate changes over time

## Why this matters

A healthy assistant stack depends less on “is the process running?” and more on “is it still behaving normally?”

That is what this skill tracks.

## Best use cases

- long-running OpenClaw deployments
- messaging-heavy automation
- ops stacks where silent degradation is dangerous
- personal assistants where missed delivery breaks trust

## Setup

Use [`SKILL.md`](./SKILL.md) for:
- log path expectations
- thresholds
- alerting behavior
- scheduling / recurring checks

## Limitations

- alert quality depends on threshold quality
- log parsing is not the same as full observability
- should be paired with a live state layer for better system truth

## File structure

```text
gateway-watchdog/
├── README.md
├── SKILL.md
└── scripts/
```

## Related skills

- [system-state-injection](../system-state-injection/)
- [weekly-cost-report](../weekly-cost-report/)

---

Built for OpenClaw workflows. Read [`SKILL.md`](./SKILL.md) before rollout.
