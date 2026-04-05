---
name: cricd-prompt-standard
description: The CRICD framework for structuring sub-agent task prompts — Context, Relevance, Instruction, Constraints, Demonstration. Produces dramatically better output from any LLM sub-agent. Use when spawning sub-agents, writing task prompts, or structuring complex instructions for AI models.
metadata:
  emoji: 📐
  category: model-behavior
  platform: any
---

# CRICD Prompt Standard

A framework for structuring sub-agent task prompts that consistently produces better output than unstructured instructions. Adopted from EgoAlpha prompt-in-context-learning research + Eric (@outsource_) cognitive framework.

## The Framework

Every sub-agent task prompt should include:

| Component | What it is | Example |
|---|---|---|
| **C**ontext | Background, what this is, why it matters | "We're migrating from Postgres to Supabase. 200 tables, 3 services depend on it." |
| **R**elevance | Specific files, data, prior decisions to reference | "Schema at db/schema.sql. Migration plan in docs/migration.md." |
| **I**nstruction | Exact steps, what to do, in order | "1. Audit schema for Supabase incompatibilities. 2. Write migration script. 3. Test against staging." |
| **C**onstraints | What NOT to do, limits, safety rails | "Do NOT drop tables. Do NOT modify the auth schema. Max 500 lines per migration file." |
| **D**emonstration | One compact example of 10/10 output | "Example migration file: ..." |

## Minimum Viable Prompt

Even simple tasks benefit from **C + I** minimum:
```
Context: The gateway crashed after a config change.
Instruction: Check ~/.openclaw/openclaw.json for syntax errors, fix them, restart gateway.
```

## Full Example

```
## Context
We're writing a weekly cost report script for OpenClaw. It needs to parse JSONL session
logs, aggregate per-model costs, and produce a formatted summary.

## Relevance
- Session logs at: ~/.openclaw/agents/main/sessions/*.jsonl
- Each line has: {"message": {"model": "...", "usage": {"cost": {"total": 0.001}}}}
- Prior version: scripts/old_report.py (broken, don't reuse — uses deprecated API)

## Instruction
1. Scan all .jsonl files for entries in the last 7 days
2. Aggregate cost by model and by day
3. Print a formatted report with totals, per-model breakdown, and daily trend
4. Handle missing/malformed entries gracefully (skip, don't crash)

## Constraints
- Python stdlib only (no pandas, no external deps)
- Must complete in <5 seconds on 500MB of logs
- Do NOT read entire files into memory — stream line by line
- Output must be WhatsApp-safe (no markdown tables, use plain text alignment)

## Demonstration
Good output looks like:
📊 Weekly API Cost Report
Period: last 7 days

Total: $12.4521 across 8,432 turns

By model:
  claude-sonnet-4-5: $8.2103 (65.9%)
  claude-haiku-4-5:  $3.1204 (25.1%)
  ...
```

## Output Quality Injections

Always inject these into sub-agent tasks alongside CRICD:

### 1. Voice Persona
Set the tone: *"pragmatic startup CTO"*, *"senior engineer"*, *"concise analyst"*. Never *"helpful assistant"*.

### 2. Output Format Rules
- Tables for comparisons and risks: `Risk | Likelihood | Mitigation`
- Word budget matched to complexity — one-liner for simple, detailed for complex
- Code > description. Diff > explanation. Numbers > vibes.

### 3. End Plans with a Key Principle
One sentence capturing the core insight of the plan.

### 4. Domain Knowledge
Inject specific mechanics. Don't make the model guess at your stack, conventions, or constraints.

### 5. Anti-Patterns (never)
- "Great question!" / "I'd be happy to help!" / "Certainly!"
- Listing options without recommending one
- Explaining what you're about to do instead of doing it
- Summarizing what you just did after doing it
- Asking permission for things you can safely try yourself

## When to Use the Full Framework

| Complexity | Use |
|---|---|
| Typo fix, simple edit | C + I only |
| Multi-file feature | Full CRICD |
| Strategy, roadmap, architecture | Full CRICD + Demonstration mandatory |
| Money involved, public publishing | Full CRICD + critique loop (see `critique-loop-protocol`) |

## Research Background

- CRICD structure draws from EgoAlpha's prompt-in-context-learning research
- The Demonstration component is the highest-leverage addition — showing one example of excellent output anchors model behavior more effectively than pages of instructions
- Anti-patterns list derived from production observation of failure modes across Claude, GPT-4, and Gemini

<!-- A·R·E·S 🛡️ | Mumbai | 2026-04-05 | github.com/rushindrasinha -->
