---
name: modern-ui-ux
description: Comprehensive modern UI/UX design skill covering design thinking, visual hierarchy, typography, color theory, scroll-driven storytelling, immersive animations (GSAP, anime.js, Lenis), 3D web experiences (Three.js, React Three Fiber), Apple-style scroll techniques, micro-interactions, creative layout patterns, and Awwwards-level web design. Use this skill for ALL creative web design, landing pages, portfolios, and immersive web experiences.
---

# Modern UI/UX Design System

This skill provides deep design knowledge and creative direction for building distinctive, immersive web experiences. It covers design theory, scroll storytelling, 3D integration, advanced animation orchestration, and the patterns behind award-winning websites.

---

## Part 1: Design Foundations

### Visual Hierarchy

Visual hierarchy controls what users see first, second, and third. Every element competes for attention. Design decides who wins.

**The hierarchy stack (strongest to weakest):**
1. **Size & scale** - Largest element dominates. Use extreme scale contrast (3x-5x jumps)
2. **Color & contrast** - High-contrast accent on neutral field commands immediate focus
3. **Position** - Top-left (LTR languages) scans first. Above-fold content is premium real estate
4. **Typography weight** - Bold 900 vs thin 200 creates clear levels
5. **Whitespace** - Isolation makes elements important. More space = more significance
6. **Motion** - The only moving element on a static page wins every time

**The 60-30-10 rule:**
- 60% dominant color (backgrounds, large surfaces)
- 30% secondary (cards, sections, supporting elements)
- 10% accent (CTAs, highlights, interactive elements)

### Typography System

Typography is the single biggest signal of design quality. Bad fonts make good design look amateur.

**Type scale using the golden ratio (1.618):**
```css
:root {
  --step--2: clamp(0.69rem, 0.66rem + 0.18vw, 0.80rem);
  --step--1: clamp(0.83rem, 0.78rem + 0.29vw, 1.00rem);
  --step-0:  clamp(1.00rem, 0.91rem + 0.43vw, 1.25rem);   /* body */
  --step-1:  clamp(1.20rem, 1.07rem + 0.63vw, 1.56rem);
  --step-2:  clamp(1.44rem, 1.26rem + 0.89vw, 1.95rem);
  --step-3:  clamp(1.73rem, 1.48rem + 1.24vw, 2.44rem);
  --step-4:  clamp(2.07rem, 1.73rem + 1.70vw, 3.05rem);
  --step-5:  clamp(2.49rem, 2.03rem + 2.31vw, 3.82rem);   /* hero */
}
```

**Font pairing strategy:**
- Pick ONE distinctive display font for headings
- Pair with a clean, readable body font
- Never use more than 2-3 fonts
- Contrast serif + sans-serif, or geometric + humanist
- Load weights at extremes: 200/300 for body elegance, 700/800/900 for headline impact

**Line height by context:**
- Headings: 1.0 - 1.2 (tight, impactful)
- Body text: 1.5 - 1.7 (comfortable reading)
- Small text / captions: 1.4 - 1.5

**Letter spacing:**
- Uppercase text: +0.05em to +0.15em (always add tracking)
- Display headings: -0.02em to -0.04em (tighten for impact)
- Body: 0 (default is usually fine)

### Color Theory

**Building a palette from scratch:**

1. **Start with one anchor color** - the brand's personality
2. **Generate harmonies:**
   - Complementary (opposite on wheel) - high energy, bold
   - Analogous (neighbors on wheel) - harmonious, calm
   - Split-complementary - vibrant but balanced
   - Triadic - dynamic, creative
3. **Add neutrals** - warm or cool tinted grays, not pure #gray
4. **Test contrast ratios** - WCAG AA minimum 4.5:1 for text

**Modern color functions:**
```css
:root {
  /* oklch for perceptually uniform colors */
  --brand: oklch(65% 0.25 250);
  --brand-light: oklch(85% 0.15 250);
  --brand-dark: oklch(35% 0.20 250);

  /* color-mix for dynamic variations */
  --hover: color-mix(in oklch, var(--brand) 85%, white);
  --pressed: color-mix(in oklch, var(--brand) 85%, black);

  /* Semantic surface system */
  --surface-0: oklch(98% 0.005 250);  /* page bg */
  --surface-1: oklch(95% 0.01 250);   /* card bg */
  --surface-2: oklch(90% 0.015 250);  /* elevated */
  --surface-3: oklch(85% 0.02 250);   /* modal */
}
```

### Spacing System

Use a consistent spacing scale based on multiples. The 8px grid is the industry standard.

```css
:root {
  --space-3xs: clamp(0.25rem, 0.23rem + 0.11vw, 0.31rem);   /* 4px */
  --space-2xs: clamp(0.50rem, 0.46rem + 0.22vw, 0.63rem);   /* 8px */
  --space-xs:  clamp(0.75rem, 0.68rem + 0.33vw, 0.94rem);   /* 12px */
  --space-s:   clamp(1.00rem, 0.91rem + 0.43vw, 1.25rem);   /* 16px */
  --space-m:   clamp(1.50rem, 1.37rem + 0.65vw, 1.88rem);   /* 24px */
  --space-l:   clamp(2.00rem, 1.83rem + 0.87vw, 2.50rem);   /* 32px */
  --space-xl:  clamp(3.00rem, 2.74rem + 1.30vw, 3.75rem);   /* 48px */
  --space-2xl: clamp(4.00rem, 3.65rem + 1.74vw, 5.00rem);   /* 64px */
  --space-3xl: clamp(6.00rem, 5.48rem + 2.61vw, 7.50rem);   /* 96px */
}
```

**Spacing rules:**
- Section padding: space-2xl to space-3xl (generous breathing room)
- Card padding: space-m to space-l
- Element gaps: space-s to space-m
- Tight groupings: space-2xs to space-xs
- Related items cluster together; unrelated items need clear separation (proximity principle)

### The Golden Ratio in Layout

The golden ratio (1.618) creates naturally pleasing proportions:

```css
/* Content + sidebar layout */
.layout {
  display: grid;
  grid-template-columns: 1fr 0.618fr;  /* ~62% + ~38% */
}

/* Hero section proportions */
.hero {
  aspect-ratio: 1.618 / 1;
}

/* Font size progression: each step is ~1.618x the previous */
h1 { font-size: calc(var(--step-0) * 1.618 * 1.618 * 1.618); }
h2 { font-size: calc(var(--step-0) * 1.618 * 1.618); }
h3 { font-size: calc(var(--step-0) * 1.618); }
```

---

## Part 2: Scroll-Driven Storytelling

Scroll storytelling transforms a webpage into a narrative experience. The scroll becomes the user's pace control, revealing content in a deliberate, cinematic sequence.

### Apple's Scroll Design Philosophy

Apple's product pages are the gold standard. Their principles:

1. **Content motion vs graphical motion** - Content motion (text fades, slides) is lightweight CSS. Graphical motion (3D product rotations, video scrubbing) is heavy but purposeful. Mix them only when it strengthens the story
2. **Video scrubbing as the default** for product showcases - compressed MP4/WebM assets mapped to scroll position, cutting asset size by up to 80%
3. **One idea per scroll section** - each section communicates a single feature or benefit
4. **Progressive reveal** - start abstract/atmospheric, get specific as user scrolls deeper
5. **Pin and transform** - sections pin in place while content transforms within them
6. **Extreme whitespace** - let each statement breathe

### GSAP ScrollTrigger Advanced Patterns

**Pinned section with content swap:**
```javascript
gsap.registerPlugin(ScrollTrigger);

// Pin a section while cycling through content
const sections = gsap.utils.toArray('.feature-panel');
const tl = gsap.timeline({
  scrollTrigger: {
    trigger: '.features-container',
    pin: true,
    scrub: 1,
    end: `+=${sections.length * 100}%`,
    snap: 1 / (sections.length - 1),
  }
});

sections.forEach((section, i) => {
  if (i > 0) {
    tl.from(section, { yPercent: 100, opacity: 0 })
      .to(sections[i - 1], { yPercent: -100, opacity: 0 }, '<');
  }
});
```

**Horizontal scroll gallery (pinned):**
```javascript
const container = document.querySelector('.horizontal-panels');
const panels = gsap.utils.toArray('.horizontal-panels .panel');

gsap.to(panels, {
  xPercent: -100 * (panels.length - 1),
  ease: 'none',
  scrollTrigger: {
    trigger: container,
    pin: true,
    scrub: 1,
    snap: 1 / (panels.length - 1),
    end: () => '+=' + container.offsetWidth,
  }
});
```

**Parallax depth layers:**
```javascript
gsap.utils.toArray('.parallax-layer').forEach(layer => {
  const depth = layer.dataset.depth || 1;
  gsap.to(layer, {
    y: () => -ScrollTrigger.maxScroll(window) * depth * 0.1,
    ease: 'none',
    scrollTrigger: {
      trigger: layer.closest('section'),
      start: 'top bottom',
      end: 'bottom top',
      scrub: true,
    }
  });
});
```

**Text reveal on scroll (character by character):**
```javascript
gsap.registerPlugin(ScrollTrigger, SplitText);

gsap.utils.toArray('.reveal-text').forEach(text => {
  const split = new SplitText(text, { type: 'chars,words,lines', linesClass: 'line' });

  gsap.from(split.chars, {
    opacity: 0,
    y: 80,
    rotateX: -90,
    stagger: 0.02,
    duration: 0.8,
    ease: 'back.out(1.7)',
    scrollTrigger: {
      trigger: text,
      start: 'top 85%',
      end: 'top 35%',
      toggleActions: 'play none none reverse',
    }
  });
});
```

**Video scrubbing on scroll (Apple-style):**
```javascript
const video = document.querySelector('.hero-video');

// Ensure video is loaded
video.addEventListener('loadedmetadata', () => {
  ScrollTrigger.create({
    trigger: '.hero-section',
    start: 'top top',
    end: 'bottom bottom',
    pin: '.hero-video-wrapper',
    scrub: true,
    onUpdate: (self) => {
      video.currentTime = video.duration * self.progress;
    }
  });
});
```

### Lenis + GSAP Integration

The modern standard for smooth scrolling with scroll-linked animations:

```javascript
import Lenis from 'lenis';
import gsap from 'gsap';
import { ScrollTrigger } from 'gsap/ScrollTrigger';

gsap.registerPlugin(ScrollTrigger);

// Initialize Lenis
const lenis = new Lenis({
  duration: 1.2,
  easing: (t) => Math.min(1, 1.001 - Math.pow(2, -10 * t)),
  smoothWheel: true,
  touchMultiplier: 2,
});

// Sync Lenis with GSAP
lenis.on('scroll', ScrollTrigger.update);
gsap.ticker.add((time) => lenis.raf(time * 1000));
gsap.ticker.lagSmoothing(0);
```

**Vanilla CDN setup:**
```html
<script src="https://cdn.jsdelivr.net/npm/lenis@latest/dist/lenis.min.js"></script>
<script src="https://cdn.jsdelivr.net/npm/gsap@3/dist/gsap.min.js"></script>
<script src="https://cdn.jsdelivr.net/npm/gsap@3/dist/ScrollTrigger.min.js"></script>
<script>
gsap.registerPlugin(ScrollTrigger);
const lenis = new Lenis({ duration: 1.2, smoothWheel: true });
lenis.on('scroll', ScrollTrigger.update);
gsap.ticker.add((time) => lenis.raf(time * 1000));
gsap.ticker.lagSmoothing(0);
</script>
```

### CSS-Only Scroll Animations (No JavaScript)

Native CSS scroll-driven animations work in Chrome and Firefox (Safari via polyfill).

**Scroll progress bar:**
```css
.progress-bar {
  position: fixed;
  top: 0;
  left: 0;
  width: 100%;
  height: 4px;
  background: var(--accent);
  transform-origin: left;
  animation: scaleX linear both;
  animation-timeline: scroll();
}
@keyframes scaleX {
  from { transform: scaleX(0); }
  to { transform: scaleX(1); }
}
```

**Element reveal on scroll into view:**
```css
.reveal {
  animation: fadeSlideUp linear both;
  animation-timeline: view();
  animation-range: entry 0% entry 100%;
}
@keyframes fadeSlideUp {
  from {
    opacity: 0;
    transform: translateY(60px);
  }
  to {
    opacity: 1;
    transform: translateY(0);
  }
}
```

**Parallax with view-timeline:**
```css
.parallax-bg {
  animation: parallaxShift linear both;
  animation-timeline: view();
  animation-range: cover 0% cover 100%;
}
@keyframes parallaxShift {
  from { transform: translateY(-20%); }
  to { transform: translateY(20%); }
}
```

**Image scale on scroll:**
```css
.hero-image {
  animation: heroZoom linear both;
  animation-timeline: scroll(nearest);
  animation-range: 0% 50%;
}
@keyframes heroZoom {
  from { transform: scale(1.3); }
  to { transform: scale(1); }
}
```

**Browser support fallback:**
```css
@supports not (animation-timeline: scroll()) {
  .reveal {
    opacity: 1;
    transform: none;
  }
}
```

---

## Part 3: Animation Orchestration

### Animation Philosophy

Great animation follows these principles:
1. **Purposeful** - every animation communicates something (entrance, state change, feedback, storytelling)
2. **Choreographed** - elements animate in a deliberate sequence, not all at once
3. **Physics-based** - springs and easing feel natural; linear feels robotic
4. **Restrained** - one wow moment per viewport; too much motion causes fatigue
5. **Accessible** - always respect `prefers-reduced-motion`

### Orchestrated Page Load Sequence

The single most impactful animation is the initial page load. Create a master timeline:

```javascript
// GSAP master page load
const master = gsap.timeline({ defaults: { ease: 'power3.out' } });

master
  // Phase 1: Background atmosphere (0s)
  .from('.bg-gradient', { opacity: 0, duration: 1.2 })
  // Phase 2: Navigation (0.3s)
  .from('.nav', { y: -40, opacity: 0, duration: 0.6 }, 0.3)
  // Phase 3: Hero headline (0.5s) - the star
  .from('.hero-title', { y: 80, opacity: 0, duration: 0.8 }, 0.5)
  // Phase 4: Supporting text (0.8s)
  .from('.hero-subtitle', { y: 40, opacity: 0, duration: 0.6 }, 0.8)
  // Phase 5: CTA (1.0s)
  .from('.hero-cta', { y: 30, opacity: 0, scale: 0.95, duration: 0.5 }, 1.0)
  // Phase 6: Hero image/3D element (0.6s)
  .from('.hero-visual', { scale: 0.9, opacity: 0, duration: 1.0 }, 0.6)
  // Phase 7: Decorative elements (1.2s)
  .from('.floating-element', { y: 20, opacity: 0, stagger: 0.1 }, 1.2);
```

### Anime.js v4 Patterns

**Staggered grid reveal:**
```javascript
import { animate, stagger } from 'animejs';

animate('.grid-item', {
  scale: [0.8, 1],
  opacity: [0, 1],
  delay: stagger(80, { grid: [4, 4], from: 'center' }),
  duration: 600,
  ease: 'outElastic(1, 0.5)',
});
```

**Spring-based draggable:**
```javascript
import { createDraggable, createSpring } from 'animejs';

createDraggable('.card', {
  container: '.board',
  releaseEase: createSpring({ stiffness: 200, damping: 15 }),
});
```

**SVG morphing:**
```javascript
import { animate } from 'animejs';

animate('.shape-path', {
  d: [
    { to: 'M10 80 C 40 10, 65 10, 95 80 S 150 150, 180 80' },
    { to: 'M10 10 L 90 10 L 90 90 L 10 90 Z' },
  ],
  duration: 2000,
  ease: 'inOutQuad',
  loop: true,
  alternate: true,
});
```

**Scroll-linked with Anime.js observer:**
```javascript
import { animate, createScope } from 'animejs';

// Anime.js v4 scroll observer
const scope = createScope({ root: document.body });

scope.add(() => {
  animate('.section-title', {
    opacity: [0, 1],
    translateY: [40, 0],
    duration: 800,
    ease: 'outExpo',
    autoplay: false,  // controlled by observer
  });
});
```

### Micro-Interactions

Small animations that make interfaces feel alive and responsive:

**Button press feedback:**
```css
.btn {
  transition: transform 0.15s cubic-bezier(0.2, 0, 0, 1),
              box-shadow 0.15s cubic-bezier(0.2, 0, 0, 1);
}
.btn:hover {
  transform: translateY(-2px);
  box-shadow: 0 8px 25px -5px rgba(0, 0, 0, 0.2);
}
.btn:active {
  transform: translateY(0) scale(0.98);
  box-shadow: 0 2px 10px -3px rgba(0, 0, 0, 0.2);
  transition-duration: 0.08s;
}
```

**Card hover lift with glow:**
```css
.card {
  transition: transform 0.3s cubic-bezier(0.34, 1.56, 0.64, 1),
              box-shadow 0.3s ease;
}
.card:hover {
  transform: translateY(-8px) rotateX(2deg);
  box-shadow:
    0 20px 40px -15px rgba(0, 0, 0, 0.15),
    0 0 0 1px rgba(255, 255, 255, 0.05);
}
```

**Magnetic cursor effect:**
```javascript
document.querySelectorAll('.magnetic').forEach(el => {
  el.addEventListener('mousemove', (e) => {
    const rect = el.getBoundingClientRect();
    const x = e.clientX - rect.left - rect.width / 2;
    const y = e.clientY - rect.top - rect.height / 2;
    gsap.to(el, { x: x * 0.3, y: y * 0.3, duration: 0.3, ease: 'power2.out' });
  });
  el.addEventListener('mouseleave', () => {
    gsap.to(el, { x: 0, y: 0, duration: 0.5, ease: 'elastic.out(1, 0.3)' });
  });
});
```

**Input focus glow:**
```css
.input-field {
  border: 2px solid transparent;
  background:
    linear-gradient(var(--surface-1), var(--surface-1)) padding-box,
    linear-gradient(135deg, var(--accent), transparent) border-box;
  transition: background 0.3s ease, box-shadow 0.3s ease;
}
.input-field:focus {
  background:
    linear-gradient(var(--surface-1), var(--surface-1)) padding-box,
    linear-gradient(135deg, var(--accent), var(--accent-secondary)) border-box;
  box-shadow: 0 0 0 4px color-mix(in oklch, var(--accent) 20%, transparent);
}
```

**Toggle switch with spring:**
```css
.toggle-thumb {
  transition: transform 0.4s cubic-bezier(0.34, 1.56, 0.64, 1);
}
.toggle[aria-checked="true"] .toggle-thumb {
  transform: translateX(24px);
}
```

---

## Part 4: 3D Web Experiences

### Three.js Basics

**Minimal scene setup:**
```javascript
import * as THREE from 'three';

const scene = new THREE.Scene();
const camera = new THREE.PerspectiveCamera(75, window.innerWidth / window.innerHeight, 0.1, 1000);
const renderer = new THREE.WebGLRenderer({ antialias: true, alpha: true });

renderer.setSize(window.innerWidth, window.innerHeight);
renderer.setPixelRatio(Math.min(window.devicePixelRatio, 2));
document.getElementById('canvas-container').appendChild(renderer.domElement);

camera.position.z = 5;

function animate() {
  requestAnimationFrame(animate);
  renderer.render(scene, camera);
}
animate();

// Responsive
window.addEventListener('resize', () => {
  camera.aspect = window.innerWidth / window.innerHeight;
  camera.updateProjectionMatrix();
  renderer.setSize(window.innerWidth, window.innerHeight);
});
```

**Floating geometry background:**
```javascript
// Create floating particles
const geometry = new THREE.BufferGeometry();
const count = 2000;
const positions = new Float32Array(count * 3);

for (let i = 0; i < count * 3; i++) {
  positions[i] = (Math.random() - 0.5) * 20;
}
geometry.setAttribute('position', new THREE.BufferAttribute(positions, 3));

const material = new THREE.PointsMaterial({
  color: 0x88c0d0,
  size: 0.02,
  transparent: true,
  opacity: 0.8,
  sizeAttenuation: true,
});
const particles = new THREE.Points(geometry, material);
scene.add(particles);

// Animate
function animate() {
  requestAnimationFrame(animate);
  particles.rotation.y += 0.0005;
  particles.rotation.x += 0.0002;
  renderer.render(scene, camera);
}
```

**Scroll-linked 3D rotation:**
```javascript
const model = new THREE.Mesh(
  new THREE.TorusKnotGeometry(1, 0.3, 128, 32),
  new THREE.MeshStandardMaterial({ color: 0x88c0d0, metalness: 0.7, roughness: 0.2 })
);
scene.add(model);

// Link rotation to scroll
ScrollTrigger.create({
  trigger: '.three-section',
  start: 'top bottom',
  end: 'bottom top',
  scrub: 1,
  onUpdate: (self) => {
    model.rotation.y = self.progress * Math.PI * 2;
    model.rotation.x = self.progress * Math.PI * 0.5;
    model.position.y = Math.sin(self.progress * Math.PI) * 0.5;
  }
});
```

### React Three Fiber

**Basic scene in React:**
```jsx
import { Canvas, useFrame } from '@react-three/fiber';
import { OrbitControls, Environment, Float } from '@react-three/drei';
import { useRef } from 'react';

function FloatingMesh() {
  const meshRef = useRef();
  useFrame((state) => {
    meshRef.current.rotation.y = state.clock.elapsedTime * 0.3;
  });

  return (
    <Float speed={2} rotationIntensity={0.5} floatIntensity={1}>
      <mesh ref={meshRef}>
        <torusKnotGeometry args={[1, 0.3, 128, 32]} />
        <meshStandardMaterial color="#88c0d0" metalness={0.7} roughness={0.2} />
      </mesh>
    </Float>
  );
}

function Scene() {
  return (
    <Canvas camera={{ position: [0, 0, 5], fov: 50 }}>
      <ambientLight intensity={0.5} />
      <directionalLight position={[5, 5, 5]} intensity={1} />
      <FloatingMesh />
      <OrbitControls enableZoom={false} autoRotate autoRotateSpeed={0.5} />
      <Environment preset="city" />
    </Canvas>
  );
}
```

**Scroll-linked 3D with R3F + GSAP:**
```jsx
import { useScroll } from '@react-three/drei';
import { useFrame } from '@react-three/fiber';

function ScrollScene() {
  const scroll = useScroll();
  const meshRef = useRef();

  useFrame(() => {
    const progress = scroll.offset; // 0 to 1
    meshRef.current.rotation.y = progress * Math.PI * 4;
    meshRef.current.position.y = Math.sin(progress * Math.PI * 2) * 2;
  });

  return (
    <mesh ref={meshRef}>
      <icosahedronGeometry args={[1.5, 4]} />
      <meshPhysicalMaterial
        color="#88c0d0"
        transmission={0.6}
        thickness={0.5}
        roughness={0.1}
      />
    </mesh>
  );
}
```

### CDN-Based 3D (No Bundler)

```html
<script type="importmap">
{
  "imports": {
    "three": "https://cdn.jsdelivr.net/npm/three@0.172/build/three.module.js",
    "three/addons/": "https://cdn.jsdelivr.net/npm/three@0.172/examples/jsm/"
  }
}
</script>
<script type="module">
import * as THREE from 'three';
import { OrbitControls } from 'three/addons/controls/OrbitControls.js';
import { GLTFLoader } from 'three/addons/loaders/GLTFLoader.js';

// Scene, camera, renderer setup...
const controls = new OrbitControls(camera, renderer.domElement);
controls.enableDamping = true;

// Load a 3D model
const loader = new GLTFLoader();
loader.load('model.glb', (gltf) => {
  scene.add(gltf.scene);
});
</script>
```

---

## Part 5: Creative Layout Patterns

### The Bento Grid

A grid of asymmetric cards at different sizes, popularized by Apple and used across modern dashboards and portfolios:

```css
.bento-grid {
  display: grid;
  grid-template-columns: repeat(4, 1fr);
  grid-auto-rows: minmax(200px, auto);
  gap: var(--space-m);
}
.bento-grid .featured {
  grid-column: span 2;
  grid-row: span 2;
}
.bento-grid .wide { grid-column: span 2; }
.bento-grid .tall { grid-row: span 2; }
```

### Overlapping Sections

Create depth by overlapping sections with negative margins and z-index:

```css
.section-overlap {
  position: relative;
  z-index: 2;
  margin-top: -8rem;
  border-radius: var(--radius-lg) var(--radius-lg) 0 0;
}
```

### Split Screen

Two halves of the viewport showing contrasting content:

```css
.split-screen {
  display: grid;
  grid-template-columns: 1fr 1fr;
  min-height: 100vh;
}
.split-left {
  background: var(--dark);
  color: var(--light);
  padding: var(--space-2xl);
  display: flex;
  align-items: center;
}
.split-right {
  position: sticky;
  top: 0;
  height: 100vh;
  overflow: hidden;
}
```

### Horizontal Scroll Section

A section that scrolls horizontally while the page scrolls vertically:

```html
<section class="horizontal-scroll-section">
  <div class="horizontal-track">
    <div class="panel">Panel 1</div>
    <div class="panel">Panel 2</div>
    <div class="panel">Panel 3</div>
    <div class="panel">Panel 4</div>
  </div>
</section>
```

```css
.horizontal-scroll-section {
  overflow: hidden;
  /* Height set by GSAP based on track width */
}
.horizontal-track {
  display: flex;
  width: fit-content;
}
.panel {
  width: 100vw;
  height: 100vh;
  flex-shrink: 0;
}
```

### Masonry Layout

```css
/* CSS-only masonry (modern browsers) */
.masonry {
  columns: 3;
  column-gap: var(--space-m);
}
.masonry-item {
  break-inside: avoid;
  margin-bottom: var(--space-m);
}

/* Or with Grid (when CSS masonry ships) */
.masonry-grid {
  display: grid;
  grid-template-columns: repeat(3, 1fr);
  grid-template-rows: masonry;
  gap: var(--space-m);
}
```

### Full-Bleed Alternating Sections

Create rhythm by alternating between contained and full-width sections:

```css
.section-contained {
  max-width: 1200px;
  margin-inline: auto;
  padding: var(--space-3xl) var(--space-l);
}
.section-full-bleed {
  width: 100vw;
  margin-left: calc(-50vw + 50%);
  padding: var(--space-3xl) var(--space-l);
  background: var(--surface-1);
}
```

---

## Part 6: Immersive Patterns (Awwwards-Level)

### Pattern 1: Cinematic Hero with Video Background

```html
<section class="cinematic-hero">
  <video class="hero-bg-video" autoplay muted loop playsinline>
    <source src="hero.mp4" type="video/mp4">
  </video>
  <div class="hero-overlay"></div>
  <div class="hero-content">
    <h1 class="hero-title" data-splitting>Experience the Future</h1>
    <p class="hero-subtitle">Crafted with intention</p>
    <a href="#" class="hero-cta magnetic">Explore</a>
  </div>
  <div class="scroll-indicator">
    <span>Scroll</span>
    <div class="scroll-line"></div>
  </div>
</section>
```

```css
.cinematic-hero {
  position: relative;
  height: 100vh;
  display: flex;
  align-items: center;
  justify-content: center;
  overflow: hidden;
}
.hero-bg-video {
  position: absolute;
  inset: 0;
  width: 100%;
  height: 100%;
  object-fit: cover;
}
.hero-overlay {
  position: absolute;
  inset: 0;
  background: linear-gradient(
    to bottom,
    rgba(0, 0, 0, 0.3) 0%,
    rgba(0, 0, 0, 0.6) 100%
  );
}
.hero-content {
  position: relative;
  z-index: 2;
  text-align: center;
}
.scroll-indicator {
  position: absolute;
  bottom: 2rem;
  left: 50%;
  transform: translateX(-50%);
  display: flex;
  flex-direction: column;
  align-items: center;
  gap: 0.5rem;
}
.scroll-line {
  width: 1px;
  height: 60px;
  background: white;
  animation: scrollPulse 2s ease-in-out infinite;
}
@keyframes scrollPulse {
  0%, 100% { transform: scaleY(0); transform-origin: top; }
  50% { transform: scaleY(1); transform-origin: top; }
  51% { transform-origin: bottom; }
  100% { transform: scaleY(0); transform-origin: bottom; }
}
```

### Pattern 2: Scroll-Triggered Number Counter

```javascript
gsap.utils.toArray('.stat-number').forEach(el => {
  const target = parseInt(el.dataset.value);

  ScrollTrigger.create({
    trigger: el,
    start: 'top 80%',
    once: true,
    onEnter: () => {
      gsap.to(el, {
        innerText: target,
        duration: 2,
        ease: 'power2.out',
        snap: { innerText: 1 },
        onUpdate: function() {
          el.textContent = Math.round(this.targets()[0].innerText).toLocaleString();
        }
      });
    }
  });
});
```

### Pattern 3: Reveal Mask Animation

```css
.reveal-mask {
  clip-path: inset(100% 0 0 0);
  transition: clip-path 0.8s cubic-bezier(0.77, 0, 0.175, 1);
}
.reveal-mask.visible {
  clip-path: inset(0 0 0 0);
}
```

```javascript
// With GSAP for more control
gsap.from('.image-reveal', {
  clipPath: 'inset(100% 0% 0% 0%)',
  duration: 1.2,
  ease: 'power4.inOut',
  scrollTrigger: {
    trigger: '.image-reveal',
    start: 'top 75%',
  }
});
```

### Pattern 4: Cursor Follower / Custom Cursor

```javascript
const cursor = document.querySelector('.custom-cursor');
const cursorDot = document.querySelector('.cursor-dot');

document.addEventListener('mousemove', (e) => {
  gsap.to(cursor, { x: e.clientX, y: e.clientY, duration: 0.5, ease: 'power3.out' });
  gsap.to(cursorDot, { x: e.clientX, y: e.clientY, duration: 0.1 });
});

// Grow on interactive elements
document.querySelectorAll('a, button, .interactive').forEach(el => {
  el.addEventListener('mouseenter', () => {
    gsap.to(cursor, { scale: 2.5, opacity: 0.5, duration: 0.3 });
  });
  el.addEventListener('mouseleave', () => {
    gsap.to(cursor, { scale: 1, opacity: 1, duration: 0.3 });
  });
});
```

```css
.custom-cursor {
  position: fixed;
  width: 40px;
  height: 40px;
  border: 1px solid var(--accent);
  border-radius: 50%;
  pointer-events: none;
  z-index: 9999;
  transform: translate(-50%, -50%);
  mix-blend-mode: difference;
}
.cursor-dot {
  position: fixed;
  width: 6px;
  height: 6px;
  background: var(--accent);
  border-radius: 50%;
  pointer-events: none;
  z-index: 10000;
  transform: translate(-50%, -50%);
}
```

### Pattern 5: Infinite Marquee

```html
<div class="marquee">
  <div class="marquee-track">
    <span class="marquee-content">DESIGN &bull; DEVELOP &bull; DELIVER &bull;&nbsp;</span>
    <span class="marquee-content" aria-hidden="true">DESIGN &bull; DEVELOP &bull; DELIVER &bull;&nbsp;</span>
  </div>
</div>
```

```css
.marquee {
  overflow: hidden;
  white-space: nowrap;
}
.marquee-track {
  display: inline-flex;
  animation: marquee 20s linear infinite;
}
.marquee-content {
  font-size: clamp(3rem, 8vw, 8rem);
  font-weight: 900;
  text-transform: uppercase;
  letter-spacing: 0.05em;
  -webkit-text-stroke: 2px currentColor;
  color: transparent;
}
@keyframes marquee {
  0% { transform: translateX(0); }
  100% { transform: translateX(-50%); }
}
/* Reverse direction on hover */
.marquee:hover .marquee-track {
  animation-direction: reverse;
}
```

### Pattern 6: Sticky Progress Navigation

```javascript
const sections = gsap.utils.toArray('.content-section');
const navDots = document.querySelectorAll('.nav-dot');

sections.forEach((section, i) => {
  ScrollTrigger.create({
    trigger: section,
    start: 'top center',
    end: 'bottom center',
    onEnter: () => setActiveDot(i),
    onEnterBack: () => setActiveDot(i),
  });
});

function setActiveDot(index) {
  navDots.forEach((dot, i) => {
    dot.classList.toggle('active', i === index);
  });
}
```

### Pattern 7: Text Gradient Reveal on Scroll

```css
.gradient-reveal {
  background: linear-gradient(to right, var(--text-primary), var(--text-muted));
  background-size: 200% 100%;
  background-position: 100% 0;
  -webkit-background-clip: text;
  background-clip: text;
  -webkit-text-fill-color: transparent;
  animation: gradientReveal linear both;
  animation-timeline: view();
  animation-range: entry 0% cover 50%;
}
@keyframes gradientReveal {
  to { background-position: 0% 0; }
}
```

---

## Part 7: UX Principles for Developers

### Progressive Disclosure

Show only what users need at each step. Reduce cognitive load.

- **Default state**: Show essential controls only
- **On demand**: Reveal advanced options via expand/accordion/drawer
- **Contextual**: Show relevant actions based on current task
- **Never hide critical actions** - primary CTAs must always be visible

### Feedback & State Communication

Every user action needs acknowledgment:

| User Action | Expected Feedback | Timing |
|---|---|---|
| Click/tap | Visual press state | < 50ms |
| Form submit | Loading indicator | Immediate |
| Async operation | Progress bar or skeleton | < 200ms |
| Success | Confirmation + next step | < 1s |
| Error | Clear message + recovery action | Immediate |

### Loading States

Never show blank screens. Use skeleton screens:

```css
.skeleton {
  background: linear-gradient(
    90deg,
    var(--surface-1) 25%,
    var(--surface-2) 50%,
    var(--surface-1) 75%
  );
  background-size: 200% 100%;
  animation: shimmer 1.5s ease-in-out infinite;
  border-radius: 4px;
}
@keyframes shimmer {
  0% { background-position: 200% 0; }
  100% { background-position: -200% 0; }
}
```

### Responsive Design Breakpoints

Design mobile-first, enhance for larger screens:

```css
/* Mobile-first base styles */
.container { padding: var(--space-s); }

/* Tablet (768px+) */
@media (min-width: 48rem) {
  .container { padding: var(--space-m); }
}

/* Desktop (1024px+) */
@media (min-width: 64rem) {
  .container { padding: var(--space-l); max-width: 1200px; margin-inline: auto; }
}

/* Large desktop (1440px+) */
@media (min-width: 90rem) {
  .container { max-width: 1400px; }
}
```

### Accessibility Baseline

Every creative design must still be accessible:

```css
/* Always respect reduced motion */
@media (prefers-reduced-motion: reduce) {
  *, *::before, *::after {
    animation-duration: 0.01ms !important;
    animation-iteration-count: 1 !important;
    transition-duration: 0.01ms !important;
    scroll-behavior: auto !important;
  }
}

/* Focus visible for keyboard users */
:focus-visible {
  outline: 2px solid var(--accent);
  outline-offset: 2px;
}

/* Ensure text contrast */
/* All text must pass WCAG AA: 4.5:1 for normal text, 3:1 for large text */
```

---

## Part 8: Creative Direction Templates

### Template: Luxury / Premium

- **Typography**: Serif heading (Playfair Display, Cormorant Garamond) + thin sans body
- **Color**: Deep blacks, warm golds, cream whites
- **Motion**: Slow, elegant reveals (0.8-1.2s), minimal but precise
- **Layout**: Extreme whitespace, asymmetric compositions, full-bleed imagery
- **Textures**: Subtle grain overlay, soft gradients
- **Reference**: Apple, Rolex, Aesop websites

### Template: Brutalist / Raw

- **Typography**: Monospace or compressed grotesque (Neue Haas Grotesk, Favorit)
- **Color**: Black + white + one raw accent (red, yellow, electric blue)
- **Motion**: Abrupt, instant transitions, glitch effects
- **Layout**: Hard grid, visible structure, overlapping elements
- **Textures**: None or extreme noise, raw borders
- **Reference**: Bloomberg, Balenciaga, Studio Dumbar

### Template: Organic / Natural

- **Typography**: Humanist sans (Lora, Libre Baskerville) + rounded body
- **Color**: Earth tones, forest greens, warm terracottas, soft creams
- **Motion**: Smooth springs, gentle parallax, organic curves
- **Layout**: Rounded shapes, flowing sections, hand-drawn accents
- **Textures**: Paper grain, watercolor splashes, organic SVG blobs

### Template: Cyberpunk / Tech

- **Typography**: Technical mono (JetBrains Mono, Space Mono) + compressed sans
- **Color**: Dark backgrounds, neon accents (cyan, magenta, electric green), terminal green
- **Motion**: Glitch effects, data stream animations, scanning lines
- **Layout**: Grid-heavy, terminal-inspired, HUD elements
- **Textures**: Scanlines, CRT effects, holographic gradients
- **Reference**: Stripe, Linear, Vercel

### Template: Playful / Creative

- **Typography**: Rounded display (Rubik, Nunito, Baloo) + fun body font
- **Color**: Vibrant primaries, unexpected combinations, gradients
- **Motion**: Bouncy springs, elastic easing, wobble effects, confetti
- **Layout**: Irregular grids, tilted elements, sticker-like compositions
- **Textures**: Bold patterns, emoji accents, hand-drawn borders

### Template: Editorial / Magazine

- **Typography**: Strong serif heading (Newsreader, Fraunces) + clean sans body
- **Color**: High contrast B/W with one color accent for emphasis
- **Motion**: Minimal, text-focused reveals, parallax on images
- **Layout**: Column-based, pull quotes, large initial caps, image bleeds
- **Textures**: Clean, minimal, relies on typography and whitespace

---

## Part 9: Performance Checklist

Before shipping any immersive experience:

- [ ] **Images**: WebP/AVIF format, responsive `srcset`, lazy loading below fold
- [ ] **Videos**: Compressed MP4, `poster` attribute, `preload="none"` below fold
- [ ] **3D assets**: Draco-compressed glTF/GLB, LOD (level of detail) for complex models
- [ ] **Fonts**: `font-display: swap`, subset to used characters, preload critical fonts
- [ ] **Animations**: Only animate `transform`, `opacity`, `filter`, `clip-path`
- [ ] **will-change**: Applied sparingly, only on actively animating elements, remove after
- [ ] **ScrollTrigger**: Kill triggers when no longer needed, use `once: true` for one-shot animations
- [ ] **Bundle size**: Tree-shake animation libraries, load 3D libraries dynamically
- [ ] **Mobile**: Test on real devices, reduce particle counts and 3D complexity on mobile
- [ ] **Reduced motion**: `prefers-reduced-motion` fallback for all animations
- [ ] **Core Web Vitals**: LCP < 2.5s, FID < 100ms, CLS < 0.1

---

## Quick Reference: When to Use What

| Goal | Tool | Why |
|------|------|-----|
| Orchestrated page load | GSAP timeline | Precise sequencing and easing control |
| Scroll-triggered reveals | GSAP ScrollTrigger or AOS | Scroll-linked animation with pinning/scrubbing |
| Smooth scrolling | Lenis | Lightweight, works with ScrollTrigger |
| React component animation | Motion (framer-motion) | Declarative, layout animations, exit animations |
| Lightweight standalone | anime.js | Small bundle, powerful stagger and morphing |
| Simple scroll reveals | AOS or CSS scroll-driven | Zero/minimal JS |
| 3D backgrounds/products | Three.js | Full WebGL control |
| 3D in React apps | React Three Fiber + drei | Declarative Three.js in JSX |
| Text splitting | Splitting.js + CSS or GSAP SplitText | Character-level animation control |
| Typewriter effect | Typed.js | Purpose-built, tiny |
| Carousels/sliders | Swiper.js | Touch-friendly, many effects |
| Particle effects | tsParticles | Configurable, interactive |
| Vector animations | Lottie | Designer-created, high quality |
| List transitions | AutoAnimate | Zero-config, just works |
| Page transitions | View Transitions API or Barba.js | Smooth SPA/MPA navigation |
| Visual 3D design | Spline | No-code 3D, exports to React/JS |

---

## Part 10: Advanced Techniques

### Glassmorphism (Frosted Glass)

```css
.glass-card {
  background: rgba(255, 255, 255, 0.12);
  backdrop-filter: blur(12px);
  -webkit-backdrop-filter: blur(12px);
  border: 1px solid rgba(255, 255, 255, 0.18);
  border-radius: 16px;
  box-shadow: 0 8px 32px rgba(0, 0, 0, 0.12);
}

/* Dark mode glass */
.glass-dark {
  background: rgba(0, 0, 0, 0.25);
  backdrop-filter: blur(16px) saturate(180%);
  -webkit-backdrop-filter: blur(16px) saturate(180%);
  border: 1px solid rgba(255, 255, 255, 0.08);
  box-shadow: 0 8px 32px rgba(0, 0, 0, 0.3), inset 0 0 0 1px rgba(255, 255, 255, 0.05);
}
```

### Neomorphism (Soft UI)

```css
:root { --bg: #e0e5ec; --shadow-dark: rgba(163,177,198,0.6); --shadow-light: rgba(255,255,255,0.8); }

.neo-raised {
  background: var(--bg);
  border-radius: 20px;
  box-shadow: 8px 8px 16px var(--shadow-dark), -8px -8px 16px var(--shadow-light);
}
.neo-pressed {
  background: var(--bg);
  border-radius: 20px;
  box-shadow: inset 5px 5px 10px var(--shadow-dark), inset -5px -5px 10px var(--shadow-light);
}
```

### @property for Animating Gradients

CSS normally cannot animate gradients. `@property` unlocks this:

```css
@property --gradient-angle {
  syntax: '<angle>';
  initial-value: 0deg;
  inherits: false;
}
@property --color-1 {
  syntax: '<color>';
  initial-value: #ff6b6b;
  inherits: false;
}
@property --color-2 {
  syntax: '<color>';
  initial-value: #4ecdc4;
  inherits: false;
}

.gradient-box {
  background: linear-gradient(var(--gradient-angle), var(--color-1), var(--color-2));
  animation: rotateGradient 3s linear infinite;
}
@keyframes rotateGradient {
  to { --gradient-angle: 360deg; }
}
```

### View Transitions API (Page Transitions)

**SPA (same-document):**
```javascript
document.startViewTransition(async () => {
  const data = await fetchNewPage();
  updateDOMContent(data);
});
```

**MPA (cross-document, CSS-only):**
```css
@view-transition { navigation: auto; }

::view-transition-old(root) { animation: fade-out 0.3s ease-out; }
::view-transition-new(root) { animation: fade-in 0.3s ease-in; }

@keyframes fade-out { to { opacity: 0; transform: scale(0.95); } }
@keyframes fade-in { from { opacity: 0; transform: scale(1.05); } }

/* Named element transitions */
.hero-image { view-transition-name: hero; }
```

**Barba.js + GSAP (wider browser support):**
```javascript
import barba from '@barba/core';

barba.init({
  transitions: [{
    name: 'slide',
    leave(data) {
      return gsap.to(data.current.container, { opacity: 0, x: -100, duration: 0.5 });
    },
    enter(data) {
      return gsap.from(data.next.container, { opacity: 0, x: 100, duration: 0.5 });
    }
  }]
});
```

### Spline (Visual 3D for Web)

No-code 3D design tool that exports to React, vanilla JS, or static files.

```jsx
// React
import Spline from '@splinetool/react-spline';
<Spline scene="https://prod.spline.design/.../scene.splinecode" />
```

```javascript
// Vanilla JS
import { Application } from '@splinetool/runtime';
const app = new Application(document.getElementById('canvas3d'));
app.load('https://prod.spline.design/.../scene.splinecode');
```

### Stripe-Style WebGL Gradient Background

```javascript
const fragmentShader = `
  uniform float uTime;
  varying vec2 vUv;
  void main() {
    vec3 c1 = vec3(0.4, 0.2, 0.8);
    vec3 c2 = vec3(0.1, 0.6, 0.8);
    vec3 c3 = vec3(0.8, 0.3, 0.5);
    float noise = sin(vUv.x * 3.0 + uTime * 0.5) * cos(vUv.y * 2.0 + uTime * 0.3) * 0.5 + 0.5;
    vec3 color = mix(c1, c2, noise);
    color = mix(color, c3, sin(uTime * 0.2) * 0.5 + 0.5);
    gl_FragColor = vec4(color, 1.0);
  }
`;
```

### Scroll-Velocity Text Skew

Text that reacts to scroll speed, not just position:

```javascript
let currentSkew = 0, lastScrollTop = 0;

function updateSkew() {
  const velocity = window.scrollY - lastScrollTop;
  const targetSkew = Math.max(-15, Math.min(15, velocity * 0.3));
  currentSkew += (targetSkew - currentSkew) * 0.1;

  document.querySelectorAll('.velocity-text').forEach(el => {
    el.style.transform = `skewY(${currentSkew}deg)`;
  });

  lastScrollTop = window.scrollY;
  requestAnimationFrame(updateSkew);
}
requestAnimationFrame(updateSkew);
```

### Broken Grid Layout

Intentionally overlapping, rotated elements for editorial impact:

```css
.broken-grid {
  display: grid;
  grid-template-columns: repeat(12, 1fr);
  gap: 2rem;
}
.broken-grid .item-1 { grid-column: 2 / 7; grid-row: 1 / 3; transform: rotate(-2deg); }
.broken-grid .item-2 { grid-column: 6 / 11; grid-row: 2 / 4; margin-top: -4rem; z-index: 2; }
.broken-grid .item-3 { grid-column: 3 / 9; grid-row: 4 / 6; transform: rotate(1deg); }
```

### Canvas Image Sequence (Apple Product Reveal)

Scrub through pre-rendered 3D frames on scroll:

```javascript
const canvas = document.querySelector('.sequence-canvas');
const ctx = canvas.getContext('2d');
const frameCount = 148;
const images = [];

// Preload frames
for (let i = 0; i < frameCount; i++) {
  const img = new Image();
  img.src = `/frames/frame-${String(i).padStart(4, '0')}.webp`;
  images.push(img);
}

// Scrub with GSAP
const obj = { frame: 0 };
gsap.to(obj, {
  frame: frameCount - 1,
  snap: 'frame',
  ease: 'none',
  scrollTrigger: {
    trigger: '.sequence-section',
    pin: true,
    scrub: 0.5,
    end: '+=300%',
  },
  onUpdate: () => {
    if (images[obj.frame]?.complete) {
      ctx.clearRect(0, 0, canvas.width, canvas.height);
      ctx.drawImage(images[obj.frame], 0, 0, canvas.width, canvas.height);
    }
  }
});
```

### Variable Font Animation on Scroll

Animate font weight, width, or slant with scroll position:

```css
@supports (font-variation-settings: normal) {
  .variable-heading {
    font-family: 'Inter Variable', sans-serif;
    font-variation-settings: 'wght' 100;
    animation: fontWeightShift linear both;
    animation-timeline: view();
    animation-range: entry 0% cover 50%;
  }

  @keyframes fontWeightShift {
    from { font-variation-settings: 'wght' 100; }
    to { font-variation-settings: 'wght' 900; }
  }
}
```

---

**Additional reference:** See `WEB-DESIGN-ANIMATION-REFERENCE.md` in this skill folder for a 2,700-line deep-dive with extended examples, full Apple-style implementation guide, and comprehensive animation library comparisons.
