# Web Artifacts Builder Skill

Suite of tools for creating elaborate, multi-component claude.ai HTML artifacts using React, Tailwind CSS, and shadcn/ui.

## What It Does

Enables building complex frontend artifacts that go beyond simple single-file HTML - things that need state management, routing, or shadcn/ui components. The workflow is:

1. **Initialize** a frontend repo using `scripts/init-artifact.sh`
2. **Develop** your artifact by editing the generated code
3. **Bundle** everything into a single HTML file using `scripts/bundle-artifact.sh`
4. **Display** the bundled artifact to the user

## How to Use

### Slash Command
```
/web-artifacts-builder
```

### When to Use
Use this for complex artifacts that need:
- Multiple React components with state management
- shadcn/ui components (buttons, dialogs, cards, etc.)
- Tailwind CSS styling
- Client-side routing

For simple single-file HTML/JSX, you don't need this skill.

## Files

| File | Purpose |
|---|---|
| `SKILL.md` | Instructions for the init, develop, bundle workflow |
| `scripts/init-artifact.sh` | Initializes a new artifact project with React + Tailwind + shadcn/ui |
| `scripts/bundle-artifact.sh` | Bundles the project into a single HTML file |
| `scripts/shadcn-components.tar.gz` | Pre-packaged shadcn/ui components |
| `LICENSE.txt` | License terms |

## Plugin Relationship

Originally from [anthropics/skills](https://github.com/anthropics/skills). This repo maintains a copy so it's included in the skill installation process. Install the plugin via:
```
/plugin marketplace add anthropics/skills
/plugin install web-artifacts-builder from anthropic-agent-skills
```
The `install-skills.py` script also copies this skill to `~/.claude/skills/` for availability even without the plugin.

## Installation

Installed automatically by `install-skills.py`. Copies to `~/.claude/skills/web-artifacts-builder/`.
