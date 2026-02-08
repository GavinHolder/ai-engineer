# Claude Bootstrap React Web Skill

React web development patterns with hooks, React Query, Zustand, and test-first methodology.

## What It Does

Provides Claude with opinionated React development patterns:

- **Test-first development**: Tests must be written before implementation (mandatory)
- **React hooks**: Correct patterns for useState, useEffect, custom hooks
- **React Query**: Data fetching, caching, and server state management
- **Zustand**: Lightweight client state management
- **CSS Modules**: Scoped styling approach
- **Playwright E2E**: End-to-end testing patterns
- **Component architecture**: File structure, naming, prop patterns

## How to Use

### Automatic
Claude activates this skill when you're working on React projects:
```
"Build a React component for user profiles"
"Add React Query data fetching to the dashboard"
"Create a Zustand store for cart state"
```

### Prerequisites
Requires the base skill (`claude-bootstrap-base`) to be installed alongside it.

## Plugin Relationship

Originally from [alinaqi/claude-bootstrap](https://github.com/alinaqi/claude-bootstrap). This repo maintains an enhanced copy. The `install-skills.py` script overwrites the default plugin version with this enhanced one, so any improvements made here take effect globally.

## Files

| File | Purpose |
|---|---|
| `SKILL.md` | React patterns: hooks, React Query, Zustand, CSS Modules, Playwright, component architecture |

## Installation

Installed automatically by `install-skills.py`. Copies to `~/.claude/skills/claude-bootstrap-react-web/`.
