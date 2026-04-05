# 🤖 Twitch AI Chatbot

Run a configurable AI chatbot in Twitch chat using IRC over WebSocket — no heavy Twitch API integration required for the core loop.

---

## What this skill does

This skill gives you a prompt-driven Twitch bot that:
- joins a channel
- watches chat
- responds to a trigger word like `!bot`
- calls a model for reply generation
- sends the answer back into chat with configurable guardrails

It is designed for practical deployment, not demos.

## Why this is useful

Most Twitch bot setups are either:
- hardcoded command trees,
- overbuilt app stacks,
- or too generic to feel on-brand.

This approach keeps the architecture simple:
- Twitch IRC via WebSocket
- bot account OAuth token
- model-backed reply generation
- configurable cooldowns and safety rules

## Best use cases

- founder / creator streams
- esports chat moderation + lightweight engagement
- “ask the bot” interactions in live chat
- AI sidekick behavior without a full Twitch app platform build

## What you can customize

- trigger word
- system prompt / personality
- model choice
- cooldowns
- reply style
- channel and bot identity

## How it works

1. connect to Twitch IRC over WebSocket
2. join the target channel
3. listen for messages starting with the trigger word
4. send prompt + recent context to the model
5. reply back in chat as the bot account

## Setup

Use [`SKILL.md`](./SKILL.md) for the exact setup flow.

You will need:
- a Twitch bot account
- an IRC OAuth token
- model credentials for the chosen provider
- the listed Python dependencies

## Why this implementation is strong

It avoids unnecessary complexity.

You do not need a giant backend just to make a Twitch bot feel intelligent.
You need:
- clean connection handling
- safe rate controls
- a good system prompt
- predictable operational behavior

That is what this skill focuses on.

## Limitations

- depends on model credentials
- still subject to Twitch chat rate limits
- prompt quality heavily affects audience experience
- `SKILL.md` remains the canonical operational spec

## File structure

```text
twitch-ai-chatbot/
├── README.md
├── SKILL.md
└── scripts/
```

## Related skills

- [twitch-stream-monitor](../twitch-stream-monitor/)

---

Built for OpenClaw workflows. Read [`SKILL.md`](./SKILL.md) before deployment.
