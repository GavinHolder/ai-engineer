# Claude Bootstrap Base Skill

Universal coding patterns and constraints that enforce simplicity, TDD workflow, and atomic task management across all projects.

## What It Does

Sets strict coding standards that Claude follows in every session:

- **Simplicity rules**: Functions under 20 lines, files under 200 lines, no premature abstractions
- **TDD workflow**: Tests written before implementation code
- **Atomic todos**: Break work into small, verifiable steps
- **Session management**: Track context, changes, and learnings across sessions
- **Credentials handling**: Safe patterns for secrets and API keys

This is a foundational skill - it applies universally regardless of what framework or language you're using.

## How to Use

This skill activates automatically in every Claude Code session. No slash command needed.

The patterns it enforces are always active:
- Claude will write shorter functions and smaller files
- Claude will suggest writing tests first
- Claude will break complex tasks into atomic steps

## Plugin Relationship

Originally from [alinaqi/claude-bootstrap](https://github.com/alinaqi/claude-bootstrap). This repo maintains an enhanced copy of the skill file. The `install-skills.py` script overwrites the default plugin version with this enhanced one, so any improvements made here take effect globally.

## Files

| File | Purpose |
|---|---|
| `SKILL.md` | Universal coding patterns, simplicity constraints, TDD workflow, atomic todos |

## Installation

Installed automatically by `install-skills.py`. Copies to `~/.claude/skills/claude-bootstrap-base/`.
