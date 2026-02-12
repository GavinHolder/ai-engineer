# Installed Claude Code Plugins & Skills

> **All plugins below are installed automatically by `install-skills.py`.** No manual plugin installation needed.

---

## How to Use Skills & Plugins

### Method 1: Slash Commands (explicit invocation)
Type `/` followed by the skill name in Claude Code to explicitly invoke a skill:

```
/frontend-design        → Build a creative, distinctive UI component or page
/frontend-aesthetics    → Apply the full aesthetics system (typography, color, animation)
/bootstrap-5            → Use Bootstrap 5.3.8 framework with full component reference
/feature-dev            → Guided feature development with architecture focus
/brainstorming          → Explore requirements before building (use BEFORE any creative work)
/writing-plans          → Plan a multi-step implementation before coding
/test-driven-development → Write tests first, then implement
/systematic-debugging   → Debug methodically instead of guessing
/verification-before-completion → Verify everything works before claiming done
/requesting-code-review → Review your work before merging
/playground             → Create an interactive HTML explorer/configurator
/web-artifacts-builder  → Build complex React+Tailwind+shadcn artifacts
/Django Framework       → Build Django web applications
/hookify                → Create hooks to enforce behaviors
/claude-automation-recommender → Get Claude Code setup recommendations
/revise-claude-md       → Update CLAUDE.md with session learnings
/claude-md-improver     → Audit and improve CLAUDE.md files
/web-design-guidelines  → Audit UI for accessibility and best practices
/keybindings-help       → Customize keyboard shortcuts
```

### Method 2: Natural Language (automatic activation)
Many skills activate automatically when you describe what you need:

| What you say | Skills that activate |
|---|---|
| "Build me a landing page" | frontend-design, frontend-aesthetics, bootstrap-5 |
| "Create a dashboard with charts" | frontend-design, frontend-aesthetics |
| "Add a login form with Bootstrap" | bootstrap-5, frontend-aesthetics |
| "Debug this failing test" | systematic-debugging |
| "Plan the implementation for..." | writing-plans |
| "Review my code before I merge" | requesting-code-review |
| "Set up this Django project" | django-framework |
| "Optimize my React components" | vercel-react-best-practices |
| "Check my site's accessibility" | web-design-guidelines |
| "Make an interactive playground for..." | playground |
| "What Claude Code features should I use?" | claude-automation-recommender |

### Method 3: Combining Skills
For best results, invoke multiple skills together:

```
"Using Bootstrap 5 with creative animations, build me a SaaS pricing page"
→ Activates: bootstrap-5 + frontend-aesthetics + frontend-design

"Plan and then build a Django REST API with React frontend"
→ Use: /writing-plans first, then /Django Framework + /vercel-react-best-practices

"Build a complex multi-page artifact with shadcn components"
→ Use: /web-artifacts-builder + /frontend-aesthetics
```

### Workflow Best Practices

1. **Always start with /brainstorming** for any new feature or creative work
2. **Use /writing-plans** before multi-step implementations
3. **Use /test-driven-development** for any feature with testable logic
4. **Use /verification-before-completion** before claiming work is done
5. **Use /requesting-code-review** before merging to main
6. **Use /revise-claude-md** at the end of sessions to capture learnings

---

## Plugins from `anthropics/claude-plugins-official`

Install command: `/plugin` then select from the `anthropics/claude-plugins-official` marketplace.

### frontend-design
Create distinctive, production-grade frontend interfaces with high design quality. Use this skill when the user asks to build web components, pages, or applications. Generates creative, polished code that avoids generic AI aesthetics.

- **/frontend-design** — Main skill entry point for building web components, pages, or applications.

```
/plugin install frontend-design from anthropics/claude-plugins-official
```

### feature-dev
Guided feature development with codebase understanding and architecture focus.

- **/feature-dev** — Main skill entry point for guided feature development.

```
/plugin install feature-dev from anthropics/claude-plugins-official
```

### typescript-lsp
TypeScript Language Server Protocol integration.

```
/plugin install typescript-lsp from anthropics/claude-plugins-official
```

### security-guidance
Security guidance for safe coding practices.

```
/plugin install security-guidance from anthropics/claude-plugins-official
```

### pyright-lsp
Pyright Language Server Protocol integration for Python type checking.

```
/plugin install pyright-lsp from anthropics/claude-plugins-official
```

### claude-md-management
Manage and maintain CLAUDE.md project memory files:

- **/revise-claude-md** — Update CLAUDE.md with learnings from the current session.
- **/claude-md-improver** — Audit and improve CLAUDE.md files in repositories. Scans for all CLAUDE.md files, evaluates quality against templates, outputs quality report, then makes targeted updates.

```
/plugin install claude-md-management from anthropics/claude-plugins-official
```

### hookify
Create and manage hooks to prevent unwanted behaviors:

- **/configure** (hookify) — Enable or disable hookify rules interactively.
- **/help** (hookify) — Get help with the hookify plugin.
- **/hookify** — Create hooks to prevent unwanted behaviors from conversation analysis or explicit instructions.
- **/list** (hookify) — List all configured hookify rules.
- **/writing-rules** (hookify) — Guidance on hookify rule syntax and patterns.

```
/plugin install hookify from anthropics/claude-plugins-official
```

### claude-code-setup
- **/claude-automation-recommender** — Analyze a codebase and recommend Claude Code automations (hooks, subagents, skills, plugins, MCP servers). Use when setting up Claude Code for a project or optimizing workflows.

```
/plugin install claude-code-setup from anthropics/claude-plugins-official
```

### playground
Creates interactive HTML playgrounds — self-contained single-file explorers that let users configure something visually through controls, see a live preview, and copy out a prompt.

- **/playground** — Main skill entry point.

```
/plugin install playground from anthropics/claude-plugins-official
```

### playwright
Browser automation via Playwright MCP server (`npx @playwright/mcp@latest`). Gives Claude the ability to navigate websites, take screenshots, interact with elements, and inspect the DOM. Used for **visual debugging and design discovery**.

```
/plugin install playwright from anthropics/claude-plugins-official
```

**Playwright MCP tools:**

| Tool | What It Does |
|------|-------------|
| `browser_navigate` | Go to a URL |
| `browser_screenshot` | Capture current viewport |
| `browser_click` | Click an element |
| `browser_fill` | Fill form fields |
| `browser_snapshot` | Get accessibility tree (structured DOM) |
| `browser_resize` | Change viewport for responsive testing |

**Visual debugging workflows** (see `visual-debugging` skill for full details):
- **Visual Discovery** — Navigate to reference sites, screenshot, extract design patterns (colors, fonts, layout)
- **Visual Debugging** — Open dev server, screenshot current state, compare against expected design
- **Responsive Testing** — Check site at mobile (375px), tablet (768px), and desktop (1440px) viewports
- **Design Audit** — Screenshot competitor/reference sites to inform design decisions

---

## Plugins from `anthropics/claude-plugins-official` (also available but NOT installed)

These are available in the same marketplace but you haven't installed them yet:

| Plugin | Install Command |
|---|---|
| agent-sdk-dev | `/plugin install agent-sdk-dev from anthropics/claude-plugins-official` |
| clangd-lsp | `/plugin install clangd-lsp from anthropics/claude-plugins-official` |
| code-review | `/plugin install code-review from anthropics/claude-plugins-official` |
| code-simplifier | `/plugin install code-simplifier from anthropics/claude-plugins-official` |
| commit-commands | `/plugin install commit-commands from anthropics/claude-plugins-official` |
| csharp-lsp | `/plugin install csharp-lsp from anthropics/claude-plugins-official` |
| explanatory-output-style | `/plugin install explanatory-output-style from anthropics/claude-plugins-official` |
| gopls-lsp | `/plugin install gopls-lsp from anthropics/claude-plugins-official` |
| jdtls-lsp | `/plugin install jdtls-lsp from anthropics/claude-plugins-official` |
| kotlin-lsp | `/plugin install kotlin-lsp from anthropics/claude-plugins-official` |
| learning-output-style | `/plugin install learning-output-style from anthropics/claude-plugins-official` |
| lua-lsp | `/plugin install lua-lsp from anthropics/claude-plugins-official` |
| php-lsp | `/plugin install php-lsp from anthropics/claude-plugins-official` |
| plugin-dev | `/plugin install plugin-dev from anthropics/claude-plugins-official` |
| pr-review-toolkit | `/plugin install pr-review-toolkit from anthropics/claude-plugins-official` |
| ralph-loop | `/plugin install ralph-loop from anthropics/claude-plugins-official` |
| rust-analyzer-lsp | `/plugin install rust-analyzer-lsp from anthropics/claude-plugins-official` |
| swift-lsp | `/plugin install swift-lsp from anthropics/claude-plugins-official` |

### External plugins (in official marketplace)

| Plugin | Install Command |
|---|---|
| asana | `/plugin install asana from anthropics/claude-plugins-official` |
| context7 | `/plugin install context7 from anthropics/claude-plugins-official` |
| firebase | `/plugin install firebase from anthropics/claude-plugins-official` |
| github | `/plugin install github from anthropics/claude-plugins-official` |
| gitlab | `/plugin install gitlab from anthropics/claude-plugins-official` |
| greptile | `/plugin install greptile from anthropics/claude-plugins-official` |
| laravel-boost | `/plugin install laravel-boost from anthropics/claude-plugins-official` |
| linear | `/plugin install linear from anthropics/claude-plugins-official` |
| serena | `/plugin install serena from anthropics/claude-plugins-official` |
| slack | `/plugin install slack from anthropics/claude-plugins-official` |
| stripe | `/plugin install stripe from anthropics/claude-plugins-official` |
| supabase | `/plugin install supabase from anthropics/claude-plugins-official` |

---

## Plugin from `affaan-m/everything-claude-code`

### superpowers
A collection of workflow skills for structured development:

- **/brainstorming** — Explores user intent, requirements and design before any creative work (creating features, building components, adding functionality, or modifying behavior).
- **/dispatching-parallel-agents** — Use when facing 2+ independent tasks that can be worked on without shared state or sequential dependencies.
- **/executing-plans** — Execute a written implementation plan in a separate session with review checkpoints.
- **/finishing-a-development-branch** — Guides completion of development work by presenting structured options for merge, PR, or cleanup.
- **/receiving-code-review** — Use when receiving code review feedback, before implementing suggestions. Requires technical rigor and verification, not blind implementation.
- **/requesting-code-review** — Use when completing tasks, implementing major features, or before merging to verify work meets requirements.
- **/subagent-driven-development** — Execute implementation plans with independent tasks in the current session.
- **/systematic-debugging** — Use when encountering any bug, test failure, or unexpected behavior, before proposing fixes.
- **/test-driven-development** — Use when implementing any feature or bugfix, before writing implementation code.
- **/using-git-worktrees** — Creates isolated git worktrees with smart directory selection and safety verification.
- **/using-superpowers** — Establishes how to find and use skills at the start of any conversation.
- **/verification-before-completion** — Requires running verification commands and confirming output before making any success claims.
- **/writing-plans** — Use when you have a spec or requirements for a multi-step task, before touching code.
- **/writing-skills** — Use when creating new skills, editing existing skills, or verifying skills work before deployment.

```
/plugin install superpowers from affaan-m/everything-claude-code
```

---

## Custom Skills (manually created)

### frontend-aesthetics
Comprehensive frontend aesthetics system for producing distinctive, polished UI that avoids generic "AI slop". Covers typography, color, motion, backgrounds, layout, and a **complete animation library reference** with GSAP, Motion, Anime.js, AOS, Lottie, Three.js, tsParticles, Typed.js, Swiper, Locomotive Scroll, Splitting.js, and AutoAnimate. Based on [Anthropic's Coding Prompting for Frontend Aesthetics](https://platform.claude.com/cookbook/coding-prompting-for-frontend-aesthetics) cookbook.

- **/frontend-aesthetics** — Main skill entry point.

Manually created at `~/.claude/skills/frontend-aesthetics/SKILL.md`

### bootstrap-5
Comprehensive Bootstrap 5.3.8 reference and rules for building production-grade, creative Bootstrap interfaces. Covers ALL components, utilities, grid system, color modes, CSS variables, forms, helpers, accessibility, data attributes, and best practices.

- **/bootstrap-5** — Main skill entry point.

Manually created at `~/.claude/skills/bootstrap-5/SKILL.md`

---

## Skills from `anthropics/skills` (manually installed)

### web-artifacts-builder
Suite of tools for creating elaborate, multi-component claude.ai HTML artifacts using modern frontend web technologies (React, Tailwind CSS, shadcn/ui). Use for complex artifacts requiring state management, routing, or shadcn/ui components — not for simple single-file HTML/JSX artifacts.

- **/web-artifacts-builder** — Main skill entry point.

```
/plugin marketplace add anthropics/skills
/plugin install web-artifacts-builder from anthropic-agent-skills
```

Or manually: `git clone https://github.com/anthropics/skills` then copy `skills/web-artifacts-builder` to `~/.claude/skills/web-artifacts-builder`

---

## Skills from `alinaqi/claude-bootstrap` (manually installed)

### claude-bootstrap-base
Universal coding patterns, constraints, TDD workflow, and atomic todos. Security-first, spec-driven, AI-native project initialization.

- **/claude-bootstrap-base** — Base TDD and development patterns.

### claude-bootstrap-react-web
React web development with hooks, React Query, Zustand. TDD-first approach to building React components with Bootstrap styling.

- **/claude-bootstrap-react-web** — React web development skill.

```
git clone https://github.com/alinaqi/claude-bootstrap ~/.claude-bootstrap
cd ~/.claude-bootstrap && ./install.sh
```

Or manually: copy `skills/base` and `skills/react-web` to `~/.claude/skills/claude-bootstrap-base` and `~/.claude/skills/claude-bootstrap-react-web`

---

## Built-in Skills (ship with Claude Code, no install needed)

### django-framework
Build production-ready web applications with Django MVC, ORM, authentication, and REST APIs.

- **/Django Framework** — Main skill entry point.

### vercel-react-best-practices
React and Next.js performance optimization guidelines from Vercel Engineering. Use when writing, reviewing, or refactoring React/Next.js code to ensure optimal performance patterns. Triggers on tasks involving React components, Next.js pages, data fetching, bundle optimization, or performance improvements.

- **/vercel-react-best-practices** — Main skill entry point.

### web-design-guidelines
Review UI code for Web Interface Guidelines compliance. Use when asked to "review my UI", "check accessibility", "audit design", "review UX", or "check my site against best practices".

- **/web-design-guidelines** — Main skill entry point.

### keybindings-help
Use when you want to customize keyboard shortcuts, rebind keys, add chord bindings, or modify `~/.claude/keybindings.json`.

- **/keybindings-help** — Rebind keys, add chord shortcuts, change the submit key, customize keybindings.

---

## Built-in Claude Code Commands

These are built-in CLI commands (not plugins):

- **/add-dir** — Add a new working directory to the current session.
- **/agents** — Manage agent configurations.
- **/chrome** — Claude in Chrome (Beta) settings.
- **/clear** — Clear conversation history.
- **/compact** — Compact conversation context.
- **/help** — Get help with using Claude Code.
- **/plugin** — Install or manage plugins.
