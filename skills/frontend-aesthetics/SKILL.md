---
name: frontend-aesthetics
description: Comprehensive frontend aesthetics system for producing distinctive, polished UI that avoids generic "AI slop". Automatically applies to all frontend generation tasks. Covers typography, color, motion, backgrounds, layout, and a complete animation library reference with GSAP, Motion, Anime.js, AOS, Lottie, Three.js, tsParticles, Typed.js, Swiper, Locomotive Scroll, Splitting.js, and AutoAnimate.
---

# Frontend Aesthetics System

You tend to converge toward generic, "on distribution" outputs. In frontend design, this creates what users call the "AI slop" aesthetic. Avoid this: make creative, distinctive frontends that surprise and delight.

This skill applies to ALL frontend code generation — HTML, CSS, JS, React, Vue, Svelte, or any UI work.

## Pre-Code Design Thinking

Before writing any code, commit to a BOLD aesthetic direction:

1. **Purpose**: What problem does this interface solve? Who uses it?
2. **Tone**: Pick an extreme — brutally minimal, maximalist chaos, retro-futuristic, organic/natural, luxury/refined, playful/toy-like, editorial/magazine, brutalist/raw, art deco/geometric, soft/pastel, industrial/utilitarian, cyberpunk, solarpunk, Memphis design, Swiss/International, Japanese minimalism, Bauhaus, Victorian, Vaporwave, Nordic, etc.
3. **Differentiation**: What makes this UNFORGETTABLE? What's the one thing someone will remember?
4. **State your choices**: Before coding, explicitly state your font choice, color palette, animation strategy, and aesthetic direction.

## Typography

Typography instantly signals quality. Choose fonts that are beautiful, unique, and distinctive.

### NEVER use
Inter, Roboto, Open Sans, Lato, Arial, Helvetica, default system fonts, or any generic sans-serif.

### Font recommendations by aesthetic

| Aesthetic | Fonts |
|---|---|
| **Code/Terminal** | JetBrains Mono, Fira Code, IBM Plex Mono, Berkeley Mono |
| **Editorial/Literary** | Playfair Display, Crimson Pro, Fraunces, Newsreader, Lora |
| **Startup/Modern** | Clash Display, Satoshi, Cabinet Grotesk, General Sans, Switzer |
| **Technical/Corporate** | IBM Plex Sans, Source Sans 3, Overpass, Manrope |
| **Distinctive/Expressive** | Bricolage Grotesque, Obviously, Syne, Instrument Serif, Outfit |
| **Display/Headlines** | Bebas Neue, Anton, Oswald, Archivo Black, Unbounded |
| **Handwritten/Organic** | Caveat, Patrick Hand, Kalam, Architects Daughter |
| **Geometric** | Poppins variant weights, Outfit, Lexend, Urbanist |
| **Retro** | Press Start 2P, VT323, Silkscreen, DM Serif Display |

### Pairing rules

- **High contrast = interesting.** Display + monospace. Serif + geometric sans. Variable font across weights.
- **Use extremes:** Weight 100/200 vs 800/900, NOT 400 vs 600. Size jumps of 3x+ (e.g. 14px body -> 48px heading), NOT 1.5x.
- **Pick ONE distinctive font** and use it decisively. Load from Google Fonts.
- **Vary across projects:** NEVER converge on the same font (Space Grotesk, DM Sans, etc.) across generations. Each project gets a fresh choice.

### Example font loading

```html
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Bricolage+Grotesque:wght@200;800&family=Instrument+Serif&display=swap" rel="stylesheet">
```

## Color & Theme

### Rules

- **Commit to a cohesive aesthetic.** Every color serves the concept.
- **Use CSS variables** for consistency across the entire interface.
- **Dominant + sharp accent** outperforms timid, evenly-distributed palettes. Pick ONE dominant color and ONE accent. The rest are neutrals.
- **Draw from real sources:** IDE themes (Dracula, Nord, Catppuccin, Gruvbox, Solarized), cultural aesthetics (Japanese wabi-sabi, Scandinavian, Mediterranean), natural palettes (forest, ocean, desert, aurora).
- **Vary between light and dark themes** across projects. Don't always default to dark.

### NEVER use
- Purple gradients on white backgrounds (the quintessential "AI slop" look)
- Generic blue/purple SaaS palettes
- Unsaturated, washed-out "safe" colors
- Rainbow or multi-color schemes without clear intent

### Theme-locking pattern

When building multiple related interfaces, lock in a specific aesthetic:

```css
:root {
  /* Example: Nord-inspired */
  --bg-primary: #2E3440;
  --bg-secondary: #3B4252;
  --text-primary: #ECEFF4;
  --text-secondary: #D8DEE9;
  --accent: #88C0D0;
  --accent-warm: #EBCB8B;
  --danger: #BF616A;
  --surface: #434C5E;
}
```

---

## Animation & Motion — COMPREHENSIVE GUIDE

Every frontend MUST include creative, well-crafted animations. Animation is not optional — it is a core part of the brand experience. Choose the right library for the context and use it deliberately.

### Animation Philosophy

- One well-orchestrated page load with staggered reveals creates MORE delight than scattered micro-interactions
- Every animation must serve the brand — purposeful, not decorative noise
- Spring physics for natural, organic motion; easing curves for precise, designed motion
- Always respect `prefers-reduced-motion` with graceful fallbacks
- Only animate compositor-friendly properties: `transform`, `opacity`, `filter`, `clip-path`
- Keep durations 200ms-600ms for interactions, up to 1.2s for page transitions

### Library Selection Guide

| Need | Library | CDN Size |
|------|---------|----------|
| Complex sequenced animations | **GSAP** | ~30kb |
| Scroll-driven experiences | **GSAP ScrollTrigger** | +8kb |
| React component animations | **Motion** (framer-motion) | ~34kb |
| Lightweight general animation | **Anime.js** | ~17kb |
| Quick scroll reveals (zero JS) | **AOS** | ~14kb |
| Vector/icon animations | **Lottie** | ~60kb light |
| 3D scenes and effects | **Three.js** | ~600kb |
| Particle backgrounds | **tsParticles** | ~15-50kb |
| Typewriter text effects | **Typed.js** | ~5kb |
| Image carousels/sliders | **Swiper.js** | ~40kb |
| Smooth scroll + parallax | **Locomotive Scroll / Lenis** | ~9kb |
| Text splitting for animation | **Splitting.js** | ~1.5kb |
| Zero-config list animations | **AutoAnimate** | ~2kb |

### Creative Combination Patterns

**Pattern 1: Smooth scroll + parallax + text reveals**
Lenis + GSAP ScrollTrigger + SplitText

**Pattern 2: React SPA with rich animations**
Motion + Three.js (3D accents) + Lottie (icons)

**Pattern 3: Marketing landing page**
AOS (quick reveals) + Typed.js (hero text) + Swiper (testimonials) + Lottie (illustrations)

**Pattern 4: Creative portfolio**
GSAP (master timeline) + ScrollTrigger (scroll control) + Splitting.js (text effects) + Three.js (3D hero)

**Pattern 5: Lightweight animated site**
Anime.js (animations) + AutoAnimate (list transitions) + CSS scroll-driven animations

---

### GSAP (GreenSock) — The Gold Standard

ALL plugins are FREE since 2024 (Webflow acquisition). Use GSAP for complex, sequenced, scroll-driven animation.

**CDN:**
```html
<script src="https://cdn.jsdelivr.net/npm/gsap@3/dist/gsap.min.js"></script>
<script src="https://cdn.jsdelivr.net/npm/gsap@3/dist/ScrollTrigger.min.js"></script>
<script src="https://cdn.jsdelivr.net/npm/gsap@3/dist/SplitText.min.js"></script>
<script src="https://cdn.jsdelivr.net/npm/gsap@3/dist/Flip.min.js"></script>
<script src="https://cdn.jsdelivr.net/npm/gsap@3/dist/DrawSVGPlugin.min.js"></script>
<script src="https://cdn.jsdelivr.net/npm/gsap@3/dist/MorphSVGPlugin.min.js"></script>
<script src="https://cdn.jsdelivr.net/npm/gsap@3/dist/MotionPathPlugin.min.js"></script>
<script src="https://cdn.jsdelivr.net/npm/gsap@3/dist/TextPlugin.min.js"></script>
<script src="https://cdn.jsdelivr.net/npm/gsap@3/dist/Observer.min.js"></script>
```

**Core patterns:**
```javascript
// Timeline with stagger
const tl = gsap.timeline({ defaults: { duration: 0.8, ease: "power2.out" } });
tl.from(".hero-title", { y: 60, opacity: 0 })
  .from(".hero-subtitle", { y: 40, opacity: 0 }, "-=0.4")
  .from(".hero-cta", { y: 30, opacity: 0 }, "-=0.3")
  .from(".hero-image", { scale: 0.9, opacity: 0 }, "-=0.5");

// ScrollTrigger batch reveal
gsap.registerPlugin(ScrollTrigger);
ScrollTrigger.batch(".card", {
  onEnter: (els) => gsap.from(els, { opacity: 0, y: 60, stagger: 0.15, duration: 0.8, ease: "power3.out" }),
  once: true
});

// SplitText character reveal
gsap.registerPlugin(SplitText);
const split = new SplitText(".headline", { type: "chars", mask: "lines" });
gsap.from(split.chars, { opacity: 0, y: 50, rotateX: -90, stagger: 0.02, duration: 0.8, ease: "back.out(1.7)" });

// Pinned scroll section
gsap.to(".panels", {
  xPercent: -100 * (panels.length - 1),
  ease: "none",
  scrollTrigger: { trigger: ".panels-container", pin: true, scrub: 1, end: "+=3000" }
});
```

**Easing reference:** `"power1-4.out/in/inOut"`, `"back.out(1.7)"`, `"elastic.out(1,0.3)"`, `"bounce.out"`, `"expo.out"`

**Timeline positions:** `"<"` (same time), `"-=0.3"` (overlap), `"+=0.5"` (gap), `2` (absolute)

**Stagger:** `{ each: 0.1, from: "center", grid: [7,15], ease: "power2.in" }`

---

### Motion (formerly Framer Motion) — React Animation

**NPM:** `npm install motion`
**Import:** `import { motion, AnimatePresence } from "motion/react"`

```jsx
// Staggered list reveal
const container = { hidden: {}, visible: { transition: { staggerChildren: 0.1 } } };
const item = { hidden: { opacity: 0, y: 20 }, visible: { opacity: 1, y: 0, transition: { type: "spring", stiffness: 300 } } };
<motion.ul variants={container} initial="hidden" animate="visible">
  {items.map(i => <motion.li key={i} variants={item}>{i}</motion.li>)}
</motion.ul>

// Layout animations
<motion.div layoutId="hero-image"><img src={img} /></motion.div>

// Scroll-linked parallax
const { scrollYProgress } = useScroll();
const y = useTransform(scrollYProgress, [0, 1], [0, -300]);
<motion.div style={{ y }}>Parallax</motion.div>

// Exit animations
<AnimatePresence mode="wait">
  {show && <motion.div key="modal" initial={{ opacity: 0 }} animate={{ opacity: 1 }} exit={{ opacity: 0 }} />}
</AnimatePresence>
```

**Vanilla JS (non-React):**
```javascript
import { animate, scroll, inView, stagger } from "motion";
animate("li", { opacity: [0, 1], x: [-20, 0] }, { delay: stagger(0.1) });
scroll(animate(".bar", { scaleX: [0, 1] }));
inView(".card", (info) => { animate(info.target, { opacity: 1, y: 0 }); });
```

---

### Anime.js v4 — Lightweight Alternative

**CDN:** `<script src="https://cdn.jsdelivr.net/npm/animejs@4/lib/anime.min.js"></script>`

```javascript
import { animate, stagger, createTimeline, spring } from 'animejs';
animate('.box', { translateX: 250, rotate: '1turn', duration: 800, ease: 'outExpo' });
animate('.grid-item', { scale: [0, 1], delay: stagger(50, { grid: [14, 5], from: 'center' }) });

const tl = createTimeline({ defaults: { duration: 600, ease: 'outExpo' } });
tl.add('.box1', { translateX: 250 }).add('.box2', { translateY: 200 }, '-=400');
```

---

### AOS (Animate on Scroll) — Zero-JS Scroll Reveals

**CDN:**
```html
<link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/aos@2/dist/aos.css">
<script src="https://cdn.jsdelivr.net/npm/aos@2/dist/aos.js"></script>
```

```html
<div data-aos="fade-up" data-aos-duration="800" data-aos-delay="200">Content</div>
<script>AOS.init({ once: true, duration: 800, easing: 'ease-out-cubic' });</script>
```

**All animations:** `fade-up/down/left/right`, `fade-up-right/left`, `flip-up/down/left/right`, `slide-up/down/left/right`, `zoom-in/out` + directional variants.

---

### Lottie — Vector Animations

**CDN:** `<script src="https://cdnjs.cloudflare.com/ajax/libs/lottie-web/5.13.0/lottie_light.min.js"></script>`

```javascript
const anim = lottie.loadAnimation({
  container: document.getElementById('lottie'),
  renderer: 'svg', loop: true, autoplay: true,
  path: '/animations/hero.json'
});
```

**Web component:** `<lottie-player src="animation.json" loop autoplay style="width:300px;height:300px;"></lottie-player>`

**Sources:** LottieFiles (lottiefiles.com), Lordicon (lordicon.com), IconScout

---

### Three.js — 3D Effects

**CDN (import map):**
```html
<script type="importmap">{ "imports": { "three": "https://cdn.jsdelivr.net/npm/three@0.172/build/three.module.js", "three/addons/": "https://cdn.jsdelivr.net/npm/three@0.172/examples/jsm/" } }</script>
```

Use for: 3D product viewers, interactive backgrounds, particle systems, generative art, WebGPU effects.

---

### tsParticles — Particle Effects

**CDN:** `<script src="https://cdn.jsdelivr.net/npm/@tsparticles/slim@3/tsparticles.slim.bundle.min.js"></script>`

```javascript
tsParticles.load({ id: "particles", options: {
  particles: { number: { value: 60 }, color: { value: "#88c0d0" }, links: { enable: true, opacity: 0.3 },
    move: { enable: true, speed: 1.5 }, opacity: { value: 0.5 }, size: { value: { min: 1, max: 4 } } },
  interactivity: { events: { onHover: { enable: true, mode: "repulse" } } }
}});
```

**Also:** Confetti (`@tsparticles/confetti`), Fireworks (`@tsparticles/fireworks`)

---

### Typed.js — Typewriter Effects

**CDN:** `<script src="https://cdn.jsdelivr.net/npm/typed.js@2/dist/typed.umd.js"></script>`

```javascript
new Typed('#typed', {
  strings: ['Build beautiful interfaces.', 'Create amazing experiences.', 'Design with intention.'],
  typeSpeed: 50, backSpeed: 30, backDelay: 1500, loop: true, showCursor: true, cursorChar: '|'
});
```

**Pauses:** `'Wait for it...^1000 BOOM!'` — `^1000` pauses for 1 second.

---

### Swiper.js — Creative Carousels

**CDN:**
```html
<link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/swiper@12/swiper-bundle.min.css">
<script src="https://cdn.jsdelivr.net/npm/swiper@12/swiper-bundle.min.js"></script>
```

**Effects:** `'fade'`, `'cube'`, `'coverflow'`, `'flip'`, `'cards'`, `'creative'`

```javascript
new Swiper('.swiper', {
  effect: 'coverflow', centeredSlides: true, slidesPerView: 'auto', loop: true, grabCursor: true,
  coverflowEffect: { rotate: 50, stretch: 0, depth: 100, modifier: 1, slideShadows: true },
  pagination: { el: '.swiper-pagination', clickable: true },
  autoplay: { delay: 3000, disableOnInteraction: false }
});
```

---

### Locomotive Scroll / Lenis — Smooth Scrolling

**Lenis CDN:** `<script src="https://cdn.jsdelivr.net/npm/lenis@latest/dist/lenis.min.js"></script>`

```javascript
const lenis = new Lenis({ duration: 1.2, smoothWheel: true });
function raf(time) { lenis.raf(time); requestAnimationFrame(raf); }
requestAnimationFrame(raf);

// With GSAP (recommended)
gsap.ticker.add((time) => { lenis.raf(time * 1000); });
gsap.ticker.lagSmoothing(0);
```

**HTML parallax:** `<div data-scroll data-scroll-speed="2">Fast parallax</div>`

---

### Splitting.js — Text Animation Utility

**CDN:**
```html
<link rel="stylesheet" href="https://unpkg.com/splitting/dist/splitting.css">
<script src="https://unpkg.com/splitting/dist/splitting.min.js"></script>
```

```html
<h1 data-splitting>Hello World</h1>
<script>Splitting();</script>
```

**CSS-only animation using generated variables:**
```css
.splitting .char {
  opacity: 0; transform: translateY(20px);
  animation: charReveal 0.5s cubic-bezier(0.16, 1, 0.3, 1) both;
  animation-delay: calc(var(--char-index) * 0.03s);
}
@keyframes charReveal { to { opacity: 1; transform: translateY(0); } }
```

---

### AutoAnimate — Zero-Config List Animations

**CDN:** `<script type="module">import autoAnimate from 'https://cdn.jsdelivr.net/npm/@formkit/auto-animate@0.9.0/index.mjs';</script>`

```javascript
autoAnimate(document.getElementById('list'));
// That's it. Adding, removing, or reordering children will animate automatically.
```

**React:** `const [parent] = useAutoAnimate(); <ul ref={parent}>...</ul>`

---

### Native CSS Animation Techniques

**Scroll-driven animations (no JS):**
```css
.progress { animation: grow linear both; animation-timeline: scroll(); }
@keyframes grow { from { transform: scaleX(0); } to { transform: scaleX(1); } }

.reveal { animation: fadeIn linear both; animation-timeline: view(); animation-range: entry 0% entry 100%; }
@keyframes fadeIn { from { opacity: 0; transform: translateY(50px); } to { opacity: 1; transform: translateY(0); } }
```

**@starting-style (entry animations):**
```css
.dialog { opacity: 1; transition: opacity 0.3s; @starting-style { opacity: 0; } }
```

**Path-based motion:**
```css
.element { offset-path: path('M 0 0 C 100 200, 300 0, 400 200'); animation: followPath 3s ease-in-out infinite; }
@keyframes followPath { 0% { offset-distance: 0%; } 100% { offset-distance: 100%; } }
```

---

### Animation Performance Rules

```css
/* Only animate compositor-friendly properties */
/* FAST: transform, opacity, filter, clip-path */
/* SLOW: width, height, top, left, margin, padding */

.animated { will-change: transform, opacity; }

@media (prefers-reduced-motion: reduce) {
  *, *::before, *::after {
    animation-duration: 0.01ms !important;
    transition-duration: 0.01ms !important;
    scroll-behavior: auto !important;
  }
}
```

---

## Backgrounds & Atmosphere

Create atmosphere and depth. NEVER default to plain solid colors.

### Techniques

- **Layered CSS gradients** — radial, conic, and linear combined
- **Geometric patterns** — repeating SVG, CSS grid patterns, dot grids
- **Noise/grain textures** — SVG filters or CSS backdrop-filter
- **Gradient meshes** — multiple radial gradients at different positions
- **Contextual effects** — match the subject matter (code = terminal green glow, finance = subtle grid, creative = paint splatter)

### Example: Atmospheric gradient mesh background

```css
body {
  background:
    radial-gradient(ellipse at 20% 50%, rgba(120, 80, 200, 0.15) 0%, transparent 50%),
    radial-gradient(ellipse at 80% 20%, rgba(80, 200, 180, 0.12) 0%, transparent 50%),
    radial-gradient(ellipse at 50% 80%, rgba(200, 120, 80, 0.1) 0%, transparent 50%),
    #0a0a0a;
}
```

### Example: Subtle noise texture overlay

```css
body::before {
  content: '';
  position: fixed;
  inset: 0;
  background-image: url("data:image/svg+xml,%3Csvg viewBox='0 0 256 256' xmlns='http://www.w3.org/2000/svg'%3E%3Cfilter id='n'%3E%3CfeTurbulence type='fractalNoise' baseFrequency='0.9' numOctaves='4' stitchTiles='stitch'/%3E%3C/filter%3E%3Crect width='100%25' height='100%25' filter='url(%23n)' opacity='0.04'/%3E%3C/svg%3E");
  pointer-events: none;
  z-index: 9999;
}
```

## Spatial Composition & Layout

- **Unexpected layouts.** Asymmetry. Overlap. Diagonal flow. Grid-breaking elements.
- **Generous negative space** OR controlled density — both work, but commit to one.
- Don't default to centered-everything card layouts.
- Use CSS Grid for complex, editorial-style layouts.
- Overlapping elements with `z-index` and negative margins create visual interest.
- Full-bleed sections alternating with contained content creates rhythm.

## Anti-Patterns Checklist

Before outputting any frontend code, verify you have NOT fallen into these traps:

- [ ] Generic font (Inter, Roboto, Arial, system-ui)
- [ ] Purple gradient on white background
- [ ] Everything centered in cards with uniform rounded corners
- [ ] No animations or only basic fade-in
- [ ] Flat solid color backgrounds with no depth
- [ ] Predictable symmetric layout
- [ ] Same font/palette as your last generation
- [ ] Timid, evenly-distributed color palette
- [ ] Safe, forgettable design that could be any website
- [ ] No scroll-triggered animations for below-the-fold content
- [ ] Missing page load animation sequence
- [ ] No hover/interaction micro-feedback
- [ ] Animation without purpose (decorative noise)

If ANY box is checked, go back and make a bolder choice.

## Output Quality

Every frontend output must be:
- **Production-grade** — working, responsive, accessible
- **Visually striking** — someone should stop and look twice
- **Cohesive** — every element serves the aesthetic vision
- **Distinctive** — genuinely different from the last thing you generated
- **Animated** — purposeful motion that reinforces the brand
- **Complete** — all CSS and JS inline for standalone HTML; proper imports for framework code

Match implementation complexity to the aesthetic vision. Maximalist designs need elaborate code with GSAP timelines and ScrollTrigger. Minimalist designs need precision with subtle CSS transitions. The key is intentionality, not intensity.
