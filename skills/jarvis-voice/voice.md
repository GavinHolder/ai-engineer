# JARVIS Voice System

A text-to-speech system that gives Claude a voice using a British neural voice, inspired by JARVIS from Iron Man.

## How It Works - Conversational Mode

The voice system operates in **conversational mode**: Claude proactively speaks at natural moments during the interaction, like a human assistant would. This replaces the old "narration mode" which read back entire responses at the end.

### What Claude Says Aloud
- Task acknowledgements: "Let me look into that", "Right away sir"
- Key findings: "Found the issue", "Interesting, here's what I see"
- Questions: spoken aloud so the user hears them
- Completions: "All done sir", "Done and dusted"
- Natural reactions: "That's a good idea", "Ah, I see the problem"

### What Claude Does NOT Say Aloud
- Tool/command outputs
- Code blocks or file contents
- Every file read, search, or edit
- Long technical explanations

### How It Works Technically
Claude calls `speak.py` via Bash with `run_in_background: true` at conversational moments. Messages are kept short (under 200 chars) and use natural JARVIS-like phrasing. The instructions live in `CLAUDE.md` so Claude knows when and how to speak.

### Old Mode: Narration (Deprecated)
Previously, a **Stop hook** fired after every Claude response, extracted the full response text via `speak_response.py`, stripped markdown, and read it all aloud. This was removed because:
- It read everything including technical details the user didn't need to hear
- It only spoke once at the end, making it feel robotic
- It couldn't react naturally during the conversation

The `speak_response.py` file is retained for reference but is no longer hooked up.

## Dependencies

| Package | Install | Purpose |
|---|---|---|
| `edge-tts` | `pip install edge-tts` | Microsoft neural TTS engine |
| PowerShell | Built into Windows | Audio playback via PresentationCore assembly |

## Enable / Disable

Toggle the voice on or off using the toggle script:

```bash
python skills/jarvis-voice/jarvis-toggle.py          # Toggle on/off
python skills/jarvis-voice/jarvis-toggle.py off      # Mute (great for demos/public places)
python skills/jarvis-voice/jarvis-toggle.py on       # Re-enable
python skills/jarvis-voice/jarvis-toggle.py status   # Check current state
```

When muted, a `~/.claude/jarvis-muted` file is created. The `speak.py` script checks for this file and silently skips TTS when it exists. Delete the file manually to re-enable, or just run `python jarvis-toggle.py on`.

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

Speak text directly without Claude's conversational triggers:

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
| `speak_response.py` | Legacy Stop hook handler (retained for reference, no longer active) |
| `jarvis-toggle.py` | Toggle script to enable/disable voice |
| `voice.md` | This documentation file |

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
