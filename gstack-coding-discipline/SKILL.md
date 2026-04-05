---
name: gstack-coding-discipline
description: A 5-tier dispatch framework for coding tasks in AI agent workflows. Routes tasks from SIMPLE (one-file typo fix) to FULL (multi-day feature build) with appropriate rigor at each level. Prevents over-engineering simple tasks and under-planning complex ones.
metadata:
  emoji: ⚙️
  category: model-behavior
  platform: any (designed for Claude Code / OpenClaw)
---

# gstack Coding Discipline

A 5-tier dispatch framework that matches coding task complexity to the right level of rigor. Inspired by the gstack skill set for Claude Code.

## The Problem

Without dispatch tiers:
- Simple typo fixes get full architecture reviews (slow, wasteful)
- Complex features get "just code it" treatment (bugs, rework)
- No shared vocabulary for "how much process does this need?"

## The 5 Tiers

### Tier 1: SIMPLE
**When**: Typo, one-file config change, single obvious fix.
**Process**: Direct execution. No planning needed.
**Example**: Fix a misspelled variable name. Update a version number. Add a missing import.

```
Task: "Fix the typo in line 42 of config.py"
→ Just do it. No plan. No review.
```

### Tier 2: MEDIUM
**When**: Multi-file feature, refactors, adding a new endpoint.
**Process**: Lightweight discipline. Read the relevant files first, state the plan in 2-3 bullets, then execute.
**Example**: Add a new API endpoint that touches the router, handler, and tests.

```
Task: "Add a /health endpoint that returns service status"
→ Read existing routes. Plan: add route + handler + test. Execute.
```

### Tier 3: HEAVY
**When**: Specific audit or review needed. Code quality concerns. Performance investigation.
**Process**: Formal investigation with structured output. Use commands like `/review`, `/qa`, `/investigate`.
**Example**: "Why is the billing endpoint slow?" → Profile, measure, report.

```
Task: "Audit the auth middleware for security issues"
→ Systematic file-by-file review. Risk matrix output. Prioritized findings.
```

### Tier 4: FULL
**When**: Complete feature build, multi-day scope, new service.
**Process**: Full lifecycle: plan → implement → test → ship → report.
**Example**: Build a new notification service from scratch.

```
Task: "Build the weekly digest email feature"
→ /autoplan → implement each component → integration test → /ship → report back
```

### Tier 5: PLAN
**When**: Plan before building. Architecture decisions. Design review needed before code.
**Process**: Plan only — no code. Produce a plan document for human review.
**Example**: "How should we restructure the database for multi-tenancy?"

```
Task: "Design the caching strategy for the API"
→ /office-hours → /autoplan → save plan file → report back for approval
```

## Dispatch Decision Tree

```
Is it a one-file, obvious change?  ──▶ SIMPLE
         │ NO
         ▼
Does it touch 2-5 files with clear scope?  ──▶ MEDIUM
         │ NO
         ▼
Is it an audit/review/investigation?  ──▶ HEAVY
         │ NO
         ▼
Is it a full feature that needs building?  ──▶ FULL
         │
Does it need design approval first?  ──▶ PLAN
```

## Key Commands (gstack vocabulary)

| Command | Tier | Purpose |
|---|---|---|
| `/autoplan` | FULL, PLAN | Generate implementation plan from requirements |
| `/review` | HEAVY | Structured code review |
| `/ship` | FULL | Pre-ship checklist (tests, lint, changelog) |
| `/qa` | HEAVY, FULL | Quality assurance pass |
| `/cso` | HEAVY | Chief Security Officer review |
| `/investigate` | HEAVY | Deep-dive into a specific problem |
| `/design-review` | PLAN | Architecture review before implementation |
| `/retro` | FULL | Post-implementation retrospective |
| `/office-hours` | PLAN | Open-ended design discussion |

## Integration with CRICD

The tier determines how much CRICD structure your prompt needs:

| Tier | CRICD | Notes |
|---|---|---|
| SIMPLE | C + I only | Context + Instruction sufficient |
| MEDIUM | C + R + I | Add Relevance (which files) |
| HEAVY | Full CRICD | Everything including Constraints |
| FULL | Full CRICD + D | Demonstration mandatory |
| PLAN | C + I + C | Context, Instruction, Constraints (no code Demo) |

## Anti-Patterns

- **Over-tiering**: Running FULL process on a SIMPLE task → 10x slower, no quality gain
- **Under-tiering**: Running SIMPLE process on a FULL task → bugs, rework, tech debt
- **Tier inflation**: Everything becomes HEAVY because "we should be thorough" → team bottleneck
- **Skipping PLAN for FULL**: Jumping to implementation without design → wrong architecture, costly rework

## Key Principle

Match the rigor to the risk. A typo fix needs zero ceremony. A billing system needs all of it. The 5 tiers give you a shared vocabulary for making that call explicitly instead of by gut feel.

<!-- A·R·E·S 🛡️ | Mumbai | 2026-04-05 | github.com/rushindrasinha -->
