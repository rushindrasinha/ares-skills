#!/usr/bin/env python3
"""
identify.py — Identify a song from an audio file using the AudD API.

Usage:
    AUDD_API_TOKEN=xxx python3 identify.py <audio_file_path>

Returns formatted song info (title, artist, album, Spotify/Apple Music links).
Get a free AudD token at: https://audd.io/
"""

import sys
import os
import json
import urllib.request
import urllib.error
import mimetypes

AUDD_API_URL = "https://api.audd.io/"


def _multipart_post(url: str, fields: dict, file_path: str) -> dict:
    """Minimal stdlib multipart/form-data POST (avoids requests dependency)."""
    boundary = "----AresSongIdentifier" + os.urandom(8).hex()
    CRLF = "\r\n"
    body = []

    for key, value in fields.items():
        body.append(f"--{boundary}{CRLF}")
        body.append(f'Content-Disposition: form-data; name="{key}"{CRLF}{CRLF}')
        body.append(f"{value}{CRLF}")

    with open(file_path, "rb") as f:
        file_bytes = f.read()
    filename = os.path.basename(file_path)
    ctype = mimetypes.guess_type(filename)[0] or "application/octet-stream"
    body.append(f"--{boundary}{CRLF}")
    body.append(f'Content-Disposition: form-data; name="file"; filename="{filename}"{CRLF}')
    body.append(f"Content-Type: {ctype}{CRLF}{CRLF}")

    head = "".join(body).encode("utf-8")
    tail = f"{CRLF}--{boundary}--{CRLF}".encode("utf-8")
    payload = head + file_bytes + tail

    req = urllib.request.Request(
        url, data=payload,
        headers={"Content-Type": f"multipart/form-data; boundary={boundary}"}
    )
    with urllib.request.urlopen(req, timeout=30) as resp:
        return json.loads(resp.read())


def identify_song(file_path: str) -> str:
    """Send audio file to AudD and return formatted result."""
    token = os.environ.get("AUDD_API_TOKEN")
    if not token:
        return "❌ AUDD_API_TOKEN env var not set. Get a free token at https://audd.io/"

    if not os.path.exists(file_path):
        return f"❌ File not found: {file_path}"

    try:
        data = _multipart_post(
            AUDD_API_URL,
            {"api_token": token, "return": "apple_music,spotify"},
            file_path,
        )
    except urllib.error.URLError as e:
        return f"❌ Request failed: {e}"
    except Exception as e:
        return f"❌ Unexpected error: {e}"

    if data.get("status") != "success":
        err = data.get("error", {}) or {}
        return f"❌ AudD error: {err.get('error_message', 'Unknown error')}"

    result = data.get("result")
    if not result:
        return "🎵 No match found — song not in AudD's database."

    lines = [
        f"🎵 *{result.get('title', 'Unknown')}*",
        f"👤 {result.get('artist', 'Unknown')}",
    ]
    if result.get("album"):
        lines.append(f"💿 {result['album']}")
    if result.get("release_date"):
        lines.append(f"📅 {result['release_date']}")

    spotify = result.get("spotify") or {}
    if isinstance(spotify, dict):
        sp_url = (spotify.get("external_urls") or {}).get("spotify")
        if sp_url:
            lines.append(f"🟢 Spotify: {sp_url}")

    apple = result.get("apple_music") or {}
    if isinstance(apple, dict) and apple.get("url"):
        lines.append(f"🍎 Apple Music: {apple['url']}")

    return "\n".join(lines)


if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: AUDD_API_TOKEN=xxx python3 identify.py <audio_file_path>")
        sys.exit(1)
    print(identify_song(sys.argv[1]))
