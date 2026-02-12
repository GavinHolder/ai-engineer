---
name: css3
description: Comprehensive modern CSS reference covering Flexbox, Grid, custom properties, container queries, :has(), nesting, layers, scroll-driven animations, view transitions, subgrid, color functions, and all modern CSS features. Use this skill for ALL CSS work.
---

# Modern CSS — Complete Reference & Patterns

---

## Selectors

### Basic Selectors

```css
*                   /* Universal */
element             /* Type: div, p, h1 */
.class              /* Class */
#id                 /* ID */
[attr]              /* Has attribute */
[attr="value"]      /* Exact match */
[attr~="value"]     /* Space-separated list contains */
[attr|="value"]     /* Starts with value or value- */
[attr^="value"]     /* Starts with */
[attr$="value"]     /* Ends with */
[attr*="value"]     /* Contains */
[attr="v" i]        /* Case-insensitive */
```

### Combinators

```css
A B                 /* Descendant (any depth) */
A > B               /* Direct child */
A + B               /* Adjacent sibling (immediately after) */
A ~ B               /* General sibling (any after) */
```

### Pseudo-classes

```css
/* State */
:hover              :focus              :focus-visible
:focus-within       :active             :visited
:target             :checked            :disabled
:enabled            :required           :optional
:valid              :invalid            :in-range
:out-of-range       :placeholder-shown  :default
:read-only          :read-write         :autofill
:indeterminate      :empty

/* Structural */
:first-child        :last-child         :only-child
:nth-child(n)       :nth-last-child(n)  :nth-of-type(n)
:first-of-type      :last-of-type       :only-of-type

/* Modern */
:is(selector, ...)       /* Matches any — forgiving list */
:where(selector, ...)    /* Same as :is() but zero specificity */
:not(selector)           /* Negation */
:has(selector)           /* Parent selector — match if contains */

/* Functional */
:nth-child(2n)           /* Even */
:nth-child(2n+1)         /* Odd */
:nth-child(3n)           /* Every 3rd */
:nth-child(-n+3)         /* First 3 */
:nth-child(n+4)          /* From 4th onward */
:nth-child(n+2):nth-child(-n+5)  /* Range: 2nd to 5th */
```

### :has() — Parent/Relational Selector

```css
/* Style parent based on children */
.card:has(img)          { padding-top: 0; }
.card:has(.badge)       { border: 2px solid gold; }

/* Style sibling based on other sibling */
h2:has(+ p)             { margin-bottom: 0.5rem; }

/* Form field styling based on state */
.field:has(:invalid)    { border-color: red; }
.field:has(:focus)      { outline: 2px solid blue; }

/* Conditional layout */
.grid:has(> :nth-child(4)) { grid-template-columns: repeat(2, 1fr); }

/* Style body based on presence of element */
body:has(.modal[open])  { overflow: hidden; }
```

### :is() and :where()

```css
/* :is() — matches any, uses highest specificity in list */
:is(h1, h2, h3) { color: navy; }
:is(.card, .panel) > :is(h2, h3) { margin-top: 0; }

/* :where() — same matching, zero specificity (easy to override) */
:where(h1, h2, h3) { margin-bottom: 1rem; }
```

### Pseudo-elements

```css
::before              /* Insert before content */
::after               /* Insert after content */
::first-line          /* First line of text */
::first-letter        /* First letter */
::placeholder         /* Input placeholder text */
::selection           /* User-selected text */
::marker              /* List bullet/number */
::backdrop            /* Behind dialog/fullscreen */
::file-selector-button /* File input button */
```

---

## CSS Nesting (Native)

```css
/* Parent context */
.card {
  padding: 1rem;

  /* Nested child */
  .title {
    font-size: 1.5rem;
  }

  /* Nested pseudo-class */
  &:hover {
    box-shadow: 0 4px 12px rgba(0,0,0,0.1);
  }

  /* Nested media query */
  @media (width >= 768px) {
    padding: 2rem;
  }

  /* Nested pseudo-element */
  &::before {
    content: '';
  }

  /* Compound selector (& required when not starting with symbol) */
  & + & {
    margin-top: 1rem;
  }

  /* Nest deeper */
  .body {
    .text {
      line-height: 1.6;
    }
  }
}
```

---

## Custom Properties (CSS Variables)

```css
/* Define on :root for global scope */
:root {
  --color-primary: #3b82f6;
  --color-primary-rgb: 59, 130, 246;
  --spacing-sm: 0.5rem;
  --spacing-md: 1rem;
  --spacing-lg: 2rem;
  --radius: 0.5rem;
  --font-sans: 'Inter', system-ui, sans-serif;
  --shadow-md: 0 4px 6px -1px rgba(0,0,0,0.1);
  --transition-fast: 150ms ease;
}

/* Use with var() */
.card {
  padding: var(--spacing-md);
  border-radius: var(--radius);
  font-family: var(--font-sans);
  box-shadow: var(--shadow-md);
  background: rgba(var(--color-primary-rgb), 0.1);
}

/* Fallback value */
.element {
  color: var(--accent, #333);
}

/* Scoped override */
.dark-section {
  --color-primary: #60a5fa;
}

/* Dynamic with calc() */
.container {
  --cols: 3;
  grid-template-columns: repeat(var(--cols), 1fr);
}

/* Toggle pattern (space toggle hack) */
:root {
  --dark: ;
  --light: initial;
}
[data-theme="dark"] {
  --dark: initial;
  --light: ;
}
.text {
  color: var(--dark, white) var(--light, black);
}
```

---

## Flexbox

### Container Properties

```css
.flex-container {
  display: flex;            /* or inline-flex */

  /* Direction */
  flex-direction: row;      /* row | row-reverse | column | column-reverse */

  /* Wrapping */
  flex-wrap: nowrap;        /* nowrap | wrap | wrap-reverse */

  /* Shorthand */
  flex-flow: row wrap;

  /* Main axis alignment */
  justify-content: flex-start;
  /* flex-start | flex-end | center | space-between | space-around | space-evenly */

  /* Cross axis alignment */
  align-items: stretch;
  /* stretch | flex-start | flex-end | center | baseline */

  /* Multi-line cross axis */
  align-content: flex-start;
  /* flex-start | flex-end | center | space-between | space-around | stretch */

  /* Gap */
  gap: 1rem;               /* row-gap and column-gap */
  row-gap: 1rem;
  column-gap: 2rem;
}
```

### Item Properties

```css
.flex-item {
  /* Growth factor (how much extra space to take) */
  flex-grow: 0;

  /* Shrink factor (how much to shrink when space is tight) */
  flex-shrink: 1;

  /* Base size before growing/shrinking */
  flex-basis: auto;

  /* Shorthand: grow shrink basis */
  flex: 1;              /* flex: 1 1 0% — grow equally */
  flex: 0 0 300px;      /* fixed 300px, no grow/shrink */
  flex: none;           /* flex: 0 0 auto */

  /* Override align-items for this item */
  align-self: center;

  /* Ordering */
  order: 0;             /* default 0, lower = first */
}
```

### Common Flexbox Patterns

```css
/* Center everything */
.center {
  display: flex;
  justify-content: center;
  align-items: center;
}

/* Sticky footer */
body {
  display: flex;
  flex-direction: column;
  min-height: 100vh;
}
main { flex: 1; }

/* Space between with wrap */
.toolbar {
  display: flex;
  justify-content: space-between;
  align-items: center;
  flex-wrap: wrap;
  gap: 1rem;
}

/* Holy grail layout */
.layout {
  display: flex;
}
.sidebar { flex: 0 0 250px; }
.content { flex: 1; }
```

---

## Grid

### Container Properties

```css
.grid-container {
  display: grid;              /* or inline-grid */

  /* Define columns */
  grid-template-columns: 200px 1fr 200px;
  grid-template-columns: repeat(3, 1fr);
  grid-template-columns: repeat(auto-fill, minmax(250px, 1fr));
  grid-template-columns: repeat(auto-fit, minmax(250px, 1fr));

  /* Define rows */
  grid-template-rows: auto 1fr auto;

  /* Implicit rows (auto-created) */
  grid-auto-rows: minmax(100px, auto);
  grid-auto-columns: 1fr;

  /* Flow direction for auto-placed items */
  grid-auto-flow: row;       /* row | column | row dense | column dense */

  /* Gap */
  gap: 1rem;
  row-gap: 1rem;
  column-gap: 2rem;

  /* Alignment */
  justify-items: stretch;    /* start | end | center | stretch */
  align-items: stretch;      /* start | end | center | stretch | baseline */
  place-items: center;       /* shorthand: align-items justify-items */

  justify-content: start;    /* start | end | center | space-between | space-around | space-evenly */
  align-content: start;      /* same values */
  place-content: center;     /* shorthand */
}
```

### Item Properties

```css
.grid-item {
  /* Placement by line number */
  grid-column: 1 / 3;        /* start-line / end-line */
  grid-row: 1 / 2;

  /* Span */
  grid-column: span 2;       /* span 2 columns */
  grid-row: span 3;

  /* Shorthand */
  grid-column-start: 1;
  grid-column-end: 3;
  grid-row-start: 1;
  grid-row-end: 2;

  /* Area placement */
  grid-area: header;

  /* Self-alignment */
  justify-self: center;
  align-self: end;
  place-self: center end;
}
```

### Named Grid Areas

```css
.layout {
  display: grid;
  grid-template-columns: 250px 1fr 250px;
  grid-template-rows: auto 1fr auto;
  grid-template-areas:
    "header  header  header"
    "sidebar content aside"
    "footer  footer  footer";
  min-height: 100vh;
}

.header  { grid-area: header; }
.sidebar { grid-area: sidebar; }
.content { grid-area: content; }
.aside   { grid-area: aside; }
.footer  { grid-area: footer; }
```

### Subgrid

```css
.parent {
  display: grid;
  grid-template-columns: repeat(3, 1fr);
  gap: 1rem;
}

.child {
  grid-column: span 3;
  display: grid;
  grid-template-columns: subgrid;  /* Inherit parent's column tracks */
  /* grid-template-rows: subgrid; — also works for rows */
}
```

### Grid Functions

```css
/* minmax — clamp track size */
grid-template-columns: minmax(200px, 1fr) 2fr;

/* repeat — shorthand for repeated tracks */
grid-template-columns: repeat(3, 1fr);

/* auto-fill — create as many tracks as fit */
grid-template-columns: repeat(auto-fill, minmax(250px, 1fr));

/* auto-fit — like auto-fill but collapses empty tracks */
grid-template-columns: repeat(auto-fit, minmax(250px, 1fr));

/* fit-content — track grows to content, capped at argument */
grid-template-columns: fit-content(300px) 1fr;
```

### Common Grid Patterns

```css
/* Responsive card grid */
.card-grid {
  display: grid;
  grid-template-columns: repeat(auto-fill, minmax(300px, 1fr));
  gap: 1.5rem;
}

/* Masonry-like (dense packing) */
.masonry {
  display: grid;
  grid-template-columns: repeat(auto-fill, minmax(200px, 1fr));
  grid-auto-rows: 10px;
  grid-auto-flow: dense;
}

/* Full-bleed layout */
.full-bleed {
  display: grid;
  grid-template-columns:
    1fr
    min(65ch, 100% - 2rem)
    1fr;
}
.full-bleed > * { grid-column: 2; }
.full-bleed > .full-width { grid-column: 1 / -1; }

/* Sidebar layout (intrinsic) */
.with-sidebar {
  display: grid;
  grid-template-columns: fit-content(300px) minmax(50%, 1fr);
}
```

---

## Container Queries

```css
/* Define a containment context */
.card-wrapper {
  container-type: inline-size;   /* Track inline (width) size */
  container-name: card;          /* Optional name */
  /* Shorthand: container: card / inline-size; */
}

/* Query the container */
@container card (min-width: 400px) {
  .card {
    display: grid;
    grid-template-columns: 200px 1fr;
  }
}

@container (min-width: 600px) {
  .card { font-size: 1.2rem; }
}

/* Container query units */
.element {
  font-size: 5cqi;     /* 5% of container inline size */
  padding: 2cqb;       /* 2% of container block size */
  /* cqi, cqb, cqw, cqh, cqmin, cqmax */
}
```

---

## Modern Color Functions

```css
/* Relative color syntax (modify existing colors) */
.element {
  --base: #3b82f6;
  color: oklch(from var(--base) l c h);
  background: oklch(from var(--base) calc(l + 0.2) c h);      /* Lighter */
  border-color: oklch(from var(--base) calc(l - 0.1) c h);    /* Darker */
  box-shadow: 0 4px 12px oklch(from var(--base) l c h / 0.3); /* Transparent */
}

/* oklch — perceptually uniform color space */
color: oklch(0.7 0.15 250);      /* lightness chroma hue */
color: oklch(0.7 0.15 250 / 0.5); /* with alpha */

/* oklab */
color: oklab(0.7 -0.1 0.1);

/* color-mix — blend colors */
color: color-mix(in oklch, var(--primary) 70%, white);
color: color-mix(in srgb, red, blue);

/* Legacy functions (still valid) */
color: rgb(59 130 246);           /* Modern syntax (no commas) */
color: rgb(59 130 246 / 0.5);    /* With alpha */
color: hsl(220 90% 60%);
color: hsl(220 90% 60% / 0.5);
```

---

## Typography

```css
/* System font stack */
font-family: system-ui, -apple-system, 'Segoe UI', Roboto, 'Helvetica Neue', Arial, sans-serif;

/* Font loading */
@font-face {
  font-family: 'CustomFont';
  src: url('font.woff2') format('woff2');
  font-weight: 100 900;           /* Variable font weight range */
  font-display: swap;             /* Show fallback while loading */
  unicode-range: U+0000-00FF;     /* Latin characters only */
}

/* Clamp for fluid typography */
font-size: clamp(1rem, 2.5vw, 2rem);

/* Text wrapping */
text-wrap: balance;        /* Balanced line lengths (headings) */
text-wrap: pretty;         /* Avoid orphans (paragraphs) */
text-wrap: stable;         /* Prevent reflow during edits */

/* Truncation */
.truncate {
  overflow: hidden;
  text-overflow: ellipsis;
  white-space: nowrap;
}

/* Multi-line truncation */
.line-clamp {
  display: -webkit-box;
  -webkit-box-orient: vertical;
  -webkit-line-clamp: 3;
  overflow: hidden;
}

/* Variable fonts */
font-variation-settings: 'wght' 600, 'wdth' 75;
```

---

## Transitions & Animations

### Transitions

```css
.element {
  transition: all 300ms ease;
  transition: transform 200ms ease, opacity 200ms ease;
  transition: color 150ms ease-in-out;

  /* Individual properties */
  transition-property: transform, opacity;
  transition-duration: 300ms;
  transition-timing-function: ease;       /* ease | linear | ease-in | ease-out | ease-in-out */
  transition-timing-function: cubic-bezier(0.4, 0, 0.2, 1);
  transition-delay: 100ms;

  /* Starting style (animate on element creation/display) */
  @starting-style {
    opacity: 0;
    transform: translateY(20px);
  }
}

/* Discrete property transitions (new) */
.element {
  transition: display 300ms allow-discrete,
              opacity 300ms;
}
```

### Keyframe Animations

```css
@keyframes fadeIn {
  from { opacity: 0; transform: translateY(20px); }
  to   { opacity: 1; transform: translateY(0); }
}

@keyframes pulse {
  0%, 100% { transform: scale(1); }
  50%      { transform: scale(1.05); }
}

.element {
  animation: fadeIn 500ms ease forwards;

  /* Individual properties */
  animation-name: fadeIn;
  animation-duration: 500ms;
  animation-timing-function: ease;
  animation-delay: 200ms;
  animation-iteration-count: infinite;   /* number | infinite */
  animation-direction: alternate;        /* normal | reverse | alternate | alternate-reverse */
  animation-fill-mode: forwards;         /* none | forwards | backwards | both */
  animation-play-state: running;         /* running | paused */
}
```

### Scroll-driven Animations

```css
/* Animate based on scroll position */
@keyframes fadeIn {
  from { opacity: 0; }
  to   { opacity: 1; }
}

.element {
  animation: fadeIn linear;
  animation-timeline: scroll();          /* Nearest scroll container */
  animation-timeline: scroll(root);      /* Document scroll */
  animation-range: entry 0% entry 100%;  /* When element enters viewport */
}

/* View timeline (element visibility in viewport) */
.element {
  animation: fadeIn linear;
  animation-timeline: view();
  animation-range: entry 0% cover 40%;
}

/* Named scroll timeline */
.scroller {
  scroll-timeline-name: --my-timeline;
  scroll-timeline-axis: block;
}
.animated {
  animation-timeline: --my-timeline;
}
```

### View Transitions

```css
/* Opt in to view transitions */
@view-transition {
  navigation: auto;
}

/* Customize the transition */
::view-transition-old(root) {
  animation: fade-out 200ms ease;
}
::view-transition-new(root) {
  animation: fade-in 200ms ease;
}

/* Named view transitions for specific elements */
.card {
  view-transition-name: card-1;
}
::view-transition-group(card-1) {
  animation-duration: 400ms;
}
```

```javascript
// Trigger view transition programmatically
document.startViewTransition(() => {
  updateDOM()
})
```

---

## Logical Properties

Use logical properties instead of physical (support RTL automatically):

```css
/* Block = vertical (in horizontal writing), Inline = horizontal */
margin-block: 1rem;           /* margin-top + margin-bottom */
margin-inline: auto;          /* margin-left + margin-right */
margin-block-start: 1rem;     /* margin-top */
margin-block-end: 1rem;       /* margin-bottom */
margin-inline-start: 1rem;    /* margin-left (in LTR) */
margin-inline-end: 1rem;      /* margin-right (in LTR) */

padding-block: 1rem;
padding-inline: 2rem;

/* Size */
inline-size: 100%;            /* width */
block-size: auto;             /* height */
max-inline-size: 65ch;        /* max-width */
min-block-size: 100vh;        /* min-height */

/* Border */
border-block: 1px solid;
border-inline-start: 2px solid;

/* Positioning */
inset: 0;                     /* top right bottom left = 0 */
inset-block: 0;               /* top + bottom */
inset-inline: 0;              /* left + right */
inset-block-start: 0;         /* top */

/* Text alignment */
text-align: start;            /* left in LTR, right in RTL */
text-align: end;
```

---

## Cascade Layers

```css
/* Define layer order (first = lowest priority) */
@layer reset, base, components, utilities;

/* Add rules to a layer */
@layer reset {
  * { margin: 0; padding: 0; box-sizing: border-box; }
}

@layer base {
  body { font-family: system-ui; line-height: 1.6; }
  a { color: var(--link-color); }
}

@layer components {
  .btn { padding: 0.5rem 1rem; border-radius: 0.25rem; }
  .card { padding: 1rem; border: 1px solid #eee; }
}

@layer utilities {
  .sr-only { position: absolute; width: 1px; height: 1px; overflow: hidden; clip: rect(0,0,0,0); }
  .hidden { display: none; }
}

/* Import into a layer */
@import url('reset.css') layer(reset);

/* Unlayered styles beat ALL layers */
.override { color: red; }  /* Wins over any layer */
```

---

## Scroll Snap

```css
/* Container */
.scroll-container {
  overflow-x: auto;
  scroll-snap-type: x mandatory;      /* x | y | both, mandatory | proximity */
  scroll-padding: 1rem;               /* Offset from snap points */
  overscroll-behavior: contain;        /* Prevent scroll chaining */
  -webkit-overflow-scrolling: touch;
}

/* Items */
.scroll-item {
  scroll-snap-align: start;           /* start | center | end */
  scroll-snap-stop: always;           /* normal | always (force stop at each) */
}
```

---

## Modern Sizing & Layout

```css
/* Viewport units */
width: 100vw;           /* Viewport width */
height: 100vh;          /* Viewport height */
height: 100dvh;         /* Dynamic viewport height (accounts for mobile browser chrome) */
height: 100svh;         /* Small viewport height */
height: 100lvh;         /* Large viewport height */

/* Content-based sizing */
width: fit-content;     /* Shrink to content, up to available space */
width: min-content;     /* Smallest content can be without overflow */
width: max-content;     /* Content without line breaks */

/* Math functions */
width: calc(100% - 2rem);
width: min(600px, 100% - 2rem);
width: max(300px, 50%);
width: clamp(300px, 50%, 800px);

/* Aspect ratio */
aspect-ratio: 16 / 9;
aspect-ratio: 1;        /* Square */

/* Object fit (for replaced elements: img, video) */
object-fit: cover;      /* contain | cover | fill | none | scale-down */
object-position: center top;
```

---

## Filters & Effects

```css
/* Filter functions */
filter: blur(4px);
filter: brightness(1.2);
filter: contrast(1.5);
filter: grayscale(100%);
filter: hue-rotate(90deg);
filter: invert(100%);
filter: opacity(50%);
filter: saturate(200%);
filter: sepia(100%);
filter: drop-shadow(4px 4px 8px rgba(0,0,0,0.3));

/* Combine filters */
filter: brightness(1.1) contrast(1.2) saturate(1.3);

/* Backdrop filter (blur behind element) */
backdrop-filter: blur(10px) saturate(180%);

/* Mix blend mode */
mix-blend-mode: multiply;
/* normal | multiply | screen | overlay | darken | lighten
   color-dodge | color-burn | hard-light | soft-light
   difference | exclusion | hue | saturation | color | luminosity */

/* Background blend mode */
background-blend-mode: overlay;

/* Clip path */
clip-path: circle(50%);
clip-path: ellipse(50% 40%);
clip-path: polygon(50% 0%, 100% 100%, 0% 100%);
clip-path: inset(10px 20px 30px 40px round 10px);

/* Mask */
mask-image: linear-gradient(to bottom, black, transparent);
```

---

## Media Queries

```css
/* Breakpoints */
@media (min-width: 640px)  { }    /* sm */
@media (min-width: 768px)  { }    /* md */
@media (min-width: 1024px) { }    /* lg */
@media (min-width: 1280px) { }    /* xl */

/* Modern range syntax */
@media (width >= 768px) { }
@media (400px <= width <= 800px) { }

/* Preferences */
@media (prefers-color-scheme: dark)    { }
@media (prefers-reduced-motion: reduce) { }
@media (prefers-contrast: high)         { }
@media (prefers-reduced-transparency: reduce) { }

/* Display */
@media (hover: hover)          { }   /* Has hover capability */
@media (hover: none)           { }   /* Touch-only */
@media (pointer: fine)         { }   /* Mouse/stylus */
@media (pointer: coarse)       { }   /* Touch */
@media (orientation: portrait) { }
@media (orientation: landscape) { }

/* Print */
@media print {
  .no-print { display: none; }
  body { font-size: 12pt; }
}
```

---

## Anchor Positioning (new)

```css
/* Define an anchor */
.trigger {
  anchor-name: --my-anchor;
}

/* Position relative to anchor */
.tooltip {
  position: fixed;
  position-anchor: --my-anchor;
  top: anchor(bottom);
  left: anchor(center);
  translate: -50% 0;

  /* Fallback if overflows viewport */
  position-try-fallbacks: --above;
}

@position-try --above {
  bottom: anchor(top);
  top: auto;
}
```

---

## Best Practices

1. **Use `box-sizing: border-box` globally** — `*, *::before, *::after { box-sizing: border-box; }`
2. **Use custom properties for design tokens** — colors, spacing, typography, shadows
3. **Use logical properties** — `margin-inline`, `padding-block` for RTL support
4. **Use `clamp()` for fluid typography** — `font-size: clamp(1rem, 2.5vw, 2rem)`
5. **Use Grid for 2D layouts, Flexbox for 1D** — don't force one where the other fits better
6. **Use `container queries` for component-level responsiveness** — not just viewport media queries
7. **Use `prefers-reduced-motion`** — disable animations for users who need it
8. **Use `prefers-color-scheme`** — support system dark mode preference
9. **Use cascade layers** — `@layer` for predictable specificity ordering
10. **Use `dvh` instead of `vh`** on mobile — accounts for browser chrome
11. **Always set `font-display: swap`** on `@font-face` — prevent invisible text
12. **Use `will-change` sparingly** — only on elements that actually animate
13. **Avoid `!important`** — use layers or increase specificity naturally
14. **Use native CSS nesting** — reduce preprocessor dependency
15. **Use `aspect-ratio`** instead of the padding hack — cleaner responsive media
