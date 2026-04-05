---
name: critique-loop-protocol
description: Formal protocol for draft → critique → revise loops in AI agent workflows. Defines when to use critique loops (money, public publishing, strategy) and when to skip (simple edits, routine coding). Prevents both over-engineering simple tasks and under-reviewing critical ones.
metadata:
  emoji: 🔄
  category: model-behavior
  platform: any
---

# Critique Loop Protocol

A formal decision framework for when and how to run draft → critique → revise loops with AI models.

## The Problem

Without clear trigger conditions:
- **Over-critique**: Simple edits get three rounds of review, wasting time and tokens
- **Under-critique**: Money-touching code ships without adversarial review
- **Cargo-cult critique**: Running the loop for optics, not quality

## When to Use

| Trigger Condition | Why |
|---|---|
| Money is involved | Billing, payments, pricing, financial reports |
| Output will be published publicly | Blog posts, docs, social media, open-source |
| Strategy/roadmap quality matters more than speed | Architecture decisions, quarterly plans |
| Comparing models or proving benchmark claims | Any claim that will be cited needs adversarial review |
| Legal/compliance implications | Contracts, terms, privacy-affecting code |

## When to Skip

| Condition | Why |
|---|---|
| Simple edits (typos, config changes) | Overhead exceeds value |
| Routine coding (well-understood patterns) | Tests catch errors cheaper |
| Low-stakes chat responses | Speed matters more than perfection |
| Time-critical fixes (production down) | Ship now, review later |

## The Three Phases

### Phase 1: Draft (Generate)

Produce the initial output with a clear CRICD prompt (see `cricd-prompt-standard`). Don't self-censor during drafting — capture all ideas, even rough ones.

**Key rule**: The drafter should commit to a recommendation. Never produce "you could do X or Y" — pick one and defend it.

### Phase 2: Critique (Adversarial Review)

A second agent (or second pass with a different system prompt) reviews the draft. The critique prompt:

```
You are reviewing this draft for [CONTEXT].

Your job is adversarial — find problems, not confirm quality. Specifically:

1. FACTUAL: Are there claims that aren't supported by the data provided?
2. COMPLETENESS: What's missing that should be there?
3. RISK: What could go wrong if this ships as-is?
4. CLARITY: Where would a reader be confused?
5. ALTERNATIVES: Is there a clearly better approach the draft missed?

Rate severity: BLOCKING (must fix) | IMPORTANT (should fix) | MINOR (nice to fix).

If the draft is genuinely good, say so and explain why — don't invent problems
to justify your existence.
```

### Phase 3: Revise (Incorporate)

The original drafter (or a synthesis agent) incorporates the critique. Rules:

- Address every BLOCKING item
- Address IMPORTANT items unless there's a clear reason not to (state the reason)
- MINOR items: fix if easy, note if not
- **Never "just patch"** — if the critique reveals a structural problem, restructure

## Anti-Pattern: Critique as Avoidance

The critique loop is NOT a way to avoid committing to a recommendation. If after three rounds of critique you still can't decide, the problem isn't quality — it's decision avoidance. Pick one, ship it, and iterate.

## Implementation Patterns

### Two-Agent Pattern (recommended for high-stakes)
```
Agent A (drafter) → output
Agent B (critic, different system prompt) → critique
Agent A → revised output incorporating critique
```

### Self-Critique Pattern (acceptable for medium-stakes)
```
Agent A → draft with system prompt emphasizing generation
Agent A → critique with system prompt emphasizing adversarial review
Agent A → synthesis
```

### Token Budget

| Complexity | Typical tokens |
|---|---|
| Blog post critique | ~2K draft + ~1K critique + ~2.5K final |
| Architecture review | ~4K draft + ~2K critique + ~5K final |
| Financial report | ~1.5K draft + ~1K critique + ~2K final |

Rule of thumb: critique loop costs ~2x a single generation. Worth it only when the cost of a bad output exceeds the cost of the extra tokens.

## Decision Flowchart

```
Is money/legal involved?  ──▶ YES ──▶ Full critique loop
         │ NO
         ▼
Will it be published?  ──▶ YES ──▶ Full critique loop
         │ NO
         ▼
Is it strategy/architecture?  ──▶ YES ──▶ Self-critique minimum
         │ NO
         ▼
Skip critique loop. Ship it.
```

<!-- A·R·E·S 🛡️ | Mumbai | 2026-04-05 | github.com/rushindrasinha -->
