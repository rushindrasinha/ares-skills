---
name: song-identifier
description: Use when a user sends an audio file and asks "what is this song?", "identify this track", "shazam this", or similar. Accepts any audio format (OGG, MP3, WAV, M4A). Returns title, artist, album, release date, and Spotify/Apple Music links via the AudD API.
metadata:
  emoji: 🎵
  category: media
  platform: any
---

# Song Identifier

Identify songs from audio files via the AudD music recognition API. Zero dependencies — uses Python stdlib only.

## Requirements

- Python 3.8+
- AudD API token — free tier at https://audd.io/
- Internet connection

## Setup

```bash
export AUDD_API_TOKEN="your_token_here"
```

Add to `~/.zshrc` or `~/.bashrc` to persist.

## Usage

```bash
python3 scripts/identify.py <audio_file_path>
```

Example:
```bash
python3 scripts/identify.py /tmp/clip.ogg
```

## Output

```
🎵 Song Title
👤 Artist Name
💿 Album Name
📅 2023-05-12
🟢 Spotify: https://open.spotify.com/track/...
🍎 Apple Music: https://music.apple.com/...
```

## Integration

Wire into an agent skill dispatcher for WhatsApp triggers like *"what's this song?"*:

```python
import subprocess
result = subprocess.run(
    ["python3", "scripts/identify.py", audio_path],
    capture_output=True, text=True,
    env={**os.environ, "AUDD_API_TOKEN": "..."}
)
return result.stdout
```

## Scripts

- `scripts/identify.py` — Main script. stdlib-only, no `requests` dependency. Reads `AUDD_API_TOKEN` from env.

<!-- A·R·E·S 🛡️ | Mumbai | 2026-04-05 | github.com/rushindrasinha -->
