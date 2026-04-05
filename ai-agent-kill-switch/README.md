# 🛑 AI Agent Kill Switch

Emergency stop infrastructure for autonomous agents. Trigger it fast, audit it easily, and make sure it fails safe.

---

## What this skill is for

If an agent can message users, mutate state, or keep running unattended, you need a kill switch.

Not a vague instruction.
Not “please stop.”
A real operational stop mechanism.

This skill packages a phrase-triggered, flag-file-based kill switch designed to be simple, explicit, and hard to accidentally bypass.

## Best use cases

- autonomous assistants with outbound messaging
- cron-driven or event-driven agents
- safety overlays for production automations
- any system where “just stop the bot” needs to work immediately

## Design philosophy

The point of a kill switch is not elegance.
The point is reliability under stress.

This skill favors:
- explicit trigger behavior
- restart-safe state
- auditable stop conditions
- operational simplicity over cleverness

## How it works

1. a trigger phrase or control path is detected
2. the skill writes a stop-state artifact
3. downstream automations check that state before acting
4. automation pauses until the stop state is cleared intentionally

## Why this matters

Most agent systems spend too much time on capability and too little on interruption.
The kill switch is what keeps power from becoming operational stupidity.

## Setup

Read [`SKILL.md`](./SKILL.md) for:
- trigger configuration
- watchdog behavior
- launch/daemon integration
- recovery and reset behavior

## Limitations

- only works if your automations actually respect the stop state
- should be paired with operational review, not treated as total safety
- `SKILL.md` remains the source of truth for implementation details

## File structure

```text
ai-agent-kill-switch/
├── README.md
├── SKILL.md
└── scripts/
```

## Related skills

- [gateway-watchdog](../gateway-watchdog/)
- [system-state-injection](../system-state-injection/)

---

Built for OpenClaw workflows. Read [`SKILL.md`](./SKILL.md) before rollout.
