---
name: whatsapp-voice-transcriber
description: Use when a user sends a voice note and wants it transcribed, or says "transcribe this voice note", "what did I say?", "convert voice to text", or "transcribe this audio". Handles OGG, MP3, WAV, and other audio formats. Outputs transcription with content classification (Idea/Task, Draft, or Note). Uses mlx_whisper large-v3-turbo for Apple Silicon — fully local, no API cost.
metadata:
  emoji: 🎙️
  category: automation
  platform: macOS (Apple Silicon)
---

# WhatsApp Voice Transcriber

Transcribes voice notes locally using mlx_whisper (Apple Silicon) and classifies by content type. No API cost, runs fully offline.

## Requirements

- **mlx_whisper** (recommended): `pip install mlx-whisper` — uses `large-v3-turbo` model on Apple Silicon
- **Fallback**: openai-whisper (`pip install openai-whisper`) — base model
- Python 3.10+
- OpenClaw CLI (optional, for send-back delivery)

## Usage

```bash
python3 scripts/transcribe.py <audio_file_path>
```

Example:
```bash
python3 scripts/transcribe.py /tmp/voice_note.ogg
```

## Configuration (env vars)

| Variable | Default | Description |
|---|---|---|
| `MLX_WHISPER_PATH` | `/opt/homebrew/bin/mlx_whisper` | Path to mlx_whisper binary |
| `WHISPER_MODEL` | `mlx-community/whisper-large-v3-turbo` | Whisper model to use |
| `NOTIFY_TARGET` | _(empty)_ | Phone/JID to send result to via openclaw |
| `NOTIFY_CHANNEL` | `whatsapp` | Channel for notification |
| `OPENCLAW_PATH` | `/opt/homebrew/bin/openclaw` | Path to openclaw binary |

Set `NOTIFY_TARGET` to auto-send transcription after processing:
```bash
NOTIFY_TARGET="+1234567890" python3 scripts/transcribe.py /tmp/voice.ogg
```

## Classification

Heuristic classifier labels each transcription:
- 💡 **Idea / Task** — keywords: remind, task, build, idea, need to
- ✉️ **Draft** — keywords: tell, message, send, write, reply
- 📝 **Note** — everything else

## OpenClaw Integration

Wire into your agent skill dispatcher to auto-transcribe incoming voice notes:

```python
# In your OpenClaw agent logic:
import subprocess, tempfile, os

def handle_voice_note(attachment_path):
    result = subprocess.run(
        ["python3", "~/clawd/.agents/skills/whatsapp-voice-transcriber/scripts/transcribe.py",
         attachment_path],
        capture_output=True, text=True
    )
    return result.stdout.strip()
```

## Model Notes

- **mlx_whisper large-v3-turbo** — best for Apple Silicon (M1/M2/M3). Highly accurate, fast enough for real-time. ~1GB model download on first use.
- **whisper base** — fallback only. Much lower accuracy. Use if no Apple Silicon.
- Model is downloaded automatically on first run.

## Scripts

- `scripts/transcribe.py` — Main script. Transcribes audio, classifies, prints, and optionally sends.

<!-- A·R·E·S 🛡️ | Mumbai | 2026-04-05 | github.com/rushindrasinha -->
