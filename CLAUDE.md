# AI Engineer - Project Configuration

## Voice - VoiceMode Plugin

This project uses the **VoiceMode** plugin (`mbailey/voicemode`) for voice interaction. It provides speech-to-text and text-to-speech directly in Claude Code, with options for local services or remote connection via phone/web app.

### Usage
- `/voicemode` — Voice interaction entry point
- `/converse` — Start an ongoing voice conversation
- `/voicemode-connect` — Remote voice via phone or web app (no local STT/TTS setup needed)
- `/voicemode-dj` — Background music control for voice sessions
- `/install` (voicemode) — Install VoiceMode, FFmpeg, and local voice services
- `/status` (voicemode) — Check service status

### Installation
Installed automatically by `scripts/install-skills.py` as a plugin from `mbailey/voicemode`.

## Design - Efecto MCP Server

This project includes the **Efecto** MCP server (`@efectoapp/mcp`) for visual design directly from Claude Code. Create artboards, build layouts with JSX + Tailwind, and export designs.

### Usage
Ask Claude to "Design a landing page in Efecto" or any design-related prompt.

### Installation
Installed automatically by `scripts/install-skills.py` via `npx @efectoapp/mcp install`.

Docs: [efecto.app/docs](https://efecto.app/docs)
