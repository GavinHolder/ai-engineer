---
name: visual-debugging
description: Visual debugging and design discovery using Playwright browser automation. Use when debugging UI issues, inspecting reference websites, testing responsive layouts, or when the user wants to build something "like" another site.
---

# Visual Debugging & Design Discovery

Use Playwright browser automation to **see** what you're building or researching. This skill activates when text-based debugging isn't enough and visual context would help.

## Prerequisites

The Playwright MCP plugin is installed automatically by `install-skills.py`. If missing, install manually:
```
/plugin install playwright from anthropics/claude-plugins-official
```

This provides browser automation tools via `npx @playwright/mcp@latest`.

---

## When to Use Visual Debugging

### Automatic Triggers

Activate this workflow when any of these conditions are met:

1. **UI debugging fails after initial attempt** - You've tried fixing a visual bug from code alone but can't resolve it
2. **User describes a UI they want but you lack context** - "Make it look like..." or "I want something similar to..."
3. **User references another website** - "Like the navbar on [site]" or "Similar to how [site] does their pricing page"
4. **Building creative UI that benefits from reference** - Landing pages, dashboards, complex layouts where seeing real examples helps
5. **Need to verify responsive behavior** - Checking how a page looks at different viewport sizes
6. **Visual regression check** - Confirming a change didn't break the layout

### Do NOT Use When

- The issue is purely logic/data (no visual component)
- Simple CSS tweaks where the fix is obvious from code
- The user hasn't provided or approved a URL to inspect

---

## Playwright MCP Tools Reference

| Tool | What It Does | Example Use |
|------|-------------|-------------|
| `browser_navigate` | Go to a URL | Navigate to a reference site or local dev server |
| `browser_screenshot` | Capture current viewport | See what the page actually looks like |
| `browser_click` | Click an element | Interact with dropdowns, modals, nav menus |
| `browser_fill` | Fill form fields | Test form layouts with real data |
| `browser_snapshot` | Get accessibility tree | Structured DOM inspection without visual |
| `browser_resize` | Change viewport dimensions | Test responsive breakpoints |

---

## Workflow Patterns

### 1. Visual Discovery (Inspecting Reference Sites)

**When:** User wants something "like" another site, or you need design inspiration.

```
Step 1: Ask user for the reference URL(s)
Step 2: browser_navigate to the URL
Step 3: browser_screenshot to capture the design
Step 4: Analyze the screenshot - extract:
        - Layout structure (grid, flexbox patterns)
        - Color palette (primary, secondary, accent, background)
        - Typography (font families, sizes, weights, spacing)
        - Spacing and whitespace patterns
        - Animation/interaction patterns (if visible)
        - Component patterns (cards, navbars, heroes, CTAs)
Step 5: browser_snapshot for structured DOM details
Step 6: Summarize findings and apply to the build
```

**Ask the user before navigating to any URL.** Never navigate to sites without permission.

### 2. Visual Debugging (Fix What You Can See)

**When:** A UI bug persists after code-level debugging.

```
Step 1: Confirm the dev server URL with the user (usually localhost:3000 or similar)
Step 2: browser_navigate to the dev server
Step 3: browser_screenshot to see current state
Step 4: Compare screenshot against expected design
Step 5: Identify the visual discrepancy
Step 6: Fix the code
Step 7: browser_screenshot again to verify the fix
```

### 3. Responsive Testing

**When:** Need to verify layout at different screen sizes.

```
Step 1: Navigate to the page
Step 2: Test at key breakpoints:
        - Mobile:  browser_resize(375, 812)   -- iPhone viewport
        - Tablet:  browser_resize(768, 1024)   -- iPad viewport
        - Desktop: browser_resize(1440, 900)   -- Standard desktop
Step 3: browser_screenshot at each size
Step 4: Identify layout issues (overflow, stacking, hidden elements)
Step 5: Fix responsive CSS and re-verify
```

### 4. Design Audit (Competitive/Reference Analysis)

**When:** Building a new feature and want to see how others handle it.

```
Step 1: Ask user for 2-3 reference URLs
Step 2: Screenshot each site at the relevant section
Step 3: Compare approaches - note what works and what doesn't
Step 4: Synthesize a design approach that draws from the best patterns
Step 5: Present findings to user before building
```

---

## Best Practices

- **Always ask before navigating** - Get user permission for any URL
- **Screenshot first, then inspect** - Visual context before DOM diving
- **Note specific design tokens** - Extract actual colors, font sizes, spacing values
- **Test at multiple viewports** - Don't assume desktop-only
- **Before/after screenshots** - When fixing bugs, capture both states
- **Keep it focused** - Screenshot the relevant section, not entire pages when possible
- **Summarize visually** - After inspecting, tell the user what you found in plain language

---

## Integration with Other Skills

Visual debugging works alongside other frontend skills:

- **frontend-aesthetics** - Use visual discovery to inform typography, color, and animation choices
- **bootstrap-5** / **css3** - Verify component rendering matches expectations
- **modern-ui-ux** - Capture reference patterns for scroll storytelling, 3D effects, etc.
- **frontend-design** - Ground creative design work in real-world reference
