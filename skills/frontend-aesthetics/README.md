# Frontend Aesthetics Skill

A design system that pushes Claude to create distinctive, polished UI instead of generic "AI slop" aesthetics.

## What It Does

Automatically applies to all frontend code generation (HTML, CSS, JS, React, Vue, Svelte) and enforces:

- **Pre-code design thinking**: Choose a bold aesthetic direction before writing any code
- **Typography**: Font pairing rules, scale, weight hierarchy, letter-spacing
- **Color theory**: Palette creation, contrast ratios, accent usage, dark mode
- **Motion & animation**: Meaningful transitions, micro-interactions, scroll effects
- **Backgrounds**: Gradients, textures, glassmorphism, layered effects
- **Layout**: Spacing rhythm, visual hierarchy, whitespace usage
- **Anti-slop checklist**: Catches generic patterns and pushes for distinctiveness

### Animation Library Reference

Includes usage guides for 12 animation libraries:
GSAP, Motion (Framer Motion), Anime.js, AOS, Lottie, Three.js, tsParticles, Typed.js, Swiper, Locomotive Scroll (Lenis), Splitting.js, and AutoAnimate.

## Plugin Relationship

This is a **custom skill** - there is no default aesthetics plugin in Claude Code. It was created based on [Anthropic's Coding Prompting for Frontend Aesthetics](https://platform.claude.com/cookbook/coding-prompting-for-frontend-aesthetics) cookbook to prevent generic "AI slop" UI output. The `frontend-design` plugin from `anthropics/claude-plugins-official` handles layout and structure - this skill complements it with aesthetic quality.

## How to Use

### Automatic (recommended)
This skill activates automatically when you're doing any frontend work:
```
"Build me a landing page"
"Create a dashboard with charts"
"Design a pricing page"
```

### Slash Command
```
/frontend-aesthetics
```

## Files

| File | Purpose |
|---|---|
| `SKILL.md` | Full aesthetics system: typography, color, motion, backgrounds, layout, animation library reference, anti-slop checklist |

## Installation

Installed automatically by `install-skills.py`. Copies to `~/.claude/skills/frontend-aesthetics/`.
