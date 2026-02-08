#!/usr/bin/env python3
"""
Install enhanced/custom Claude Code skills from this repo into ~/.claude/skills/.

Only overwrites files that exist in this repo's skills/ folder.
Does NOT touch other installed skills.

Usage:
    python install-skills.py
"""

import os
import shutil
from pathlib import Path


def main():
    repo_skills = Path(__file__).parent / "skills"
    target_skills = Path.home() / ".claude" / "skills"

    if not repo_skills.exists():
        print("ERROR: No skills/ folder found in repo.")
        return

    if not target_skills.exists():
        target_skills.mkdir(parents=True, exist_ok=True)
        print(f"Created {target_skills}")

    copied = 0
    skipped = 0

    for skill_dir in sorted(repo_skills.iterdir()):
        if not skill_dir.is_dir():
            continue

        skill_name = skill_dir.name
        target_dir = target_skills / skill_name

        if not target_dir.exists():
            target_dir.mkdir(parents=True, exist_ok=True)

        for root, dirs, files in os.walk(skill_dir):
            rel_root = Path(root).relative_to(skill_dir)
            target_root = target_dir / rel_root

            if not target_root.exists():
                target_root.mkdir(parents=True, exist_ok=True)

            for file in files:
                src = Path(root) / file
                dst = target_root / file
                existed = dst.exists()

                shutil.copy2(src, dst)
                action = "OVERWRITTEN" if existed else "INSTALLED"
                print(f"  [{action}] {skill_name}/{rel_root / file}")
                copied += 1

    print(f"\nDone! {copied} file(s) copied, {skipped} skipped.")
    print(f"Skills installed to: {target_skills}")


if __name__ == "__main__":
    main()
