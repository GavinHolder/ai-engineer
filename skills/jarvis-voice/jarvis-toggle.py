#!/usr/bin/env python3
"""
Toggle JARVIS voice on or off.

Usage:
    python jarvis-toggle.py          # Toggle current state
    python jarvis-toggle.py on       # Enable voice
    python jarvis-toggle.py off      # Mute voice
    python jarvis-toggle.py status   # Show current state
"""

import os
import sys
from pathlib import Path

MUTE_FILE = Path.home() / ".claude" / "jarvis-muted"


def is_muted() -> bool:
    return MUTE_FILE.exists()


def mute():
    MUTE_FILE.parent.mkdir(parents=True, exist_ok=True)
    MUTE_FILE.touch()
    print("JARVIS voice: MUTED")
    print(f"  (mute file: {MUTE_FILE})")


def unmute():
    if MUTE_FILE.exists():
        MUTE_FILE.unlink()
    print("JARVIS voice: ENABLED")


def status():
    if is_muted():
        print("JARVIS voice: MUTED")
    else:
        print("JARVIS voice: ENABLED")


def main():
    action = sys.argv[1].lower() if len(sys.argv) > 1 else None

    if action == "on":
        unmute()
    elif action == "off":
        mute()
    elif action == "status":
        status()
    elif action is None:
        # Toggle
        if is_muted():
            unmute()
        else:
            mute()
    else:
        print(f"Unknown action: {action}")
        print("Usage: python jarvis-toggle.py [on|off|status]")
        sys.exit(1)


if __name__ == "__main__":
    main()
