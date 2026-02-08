# Animation Libraries Reference for Creative Frontend Development (2025-2026)

Comprehensive reference for modern CSS/JS animation libraries, CDN links, APIs, usage patterns, and performance considerations.

---

## Table of Contents

1. [GSAP (GreenSock)](#1-gsap-greensock)
2. [Motion (formerly Framer Motion)](#2-motion-formerly-framer-motion)
3. [Anime.js](#3-animejs)
4. [AOS (Animate on Scroll)](#4-aos-animate-on-scroll)
5. [Lottie](#5-lottie)
6. [Three.js](#6-threejs)
7. [tsParticles](#7-tsparticles)
8. [Typed.js](#8-typedjs)
9. [Swiper.js](#9-swiperjs)
10. [Locomotive Scroll](#10-locomotive-scroll)
11. [Splitting.js](#11-splittingjs)
12. [AutoAnimate](#12-autoanimate)
13. [Native CSS Animation Techniques (2025-2026)](#13-native-css-animation-techniques-2025-2026)
14. [Animation Trends & Best Practices (2025-2026)](#14-animation-trends--best-practices-2025-2026)

---

## 1. GSAP (GreenSock)

**Version:** 3.14.x (latest: 3.14.2)
**License:** FREE for all use including commercial (since Webflow acquisition in late 2024, ALL plugins are free)
**Size:** ~30kb core (minified + gzipped)
**Website:** https://gsap.com

### CDN Links

```html
<!-- Core GSAP -->
<script src="https://cdn.jsdelivr.net/npm/gsap@3/dist/gsap.min.js"></script>

<!-- ScrollTrigger -->
<script src="https://cdn.jsdelivr.net/npm/gsap@3/dist/ScrollTrigger.min.js"></script>

<!-- ScrollToPlugin -->
<script src="https://cdn.jsdelivr.net/npm/gsap@3/dist/ScrollToPlugin.min.js"></script>

<!-- SplitText (NOW FREE) -->
<script src="https://cdn.jsdelivr.net/npm/gsap@3/dist/SplitText.min.js"></script>

<!-- Flip Plugin -->
<script src="https://cdn.jsdelivr.net/npm/gsap@3/dist/Flip.min.js"></script>

<!-- Observer Plugin -->
<script src="https://cdn.jsdelivr.net/npm/gsap@3/dist/Observer.min.js"></script>

<!-- DrawSVG Plugin (NOW FREE) -->
<script src="https://cdn.jsdelivr.net/npm/gsap@3/dist/DrawSVGPlugin.min.js"></script>

<!-- MotionPathPlugin -->
<script src="https://cdn.jsdelivr.net/npm/gsap@3/dist/MotionPathPlugin.min.js"></script>

<!-- MorphSVGPlugin (NOW FREE) -->
<script src="https://cdn.jsdelivr.net/npm/gsap@3/dist/MorphSVGPlugin.min.js"></script>

<!-- TextPlugin -->
<script src="https://cdn.jsdelivr.net/npm/gsap@3/dist/TextPlugin.min.js"></script>
```

### NPM Install

```bash
npm install gsap
```

### Plugin Registration

```javascript
import gsap from "gsap";
import { ScrollTrigger } from "gsap/ScrollTrigger";
import { SplitText } from "gsap/SplitText";
import { Flip } from "gsap/Flip";
import { DrawSVGPlugin } from "gsap/DrawSVGPlugin";
import { MotionPathPlugin } from "gsap/MotionPathPlugin";
import { MorphSVGPlugin } from "gsap/MorphSVGPlugin";
import { Observer } from "gsap/Observer";

gsap.registerPlugin(ScrollTrigger, SplitText, Flip, DrawSVGPlugin, MotionPathPlugin, MorphSVGPlugin, Observer);
```

### Core API Methods

#### gsap.to() - Animate TO target values
```javascript
gsap.to(".box", {
  x: 200,
  y: 100,
  rotation: 360,
  scale: 1.5,
  opacity: 0.5,
  duration: 1,
  ease: "power2.out",
  delay: 0.5,
  onComplete: () => console.log("done")
});
```

#### gsap.from() - Animate FROM target values
```javascript
gsap.from(".box", {
  x: -200,
  opacity: 0,
  duration: 1,
  ease: "back.out(1.7)"
});
```

#### gsap.fromTo() - Define both start and end
```javascript
gsap.fromTo(".box",
  { opacity: 0, y: 50 },
  { opacity: 1, y: 0, duration: 1, ease: "power3.out" }
);
```

#### gsap.set() - Instantly set properties (no animation)
```javascript
gsap.set(".box", { x: 100, opacity: 0, transformOrigin: "center center" });
```

#### gsap.timeline() - Sequence animations
```javascript
const tl = gsap.timeline({
  defaults: { duration: 0.8, ease: "power2.out" },
  repeat: -1,        // infinite repeat
  repeatDelay: 1,
  yoyo: true,        // reverse on repeat
  paused: false
});

tl.to(".box1", { x: 300 })
  .to(".box2", { y: 200 }, "-=0.3")   // overlap by 0.3s
  .to(".box3", { rotation: 360 }, "<") // start at same time as previous
  .to(".box4", { scale: 2 }, "+=0.5"); // 0.5s gap after previous ends

// Timeline control
tl.play();
tl.pause();
tl.reverse();
tl.restart();
tl.progress(0.5);  // jump to 50%
tl.timeScale(2);   // 2x speed
```

### Timeline Position Parameters

```
"<"          Start at same time as previous animation
">"          Start at end of previous animation (default)
"-=0.5"      0.5 seconds before end of previous
"+=0.5"      0.5 seconds after end of previous
2            At exactly 2 seconds on the timeline
"myLabel"    At a specific label
"myLabel+=1" 1 second after a specific label
```

### Easing Functions

```
"none"               Linear
"power1.out"         Subtle ease out (same as "quad.out")
"power2.out"         Medium ease out (same as "cubic.out")
"power3.out"         Strong ease out (same as "quart.out")
"power4.out"         Very strong ease out (same as "quint.out")
"back.out(1.7)"      Overshoot then settle
"elastic.out(1,0.3)" Bouncy elastic
"bounce.out"         Bouncing effect
"expo.out"           Exponential ease out
"circ.out"           Circular ease out
"steps(12)"          Stepped animation (12 steps)
"slow(0.7,0.7,false)" Slow start/end, fast middle

// All easing types also have .in and .inOut variants:
"power2.in"
"power2.inOut"
```

### ScrollTrigger

```javascript
gsap.registerPlugin(ScrollTrigger);

// Basic scroll-triggered animation
gsap.to(".box", {
  scrollTrigger: {
    trigger: ".box",           // element that triggers
    start: "top center",       // trigger start: "triggerTop viewportPosition"
    end: "bottom top",         // trigger end
    scrub: true,               // link animation to scroll (true = instant, 1 = 1s catchup)
    pin: true,                 // pin the trigger element
    markers: true,             // debug markers (remove in production)
    toggleActions: "play pause resume reverse",  // onEnter onLeave onEnterBack onLeaveBack
    snap: {
      snapTo: 1/5,            // snap to 20% increments
      duration: { min: 0.2, max: 0.5 },
      ease: "power1.inOut"
    },
    onEnter: () => {},
    onLeave: () => {},
    onEnterBack: () => {},
    onLeaveBack: () => {},
    onUpdate: (self) => console.log("progress:", self.progress)
  },
  x: 500,
  rotation: 360
});

// ScrollTrigger with Timeline
const tl = gsap.timeline({
  scrollTrigger: {
    trigger: ".section",
    start: "top top",
    end: "+=3000",             // scroll for 3000px
    scrub: 1,
    pin: true
  }
});
tl.to(".panel-1", { xPercent: -100 })
  .to(".panel-2", { xPercent: -100 })
  .to(".panel-3", { xPercent: -100 });

// Batch stagger on scroll
ScrollTrigger.batch(".card", {
  onEnter: (elements) => {
    gsap.from(elements, {
      opacity: 0,
      y: 60,
      stagger: 0.15,
      duration: 0.8,
      ease: "power3.out"
    });
  },
  once: true
});
```

#### ScrollTrigger start/end Reference

```
"top top"        Element top hits viewport top
"top center"     Element top hits viewport center
"top bottom"     Element top hits viewport bottom (enters view)
"center center"  Element center hits viewport center
"bottom top"     Element bottom hits viewport top
"top 80%"        Element top hits 80% from viewport top
"top+=100 center" Element top + 100px hits viewport center
```

### SplitText (NOW FREE)

```javascript
gsap.registerPlugin(SplitText);

// Split text into chars, words, and lines
const split = new SplitText(".headline", {
  type: "chars, words, lines",
  linesClass: "line",
  wordsClass: "word",
  charsClass: "char",
  mask: "lines"   // adds masking wrapper for reveal effects
});

// Animate characters with stagger
gsap.from(split.chars, {
  opacity: 0,
  y: 50,
  rotateX: -90,
  stagger: 0.02,
  duration: 0.8,
  ease: "back.out(1.7)"
});

// Auto re-split on resize
const split2 = new SplitText(".responsive-text", {
  type: "lines",
  autoSplit: true,    // NEW: automatically re-splits on resize
  mask: "lines"
});

// Line reveal animation
gsap.from(split2.lines, {
  yPercent: 100,
  stagger: 0.1,
  duration: 0.6,
  ease: "power3.out"
});
```

### Flip Plugin

```javascript
gsap.registerPlugin(Flip);

// Record current state
const state = Flip.getState(".items");

// Make DOM changes (reorder, reparent, add/remove classes)
container.appendChild(item);
item.classList.toggle("active");

// Animate from old state to new state
Flip.from(state, {
  duration: 0.6,
  ease: "power1.inOut",
  stagger: 0.05,
  absolute: true,      // use absolute positioning during flip
  scale: true,         // animate scale changes
  onEnter: elements => gsap.fromTo(elements, { opacity: 0, scale: 0 }, { opacity: 1, scale: 1, duration: 0.6 }),
  onLeave: elements => gsap.to(elements, { opacity: 0, scale: 0, duration: 0.4 })
});
```

### Observer Plugin

```javascript
gsap.registerPlugin(Observer);

Observer.create({
  target: window,
  type: "wheel, touch, pointer",
  onUp: () => goToPreviousSection(),
  onDown: () => goToNextSection(),
  tolerance: 10,
  preventDefault: true,
  wheelSpeed: -1
});
```

### Stagger Options

```javascript
gsap.to(".box", {
  y: -20,
  stagger: {
    each: 0.1,           // time between each
    from: "center",      // "start", "end", "center", "edges", "random", or index number
    grid: [7, 15],       // treat targets as a grid
    axis: "y",           // "x" or "y" for grid direction
    ease: "power2.in",   // distribution easing
    amount: 1            // total time for stagger (alternative to 'each')
  }
});
```

### Performance Considerations

- GSAP uses requestAnimationFrame; animations stop when tab is not visible
- Use `will-change: transform` on animated elements for GPU compositing
- Prefer transforms (x, y, rotation, scale) over layout properties (top, left, width, height)
- Use `force3D: true` (default) to promote to GPU layer
- ScrollTrigger calculates trigger points upfront for efficiency
- Use `gsap.ticker` for synchronized animations instead of separate rAF loops
- Kill animations when no longer needed: `tl.kill()` or `ScrollTrigger.kill()`
- Use `invalidateOnRefresh: true` on ScrollTriggers for responsive designs

### Best Use Cases

- Complex, sequenced multi-step animations
- Scroll-driven storytelling experiences
- Text reveal animations (SplitText)
- FLIP layout transitions
- SVG path drawing and morphing
- Pinned scrolling sections
- Parallax effects
- Interactive microinteractions

---

## 2. Motion (formerly Framer Motion)

**Version:** 12.x (latest: ~12.33.0)
**License:** MIT
**Size:** ~34kb (minified + gzipped, tree-shakeable)
**Website:** https://motion.dev
**Note:** Rebranded from "Framer Motion" to "Motion" in 2024. Now supports BOTH React AND vanilla JavaScript.

### CDN Links (Vanilla JavaScript)

```html
<!-- ES Module -->
<script type="module">
  import { animate, scroll, inView } from "https://cdn.jsdelivr.net/npm/motion@latest/+esm";
</script>

<!-- Legacy UMD (global "Motion" object) -->
<script src="https://cdn.jsdelivr.net/npm/motion@latest/dist/motion.js"></script>
<script>
  const { animate, scroll } = Motion;
</script>
```

### NPM Install

```bash
npm install motion       # Vanilla JS + React
npm install framer-motion  # React only (legacy package name, still works)
```

### React: Core motion Component

```jsx
import { motion } from "motion/react";

// Basic animation
<motion.div
  initial={{ opacity: 0, y: 20 }}
  animate={{ opacity: 1, y: 0 }}
  transition={{ duration: 0.5, ease: "easeOut" }}
>
  Hello World
</motion.div>

// Hover and tap gestures
<motion.button
  whileHover={{ scale: 1.05, backgroundColor: "#ff6b6b" }}
  whileTap={{ scale: 0.95 }}
  transition={{ type: "spring", stiffness: 400, damping: 17 }}
>
  Click me
</motion.button>

// Drag
<motion.div
  drag
  dragConstraints={{ left: -100, right: 100, top: -50, bottom: 50 }}
  dragElastic={0.2}
  whileDrag={{ scale: 1.1 }}
/>
```

### React: AnimatePresence (Exit Animations)

```jsx
import { AnimatePresence, motion } from "motion/react";

function Modal({ isOpen }) {
  return (
    <AnimatePresence mode="wait">
      {isOpen && (
        <motion.div
          key="modal"
          initial={{ opacity: 0, scale: 0.8, y: 20 }}
          animate={{ opacity: 1, scale: 1, y: 0 }}
          exit={{ opacity: 0, scale: 0.8, y: 20 }}
          transition={{ type: "spring", damping: 25, stiffness: 300 }}
        >
          Modal Content
        </motion.div>
      )}
    </AnimatePresence>
  );
}

// AnimatePresence modes:
// "sync"      - all enter/exit at same time (default)
// "wait"      - exit completes before enter starts
// "popLayout" - exiting elements removed from layout flow immediately
```

### React: Layout Animations

```jsx
import { motion, LayoutGroup } from "motion/react";

// Automatic layout animation
<motion.div layout>
  {/* When this element's size/position changes in the DOM, it animates smoothly */}
</motion.div>

// Layout with ID for shared element transitions
<motion.div layoutId="hero-image">
  <img src={image} />
</motion.div>

// LayoutGroup to scope layoutId matching
<LayoutGroup>
  <motion.div layoutId="underline" />
</LayoutGroup>

// Layout animation with scroll container
<motion.div layoutScroll style={{ overflow: "scroll" }}>
  <motion.div layout />
</motion.div>
```

### React: Variants (Orchestrated Animations)

```jsx
const containerVariants = {
  hidden: { opacity: 0 },
  visible: {
    opacity: 1,
    transition: {
      staggerChildren: 0.1,
      delayChildren: 0.3
    }
  }
};

const itemVariants = {
  hidden: { opacity: 0, y: 20 },
  visible: {
    opacity: 1,
    y: 0,
    transition: { type: "spring", stiffness: 300, damping: 24 }
  }
};

<motion.ul variants={containerVariants} initial="hidden" animate="visible">
  {items.map(item => (
    <motion.li key={item.id} variants={itemVariants}>
      {item.text}
    </motion.li>
  ))}
</motion.ul>
```

### React: useAnimate Hook (Imperative Control)

```jsx
import { useAnimate, stagger } from "motion/react";

function Component() {
  const [scope, animate] = useAnimate();

  async function handleClick() {
    await animate("li", { opacity: 0, x: -100 }, { duration: 0.3 });
    await animate("li", { opacity: 1, x: 0 }, { delay: stagger(0.05) });
  }

  return (
    <ul ref={scope}>
      <li>Item 1</li>
      <li>Item 2</li>
    </ul>
  );
}
```

### React: useScroll & useTransform

```jsx
import { motion, useScroll, useTransform } from "motion/react";

function ParallaxSection() {
  const { scrollYProgress } = useScroll();
  const y = useTransform(scrollYProgress, [0, 1], [0, -300]);
  const opacity = useTransform(scrollYProgress, [0, 0.5, 1], [1, 0.5, 0]);
  const scale = useTransform(scrollYProgress, [0, 1], [1, 0.8]);

  return (
    <motion.div style={{ y, opacity, scale }}>
      Parallax content
    </motion.div>
  );
}

// Scroll-linked to specific element
function ElementScroll() {
  const ref = useRef(null);
  const { scrollYProgress } = useScroll({
    target: ref,
    offset: ["start end", "end start"]
  });

  return <motion.div ref={ref} style={{ opacity: scrollYProgress }} />;
}
```

### React: useInView

```jsx
import { useInView } from "motion/react";

function Component() {
  const ref = useRef(null);
  const isInView = useInView(ref, {
    once: true,
    margin: "-100px",
    amount: 0.5  // 50% visible
  });

  return (
    <motion.div
      ref={ref}
      initial={{ opacity: 0, y: 50 }}
      animate={isInView ? { opacity: 1, y: 0 } : {}}
      transition={{ duration: 0.6 }}
    />
  );
}
```

### Vanilla JS: animate()

```javascript
import { animate, stagger, scroll, inView } from "motion";

// Basic animation
animate(".box", { opacity: [0, 1], y: [20, 0] }, { duration: 0.6, ease: "ease-out" });

// Spring physics
animate(".card", { scale: 1.1 }, { type: "spring", stiffness: 300, damping: 20 });

// Stagger
animate("li", { opacity: [0, 1], x: [-20, 0] }, { delay: stagger(0.1) });

// Keyframes
animate(".spinner", { rotate: [0, 180, 360] }, { duration: 2, repeat: Infinity });

// Scroll-linked
scroll(
  animate(".progress-bar", { scaleX: [0, 1] }),
  { target: document.querySelector(".article") }
);

// In-view detection
inView(".card", (info) => {
  animate(info.target, { opacity: 1, y: 0 }, { duration: 0.5 });
  return () => {
    // cleanup when element leaves view
  };
});
```

### Transition Types

```javascript
// Spring (physics-based, default for most properties)
{ type: "spring", stiffness: 300, damping: 20, mass: 1 }
{ type: "spring", bounce: 0.25, duration: 0.6 }

// Tween (duration-based)
{ type: "tween", duration: 0.5, ease: "easeInOut" }
{ type: "tween", ease: [0.16, 1, 0.3, 1] }  // custom cubic bezier

// Inertia (for drag/scroll deceleration)
{ type: "inertia", velocity: 200, power: 0.8 }
```

### Performance Considerations

- Motion uses the Web Animations API (WAAPI) for hardware-accelerated animations
- Layout animations use FLIP technique (calculate → apply inverse transform → animate)
- Tree-shakeable: only import what you use
- Use `layout="position"` instead of `layout` when only position changes (not size)
- Avoid animating layout-triggering properties (width, height, padding)
- AnimatePresence with `mode="popLayout"` is most performant for lists

### Best Use Cases

- React component transitions and mount/unmount animations
- Shared layout transitions (e.g., expanding cards, tabs with sliding underline)
- Gesture-driven interactions (drag, hover, tap)
- Page route transitions
- List reordering animations
- Scroll-linked animations in React
- Spring physics for natural motion

---

## 3. Anime.js

**Version:** 4.x (latest: 4.0.2)
**License:** MIT
**Size:** ~17kb (minified + gzipped)
**Website:** https://animejs.com

### CDN Links

```html
<!-- UMD Bundle -->
<script src="https://cdn.jsdelivr.net/npm/animejs@4/lib/anime.min.js"></script>

<!-- ES Module -->
<script type="module">
  import { animate, createTimeline, stagger, utils, eases, svg, spring } from 'https://cdn.jsdelivr.net/npm/animejs@4/+esm';
</script>
```

### NPM Install

```bash
npm install animejs
```

### V4 API - animate()

```javascript
import { animate, stagger, createTimeline, utils, eases, svg, spring } from 'animejs';

// Basic animation
animate('.box', {
  translateX: 250,
  rotate: '1turn',
  backgroundColor: '#FF6B6B',
  borderRadius: ['0%', '50%'],
  duration: 800,
  ease: 'outExpo'
});

// With keyframes
animate('.box', {
  translateX: [
    { to: 250, duration: 1000 },
    { to: 0, duration: 1000, delay: 500 }
  ],
  rotate: { to: '1turn', ease: 'inOutQuad' },
  duration: 2000
});

// Animation controls (returned object)
const anim = animate('.box', {
  translateX: 250,
  duration: 1000,
  autoplay: false
});

anim.play();
anim.pause();
anim.reverse();
anim.restart();
anim.seek(500);  // seek to 500ms
```

### V4 API - createTimeline()

```javascript
const tl = createTimeline({
  defaults: {
    duration: 600,
    ease: 'outExpo'
  },
  loop: true,
  autoplay: true
});

tl.add('.box1', {
  translateX: 250,
  rotate: '1turn'
})
.add('.box2', {
  translateY: 200,
  scale: 2
}, '-=400')   // overlap by 400ms
.add('.box3', {
  opacity: [0, 1],
  translateX: [-50, 0]
}, '+=200');   // 200ms gap

// Timeline control
tl.play();
tl.pause();
tl.reverse();
tl.restart();
```

### V4 API - stagger()

```javascript
// Stagger with value
animate('.item', {
  translateY: [-20, 0],
  opacity: [0, 1],
  delay: stagger(100)           // 100ms between each
});

// Stagger with range
animate('.item', {
  rotate: stagger([0, 360]),    // distribute 0-360 across all items
  delay: stagger(100, { start: 500 })  // start after 500ms
});

// Stagger from center
animate('.grid-item', {
  scale: [0, 1],
  delay: stagger(50, {
    grid: [14, 5],              // grid dimensions
    from: 'center',             // 'first', 'last', 'center', index number
    axis: 'x'                   // 'x', 'y', or undefined for both
  })
});

// Stagger in timeline positions
tl.add('.item', {
  translateX: 250
}, stagger(100));               // stagger start positions in timeline
```

### V4 API - spring()

```javascript
// Physics-based spring easing
animate('.box', {
  translateX: 300,
  ease: spring({ stiffness: 100, damping: 10, mass: 1 })
});

// Spring with velocity
animate('.box', {
  scale: 1.5,
  ease: spring({ stiffness: 300, damping: 15, velocity: 5 })
});
```

### V4 API - SVG

```javascript
// SVG path animation (line drawing)
animate('path', {
  strokeDashoffset: [svg.getLength('path'), 0],
  duration: 2000,
  ease: 'inOutQuad'
});

// SVG morph (path morphing)
animate('path', {
  d: [
    { to: 'M10 80 Q 95 10 180 80' },
    { to: 'M10 80 Q 52 150 180 80' }
  ],
  duration: 2000,
  ease: 'inOutSine',
  loop: true,
  alternate: true
});
```

### V4 Key Changes from V3

```
V3                          V4
-------                     -------
anime({targets:...})        animate(targets, {...})
anime.timeline()            createTimeline()
anime.stagger()             stagger()
anime.set()                 utils.set()
easing: 'easeOutExpo'       ease: 'outExpo'
direction: 'alternate'      alternate: true
loop: true                  loop: true (same)
```

### Performance Considerations

- Lightweight (~17kb), excellent for bundle-size-conscious projects
- V4 has 300+ tests and improved performance over V3
- Native TypeScript support in V4 reduces bugs
- Works with CSS transforms, SVG, DOM attributes, and JS objects
- Prefer transforms over layout-triggering properties
- Use `autoplay: false` for animations triggered by user interaction

### Best Use Cases

- Lightweight alternative to GSAP
- SVG path animations and morphing
- Staggered grid animations
- Micro-interactions
- Logo animations
- UI state transitions
- Projects where bundle size matters

---

## 4. AOS (Animate on Scroll)

**Version:** 2.3.4 (stable, mature library)
**License:** MIT
**Size:** ~14kb (JS + CSS)
**Website:** https://michalsnik.github.io/aos/

### CDN Links

```html
<!-- CSS -->
<link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/aos@2/dist/aos.css">

<!-- JavaScript -->
<script src="https://cdn.jsdelivr.net/npm/aos@2/dist/aos.js"></script>
```

### NPM Install

```bash
npm install aos
```

### Initialization

```javascript
// Basic init
AOS.init();

// With options
AOS.init({
  duration: 800,              // animation duration (ms)
  easing: 'ease-out-cubic',   // easing function
  once: true,                 // animate only once
  mirror: false,              // animate on scroll back up
  offset: 120,                // offset (px) from original trigger point
  delay: 0,                   // default delay
  anchorPlacement: 'top-bottom',  // anchor placement
  disable: 'mobile',         // disable on mobile: 'mobile', 'phone', 'tablet', or function
  startEvent: 'DOMContentLoaded',
  debounceDelay: 50,
  throttleDelay: 99
});

// Refresh (after DOM changes)
AOS.refresh();
AOS.refreshHard();  // reinitialize
```

### Animation Types (data-aos values)

```
Fade animations:
  fade, fade-up, fade-down, fade-left, fade-right
  fade-up-right, fade-up-left, fade-down-right, fade-down-left

Flip animations:
  flip-up, flip-down, flip-left, flip-right

Slide animations:
  slide-up, slide-down, slide-left, slide-right

Zoom animations:
  zoom-in, zoom-in-up, zoom-in-down, zoom-in-left, zoom-in-right
  zoom-out, zoom-out-up, zoom-out-down, zoom-out-left, zoom-out-right
```

### Data Attributes

```html
<!-- Basic usage -->
<div data-aos="fade-up">Content</div>

<!-- With duration and delay -->
<div data-aos="fade-up"
     data-aos-duration="1000"
     data-aos-delay="200">
  Content
</div>

<!-- With anchor (trigger based on another element) -->
<div data-aos="fade-left"
     data-aos-anchor="#trigger-element"
     data-aos-offset="300">
  Content
</div>

<!-- With anchor placement -->
<div data-aos="zoom-in"
     data-aos-anchor-placement="top-center"
     data-aos-easing="ease-in-back">
  Content
</div>

<!-- Once only (no repeat) -->
<div data-aos="flip-up"
     data-aos-once="true">
  Content
</div>
```

#### Anchor Placement Values

```
top-bottom (default)  - element top reaches viewport bottom
top-center           - element top reaches viewport center
top-top              - element top reaches viewport top
center-bottom        - element center reaches viewport bottom
center-center        - element center reaches viewport center
center-top           - element center reaches viewport top
bottom-bottom        - element bottom reaches viewport bottom
bottom-center        - element bottom reaches viewport center
bottom-top           - element bottom reaches viewport top
```

#### Easing Values

```
linear, ease, ease-in, ease-out, ease-in-out
ease-in-back, ease-out-back, ease-in-out-back
ease-in-sine, ease-out-sine, ease-in-out-sine
ease-in-quad, ease-out-quad, ease-in-out-quad
ease-in-cubic, ease-out-cubic, ease-in-out-cubic
ease-in-quart, ease-out-quart, ease-in-out-quart
```

### Custom Animations

```css
/* Define your own AOS animation */
[data-aos="custom-fade-rotate"] {
  opacity: 0;
  transform: rotate(-10deg) translateY(30px);
  transition-property: opacity, transform;
}
[data-aos="custom-fade-rotate"].aos-animate {
  opacity: 1;
  transform: rotate(0) translateY(0);
}
```

### Performance Considerations

- Pure CSS-driven animations (CSS transitions applied via classes)
- Uses Intersection Observer internally
- Debounces scroll events by default
- Set `once: true` globally to prevent re-triggering (better performance)
- Disable on mobile if animations are heavy: `disable: 'mobile'`
- Duration values only accept 50-3000 in steps of 50

### Best Use Cases

- Quick scroll reveal animations without writing JS
- Marketing and landing pages
- Content-heavy sites with many sections
- Rapid prototyping
- CMS-driven sites where non-developers add content
- Projects that need simple scroll animations without complex sequencing

---

## 5. Lottie

**Version:** lottie-web 5.13.0 | @lottiefiles/dotlottie-web (newer player)
**License:** MIT
**Size:** ~250kb (lottie-web full), ~60kb (light version)
**Website:** https://lottiefiles.com | https://lottie.github.io

### CDN Links

```html
<!-- lottie-web (Airbnb original) -->
<script src="https://cdnjs.cloudflare.com/ajax/libs/lottie-web/5.13.0/lottie.min.js"></script>

<!-- lottie-web light (SVG only, smaller) -->
<script src="https://cdnjs.cloudflare.com/ajax/libs/lottie-web/5.13.0/lottie_light.min.js"></script>

<!-- DotLottie Web Player (modern, recommended) -->
<script src="https://cdn.jsdelivr.net/npm/@lottiefiles/dotlottie-web@latest/dist/dotlottie-player.js"></script>

<!-- Lottie Player Web Component -->
<script src="https://unpkg.com/@lottiefiles/lottie-player@latest/dist/lottie-player.js"></script>
```

### NPM Install

```bash
npm install lottie-web
# or modern player
npm install @lottiefiles/dotlottie-web
# React component
npm install @lottiefiles/dotlottie-react
```

### lottie-web: loadAnimation API

```javascript
// Basic usage
const animation = lottie.loadAnimation({
  container: document.getElementById('lottie-container'),
  renderer: 'svg',          // 'svg', 'canvas', 'html'
  loop: true,
  autoplay: true,
  path: '/animations/hero.json'    // URL to JSON file
});

// OR with inline data
const animation = lottie.loadAnimation({
  container: document.getElementById('lottie-container'),
  renderer: 'svg',
  loop: false,
  autoplay: false,
  animationData: jsonData    // imported/fetched JSON object
});
```

### Animation Control Methods

```javascript
animation.play();
animation.pause();
animation.stop();
animation.setSpeed(2);            // 2x speed
animation.setDirection(-1);       // reverse
animation.goToAndStop(30, true);  // go to frame 30, true = frame, false = time(ms)
animation.goToAndPlay(0, true);   // go to frame 0 and play
animation.playSegments([0, 60], true);  // play frames 0-60, true = force immediately
animation.setSubframe(false);     // for crisp pixel animations
animation.destroy();              // cleanup

// Properties
animation.totalFrames;   // total number of frames
animation.currentFrame;  // current frame
animation.playSpeed;     // current speed
animation.isPaused;      // boolean
animation.isLoaded;      // boolean
```

### Events

```javascript
animation.addEventListener('complete', () => {});
animation.addEventListener('loopComplete', () => {});
animation.addEventListener('enterFrame', () => {});
animation.addEventListener('segmentStart', () => {});
animation.addEventListener('config_ready', () => {});   // initial config done
animation.addEventListener('data_ready', () => {});     // all data loaded
animation.addEventListener('DOMLoaded', () => {});      // DOM elements created
animation.addEventListener('loaded_images', () => {});  // images loaded
```

### Web Component (lottie-player)

```html
<!-- Simple usage with web component -->
<lottie-player
  src="https://assets.lottiefiles.com/packages/lf20_animation.json"
  background="transparent"
  speed="1"
  style="width: 300px; height: 300px;"
  loop
  autoplay
></lottie-player>

<!-- Interactive hover -->
<lottie-player
  src="animation.json"
  hover
  style="width: 200px; height: 200px;"
></lottie-player>

<!-- With controls visible -->
<lottie-player
  src="animation.json"
  loop
  autoplay
  controls
></lottie-player>
```

### Scroll-Linked Lottie

```javascript
const animation = lottie.loadAnimation({
  container: document.getElementById('scroll-lottie'),
  renderer: 'svg',
  loop: false,
  autoplay: false,
  path: 'scroll-animation.json'
});

// Link to scroll position
window.addEventListener('scroll', () => {
  const scrollPercent = window.scrollY / (document.body.scrollHeight - window.innerHeight);
  const frame = Math.floor(scrollPercent * animation.totalFrames);
  animation.goToAndStop(frame, true);
});

// Or with GSAP ScrollTrigger
gsap.to({ frame: 0 }, {
  frame: animation.totalFrames - 1,
  snap: "frame",
  ease: "none",
  scrollTrigger: {
    trigger: "#lottie-section",
    start: "top top",
    end: "bottom bottom",
    scrub: 0.5
  },
  onUpdate: function() {
    animation.goToAndStop(Math.round(this.targets()[0].frame), true);
  }
});
```

### React Usage

```jsx
import { DotLottieReact } from "@lottiefiles/dotlottie-react";

function AnimatedIcon() {
  return (
    <DotLottieReact
      src="https://lottiefiles.com/animation.lottie"
      loop
      autoplay
      style={{ width: 300, height: 300 }}
    />
  );
}
```

### Renderer Comparison

```
SVG (default):
  + Best feature support, sharp at any scale
  + Supports all AE features
  - Higher CPU usage for complex animations
  - More DOM nodes

Canvas:
  + Better performance for complex animations
  + Fewer DOM nodes
  - No CSS styling on elements
  - Not sharp on retina without scaling

HTML:
  + Supports 3D layers
  + Can be more performant than SVG
  - Least feature support
  - Limited to simple shapes
```

### Performance Considerations

- Use `lottie_light.min.js` (SVG only) when canvas/HTML rendering not needed (~60kb vs ~250kb)
- Use `.lottie` (dotLottie) format over `.json` -- it's compressed and can bundle assets
- Prefer SVG renderer for quality; Canvas for performance-critical animations
- Set `setSubframe(false)` for animations that look better snapped to whole frames
- Destroy animations when they leave view: `animation.destroy()`
- Reduce animation complexity in After Effects to improve playback
- Use `playSegments()` for partial playback instead of full animation

### Where to Get Lottie Animations

- **LottieFiles:** https://lottiefiles.com (largest library, free + premium)
- **IconScout:** https://iconscout.com/lottie-animations
- **Lordicon:** https://lordicon.com (animated icons)
- **Create your own:** Adobe After Effects + Bodymovin plugin
- **Lottie Creator:** https://lottiefiles.com/lottie-creator (browser-based)

### Best Use Cases

- Loading/progress indicators
- Illustrated icons and micro-animations
- Onboarding flows
- Empty states and error pages
- Hero section animations
- Interactive illustrations
- Success/completion feedback

---

## 6. Three.js

**Version:** r182 (0.182.0)
**License:** MIT
**Size:** ~600kb (full), tree-shakeable with bundler
**Website:** https://threejs.org

### CDN Links (Import Map Pattern)

```html
<script type="importmap">
{
  "imports": {
    "three": "https://cdn.jsdelivr.net/npm/three@0.172/build/three.module.js",
    "three/addons/": "https://cdn.jsdelivr.net/npm/three@0.172/examples/jsm/"
  }
}
</script>
<script type="module" src="main.js"></script>
```

### NPM Install

```bash
npm install three
```

### Basic Scene Setup

```javascript
import * as THREE from 'three';
import { OrbitControls } from 'three/addons/controls/OrbitControls.js';

// Scene
const scene = new THREE.Scene();
scene.background = new THREE.Color(0x0a0a0a);
scene.fog = new THREE.Fog(0x0a0a0a, 10, 50);

// Camera
const camera = new THREE.PerspectiveCamera(
  75,                                    // FOV
  window.innerWidth / window.innerHeight, // aspect ratio
  0.1,                                   // near plane
  1000                                   // far plane
);
camera.position.set(0, 2, 5);

// Renderer
const renderer = new THREE.WebGLRenderer({
  antialias: true,
  alpha: true,       // transparent background
  powerPreference: "high-performance"
});
renderer.setSize(window.innerWidth, window.innerHeight);
renderer.setPixelRatio(Math.min(window.devicePixelRatio, 2));
renderer.shadowMap.enabled = true;
renderer.toneMapping = THREE.ACESFilmicToneMapping;
document.body.appendChild(renderer.domElement);

// Controls
const controls = new OrbitControls(camera, renderer.domElement);
controls.enableDamping = true;
controls.dampingFactor = 0.05;

// Lighting
const ambientLight = new THREE.AmbientLight(0xffffff, 0.5);
scene.add(ambientLight);

const directionalLight = new THREE.DirectionalLight(0xffffff, 1);
directionalLight.position.set(5, 5, 5);
directionalLight.castShadow = true;
scene.add(directionalLight);

// Geometry + Material + Mesh
const geometry = new THREE.BoxGeometry(1, 1, 1);
const material = new THREE.MeshStandardMaterial({
  color: 0x88c0d0,
  roughness: 0.3,
  metalness: 0.7
});
const cube = new THREE.Mesh(geometry, material);
cube.castShadow = true;
scene.add(cube);

// Animation loop
function animate() {
  requestAnimationFrame(animate);
  cube.rotation.x += 0.01;
  cube.rotation.y += 0.01;
  controls.update();
  renderer.render(scene, camera);
}
animate();

// Resize handler
window.addEventListener('resize', () => {
  camera.aspect = window.innerWidth / window.innerHeight;
  camera.updateProjectionMatrix();
  renderer.setSize(window.innerWidth, window.innerHeight);
  renderer.setPixelRatio(Math.min(window.devicePixelRatio, 2));
});
```

### Common Geometries

```javascript
new THREE.BoxGeometry(width, height, depth);
new THREE.SphereGeometry(radius, widthSegments, heightSegments);
new THREE.PlaneGeometry(width, height, widthSegments, heightSegments);
new THREE.TorusGeometry(radius, tube, radialSegments, tubularSegments);
new THREE.TorusKnotGeometry(radius, tube, tubularSegments, radialSegments);
new THREE.CylinderGeometry(radiusTop, radiusBottom, height);
new THREE.IcosahedronGeometry(radius, detail);
new THREE.BufferGeometry();  // custom geometry with vertex data
```

### Common Materials

```javascript
new THREE.MeshBasicMaterial({ color: 0xff0000 });           // unlit, flat color
new THREE.MeshStandardMaterial({ color, roughness, metalness }); // PBR standard
new THREE.MeshPhysicalMaterial({ clearcoat, transmission }); // advanced PBR
new THREE.MeshNormalMaterial();                              // debug normals
new THREE.ShaderMaterial({ vertexShader, fragmentShader, uniforms }); // custom GLSL
new THREE.PointsMaterial({ size: 0.02, color: 0xffffff });  // for particle systems
```

### Particle System Pattern

```javascript
const particleCount = 5000;
const positions = new Float32Array(particleCount * 3);

for (let i = 0; i < particleCount * 3; i++) {
  positions[i] = (Math.random() - 0.5) * 20;
}

const geometry = new THREE.BufferGeometry();
geometry.setAttribute('position', new THREE.BufferAttribute(positions, 3));

const material = new THREE.PointsMaterial({
  size: 0.02,
  color: 0x88c0d0,
  transparent: true,
  opacity: 0.8,
  blending: THREE.AdditiveBlending,
  depthWrite: false
});

const particles = new THREE.Points(geometry, material);
scene.add(particles);
```

### Post-Processing

```javascript
import { EffectComposer } from 'three/addons/postprocessing/EffectComposer.js';
import { RenderPass } from 'three/addons/postprocessing/RenderPass.js';
import { UnrealBloomPass } from 'three/addons/postprocessing/UnrealBloomPass.js';

const composer = new EffectComposer(renderer);
composer.addPass(new RenderPass(scene, camera));
composer.addPass(new UnrealBloomPass(
  new THREE.Vector2(window.innerWidth, window.innerHeight),
  1.5,  // strength
  0.4,  // radius
  0.85  // threshold
));

// In animation loop, use composer.render() instead of renderer.render()
```

### 2025-2026 Features

- **WebGPU support:** Three.js now has production-ready WebGPU renderer across all major browsers
- **WebXR:** Unified API for VR/AR experiences
- **Compute shaders:** via WebGPU for GPU-computed physics, particles
- **Node-based materials:** for procedural textures and effects
- **glTF/GLB:** standard 3D format loading with `GLTFLoader`

### Performance Considerations

- Set `renderer.setPixelRatio(Math.min(window.devicePixelRatio, 2))` to cap at 2x
- Use `BufferGeometry` (not the deprecated `Geometry`)
- Merge geometries when possible to reduce draw calls
- Use instanced meshes (`InstancedMesh`) for many identical objects
- Dispose geometries, materials, and textures when removing from scene
- Use LOD (Level of Detail) for complex scenes
- Enable frustum culling (on by default)
- Use compressed textures (KTX2/Basis)
- Profile with `renderer.info` to see draw calls, triangles, etc.

### Best Use Cases

- 3D product viewers and configurators
- Interactive 3D backgrounds
- Data visualization in 3D
- Particle effects and generative art
- WebXR (VR/AR) experiences
- 3D scrollytelling
- Games and interactive experiences
- Architectural visualization

---

## 7. tsParticles

**Version:** 3.x (latest: ~3.8.x)
**License:** MIT
**Size:** Modular (basic ~15kb, full ~50kb)
**Website:** https://particles.js.org

### CDN Links

```html
<!-- Full bundle (all features) -->
<script src="https://cdn.jsdelivr.net/npm/tsparticles@3/tsparticles.bundle.min.js"></script>

<!-- Slim bundle (most common features, smaller) -->
<script src="https://cdn.jsdelivr.net/npm/@tsparticles/slim@3/tsparticles.slim.bundle.min.js"></script>

<!-- Basic bundle (minimal features, smallest) -->
<script src="https://cdn.jsdelivr.net/npm/@tsparticles/basic@3/tsparticles.basic.bundle.min.js"></script>

<!-- Confetti only -->
<script src="https://cdn.jsdelivr.net/npm/@tsparticles/confetti@3/tsparticles.confetti.bundle.min.js"></script>

<!-- Fireworks only -->
<script src="https://cdn.jsdelivr.net/npm/@tsparticles/fireworks@3/tsparticles.fireworks.bundle.min.js"></script>
```

### NPM Install

```bash
npm install tsparticles           # full
npm install @tsparticles/slim     # slim
npm install @tsparticles/basic    # basic
npm install @tsparticles/confetti # confetti only
npm install @tsparticles/react    # React component
npm install @tsparticles/vue3     # Vue 3 component
npm install @tsparticles/svelte   # Svelte component
```

### Basic Usage

```html
<div id="tsparticles"></div>
<script>
  tsParticles.load({
    id: "tsparticles",
    options: {
      background: { color: { value: "#0d1117" } },
      fpsLimit: 120,
      particles: {
        color: { value: "#ffffff" },
        links: {
          color: "#ffffff",
          distance: 150,
          enable: true,
          opacity: 0.3,
          width: 1
        },
        move: {
          enable: true,
          speed: 2,
          direction: "none",
          outModes: { default: "bounce" }
        },
        number: {
          density: { enable: true, area: 800 },
          value: 80
        },
        opacity: { value: 0.5 },
        shape: { type: "circle" },
        size: { value: { min: 1, max: 5 } }
      },
      interactivity: {
        events: {
          onHover: { enable: true, mode: "repulse" },
          onClick: { enable: true, mode: "push" }
        },
        modes: {
          repulse: { distance: 100, duration: 0.4 },
          push: { quantity: 4 }
        }
      },
      detectRetina: true
    }
  });
</script>
```

### Presets

```javascript
// Snow effect
tsParticles.load({
  id: "snow",
  options: {
    preset: "snow"  // requires @tsparticles/preset-snow
  }
});

// Stars
tsParticles.load({
  id: "stars",
  options: {
    preset: "stars"  // requires @tsparticles/preset-stars
  }
});

// Confetti
tsParticles.load({
  id: "confetti",
  options: {
    preset: "confetti"  // requires @tsparticles/preset-confetti
  }
});
```

### Confetti Function

```javascript
// Simple confetti burst
confetti({
  count: 100,
  spread: 70,
  origin: { y: 0.6 }
});

// Custom confetti
confetti({
  particleCount: 100,
  angle: 90,
  spread: 45,
  startVelocity: 45,
  decay: 0.9,
  gravity: 1,
  ticks: 200,
  colors: ['#ff0000', '#00ff00', '#0000ff'],
  shapes: ['circle', 'square'],
  origin: { x: 0.5, y: 0.5 }
});

// Continuous cannon
const emitter = tsParticles.load({
  id: "cannon",
  options: {
    preset: "confetti",
    emitters: {
      life: { duration: 0, count: 0 },  // infinite
      rate: { quantity: 5, delay: 0.1 },
      position: { x: 50, y: 100 }
    }
  }
});
```

### Interactivity Modes

```
Hover modes:  "attract", "bounce", "bubble", "connect", "grab", "repulse", "slow", "trail"
Click modes:  "attract", "bubble", "push", "remove", "repulse", "trail"
```

### React Usage

```jsx
import Particles, { initParticlesEngine } from "@tsparticles/react";
import { loadSlim } from "@tsparticles/slim";
import { useEffect, useState } from "react";

function ParticleBackground() {
  const [init, setInit] = useState(false);

  useEffect(() => {
    initParticlesEngine(async (engine) => {
      await loadSlim(engine);
    }).then(() => setInit(true));
  }, []);

  if (!init) return null;

  return (
    <Particles
      id="tsparticles"
      options={{
        particles: {
          number: { value: 50 },
          color: { value: "#88c0d0" },
          move: { enable: true, speed: 1 },
          opacity: { value: 0.5 },
          size: { value: { min: 1, max: 3 } }
        }
      }}
    />
  );
}
```

### Performance Considerations

- Use the smallest bundle possible (basic > slim > full)
- Limit particle count (50-200 for backgrounds)
- Use `fpsLimit: 60` to avoid excessive rendering
- Enable `detectRetina: true` for proper display but note it doubles particle size
- Reduce link distance and particle count on mobile
- Use `pauseOnBlur: true` and `pauseOnOutsideViewport: true`
- Destroy instance when not needed: `tsParticles.destroy("id")`

### Best Use Cases

- Animated backgrounds (connected dots, floating particles)
- Confetti celebrations
- Snow/rain weather effects
- Fireworks displays
- Interactive cursor trails
- Ambient floating elements
- Hero section atmospherics

---

## 8. Typed.js

**Version:** 2.1.0 (stable) / 3.0.0 (new major)
**License:** MIT
**Size:** ~5kb (minified + gzipped)
**Website:** https://mattboldt.github.io/typed.js/

### CDN Links

```html
<!-- Typed.js v2 (stable) -->
<script src="https://cdn.jsdelivr.net/npm/typed.js@2/dist/typed.umd.js"></script>

<!-- Typed.js v3 (latest) -->
<script src="https://unpkg.com/typed.js@3.0.0/dist/typed.umd.js"></script>
```

### NPM Install

```bash
npm install typed.js
```

### Basic Usage

```html
<span id="typed-output"></span>

<script>
const typed = new Typed('#typed-output', {
  strings: [
    'Build beautiful interfaces.',
    'Create amazing experiences.',
    'Design with intention.'
  ],
  typeSpeed: 50,         // typing speed (ms per character)
  backSpeed: 30,         // backspacing speed
  backDelay: 1500,       // delay before backspacing (ms)
  startDelay: 500,       // delay before typing starts
  loop: true,            // loop through strings
  loopCount: Infinity,   // number of loops (Infinity = forever)
  showCursor: true,      // show blinking cursor
  cursorChar: '|',       // cursor character
  smartBackspace: true,  // only backspace what doesn't match next string
  shuffle: false,        // shuffle the strings
  fadeOut: false,         // fade out instead of backspace
  fadeOutClass: 'typed-fade-out',
  fadeOutDelay: 500
});
</script>
```

### HTML Strings (Type HTML Tags)

```javascript
new Typed('#output', {
  strings: [
    '<strong>Bold text</strong> and <em>italic</em>.',
    '<span style="color: #88c0d0;">Colored text</span>.',
    'Regular text with <br>line break.'
  ],
  contentType: 'html',  // 'html' or 'null' for plaintext
  typeSpeed: 40
});
```

### Using HTML Element as Source

```html
<span id="typed-output"></span>
<div id="typed-strings">
  <p>First string from HTML.</p>
  <p>Second string from HTML.</p>
  <p>Third string <strong>with HTML</strong>.</p>
</div>

<script>
new Typed('#typed-output', {
  stringsElement: '#typed-strings',
  typeSpeed: 50
});
</script>
```

### Callbacks & Methods

```javascript
const typed = new Typed('#output', {
  strings: ['Hello World'],
  typeSpeed: 50,

  // Callbacks
  onBegin: (self) => {},        // before typing begins
  onComplete: (self) => {},     // after all strings typed
  preStringTyped: (arrayPos, self) => {},   // before each string
  onStringTyped: (arrayPos, self) => {},    // after each string
  onLastStringBackspaced: (self) => {},     // after last string backspaced
  onTypingPaused: (arrayPos, self) => {},   // during typing pause
  onTypingResumed: (arrayPos, self) => {},  // after pause resumes
  onReset: (self) => {},        // after reset
  onStop: (arrayPos, self) => {},  // after stop
  onStart: (arrayPos, self) => {} // after start
});

// Control methods
typed.toggle();     // toggle between typing/not
typed.stop();       // stop typing
typed.start();      // start typing
typed.destroy();    // destroy instance, remove cursor
typed.reset();      // reset to beginning
```

### Pause/Resume with Caret Notation

```javascript
new Typed('#output', {
  strings: [
    'Wait for it...^1000 BOOM!',       // ^1000 = 1 second pause
    'First part^500 then second^1000 then third.'
  ],
  typeSpeed: 50
});
```

### Smart Backspace Example

```javascript
// With smartBackspace: true (default)
// Strings: "I love coding" → "I love design"
// Only backspaces "coding" and types "design", keeps "I love "
new Typed('#output', {
  strings: ['I love coding.', 'I love design.', 'I love creating.'],
  smartBackspace: true,
  typeSpeed: 50,
  backSpeed: 30
});
```

### Custom Cursor Styling

```css
.typed-cursor {
  font-weight: 100;
  font-size: 1.1em;
  color: #88c0d0;
  animation: typedjsBlink 0.7s infinite;
}

@keyframes typedjsBlink {
  50% { opacity: 0; }
}
```

### Performance Considerations

- Extremely lightweight (~5kb)
- Uses `setTimeout`/`requestAnimationFrame` for typing simulation
- Destroy instance when component unmounts to prevent memory leaks
- No dependencies
- Minimal DOM manipulation (single text node updates)

### Best Use Cases

- Hero section dynamic text
- Terminal/console-style typing effects
- Interactive storytelling
- Job title / skill cycling
- Command-line interfaces
- Chatbot message simulation
- Developer portfolio pages

---

## 9. Swiper.js

**Version:** 12.x (latest: 12.1.0, released 2026-01-29)
**License:** MIT
**Size:** ~40kb core (modular, tree-shakeable)
**Website:** https://swiperjs.com

### CDN Links

```html
<!-- CSS (all styles including effects) -->
<link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/swiper@12/swiper-bundle.min.css">

<!-- JavaScript (all modules) -->
<script src="https://cdn.jsdelivr.net/npm/swiper@12/swiper-bundle.min.js"></script>

<!-- OR modular CSS imports -->
<link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/swiper@12/modules/navigation.min.css">
<link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/swiper@12/modules/pagination.min.css">
<link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/swiper@12/modules/effect-coverflow.min.css">
```

### NPM Install

```bash
npm install swiper
```

### Basic HTML Structure

```html
<div class="swiper">
  <div class="swiper-wrapper">
    <div class="swiper-slide">Slide 1</div>
    <div class="swiper-slide">Slide 2</div>
    <div class="swiper-slide">Slide 3</div>
  </div>
  <div class="swiper-pagination"></div>
  <div class="swiper-button-prev"></div>
  <div class="swiper-button-next"></div>
  <div class="swiper-scrollbar"></div>
</div>
```

### JavaScript Initialization

```javascript
const swiper = new Swiper('.swiper', {
  // Core
  direction: 'horizontal',    // 'horizontal' or 'vertical'
  slidesPerView: 1,
  spaceBetween: 30,
  speed: 600,
  loop: true,
  centeredSlides: true,
  grabCursor: true,
  freeMode: true,

  // Autoplay
  autoplay: {
    delay: 3000,
    disableOnInteraction: false,
    pauseOnMouseEnter: true
  },

  // Pagination
  pagination: {
    el: '.swiper-pagination',
    clickable: true,
    type: 'bullets',         // 'bullets', 'fraction', 'progressbar', 'custom'
    dynamicBullets: true
  },

  // Navigation
  navigation: {
    nextEl: '.swiper-button-next',
    prevEl: '.swiper-button-prev'
  },

  // Scrollbar
  scrollbar: {
    el: '.swiper-scrollbar',
    draggable: true
  },

  // Breakpoints
  breakpoints: {
    640: { slidesPerView: 2, spaceBetween: 20 },
    768: { slidesPerView: 3, spaceBetween: 30 },
    1024: { slidesPerView: 4, spaceBetween: 40 }
  },

  // Keyboard
  keyboard: { enabled: true, onlyInViewport: true },

  // Mousewheel
  mousewheel: { forceToAxis: true },

  // Parallax
  parallax: true
});
```

### Effect Types

```javascript
// Fade effect
new Swiper('.swiper', {
  effect: 'fade',
  fadeEffect: { crossFade: true }
});

// Cube effect
new Swiper('.swiper', {
  effect: 'cube',
  cubeEffect: {
    shadow: true,
    slideShadows: true,
    shadowOffset: 20,
    shadowScale: 0.94
  }
});

// Coverflow effect
new Swiper('.swiper', {
  effect: 'coverflow',
  centeredSlides: true,
  slidesPerView: 'auto',
  coverflowEffect: {
    rotate: 50,
    stretch: 0,
    depth: 100,
    modifier: 1,
    slideShadows: true
  }
});

// Flip effect
new Swiper('.swiper', {
  effect: 'flip',
  flipEffect: { slideShadows: true, limitRotation: true }
});

// Cards effect
new Swiper('.swiper', {
  effect: 'cards',
  cardsEffect: { perSlideOffset: 8, perSlideRotate: 2 }
});

// Creative effect (custom transforms)
new Swiper('.swiper', {
  effect: 'creative',
  creativeEffect: {
    prev: {
      shadow: true,
      translate: [0, 0, -400]
    },
    next: {
      translate: ['100%', 0, 0]
    }
  }
});
```

### Parallax Content

```html
<div class="swiper">
  <div class="parallax-bg" data-swiper-parallax="-23%"></div>
  <div class="swiper-wrapper">
    <div class="swiper-slide">
      <div class="title" data-swiper-parallax="-300">Slide Title</div>
      <div class="subtitle" data-swiper-parallax="-200">Subtitle</div>
      <div class="text" data-swiper-parallax="-100">
        <p>Paragraph text here</p>
      </div>
    </div>
  </div>
</div>
```

### Web Component Usage

```html
<swiper-container
  slides-per-view="3"
  space-between="30"
  navigation="true"
  pagination="true"
  loop="true"
>
  <swiper-slide>Slide 1</swiper-slide>
  <swiper-slide>Slide 2</swiper-slide>
  <swiper-slide>Slide 3</swiper-slide>
</swiper-container>
```

### React Usage

```jsx
import { Swiper, SwiperSlide } from 'swiper/react';
import { Navigation, Pagination, EffectCoverflow, Autoplay } from 'swiper/modules';
import 'swiper/css';
import 'swiper/css/navigation';
import 'swiper/css/pagination';
import 'swiper/css/effect-coverflow';

function Gallery() {
  return (
    <Swiper
      modules={[Navigation, Pagination, EffectCoverflow, Autoplay]}
      effect="coverflow"
      grabCursor={true}
      centeredSlides={true}
      slidesPerView="auto"
      coverflowEffect={{ rotate: 50, stretch: 0, depth: 100, modifier: 1 }}
      pagination={{ clickable: true }}
      navigation={true}
      autoplay={{ delay: 3000 }}
    >
      <SwiperSlide><img src="image1.jpg" /></SwiperSlide>
      <SwiperSlide><img src="image2.jpg" /></SwiperSlide>
    </Swiper>
  );
}
```

### Available Modules

```
Navigation, Pagination, Scrollbar, Autoplay,
FreeMode, Grid, Manipulation, Parallax, Zoom,
Keyboard, Mousewheel, Virtual, Thumbs,
EffectFade, EffectCube, EffectFlip, EffectCoverflow, EffectCards, EffectCreative,
Controller, A11y, History, HashNavigation
```

### Methods & Properties

```javascript
swiper.slideNext();           // go to next slide
swiper.slidePrev();           // go to previous slide
swiper.slideTo(index);        // go to specific slide
swiper.update();              // update after DOM changes
swiper.destroy();             // destroy instance
swiper.activeIndex;           // current active slide index
swiper.realIndex;             // real index (accounts for loop)
swiper.isBeginning;           // is at first slide
swiper.isEnd;                 // is at last slide

// Events
swiper.on('slideChange', () => {});
swiper.on('reachEnd', () => {});
swiper.on('progress', (swiper, progress) => {});
```

### Performance Considerations

- Import only needed modules (not the full bundle) for tree-shaking
- Use `virtual: true` for many slides (renders only visible)
- Lazy load images with `loading="lazy"` on img tags
- `preloadImages: false` to prevent loading all images upfront
- Use CSS-based transitions (hardware accelerated)
- V12: Moved to CSS-only styles (removed LESS/SCSS for smaller bundles)
- V12: SVG icons for navigation (smaller than font icons)

### Best Use Cases

- Image galleries and portfolios
- Product carousels
- Testimonial sliders
- Full-screen hero sections
- Card-based layouts
- Mobile app-like swipe interfaces
- Creative transition showcases
- Thumbnail navigation galleries

---

## 10. Locomotive Scroll

**Version:** 5.x (latest: 5.0.x)
**License:** MIT
**Size:** ~9.4kb (minified + gzipped)
**Website:** https://scroll.locomotive.ca

### CDN Links

```html
<!-- V5 (built on Lenis) -->
<script src="https://cdn.jsdelivr.net/npm/locomotive-scroll@5/dist/locomotive-scroll.min.js"></script>

<!-- V4 (legacy, widely used) -->
<link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/locomotive-scroll@4/dist/locomotive-scroll.min.css">
<script src="https://cdn.jsdelivr.net/npm/locomotive-scroll@4/dist/locomotive-scroll.min.js"></script>

<!-- Lenis (the underlying smooth scroll engine in v5) -->
<script src="https://cdn.jsdelivr.net/npm/lenis@latest/dist/lenis.min.js"></script>
```

### NPM Install

```bash
npm install locomotive-scroll  # v5
npm install lenis              # standalone Lenis (lighter alternative)
```

### V5 Basic Setup

```javascript
import LocomotiveScroll from 'locomotive-scroll';

const scroll = new LocomotiveScroll({
  lenisOptions: {
    lerp: 0.1,              // linear interpolation (0-1, lower = smoother)
    duration: 1.2,           // scroll duration
    orientation: 'vertical', // 'vertical' or 'horizontal'
    gestureOrientation: 'vertical',
    smoothWheel: true,
    smoothTouch: false,      // native touch recommended
    wheelMultiplier: 1,
    touchMultiplier: 2
  }
});

// Custom scroll container (not default window)
const scroll = new LocomotiveScroll({
  lenisOptions: {
    wrapper: document.querySelector('.scroll-wrapper'),
    content: document.querySelector('.scroll-content')
  }
});
```

### V5 HTML Attributes

```html
<!-- Detect when element enters viewport -->
<div data-scroll>I will be detected</div>

<!-- Parallax speed -->
<div data-scroll data-scroll-speed="2">Fast parallax</div>
<div data-scroll data-scroll-speed="0.5">Slow parallax</div>
<div data-scroll data-scroll-speed="-1">Reverse parallax</div>

<!-- Parallax on desktop only -->
<div data-scroll data-scroll-speed="2" data-scroll-enable-touch-speed>
  Parallax on all devices
</div>

<!-- Custom scroll position for animation -->
<div data-scroll data-scroll-position="top">
  Triggers relative to viewport top
</div>

<!-- Repeat animation -->
<div data-scroll data-scroll-repeat>
  Animates every time it enters viewport
</div>

<!-- Scroll call (custom event) -->
<div data-scroll data-scroll-call="myEvent">
  Fires "myEvent" when in view
</div>

<!-- Offset -->
<div data-scroll data-scroll-offset="200">
  200px offset before triggering
</div>
```

### V5 Scroll Events

```javascript
const scroll = new LocomotiveScroll();

// Listen to scroll
scroll.on('scroll', (args) => {
  console.log(args.scroll);     // current scroll position
  console.log(args.limit);      // max scroll
  console.log(args.velocity);   // scroll velocity
  console.log(args.direction);  // 1 (down) or -1 (up)
  console.log(args.progress);   // 0 to 1
});

// Scroll call events
scroll.on('call', (value, way, obj) => {
  if (value === 'myEvent') {
    if (way === 'enter') { /* element entered view */ }
    if (way === 'exit') { /* element exited view */ }
  }
});

// Scroll to
scroll.scrollTo(targetElement);
scroll.scrollTo('#section-2');
scroll.scrollTo(500);            // px position
scroll.scrollTo('top');
scroll.scrollTo('bottom');

// Control
scroll.start();
scroll.stop();
scroll.destroy();
```

### V4 Setup (Legacy but Common)

```html
<div data-scroll-container>
  <section data-scroll-section>
    <h1 data-scroll data-scroll-speed="3">Parallax Title</h1>
    <div data-scroll data-scroll-speed="1" data-scroll-direction="horizontal">
      Horizontal parallax
    </div>
    <div data-scroll data-scroll-sticky data-scroll-target="#sticky-trigger">
      Sticky element
    </div>
  </section>
</div>
```

```javascript
const scroll = new LocomotiveScroll({
  el: document.querySelector('[data-scroll-container]'),
  smooth: true,
  lerp: 0.06,
  multiplier: 1,
  smartphone: { smooth: false },
  tablet: { smooth: false, breakpoint: 1024 }
});
```

### Using Lenis Directly (Lighter Alternative)

```javascript
import Lenis from 'lenis';

const lenis = new Lenis({
  duration: 1.2,
  easing: (t) => Math.min(1, 1.001 - Math.pow(2, -10 * t)),
  orientation: 'vertical',
  smoothWheel: true
});

function raf(time) {
  lenis.raf(time);
  requestAnimationFrame(raf);
}
requestAnimationFrame(raf);

// Scroll to
lenis.scrollTo('#target', { offset: -100, duration: 2 });

// With GSAP ticker (better)
gsap.ticker.add((time) => {
  lenis.raf(time * 1000);
});
gsap.ticker.lagSmoothing(0);
```

### V5 Migration Notes (from V4)

```
V4                              V5
---                             ---
data-scroll-container           No longer needed (uses window by default)
data-scroll-section             No longer needed
data-scroll-direction           Removed (use CSS transforms)
data-scroll-sticky              Removed (use CSS sticky)
el: element                     lenisOptions.wrapper / lenisOptions.content
smooth: true                    lenisOptions.smoothWheel: true
lerp: 0.1                       lenisOptions.lerp: 0.1
```

### Performance Considerations

- V5 is built on Lenis which is more performant than V4
- Lightweight at 9.4kb (gzipped)
- Uses dual Intersection Observer strategy for efficient detection
- Parallax auto-disabled on touch devices by default (prevents jank)
- Smart touch detection to maintain 60fps on mobile
- Use CSS `will-change: transform` on parallax elements
- Destroy instance on component unmount for SPA cleanup
- Keyboard navigation and native scrollbar preserved (accessibility)

### Best Use Cases

- Smooth scrolling portfolio sites
- Parallax storytelling pages
- Creative agency websites
- Long-form editorial content
- Product showcases with scroll-driven animation
- Full-page experiences with custom scroll behavior

---

## 11. Splitting.js

**Version:** 1.1.0
**License:** MIT
**Size:** ~1.5kb (minified + gzipped)
**Website:** https://splitting.js.org

### CDN Links

```html
<!-- CSS (required for default styles) -->
<link rel="stylesheet" href="https://unpkg.com/splitting/dist/splitting.css">

<!-- CSS for cells/grid splitting (optional) -->
<link rel="stylesheet" href="https://unpkg.com/splitting/dist/splitting-cells.css">

<!-- JavaScript -->
<script src="https://unpkg.com/splitting/dist/splitting.min.js"></script>
```

### NPM Install

```bash
npm install splitting
```

### Basic Usage

```javascript
import Splitting from 'splitting';
import 'splitting/dist/splitting.css';

// Split all elements with data-splitting attribute
Splitting();

// Split specific element
Splitting({ target: '.headline' });

// Split with options
const results = Splitting({
  target: '.text',
  by: 'chars'       // 'chars', 'words', 'lines', 'items', 'grid', 'cols', 'rows', 'cellRows', 'cellCols', 'cells'
});
```

### HTML Usage

```html
<!-- Data attribute approach -->
<h1 data-splitting>Hello World</h1>
<p data-splitting="words">Split by words</p>
<p data-splitting="lines">Split by lines</p>

<script>
  Splitting();
</script>
```

### Generated Output

For `<h1 data-splitting>Hello</h1>`, Splitting generates:

```html
<h1 data-splitting="chars" class="splitting chars" style="--word-count: 1; --char-count: 5;">
  <span class="word" data-word="Hello" style="--word-index: 0;">
    <span class="char" data-char="H" style="--char-index: 0;">H</span>
    <span class="char" data-char="e" style="--char-index: 1;">e</span>
    <span class="char" data-char="l" style="--char-index: 2;">l</span>
    <span class="char" data-char="l" style="--char-index: 3;">l</span>
    <span class="char" data-char="o" style="--char-index: 4;">o</span>
  </span>
</h1>
```

### CSS Variables Created

```css
/* Available CSS variables per element */
--word-count      /* total words */
--char-count      /* total characters */
--word-index      /* index of current word */
--char-index      /* index of current character */
--line-index      /* index of current line */

/* For grid/cells splitting */
--row-count
--col-count
--row-index
--col-index
--cell-count
--cell-index
```

### CSS-Only Animations Using Variables

```css
/* Staggered character reveal */
.splitting .char {
  opacity: 0;
  transform: translateY(20px);
  animation: charReveal 0.5s cubic-bezier(0.16, 1, 0.3, 1) both;
  animation-delay: calc(var(--char-index) * 0.03s);
}

@keyframes charReveal {
  to {
    opacity: 1;
    transform: translateY(0);
  }
}

/* Wave animation */
.splitting .char {
  animation: wave 2s ease-in-out infinite;
  animation-delay: calc(var(--char-index) * 0.1s);
}

@keyframes wave {
  0%, 100% { transform: translateY(0); }
  50% { transform: translateY(-10px); }
}

/* Color gradient across characters */
.splitting .char {
  color: hsl(calc(var(--char-index) * 30), 70%, 60%);
}

/* Grid reveal */
.splitting.cells .cell {
  opacity: 0;
  animation: cellReveal 0.4s ease both;
  animation-delay: calc(var(--cell-index) * 0.05s);
}
@keyframes cellReveal {
  to { opacity: 1; }
}
```

### With GSAP

```javascript
const results = Splitting({ target: '.headline', by: 'chars' });

gsap.from(results[0].chars, {
  opacity: 0,
  y: 40,
  rotateX: -90,
  stagger: 0.03,
  duration: 0.6,
  ease: "back.out(1.7)"
});
```

### With Anime.js

```javascript
const results = Splitting({ target: '.headline', by: 'chars' });

animate(results[0].chars, {
  opacity: [0, 1],
  translateY: [40, 0],
  delay: stagger(30),
  duration: 600,
  ease: 'outExpo'
});
```

### Splitting Types

```
chars     - Split text into individual characters
words     - Split text into words
lines     - Split text into lines (requires element to have defined width)
items     - Index child elements
grid      - Overlay grid on element
cols      - Grid columns
rows      - Grid rows
cells     - Grid cells
cellRows  - Grid cells by row
cellCols  - Grid cells by column
```

### Performance Considerations

- Extremely lightweight (1.5kb)
- No animation engine -- purely splits DOM and sets CSS variables
- Pair with CSS animations for zero-JS motion
- Pair with GSAP/anime.js for complex sequences
- Splits happen synchronously, so run on load or after DOM ready
- Re-run `Splitting()` after dynamic content changes
- Many small DOM elements can impact layout performance for very long text

### Best Use Cases

- Character-by-character text reveal animations
- Staggered text animations (headlines, hero text)
- Color gradients across text characters
- Wave/ripple text effects
- Image grid reveal effects
- Creative typography effects
- CSS-only animation when combined with CSS variables

### Alternatives

- **GSAP SplitText** (now free): More features, auto re-split on resize, masking, accessibility
- **SplitType**: Inspired by SplitText, supports lines/words/chars
- **splitbun**: Modern alternative
- **Motion splitText**: Available in motion.dev

---

## 12. AutoAnimate

**Version:** 0.9.0
**License:** MIT
**Size:** ~2kb (minified + gzipped)
**Website:** https://auto-animate.formkit.com

### CDN Links

```html
<!-- ES Module -->
<script type="module">
  import autoAnimate from 'https://cdn.jsdelivr.net/npm/@formkit/auto-animate@0.9.0/index.mjs';
</script>

<!-- UMD -->
<script src="https://cdn.jsdelivr.net/npm/@formkit/auto-animate@0.9.0/dist/auto-animate.umd.js"></script>
```

### NPM Install

```bash
npm install @formkit/auto-animate
```

### Vanilla JS Usage

```javascript
import autoAnimate from '@formkit/auto-animate';

// Single function call -- that's it!
autoAnimate(document.getElementById('list'));

// With options
autoAnimate(document.getElementById('list'), {
  duration: 250,                  // animation duration (ms)
  easing: 'ease-in-out',         // easing function
  disrespectUserMotionPreference: false  // respect prefers-reduced-motion
});

// Enable/disable
const controller = autoAnimate(element);
controller.enable();
controller.disable();
```

### What Gets Animated

AutoAnimate watches for three DOM changes and animates them:
1. **Child added** -- fades/scales in
2. **Child removed** -- fades/scales out
3. **Child moved** -- slides to new position (FLIP animation)

```html
<!-- Any list/container that changes dynamically -->
<ul id="todo-list">
  <li>Buy groceries</li>
  <li>Walk the dog</li>
  <li>Read a book</li>
</ul>

<script>
  autoAnimate(document.getElementById('todo-list'));
  // Now adding, removing, or reordering <li> items will animate automatically
</script>
```

### React Usage

```jsx
import { useAutoAnimate } from '@formkit/auto-animate/react';

function TodoList() {
  const [items, setItems] = useState(['Item 1', 'Item 2', 'Item 3']);
  const [parent, enableAnimations] = useAutoAnimate();

  const addItem = () => setItems([...items, `Item ${items.length + 1}`]);
  const removeItem = (i) => setItems(items.filter((_, idx) => idx !== i));

  return (
    <ul ref={parent}>
      {items.map((item, i) => (
        <li key={item} onClick={() => removeItem(i)}>
          {item}
        </li>
      ))}
      <button onClick={addItem}>Add</button>
    </ul>
  );
}
```

### Vue Usage

```vue
<template>
  <ul v-auto-animate>
    <li v-for="item in items" :key="item.id">{{ item.text }}</li>
  </ul>
</template>

<script setup>
import { vAutoAnimate } from '@formkit/auto-animate/vue';
const items = ref([...]);
</script>

<!-- Or with global registration in plugin -->
<!-- app.use(autoAnimatePlugin) then use v-auto-animate anywhere -->
```

### Svelte Usage

```svelte
<script>
  import autoAnimate from '@formkit/auto-animate';
  function animate(node) {
    autoAnimate(node);
  }
</script>

<ul use:animate>
  {#each items as item (item.id)}
    <li>{item.text}</li>
  {/each}
</ul>
```

### Custom Animation with Keyframes

```javascript
autoAnimate(element, (el, action, oldCoords, newCoords) => {
  let keyframes;

  if (action === 'add') {
    keyframes = [
      { transform: 'scale(0)', opacity: 0 },
      { transform: 'scale(1)', opacity: 1 }
    ];
  }

  if (action === 'remove') {
    keyframes = [
      { transform: 'scale(1)', opacity: 1 },
      { transform: 'scale(0)', opacity: 0 }
    ];
  }

  if (action === 'remain') {
    // FLIP animation for moved elements
    const deltaX = oldCoords.left - newCoords.left;
    const deltaY = oldCoords.top - newCoords.top;
    keyframes = [
      { transform: `translate(${deltaX}px, ${deltaY}px)` },
      { transform: 'translate(0, 0)' }
    ];
  }

  return new KeyframeEffect(el, keyframes, {
    duration: 300,
    easing: 'ease-out'
  });
});
```

### Performance Considerations

- Incredibly lightweight (~2kb)
- Uses Web Animations API (hardware accelerated)
- Uses MutationObserver to detect DOM changes (no polling)
- FLIP technique for position changes
- Respects `prefers-reduced-motion` by default
- Zero config needed for basic usage
- Only animates direct children of the targeted parent

### Best Use Cases

- Todo lists, sortable lists, any reorderable content
- Shopping carts (add/remove items)
- Notification stacks
- Tab content transitions
- Accordion content
- Search results that filter/sort
- Any dynamic list where items are added, removed, or reordered
- When you want animation without configuring anything

---

## 13. Native CSS Animation Techniques (2025-2026)

### Scroll-Driven Animations (CSS-only)

```css
/* Scroll progress indicator */
.progress-bar {
  position: fixed;
  top: 0;
  left: 0;
  width: 100%;
  height: 4px;
  background: #88c0d0;
  transform-origin: left;
  animation: grow-progress linear both;
  animation-timeline: scroll();
}

@keyframes grow-progress {
  from { transform: scaleX(0); }
  to { transform: scaleX(1); }
}

/* Element reveal on scroll (view-based timeline) */
.reveal-element {
  animation: reveal linear both;
  animation-timeline: view();
  animation-range: entry 0% entry 100%;
}

@keyframes reveal {
  from {
    opacity: 0;
    transform: translateY(50px);
  }
  to {
    opacity: 1;
    transform: translateY(0);
  }
}

/* Parallax with scroll-driven animations */
.parallax-element {
  animation: parallax linear both;
  animation-timeline: scroll();
}

@keyframes parallax {
  from { transform: translateY(0); }
  to { transform: translateY(-200px); }
}
```

### View Transitions API

```css
/* Page transition */
::view-transition-old(root) {
  animation: fade-out 0.3s ease-out;
}
::view-transition-new(root) {
  animation: fade-in 0.3s ease-in;
}

/* Named view transitions for specific elements */
.hero-image {
  view-transition-name: hero;
}
::view-transition-old(hero) {
  animation: scale-down 0.4s ease-out;
}
::view-transition-new(hero) {
  animation: scale-up 0.4s ease-in;
}
```

```javascript
// Triggering a view transition
document.startViewTransition(() => {
  // Update DOM here
  updateContent();
});
```

### CSS sibling-index() and sibling-count() (Chrome 2025+)

```css
/* Auto-staggered animations with pure CSS */
.item {
  animation: fadeInUp 0.5s ease both;
  animation-delay: calc(sibling-index() * 0.05s);
}

/* Distribute colors across siblings */
.item {
  --hue: calc(360 / sibling-count() * sibling-index());
  background: hsl(var(--hue), 70%, 60%);
}
```

### Path-Based Motion (offset-path)

```css
/* Animate element along a custom path */
.moving-element {
  offset-path: path('M 0 0 C 100 200, 300 0, 400 200');
  animation: followPath 3s ease-in-out infinite;
}

@keyframes followPath {
  0% { offset-distance: 0%; }
  100% { offset-distance: 100%; }
}
```

### @starting-style (Entry Animations)

```css
/* Animate elements when they first appear */
.dialog {
  opacity: 1;
  transform: scale(1);
  transition: opacity 0.3s, transform 0.3s;

  @starting-style {
    opacity: 0;
    transform: scale(0.9);
  }
}

/* Works for elements added to DOM or display changes */
.notification {
  display: block;
  opacity: 1;
  translate: 0;
  transition: opacity 0.4s, translate 0.4s, display 0.4s allow-discrete;

  @starting-style {
    opacity: 0;
    translate: 0 20px;
  }

  &.hidden {
    display: none;
    opacity: 0;
    translate: 0 -20px;
  }
}
```

### interpolate-size (Animate to/from auto)

```css
/* NEW: Animate height to/from auto */
:root {
  interpolate-size: allow-keywords;
}

.collapsible {
  height: 0;
  overflow: hidden;
  transition: height 0.3s ease;
}
.collapsible.open {
  height: auto;  /* Now animatable! */
}
```

### Discrete Property Transitions (display, content-visibility)

```css
/* Animate display: none to display: block */
.element {
  transition: opacity 0.3s, display 0.3s allow-discrete;
  opacity: 1;
}
.element.hidden {
  opacity: 0;
  display: none;
}
```

---

## 14. Animation Trends & Best Practices (2025-2026)

### Key Trends

1. **Scroll-Driven Storytelling**: Full-page experiences where scrolling drives narrative, with pinned sections, parallax layers, and progressive reveals. GSAP ScrollTrigger remains the gold standard; CSS `animation-timeline: scroll()` is catching up.

2. **Micro-Interactions Everywhere**: Buttons that breathe, cards that tilt on hover, cursors that morph. Small, meaningful feedback that makes interfaces feel alive.

3. **3D Elements Integrated in 2D Layouts**: Subtle 3D objects (Three.js) embedded in otherwise 2D pages. Rotating product models, floating geometric shapes, parallax depth.

4. **Kinetic Typography**: Text that moves, splits, reveals character by character. SplitText (GSAP), Splitting.js, and Motion's `splitText` enable this.

5. **Scroll-Triggered Animations (CSS-native, 2026)**: Chrome 145 introduces true scroll-triggered animations -- time-based animations that START when a scroll threshold is crossed, different from scroll-driven animations that are LINKED to scroll position.

6. **View Transitions API**: Seamless page-to-page transitions for MPAs and SPAs. Shared element transitions between pages.

7. **Spring Physics**: Motion, GSAP, and anime.js v4 all support spring-based easing for natural, organic movement that feels responsive.

8. **Reduced Motion Awareness**: Always respect `prefers-reduced-motion`. Provide meaningful alternatives, not just disabling all animation.

9. **WebGPU-Powered Effects**: Three.js with WebGPU for compute shader particles, post-processing, and complex visual effects at higher performance.

10. **AI-Generated Motion Design**: Tools generating Lottie animations and motion parameters from descriptions. Lower barrier to entry for complex animations.

### Performance Best Practices

```css
/* Promote to compositor layer for smooth animations */
.animated {
  will-change: transform, opacity;
  /* Remove will-change after animation completes if possible */
}

/* Only animate compositor-friendly properties */
/* FAST: transform, opacity, filter, clip-path */
/* SLOW: width, height, top, left, margin, padding, border */

/* Respect user preferences */
@media (prefers-reduced-motion: reduce) {
  *, *::before, *::after {
    animation-duration: 0.01ms !important;
    animation-iteration-count: 1 !important;
    transition-duration: 0.01ms !important;
    scroll-behavior: auto !important;
  }
}
```

### Library Selection Guide

| Need | Recommended Library |
|------|-------------------|
| Complex sequenced animations | GSAP |
| Scroll-driven experiences | GSAP ScrollTrigger |
| React component animations | Motion (framer-motion) |
| Lightweight general animation | Anime.js |
| Quick scroll reveals (no-code) | AOS |
| Vector/icon animations | Lottie |
| 3D scenes and effects | Three.js |
| Particle backgrounds | tsParticles |
| Typewriter text effects | Typed.js |
| Image carousels/sliders | Swiper.js |
| Smooth scroll + parallax | Locomotive Scroll / Lenis |
| Text splitting for animation | Splitting.js / GSAP SplitText |
| Zero-config list animations | AutoAnimate |
| CSS-only scroll animations | Native scroll-driven animations |
| Page transitions | View Transitions API |
| Layout animations (React) | Motion layout / layoutId |

### Creative Combination Patterns

**Pattern 1: Smooth scroll + parallax + text reveals**
```
Lenis/Locomotive Scroll + GSAP ScrollTrigger + SplitText
```

**Pattern 2: React SPA with rich animations**
```
Motion (framer-motion) + Three.js (3D accents) + Lottie (icons)
```

**Pattern 3: Marketing landing page**
```
AOS (quick reveals) + Typed.js (hero text) + Swiper (testimonials) + Lottie (illustrations)
```

**Pattern 4: Creative portfolio**
```
GSAP (master timeline) + ScrollTrigger (scroll control) + Splitting.js (text effects) + Three.js (3D hero)
```

**Pattern 5: Lightweight animated site**
```
Anime.js (animations) + AutoAnimate (list transitions) + CSS scroll-driven animations
```
