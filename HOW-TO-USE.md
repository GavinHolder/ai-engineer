# AI Engineer Toolkit - How to Use Guide

A comprehensive skills system for Claude Code that gives it deep knowledge of modern web technologies, design patterns, and development workflows. Each skill is a markdown reference that Claude loads automatically when relevant to your project.

---

## Table of Contents

1. [Quick Start](#quick-start)
2. [Installation](#installation)
3. [Skills Overview](#skills-overview)
4. [Skill Details](#skill-details)
5. [Framework Detection](#framework-detection)
6. [Project Initialization](#project-initialization)
7. [JARVIS Voice System](#jarvis-voice-system)
8. [Workflow Examples](#workflow-examples)
9. [Tips & Best Practices](#tips--best-practices)

---

## Quick Start

```bash
# Clone the repo
git clone <repo-url> ai_engineer
cd ai_engineer

# Install all skills to ~/.claude/skills/
python install-skills.py

# Initialize a specific project with CLAUDE.md + memory files
python install-skills.py --init /path/to/your/project

# Just detect what frameworks a project uses
python install-skills.py --detect /path/to/your/project
```

After installation, Claude Code automatically picks up the skills when you work in any project. No manual activation needed.

---

## Installation

### What `install-skills.py` Does

0. **Checks Claude CLI** - verifies `claude` is installed, installs via npm if missing
1. **Copies skills** from `skills/` to `~/.claude/skills/` (global availability)
2. **Installs all plugins** automatically via `claude plugin install` (Playwright, frontend-design, feature-dev, superpowers, etc.)
3. **Mutes JARVIS voice** by default (enable with `python skills/jarvis-voice/jarvis-toggle.py`)
4. **Fixes Windows hooks** - replaces `python3` with `python` in plugin hook files
5. **Generates CLAUDE.md** (if `--init` is used) with session management, task protocols, and memory files
6. **Detects frameworks** in your project and tells you which skills are relevant

### Running the Installer

```bash
# From the ai_engineer repo directory:
python install-skills.py

# Output:
#   PRE-FLIGHT: Checking Claude CLI
#   Claude CLI found: 2.x.x
#
#   STEP 1: Installing Enhanced Skills
#   [INSTALLED] bootstrap-5/SKILL.md
#   [INSTALLED] react-19/SKILL.md
#   [INSTALLED] visual-debugging/SKILL.md
#   ... etc
#
#   STEP 1b: Installing Claude Code Plugins
#   [INSTALLED] frontend-design from anthropics/claude-plugins-official
#   [INSTALLED] playwright from anthropics/claude-plugins-official
#   [INSTALLED] superpowers from affaan-m/everything-claude-code
#   ... etc
#
#   [MUTED] JARVIS voice disabled by default.
#
#   STEP 2: Fixing Windows Hook Compatibility
#   No python3 references found - all hooks OK.
#
#   STEP 3: Framework Detection
#   Setup Complete!
```

### Initializing a Project

```bash
# From inside your project:
python /path/to/ai_engineer/install-skills.py

# Or pass the project path:
python install-skills.py --init /path/to/my-django-app
```

This creates:
- `CLAUDE.md` - Session guide with task protocols and verification rules
- `.claude/memory/SESSION_CONTEXT.md` - Active task state
- `.claude/memory/SESSION_CHANGELOG.md` - Session history log
- `.claude/memory/TASK_PROTOCOL.md` - Hierarchical task management
- `.claude/memory/LEARNED_PATTERNS.md` - Continuous learning log

If a `CLAUDE.md` already exists, the AI Engineer content is **appended** (not overwritten), marked with an HTML comment so it can be identified and won't duplicate on re-runs.

---

## Skills Overview

| Skill | What It Does | When Claude Uses It |
|-------|-------------|---------------------|
| **react-19** | Complete React 19 API reference - all hooks, Server Components, Actions | Any React development |
| **html5** | All HTML5 elements, attributes, forms, media, ARIA, meta tags | Any HTML work |
| **css3** | Modern CSS - Flexbox, Grid, :has(), nesting, container queries, scroll animations | Any CSS work |
| **javascript-es2025** | ES2024/2025 syntax, all built-in methods, async patterns, modules | Any JavaScript work |
| **bootstrap-5** | Bootstrap 5.3.8 complete reference - components, utilities, grid, forms | Bootstrap projects |
| **django-python** | Django models, views, DRF, Celery, HTMX, testing, Docker deployment | Django/Python projects |
| **frontend-aesthetics** | Typography, color, animation libraries (GSAP, anime.js, Three.js, etc.) | All frontend code generation |
| **claude-bootstrap-base** | TDD workflow, simplicity rules, code quality constraints | All coding tasks |
| **claude-bootstrap-react-web** | React patterns with hooks, React Query, Zustand | React web apps |
| **web-artifacts-builder** | Complex React+Tailwind+shadcn artifacts for claude.ai | Building claude.ai artifacts |
| **jarvis-voice** | JARVIS-style text-to-speech (British neural voice) | Voice-enabled sessions |
| **modern-ui-ux** | UI/UX design, scroll storytelling, 3D, animation, Apple-style design | Creative web design |
| **visual-debugging** | Visual debugging and design discovery via Playwright browser automation | UI bugs, responsive testing, reference site inspection |

---

## Skill Details

### react-19 - React 19 Complete Reference

**~680 lines** of comprehensive React 19 coverage.

**What's included:**
- All hooks: useState, useEffect, useContext, useReducer, useRef, useMemo, useCallback, useTransition, useDeferredValue, useId, useSyncExternalStore, useInsertionEffect
- React 19 new APIs: `use()`, `useActionState`, `useOptimistic`, `useFormStatus`
- Server Components and Client Components
- Server Actions and form handling
- Suspense, Error Boundaries, Portals
- Custom hook patterns with full code examples
- Data fetching patterns, performance optimization

**Example - Claude automatically knows React 19 patterns:**
```
You: "Add a form that submits to a server action with optimistic updates"
Claude: Uses useActionState + useOptimistic (React 19 APIs) correctly
```

---

### html5 - HTML5 Complete Reference

**~470 lines** of modern HTML5 coverage.

**What's included:**
- All semantic elements (header, nav, main, article, section, aside, footer, etc.)
- Complete document structure and meta tags (SEO, Open Graph, Twitter Cards, PWA)
- All form input types and attributes with validation patterns
- Responsive images (srcset, sizes, picture element)
- Interactive elements: dialog, popover API, details/summary
- Full ARIA reference for accessibility
- Script loading strategies (async, defer, module)
- Structured data (JSON-LD)

**Example:**
```
You: "Create a contact form with proper validation and accessibility"
Claude: Uses correct input types, autocomplete values, aria attributes, validation patterns
```

---

### css3 - Modern CSS Complete Reference

**~580 lines** of cutting-edge CSS coverage.

**What's included:**
- All selectors including :has(), :is(), :where(), nesting syntax
- Complete Flexbox and Grid reference (including subgrid)
- Container queries with @container
- Custom properties and modern color functions (oklch, color-mix)
- Scroll-driven animations and view transitions API
- Cascade layers (@layer)
- Anchor positioning
- Logical properties (inline/block instead of left/right)
- Media queries with modern range syntax
- @starting-style for entry animations

**Example:**
```
You: "Style this component to respond to its container size, not the viewport"
Claude: Uses @container queries correctly instead of @media queries
```

---

### javascript-es2025 - Modern JavaScript Complete Reference

**~530 lines** of ES2024/2025 JavaScript coverage.

**What's included:**
- All Array methods (at, findLast, toSorted, toReversed, toSpliced, with, group)
- All Object methods (Object.groupBy, fromEntries, hasOwn)
- All String methods (replaceAll, at, isWellFormed)
- ES2024/2025 features: Set operations (union, intersection, difference), iterator helpers, Promise.withResolvers, Temporal API
- Classes with private fields, static blocks
- Async patterns: Promise.allSettled, Promise.any, async generators
- Modules: import/export, dynamic import, import.meta
- Proxy, Reflect, WeakRef, FinalizationRegistry
- Web APIs: Fetch, DOM, Storage, Structured Clone

**Example:**
```
You: "Group these items by category"
Claude: Uses Object.groupBy() (ES2024) instead of manual reduce
```

---

### bootstrap-5 - Bootstrap 5.3.8 Complete Reference

**~1100+ lines** of comprehensive Bootstrap coverage.

**What's included:**
- Complete grid system (containers, rows, columns, breakpoints)
- All components with code examples (accordion, alerts, buttons, cards, carousel, dropdowns, modals, navbar, offcanvas, toast, etc.)
- All utility classes (spacing, colors, display, flex, position, sizing, text)
- Color modes (light/dark theme switching)
- CSS variables customization
- Complete forms reference (inputs, selects, checks, ranges, validation)
- Helpers (clearfix, color/background, position, stacks, visually-hidden)

**Example:**
```
You: "Build a responsive dashboard with a sidebar nav and cards"
Claude: Uses Bootstrap grid, navbar, cards, utilities correctly with proper breakpoints
```

---

### django-python - Django & Python Complete Reference

**~1105 lines** of production Django coverage.

**What's included:**
- Project structure and settings configuration
- Models, fields, querysets, managers, signals
- Class-based and function-based views
- URL routing patterns
- Django REST Framework (serializers, viewsets, permissions, pagination)
- Celery task queues
- HTMX SPA patterns (no-refresh UI)
- Forms and validation
- Template system
- Authentication and permissions
- Testing (pytest, factories, fixtures)
- Security best practices
- Docker deployment with Gunicorn/Nginx

**Example:**
```
You: "Create a REST API for a blog with pagination and authentication"
Claude: Uses DRF viewsets, serializers, token auth, PageNumberPagination correctly
```

---

### frontend-aesthetics - Design & Animation System

**~520 lines** covering design philosophy and animation libraries.

**What's included:**
- Pre-code design thinking (purpose, tone, differentiation)
- Typography rules with font recommendations by aesthetic
- Color and theme system (avoid AI slop patterns)
- Complete animation library reference:
  - **GSAP** - Timeline, ScrollTrigger, SplitText, easing
  - **Motion** (Framer Motion) - React animation, layout, scroll
  - **Anime.js** - Lightweight general animation
  - **AOS** - Zero-JS scroll reveals
  - **Lottie** - Vector/icon animations
  - **Three.js** - 3D effects
  - **tsParticles** - Particle backgrounds
  - **Typed.js** - Typewriter effects
  - **Swiper** - Creative carousels
  - **Lenis** - Smooth scrolling
  - **Splitting.js** - Text split animation
  - **AutoAnimate** - Zero-config list animations
- Background techniques (gradients, noise, patterns)
- Layout composition rules
- Anti-patterns checklist

**Example:**
```
You: "Build a landing page with scroll-triggered animations"
Claude: Uses GSAP ScrollTrigger with staggered reveals, Lenis smooth scroll, distinctive typography
```

---

### claude-bootstrap-base - Code Quality & TDD

Universal coding constraints that apply to all projects:

- **Simplicity rules**: Max 20 lines/function, 200 lines/file, 3 params/function
- **TDD workflow**: Red-Green-Refactor cycle, tests before code
- **Atomic todos**: Granular task tracking
- **Error handling**: No silent failures
- **No dead code**: Delete it, git remembers

---

### claude-bootstrap-react-web - React Development Patterns

React-specific development patterns:

- Test-first development workflow for components
- Hook patterns (React Query, Zustand state management)
- Component architecture
- Performance patterns
- Error boundary strategies

---

### web-artifacts-builder - Claude.ai Artifacts

For building complex interactive artifacts in claude.ai:

- React 18 + TypeScript + Vite + Tailwind + shadcn/ui
- Project initialization scripts
- Bundle into single HTML file
- State management and routing in artifacts

---

### jarvis-voice - JARVIS Text-to-Speech

A JARVIS-inspired voice system using Microsoft's neural TTS:

```bash
# Speak text
python skills/jarvis-voice/speak.py --text "Hello Gavin"

# Toggle mute
python skills/jarvis-voice/jarvis-toggle.py
```

- Voice: en-GB-RyanNeural (British male)
- Rate: -2% (natural pacing)
- Pitch: -3Hz (slightly deeper)
- Auto-respects mute toggle via `~/.claude/jarvis-muted`

---

### visual-debugging - Playwright Visual Debugging & Discovery

Uses Playwright browser automation to visually debug UI issues and inspect reference websites for design patterns.

**Prerequisite:** Playwright MCP plugin (installed automatically by `install-skills.py`).

**Workflows:**
- **Visual Discovery** - Navigate to reference sites, screenshot, extract design patterns (colors, fonts, layout, animations)
- **Visual Debugging** - Open dev server URL, screenshot current state vs expected design
- **Responsive Testing** - Verify layout at mobile (375px), tablet (768px), and desktop (1440px) viewports
- **Design Audit** - Screenshot competitor sites to inform design decisions

**Automatic triggers:**
- UI debugging fails after initial code-level attempt
- User describes a UI they want but Claude lacks visual context
- User mentions wanting something "like" another website
- Need to verify responsive behavior at different viewports

**Example:**
```
You: "Make the hero section look like stripe.com's homepage"
Claude: Uses Playwright to screenshot stripe.com, extracts the gradient, typography,
        layout patterns, and builds something inspired by those design tokens
```

---

## Framework Detection

When you run `install-skills.py`, it scans your project and tells you which frameworks it detected and which skills are relevant:

```bash
$ cd my-react-app
$ python /path/to/install-skills.py

  STEP 3: Framework Detection
  Project: /home/user/my-react-app

  Detected stack:
    - React
    - TypeScript
    - Bootstrap

  Relevant installed skills:
    [INSTALLED] react-19
    [INSTALLED] claude-bootstrap-react-web
    [INSTALLED] javascript-es2025
    [INSTALLED] bootstrap-5
    [INSTALLED] html5
    [INSTALLED] css3
    [INSTALLED] frontend-aesthetics
    [INSTALLED] claude-bootstrap-base (always available)
```

### What It Detects

| Framework | How It's Detected |
|-----------|-------------------|
| **Django** | `manage.py` + `settings.py`, or `django` in requirements |
| **Python** | `requirements.txt`, `pyproject.toml`, `setup.py`, `Pipfile`, `.py` files |
| **React** | `react` in package.json dependencies |
| **Next.js** | `next` in package.json, or `next.config.*` file |
| **TypeScript** | `tsconfig.json` present |
| **Bootstrap** | `bootstrap` in package.json or referenced in HTML files |
| **Tailwind** | `tailwind.config.*` file present |
| **Frontend** | HTML/CSS files present (generic fallback) |

---

## Project Initialization

Running `--init` sets up a complete session management system:

```bash
python install-skills.py --init /path/to/project
```

### What Gets Created

**CLAUDE.md** - The master session guide containing:
- Session start protocol (which files to read first)
- Risk-level classification (Level 1-4) for features
- Test-driven development workflow
- Verification checklist before claiming completion
- Task management with hierarchical numbering (5 levels deep)
- Deviation handling with letter suffixes
- Automatic checkpoints every 5 tasks
- Deployment architecture (Docker + Portainer + Traefik)
- Skill quick reference

**Memory Files** (in `.claude/memory/`):
- `SESSION_CONTEXT.md` - Live state: active tasks, current files, blockers, next action
- `SESSION_CHANGELOG.md` - Timestamped session history
- `TASK_PROTOCOL.md` - Full hierarchical task numbering protocol
- `LEARNED_PATTERNS.md` - Patterns learned from each session (auto-updated)

### Safe Append Behavior

If your project already has a `CLAUDE.md`:
- The AI Engineer content is **appended** with an `<!-- AI Engineer Toolkit -->` marker
- Your existing content is preserved untouched
- Running again won't duplicate - the marker prevents double-append
- Memory files are only created if they don't exist

---

## Workflow Examples

### Example 1: Starting a New Django Project

```bash
# 1. Create your Django project
django-admin startproject mysite
cd mysite

# 2. Initialize with AI Engineer
python /path/to/install-skills.py --init .

# 3. Open Claude Code
claude

# Claude now has:
# - Django/Python skill loaded (models, views, DRF, Celery, etc.)
# - Session management (tasks, changelog, patterns)
# - TDD workflow enforced
# - Risk classification for features
```

### Example 2: Working on a React + Bootstrap App

```bash
cd my-react-app
python /path/to/install-skills.py --init .

# Claude automatically gets:
# - react-19 (all hooks, Server Components, Actions)
# - javascript-es2025 (modern JS syntax)
# - bootstrap-5 (all components and utilities)
# - html5 + css3 (modern standards)
# - frontend-aesthetics (design system, animations)
# - claude-bootstrap-react-web (React patterns)
# - TDD and code quality enforcement
```

### Example 3: Building a Creative Landing Page

```bash
# Even without --init, skills are globally available
claude

You: "Build a landing page for a coffee shop with scroll animations and 3D elements"

# Claude uses:
# - frontend-aesthetics (chooses distinctive fonts, colors, GSAP animations)
# - html5 (semantic structure, accessibility)
# - css3 (modern layout, scroll-driven animations)
# - javascript-es2025 (clean JS patterns)
# Result: A polished, non-generic page with scroll reveals, parallax, and personality
```

### Example 4: Session Recovery After Context Reset

```
Claude session resets mid-task...

Claude automatically:
1. Reads SESSION_CONTEXT.md -> sees active tasks and current state
2. Reads SESSION_CHANGELOG.md -> sees what happened last session
3. Reads LEARNED_PATTERNS.md -> remembers project-specific patterns
4. Resumes from "Next Action" without you repeating anything
```

---

## Tips & Best Practices

### Skill Selection

- **Don't worry about manual selection** - Claude picks up relevant skills automatically based on file types and project context
- **Framework detection is informational** - it tells you what's relevant but doesn't limit what Claude can use
- **All skills are always available** - even if detection doesn't flag them

### Getting the Best Results

- **Be specific about aesthetics**: "Build a landing page" gives generic results. "Build a brutalist landing page with a dark theme and GSAP scroll animations" gives distinctive results
- **Mention animation preferences**: "Use AOS for simple reveals" vs "Use GSAP with ScrollTrigger for a cinematic scroll experience"
- **Reference the skill directly**: "Using the Bootstrap 5 skill, build a dashboard" helps Claude focus

### Updating Skills

After modifying any skill file in the repo:

```bash
# Re-run installer to push updates to ~/.claude/skills/
python install-skills.py
```

### Creating Your Own Skills

Skills are just markdown files at `skills/<name>/SKILL.md` with a YAML frontmatter:

```markdown
---
name: my-skill
description: What this skill does and when to use it
---

# My Skill

Content here - reference docs, patterns, rules, code examples.
Claude reads this as context when the skill is relevant.
```

After creating a new skill, run `install-skills.py` to install it globally.

---

## File Structure

```
ai_engineer/
  install-skills.py          # Installer script
  HOW-TO-USE.md              # This file
  CLAUDE.md                  # Project-specific Claude config
  skills/
    bootstrap-5/SKILL.md     # Bootstrap 5.3.8 reference
    claude-bootstrap-base/   # Code quality & TDD
    claude-bootstrap-react-web/ # React patterns
    css3/SKILL.md            # Modern CSS reference
    django-python/SKILL.md   # Django & Python reference
    frontend-aesthetics/SKILL.md # Design & animation system
    html5/SKILL.md           # HTML5 reference
    jarvis-voice/            # TTS voice system
      speak.py               # Main TTS engine
      jarvis-toggle.py       # Mute/unmute toggle
    javascript-es2025/SKILL.md # Modern JS reference
    modern-ui-ux/SKILL.md    # UI/UX design skill
    react-19/SKILL.md        # React 19 reference
    visual-debugging/SKILL.md # Playwright visual debugging
    web-artifacts-builder/   # Claude.ai artifact builder
```

---

**Toolkit by GavinHolder** | Skills are automatically loaded by Claude Code
