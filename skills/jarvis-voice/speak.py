"""
JARVIS-style Text-to-Speech engine using Microsoft Edge neural voices.
Converts text to natural-sounding speech and plays it.

Usage:
    echo "Hello world" | python speak.py
    python speak.py --text "Hello world"
    python speak.py --text "Hello world" --voice en-GB-RyanNeural --rate "+10%"
"""

import argparse
import asyncio
import os
import re
import subprocess
import sys
import tempfile

import edge_tts

# Default JARVIS-like voice settings
DEFAULT_VOICE = "en-GB-RyanNeural"
DEFAULT_RATE = "+5%"       # Slightly faster for that snappy JARVIS feel
DEFAULT_VOLUME = "+0%"
DEFAULT_PITCH = "-5Hz"     # Slightly deeper


def strip_markdown(text: str) -> str:
    """Strip markdown formatting to produce clean spoken text."""
    # Remove code blocks (``` ... ```)
    text = re.sub(r"```[\s\S]*?```", " code block omitted ", text)
    # Remove inline code (`...`)
    text = re.sub(r"`([^`]+)`", r"\1", text)
    # Remove headers (# ... )
    text = re.sub(r"^#{1,6}\s+", "", text, flags=re.MULTILINE)
    # Remove bold/italic markers
    text = re.sub(r"\*{1,3}(.*?)\*{1,3}", r"\1", text)
    text = re.sub(r"_{1,3}(.*?)_{1,3}", r"\1", text)
    # Remove links [text](url) -> text
    text = re.sub(r"\[([^\]]+)\]\([^\)]+\)", r"\1", text)
    # Remove images ![alt](url)
    text = re.sub(r"!\[([^\]]*)\]\([^\)]+\)", r"\1", text)
    # Remove horizontal rules
    text = re.sub(r"^[-*_]{3,}\s*$", "", text, flags=re.MULTILINE)
    # Remove bullet points
    text = re.sub(r"^\s*[-*+]\s+", "", text, flags=re.MULTILINE)
    # Remove numbered lists prefix
    text = re.sub(r"^\s*\d+\.\s+", "", text, flags=re.MULTILINE)
    # Remove blockquotes
    text = re.sub(r"^>\s+", "", text, flags=re.MULTILINE)
    # Remove HTML tags
    text = re.sub(r"<[^>]+>", "", text)
    # Collapse multiple newlines
    text = re.sub(r"\n{3,}", "\n\n", text)
    # Collapse multiple spaces
    text = re.sub(r"  +", " ", text)
    # Remove file paths like /path/to/file:123
    text = re.sub(r"[\w/\\.-]+:\d+", "", text)
    return text.strip()


def truncate_for_speech(text: str, max_chars: int = 2000) -> str:
    """Truncate long text for speech, keeping it natural."""
    if len(text) <= max_chars:
        return text
    # Find a sentence boundary near the limit
    truncated = text[:max_chars]
    last_period = truncated.rfind(".")
    last_question = truncated.rfind("?")
    last_exclaim = truncated.rfind("!")
    cut_point = max(last_period, last_question, last_exclaim)
    if cut_point > max_chars * 0.5:
        return truncated[:cut_point + 1] + " That's the summary of my response."
    return truncated + "... I'll spare you the rest."


async def generate_speech(text: str, output_path: str, voice: str, rate: str, volume: str, pitch: str):
    """Generate speech audio file using edge-tts."""
    communicate = edge_tts.Communicate(
        text,
        voice=voice,
        rate=rate,
        volume=volume,
        pitch=pitch,
    )
    await communicate.save(output_path)


def play_audio(filepath: str):
    """Play an MP3 file using PowerShell's WPF MediaPlayer (Windows)."""
    ps_script = f'''
Add-Type -AssemblyName PresentationCore
$player = New-Object System.Windows.Media.MediaPlayer
$player.Open([uri]"{filepath}")
Start-Sleep -Milliseconds 300
$player.Play()
# Wait for duration to be available
$attempts = 0
while ($player.NaturalDuration.HasTimeSpan -eq $false -and $attempts -lt 50) {{
    Start-Sleep -Milliseconds 100
    $attempts++
}}
if ($player.NaturalDuration.HasTimeSpan) {{
    $duration = $player.NaturalDuration.TimeSpan.TotalSeconds
    Start-Sleep -Seconds ($duration + 0.3)
}}
else {{
    Start-Sleep -Seconds 5
}}
$player.Close()
'''
    subprocess.run(
        ["powershell", "-ExecutionPolicy", "Bypass", "-Command", ps_script],
        capture_output=True,
        timeout=120,
    )


def main():
    parser = argparse.ArgumentParser(description="JARVIS TTS - Speak text aloud")
    parser.add_argument("--text", "-t", type=str, help="Text to speak (reads from stdin if not provided)")
    parser.add_argument("--voice", "-v", type=str, default=DEFAULT_VOICE, help=f"Voice name (default: {DEFAULT_VOICE})")
    parser.add_argument("--rate", "-r", type=str, default=DEFAULT_RATE, help="Speech rate adjustment")
    parser.add_argument("--volume", type=str, default=DEFAULT_VOLUME, help="Volume adjustment")
    parser.add_argument("--pitch", "-p", type=str, default=DEFAULT_PITCH, help="Pitch adjustment")
    parser.add_argument("--raw", action="store_true", help="Don't strip markdown formatting")
    parser.add_argument("--max-chars", type=int, default=2000, help="Max characters to speak (default: 2000)")
    args = parser.parse_args()

    # Get text from argument or stdin
    if args.text:
        text = args.text
    elif not sys.stdin.isatty():
        text = sys.stdin.read()
    else:
        print("Error: No text provided. Use --text or pipe text via stdin.", file=sys.stderr)
        sys.exit(1)

    if not text.strip():
        sys.exit(0)

    # Clean up text for speech
    if not args.raw:
        text = strip_markdown(text)
    text = truncate_for_speech(text, args.max_chars)

    if not text.strip():
        sys.exit(0)

    # Generate and play speech
    with tempfile.NamedTemporaryFile(suffix=".mp3", delete=False) as tmp:
        tmp_path = tmp.name

    try:
        asyncio.run(generate_speech(text, tmp_path, args.voice, args.rate, args.volume, args.pitch))
        play_audio(tmp_path)
    finally:
        try:
            os.unlink(tmp_path)
        except OSError:
            pass


if __name__ == "__main__":
    main()
