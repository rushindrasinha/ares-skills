#!/usr/bin/env python3
"""
transcribe.py — WhatsApp voice note transcriber using mlx_whisper (Apple Silicon).

Usage:
    python3 transcribe.py <audio_file_path>

Transcribes the audio, classifies content type, and prints the result.
Optionally sends via openclaw if NOTIFY_TARGET env var is set.
"""
import sys
import subprocess
import os
from pathlib import Path

# ── Config (override with env vars) ──────────────────────────────────────────
MLX_WHISPER_PATH = os.environ.get("MLX_WHISPER_PATH", "/opt/homebrew/bin/mlx_whisper")
WHISPER_MODEL    = os.environ.get("WHISPER_MODEL", "mlx-community/whisper-large-v3-turbo")
NOTIFY_TARGET    = os.environ.get("NOTIFY_TARGET", "")       # e.g. "+1234567890"
NOTIFY_CHANNEL   = os.environ.get("NOTIFY_CHANNEL", "whatsapp")
OPENCLAW_PATH    = os.environ.get("OPENCLAW_PATH", "/opt/homebrew/bin/openclaw")


def transcribe(filepath: str) -> str | None:
    """
    Transcribe audio using mlx_whisper (Apple Silicon, large-v3-turbo).
    Falls back to openai-whisper base if mlx_whisper not available.
    """
    stem = Path(filepath).stem

    # Primary: mlx_whisper (Apple Silicon optimised, much higher accuracy)
    if Path(MLX_WHISPER_PATH).exists():
        result = subprocess.run(
            [MLX_WHISPER_PATH, str(filepath),
             "--model", WHISPER_MODEL,
             "--output-format", "txt",
             "--output-dir", "/tmp/"],
            capture_output=True, text=True, timeout=120
        )
        txt_file = Path(f"/tmp/{stem}.txt")
        if txt_file.exists():
            return txt_file.read_text().strip()
        if result.stdout.strip():
            return result.stdout.strip()

    # Fallback: openai-whisper (base model)
    whisper_path = os.environ.get("WHISPER_PATH", "/opt/homebrew/bin/whisper")
    if Path(whisper_path).exists():
        result = subprocess.run(
            [whisper_path, str(filepath),
             "--model", "base",
             "--output_format", "txt",
             "--output_dir", "/tmp/"],
            capture_output=True, text=True, timeout=120
        )
        txt_file = Path(f"/tmp/{stem}.txt")
        if txt_file.exists():
            return txt_file.read_text().strip()

    return None


def classify(text: str) -> str:
    """Heuristic content classifier."""
    lower = text.lower()
    if any(w in lower for w in ["remind", "todo", "task", "need to", "should", "must", "idea", "build", "make"]):
        return "💡 *Idea / Task*"
    elif any(w in lower for w in ["tell", "message", "send", "write", "reply", "say"]):
        return "✉️ *Draft*"
    return "📝 *Note*"


def notify(message: str) -> None:
    """Send via openclaw if NOTIFY_TARGET is configured."""
    if not NOTIFY_TARGET:
        return
    subprocess.run(
        [OPENCLAW_PATH, "message", "send",
         "--target", NOTIFY_TARGET,
         "--channel", NOTIFY_CHANNEL,
         "--message", message],
        capture_output=True, timeout=30
    )


if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: transcribe.py <audio_file_path>")
        sys.exit(1)

    filepath = sys.argv[1]
    transcript = transcribe(filepath)

    if not transcript:
        msg = f"🎙️ *Voice Note* (transcription failed)\nFile: {Path(filepath).name}"
        print(msg)
        notify(msg)
        sys.exit(1)

    prefix = classify(transcript)
    msg = f"{prefix}\n\n{transcript}\n\n_Transcribed from voice note_"
    print(msg)
    notify(msg)
