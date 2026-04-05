# 📊 Weekly Cost Report

Turn OpenClaw session logs into a weekly per-model cost breakdown you can actually use.

---

## What this skill is for

Cost awareness usually fails in one of two ways:
- you track nothing and get surprised later
- you collect data but never turn it into a decision-ready summary

This skill fixes that by aggregating session usage into a weekly report.

## What it helps you answer

- which models are costing the most
- how usage changed this week
- whether costs are concentrated or diffuse
- where optimization is likely to matter

## Best use cases

- personal AI ops stacks
- founder/operator cost visibility
- weekly reporting rituals
- model mix reviews

## Setup

Read [`SKILL.md`](./SKILL.md) for:
- log source expectations
- aggregation behavior
- reporting format
- delivery options

## Why this matters

Usage without visibility becomes drift.
A simple weekly breakdown is often enough to catch waste before it becomes habit.

## Limitations

- depends on reliable session log data
- reporting quality is only as good as the underlying usage metadata
- not a replacement for provider billing exports when exact finance-grade reconciliation is required

## File structure

```text
weekly-cost-report/
├── README.md
├── SKILL.md
└── scripts/
```

## Related skills

- [gateway-watchdog](../gateway-watchdog/)
- [weekly-reality-capture](../weekly-reality-capture/)

---

Built for OpenClaw workflows. Read [`SKILL.md`](./SKILL.md) before deployment.
