# 📸 Weekly Reality Capture

Build a reality-first weekly synthesis from logs, git history, and agent state.

---

## Why this skill exists

Most weekly reviews drift toward narrative.
They become strategy theater, selective memory, or self-flattery.

This skill is built around a different standard:
**what actually happened?**

## Inputs it can pull from

Depending on your setup:
- daily memory logs
- git history
- agent state
- open threads or structured state files
- related operational artifacts

## What makes it valuable

It does not try to sound strategic first.
It tries to be true first.

That makes it useful for:
- weekly reviews
- founder reflection
- ops retrospectives
- seeing drift between intention and execution

## Typical workflow

1. collect the week’s artifacts
2. synthesize them into a structured weekly capture
3. output a reality-based summary you can inspect or build on

## Setup

Read [`SKILL.md`](./SKILL.md) for:
- source configuration
- backfill support
- output conventions
- scheduling

## Limitations

- quality depends on source hygiene
- weak logs create weak captures
- synthesis is still interpretation, so the source set matters

## File structure

```text
weekly-reality-capture/
├── README.md
├── SKILL.md
└── scripts/
```

## Related skills

- [system-state-injection](../system-state-injection/)
- [weekly-cost-report](../weekly-cost-report/)

---

Built for OpenClaw workflows. Read [`SKILL.md`](./SKILL.md) before deployment.
