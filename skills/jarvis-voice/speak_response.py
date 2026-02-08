"""
Claude Code Stop hook - Speaks the assistant's last response using JARVIS TTS.

This script is triggered by the 'Stop' hook event in Claude Code.
It reads the conversation transcript, extracts the last assistant message,
and speaks it aloud using edge-tts neural voices.
"""

import json
import os
import subprocess
import sys


def get_last_assistant_text(transcript_path: str) -> str:
    """Extract the last assistant text response from the transcript JSONL file."""
    if not os.path.exists(transcript_path):
        return ""

    last_assistant_text = ""

    with open(transcript_path, "r", encoding="utf-8") as f:
        for line in f:
            line = line.strip()
            if not line:
                continue
            try:
                entry = json.loads(line)
            except json.JSONDecodeError:
                continue

            # Handle different transcript formats
            role = entry.get("role") or entry.get("type")
            if role != "assistant":
                continue

            # Extract text content
            content = entry.get("message", {}).get("content") or entry.get("content")
            if content is None:
                continue

            text_parts = []
            if isinstance(content, str):
                text_parts.append(content)
            elif isinstance(content, list):
                for block in content:
                    if isinstance(block, str):
                        text_parts.append(block)
                    elif isinstance(block, dict) and block.get("type") == "text":
                        text_parts.append(block.get("text", ""))

            if text_parts:
                last_assistant_text = "\n".join(text_parts)

    return last_assistant_text


def main():
    # Read hook input from stdin
    try:
        hook_input = json.loads(sys.stdin.read())
    except (json.JSONDecodeError, EOFError):
        sys.exit(0)

    transcript_path = hook_input.get("transcript_path", "")
    if not transcript_path:
        sys.exit(0)

    # Get the last assistant response
    text = get_last_assistant_text(transcript_path)
    if not text.strip():
        sys.exit(0)

    # Speak it using the TTS script
    script_dir = os.path.dirname(os.path.abspath(__file__))
    speak_script = os.path.join(script_dir, "speak.py")

    subprocess.run(
        [sys.executable, speak_script, "--text", text],
        timeout=120,
        capture_output=True,
    )

    # Output success (no blocking)
    print(json.dumps({"continue": True}))
    sys.exit(0)


if __name__ == "__main__":
    main()
