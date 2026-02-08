# AI Engineer Startup Toolkit

by **GavinHolder**

A complete Claude Code development environment with enhanced skills, plugin configurations, and workflow documentation for building production-grade web applications.

## What's Included

- **Enhanced Skills** (`skills/`) - Custom and improved Claude Code skill files that replace defaults
- **Plugin Documentation** (`plugins.md`) - Full list of installed plugins with install commands
- **Install Script** (`install-skills.py`) - Copies enhanced skills into your Claude Code environment
- **Reference Docs** - Bootstrap 5.3.8 reference, animation library guide

## Prerequisites

- [Claude Code](https://claude.ai/code) (CLI) installed and authenticated
- Python 3.10+
- Git
- [GitHub CLI](https://cli.github.com/) (`gh`) installed and authenticated

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

### 3. Apply enhanced skills

After plugins are installed (which creates default skill files), run the install script to overwrite with the enhanced versions from this repo:

```bash
python install-skills.py
```

This copies only the files in `skills/` to `~/.claude/skills/`, overwriting defaults where they exist and leaving all other installed skills untouched.

## Enhanced Skills

| Skill | What It Does |
|---|---|
| `bootstrap-5` | Comprehensive Bootstrap 5.3.8 reference covering all components, utilities, grid, color modes, CSS variables, forms, accessibility, data attributes, and rules for creative Bootstrap work. Replaces the default plugin version. |
| `frontend-aesthetics` | Aesthetics system for distinctive UI: typography rules, color theory, background techniques, animation library reference (GSAP, Motion, Anime.js, AOS, Lottie, Three.js, tsParticles, Typed.js, Swiper, Lenis, Splitting.js, AutoAnimate), and anti-slop checklist. Custom skill, no default exists. |
| `claude-bootstrap-base` | Universal coding patterns from alinaqi/claude-bootstrap: simplicity rules (20-line functions, 200-line files), TDD workflow, atomic todos, session management, credentials handling. |
| `claude-bootstrap-react-web` | React web development patterns: test-first development, hooks, React Query, Zustand, CSS Modules, Playwright E2E, component architecture. |
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
/web-design-guidelines     Accessibility and UX audit
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
├── skills/                          # Enhanced/custom Claude Code skills
│   ├── bootstrap-5/SKILL.md         # Bootstrap 5.3.8 reference (replaces default)
│   ├── frontend-aesthetics/SKILL.md # Aesthetics + animation library guide
│   ├── claude-bootstrap-base/SKILL.md
│   ├── claude-bootstrap-react-web/SKILL.md
│   └── web-artifacts-builder/       # Includes scripts/ and LICENSE.txt
├── install-skills.py                # Copies skills to ~/.claude/skills/
├── plugins.md                       # Full plugin list with install commands
├── startup.md                       # Original startup vision document
├── bootstrap-5.3-reference.md       # Standalone Bootstrap reference
├── animation-libraries-reference.md # Standalone animation library guide
├── .gitignore
└── README.md
```
