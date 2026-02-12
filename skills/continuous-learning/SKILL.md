---
name: continuous-learning
description: Automatic knowledge extraction and skill improvement system. Activates after task completions, debugging sessions, and checkpoints. Writes learned knowledge as individual files inside each skill's learned/ folder. Inspired by Claudeception.
---

# Continuous Learning System

Extract and persist knowledge from every work session. Each piece of learned knowledge becomes its own small file inside the relevant skill's `learned/` folder.

## Golden Rule

**Every completed task list is a learning opportunity.** After finishing a set of tasks, extract what was learned and write it down. This is not optional.

---

## When to Extract Knowledge

### Automatic Triggers

1. **After every task list completion** - Review what was done, extract patterns
2. **After debugging sessions** - Non-obvious solutions, misleading errors
3. **At checkpoints** (every 5-10 tasks) - Pause, reflect, write learnings
4. **After discovering workarounds** - Things that weren't in docs
5. **After user corrections** - "Use X instead of Y" type feedback
6. **After configuration insights** - Settings, environment, tooling quirks

### Quality Filter

Only extract knowledge that is:
- **Reusable** - Applicable to future tasks, not just this one
- **Non-trivial** - Required discovery, not a docs lookup
- **Specific** - Clear trigger conditions and exact solutions
- **Verified** - Actually worked, not theoretical

Do NOT extract:
- Basic syntax or API usage (that's what skill references are for)
- One-off project-specific fixes with no broader application
- Unverified guesses

---

## Where to Write Learnings

### Per-Skill Learned Folders

Each skill has a `learned/` subfolder. Knowledge goes into the skill it relates to:

```
~/.claude/skills/
  react-19/
    SKILL.md
    learned/
      hook-ordering-in-concurrent-mode.md
      server-component-data-fetching-gotcha.md
  bootstrap-5/
    SKILL.md
    learned/
      modal-z-index-conflict-with-offcanvas.md
  django-python/
    SKILL.md
    learned/
      celery-task-retry-with-countdown.md
      drf-pagination-with-filters.md
```

### File Naming

- Use kebab-case descriptive names
- Name describes the problem/pattern, not the solution
- Max 60 chars in filename
- Extension: `.md`

### General Learnings

For knowledge that doesn't fit a specific skill, write to:
```
~/.claude/skills/continuous-learning/learned/
  git-worktree-branch-cleanup.md
  windows-path-length-issues.md
```

---

## Learning File Format

Each file is small and focused. One topic per file. Use this structure:

```markdown
# [Short descriptive title]

**Discovered:** YYYY-MM-DD
**Context:** [What task/project triggered this]
**Skill:** [Which skill this relates to]

## Problem
[What went wrong or was non-obvious]

## Solution
[The fix or pattern that worked]

## Why
[Why this happens - root cause understanding]

## Remember
[One-line takeaway for quick scanning]
```

### Example

```markdown
# React useEffect cleanup runs on every re-render in Strict Mode

**Discovered:** 2026-02-12
**Context:** Building dashboard with WebSocket connections
**Skill:** react-19

## Problem
WebSocket connections were doubling in development. useEffect cleanup
was running unexpectedly, then the effect re-ran, creating two connections.

## Solution
React 18+ Strict Mode intentionally double-invokes effects in dev.
Use a ref to track connection state:
const connectedRef = useRef(false)

## Why
Strict Mode does this to surface cleanup bugs early. Production
only runs effects once. The ref pattern ensures idempotent connections.

## Remember
Strict Mode double-fires effects in dev. Use refs for connection tracking.
```

---

## Learning Workflow

### After Task List Completion

```
1. Review completed tasks
2. For each task, ask: "Did I discover anything non-obvious?"
3. If yes, write a learning file to the relevant skill's learned/ folder
4. Create the learned/ folder if it doesn't exist
5. Log a summary of learnings extracted
```

### At Checkpoints (Every 5-10 Tasks)

```
1. Pause current work
2. Review tasks since last checkpoint
3. Extract any learnings missed during task completion
4. Update session changelog with learnings count
5. Resume work
```

### After User Corrections

When the user says something like "don't do X, do Y instead":
```
1. Immediately write a learning file
2. File goes in the most relevant skill's learned/ folder
3. Title should capture the correction clearly
4. Include both the wrong approach and the correct one
```

---

## Reinforcement

### Session Start

At the start of each session, scan `learned/` folders in active skills for recent learnings. Apply them proactively - don't wait to rediscover the same issues.

### Skill Loading

When a skill is loaded (e.g., react-19 for a React project), its `learned/` folder contents are part of the skill's context. Learnings are automatically available.

---

## File Size Management

- **Each learning file: 10-30 lines max.** If it's longer, split into multiple files.
- **No monolithic learning files.** One topic per file, always.
- **Prune stale learnings.** If a learning is outdated (library updated, pattern changed), delete the file.
- **Merge duplicates.** If two learnings cover the same topic, combine into one clean file.

---

## Integration with Task Protocol

The task protocol requires:
1. **Tasks for everything** - no exceptions
2. **Checkpoints every 5-10 tasks** - includes learning extraction
3. **Learning after every task list completion** - mandatory review
4. **Reinforcement** - apply learned knowledge in future tasks

This skill ensures the learning step never gets skipped.
