# Bootstrap 5 Skill

A comprehensive Bootstrap 5.3.8 reference that Claude Code loads automatically when you work on Bootstrap-based projects.

## What It Does

Provides Claude with complete knowledge of Bootstrap 5.3.8: all components, utilities, grid system, color modes, CSS variables, forms, helpers, accessibility patterns, and data attributes. This replaces the default plugin version with a more thorough reference.

When this skill is active, Claude will:
- Use correct Bootstrap 5.3.8 class names and patterns
- Follow accessibility best practices (`aria-*` attributes, semantic HTML)
- Apply responsive grid layouts properly
- Use Bootstrap's color mode system for dark/light themes
- Reference the correct CDN links and versions

## Plugin Relationship

This is a **custom skill** - there is no default Bootstrap plugin in Claude Code. This was manually created as a comprehensive reference so Claude has full knowledge of Bootstrap 5.3.8 without needing to search documentation.

## How to Use

### Automatic (recommended)
Just describe what you want to build. Claude will use the skill automatically when it detects Bootstrap work:
```
"Build me a responsive dashboard with Bootstrap"
"Add a Bootstrap modal with a form"
"Create a navbar with dropdowns"
```

### Slash Command
Explicitly invoke the skill:
```
/bootstrap-5
```

## Files

| File | Purpose |
|---|---|
| `SKILL.md` | Full Bootstrap 5.3.8 reference (components, utilities, grid, forms, accessibility, CDN links) |

## Installation

Installed automatically by `install-skills.py`. Copies to `~/.claude/skills/bootstrap-5/`.
