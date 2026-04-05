# ⚙️ gstack Coding Discipline

A scope-aware dispatch framework for coding work: match the task to the right level of planning, review, and implementation rigor.

---

## Why this skill exists

Not every coding task deserves the same process.

A typo fix should not get a full architecture review.
A multi-file feature should not be treated like a one-line patch.

This skill gives you a clean routing model so coding work gets the right amount of structure.

## The dispatch model

Typical tiers:
- **SIMPLE** — tiny, obvious, low-risk changes
- **MEDIUM** — multi-file work with some ambiguity
- **HEAVY** — audits, reviews, deep diagnosis, quality-sensitive implementation
- **FULL** — large features or project-scale execution
- **PLAN** — when planning must happen before building

## What it improves

- less over-processing on simple work
- more rigor on risky work
- better use of coding agents like Claude Code / Codex
- cleaner decision about when to review vs when to ship

## Why this matters

Bad engineering process is usually a mismatch problem:
- too much ceremony for small tasks
- too little rigor for large ones

This skill fixes that mismatch.

## Setup

Read [`SKILL.md`](./SKILL.md) for the exact routing rules, tier logic, and recommended commands.

## Limitations

- process quality still depends on operator judgment
- tiers help triage, not truth
- should be paired with clear output standards, not used as process theater

## File structure

```text
gstack-coding-discipline/
├── README.md
└── SKILL.md
```

## Related skills

- [cricd-prompt-standard](../cricd-prompt-standard/)
- [critique-loop-protocol](../critique-loop-protocol/)

---

Built for OpenClaw workflows. Read [`SKILL.md`](./SKILL.md) before adoption.
