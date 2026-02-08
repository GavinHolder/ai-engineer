# AI Engineer - Project Configuration

## Voice / TTS System (JARVIS) - Conversational Mode

This project has a text-to-speech system using a British neural voice (en-GB-RyanNeural), inspired by JARVIS from Iron Man. The voice operates in **conversational mode** - Claude speaks naturally at key moments throughout the interaction, rather than reading back entire responses.

### How to Speak

Call `speak.py` via Bash with `run_in_background: true` so speech doesn't block your work:

```bash
python skills/jarvis-voice/speak.py --text "Message here"
```

Keep messages short and conversational (under 200 chars ideally). Use natural JARVIS-like phrasing.

### When to Speak

Speak at natural conversational moments - like a human assistant would:

- **Acknowledging a new task**: "Let me look into that", "Good catch, let me check", "Right away sir"
- **Starting work**: "On it", "Let's see what we can do", "I'll get right on that"
- **Asking the user a question**: Speak the question aloud so they hear it
- **Reporting key findings**: "Found the issue", "Interesting, here's what I see"
- **Finishing a task**: "All done sir", "That should do it", "Done and dusted"
- **Reacting naturally**: "That's a good idea", "Right, makes sense", "Ah, I see the problem"

### When NOT to Speak

Do NOT speak for technical/noisy output:

- Tool or command outputs
- Code blocks or file contents
- Every single file read, search, or edit operation
- Intermediate technical steps
- Long explanations (keep spoken text to 1-2 sentences max)

### Mute Check

Before speaking, the mute toggle must be respected. The `speak.py` script checks for `~/.claude/jarvis-muted` internally - if the file exists, it silently exits. No extra check needed from Claude.

### Files
- `skills/jarvis-voice/speak.py` - Main TTS engine (voice: en-GB-RyanNeural, slightly deeper pitch, faster rate)
- `skills/jarvis-voice/speak_response.py` - Legacy Stop hook handler (no longer used in conversational mode)
- `skills/jarvis-voice/jarvis-toggle.py` - Enable/disable voice
- `.claude/settings.local.json` - Permissions config

### Manual Usage
```bash
# Speak text directly
python skills/jarvis-voice/speak.py --text "Hello sir"

# Pipe text
echo "Hello sir" | python skills/jarvis-voice/speak.py

# Adjust voice
python skills/jarvis-voice/speak.py --text "Hello" --rate "+15%" --pitch "-10Hz"
```

### Dependencies
- `edge-tts` (pip install edge-tts) - Neural TTS engine
- PowerShell with PresentationCore assembly (built into Windows)

### Voice Settings (in speak.py)
- Voice: `en-GB-RyanNeural` (British male, JARVIS-like)
- Rate: `+5%` (slightly fast)
- Pitch: `-5Hz` (slightly deeper)
- Max chars: 2000 (truncates long responses gracefully)

### Installation
The `install-skills.py` script copies `skills/jarvis-voice/` to `~/.claude/skills/jarvis-voice/` for global availability.
