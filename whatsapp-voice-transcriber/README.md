# 🎙️ WhatsApp Voice Transcriber

Transcribe voice notes locally on Apple Silicon using `mlx_whisper`, then classify the result into something operationally useful.

---

## What this skill is for

Voice notes are fast for humans and expensive for workflows. This skill converts incoming audio into text you can search, quote, route, and act on — without paying per minute to an API.

It is optimized for Apple Silicon and uses `mlx_whisper large-v3-turbo` as the default path.

## Best use cases

- turning WhatsApp voice notes into text automatically
- classifying notes into idea / task / draft / note buckets
- building local-first personal assistant workflows
- keeping transcription private and offline

## What you get

- local transcription with no API cost
- Apple Silicon-friendly performance
- optional content classification on top of raw transcript
- clean integration point for OpenClaw-based messaging flows

## How it works

1. a voice note or audio file is passed to the script
2. `mlx_whisper` transcribes the file locally
3. the transcript is heuristically classified
4. the result can be printed, stored, or sent back via OpenClaw

## Setup

Read [`SKILL.md`](./SKILL.md) for exact requirements and environment variables.

At a high level you need:
- Python 3.10+
- `mlx_whisper` on Apple Silicon
- optional OpenClaw CLI if you want automatic send-back delivery

## Usage

```bash
python3 scripts/transcribe.py /path/to/voice-note.ogg
```

If you want delivery back into chat, configure the relevant env vars in `SKILL.md`.

## Why this matters

Most transcription workflows are either:
- cloud-only,
- too expensive to leave running,
- or too raw to be useful operationally.

This one is designed for everyday assistant use: fast enough, cheap enough, and structured enough to plug into real workflows.

## Limitations

- best on Apple Silicon
- classification is heuristic, not semantic reasoning
- `SKILL.md` is still the source of truth for config and operational details

## File structure

```text
whatsapp-voice-transcriber/
├── README.md
├── SKILL.md
└── scripts/
```

## Related skills

- [indic-language-translator](../indic-language-translator/)
- [song-identifier](../song-identifier/)

---

Built for OpenClaw workflows. Read [`SKILL.md`](./SKILL.md) before deployment.
