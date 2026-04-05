# ares-skills

Public [OpenClaw](https://openclaw.com) agent skills built by **Ares** — an AI co-founder stack for founders and operators.

WhatsApp automation, Twitch monitoring, AI chatbots, model behavior frameworks, and more.

> Also see: [ares-mbl](https://github.com/rushindrasinha/ares-mbl) — Make any AI model behave more like Claude. 8 named failure modes. Drop-in system prompt.

---

## Skills Index

### Automation & Media

| Skill | Description |
|---|---|
| 🎙️ [whatsapp-voice-transcriber](./whatsapp-voice-transcriber/) | Transcribe voice notes locally with mlx_whisper (Apple Silicon). Classify content as task, draft, or note. Zero API cost. |
| 🎵 [song-identifier](./song-identifier/) | Identify songs from audio files via AudD. Returns title, artist, Spotify & Apple Music links. |
| 🌐 [indic-language-translator](./indic-language-translator/) | Translate to/from 13 Indian + 10 global languages using Gemini 2.5 Flash. CLI + module. |

### Twitch

| Skill | Description |
|---|---|
| 📺 [twitch-stream-monitor](./twitch-stream-monitor/) | Auto-detect channels going live, record with streamlink, upload to Drive, send notifications. |
| 🤖 [twitch-ai-chatbot](./twitch-ai-chatbot/) | AI chatbot for Twitch via pure WebSocket IRC. Model-agnostic, configurable trigger word, viewer memory. |

### Agent Operations

| Skill | Description |
|---|---|
| 🛑 [ai-agent-kill-switch](./ai-agent-kill-switch/) | Phrase-triggered emergency stop for AI agents. Flag-file architecture. Survives restarts. |
| 🛰️ [gateway-watchdog](./gateway-watchdog/) | Monitor OpenClaw Gateway logs for 429s, auth failures, timeouts. Alert on threshold breach. |
| 📊 [weekly-cost-report](./weekly-cost-report/) | Parse OpenClaw session logs, aggregate per-model API costs for the last 7 days. |
| 🔬 [system-state-injection](./system-state-injection/) | Inject live system health into agent context. Eliminates stale-recall failures. |
| 📸 [weekly-reality-capture](./weekly-reality-capture/) | Auto-generate reality-first weekly logs from memory + git + agent state. |

### Model Behavior & Prompt Engineering

| Skill | Description |
|---|---|
| 📐 [cricd-prompt-standard](./cricd-prompt-standard/) | The CRICD framework for sub-agent prompts — Context, Relevance, Instruction, Constraints, Demonstration. |
| 🔄 [critique-loop-protocol](./critique-loop-protocol/) | When and how to run draft → critique → revise loops. Trigger conditions + anti-patterns. |
| ⚙️ [gstack-coding-discipline](./gstack-coding-discipline/) | 5-tier dispatch for coding tasks — SIMPLE to FULL, matched rigor to risk. |

---

## Usage

Each skill is a self-contained directory with:
- `SKILL.md` — what it does, how to configure, how to use
- `scripts/` — runnable scripts (where applicable)

Most skills are designed for [OpenClaw](https://openclaw.com) but work standalone with any agent framework or even plain CLI usage.

## Configuration

All skills use **environment variables** for configuration — no hardcoded paths, tokens, or account data. Check each skill's `SKILL.md` for the full env var reference.

## License

MIT

---

*Built by [Ares](https://github.com/rushindrasinha) — Mumbai, India*

<!-- A·R·E·S 🛡️ | Mumbai | 2026-04-05 | github.com/rushindrasinha -->
