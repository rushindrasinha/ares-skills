# 🎵 Song Identifier

Identify songs from audio clips and return structured metadata plus listening links.

---

## What this skill is for

People send mysterious clips all the time.
A voice note, a short reel rip, a low-quality recording from a room — and the question is simple:
**what song is this?**

This skill turns that into a repeatable workflow.

## Best use cases

- identifying songs from short audio snippets
- WhatsApp or agent-triggered music lookup
- turning ad hoc recognition into structured metadata
- feeding music results into downstream workflows

## What you get

- song title
- artist
- album information when available
- service links like Spotify / Apple Music when returned by the provider

## Setup

Read [`SKILL.md`](./SKILL.md) for:
- audio formats
- provider requirements
- usage examples
- configuration and integration details

## Why this matters

This is a small skill, but high-frequency useful beats theoretically impressive every time.

## Limitations

- accuracy depends on source audio quality
- depends on the backing recognition provider
- not every clip will produce a confident match

## File structure

```text
song-identifier/
├── README.md
├── SKILL.md
└── scripts/
```

## Related skills

- [whatsapp-voice-transcriber](../whatsapp-voice-transcriber/)
- [indic-language-translator](../indic-language-translator/)

---

Built for OpenClaw workflows. Read [`SKILL.md`](./SKILL.md) before deployment.
