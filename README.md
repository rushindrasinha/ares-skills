<h1 align="center">ares-skills</h1>

<p align="center">
  <strong>Production-tested OpenClaw skills for operators, creators, and technical founders.</strong>
</p>

<p align="center">
  Built by <strong>Ares</strong> from running a real autonomous AI operation across WhatsApp, Twitch, media workflows, and agent infrastructure.
</p>

<p align="center">
  <img alt="Skills" src="https://img.shields.io/badge/skills-13-111827?style=flat-square">
  <img alt="OpenClaw" src="https://img.shields.io/badge/OpenClaw-compatible-7c3aed?style=flat-square">
  <img alt="Focus" src="https://img.shields.io/badge/focus-operations%20%2B%20automation-0f766e?style=flat-square">
</p>

> Packaged OpenClaw skills for people who want useful agent behavior, not brittle prompt glue.

Also see: [ares-mbl](https://github.com/rushindrasinha/ares-mbl) — a portable model behavior layer for making LLMs behave with more discipline.

---

## What this repo is

This is a public skill library for OpenClaw.

Each folder is a packaged capability with its own instructions and, where needed, implementation scripts.

The emphasis is practical:
- automation that can survive contact with reality
- operational clarity over prompt mysticism
- explicit configuration over hidden personal context
- behavior that stays auditable under pressure

## Quick install

### Option A — copy one skill into your OpenClaw skills directory

```bash
cp -R whatsapp-voice-transcriber ~/.openclaw/skills/
```

### Option B — symlink during development

```bash
ln -s "$(pwd)/whatsapp-voice-transcriber" ~/.openclaw/skills/whatsapp-voice-transcriber
```

### Option C — browse and adapt for your own stack

```bash
cd whatsapp-voice-transcriber
cat README.md
cat SKILL.md
```

## How each skill is structured

Every skill is self-contained:
- `README.md` — what it does, when to use it, and limitations
- `SKILL.md` — canonical operating instructions for the agent
- `scripts/` — runnable implementation files where needed

That means you can:
- install a skill directly
- study it as a pattern
- fork it into your own internal stack

## Skill index

### Automation & Media

| Skill | What it does | Best for |
|---|---|---|
| [whatsapp-voice-transcriber](./whatsapp-voice-transcriber/) | Local voice-note transcription on Apple Silicon with lightweight classification. | WhatsApp-heavy ops workflows |
| [song-identifier](./song-identifier/) | Identify songs from audio clips and return structured metadata plus links. | Media and research workflows |
| [indic-language-translator](./indic-language-translator/) | Translate across Indian and global languages in an agent-friendly workflow. | Multilingual support and creator ops |

### Twitch

| Skill | What it does | Best for |
|---|---|---|
| [twitch-stream-monitor](./twitch-stream-monitor/) | Detect Twitch channels going live, record automatically, and trigger downstream actions. | Stream capture and monitoring |
| [twitch-ai-chatbot](./twitch-ai-chatbot/) | Run an AI chatbot in Twitch chat with configurable triggers and guardrails. | Live community interaction |

### Agent Operations

| Skill | What it does | Best for |
|---|---|---|
| [ai-agent-kill-switch](./ai-agent-kill-switch/) | Emergency stop primitive for autonomous agents. | Safety and shutdown control |
| [gateway-watchdog](./gateway-watchdog/) | Monitor OpenClaw Gateway logs for auth failures, 429s, and timeout signatures. | Reliability and incident response |
| [weekly-cost-report](./weekly-cost-report/) | Parse OpenClaw logs into a weekly cost breakdown by model. | Usage and cost review |
| [system-state-injection](./system-state-injection/) | Inject live infra and integration state into agent context. | Reducing stale-recall failures |
| [weekly-reality-capture](./weekly-reality-capture/) | Build a reality-first weekly synthesis from logs, git history, and agent state. | Executive review and retrospectives |

### Model Behavior & Prompt Engineering

| Skill | What it does | Best for |
|---|---|---|
| [cricd-prompt-standard](./cricd-prompt-standard/) | Structured prompt format for delegated work: Context, Relevance, Instruction, Constraints, Demonstration. | Delegation quality control |
| [critique-loop-protocol](./critique-loop-protocol/) | Draft → critique → revise pattern for high-stakes outputs. | Strategy, publishing, money work |
| [gstack-coding-discipline](./gstack-coding-discipline/) | Scope-aware coding-task dispatch from simple fixes to full implementation pipelines. | Better coding agent execution |

## Example workflow

A typical adoption path looks like this:

1. pick one skill that solves a real recurring pain
2. copy it into your OpenClaw skills directory
3. read `README.md` for the overview
4. read `SKILL.md` for exact behavior
5. test it on one live workflow
6. adapt config and scripts only after the baseline works

## Design philosophy

These skills are built around a few non-negotiables:
- **useful over clever**
- **operational clarity over prompt mysticism**
- **configuration over hardcoded personal context**
- **strong source-of-truth discipline**
- **agent behavior that remains inspectable under pressure**

## Who this is for

This repo is best for:
- OpenClaw operators
- solo founders building personal AI infrastructure
- creator-operators automating media workflows
- teams that want skill patterns they can actually adapt

## Contributing

If you want to contribute:

1. fork the repo
2. add a self-contained skill folder
3. include both `README.md` and `SKILL.md`
4. keep assumptions explicit
5. submit a PR with a clear real-world use case

Good skills are narrow, legible, and operationally honest.

## Repo description recommendation

If you keep the current GitHub description, it’s fine. If you want a stronger one, use:

**Production-tested OpenClaw skills for WhatsApp automation, Twitch ops, agent safety, and prompt discipline.**

---

Built by [Ares](https://github.com/rushindrasinha)
