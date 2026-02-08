#!/usr/bin/env python3
"""
AI Engineer Toolkit - Skill Installer & Environment Setup

1. Copies enhanced/custom skills from repo to ~/.claude/skills/
2. Fixes Windows hook compatibility (python3 -> python)
3. Generates project CLAUDE.md with full session management framework

Usage:
    python install-skills.py
"""

import json
import os
import platform
import re
import shutil
import sys
from datetime import datetime, timezone
from pathlib import Path


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
# 3. CLAUDE.MD GENERATION
# ---------------------------------------------------------------------------

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

## Task Management Protocol

### Hierarchical Numbering (5 Levels Max)

```
1. Main Task (Level 1)
   1.1 Subtask (Level 2)
       1.1.1 Sub-subtask (Level 3)
             1.1.1.1 Detail task (Level 4)
                     1.1.1.1.1 Granular task (Level 5 - max)
```

### Deviation Handling

When issues are discovered mid-task, use letter suffixes:
```
1. Main Task
   1.1 Subtask [IN PROGRESS]
   DEVIATION 1.1.a: Bug discovered in X
       1.1.a.1 Investigate root cause
       1.1.a.2 Fix implementation
       1.1.a.3 Verify fix with tests
   1.2 Continue original plan
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

1. **Classify risk level** (Level 1-4)
2. **Plan first** - Use `/writing-plans` or `/brainstorming` for Level 2+
3. **For Level 3+**: Run `/adversarial-review` before coding
4. **Write tests first** (TDD for Level 2+)
5. **Implement** - Follow code style rules below
6. **Verify** - Run full test suite, lint, typecheck
7. **Review** - `/requesting-code-review` for Level 2+
8. **Update memory** - Log to changelog, extract patterns

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

TASK_PROTOCOL_TEMPLATE = """# Hierarchical Task Management Protocol

**Version:** 2.0 (Enhanced)
**Created:** {timestamp}
**Max Depth:** 5 levels

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

## Deviation Handling

When issues are discovered mid-task, use letter suffixes:

```
1. Main Task
   1.1 Subtask [IN PROGRESS]
   DEVIATION 1.1.a: Bug discovered in X
       1.1.a.1 Investigate root cause
       1.1.a.2 Fix implementation
       1.1.a.3 Verify fix with tests
   1.2 Continue original plan
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
[!] DEVIATION - issue discovered, deviation branch created
[-] BLOCKED - waiting on dependency
[X] FAILED - requires replanning
[#] CHECKPOINT
```

---

## When to Create Subtasks

**Create subtasks when:**
- Main task has >3 distinct steps
- Task touches >3 files
- Task is Level 3+ (critical logic, integrations)

**Keep flat when:**
- Task is single-step
- Task is trivial (doc update, formatting)

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

**This protocol is active for all sessions.**
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
    """Generate CLAUDE.md and memory files for a project."""
    print("\n" + "=" * 60)
    print("  STEP 3: Generating CLAUDE.md & Memory Files")
    print("=" * 60)

    claude_md_path = project_root / "CLAUDE.md"
    memory_dir = project_root / ".claude" / "memory"

    if claude_md_path.exists():
        print(f"  CLAUDE.md already exists at {claude_md_path}")
        print("  Skipping generation (will not overwrite).")
        print("  To regenerate, delete CLAUDE.md first.")
        return

    project_name = project_root.name
    timestamp = datetime.now(timezone.utc).strftime("%Y-%m-%d %H:%M:%S UTC")

    # Create CLAUDE.md
    content = CLAUDE_MD_TEMPLATE.format(
        project_name=project_name,
        timestamp=timestamp,
    )
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
# MAIN
# ---------------------------------------------------------------------------

def main():
    print()
    print("=" * 60)
    print("  AI Engineer Toolkit - Setup")
    print("  by GavinHolder")
    print("=" * 60)

    repo_root = Path(__file__).parent

    # Step 1: Install skills
    install_skills(repo_root)

    # Step 2: Fix Windows hooks
    fix_windows_hooks()

    # Step 3: Generate CLAUDE.md (in current working directory)
    cwd = Path.cwd()
    if cwd == repo_root:
        print("\n" + "=" * 60)
        print("  STEP 3: CLAUDE.md Generation")
        print("=" * 60)
        print("  You're running from the ai-engineer repo itself.")
        print("  To generate CLAUDE.md for a project, run from that project:")
        print(f"    cd <your-project>")
        print(f"    python \"{repo_root / 'install-skills.py'}\"")
        print()
        print("  Or pass the project path as argument:")
        print(f"    python install-skills.py --init <project-path>")
    else:
        generate_claude_md(cwd)

    # Handle --init argument
    if len(sys.argv) > 2 and sys.argv[1] == "--init":
        target = Path(sys.argv[2]).resolve()
        if target.exists() and target.is_dir():
            generate_claude_md(target)
        else:
            print(f"\n  ERROR: Directory not found: {target}")

    print("\n" + "=" * 60)
    print("  Setup Complete!")
    print("=" * 60)
    print()


if __name__ == "__main__":
    main()
