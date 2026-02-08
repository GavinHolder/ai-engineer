# AI Engineer - Project Configuration

## Voice / TTS System (JARVIS)

This project has a text-to-speech system that makes Claude responses audible using a British neural voice (en-GB-RyanNeural), similar to JARVIS from Iron Man.

### How It Works
- A **Stop hook** in `.claude/settings.local.json` fires after every Claude response
- The hook runs `skills/jarvis-voice/speak_response.py` which reads the conversation transcript
- It extracts the last assistant message, strips markdown, and speaks it via `skills/jarvis-voice/speak.py`
- Audio is generated using `edge-tts` (Microsoft neural voices) and played via PowerShell MediaPlayer

### Files
- `skills/jarvis-voice/speak.py` - Main TTS engine (voice: en-GB-RyanNeural, slightly deeper pitch, faster rate)
- `skills/jarvis-voice/speak_response.py` - Stop hook handler that extracts and speaks responses
- `.claude/settings.local.json` - Hook configuration

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
The `install-skills.py` script copies `skills/jarvis-voice/` to `~/.claude/skills/jarvis-voice/` for global availability. The Stop hook in `.claude/settings.local.json` must be added to each project that wants auto-speak.
