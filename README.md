# AI Engineer Startup Toolkit

by **GavinHolder**

A complete Claude Code development environment with enhanced skills, plugin configurations, JARVIS voice system, and workflow documentation for building production-grade web applications.

## What's Included

- **Enhanced Skills** (`skills/`) - Custom and improved Claude Code skill files that replace defaults
- **JARVIS Voice System** (`skills/jarvis-voice/`) - Text-to-speech that reads Claude responses aloud using a British neural voice (JARVIS-style)
- **Plugin Documentation** (`plugins.md`) - Full list of installed plugins with install commands and usage guide
- **Install Script** (`install-skills.py`) - Installs skills, fixes Windows hooks, generates project CLAUDE.md
- **Version Scout** (`update-django-skill.py`) - Auto-updates Django/Python skill with latest package versions from PyPI
- **Project Config** (`CLAUDE.md`) - Project-level instructions that Claude Code loads automatically
- **Reference Docs** - Bootstrap 5.3.8 reference, animation library guide

## Prerequisites

### 1. Claude Code CLI

Install and authenticate the Claude Code CLI:

```bash
npm install -g @anthropic-ai/claude-code
claude login
```

Verify: `claude --version` should return a version number.

### 2. Python 3.10+

Download from [python.org](https://www.python.org/downloads/) or install via a package manager:

```bash
# Windows (winget)
winget install Python.Python.3.12

# macOS (Homebrew)
brew install python@3.12
```

Verify: `python --version` should return 3.10 or higher.

### 3. Git

Download from [git-scm.com](https://git-scm.com/downloads) or install via a package manager:

```bash
# Windows (winget)
winget install Git.Git

# macOS (Homebrew)
brew install git
```

Verify: `git --version`

### 4. GitHub CLI (`gh`)

Download from [cli.github.com](https://cli.github.com/) or install via a package manager:

```bash
# Windows (winget)
winget install GitHub.cli

# macOS (Homebrew)
brew install gh
```

Then authenticate: `gh auth login`

Verify: `gh auth status` should show you're logged in.

### 5. edge-tts (for JARVIS voice)

```bash
pip install edge-tts
```

Verify: `python -m edge_tts --list-voices` should list available voices.

### 6. PowerShell (Windows only)

Built into Windows - no installation needed. Used for audio playback via the PresentationCore assembly.

## Quick Start

### 1. Clone the repo

```bash
git clone https://github.com/GavinHolder/ai-engineer.git
cd ai-engineer
```

### 2. Install plugins

Install each plugin into Claude Code. Run these inside any Claude Code session:

**From `anthropics/claude-plugins-official`:**
```
/plugin install frontend-design from anthropics/claude-plugins-official
/plugin install feature-dev from anthropics/claude-plugins-official
/plugin install typescript-lsp from anthropics/claude-plugins-official
/plugin install security-guidance from anthropics/claude-plugins-official
/plugin install pyright-lsp from anthropics/claude-plugins-official
/plugin install claude-md-management from anthropics/claude-plugins-official
/plugin install hookify from anthropics/claude-plugins-official
/plugin install claude-code-setup from anthropics/claude-plugins-official
/plugin install playground from anthropics/claude-plugins-official
```

**From `affaan-m/everything-claude-code`:**
```
/plugin install superpowers from affaan-m/everything-claude-code
```

**From `anthropics/skills` (manual):**
```
/plugin marketplace add anthropics/skills
/plugin install web-artifacts-builder from anthropic-agent-skills
```

**From `alinaqi/claude-bootstrap` (manual):**
```bash
git clone https://github.com/alinaqi/claude-bootstrap ~/.claude-bootstrap
cd ~/.claude-bootstrap && ./install.sh
```

### 3. Run the setup script

After plugins are installed, run the setup script:

```bash
python install-skills.py
```

The script does 3 things:
1. **Installs enhanced skills** - Copies `skills/` to `~/.claude/skills/`, overwriting defaults
2. **Fixes Windows hooks** - Patches `python3` -> `python` in all plugin hook files (Windows only)
3. **Generates CLAUDE.md** - Creates project session guide + memory files (when run from a project directory)

To initialize a new project with CLAUDE.md and the full session management framework:

```bash
# Option A: Run from the project directory
cd <your-project>
python path/to/ai-engineer/install-skills.py

# Option B: Use --init flag
python install-skills.py --init <project-path>
```

This generates:
- `CLAUDE.md` - Session guide with adversarial verification, TDD workflow, risk classification
- `.claude/memory/SESSION_CONTEXT.md` - Active state tracking
- `.claude/memory/SESSION_CHANGELOG.md` - Timestamped session history
- `.claude/memory/TASK_PROTOCOL.md` - Hierarchical task management (5 levels, checkpoints)
- `.claude/memory/LEARNED_PATTERNS.md` - Continuous learning log

### 4. Keep Django/Python skill up to date

The Django/Python skill tracks package versions. To check for updates:

```bash
python update-django-skill.py           # Interactive: choose what to update
python update-django-skill.py --check   # Check only, no changes
python update-django-skill.py --auto    # Auto-update all to latest
```

The script:
- Checks PyPI for latest versions of all tracked packages
- Compares against `skills/django-python/versions.json`
- Prompts you to choose which to update
- Scrapes official Django/Python docs for release notes and changes
- Updates `SKILL.md` version table and appends release notes

## JARVIS Voice System

Text-to-speech that gives Claude a voice using a British neural voice (`en-GB-RyanNeural`), inspired by JARVIS from Iron Man. Operates in **conversational mode** - Claude speaks naturally at key moments (acknowledging tasks, reporting findings, asking questions) rather than reading back entire responses.

```bash
python skills/jarvis-voice/jarvis-toggle.py          # Toggle on/off
python skills/jarvis-voice/jarvis-toggle.py off      # Mute (great for demos/public places)
python skills/jarvis-voice/jarvis-toggle.py on       # Re-enable
python skills/jarvis-voice/jarvis-toggle.py status   # Check current state
```

See **[skills/jarvis-voice/voice.md](skills/jarvis-voice/voice.md)** for full documentation: voice settings, CLI arguments, hook configuration, available voices, and manual usage.

## Enhanced Skills

| Skill | What It Does |
|---|---|
| `bootstrap-5` | Comprehensive Bootstrap 5.3.8 reference covering all components, utilities, grid, color modes, CSS variables, forms, accessibility, data attributes, and rules for creative Bootstrap work. Replaces the default plugin version. |
| `frontend-aesthetics` | Aesthetics system for distinctive UI: typography rules, color theory, background techniques, animation library reference (GSAP, Motion, Anime.js, AOS, Lottie, Three.js, tsParticles, Typed.js, Swiper, Lenis, Splitting.js, AutoAnimate), and anti-slop checklist. Custom skill, no default exists. |
| `claude-bootstrap-base` | Universal coding patterns from alinaqi/claude-bootstrap: simplicity rules (20-line functions, 200-line files), TDD workflow, atomic todos, session management, credentials handling. |
| `claude-bootstrap-react-web` | React web development patterns: test-first development, hooks, React Query, Zustand, CSS Modules, Playwright E2E, component architecture. |
| `django-python` | Comprehensive Django & Python reference: project structure, models, views, DRF, Celery, HTMX SPA, testing, security, Docker deployment, service layer architecture. Auto-updated with latest package versions. |
| `jarvis-voice` | JARVIS-style TTS engine using Microsoft Edge neural voices. Claude speaks conversationally at natural moments - acknowledging tasks, reporting findings, asking questions aloud. |
| `web-artifacts-builder` | From anthropics/skills: build complex React + Tailwind + shadcn/ui artifacts as single bundled HTML files. Includes init and bundle scripts. |

## Plugin Commands Quick Reference

```
/frontend-design           Build creative, distinctive UI
/frontend-aesthetics       Apply aesthetics system (typography, color, animation)
/bootstrap-5               Bootstrap 5.3.8 component reference
/feature-dev               Guided feature development
/brainstorming             Explore requirements before building
/writing-plans             Plan multi-step implementations
/test-driven-development   TDD workflow
/systematic-debugging      Debug methodically
/verification-before-completion  Verify before claiming done
/requesting-code-review    Review code before merging
/playground                Create interactive HTML explorers
/web-artifacts-builder     Build React+shadcn artifacts
/Django Framework          Django web applications
/hookify                   Create enforcement hooks
/revise-claude-md          Update CLAUDE.md with learnings
/claude-md-improver        Audit and improve CLAUDE.md files
/claude-automation-recommender  Get Claude Code setup recommendations
/web-design-guidelines     Accessibility and UX audit
/keybindings-help          Customize keyboard shortcuts
```

## Development Workflow

1. **Plan first** - Always use plan mode (Opus model) to architect the project
2. **Use /brainstorming** before any creative or feature work
3. **Use /writing-plans** for multi-step implementations
4. **Use /test-driven-development** for any feature with testable logic
5. **Use /verification-before-completion** before claiming work is done
6. **Use /revise-claude-md** at end of sessions to capture learnings

## Deployment Architecture

All deployments follow a Docker + Portainer + Traefik stack approach:

- **Portainer** - Own stack, manages all containers via UI
- **Traefik** - Own stack, reverse proxy and SSL termination
- **Applications** - Each app is its own stack, manually built via Portainer (never auto-build)
- Docker Compose files use `image: build` structure with local VM-mounted volumes
- Apps managed post-deployment via WebAppManager (`K:\2025\WebAppManager`)

## Project Structure

```
ai-engineer/
├── .claude/
│   └── settings.local.json          # Permissions config
├── skills/                          # Enhanced/custom Claude Code skills
│   ├── bootstrap-5/SKILL.md         # Bootstrap 5.3.8 reference (replaces default)
│   ├── frontend-aesthetics/SKILL.md # Aesthetics + animation library guide
│   ├── claude-bootstrap-base/SKILL.md
│   ├── claude-bootstrap-react-web/SKILL.md
│   ├── django-python/               # Django+Python reference + versions.json
│   ├── jarvis-voice/                # JARVIS TTS system
│   │   ├── speak.py                 # Main TTS engine (edge-tts + PowerShell)
│   │   ├── speak_response.py       # Stop hook handler
│   │   ├── jarvis-toggle.py        # Enable/disable JARVIS voice
│   │   └── voice.md                # Full voice system documentation
│   └── web-artifacts-builder/       # Includes scripts/ and LICENSE.txt
├── install-skills.py                # Skills install + hook fix + CLAUDE.md generation
├── update-django-skill.py           # Version scout: checks PyPI, scrapes official docs
├── plugins.md                       # Full plugin list with install commands + usage guide
├── CLAUDE.md                        # Project config (auto-loaded by Claude Code)
├── startup.md                       # Original startup vision document
├── bootstrap-5.3-reference.md       # Standalone Bootstrap reference
├── animation-libraries-reference.md # Standalone animation library guide
├── .gitignore
└── README.md
```

# Agents
Use --agent <agent_name> to directly start a conversation with a subagent 