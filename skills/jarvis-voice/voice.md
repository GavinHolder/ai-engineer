# JARVIS Voice System

A text-to-speech system that makes Claude Code responses audible using a British neural voice, inspired by JARVIS from Iron Man.

## How It Works

1. A **Stop hook** in `.claude/settings.local.json` fires after every Claude response
2. The hook runs `skills/jarvis-voice/speak_response.py` which reads the conversation transcript
3. It extracts the last assistant message, strips markdown formatting, and speaks it aloud
4. Audio is generated via `edge-tts` (Microsoft neural voices) and played through PowerShell MediaPlayer

## Dependencies

| Package | Install | Purpose |
|---|---|---|
| `edge-tts` | `pip install edge-tts` | Microsoft neural TTS engine |
| PowerShell | Built into Windows | Audio playback via PresentationCore assembly |

## Enable / Disable

Toggle the voice on or off using the toggle script at the repo root:

```bash
python jarvis-toggle.py          # Toggle on/off
python jarvis-toggle.py off      # Mute (great for demos/public places)
python jarvis-toggle.py on       # Re-enable
python jarvis-toggle.py status   # Check current state
```

When muted, a `~/.claude/jarvis-muted` file is created. The Stop hook checks for this file and silently skips TTS when it exists. Delete the file manually to re-enable, or just run `python jarvis-toggle.py on`.

## Voice Settings

Configured as defaults in `skills/jarvis-voice/speak.py`:

| Setting | Default | Description |
|---|---|---|
| Voice | `en-GB-RyanNeural` | British male, JARVIS-like |
| Rate | `+5%` | Slightly faster for snappy delivery |
| Pitch | `-5Hz` | Slightly deeper tone |
| Volume | `+0%` | Default volume |
| Max chars | `2000` | Truncates long responses gracefully at a sentence boundary |

## Manual Usage

Speak text directly without the Stop hook:

```bash
# Speak text directly
python skills/jarvis-voice/speak.py --text "Hello sir"

# Pipe text
echo "Hello sir" | python skills/jarvis-voice/speak.py

# Custom voice settings
python skills/jarvis-voice/speak.py --text "Hello" --rate "+15%" --pitch "-10Hz"

# Skip markdown stripping (for raw text)
python skills/jarvis-voice/speak.py --text "Hello" --raw

# Set a custom character limit
python skills/jarvis-voice/speak.py --text "Long text..." --max-chars 500
```

### All CLI Arguments

| Argument | Short | Default | Description |
|---|---|---|---|
| `--text` | `-t` | stdin | Text to speak |
| `--voice` | `-v` | `en-GB-RyanNeural` | Edge TTS voice name |
| `--rate` | `-r` | `+5%` | Speech rate adjustment |
| `--pitch` | `-p` | `-5Hz` | Pitch adjustment |
| `--volume` | | `+0%` | Volume adjustment |
| `--raw` | | `false` | Don't strip markdown formatting |
| `--max-chars` | | `2000` | Max characters to speak |

## Files

| File | Purpose |
|---|---|
| `speak.py` | Main TTS engine - generates audio with edge-tts and plays via PowerShell |
| `speak_response.py` | Stop hook handler - reads transcript, extracts last response, calls speak.py |
| `jarvis-toggle.py` | Toggle script to enable/disable voice |
| `voice.md` | This documentation file |
| `.claude/settings.local.json` | Hook configuration that triggers the voice system (project root) |

## Hook Configuration

The Stop hook is defined in `.claude/settings.local.json`:

```json
{
  "hooks": {
    "Stop": [
      {
        "hooks": [
          {
            "type": "command",
            "command": "python \"F:\\Projects\\2026\\ai_engineer\\skills\\jarvis-voice\\speak_response.py\"",
            "timeout": 120
          }
        ]
      }
    ]
  }
}
```

To add JARVIS voice to another project, copy this hook config into that project's `.claude/settings.local.json`.

## Installation

The `install-skills.py` script copies `skills/jarvis-voice/` to `~/.claude/skills/jarvis-voice/` for global availability. The Stop hook path in `.claude/settings.local.json` must be updated per-project to point to the correct script location.

## Text Processing

Before speaking, the system:

1. **Strips markdown** - Removes code blocks, inline code, headers, bold/italic, links, images, lists, blockquotes, HTML tags, and file paths
2. **Truncates** - Cuts at sentence boundaries near the 2000-char limit, adding a natural closing phrase
3. **Cleans whitespace** - Collapses multiple newlines and spaces

## Available Voices

To list all available Edge TTS voices:

```bash
python -m edge_tts --list-voices
```

Some alternatives to try:

| Voice | Description |
|---|---|
| `en-GB-RyanNeural` | British male (default) |
| `en-GB-SoniaNeural` | British female |
| `en-US-GuyNeural` | American male |
| `en-US-JennyNeural` | American female |
| `en-AU-WilliamNeural` | Australian male |
