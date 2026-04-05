# 📐 CRICD Prompt Standard

A structured prompt framework for delegated agent work: **Context → Relevance → Instruction → Constraints → Demonstration**.

---

## Why this skill exists

Most bad sub-agent output is not a model problem.
It is a briefing problem.

CRICD exists to force a better prompt shape before work starts. It gives the agent:
- the world it is operating in
- the exact materials that matter
- the concrete job to do
- the rails it must stay inside
- one example of what good looks like

That last part matters more than most people think.

## What CRICD does well

- reduces ambiguous delegations
- improves output consistency across models
- makes high-stakes tasks easier to review
- forces you to specify quality before you ask for it

## The framework

### C — Context
What this task is, why it matters, and what environment it lives inside.

### R — Relevance
Which files, docs, prior work, or constraints the agent should anchor to.

### I — Instruction
The exact job. Prefer ordered steps over fuzzy objectives.

### C — Constraints
What the agent must not do. Scope boundaries, safety rails, format rules.

### D — Demonstration
One compact example of what a 10/10 answer or deliverable looks like.

## When to use it

Use CRICD when:
- you are spawning a sub-agent
- the task is non-trivial
- output quality matters more than raw speed
- you want repeatability across runs or models

## Why this matters operationally

A good prompt framework is not documentation theater.
It is a force multiplier.

The better the briefing, the less cleanup you do later.

## Setup

Read [`SKILL.md`](./SKILL.md) for the exact guidance and integration pattern.

## Limitations

- CRICD improves task quality; it does not replace judgment
- overusing it for tiny tasks can add unnecessary ceremony
- demonstration quality matters — weak examples produce weak outputs

## File structure

```text
cricd-prompt-standard/
├── README.md
└── SKILL.md
```

## Related skills

- [critique-loop-protocol](../critique-loop-protocol/)
- [gstack-coding-discipline](../gstack-coding-discipline/)

---

Built for OpenClaw workflows. Read [`SKILL.md`](./SKILL.md) before adoption.
