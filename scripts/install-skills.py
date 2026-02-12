#!/usr/bin/env python3
"""
AI Engineer Toolkit - Skill Installer & Environment Setup

1. Copies enhanced/custom skills from repo to ~/.claude/skills/
2. Fixes Windows hook compatibility (python3 -> python)
3. Generates CLAUDE.md & memory files (or appends to existing CLAUDE.md)
4. Detects project frameworks and recommends relevant skills (read-only)

Usage:
    python install-skills.py
    python install-skills.py --detect <project-path>
    python install-skills.py --init <project-path>
"""

import json
import os
import platform
import shutil
import subprocess
import sys
from datetime import datetime, timezone
from pathlib import Path


# ---------------------------------------------------------------------------
# 0. PRE-FLIGHT: ENSURE CLAUDE CLI IS INSTALLED
# ---------------------------------------------------------------------------

def ensure_claude_cli() -> bool:
    """Check if Claude CLI is installed, install via npm if missing."""
    print("\n" + "=" * 60)
    print("  PRE-FLIGHT: Checking Claude CLI")
    print("=" * 60)

    if shutil.which("claude"):
        try:
            result = subprocess.run(
                ["claude", "--version"],
                capture_output=True, text=True, timeout=10,
            )
            version = (result.stdout.strip() or result.stderr.strip() or "unknown")
            print(f"  Claude CLI found: {version}")
        except Exception:
            print("  Claude CLI found in PATH.")
        return True

    print("  Claude CLI not found. Attempting install via npm...")

    npm_cmd = shutil.which("npm")
    if not npm_cmd:
        print("  ERROR: npm not found. Install Node.js first, then run:")
        print("    npm install -g @anthropic-ai/claude-code")
        return False

    try:
        result = subprocess.run(
            [npm_cmd, "install", "-g", "@anthropic-ai/claude-code"],
            capture_output=True, text=True, timeout=120,
        )
        if result.returncode == 0:
            print("  [INSTALLED] Claude CLI (@anthropic-ai/claude-code)")
            return True
        else:
            print(f"  ERROR: npm install failed: {result.stderr.strip()[:200]}")
            print("  Try manually: npm install -g @anthropic-ai/claude-code")
            return False
    except subprocess.TimeoutExpired:
        print("  TIMEOUT: npm install took too long. Try manually.")
        return False


# ---------------------------------------------------------------------------
# 1. SKILL INSTALLATION
# ---------------------------------------------------------------------------

def install_skills(repo_root: Path) -> int:
    """Copy enhanced skills from repo to ~/.claude/skills/."""
    print("\n" + "=" * 60)
    print("  STEP 1: Installing Enhanced Skills")
    print("=" * 60)

    repo_skills = repo_root / "skills"
    target_skills = Path.home() / ".claude" / "skills"

    if not repo_skills.exists():
        print("  ERROR: No skills/ folder found in repo.")
        return 0

    target_skills.mkdir(parents=True, exist_ok=True)
    copied = 0

    for skill_dir in sorted(repo_skills.iterdir()):
        if not skill_dir.is_dir():
            continue

        skill_name = skill_dir.name
        target_dir = target_skills / skill_name

        for root, dirs, files in os.walk(skill_dir):
            rel_root = Path(root).relative_to(skill_dir)
            target_root = target_dir / rel_root
            target_root.mkdir(parents=True, exist_ok=True)

            for file in files:
                src = Path(root) / file
                dst = target_root / file
                existed = dst.exists()
                shutil.copy2(src, dst)
                action = "OVERWRITTEN" if existed else "INSTALLED"
                print(f"  [{action}] {skill_name}/{rel_root / file}")
                copied += 1

    print(f"\n  {copied} file(s) installed to {target_skills}")
    return copied


# ---------------------------------------------------------------------------
# 1b. PLUGIN INSTALLATION
# ---------------------------------------------------------------------------

# All plugins to install automatically
# Format: (plugin_name, source_repo)
PLUGINS_TO_INSTALL = [
    # From anthropics/claude-plugins-official
    ("frontend-design", "anthropics/claude-plugins-official"),
    ("feature-dev", "anthropics/claude-plugins-official"),
    ("typescript-lsp", "anthropics/claude-plugins-official"),
    ("security-guidance", "anthropics/claude-plugins-official"),
    ("pyright-lsp", "anthropics/claude-plugins-official"),
    ("claude-md-management", "anthropics/claude-plugins-official"),
    ("hookify", "anthropics/claude-plugins-official"),
    ("claude-code-setup", "anthropics/claude-plugins-official"),
    ("playground", "anthropics/claude-plugins-official"),
    ("playwright", "anthropics/claude-plugins-official"),
    # From affaan-m/everything-claude-code
    ("superpowers", "affaan-m/everything-claude-code"),
]


def install_plugins() -> int:
    """Install Claude Code plugins via the claude CLI."""
    print("\n" + "=" * 60)
    print("  STEP 1b: Installing Claude Code Plugins")
    print("=" * 60)

    # Check if claude CLI is available
    claude_cmd = shutil.which("claude")
    if not claude_cmd:
        print("  WARNING: 'claude' CLI not found in PATH.")
        print("  Plugins must be installed manually. See plugins.md for commands.")
        return 0

    installed = 0
    skipped = 0
    failed = 0

    for plugin_name, source_repo in PLUGINS_TO_INSTALL:
        try:
            result = subprocess.run(
                [claude_cmd, "plugin", "install", plugin_name, "from", source_repo],
                capture_output=True,
                text=True,
                timeout=60,
            )
            if result.returncode == 0:
                if "already installed" in result.stdout.lower():
                    print(f"  [SKIPPED] {plugin_name} (already installed)")
                    skipped += 1
                else:
                    print(f"  [INSTALLED] {plugin_name} from {source_repo}")
                    installed += 1
            else:
                # Check stderr for "already installed" too
                combined = (result.stdout + result.stderr).lower()
                if "already installed" in combined or "already" in combined:
                    print(f"  [SKIPPED] {plugin_name} (already installed)")
                    skipped += 1
                else:
                    print(f"  [FAILED] {plugin_name}: {result.stderr.strip()[:100]}")
                    failed += 1
        except subprocess.TimeoutExpired:
            print(f"  [TIMEOUT] {plugin_name} (skipped)")
            failed += 1
        except Exception as e:
            print(f"  [ERROR] {plugin_name}: {e}")
            failed += 1

    print(f"\n  {installed} installed, {skipped} already present, {failed} failed")
    return installed


# ---------------------------------------------------------------------------
# 2. WINDOWS HOOK FIXES
# ---------------------------------------------------------------------------

def fix_windows_hooks() -> int:
    """Fix python3 -> python in all plugin hook files on Windows."""
    print("\n" + "=" * 60)
    print("  STEP 2: Fixing Windows Hook Compatibility")
    print("=" * 60)

    if platform.system() != "Windows":
        print("  Not Windows - skipping hook fixes.")
        return 0

    claude_dir = Path.home() / ".claude" / "plugins"
    if not claude_dir.exists():
        print("  No plugins directory found - skipping.")
        return 0

    fixed = 0
    hook_files = list(claude_dir.rglob("hooks.json"))

    for hook_file in hook_files:
        try:
            content = hook_file.read_text(encoding="utf-8")
        except (OSError, UnicodeDecodeError):
            continue

        if "python3 " not in content:
            continue

        new_content = content.replace("python3 ", "python ")
        hook_file.write_text(new_content, encoding="utf-8")

        rel_path = hook_file.relative_to(claude_dir)
        count = content.count("python3 ")
        print(f"  [FIXED] {rel_path} ({count} occurrence(s))")
        fixed += count

    if fixed == 0:
        print("  No python3 references found - all hooks OK.")
    else:
        print(f"\n  {fixed} hook command(s) fixed (python3 -> python)")

    return fixed


# ---------------------------------------------------------------------------
# 3. CLAUDE.MD & MEMORY FILE GENERATION
# ---------------------------------------------------------------------------

AI_ENGINEER_MARKER = "<!-- AI Engineer Toolkit -->"

CLAUDE_MD_TEMPLATE = r"""# Claude Code Session Guide - {project_name}

**Project:** {project_name}
**Created:** {timestamp}
**Last Updated:** {timestamp}

---

## Quick Start

### Essential Files (Read These First)
1. `.claude/memory/SESSION_CONTEXT.md` - Active tasks and current state
2. `.claude/memory/TASK_PROTOCOL.md` - Hierarchical task management (5 levels, checkpoints)
3. `.claude/memory/SESSION_CHANGELOG.md` - Session history with timestamps
4. `.claude/memory/LEARNED_PATTERNS.md` - Continuous learning log
5. `CLAUDE.md` - This file (session guide and project rules)

### Session Start Protocol
1. Read `SESSION_CONTEXT.md` for active tasks and state
2. Read `SESSION_CHANGELOG.md` for last session summary
3. Resume from "Next Action" in SESSION_CONTEXT.md
4. If new session: create task list, update SESSION_CONTEXT.md

---

## Core Principles

### 1. Adversarial Verification (Non-Negotiable)

Every feature implementation must be classified and verified at the appropriate level:

| Level | Risk | Examples | Workflow |
|-------|------|----------|----------|
| **Level 4 (CRITICAL)** | Data loss, security, money | Auth, payments, data migrations, API keys | `/plan` -> `/adversarial-review` -> TDD -> `/security-review` -> `/code-review` |
| **Level 3 (HIGH)** | Breaking changes, integrations | DB schema, external APIs, deployment configs | `/plan` -> `/adversarial-review` -> TDD -> `/code-review` |
| **Level 2 (MEDIUM)** | Standard features | UI components, new pages, utilities | `/plan` -> Code -> `/code-review` |
| **Level 1 (LOW)** | Minimal risk | Docs, tests, formatting, refactoring | Code -> Optional review |

**Adversarial Review Checklist (Level 3+):**
- [ ] Edge cases identified and tested
- [ ] Failure modes documented with mitigations
- [ ] Input validation at all boundaries
- [ ] Error handling covers all paths (no silent failures)
- [ ] Security implications reviewed (OWASP Top 10)
- [ ] Performance implications considered
- [ ] Rollback plan defined

### 2. Test-Driven Development (Level 2+)

```
1. RED: Write failing tests first (proves tests are valid)
2. GREEN: Write minimum code to pass
3. VALIDATE: Run lint + typecheck + full test suite
4. COMPLETE: Only after ALL validations pass
```

**Never skip TDD. Tests must fail before implementation begins.**

### 3. Verification Before Completion

Before claiming ANY task is done:
- [ ] All tests passing
- [ ] Linter clean (no errors)
- [ ] Type checker clean (if applicable)
- [ ] Manual verification of the feature
- [ ] Edge cases tested
- [ ] No regressions introduced

---

## Task Management Protocol (Non-Negotiable)

**NOTHING gets done without tasks.** Before writing any code, making any change, or starting any work, you MUST create a task list first. This is not optional. This is how we work.

### Why This Matters

Without tasks, Claude loses track of multi-step work, skips steps, forgets what's next after fixing a bug, and fails to recover after context resets. Tasks are the backbone of reliable work.

### Rule: Always Create Tasks First

1. **Receive a request** -> Create tasks BEFORE touching any code
2. **Each task gets subtasks** if it involves more than one step
3. **Mark tasks in_progress** before starting, **completed** when done
4. **Never skip ahead** - finish or explicitly pause the current task before moving to the next

### Hierarchical Numbering (5 Levels Max)

```
1. Main Task (Level 1)
   1.1 Subtask (Level 2)
       1.1.1 Sub-subtask (Level 3)
             1.1.1.1 Detail task (Level 4)
                     1.1.1.1.1 Granular task (Level 5 - max)
```

### Debug Tasks (Fixing Bugs Mid-Step)

When something breaks while working on a step, create a **debug task** as a child of the current task. Do NOT abandon the parent task or skip ahead. Fix the issue, then resume exactly where you left off.

```
1. Build user dashboard
   1.1 Create layout component [IN PROGRESS]
   1.1.debug.a: CSS grid not rendering correctly
       1.1.debug.a.1 Investigate - check browser output
       1.1.debug.a.2 Fix - missing display:grid on container
       1.1.debug.a.3 Verify fix renders correctly
   1.1 [RESUMED] - Continue layout component
   1.2 Add data widgets (NEXT - untouched, waiting)
```

**Key rule:** Debug tasks fix the current step. They do NOT affect or reorder the remaining steps. Steps 1.2, 1.3, etc. stay exactly where they are.

### Amendment Tasks (Revising a Completed Step)

When a completed step needs changes (user feedback, missed requirement, etc.), create an **amendment task**. Do NOT re-do the entire step.

```
1. Build API endpoints
   1.1 Create GET /users [COMPLETE]
   1.2 Create POST /users [COMPLETE]
   1.2.amend.a: Add email validation to POST /users
       1.2.amend.a.1 Add validation logic
       1.2.amend.a.2 Update tests
       1.2.amend.a.3 Verify
   1.3 Create DELETE /users (NEXT - still in queue)
```

### Deviation Handling (Unexpected Discoveries)

When issues are discovered mid-task that aren't bugs in the current step but broader problems:

```
1. Main Task
   1.1 Subtask [IN PROGRESS]
   DEVIATION 1.1.a: Discovered auth middleware is missing
       1.1.a.1 Investigate scope of the issue
       1.1.a.2 Fix implementation
       1.1.a.3 Verify fix with tests
   1.2 Continue original plan (unchanged)
```

**Multiple deviations:** a, b, c, d, e
**Nested deviations:** use Greek letters (alpha, beta, gamma)

### Automatic Checkpoints

**Every 5 main tasks, insert a checkpoint:**
```
1. Task 1
2. Task 2
3. Task 3
4. Task 4
5. Task 5
6. CHECKPOINT: Review progress, update memory files
```

**Checkpoint Actions:**
1. Update `SESSION_CHANGELOG.md` with completed tasks + timestamps
2. Update `SESSION_CONTEXT.md` with current state
3. Run continuous learning (extract patterns from what worked/failed)
4. Report summary to user

**Manual checkpoint:** User says "checkpoint" at any time.

### Task Status Indicators

```
[ ] NOT STARTED
[>] IN PROGRESS
[x] COMPLETE
[!] DEVIATION - issue discovered
[D] DEBUG - fixing a bug in current step
[A] AMENDMENT - revising a completed step
[-] BLOCKED - waiting on dependency
[X] FAILED - requires replanning
[#] CHECKPOINT
```

---

## Session Management

### Session Changelog (Mandatory)

Every session MUST be logged in `.claude/memory/SESSION_CHANGELOG.md`:

```markdown
### YYYY-MM-DD HH:MM:SS UTC - Session Start
**Focus:** [What this session will accomplish]

### YYYY-MM-DD HH:MM:SS UTC - Task N: [Name]
**Status:** COMPLETE/IN PROGRESS/BLOCKED
**Subtasks:**
- [x] N.1 Description
- [x] N.2 Description
**Result:** [What was accomplished]

### YYYY-MM-DD HH:MM:SS UTC - CHECKPOINT (Tasks 1-5)
**Tasks Completed:** N
**Tasks Remaining:** N
**Memory Files Updated:** [list]
**Next:** Task N+1 - [Name]

### YYYY-MM-DD HH:MM:SS UTC - Session End
**Tasks completed:** N
**Tasks pending:** N
**Next session:** Resume at [Task]
**Patterns learned:** [Count]
```

### Session Context (Active State)

`.claude/memory/SESSION_CONTEXT.md` tracks the live state:
- Active task list with status indicators
- Current working state (what files are being edited)
- Known blockers
- System configuration summary
- Next action (always specific and actionable)

---

## Continuous Learning

### When to Learn

After every checkpoint and session end:
1. **What worked?** Extract successful patterns
2. **What failed?** Document mistakes and root causes
3. **What was slow?** Identify workflow improvements
4. **What was new?** Capture domain knowledge

### Where to Store

`.claude/memory/LEARNED_PATTERNS.md` organized by category:
- **Code Patterns** - File organization, naming, structure
- **Architecture Patterns** - Service layer, data flow, API design
- **Frontend Patterns** - Components, styling, animation
- **Domain Knowledge** - Business logic, constraints, invariants
- **Mistakes & Fixes** - Bugs encountered and how they were resolved
- **User Preferences** - Communication style, UI aesthetic, workflow

### Auto-Apply

All learned patterns are automatically applied to future work.
When a pattern conflicts with a new requirement, flag it and ask.

---

## Development Workflow

### Starting New Features

0. **Create tasks first** - Break the work into tasks and subtasks BEFORE writing any code
1. **Classify risk level** (Level 1-4)
2. **Plan first** - Use `/writing-plans` or `/brainstorming` for Level 2+
3. **Visualize UI** - Use `/playground` to mock up, or `visual-debugging` to screenshot reference sites
4. **For Level 3+**: Run `/adversarial-review` before coding
5. **Write tests first** (TDD for Level 2+)
6. **Implement** - Follow code style rules below. Create debug/amendment tasks for issues, never skip steps.
7. **Verify** - Run full test suite, lint, typecheck
8. **Review** - `/requesting-code-review` for Level 2+
9. **Update memory** - Log to changelog, extract patterns

### Code Style Rules

- **Max file size:** 500 lines (aim for 200-400)
- **Max function length:** 20 lines
- **Max parameters:** 3 (use options object if more)
- **Max nesting:** 2 levels (flatten with early returns)
- **Single responsibility** per file and function
- **No dead code** - delete it, git remembers
- **No magic numbers** - use named constants
- **No silent failures** - every error is logged or thrown
- **Descriptive names** over comments

### Deployment Architecture

All deployments follow Docker + Portainer + Traefik:
- **Portainer** - Own stack, manages all containers via UI
- **Traefik** - Own stack, reverse proxy and SSL
- **Applications** - Each app is its own stack, manually built via Portainer
- Docker Compose files use `image: build` structure (never auto-build)
- Always use local VM-mounted volumes for container access

---

## Non-Negotiable Rules

These rules apply to EVERY session, EVERY task, no exceptions:

1. **Always create tasks first** - No code gets written without a task list. Period.
2. **Tasks have subtasks** - Break work into trackable steps. Mark in_progress before starting, completed when done.
3. **Debug tasks for bugs** - When something breaks mid-step, create a debug child task. Fix it in place. Do NOT skip ahead or lose track of remaining steps.
4. **Amendment tasks for revisions** - When a completed step needs changes, create an amendment task. Do NOT redo the entire step.
5. **Visual debugging for UI work** - When debugging UI issues or building creative frontends, use the `visual-debugging` skill (Playwright) to screenshot, inspect, and verify visually.
6. **Never skip steps** - Remaining tasks in the queue are sacred. Debug/amend the current step without touching the plan.
7. **Verify before claiming done** - Run tests, check output, confirm visually if applicable.

---

## Plugin & Skill Quick Reference

### Workflow Skills (use in order)
```
/brainstorming                    -> Before ANY creative work
/writing-plans                    -> Before multi-step implementations
/test-driven-development          -> Before writing implementation code
/systematic-debugging             -> When encountering bugs
/verification-before-completion   -> Before claiming work is done
/requesting-code-review           -> Before merging
/revise-claude-md                 -> End of session to capture learnings
```

### Frontend Skills
```
/frontend-design                  -> Build distinctive UI
/frontend-aesthetics              -> Typography, color, animation system
/bootstrap-5                      -> Bootstrap 5.3.8 component reference
/playground                       -> Interactive HTML explorers
/web-artifacts-builder            -> Complex React+shadcn artifacts
visual-debugging                  -> Playwright browser screenshots & design discovery
```

### Development Skills
```
/feature-dev                      -> Guided feature development
/Django Framework                 -> Django web applications
/claude-bootstrap-base            -> TDD workflow, coding patterns
/claude-bootstrap-react-web       -> React development patterns
```

---

## Session Recovery

If Claude session resets:
1. Read `.claude/memory/SESSION_CONTEXT.md` (active tasks + state)
2. Read `.claude/memory/SESSION_CHANGELOG.md` (what happened last)
3. Read `.claude/memory/LEARNED_PATTERNS.md` (project patterns)
4. Resume from "Next Action" in SESSION_CONTEXT.md

---

**Document Version:** 1.0
**Generated by:** install-skills.py
**Framework:** AI Engineer Startup Toolkit by GavinHolder
"""

SESSION_CHANGELOG_TEMPLATE = """# Session Changelog - {project_name}

**Created:** {timestamp}

---

## Changelog Format

### [Date Time UTC] - Session Start
- **Focus:** [Session objectives]

### [Date Time UTC] - Task N: [Description]
- **Status:** COMPLETE/IN PROGRESS/BLOCKED
- **Result:** [What was accomplished]

### [Date Time UTC] - CHECKPOINT (Tasks 1-N)
- **Tasks Completed:** N
- **Tasks Remaining:** N
- **Memory Files Updated:** [list]

### [Date Time UTC] - Session End
- **Tasks completed:** N
- **Tasks pending:** N
- **Next session:** [Resume point]
- **Patterns learned:** [Count]

---

## Session History

### {timestamp} - Project Initialized
- Created CLAUDE.md (session guide)
- Created memory files (SESSION_CONTEXT, SESSION_CHANGELOG, TASK_PROTOCOL, LEARNED_PATTERNS)
- Enhanced skills installed
- Windows hook compatibility verified

---
"""

SESSION_CONTEXT_TEMPLATE = """# Session Context - Active State

**Session Started:** {timestamp}
**Last Updated:** {timestamp}
**Current Checkpoint:** Initial setup

---

## Active Tasks
- [x] Project initialized with AI Engineer Toolkit
- [ ] **Next: Define project scope and first task list**

---

## Current State
- **Working on:** Ready for first task list
- **Last files created:** CLAUDE.md, memory files
- **Migrations pending:** None
- **Tests passing:** N/A

---

## Known Blockers
None currently

---

## System Configuration Summary

**SESSION MANAGEMENT:**
- Changelog granularity: Balanced (tasks/subtasks with timestamps)
- Checkpoint frequency: Auto every 5 tasks
- Checkpoint retention: All (forever)

**LEARNING:**
- Trigger: After every session/checkpoint
- Scope: Everything (code, architecture, domain, mistakes, preferences)
- Storage: Per-project categorized files
- Auto-apply: Enabled

**ADVERSARIAL:**
- Level 4: /plan -> /adversarial-review -> TDD -> /security-review -> /code-review
- Level 3: /plan -> /adversarial-review -> TDD -> /code-review
- Auto-trigger: Enabled for Level 3+

---

## Next Action
**READY FOR WORK:** Provide task list or describe what to build.
"""

TASK_PROTOCOL_TEMPLATE = """# Hierarchical Task Management Protocol (Non-Negotiable)

**Version:** 3.0
**Created:** {timestamp}
**Max Depth:** 5 levels

---

## Golden Rule

**NOTHING gets done without tasks.** Before writing any code, making any change, or starting any work, create a task list first. Every task must be tracked from start to completion. This is mandatory, not a suggestion.

---

## Numbering System

### Level 1-5 Hierarchy
```
1. Main Task (Level 1)
   1.1 Subtask (Level 2)
       1.1.1 Sub-subtask (Level 3)
             1.1.1.1 Detail task (Level 4)
                     1.1.1.1.1 Granular task (Level 5 - maximum)
```

**Max depth = 5.** If you need 6 levels, the task is too complex - break into multiple Level 1 tasks.

---

## Debug Tasks (Fixing Bugs Mid-Step)

When something breaks while working on a step, create a **debug task** as a child. Do NOT abandon the parent task. Do NOT skip to the next step. Fix the issue in place, then resume.

```
1. Build user dashboard
   1.1 Create layout component [IN PROGRESS]
   1.1.debug.a: CSS grid not rendering correctly
       1.1.debug.a.1 Investigate - check browser output
       1.1.debug.a.2 Fix - missing display:grid on container
       1.1.debug.a.3 Verify fix
   1.1 [RESUMED] Continue layout component
   1.2 Add data widgets (NEXT - untouched, stays in queue)
```

**Critical:** The remaining steps (1.2, 1.3, etc.) do NOT move or change when a debug task is created. They stay exactly where they are.

---

## Amendment Tasks (Revising a Completed Step)

When a completed step needs changes (user feedback, missed requirement, discovered issue), create an **amendment task**. Do NOT re-do the entire step or shuffle the remaining plan.

```
1. Build API endpoints
   1.1 Create GET /users [COMPLETE]
   1.2 Create POST /users [COMPLETE]
   1.2.amend.a: Add email validation to POST /users
       1.2.amend.a.1 Add validation logic
       1.2.amend.a.2 Update tests
       1.2.amend.a.3 Verify
   1.3 Create DELETE /users (NEXT - still in queue)
```

---

## Deviation Handling (Unexpected Discoveries)

When broader issues are discovered mid-task (not bugs in the current step):

```
1. Main Task
   1.1 Subtask [IN PROGRESS]
   DEVIATION 1.1.a: Discovered auth middleware is missing
       1.1.a.1 Investigate scope
       1.1.a.2 Fix implementation
       1.1.a.3 Verify fix with tests
   1.2 Continue original plan (unchanged)
```

**Multiple deviations:** a, b, c, d, e (max 5 per level)
**Nested deviations:** alpha, beta, gamma, delta, epsilon

---

## Checkpoint System

### Automatic Checkpoints (Every 5 Tasks)

```
1. Task 1
2. Task 2
3. Task 3
4. Task 4
5. Task 5
6. CHECKPOINT: Review progress, update memory files
7. Task 6
...
12. CHECKPOINT: Review progress, update memory files
```

### Checkpoint Actions

1. Update SESSION_CHANGELOG.md with completed tasks + timestamps
2. Update SESSION_CONTEXT.md with current state
3. Run continuous learning (extract patterns)
4. Report summary to user:
   ```
   CHECKPOINT (Tasks 1-5 complete)
   - N tasks completed
   - N tasks remaining
   - Memory files updated
   - Next: Task N - [Name]
   ```

### Manual Checkpoints

User says "checkpoint" at any time to trigger checkpoint actions.

---

## Task Status Indicators

```
[ ] NOT STARTED
[>] IN PROGRESS
[x] COMPLETE
[D] DEBUG - fixing a bug in current step
[A] AMENDMENT - revising a completed step
[!] DEVIATION - unexpected issue discovered
[-] BLOCKED - waiting on dependency
[X] FAILED - requires replanning
[#] CHECKPOINT
```

---

## When to Create Subtasks

**Always create subtasks when:**
- Main task has >1 distinct step
- Task touches >1 file
- Task is Level 2+ (any non-trivial work)

**Keep flat only when:**
- Task is genuinely single-step (rename a variable, fix a typo)

---

## Depth Guidelines

| Depth | Use Case | Example |
|-------|----------|---------|
| Level 1 | Major features, phases | 1. Build user auth system |
| Level 2 | Feature components | 1.1 Create login form |
| Level 3 | Implementation steps | 1.1.1 Add form validation |
| Level 4 | Detailed actions | 1.1.1.1 Write Zod schema |
| Level 5 | Granular fixes (rare) | 1.1.1.1.1 Handle edge case |

---

**This protocol is mandatory for all sessions. No exceptions.**
"""

LEARNED_PATTERNS_TEMPLATE = """# Learned Patterns - {project_name}

**Created:** {timestamp}
**Last Updated:** {timestamp}
**Total Patterns:** 0
**Auto-Apply:** Enabled

---

## Code Patterns
*Patterns will be extracted from each session and logged here.*

---

## Architecture Patterns
*Service layer, data flow, API design patterns.*

---

## Frontend Patterns
*Component structure, styling, animation preferences.*

---

## Domain Knowledge
*Business logic, constraints, invariants.*

---

## Mistakes & Fixes
*Bugs encountered and how they were resolved.*

---

## User Preferences
- **Communication style:** Concise, results-focused
- **UI aesthetic:** Distinctive, avoids generic AI slop
- **Deployment:** Docker + Portainer + Traefik
- **Workflow:** Plan -> Build -> Verify -> Review

---

*This file is auto-updated after each session via continuous learning.*
"""


def generate_claude_md(project_root: Path):
    """Generate CLAUDE.md and memory files for a project.

    If CLAUDE.md already exists, appends the AI Engineer content
    (marked with a comment) instead of skipping.
    """
    print("\n" + "=" * 60)
    print("  Generating CLAUDE.md & Memory Files")
    print("=" * 60)

    claude_md_path = project_root / "CLAUDE.md"
    memory_dir = project_root / ".claude" / "memory"

    project_name = project_root.name
    timestamp = datetime.now(timezone.utc).strftime("%Y-%m-%d %H:%M:%S UTC")

    ai_engineer_content = CLAUDE_MD_TEMPLATE.format(
        project_name=project_name,
        timestamp=timestamp,
    )

    if claude_md_path.exists():
        existing = claude_md_path.read_text(encoding="utf-8")

        # Check if AI Engineer content was already appended
        if AI_ENGINEER_MARKER in existing:
            print(f"  CLAUDE.md already contains AI Engineer section - skipping.")
        else:
            # Append AI Engineer content to existing CLAUDE.md
            appendix = (
                f"\n\n{AI_ENGINEER_MARKER}\n"
                f"<!-- Appended by install-skills.py on {timestamp} -->\n\n"
                f"{ai_engineer_content}"
            )
            claude_md_path.write_text(existing + appendix, encoding="utf-8")
            print(f"  [APPENDED] AI Engineer section added to existing CLAUDE.md")
    else:
        # Create new CLAUDE.md with marker at the top
        content = f"{AI_ENGINEER_MARKER}\n\n{ai_engineer_content}"
        claude_md_path.write_text(content, encoding="utf-8")
        print(f"  [CREATED] CLAUDE.md")

    # Create memory directory and files
    memory_dir.mkdir(parents=True, exist_ok=True)

    files = {
        "SESSION_CHANGELOG.md": SESSION_CHANGELOG_TEMPLATE,
        "SESSION_CONTEXT.md": SESSION_CONTEXT_TEMPLATE,
        "TASK_PROTOCOL.md": TASK_PROTOCOL_TEMPLATE,
        "LEARNED_PATTERNS.md": LEARNED_PATTERNS_TEMPLATE,
    }

    for filename, template in files.items():
        filepath = memory_dir / filename
        if filepath.exists():
            print(f"  [SKIPPED] .claude/memory/{filename} (already exists)")
        else:
            content = template.format(
                project_name=project_name,
                timestamp=timestamp,
            )
            filepath.write_text(content, encoding="utf-8")
            print(f"  [CREATED] .claude/memory/{filename}")

    print(f"\n  CLAUDE.md and memory files ready at {project_root}")


# ---------------------------------------------------------------------------
# 4. FRAMEWORK DETECTION (read-only)
# ---------------------------------------------------------------------------

# Maps detected frameworks to recommended skills
SKILL_MAP = {
    "Django":     ["django-python"],
    "Python":     ["django-python"],
    "React":      ["react-19", "claude-bootstrap-react-web", "javascript-es2025", "frontend-aesthetics", "modern-ui-ux", "visual-debugging"],
    "Next.js":    ["react-19", "claude-bootstrap-react-web", "javascript-es2025", "modern-ui-ux", "visual-debugging"],
    "TypeScript": ["react-19", "claude-bootstrap-react-web", "javascript-es2025"],
    "Bootstrap":  ["bootstrap-5", "html5", "css3", "modern-ui-ux", "visual-debugging"],
    "Tailwind":   ["css3", "frontend-aesthetics", "modern-ui-ux", "visual-debugging"],
    "Frontend":   ["html5", "css3", "javascript-es2025", "frontend-aesthetics", "modern-ui-ux", "visual-debugging"],
}


def _read_json(path: Path) -> dict:
    """Safely read a JSON file, returning empty dict on failure."""
    try:
        return json.loads(path.read_text(encoding="utf-8"))
    except (OSError, UnicodeDecodeError, json.JSONDecodeError):
        return {}


def _read_text(path: Path) -> str:
    """Safely read a text file, returning empty string on failure."""
    try:
        return path.read_text(encoding="utf-8")
    except (OSError, UnicodeDecodeError):
        return ""


def detect_frameworks(project_path: Path) -> dict[str, list[str]]:
    """
    Scan a project directory for framework markers.

    Returns a dict of {framework_name: [recommended_skills]}.
    This function is purely read-only — it never modifies anything.
    """
    detected: dict[str, list[str]] = {}

    # -- Python detection --
    has_requirements = (project_path / "requirements.txt").exists()
    has_pyproject = (project_path / "pyproject.toml").exists()
    has_setup_py = (project_path / "setup.py").exists()
    has_pipfile = (project_path / "Pipfile").exists()
    has_py_files = bool(list(project_path.glob("*.py")))

    python_detected = any([has_requirements, has_pyproject, has_setup_py, has_pipfile, has_py_files])

    # Check for Django markers
    django_detected = False
    has_manage_py = (project_path / "manage.py").exists()

    if has_manage_py:
        # manage.py is a strong Django signal, but check for settings too
        settings_candidates = list(project_path.glob("*/settings.py")) + list(project_path.glob("*/settings/*.py"))
        if settings_candidates:
            django_detected = True

    # Check requirements/pyproject for django dependency
    if not django_detected:
        deps_text = ""
        if has_requirements:
            deps_text += _read_text(project_path / "requirements.txt").lower()
        if has_pyproject:
            deps_text += _read_text(project_path / "pyproject.toml").lower()
        if has_pipfile:
            deps_text += _read_text(project_path / "Pipfile").lower()
        if "django" in deps_text:
            django_detected = True

    if django_detected:
        detected["Django"] = SKILL_MAP["Django"]
    elif python_detected:
        detected["Python"] = SKILL_MAP["Python"]

    # -- JavaScript/Node detection via package.json --
    pkg_json_path = project_path / "package.json"
    pkg = _read_json(pkg_json_path) if pkg_json_path.exists() else {}
    all_deps = {}
    if pkg:
        all_deps.update(pkg.get("dependencies", {}))
        all_deps.update(pkg.get("devDependencies", {}))

    # Next.js (check before React since Next includes React)
    next_config_exists = bool(
        list(project_path.glob("next.config.*"))
    )
    if "next" in all_deps or next_config_exists:
        detected["Next.js"] = SKILL_MAP["Next.js"]

    # React
    if "react" in all_deps:
        detected["React"] = SKILL_MAP["React"]

    # TypeScript
    if (project_path / "tsconfig.json").exists():
        detected["TypeScript"] = SKILL_MAP["TypeScript"]

    # -- CSS framework detection --
    # Bootstrap (in package.json deps or in HTML files)
    bootstrap_in_deps = "bootstrap" in all_deps
    bootstrap_in_html = False
    if not bootstrap_in_deps:
        for html_file in project_path.rglob("*.html"):
            try:
                content = html_file.read_text(encoding="utf-8", errors="ignore")
                if "bootstrap" in content.lower():
                    bootstrap_in_html = True
                    break
            except OSError:
                continue

    if bootstrap_in_deps or bootstrap_in_html:
        detected["Bootstrap"] = SKILL_MAP["Bootstrap"]

    # Tailwind
    if list(project_path.glob("tailwind.config.*")):
        detected["Tailwind"] = SKILL_MAP["Tailwind"]

    # Generic frontend (HTML/CSS files present but no specific framework yet)
    has_html = bool(list(project_path.glob("**/*.html"))[:1])
    has_css = bool(list(project_path.glob("**/*.css"))[:1])
    if (has_html or has_css) and "Frontend" not in detected:
        # Only add generic frontend if no more specific frontend framework detected
        frontend_frameworks = {"React", "Next.js", "Bootstrap", "Tailwind"}
        if not detected.keys() & frontend_frameworks:
            detected["Frontend"] = SKILL_MAP["Frontend"]

    return detected


def print_detection_results(detected: dict[str, list[str]], project_path: Path):
    """Print a clear summary of detected frameworks and relevant skills."""
    print("\n" + "=" * 60)
    print("  STEP 3: Framework Detection")
    print("=" * 60)
    print(f"  Project: {project_path}")

    if not detected:
        print("\n  No specific frameworks detected.")
        print("  All general-purpose skills are available (claude-bootstrap-base, etc.)")
        return

    print(f"\n  Detected stack:")
    for framework in detected:
        print(f"    - {framework}")

    # Collect unique recommended skills
    all_skills: list[str] = []
    for skills in detected.values():
        for s in skills:
            if s not in all_skills:
                all_skills.append(s)

    # Check which recommended skills are actually installed
    installed_skills_dir = Path.home() / ".claude" / "skills"
    print(f"\n  Relevant installed skills:")
    for skill in all_skills:
        installed = (installed_skills_dir / skill).exists()
        status = "INSTALLED" if installed else "NOT FOUND"
        print(f"    [{status}] {skill}")

    # Always mention the base skill
    if "claude-bootstrap-base" not in all_skills:
        base_installed = (installed_skills_dir / "claude-bootstrap-base").exists()
        if base_installed:
            print(f"    [INSTALLED] claude-bootstrap-base (always available)")


# ---------------------------------------------------------------------------
# MAIN
# ---------------------------------------------------------------------------

def main():
    print()
    print("=" * 60)
    print("  AI Engineer Toolkit - Setup")
    print("  by GavinHolder")
    print("=" * 60)

    repo_root = Path(__file__).parent.parent

    # Step 0: Ensure Claude CLI is available
    has_claude = ensure_claude_cli()

    # Step 1: Install skills
    install_skills(repo_root)

    # Step 1b: Install plugins (requires Claude CLI)
    if has_claude:
        install_plugins()
    else:
        print("\n  SKIPPED plugin installation (Claude CLI not available).")

    # Step 1c: Mute JARVIS voice by default (users can enable via jarvis-toggle.py)
    mute_file = Path.home() / ".claude" / "jarvis-muted"
    if not mute_file.exists():
        mute_file.parent.mkdir(parents=True, exist_ok=True)
        mute_file.touch()
        print(f"\n  [MUTED] JARVIS voice disabled by default.")
        print(f"  To enable: python skills/jarvis-voice/jarvis-toggle.py")
    else:
        print(f"\n  JARVIS voice already muted (default). Toggle with jarvis-toggle.py")

    # Step 2: Fix Windows hooks
    fix_windows_hooks()

    # Determine target project directory
    # --init <path> or --detect <path> set the target; otherwise use cwd
    target = Path.cwd()
    if len(sys.argv) > 2 and sys.argv[1] in ("--init", "--detect"):
        target = Path(sys.argv[2]).resolve()
        if not target.exists() or not target.is_dir():
            print(f"\n  ERROR: Directory not found: {target}")
            sys.exit(1)

    # Step 3: Generate CLAUDE.md & memory files
    if target == repo_root:
        print("\n" + "=" * 60)
        print("  CLAUDE.md Generation")
        print("=" * 60)
        print("  You're running from the ai-engineer repo itself.")
        print("  To generate CLAUDE.md for a project, run from that project:")
        print(f"    cd <your-project>")
        print(f"    python \"{repo_root / 'scripts' / 'install-skills.py'}\"")
        print()
        print("  Or pass the project path as argument:")
        print(f"    python scripts/install-skills.py --init <project-path>")
    else:
        generate_claude_md(target)

    # Step 4: Detect frameworks (read-only)
    detected = detect_frameworks(target)
    print_detection_results(detected, target)

    print("\n" + "=" * 60)
    print("  Setup Complete!")
    print("=" * 60)
    print()


if __name__ == "__main__":
    main()
