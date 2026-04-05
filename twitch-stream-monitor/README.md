# 📺 Twitch Stream Monitor

Detect Twitch channels going live, record automatically, and trigger downstream notifications or uploads.

---

## What this skill is for

If a stream matters, manual checking is a bad system.

This skill watches a defined channel set and turns “someone just went live” into an operational event you can act on.

## Best use cases

- creator monitoring
- team or org stream tracking
- automatic VOD capture
- downstream upload / archive workflows
- live status notifications for operators

## What it does

Typical flow:
1. poll the configured channel set
2. detect a live transition
3. start recording via `streamlink`
4. optionally upload or notify downstream systems
5. maintain enough state to avoid duplicate triggers

## Why this matters

This is useful because it closes the gap between monitoring and action.
You are not just told a stream is live.
You can capture it immediately.

## Setup

Read [`SKILL.md`](./SKILL.md) for:
- channel configuration
- recording behavior
- destination handling
- scheduling
- notification wiring

## Limitations

- depends on streamlink / environment setup
- polling cadence affects responsiveness
- recording/upload behavior depends on downstream infrastructure

## File structure

```text
twitch-stream-monitor/
├── README.md
├── SKILL.md
└── scripts/
```

## Related skills

- [twitch-ai-chatbot](../twitch-ai-chatbot/)

---

Built for OpenClaw workflows. Read [`SKILL.md`](./SKILL.md) before deployment.
