# Web Design & Animation Comprehensive Reference

A deep-dive technical reference covering modern UI/UX design concepts, animation libraries, scroll-driven storytelling, 3D web content, and performance optimization. This is a practical implementation guide with code patterns, not surface-level descriptions.

---

## Table of Contents

1. [Modern UI/UX Design Concepts 2025-2026](#1-modern-uiux-design-concepts-2025-2026)
2. [Anime.js v4 Deep Dive](#2-animejs-v4-deep-dive)
3. [Apple.com Design Patterns](#3-applecom-design-patterns)
4. [3D Content in Websites](#4-3d-content-in-websites)
5. [Scroll-Driven Storytelling Sites](#5-scroll-driven-storytelling-sites)
6. [Modern Animation Libraries & Techniques](#6-modern-animation-libraries--techniques)
7. [Building Apple-Style Scroll Experiences](#7-building-apple-style-scroll-experiences)
8. [Modern CSS Animation Techniques](#8-modern-css-animation-techniques)
9. [Performance Considerations](#9-performance-considerations)
10. [Award-Winning Web Design Patterns](#10-award-winning-web-design-patterns)

---

## 1. Modern UI/UX Design Concepts 2025-2026

### Bento Grids

Bento grids are modular, asymmetric layouts inspired by Japanese bento boxes. Apple, Samsung, Microsoft, and Google all use them. They arrange content in card-based blocks of varying sizes -- larger feature blocks alongside smaller supporting elements.

**CSS Implementation:**
```css
.bento {
  display: grid;
  gap: 1rem;
  grid-template-columns: repeat(12, minmax(0, 1fr));
  grid-auto-rows: 90px;
}

/* Tile sizing with span */
.tile-wide    { grid-column: span 6; grid-row: span 2; }
.tile-tall    { grid-column: span 3; grid-row: span 4; }
.tile-large   { grid-column: span 6; grid-row: span 4; }
.tile-small   { grid-column: span 3; grid-row: span 2; }
.tile-feature { grid-column: span 8; grid-row: span 3; }

/* Auto-fill gaps */
.bento {
  grid-auto-flow: dense;
}
```

**Two layout approaches:**
1. **Auto-placement with `grid-auto-flow: dense`** -- tiles fill gaps automatically, great for dynamic content
2. **Explicit positioning with line numbers** -- `grid-column: 1 / 7` for precise control of each tile position

**Responsive bento:**
```css
.bento {
  grid-template-columns: repeat(12, 1fr);
}

@media (max-width: 768px) {
  .bento {
    grid-template-columns: repeat(4, 1fr);
    grid-auto-rows: 60px;
  }
  .tile-wide, .tile-large, .tile-feature {
    grid-column: span 4;
    grid-row: span 2;
  }
}
```

### Glassmorphism

Frosted-glass effect using transparency, blur, and subtle borders to create depth and hierarchy. Four core CSS properties make it work: `backdrop-filter`, `background`, `border`, and `box-shadow`.

**Implementation:**
```css
.glass-card {
  background: rgba(255, 255, 255, 0.12);
  backdrop-filter: blur(12px);
  -webkit-backdrop-filter: blur(12px); /* Safari */
  border: 1px solid rgba(255, 255, 255, 0.18);
  border-radius: 16px;
  box-shadow: 0 8px 32px rgba(0, 0, 0, 0.12);
}

/* Dark mode glassmorphism */
.glass-card-dark {
  background: rgba(0, 0, 0, 0.25);
  backdrop-filter: blur(16px) saturate(180%);
  -webkit-backdrop-filter: blur(16px) saturate(180%);
  border: 1px solid rgba(255, 255, 255, 0.08);
  border-radius: 16px;
  box-shadow:
    0 8px 32px rgba(0, 0, 0, 0.3),
    inset 0 0 0 1px rgba(255, 255, 255, 0.05);
}

/* Colorful glass */
.glass-accent {
  background: rgba(99, 102, 241, 0.15);
  backdrop-filter: blur(20px);
  border: 1px solid rgba(99, 102, 241, 0.25);
}
```

**Performance note:** `backdrop-filter` triggers GPU compositing. Limit glass effects to key UI elements (cards, modals, navigation) rather than entire page sections. Browser support is above 97%.

### Neomorphism (Soft UI)

Elements appear to extrude from or press into the background surface using dual offset shadows -- one dark, one light. The effect requires matching the element background to the page background.

**Implementation:**
```css
:root {
  --bg: #e0e5ec;
  --shadow-dark: rgba(163, 177, 198, 0.6);
  --shadow-light: rgba(255, 255, 255, 0.8);
}

body { background: var(--bg); }

/* Raised (extruded) element */
.neo-raised {
  background: var(--bg);
  border-radius: 20px;
  box-shadow:
    8px 8px 16px var(--shadow-dark),
    -8px -8px 16px var(--shadow-light);
}

/* Pressed (inset) element */
.neo-pressed {
  background: var(--bg);
  border-radius: 20px;
  box-shadow:
    inset 5px 5px 10px var(--shadow-dark),
    inset -5px -5px 10px var(--shadow-light);
}

/* Button with hover state */
.neo-button {
  background: var(--bg);
  border: none;
  border-radius: 12px;
  padding: 12px 24px;
  box-shadow:
    5px 5px 10px var(--shadow-dark),
    -5px -5px 10px var(--shadow-light);
  transition: box-shadow 0.2s ease;
  cursor: pointer;
}
.neo-button:active {
  box-shadow:
    inset 3px 3px 6px var(--shadow-dark),
    inset -3px -3px 6px var(--shadow-light);
}
```

**Key rules:** Keep shadows soft and low-contrast. Use rounded corners. Background of element must match page background color. Works best with light, muted color palettes.

### Micro-Interactions

Small, targeted feedback animations that inject personality into every tap, swipe, and hover. These have shifted from "subtle and flashy" to "purposeful Motion UI" -- character-filled moments that serve a function.

**Common micro-interaction patterns:**
```css
/* Button with multiple feedback layers */
.btn-micro {
  position: relative;
  overflow: hidden;
  transition: transform 0.2s cubic-bezier(0.34, 1.56, 0.64, 1);
}
.btn-micro:hover { transform: translateY(-2px); }
.btn-micro:active { transform: translateY(0) scale(0.98); }

/* Input focus glow */
.input-glow {
  transition: box-shadow 0.3s ease, border-color 0.3s ease;
  border: 2px solid transparent;
}
.input-glow:focus {
  border-color: var(--accent);
  box-shadow: 0 0 0 4px rgba(var(--accent-rgb), 0.15);
  outline: none;
}

/* Card hover lift */
.card-hover {
  transition: transform 0.3s cubic-bezier(0.34, 1.56, 0.64, 1),
              box-shadow 0.3s ease;
}
.card-hover:hover {
  transform: translateY(-8px);
  box-shadow: 0 20px 40px rgba(0, 0, 0, 0.15);
}
```

### Dark Mode Design

Dark mode is no longer optional -- it is the expected default for many sites. Key principles:
- Use `#0a0a0a` to `#1a1a2e` for backgrounds (not pure `#000000`)
- Text in `#e0e0e0` range (not pure white `#ffffff` which causes eye strain)
- Reduce shadow intensity, increase border visibility for element separation
- Use CSS `color-scheme: dark` and `prefers-color-scheme` media query

```css
:root {
  color-scheme: light dark;
  --bg: light-dark(#ffffff, #0f0f0f);
  --text: light-dark(#1a1a1a, #e0e0e0);
  --surface: light-dark(#f5f5f5, #1a1a1a);
  --border: light-dark(rgba(0,0,0,0.1), rgba(255,255,255,0.08));
}
```

### 2026 Design Philosophy

The real trends are driven by three forces:
1. **Regulation** -- accessibility laws going into effect (EAA in Europe)
2. **Technology** -- AI that adapts content in real-time to individual users
3. **User behavior** -- people are exhausted by interfaces; purposeful simplicity wins

Key shifts: AI-generated layouts adapting per user, broken/deconstructed grid layouts, kinetic typography as hero content, 3D interactive environments replacing flat pages, and microinteractions becoming brand identity signals.

---

## 2. Anime.js v4 Deep Dive

### Overview

Anime.js v4 is a complete rewrite of the lightweight JavaScript animation library. It animates CSS properties, SVG, DOM attributes, and JavaScript objects. The entire library is ~10KB gzipped with full tree-shaking support via ES modules.

### Key v4 Changes from v3

| v3 Syntax | v4 Syntax |
|-----------|-----------|
| `anime({ targets: '.box', ... })` | `animate('.box', { ... })` |
| `anime.timeline()` | `createTimeline()` |
| `easing: 'easeOutExpo'` | `ease: 'outExpo'` (dropped 'ease' prefix) |
| `changeBegin()`, `change()`, `changeComplete()` | `onRender()` (single callback) |
| String values only | Unit values accepted: `stagger('1rem')` |

### Module Imports (Tree-Shakeable)

```javascript
// Import only what you need
import { animate } from 'animejs';
import { createTimeline } from 'animejs';
import { createTimer } from 'animejs';
import { createDraggable } from 'animejs';
import { createScope } from 'animejs';
import { stagger } from 'animejs';
import { spring } from 'animejs';
import { svg } from 'animejs';
import { utils } from 'animejs';

// Or specific sub-paths for minimal bundles
import { animate } from 'animejs/animation';     // smallest
import { createTimer } from 'animejs/timer';
import { createTimeline } from 'animejs/timeline';
import { createDraggable } from 'animejs/draggable';
import { createScope } from 'animejs/scope';
```

### Core Animation API

```javascript
// Basic animation
animate('.box', {
  translateX: 250,
  rotate: '1turn',
  duration: 800,
  ease: 'outExpo'
});

// With keyframes
animate('.box', {
  translateX: [0, 100, 200],   // keyframe values
  rotate: ['0turn', '1turn'],
  scale: [1, 1.2, 1],
  duration: 1200,
  ease: 'inOutQuad'
});

// Function-based values (per-target)
animate('.item', {
  translateX: (el, i) => i * 50,
  rotate: (el, i) => i * 45,
  delay: (el, i) => i * 100,
  duration: 800
});

// Spring physics
animate('.box', {
  translateX: 250,
  ease: spring(1, 80, 10, 0)  // mass, stiffness, damping, velocity
});
```

### Timeline API

```javascript
const tl = createTimeline({
  defaults: {
    duration: 600,
    ease: 'outExpo'
  }
});

// Chain animations
tl.add('.box1', { translateX: 250 })
  .add('.box2', { translateY: 200 }, '-=400')  // overlap by 400ms
  .add('.box3', { scale: [0, 1] }, '+=200')    // gap of 200ms
  .add('.box4', { rotate: '1turn' }, '<');      // same start as previous
```

### Stagger System

```javascript
// Basic stagger
animate('.grid-item', {
  scale: [0, 1],
  delay: stagger(50)
});

// Grid stagger from center
animate('.grid-item', {
  scale: [0, 1],
  delay: stagger(50, {
    grid: [14, 5],
    from: 'center',
    ease: 'outQuad'
  })
});

// Stagger parameters:
stagger(value, {
  start: 0,           // Starting value
  from: 'center',     // 'first', 'center', 'last', 'random', or index number
  reversed: false,
  ease: 'outQuad',
  grid: [cols, rows],
  axis: 'x',          // 'x' or 'y' for grid stagger direction
  modifier: (v) => v, // Transform the stagger value
});

// Unit stagger values (new in v4)
stagger('1rem');
stagger('50px', { from: 'center' });
```

### Composition (Blending Animations)

```javascript
// Blend multiple animations on the same target
animate('.box', {
  translateX: 100,
  duration: 1000
});

animate('.box', {
  translateY: 50,
  composition: 'add',   // Blend with existing animation
  duration: 800
});
```

### Draggable (New in v4)

```javascript
const draggable = createDraggable('.drag-target', {
  container: '.container',
  snap: { x: 50, y: 50 },       // Snap to grid
  releaseEase: spring(1, 80, 10),
  onDragStart: (d) => { /* */ },
  onDrag: (d) => { /* */ },
  onDragEnd: (d) => { /* */ },
  onThrow: (d) => { /* */ },
});
```

### Scope (Component-Based)

```javascript
const scope = createScope('.component', {
  defaults: {
    duration: 400,
    ease: 'outQuad'
  },
  mediaQueries: {
    mobile: '(max-width: 768px)',
    desktop: '(min-width: 769px)'
  }
});

// All animations in scope inherit defaults and resolve selectors relative to root
scope.add(() => {
  animate('.title', { opacity: [0, 1] });
  animate('.content', { translateY: [20, 0] });
});

// Clean up all animations in scope
scope.revert();
```

### Timer (Base Class)

```javascript
// Timer with infinite default duration
const timer = createTimer({
  onUpdate: (self) => {
    console.log(self.currentTime);  // Use for custom rendering
  },
  duration: Infinity  // Default
});

timer.play();
timer.pause();
timer.restart();
```

### onRender Callback

```javascript
animate('.box', {
  translateX: 250,
  duration: 1000,
  onRender: (anim) => {
    // Called every frame when animation renders to screen
    // Replaces v3's change(), changeBegin(), changeComplete()
  }
});
```

### Web Animation API Version

Anime.js v4 also provides a lightweight 3KB version built on the native Web Animation API:

```javascript
import { animate } from 'animejs/waapi';

animate('.box', {
  translateX: 250,
  ease: 'outExpo',
  duration: 800
});
```

This is more performant for simple animations as it runs on the compositor thread, but has fewer features than the full library.

### Performance

V4 benchmarks show consistent 60fps when animating 3,000 DOM elements' CSS transforms and 50,000 Three.js Instanced Mesh position values. The library uses optimized internal scheduling and minimal memory allocation.

### Anime.js vs GSAP Comparison

| Aspect | Anime.js | GSAP |
|--------|----------|------|
| **Size** | ~10KB gzipped | ~30KB + plugins |
| **Learning curve** | Easier, simpler API | Steeper, more features |
| **Performance** | Great for typical animations | Better for complex/heavy scenes |
| **Plugin ecosystem** | Draggable, scope | ScrollTrigger, MorphSVG, DrawSVG, SplitText, Flip, MotionPath |
| **Timeline** | `createTimeline()` | `gsap.timeline()` with more control |
| **Scroll animations** | No built-in scroll | ScrollTrigger (industry standard) |
| **Community** | Growing | Largest, ranked #1 animation library |
| **License** | MIT (fully free) | Free since 2024 (Webflow acquisition) |
| **Best for** | Lightweight sites, simple sequences | Complex scroll-driven, SVG morphing, professional-grade |

**When to choose Anime.js:** Lightweight projects, simple animations, small bundle requirements, quick prototyping.
**When to choose GSAP:** Scroll-driven experiences, complex timelines, SVG animation, professional production sites.

---

## 3. Apple.com Design Patterns

### What Makes Apple's Website Exceptional

Apple's web design philosophy can be summarized as: **disciplined restraint with technical excellence**. The scroll is not there to impress -- it is there to control the pace. Each motion has a job: it reveals, directs, or reinforces. Nothing moves just to move.

### Core Design Principles

1. **Content motion vs graphical motion separation**
   - Content motion: text fades, product names slide in, sections pin during scroll -- lightweight CSS-driven transitions
   - Graphical motion: 3D product rotations, hardware reveals -- heavy canvas/WebGL driven by scroll position

2. **Scroll as narrative pacing**
   - Users explore one feature at a time as they scroll
   - Information is revealed progressively, never all at once
   - The scroll controls the story's tempo

3. **Massive whitespace**
   - Enormous padding between sections (often 200-400px)
   - Single ideas per viewport
   - Text is often just a headline + one sentence

4. **Typography hierarchy**
   - San Francisco font family (system font), very large headlines (60-96px)
   - Extreme weight contrast (Ultra Light for subheads, Bold for headlines)
   - Very short copy -- Apple writes less, not more

5. **Sticky sections**
   - Entire viewport-height sections pin in place while content within them animates
   - Background colors transition between sections
   - Multiple animation phases within a single pinned section

### Technical Implementation Patterns

**Pattern 1: Scroll-driven image sequence (Canvas)**

Apple's signature technique -- rendering pre-downloaded image frames to a canvas element based on scroll position. Used on AirPods Pro, MacBook, iPhone pages.

```html
<style>
  html { height: 100%; }
  body { height: 500vh; margin: 0; }
  canvas {
    position: fixed;
    top: 50%;
    left: 50%;
    transform: translate(-50%, -50%);
    max-width: 100vw;
    max-height: 100vh;
  }
</style>

<canvas id="hero-canvas" width="1920" height="1080"></canvas>

<script>
const canvas = document.getElementById('hero-canvas');
const ctx = canvas.getContext('2d');
const frameCount = 148;  // Total frames
const currentFrame = (index) =>
  `/images/hero/frame_${index.toString().padStart(4, '0')}.webp`;

// Preload all images
const images = [];
for (let i = 0; i < frameCount; i++) {
  const img = new Image();
  img.src = currentFrame(i);
  images.push(img);
}

// Render frame based on scroll position
function updateFrame() {
  const scrollTop = document.documentElement.scrollTop;
  const maxScroll = document.documentElement.scrollHeight - window.innerHeight;
  const scrollFraction = scrollTop / maxScroll;
  const frameIndex = Math.min(
    frameCount - 1,
    Math.ceil(scrollFraction * frameCount)
  );

  requestAnimationFrame(() => {
    if (images[frameIndex].complete) {
      ctx.clearRect(0, 0, canvas.width, canvas.height);
      ctx.drawImage(images[frameIndex], 0, 0);
    }
  });
}

window.addEventListener('scroll', updateFrame, { passive: true });
images[0].onload = updateFrame;
</script>
```

**Pattern 2: GSAP-powered Apple-style pinned section**

```javascript
gsap.registerPlugin(ScrollTrigger);

// Pin a section and animate multiple phases within it
const tl = gsap.timeline({
  scrollTrigger: {
    trigger: '.product-section',
    start: 'top top',
    end: '+=4000',        // 4000px of scroll distance
    pin: true,
    scrub: 1,             // Smooth 1-second catch-up
    anticipatePin: 1
  }
});

// Phase 1: Text fades in
tl.from('.product-title', {
  opacity: 0,
  y: 60,
  duration: 1
})
// Phase 2: Product rotates
.to('.product-3d', {
  rotationY: 180,
  duration: 3,
  ease: 'none'
}, '+=0.5')
// Phase 3: Feature callouts appear
.from('.feature-callout', {
  opacity: 0,
  scale: 0.8,
  stagger: 0.3,
  duration: 1
})
// Phase 4: Text swaps
.to('.product-title', { opacity: 0, y: -40 })
.from('.feature-title', { opacity: 0, y: 40 }, '<');
```

**Pattern 3: Smooth background color transitions between sections**

```javascript
const sections = gsap.utils.toArray('.section');

sections.forEach((section) => {
  const bgColor = section.dataset.bg;
  const textColor = section.dataset.text;

  gsap.to('body', {
    backgroundColor: bgColor,
    color: textColor,
    scrollTrigger: {
      trigger: section,
      start: 'top center',
      end: 'top 20%',
      scrub: true
    }
  });
});
```

**Pattern 4: Text fade-in with scroll position**

```css
/* CSS-only approach using scroll-driven animations */
.hero-text {
  animation: fadeSlideIn linear both;
  animation-timeline: view();
  animation-range: entry 0% entry 50%;
}

@keyframes fadeSlideIn {
  from {
    opacity: 0;
    transform: translateY(40px);
  }
  to {
    opacity: 1;
    transform: translateY(0);
  }
}
```

### Apple's Key Technical Choices

- **Video over image sequences in newer pages** -- shifted from frame-by-frame canvas to video-based flow, trading microscopic precision for perceived smoothness
- **Lazy section loading** -- only animates and loads assets for sections approaching the viewport
- **Disciplined easing** -- custom cubic-bezier curves, never default `ease-in-out`
- **Progressive enhancement** -- simpler animations on mobile, full experience on desktop
- **System fonts** -- Apple uses its own San Francisco, but the principle is: fewer font loads = faster paint

---

## 4. 3D Content in Websites

### Three.js

The foundational JavaScript 3D library. Core architecture:

```javascript
import * as THREE from 'three';
import { OrbitControls } from 'three/addons/controls/OrbitControls.js';
import { GLTFLoader } from 'three/addons/loaders/GLTFLoader.js';

// Scene setup
const scene = new THREE.Scene();
const camera = new THREE.PerspectiveCamera(
  75, window.innerWidth / window.innerHeight, 0.1, 1000
);
const renderer = new THREE.WebGLRenderer({ antialias: true, alpha: true });
renderer.setSize(window.innerWidth, window.innerHeight);
renderer.setPixelRatio(Math.min(window.devicePixelRatio, 2));
document.body.appendChild(renderer.domElement);

// Lighting
const ambientLight = new THREE.AmbientLight(0xffffff, 0.5);
scene.add(ambientLight);
const directionalLight = new THREE.DirectionalLight(0xffffff, 1);
directionalLight.position.set(5, 5, 5);
scene.add(directionalLight);

// Load 3D model
const loader = new GLTFLoader();
loader.load('/models/product.glb', (gltf) => {
  const model = gltf.scene;
  model.scale.set(2, 2, 2);
  scene.add(model);
});

// Controls
const controls = new OrbitControls(camera, renderer.domElement);
controls.enableDamping = true;
controls.dampingFactor = 0.05;
controls.enablePan = false;
controls.maxPolarAngle = Math.PI / 2;

camera.position.z = 5;

// Animation loop
function animate() {
  requestAnimationFrame(animate);
  controls.update();
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

**3D product viewer with scroll-driven rotation (GSAP):**

```javascript
const loader = new GLTFLoader();
let model;

loader.load('/models/phone.glb', (gltf) => {
  model = gltf.scene;
  scene.add(model);

  // Rotate model based on scroll
  gsap.to(model.rotation, {
    y: Math.PI * 2,
    ease: 'none',
    scrollTrigger: {
      trigger: '.product-section',
      start: 'top top',
      end: 'bottom bottom',
      scrub: 1
    }
  });

  // Exploded view on scroll
  gsap.to(model.children[0].position, {
    y: 0.5,
    scrollTrigger: {
      trigger: '.exploded-section',
      start: 'top center',
      end: 'bottom center',
      scrub: true
    }
  });
});
```

### React Three Fiber (R3F)

Declarative Three.js for React. Uses JSX to define 3D scenes.

```jsx
import { Canvas, useFrame, useThree } from '@react-three/fiber';
import {
  OrbitControls, Environment, useGLTF, Float, Text3D
} from '@react-three/drei';
import { useRef } from 'react';

function Product() {
  const { scene } = useGLTF('/models/product.glb');
  const meshRef = useRef();

  useFrame((state) => {
    // Subtle floating animation
    meshRef.current.rotation.y += 0.003;
    meshRef.current.position.y =
      Math.sin(state.clock.elapsedTime) * 0.1;
  });

  return <primitive ref={meshRef} object={scene} scale={2} />;
}

function Scene() {
  return (
    <Canvas
      camera={{ position: [0, 0, 5], fov: 45 }}
      dpr={[1, 2]}
      gl={{ antialias: true, alpha: true }}
    >
      <ambientLight intensity={0.5} />
      <directionalLight position={[5, 5, 5]} intensity={1} />

      <Float speed={2} rotationIntensity={0.5} floatIntensity={0.5}>
        <Product />
      </Float>

      <OrbitControls
        enablePan={false}
        enableZoom={false}
        maxPolarAngle={Math.PI / 2}
        autoRotate
        autoRotateSpeed={0.5}
      />
      <Environment preset="city" />
    </Canvas>
  );
}
```

**Drei helper library highlights:**
- `<Float>` -- automatic floating animation
- `<Environment>` -- HDR environment maps for realistic lighting
- `<Text3D>` -- 3D text geometry
- `<useGLTF>` -- GLTF model loader hook
- `<OrbitControls>` -- camera controls
- `<ScrollControls>` -- scroll-driven camera movement
- `<Sparkles>`, `<Stars>` -- particle effects
- `<MeshTransmissionMaterial>` -- glass/refraction material

### Spline

Visual 3D design tool that exports directly to web. Lower barrier to entry than Three.js.

**React integration:**
```jsx
import Spline from '@splinetool/react-spline';

export default function App() {
  return (
    <Spline
      scene="https://prod.spline.design/6Wq1Q7YGyM-iab9i/scene.splinecode"
    />
  );
}
```

**With runtime API for interaction:**
```jsx
import { useRef } from 'react';
import Spline from '@splinetool/react-spline';

export default function App() {
  const splineRef = useRef();

  function onLoad(spline) {
    splineRef.current = spline;
    const cube = spline.findObjectByName('Cube');
    // Manipulate at runtime
    cube.position.x = 100;
    cube.rotation.y = Math.PI / 4;
  }

  return <Spline scene="scene-url" onLoad={onLoad} />;
}
```

**Vanilla JS runtime:**
```javascript
import { Application } from '@splinetool/runtime';

const canvas = document.getElementById('canvas3d');
const app = new Application(canvas);
app.load('https://prod.spline.design/.../scene.splinecode');
```

**Export options:** GLB/GLTF, FBX, USDZ (AR), OBJ, React component, Vanilla JS, Next.js.

### WebGL Techniques for Backgrounds

**Animated gradient background (Stripe-style):**
```javascript
// Minimal WebGL gradient shader
const vertexShader = `
  varying vec2 vUv;
  void main() {
    vUv = uv;
    gl_Position = projectionMatrix
      * modelViewMatrix * vec4(position, 1.0);
  }
`;

const fragmentShader = `
  uniform float uTime;
  varying vec2 vUv;

  void main() {
    vec3 color1 = vec3(0.4, 0.2, 0.8);
    vec3 color2 = vec3(0.1, 0.6, 0.8);
    vec3 color3 = vec3(0.8, 0.3, 0.5);

    float noise = sin(vUv.x * 3.0 + uTime * 0.5) *
                  cos(vUv.y * 2.0 + uTime * 0.3) * 0.5 + 0.5;

    vec3 color = mix(color1, color2, noise);
    color = mix(color, color3, sin(uTime * 0.2) * 0.5 + 0.5);

    gl_FragColor = vec4(color, 1.0);
  }
`;
```

### Performance Tips for 3D Web Content

- **Reduce polygon count** -- optimize models before loading (use Draco compression)
- **Compressed textures** at 2048x2048 max resolution
- **glTF format** (`.glb`) is the most efficient for web
- **Instanced meshes** for repeated elements (`THREE.InstancedMesh`)
- **Level of Detail (LOD)** -- lower quality at distance
- **Dispose resources** -- call `.dispose()` on geometries, materials, textures when done
- **Limit pixel ratio** -- `renderer.setPixelRatio(Math.min(window.devicePixelRatio, 2))`
- **Show loading states** -- 3D assets are heavy, always show progress

---

## 5. Scroll-Driven Storytelling Sites

### Notable Examples and Their Techniques

**Apple** -- Scroll-controlled image sequences on canvas, pinned sections with phased animations, massive whitespace between ideas.

**Stripe** -- Animated gradient WebGL backgrounds, progressive feature reveals, elegant micro-interactions. Uses a custom minimal WebGL implementation ("minigl") and a Gradient class for animation properties.

**Linear** -- Subtle animations and live product previews that showcase speed without feeling gimmicky. Motion is purposeful -- every animation enhances understanding rather than distracting.

**Vercel** -- Clean typography, scroll-triggered code examples, performance-focused design. Uses subtle parallax and reveal animations.

### Parallax Scrolling Techniques

**CSS-only parallax (modern):**
```css
/* Using scroll-driven animations */
.parallax-bg {
  animation: parallaxMove linear both;
  animation-timeline: scroll();
}

@keyframes parallaxMove {
  from { transform: translateY(0); }
  to { transform: translateY(-200px); }
}

/* Traditional CSS parallax with perspective */
.parallax-container {
  perspective: 1px;
  height: 100vh;
  overflow-x: hidden;
  overflow-y: auto;
}

.parallax-layer-back {
  transform: translateZ(-1px) scale(2);
}

.parallax-layer-front {
  transform: translateZ(0);
}
```

**GSAP parallax:**
```javascript
// Multi-speed parallax layers
gsap.utils.toArray('.parallax').forEach(layer => {
  const speed = layer.dataset.speed || 0.5;

  gsap.to(layer, {
    yPercent: -100 * speed,
    ease: 'none',
    scrollTrigger: {
      trigger: layer.closest('section'),
      start: 'top bottom',
      end: 'bottom top',
      scrub: true
    }
  });
});
```

### Horizontal Scroll Sections

**GSAP horizontal scroll:**
```javascript
const sections = gsap.utils.toArray('.panel');

gsap.to(sections, {
  xPercent: -100 * (sections.length - 1),
  ease: 'none',
  scrollTrigger: {
    trigger: '.horizontal-container',
    pin: true,
    scrub: 1,
    snap: 1 / (sections.length - 1),   // Snap to each panel
    end: () => '+=' +
      document.querySelector('.horizontal-container').offsetWidth
  }
});
```

**CSS-only horizontal snap:**
```css
.horizontal-scroll {
  display: flex;
  overflow-x: auto;
  scroll-snap-type: x mandatory;
  -webkit-overflow-scrolling: touch;
}

.horizontal-scroll::-webkit-scrollbar {
  display: none;
}

.panel {
  flex: 0 0 100vw;
  height: 100vh;
  scroll-snap-align: start;
}
```

### Scroll-Snap Experiences

```css
/* Full-page scroll snap */
html {
  scroll-snap-type: y mandatory;
}

section {
  height: 100vh;
  scroll-snap-align: start;
}

/* Proximity snap (less aggressive) */
html {
  scroll-snap-type: y proximity;
}

/* With scroll padding for fixed headers */
html {
  scroll-snap-type: y mandatory;
  scroll-padding-top: 80px;  /* Header height */
}
```

### Progressive Content Loading Pattern

```javascript
// Intersection Observer for lazy section loading
const observer = new IntersectionObserver((entries) => {
  entries.forEach(entry => {
    if (entry.isIntersecting) {
      const section = entry.target;

      // Load heavy assets
      section.querySelectorAll('[data-src]').forEach(el => {
        el.src = el.dataset.src;
      });

      // Trigger section animation
      section.classList.add('in-view');

      // Unobserve after loading
      observer.unobserve(section);
    }
  });
}, {
  rootMargin: '200px',  // Start loading 200px before viewport
  threshold: 0.1
});

document.querySelectorAll('.lazy-section').forEach(section => {
  observer.observe(section);
});
```

---

## 6. Modern Animation Libraries & Techniques

### GSAP (GreenSock) -- The Gold Standard

**All plugins are FREE since 2024** (Webflow acquisition). GSAP is the industry standard for complex, sequenced, scroll-driven animation.

**Core API:**
```javascript
// Tween methods
gsap.to('.box', { x: 100, duration: 1 });       // Animate TO values
gsap.from('.box', { x: -100, opacity: 0 });     // Animate FROM values
gsap.fromTo('.box', { x: 0 }, { x: 100 });      // FROM -> TO
gsap.set('.box', { x: 0, opacity: 1 });          // Instant set
```

**Timeline (sequencing):**
```javascript
const tl = gsap.timeline({
  defaults: { duration: 0.8, ease: 'power2.out' }
});

tl.from('.hero-title', { y: 60, opacity: 0 })
  .from('.hero-subtitle', { y: 40, opacity: 0 }, '-=0.4')  // overlap
  .from('.hero-cta', { y: 30, opacity: 0 }, '-=0.3')
  .from('.hero-image', { scale: 0.9, opacity: 0 }, '-=0.5');

// Timeline position syntax:
// '-=0.3'  -- 0.3s before previous ends (overlap)
// '+=0.5'  -- 0.5s after previous ends (gap)
// '<'      -- same start time as previous
// '<+=0.2' -- 0.2s after previous starts
// 2        -- absolute time of 2 seconds
```

**ScrollTrigger:**
```javascript
gsap.registerPlugin(ScrollTrigger);

// Basic scroll trigger
gsap.from('.card', {
  opacity: 0,
  y: 60,
  scrollTrigger: {
    trigger: '.card',
    start: 'top 80%',    // trigger-position viewport-position
    end: 'top 30%',
    scrub: true,          // tie animation to scroll
    markers: true,        // debug markers (remove in production)
  }
});

// Pinned section with scrub
gsap.to('.progress-bar', {
  scaleX: 1,
  ease: 'none',
  scrollTrigger: {
    trigger: '.reading-section',
    start: 'top top',
    end: 'bottom bottom',
    pin: true,
    scrub: 1,    // 1-second smooth catch-up
  }
});

// Batch reveal (multiple elements)
ScrollTrigger.batch('.card', {
  onEnter: (elements) => {
    gsap.from(elements, {
      opacity: 0,
      y: 60,
      stagger: 0.15,
      duration: 0.8,
      ease: 'power3.out'
    });
  },
  once: true
});

// scrub values:
// true     -- precise 1:1 scroll tracking
// 1        -- 1 second to catch up (smooth)
// 0.5      -- snappier catch-up
// 2        -- very smooth, 2 seconds
```

**MorphSVG Plugin:**
```javascript
gsap.registerPlugin(MorphSVGPlugin);

// Morph one SVG path into another
gsap.to('#diamond', {
  duration: 1,
  morphSVG: '#lightning',  // Target shape
  ease: 'power2.inOut'
});

// With options
gsap.to('#circle', {
  morphSVG: {
    shape: '#star',
    type: 'rotational',     // 'linear', 'rotational'
    origin: '50% 50%',
    map: 'complexity'        // 'size', 'position', 'complexity'
  }
});
```

**DrawSVG Plugin:**
```javascript
gsap.registerPlugin(DrawSVGPlugin);

// Draw SVG stroke from nothing to full
gsap.from('.svg-path', {
  drawSVG: 0,              // Start from 0%
  duration: 2,
  ease: 'power2.inOut'
});

// Animate specific range
gsap.fromTo('.svg-path',
  { drawSVG: '0% 0%' },
  { drawSVG: '0% 100%', duration: 2 }
);
```

**SplitText Plugin:**
```javascript
gsap.registerPlugin(SplitText);

const split = new SplitText('.headline', {
  type: 'chars, words, lines',
  mask: 'lines'     // Clip overflow per line
});

gsap.from(split.chars, {
  opacity: 0,
  y: 50,
  rotateX: -90,
  stagger: 0.02,
  duration: 0.8,
  ease: 'back.out(1.7)'
});
```

**MotionPath Plugin:**
```javascript
gsap.registerPlugin(MotionPathPlugin);

gsap.to('.element', {
  motionPath: {
    path: '#curved-path',
    align: '#curved-path',
    alignOrigin: [0.5, 0.5],
    autoRotate: true
  },
  duration: 3,
  ease: 'power1.inOut'
});
```

**Easing reference:** `power1-4.out/in/inOut`, `back.out(1.7)`, `elastic.out(1, 0.3)`, `bounce.out`, `expo.out`, `circ.out`, `sine.inOut`

### Motion (formerly Framer Motion) -- React Animation

**Installation:** `npm install motion`

**Core concepts:**

```jsx
import {
  motion, AnimatePresence, useScroll, useTransform
} from 'motion/react';

// Basic animation
<motion.div
  initial={{ opacity: 0, y: 20 }}
  animate={{ opacity: 1, y: 0 }}
  transition={{ type: 'spring', stiffness: 300, damping: 30 }}
/>

// Hover and tap gestures
<motion.button
  whileHover={{ scale: 1.05 }}
  whileTap={{ scale: 0.95 }}
  transition={{ type: 'spring', stiffness: 400, damping: 17 }}
>
  Click me
</motion.button>

// Variants for orchestrated animations
const container = {
  hidden: {},
  visible: {
    transition: { staggerChildren: 0.1, delayChildren: 0.3 }
  }
};

const item = {
  hidden: { opacity: 0, y: 20 },
  visible: {
    opacity: 1, y: 0,
    transition: { type: 'spring', stiffness: 300 }
  }
};

<motion.ul variants={container} initial="hidden" animate="visible">
  {items.map(i => (
    <motion.li key={i} variants={item}>{i}</motion.li>
  ))}
</motion.ul>

// Layout animations (magic move)
<motion.div layoutId="hero-image">
  <img src={img} />
</motion.div>

// Scroll-linked parallax
function ParallaxSection() {
  const { scrollYProgress } = useScroll();
  const y = useTransform(scrollYProgress, [0, 1], [0, -300]);
  const opacity = useTransform(
    scrollYProgress, [0, 0.5, 1], [1, 0.5, 0]
  );

  return (
    <motion.div style={{ y, opacity }}>Parallax content</motion.div>
  );
}

// Exit animations
<AnimatePresence mode="wait">
  {show && (
    <motion.div
      key="modal"
      initial={{ opacity: 0, scale: 0.9 }}
      animate={{ opacity: 1, scale: 1 }}
      exit={{ opacity: 0, scale: 0.9 }}
      transition={{ type: 'spring', damping: 25 }}
    />
  )}
</AnimatePresence>
```

**Vanilla JS API (non-React):**
```javascript
import { animate, scroll, inView, stagger } from 'motion';

// Animate elements
animate('li',
  { opacity: [0, 1], x: [-20, 0] },
  { delay: stagger(0.1) }
);

// Scroll-linked
scroll(animate('.progress-bar', { scaleX: [0, 1] }));

// In-view trigger
inView('.card', (info) => {
  animate(info.target, { opacity: 1, y: 0 }, { duration: 0.5 });
});
```

**Key features:** Hybrid engine (JavaScript + native browser APIs), 120fps GPU-accelerated, spring physics, layout animations, gesture system, scroll-linked animations, AnimatePresence for exit animations.

### Lottie -- After Effects to Web

Lottie renders After Effects animations exported as JSON (via Bodymovin plugin) natively on web, mobile, and desktop.

**Basic implementation:**
```javascript
// Using lottie-web
import lottie from 'lottie-web';

const animation = lottie.loadAnimation({
  container: document.getElementById('lottie-container'),
  renderer: 'svg',      // 'svg', 'canvas', or 'html'
  loop: true,
  autoplay: true,
  path: '/animations/hero.json'  // Path to animation JSON
});

// Control playback
animation.play();
animation.pause();
animation.stop();
animation.setSpeed(1.5);
animation.goToAndPlay(30, true);  // Go to frame 30
animation.setDirection(-1);       // Reverse
```

**Web component (simplest):**
```html
<script src="https://unpkg.com/@lottiefiles/lottie-player@latest/dist/lottie-player.js"></script>

<lottie-player
  src="/animations/loading.json"
  background="transparent"
  speed="1"
  style="width: 300px; height: 300px;"
  loop
  autoplay
></lottie-player>
```

**DotLottie React (modern):**
```jsx
import { DotLottieReact } from '@lottiefiles/dotlottie-react';

function AnimatedIcon() {
  const [dotLottie, setDotLottie] = useState(null);

  return (
    <DotLottieReact
      src="/animations/icon.lottie"
      loop
      autoplay
      dotLottieRefCallback={setDotLottie}
      style={{ width: 200, height: 200 }}
    />
  );
}
```

**Scroll-synced Lottie (interactivity):**
```javascript
LottieInteractivity.create({
  mode: 'scroll',
  player: '#lottie-player',
  actions: [
    {
      visibility: [0, 1],       // Visible 0% to 100%
      type: 'seek',
      frames: [0, 120]          // Map scroll to frames 0-120
    }
  ]
});
```

**Sources for Lottie animations:** LottieFiles.com (largest marketplace), Lordicon, IconScout, Motion Corpse.

### View Transitions API

Native browser API for smooth page transitions -- both same-document (SPA) and cross-document (MPA).

**Same-document (SPA) transition:**
```javascript
// Trigger a view transition
document.startViewTransition(() => {
  // Update the DOM
  updateContent();
});

// With async updates
document.startViewTransition(async () => {
  const data = await fetchNewPage();
  document.querySelector('.content').textContent = data;
});
```

**Cross-document (MPA) transition -- CSS only, no JavaScript:**
```css
/* Add to BOTH pages */
@view-transition {
  navigation: auto;
}

/* Customize the transition animation */
::view-transition-old(root) {
  animation: fade-out 0.3s ease-out;
}

::view-transition-new(root) {
  animation: fade-in 0.3s ease-in;
}

@keyframes fade-out {
  to { opacity: 0; transform: scale(0.95); }
}

@keyframes fade-in {
  from { opacity: 0; transform: scale(1.05); }
}

/* Named transitions for specific elements */
.hero-image {
  view-transition-name: hero;
}

::view-transition-old(hero) {
  animation: slide-out 0.4s ease;
}

::view-transition-new(hero) {
  animation: slide-in 0.4s ease;
}
```

**Auto-naming with `match-element` (new 2025):**
```css
.card {
  view-transition-name: match-element;
}
```

**Browser support (2025):** Chromium full support, Safari support for same-document transitions, Firefox behind flag. Focus area of Interop 2025.

---

## 7. Building Apple-Style Scroll Experiences

### Complete Implementation Guide

This section provides a step-by-step approach to building scroll-driven storytelling pages similar to Apple's product pages.

### Architecture Pattern

```
[Hero Section - Pinned, canvas animation]
    |
[Feature 1 - Pinned, text + image phased reveal]
    |
[Feature 2 - Horizontal scroll panels]
    |
[Specs Section - Parallax layers]
    |
[CTA - Fade up on scroll]
```

### Step 1: HTML Structure

```html
<main>
  <!-- Hero with image sequence -->
  <section class="hero" style="height: 400vh;">
    <div class="hero-sticky">
      <canvas id="hero-canvas"></canvas>
      <div class="hero-copy">
        <h1 class="hero-title">iPhone</h1>
        <p class="hero-subtitle">A magical new way</p>
      </div>
    </div>
  </section>

  <!-- Feature section with pinned animation -->
  <section class="feature" data-bg="#000" data-text="#fff">
    <div class="feature-content">
      <span class="feature-label">A17 Pro chip</span>
      <h2 class="feature-title">
        Game-changing chip.<br>Ground-breaking performance.
      </h2>
      <div class="feature-media">
        <video data-src="chip-animation.mp4" muted playsinline></video>
      </div>
    </div>
  </section>

  <!-- Horizontal scroll features -->
  <section class="horizontal-section">
    <div class="horizontal-track">
      <div class="panel">Feature 1</div>
      <div class="panel">Feature 2</div>
      <div class="panel">Feature 3</div>
    </div>
  </section>
</main>
```

### Step 2: CSS Foundation

```css
* { margin: 0; padding: 0; box-sizing: border-box; }

body {
  font-family: -apple-system, 'SF Pro Display',
    'Helvetica Neue', sans-serif;
  background: #000;
  color: #f5f5f7;
  -webkit-font-smoothing: antialiased;
}

/* Hero section */
.hero { position: relative; }
.hero-sticky {
  position: sticky;
  top: 0;
  height: 100vh;
  display: flex;
  align-items: center;
  justify-content: center;
  overflow: hidden;
}

#hero-canvas {
  position: absolute;
  width: 100%;
  height: 100%;
  object-fit: cover;
}

.hero-copy {
  position: relative;
  z-index: 2;
  text-align: center;
}

.hero-title {
  font-size: clamp(48px, 10vw, 96px);
  font-weight: 700;
  letter-spacing: -0.02em;
}

.hero-subtitle {
  font-size: clamp(18px, 3vw, 28px);
  font-weight: 400;
  opacity: 0.8;
  margin-top: 0.5em;
}

/* Feature section - Apple-style spacing */
.feature {
  min-height: 100vh;
  display: flex;
  align-items: center;
  justify-content: center;
  padding: 200px 5vw;
}

.feature-label {
  font-size: 14px;
  text-transform: uppercase;
  letter-spacing: 0.1em;
  color: var(--accent, #2997ff);
}

.feature-title {
  font-size: clamp(32px, 5vw, 64px);
  font-weight: 700;
  line-height: 1.1;
  letter-spacing: -0.02em;
  max-width: 800px;
  margin-top: 16px;
}

/* Horizontal scroll */
.horizontal-section {
  overflow: hidden;
}

.horizontal-track {
  display: flex;
  width: fit-content;
}

.panel {
  width: 100vw;
  height: 100vh;
  display: flex;
  align-items: center;
  justify-content: center;
  flex-shrink: 0;
}
```

### Step 3: JavaScript Animation Orchestration

```javascript
import gsap from 'gsap';
import { ScrollTrigger } from 'gsap/ScrollTrigger';
import { SplitText } from 'gsap/SplitText';

gsap.registerPlugin(ScrollTrigger, SplitText);

// =============================================
// 1. HERO: Image sequence on canvas
// =============================================
function initHeroSequence() {
  const canvas = document.getElementById('hero-canvas');
  const ctx = canvas.getContext('2d');
  const frameCount = 148;
  const images = [];
  let loadedCount = 0;

  // Set canvas size
  canvas.width = 1920;
  canvas.height = 1080;

  // Preload frames
  for (let i = 0; i < frameCount; i++) {
    const img = new Image();
    img.src = `/frames/hero_${String(i).padStart(4, '0')}.webp`;
    img.onload = () => {
      loadedCount++;
      if (loadedCount === 1) renderFrame(0);
    };
    images.push(img);
  }

  const frameObj = { frame: 0 };

  gsap.to(frameObj, {
    frame: frameCount - 1,
    snap: 'frame',
    ease: 'none',
    scrollTrigger: {
      trigger: '.hero',
      start: 'top top',
      end: 'bottom bottom',
      scrub: 0.5
    },
    onUpdate: () => renderFrame(Math.round(frameObj.frame))
  });

  function renderFrame(index) {
    if (images[index] && images[index].complete) {
      ctx.clearRect(0, 0, canvas.width, canvas.height);
      ctx.drawImage(images[index], 0, 0, canvas.width, canvas.height);
    }
  }
}

// =============================================
// 2. HERO TEXT: Fade and scale with scroll
// =============================================
function initHeroText() {
  const tl = gsap.timeline({
    scrollTrigger: {
      trigger: '.hero',
      start: 'top top',
      end: '30% top',
      scrub: true
    }
  });

  tl.to('.hero-title', { scale: 0.8, opacity: 0, y: -50 })
    .to('.hero-subtitle', { opacity: 0, y: -30 }, '<');
}

// =============================================
// 3. FEATURE SECTIONS: Staggered reveal
// =============================================
function initFeatureSections() {
  gsap.utils.toArray('.feature').forEach(section => {
    const label = section.querySelector('.feature-label');
    const title = section.querySelector('.feature-title');
    const media = section.querySelector('.feature-media');

    // Split title text for character animation
    const split = new SplitText(title, {
      type: 'lines', mask: 'lines'
    });

    const tl = gsap.timeline({
      scrollTrigger: {
        trigger: section,
        start: 'top 70%',
        end: 'top 20%',
        toggleActions: 'play none none reverse'
      }
    });

    tl.from(label, { opacity: 0, y: 20, duration: 0.6 })
      .from(split.lines, {
        opacity: 0,
        y: 40,
        stagger: 0.1,
        duration: 0.8,
        ease: 'power3.out'
      }, '-=0.3')
      .from(media, {
        opacity: 0,
        scale: 0.95,
        duration: 1,
        ease: 'power2.out'
      }, '-=0.4');

    // Lazy load video when section is near
    ScrollTrigger.create({
      trigger: section,
      start: 'top 120%',
      once: true,
      onEnter: () => {
        const video = section.querySelector('video[data-src]');
        if (video) {
          video.src = video.dataset.src;
          video.load();
        }
      }
    });
  });
}

// =============================================
// 4. HORIZONTAL SCROLL
// =============================================
function initHorizontalScroll() {
  const track = document.querySelector('.horizontal-track');
  const panels = gsap.utils.toArray('.panel');

  gsap.to(panels, {
    xPercent: -100 * (panels.length - 1),
    ease: 'none',
    scrollTrigger: {
      trigger: '.horizontal-section',
      pin: true,
      scrub: 1,
      snap: 1 / (panels.length - 1),
      end: () => `+=${track.offsetWidth}`
    }
  });
}

// =============================================
// 5. BACKGROUND COLOR TRANSITIONS
// =============================================
function initColorTransitions() {
  gsap.utils.toArray('[data-bg]').forEach(section => {
    gsap.to('body', {
      backgroundColor: section.dataset.bg,
      color: section.dataset.text,
      scrollTrigger: {
        trigger: section,
        start: 'top center',
        end: 'top 20%',
        scrub: true
      }
    });
  });
}

// Initialize everything
document.addEventListener('DOMContentLoaded', () => {
  initHeroSequence();
  initHeroText();
  initFeatureSections();
  initHorizontalScroll();
  initColorTransitions();
});
```

### Step 4: Smooth Scrolling Layer (Lenis)

```javascript
import Lenis from 'lenis';

const lenis = new Lenis({
  duration: 1.2,
  easing: (t) => Math.min(1, 1.001 - Math.pow(2, -10 * t)),
  smoothWheel: true
});

// Integrate with GSAP ticker
gsap.ticker.add((time) => {
  lenis.raf(time * 1000);
});
gsap.ticker.lagSmoothing(0);
```

### Design Rules for Scroll Storytelling

1. **One idea per viewport** -- never cram multiple features into one scroll section
2. **Generous scroll distance** -- give each section 2-4x viewport height of scroll room
3. **Custom easing on everything** -- never use default `ease-in-out`
4. **Progressive disclosure** -- reveal details as users commit more scroll
5. **Clear visual hierarchy** -- large headlines, small supporting text, huge media
6. **Restrained animation** -- every motion must have a purpose (reveal, direct, reinforce)
7. **Performance first** -- test on mobile, use `will-change` sparingly, lazy load all media

---

## 8. Modern CSS Animation Techniques

### @keyframes Animations

```css
/* Multi-step animation */
@keyframes complexReveal {
  0% {
    opacity: 0;
    transform: translateY(40px) scale(0.95);
    filter: blur(4px);
  }
  50% {
    opacity: 0.8;
    filter: blur(0px);
  }
  100% {
    opacity: 1;
    transform: translateY(0) scale(1);
    filter: blur(0px);
  }
}

.reveal {
  animation: complexReveal 0.8s cubic-bezier(0.16, 1, 0.3, 1) both;
}

/* Staggered children with CSS custom properties */
.stagger-item {
  animation: fadeUp 0.6s ease both;
  animation-delay: calc(var(--i, 0) * 0.08s);
}

@keyframes fadeUp {
  from { opacity: 0; transform: translateY(20px); }
  to { opacity: 1; transform: translateY(0); }
}
```

```html
<div class="stagger-item" style="--i: 0">First</div>
<div class="stagger-item" style="--i: 1">Second</div>
<div class="stagger-item" style="--i: 2">Third</div>
```

### Scroll-Driven Animations (Native CSS)

Two timeline functions: `scroll()` and `view()`.

**scroll()** -- ties animation to scroll position of a container:
```css
/* Reading progress bar */
.progress-bar {
  position: fixed;
  top: 0;
  left: 0;
  height: 3px;
  width: 100%;
  background: var(--accent);
  transform-origin: left;
  animation: scaleProgress linear both;
  animation-timeline: scroll(root block);
}

@keyframes scaleProgress {
  from { transform: scaleX(0); }
  to { transform: scaleX(1); }
}
```

**view()** -- ties animation to element's visibility in viewport:
```css
/* Fade-in as element enters viewport */
.fade-in-view {
  animation: fadeIn linear both;
  animation-timeline: view();
  animation-range: entry 0% entry 100%;
}

@keyframes fadeIn {
  from {
    opacity: 0;
    transform: translateY(50px);
  }
  to {
    opacity: 1;
    transform: translateY(0);
  }
}

/* Parallax effect */
.parallax-element {
  animation: parallaxShift linear both;
  animation-timeline: view();
  animation-range: entry 0% exit 100%;
}

@keyframes parallaxShift {
  from { transform: translateY(100px); }
  to { transform: translateY(-100px); }
}

/* Scale up as element crosses viewport */
.scale-through {
  animation: scaleThrough linear both;
  animation-timeline: view();
  animation-range: entry 0% contain 50%;
}

@keyframes scaleThrough {
  from { transform: scale(0.8); opacity: 0.5; }
  to { transform: scale(1); opacity: 1; }
}
```

**Important:** When using scroll timelines, set `animation-duration: auto` (or omit from shorthand). These animations run off the main thread for better performance.

**animation-range values:**
- `entry 0%` to `entry 100%` -- while element enters viewport
- `exit 0%` to `exit 100%` -- while element exits viewport
- `contain 0%` to `contain 100%` -- while fully contained in viewport
- `cover 0%` to `cover 100%` -- entire time element overlaps viewport

**Browser support:** Chromium (full), Safari 26+ (2025), Firefox (behind flag).

### Scroll-Triggered Animations (New 2026)

Distinct from scroll-driven: these are time-based animations that **trigger** at a scroll position but run on their own clock.

```css
/* Triggers when element is 50% visible, plays as normal timed animation */
.trigger-animate {
  animation: bounceIn 0.6s cubic-bezier(0.34, 1.56, 0.64, 1) both;
  animation-trigger: view(50%);  /* Chrome 145+ */
}
```

### @starting-style (Entry Animations)

Defines the starting state for elements that are newly inserted or transitioning from `display: none`. Replaces the need for JavaScript toggle-class patterns.

```css
/* Dialog entry animation */
dialog {
  opacity: 1;
  transform: scale(1);
  transition: opacity 0.3s ease, transform 0.3s ease,
              display 0.3s allow-discrete;

  @starting-style {
    opacity: 0;
    transform: scale(0.95);
  }
}

dialog:not([open]) {
  opacity: 0;
  transform: scale(0.95);
}

/* Popover entry */
[popover] {
  opacity: 1;
  transform: translateY(0);
  transition: opacity 0.2s, transform 0.2s,
              display 0.2s allow-discrete;

  @starting-style {
    opacity: 0;
    transform: translateY(-8px);
  }
}

/* List item entry animation */
.list-item {
  opacity: 1;
  transform: translateX(0);
  transition: opacity 0.3s, transform 0.3s;

  @starting-style {
    opacity: 0;
    transform: translateX(-20px);
  }
}
```

**Browser support:** ~86% as of late 2025.

### @property for Animatable Custom Properties

Allows animating values that CSS normally cannot interpolate (gradients, complex values).

```css
/* Animating gradient colors */
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
  background: linear-gradient(
    var(--gradient-angle), var(--color-1), var(--color-2)
  );
  animation: rotateGradient 3s linear infinite;
}

@keyframes rotateGradient {
  to { --gradient-angle: 360deg; }
}

/* Animating border gradient */
@property --border-progress {
  syntax: '<percentage>';
  initial-value: 0%;
  inherits: false;
}

.border-animate {
  background: conic-gradient(
    var(--accent) var(--border-progress),
    transparent var(--border-progress)
  );
  animation: fillBorder 2s ease forwards;
}

@keyframes fillBorder {
  to { --border-progress: 100%; }
}
```

### Container Queries for Responsive Animation

```css
.card-container {
  container-type: inline-size;
  container-name: card;
}

/* Different animations based on container size */
@container card (min-width: 400px) {
  .card-content {
    animation: slideInRight 0.5s ease both;
  }
}

@container card (max-width: 399px) {
  .card-content {
    animation: fadeIn 0.3s ease both;
  }
}
```

### Path-Based CSS Motion

```css
.element {
  offset-path: path('M 0 200 Q 200 0 400 200 T 800 200');
  offset-distance: 0%;
  animation: followPath 4s ease-in-out infinite alternate;
}

@keyframes followPath {
  to { offset-distance: 100%; }
}

/* Combined with rotation */
.element {
  offset-path: path('M 0 0 C 100 200, 300 0, 400 200');
  offset-rotate: auto;
  animation: movePath 3s ease-in-out infinite;
}
```

### View Transition Pseudo-Elements

```css
/* Customizing view transitions */
::view-transition-old(root) {
  animation: 300ms ease-out both fade-out,
             300ms ease-out both slide-to-left;
}

::view-transition-new(root) {
  animation: 300ms ease-in both fade-in,
             300ms ease-in both slide-from-right;
}

/* Per-element transitions */
.hero { view-transition-name: hero; }

::view-transition-old(hero) {
  animation: 400ms ease-out both shrink-out;
}

::view-transition-new(hero) {
  animation: 400ms ease-in both grow-in;
}

/* View transition classes (new 2025) */
.card { view-transition-class: card-transition; }

::view-transition-group(*.card-transition) {
  animation-duration: 0.3s;
}
```

---

## 9. Performance Considerations

### The Rendering Pipeline

The browser renders in three stages, each triggering everything after it:

```
Layout (Reflow)  -->  Paint  -->  Composite
   Most expensive              Cheapest
```

- **Layout:** Calculates geometry (position, size) of every element. Triggered by: `width`, `height`, `top`, `left`, `margin`, `padding`, `font-size`, `display`.
- **Paint:** Converts elements into bitmap layers. Triggered by: `color`, `background`, `border`, `box-shadow`, `visibility`.
- **Composite:** Combines layers into final frame. Triggered by: `transform`, `opacity`, `filter`, `clip-path`.

### Performance Tier List

**S-Tier (Compositor only -- 60-120fps guaranteed):**
Animate these exclusively when possible:
- `transform` (translate, rotate, scale, skew)
- `opacity`
- `filter` (blur, brightness, contrast, etc.)
- `clip-path`

These run on the compositor thread, independent of main thread. Even if JavaScript is busy, these stay smooth.

**A-Tier (Main thread but fast):**
- `color`, `background-color` (triggers paint, not layout)
- `box-shadow` (expensive paint, use sparingly)
- `border-color`

**F-Tier (Triggers layout -- avoid animating):**
- `width`, `height`
- `top`, `right`, `bottom`, `left`
- `margin`, `padding`
- `font-size`
- `border-width`

### GPU Acceleration

```css
/* Promote element to its own compositor layer */
.animated-element {
  will-change: transform;
  /* Inform browser of upcoming animation */
}

/* IMPORTANT: will-change best practices */
/* DO: Add before animation starts */
.element:hover { will-change: transform; }
.element:hover .child { transform: scale(1.1); }

/* DON'T: Apply to everything globally */
/* * { will-change: transform; }  <-- BAD: wastes GPU memory */
```

```javascript
// Remove will-change after animation completes
element.addEventListener('transitionend', () => {
  element.style.willChange = 'auto';
});
```

### Intersection Observer for Lazy Animation

```javascript
// Only animate elements when they enter viewport
const animationObserver = new IntersectionObserver(
  (entries) => {
    entries.forEach(entry => {
      if (entry.isIntersecting) {
        entry.target.classList.add('animate');
        animationObserver.unobserve(entry.target);
      }
    });
  },
  {
    threshold: 0.2,
    rootMargin: '0px 0px -50px 0px'
  }
);

document.querySelectorAll('.reveal-on-scroll').forEach(el => {
  animationObserver.observe(el);
});
```

```css
/* Animation starts paused, plays when class added */
.reveal-on-scroll {
  opacity: 0;
  transform: translateY(30px);
  transition: opacity 0.6s ease,
    transform 0.6s cubic-bezier(0.16, 1, 0.3, 1);
}

.reveal-on-scroll.animate {
  opacity: 1;
  transform: translateY(0);
}
```

### Avoiding Layout Thrashing

```javascript
// BAD: Causes forced synchronous layout
elements.forEach(el => {
  const height = el.offsetHeight;     // Read
  el.style.height = height + 10;     // Write -- forces layout
});

// GOOD: Batch reads, then batch writes
const heights = elements.map(el => el.offsetHeight);
elements.forEach((el, i) => {
  el.style.height = heights[i] + 10;
});

// BEST: Use requestAnimationFrame
function batchUpdate() {
  const measurements = elements.map(el =>
    el.getBoundingClientRect()
  );

  requestAnimationFrame(() => {
    elements.forEach((el, i) => {
      el.style.transform =
        `translateY(${measurements[i].top}px)`;
    });
  });
}
```

### Animation Frame Budget

At 60fps, each frame has **16.7ms** to complete. At 120fps, it is **8.3ms**.

### Reduced Motion Respect

```css
@media (prefers-reduced-motion: reduce) {
  *,
  *::before,
  *::after {
    animation-duration: 0.01ms !important;
    animation-iteration-count: 1 !important;
    transition-duration: 0.01ms !important;
    scroll-behavior: auto !important;
  }
}
```

```javascript
// JavaScript check
const prefersReducedMotion =
  window.matchMedia('(prefers-reduced-motion: reduce)').matches;

if (prefersReducedMotion) {
  gsap.globalTimeline.timeScale(100); // Effectively instant
}
```

### Performance Checklist

- [ ] Only animate `transform`, `opacity`, `filter`, `clip-path`
- [ ] Use `will-change` only on actively animating elements, remove after
- [ ] Batch DOM reads/writes to prevent layout thrashing
- [ ] Use Intersection Observer for off-screen elements (not scroll events)
- [ ] Test on mid-range mobile devices (not just your fast desktop)
- [ ] Limit simultaneous animations to 10-15 elements
- [ ] Use `passive: true` on scroll event listeners
- [ ] Lazy-load heavy assets (videos, 3D models, large images)
- [ ] Set `transform: translateZ(0)` only when needed
- [ ] Use CSS scroll-driven animations over JS where possible (off main thread)
- [ ] Respect `prefers-reduced-motion`
- [ ] Debounce resize handlers, use ResizeObserver where appropriate
- [ ] Profile with Chrome DevTools Performance tab -- look for long frames

---

## 10. Award-Winning Web Design Patterns

### What Makes Sites Win Awards (Awwwards, FWA, CSS Design Awards)

The common thread across award-winning sites is not complexity -- it is **intentionality**. Every design decision serves the content and brand.

### Common Patterns in Award-Winners

**1. Immersive Scroll Experiences**
- Scroll is the primary interaction mechanism
- Content reveals progressively, never all at once
- Multiple animation phases within pinned sections
- Scroll distance is generous (300-500vh for a single story)

**2. Custom Cursors and Pointer Interactions**
```css
body { cursor: none; }

.custom-cursor {
  width: 20px;
  height: 20px;
  border: 2px solid white;
  border-radius: 50%;
  position: fixed;
  pointer-events: none;
  z-index: 9999;
  transition: transform 0.15s ease,
    width 0.3s ease, height 0.3s ease;
  mix-blend-mode: difference;
}

.custom-cursor.hovering {
  width: 60px;
  height: 60px;
  border-width: 1px;
}
```

```javascript
const cursor = document.querySelector('.custom-cursor');

document.addEventListener('mousemove', (e) => {
  gsap.to(cursor, {
    x: e.clientX - 10,
    y: e.clientY - 10,
    duration: 0.15,
    ease: 'power2.out'
  });
});

// Magnetic buttons
document.querySelectorAll('.magnetic').forEach(btn => {
  btn.addEventListener('mousemove', (e) => {
    const rect = btn.getBoundingClientRect();
    const x = e.clientX - rect.left - rect.width / 2;
    const y = e.clientY - rect.top - rect.height / 2;

    gsap.to(btn, {
      x: x * 0.3,
      y: y * 0.3,
      duration: 0.3,
      ease: 'power2.out'
    });
  });

  btn.addEventListener('mouseleave', () => {
    gsap.to(btn, {
      x: 0, y: 0,
      duration: 0.5,
      ease: 'elastic.out(1, 0.3)'
    });
  });
});
```

**3. Kinetic Typography**
- Huge, animated text as the hero element
- Characters split and animated individually
- Text that responds to scroll, hover, or mouse movement
- Variable fonts with animated weight/width

```javascript
// Variable font animation on scroll
gsap.to('.kinetic-text', {
  '--font-weight': 900,
  '--font-width': 125,
  scrollTrigger: {
    trigger: '.kinetic-section',
    start: 'top center',
    end: 'bottom center',
    scrub: true
  }
});
```

```css
.kinetic-text {
  font-family: 'Instrument Serif', serif;
  font-variation-settings:
    'wght' var(--font-weight, 400),
    'wdth' var(--font-width, 100);
  font-size: clamp(48px, 12vw, 180px);
  transition: font-variation-settings 0.1s ease;
}
```

**4. Noise/Grain Overlays**
Nearly every award-winning dark-themed site uses a subtle noise texture to add organic quality.

```css
.noise-overlay::after {
  content: '';
  position: fixed;
  inset: 0;
  background-image: url("data:image/svg+xml,%3Csvg viewBox='0 0 256 256' xmlns='http://www.w3.org/2000/svg'%3E%3Cfilter id='n'%3E%3CfeTurbulence type='fractalNoise' baseFrequency='0.85' numOctaves='4' stitchTiles='stitch'/%3E%3C/filter%3E%3Crect width='100%25' height='100%25' filter='url(%23n)' opacity='0.04'/%3E%3C/svg%3E");
  pointer-events: none;
  z-index: 9999;
  opacity: 0.5;
  mix-blend-mode: overlay;
}
```

**5. Smooth Page Transitions**
Award-winning sites never have hard page loads. They use:
- View Transitions API (modern)
- Barba.js + GSAP (established pattern)
- Custom preloading with transition overlays

```javascript
// Barba.js + GSAP page transitions
import barba from '@barba/core';

barba.init({
  transitions: [{
    name: 'slide',
    leave(data) {
      return gsap.to(data.current.container, {
        opacity: 0,
        x: -100,
        duration: 0.5
      });
    },
    enter(data) {
      return gsap.from(data.next.container, {
        opacity: 0,
        x: 100,
        duration: 0.5
      });
    }
  }]
});
```

**6. Deconstructed / Broken Grid Layouts**
```css
.broken-grid {
  display: grid;
  grid-template-columns: repeat(12, 1fr);
  gap: 2rem;
}

.broken-grid .item-1 {
  grid-column: 2 / 7;
  grid-row: 1 / 3;
  transform: rotate(-2deg);
}

.broken-grid .item-2 {
  grid-column: 6 / 11;
  grid-row: 2 / 4;
  margin-top: -4rem;
  z-index: 2;
}

.broken-grid .item-3 {
  grid-column: 3 / 9;
  grid-row: 4 / 6;
  transform: rotate(1deg);
}
```

**7. Scroll-Velocity Effects**
Text or elements that respond to scroll speed, not just scroll position.

```javascript
// Text skew based on scroll velocity
let currentSkew = 0;
let lastScrollTop = 0;

function updateSkew() {
  const scrollTop = window.scrollY;
  const velocity = scrollTop - lastScrollTop;
  const targetSkew = Math.max(
    -15, Math.min(15, velocity * 0.3)
  );

  currentSkew += (targetSkew - currentSkew) * 0.1;

  document.querySelectorAll('.velocity-text').forEach(el => {
    el.style.transform = `skewY(${currentSkew}deg)`;
  });

  lastScrollTop = scrollTop;
  requestAnimationFrame(updateSkew);
}

requestAnimationFrame(updateSkew);
```

**8. WebGL Backgrounds and Effects**
Sites like Lusion, Active Theory, and Resn use WebGL for immersive backgrounds:
- Fluid simulations
- Particle systems
- Distortion effects on images
- Noise-based generative art
- Metaball effects

**9. Color and Theme Shifts**
Sections of the page have dramatically different color schemes, with smooth transitions between them as you scroll.

**10. Loading Experiences**
Award-winning sites turn the loading screen into a design moment:
```javascript
// Percentage-based loader with GSAP
const loader = { progress: 0 };

gsap.to(loader, {
  progress: 100,
  duration: 2.5,
  ease: 'power2.inOut',
  onUpdate: () => {
    document.querySelector('.loader-text').textContent =
      `${Math.round(loader.progress)}%`;
    document.querySelector('.loader-bar').style.transform =
      `scaleX(${loader.progress / 100})`;
  },
  onComplete: () => {
    const tl = gsap.timeline();
    tl.to('.loader', {
      yPercent: -100, duration: 0.8, ease: 'power4.inOut'
    })
    .from('.hero-content', {
      opacity: 0, y: 40, duration: 0.8
    }, '-=0.3');
  }
});
```

### Notable 2025-2026 Award Winners

- **Jeton** -- Fintech with scroll-based morphing desktop-to-mobile experience
- **Lusion** -- WebGL and 3D animations for immersive interactive design
- **The Renaissance Edition** -- Editorial design with scroll-driven storytelling
- **Design by Dylan** -- Portfolio with kinetic typography and custom transitions
- **Nicola Romei** -- Creative portfolio with experimental layouts

### What Separates Good from Great

1. **Restraint** -- The best sites know what NOT to animate
2. **Custom easing** -- Every animation has a crafted timing function, never defaults
3. **60fps everywhere** -- No frame drops, even on mobile
4. **Scroll as narrative** -- Scroll controls pacing, not just position
5. **Sound design** -- Subtle audio cues for interactions (emerging trend)
6. **Attention to load** -- Fast initial paint, progressive enhancement of animations
7. **Cross-device excellence** -- Thoughtful adaptation, not just responsive scaling
8. **Brand cohesion** -- Animation style is as distinctive as the logo

---

## Quick Reference: Library CDN Links

```html
<!-- GSAP + All Free Plugins -->
<script src="https://cdn.jsdelivr.net/npm/gsap@3/dist/gsap.min.js"></script>
<script src="https://cdn.jsdelivr.net/npm/gsap@3/dist/ScrollTrigger.min.js"></script>
<script src="https://cdn.jsdelivr.net/npm/gsap@3/dist/SplitText.min.js"></script>
<script src="https://cdn.jsdelivr.net/npm/gsap@3/dist/Flip.min.js"></script>
<script src="https://cdn.jsdelivr.net/npm/gsap@3/dist/DrawSVGPlugin.min.js"></script>
<script src="https://cdn.jsdelivr.net/npm/gsap@3/dist/MorphSVGPlugin.min.js"></script>
<script src="https://cdn.jsdelivr.net/npm/gsap@3/dist/MotionPathPlugin.min.js"></script>
<script src="https://cdn.jsdelivr.net/npm/gsap@3/dist/Observer.min.js"></script>
<script src="https://cdn.jsdelivr.net/npm/gsap@3/dist/TextPlugin.min.js"></script>

<!-- Anime.js v4 -->
<script src="https://cdn.jsdelivr.net/npm/animejs@4/lib/anime.min.js"></script>

<!-- Lenis (smooth scroll) -->
<script src="https://cdn.jsdelivr.net/npm/lenis@latest/dist/lenis.min.js"></script>

<!-- Lottie -->
<script src="https://cdnjs.cloudflare.com/ajax/libs/lottie-web/5.13.0/lottie_light.min.js"></script>

<!-- Three.js (import map) -->
<script type="importmap">
{
  "imports": {
    "three": "https://cdn.jsdelivr.net/npm/three@0.172/build/three.module.js",
    "three/addons/": "https://cdn.jsdelivr.net/npm/three@0.172/examples/jsm/"
  }
}
</script>

<!-- AOS -->
<link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/aos@2/dist/aos.css">
<script src="https://cdn.jsdelivr.net/npm/aos@2/dist/aos.js"></script>

<!-- Swiper -->
<link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/swiper@12/swiper-bundle.min.css">
<script src="https://cdn.jsdelivr.net/npm/swiper@12/swiper-bundle.min.js"></script>

<!-- tsParticles -->
<script src="https://cdn.jsdelivr.net/npm/@tsparticles/slim@3/tsparticles.slim.bundle.min.js"></script>

<!-- Typed.js -->
<script src="https://cdn.jsdelivr.net/npm/typed.js@2/dist/typed.umd.js"></script>

<!-- Splitting.js -->
<link rel="stylesheet" href="https://unpkg.com/splitting/dist/splitting.css">
<script src="https://unpkg.com/splitting/dist/splitting.min.js"></script>

<!-- Barba.js (page transitions) -->
<script src="https://unpkg.com/@barba/core"></script>
```

---

## Quick Reference: NPM Packages

```bash
# Animation
npm install gsap                        # GSAP + all plugins
npm install motion                      # Motion (Framer Motion successor)
npm install animejs                     # Anime.js v4
npm install @formkit/auto-animate       # AutoAnimate

# 3D
npm install three @types/three          # Three.js
npm install @react-three/fiber          # React Three Fiber
npm install @react-three/drei           # R3F helpers
npm install @splinetool/react-spline    # Spline React
npm install @splinetool/runtime         # Spline Vanilla JS

# Scroll
npm install lenis                       # Lenis smooth scroll
npm install locomotive-scroll           # Locomotive Scroll

# Lottie
npm install lottie-web                  # Lottie renderer
npm install @lottiefiles/dotlottie-react  # DotLottie React

# UI
npm install swiper                      # Swiper carousel
npm install typed.js                    # Typewriter effect
npm install splitting                   # Text splitting

# Page transitions
npm install @barba/core                 # Barba.js
```
