# ares-skills

A curated collection of public OpenClaw skills built by **Ares** — practical agent capabilities for operators, creators, and technical founders.

This repository is not a random dump of prompts. It is a packaged skill library covering:
- automation and media workflows
- Twitch operations
- agent safety and observability
- model behavior and prompt discipline

> Also see: [ares-mbl](https://github.com/rushindrasinha/ares-mbl) — a portable model behavior layer for making LLMs behave with more discipline.

---

## Repository structure

Each skill is packaged as its own folder and is meant to be understandable on its own.

Every skill contains:
- `README.md` — product-facing overview, what it does, when to use it, limitations, and navigation
- `SKILL.md` — canonical operational instructions, requirements, configuration, and usage details
- `scripts/` — runnable implementation files where needed

---

## Skills

### Automation & Media

| Skill | What it does |
|---|---|
| [whatsapp-voice-transcriber](./whatsapp-voice-transcriber/) | Local voice-note transcription on Apple Silicon using mlx_whisper, with lightweight content classification. |
| [song-identifier](./song-identifier/) | Identify songs from audio clips and return structured metadata plus listening links. |
| [indic-language-translator](./indic-language-translator/) | Translate across Indian and global languages in a CLI- and agent-friendly workflow. |

### Twitch

| Skill | What it does |
|---|---|
| [twitch-stream-monitor](./twitch-stream-monitor/) | Detect Twitch channels going live, record automatically, and trigger uploads or notifications. |
| [twitch-ai-chatbot](./twitch-ai-chatbot/) | Run an AI chatbot in Twitch chat over IRC/WebSocket with configurable trigger words and guardrails. |

### Agent Operations

| Skill | What it does |
|---|---|
| [ai-agent-kill-switch](./ai-agent-kill-switch/) | Emergency stop primitive for autonomous agents. Safe, explicit, and restart-resistant. |
| [gateway-watchdog](./gateway-watchdog/) | Monitor OpenClaw Gateway logs for failure signatures like auth errors, 429s, and timeouts. |
| [weekly-cost-report](./weekly-cost-report/) | Parse OpenClaw logs into a usable weekly cost breakdown by model. |
| [system-state-injection](./system-state-injection/) | Inject live infra and integration state into agent context to reduce stale-recall failures. |
| [weekly-reality-capture](./weekly-reality-capture/) | Build a reality-first weekly synthesis from logs, git history, and agent state. |

### Model Behavior & Prompt Engineering

| Skill | What it does |
|---|---|
| [cricd-prompt-standard](./cricd-prompt-standard/) | Structured prompt format for delegated work: Context, Relevance, Instruction, Constraints, Demonstration. |
| [critique-loop-protocol](./critique-loop-protocol/) | A clear draft → critique → revise pattern for high-stakes outputs. |
| [gstack-coding-discipline](./gstack-coding-discipline/) | Scope-aware coding-task dispatch framework, from simple fixes to full implementation pipelines. |

---

## How to use this repo

If you want to explore a skill quickly:
1. open that skill folder
2. read `README.md` for the overview
3. read `SKILL.md` for the exact operational instructions
4. inspect `scripts/` if you are adapting or extending the implementation

If you want to install or adapt these for your own stack, prefer making configuration explicit instead of baking credentials or environment assumptions into the code.

---

## Design principles

These skills are built around a few non-negotiables:
- **useful over clever**
- **operational clarity over prompt mysticism**
- **configuration over hardcoded personal context**
- **strong source-of-truth discipline**
- **agent behavior that stays auditable under pressure**

---

## License

MIT

---

Built by [Ares](https://github.com/rushindrasinha)
