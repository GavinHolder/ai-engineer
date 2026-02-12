---
name: html5
description: Comprehensive HTML5 reference covering all semantic elements, attributes, forms, media, accessibility (ARIA), meta tags, structured data, and modern best practices. Use this skill for ALL HTML work.
---

# HTML5 — Complete Reference & Best Practices

---

## Document Structure

```html
<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width, initial-scale=1">
  <meta name="description" content="Page description for SEO (150-160 chars)">
  <meta name="theme-color" content="#000000">
  <title>Page Title</title>
  <link rel="icon" href="/favicon.ico">
  <link rel="stylesheet" href="/styles.css">
</head>
<body>
  <!-- content -->
  <script src="/app.js" defer></script>
</body>
</html>
```

### Essential Meta Tags

```html
<!-- Character encoding (must be first in <head>) -->
<meta charset="utf-8">

<!-- Responsive viewport -->
<meta name="viewport" content="width=device-width, initial-scale=1">

<!-- SEO -->
<meta name="description" content="Page description">
<meta name="robots" content="index, follow">
<link rel="canonical" href="https://example.com/page">

<!-- Open Graph (social sharing) -->
<meta property="og:title" content="Title">
<meta property="og:description" content="Description">
<meta property="og:image" content="https://example.com/image.jpg">
<meta property="og:url" content="https://example.com/page">
<meta property="og:type" content="website">

<!-- Twitter Card -->
<meta name="twitter:card" content="summary_large_image">
<meta name="twitter:title" content="Title">
<meta name="twitter:description" content="Description">
<meta name="twitter:image" content="https://example.com/image.jpg">

<!-- PWA -->
<meta name="theme-color" content="#4285f4">
<link rel="manifest" href="/manifest.json">
<link rel="apple-touch-icon" href="/icon-192.png">

<!-- Preconnect / Prefetch -->
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="dns-prefetch" href="https://api.example.com">
<link rel="preload" href="/critical.css" as="style">
<link rel="prefetch" href="/next-page.html">
```

---

## Semantic Elements

### Page Layout

```html
<header>        <!-- Introductory content, nav, logo -->
<nav>           <!-- Navigation links -->
<main>          <!-- Primary content (one per page) -->
<article>       <!-- Self-contained content (blog post, news story) -->
<section>       <!-- Thematic grouping with heading -->
<aside>         <!-- Sidebar, tangentially related content -->
<footer>        <!-- Footer info, copyright, links -->
```

**Complete page layout:**

```html
<body>
  <header>
    <nav aria-label="Main navigation">
      <ul>
        <li><a href="/" aria-current="page">Home</a></li>
        <li><a href="/about">About</a></li>
        <li><a href="/contact">Contact</a></li>
      </ul>
    </nav>
  </header>

  <main>
    <article>
      <header>
        <h1>Article Title</h1>
        <time datetime="2026-02-12">February 12, 2026</time>
      </header>
      <section>
        <h2>Section Heading</h2>
        <p>Content...</p>
      </section>
      <footer>
        <p>Written by Author Name</p>
      </footer>
    </article>

    <aside aria-label="Related articles">
      <h2>Related</h2>
      <ul>
        <li><a href="/article-2">Related Article</a></li>
      </ul>
    </aside>
  </main>

  <footer>
    <p>&copy; 2026 Company Name</p>
  </footer>
</body>
```

### Content Sectioning

```html
<h1> - <h6>    <!-- Headings (only one h1 per page) -->
<hgroup>        <!-- Group heading + subtitle -->
<address>       <!-- Contact information for nearest article/body -->
<search>        <!-- Container for search functionality (new in HTML5) -->
```

```html
<hgroup>
  <h1>Main Title</h1>
  <p>Subtitle or tagline</p>
</hgroup>

<search>
  <form action="/search">
    <input type="search" name="q" placeholder="Search...">
    <button type="submit">Search</button>
  </form>
</search>
```

### Text Content

```html
<p>             <!-- Paragraph -->
<blockquote>    <!-- Extended quotation (cite attribute for source URL) -->
<figure>        <!-- Self-contained content with caption -->
<figcaption>    <!-- Caption for figure -->
<hr>            <!-- Thematic break -->
<pre>           <!-- Preformatted text -->
<ul> <ol> <li>  <!-- Unordered/ordered lists -->
<dl> <dt> <dd>  <!-- Description list -->
```

```html
<figure>
  <img src="chart.png" alt="Sales data for Q1 2026">
  <figcaption>Figure 1: Q1 2026 sales performance</figcaption>
</figure>

<blockquote cite="https://example.com/source">
  <p>The only way to do great work is to love what you do.</p>
  <footer>— <cite>Steve Jobs</cite></footer>
</blockquote>

<dl>
  <dt>HTML</dt>
  <dd>HyperText Markup Language</dd>
  <dt>CSS</dt>
  <dd>Cascading Style Sheets</dd>
</dl>
```

### Inline Text Semantics

```html
<a href="url">          <!-- Hyperlink -->
<strong>                <!-- Strong importance (bold) -->
<em>                    <!-- Emphasis (italic) -->
<mark>                  <!-- Highlighted/relevant text -->
<small>                 <!-- Side comments, fine print -->
<s>                     <!-- No longer accurate (strikethrough) -->
<del>                   <!-- Deleted text -->
<ins>                   <!-- Inserted text -->
<code>                  <!-- Code fragment -->
<kbd>                   <!-- Keyboard input -->
<samp>                  <!-- Sample output -->
<var>                   <!-- Variable -->
<time datetime="">      <!-- Machine-readable date/time -->
<abbr title="">         <!-- Abbreviation -->
<cite>                  <!-- Title of a work -->
<q>                     <!-- Inline quotation -->
<sub>                   <!-- Subscript -->
<sup>                   <!-- Superscript -->
<br>                    <!-- Line break -->
<wbr>                   <!-- Word break opportunity -->
<span>                  <!-- Generic inline container -->
<data value="">         <!-- Machine-readable content -->
<ruby> <rt> <rp>        <!-- Ruby annotation (east Asian text) -->
<bdi>                   <!-- Bidirectional isolate -->
<bdo dir="rtl">         <!-- Bidirectional override -->
```

```html
<p>The meeting is at <time datetime="2026-02-12T14:00">2pm on Feb 12</time>.</p>
<p>Press <kbd>Ctrl</kbd> + <kbd>C</kbd> to copy.</p>
<p>The <abbr title="World Wide Web Consortium">W3C</abbr> maintains web standards.</p>
<p>Status: <data value="2">Shipped</data></p>
```

---

## Forms — Complete Reference

### Form Element

```html
<form action="/submit" method="post" enctype="multipart/form-data"
      autocomplete="on" novalidate>
```

| Attribute | Values | Purpose |
|-----------|--------|---------|
| `action` | URL | Where to submit |
| `method` | `get`, `post`, `dialog` | HTTP method |
| `enctype` | `application/x-www-form-urlencoded`, `multipart/form-data`, `text/plain` | Encoding (use multipart for file uploads) |
| `autocomplete` | `on`, `off` | Browser autofill |
| `novalidate` | boolean | Skip HTML validation |
| `target` | `_self`, `_blank`, `_parent`, `_top` | Where to display response |

### Input Types

```html
<!-- Text inputs -->
<input type="text" name="name" placeholder="Your name" required>
<input type="email" name="email" required>
<input type="password" name="password" minlength="8">
<input type="url" name="website" placeholder="https://...">
<input type="tel" name="phone" pattern="[0-9]{3}-[0-9]{4}">
<input type="search" name="q" placeholder="Search...">

<!-- Numeric inputs -->
<input type="number" name="qty" min="1" max="100" step="1">
<input type="range" name="volume" min="0" max="100" value="50">

<!-- Date/time inputs -->
<input type="date" name="date" min="2026-01-01" max="2026-12-31">
<input type="time" name="time">
<input type="datetime-local" name="meeting">
<input type="month" name="month">
<input type="week" name="week">

<!-- Selection inputs -->
<input type="checkbox" name="agree" value="yes" checked>
<input type="radio" name="color" value="red">
<input type="radio" name="color" value="blue">

<!-- File inputs -->
<input type="file" name="avatar" accept="image/*">
<input type="file" name="docs" accept=".pdf,.doc" multiple>

<!-- Color picker -->
<input type="color" name="theme" value="#ff0000">

<!-- Hidden data -->
<input type="hidden" name="csrf_token" value="abc123">

<!-- Buttons -->
<input type="submit" value="Submit">
<input type="reset" value="Reset">
<button type="submit">Submit</button>
<button type="button">Custom Action</button>
```

### Input Attributes

| Attribute | Purpose | Example |
|-----------|---------|---------|
| `required` | Must be filled | `<input required>` |
| `disabled` | Cannot interact | `<input disabled>` |
| `readonly` | Cannot edit, submits | `<input readonly>` |
| `placeholder` | Hint text | `<input placeholder="Enter name">` |
| `value` | Default value | `<input value="default">` |
| `name` | Form data key | `<input name="email">` |
| `id` | Unique identifier | `<input id="email">` |
| `autocomplete` | Autofill hint | `<input autocomplete="email">` |
| `autofocus` | Focus on load | `<input autofocus>` |
| `pattern` | Regex validation | `<input pattern="[A-Z]{3}">` |
| `minlength` / `maxlength` | Text length | `<input minlength="3" maxlength="50">` |
| `min` / `max` | Numeric range | `<input min="0" max="100">` |
| `step` | Numeric increment | `<input step="0.01">` |
| `multiple` | Multiple values | `<input type="file" multiple>` |
| `accept` | File types | `<input accept="image/*,.pdf">` |
| `list` | Datalist reference | `<input list="options">` |
| `form` | Associate with form | `<input form="formId">` |
| `inputmode` | Virtual keyboard | `<input inputmode="numeric">` |
| `enterkeyhint` | Enter key label | `<input enterkeyhint="search">` |
| `spellcheck` | Spell check | `<input spellcheck="false">` |

### Autocomplete Values

```html
<input autocomplete="name">            <!-- Full name -->
<input autocomplete="given-name">      <!-- First name -->
<input autocomplete="family-name">     <!-- Last name -->
<input autocomplete="email">           <!-- Email -->
<input autocomplete="tel">             <!-- Phone -->
<input autocomplete="street-address">  <!-- Street -->
<input autocomplete="address-line1">   <!-- Address line 1 -->
<input autocomplete="postal-code">     <!-- Zip/postal -->
<input autocomplete="country">         <!-- Country -->
<input autocomplete="cc-number">       <!-- Credit card -->
<input autocomplete="cc-exp">          <!-- Card expiry -->
<input autocomplete="new-password">    <!-- New password (password managers) -->
<input autocomplete="current-password"> <!-- Existing password -->
<input autocomplete="one-time-code">   <!-- OTP/2FA code -->
<input autocomplete="off">             <!-- Disable autofill -->
```

### Textarea

```html
<textarea name="message" rows="5" cols="40"
          maxlength="500" placeholder="Your message..."
          wrap="soft" required></textarea>
```

### Select / Datalist

```html
<!-- Dropdown -->
<select name="country" required>
  <option value="">Choose...</option>
  <optgroup label="Europe">
    <option value="uk">United Kingdom</option>
    <option value="fr">France</option>
  </optgroup>
  <optgroup label="Americas">
    <option value="us">United States</option>
  </optgroup>
</select>

<!-- Multi-select -->
<select name="skills" multiple size="4">
  <option value="html">HTML</option>
  <option value="css">CSS</option>
  <option value="js">JavaScript</option>
</select>

<!-- Datalist (autocomplete suggestions) -->
<input type="text" list="browsers" name="browser">
<datalist id="browsers">
  <option value="Chrome">
  <option value="Firefox">
  <option value="Safari">
  <option value="Edge">
</datalist>
```

### Labels & Fieldset

```html
<!-- Explicit label (preferred) -->
<label for="email">Email:</label>
<input type="email" id="email" name="email">

<!-- Implicit label -->
<label>Email: <input type="email" name="email"></label>

<!-- Fieldset for grouping -->
<fieldset>
  <legend>Shipping Address</legend>
  <label for="street">Street:</label>
  <input type="text" id="street" name="street">
  <label for="city">City:</label>
  <input type="text" id="city" name="city">
</fieldset>
```

### Output & Meter & Progress

```html
<!-- Calculation result -->
<output name="result" for="a b">60</output>

<!-- Scalar measurement (known range) -->
<meter value="0.7" min="0" max="1" low="0.3" high="0.7" optimum="0.8">70%</meter>

<!-- Task completion -->
<progress value="70" max="100">70%</progress>
<progress>Loading...</progress> <!-- Indeterminate -->
```

### Form Validation (HTML5 Built-in)

```html
<form>
  <input type="email" required>               <!-- Must be valid email -->
  <input type="text" pattern="[A-Z]{2,5}"     <!-- Regex match -->
         title="2-5 uppercase letters">
  <input type="number" min="1" max="10">      <!-- Range check -->
  <input type="text" minlength="3">           <!-- Min length -->

  <!-- Custom validation message -->
  <input type="text" required
         oninvalid="this.setCustomValidity('Please fill this in')"
         oninput="this.setCustomValidity('')">
</form>

<!-- CSS pseudo-classes for validation state -->
<!-- :valid, :invalid, :required, :optional, :in-range, :out-of-range -->
```

---

## Media Elements

### Images

```html
<!-- Basic image (always include alt) -->
<img src="photo.jpg" alt="Descriptive text" width="800" height="600" loading="lazy">

<!-- Responsive images (different sizes) -->
<img src="photo-800.jpg"
     srcset="photo-400.jpg 400w,
             photo-800.jpg 800w,
             photo-1200.jpg 1200w"
     sizes="(max-width: 600px) 400px,
            (max-width: 1000px) 800px,
            1200px"
     alt="Photo description">

<!-- Art direction (different crops) -->
<picture>
  <source media="(max-width: 600px)" srcset="photo-mobile.jpg">
  <source media="(max-width: 1000px)" srcset="photo-tablet.jpg">
  <img src="photo-desktop.jpg" alt="Photo description">
</picture>

<!-- Modern formats with fallback -->
<picture>
  <source type="image/avif" srcset="photo.avif">
  <source type="image/webp" srcset="photo.webp">
  <img src="photo.jpg" alt="Photo description">
</picture>
```

| Attribute | Purpose |
|-----------|---------|
| `alt` | Alternative text (required for accessibility) |
| `loading="lazy"` | Defer offscreen images |
| `loading="eager"` | Load immediately (default) |
| `decoding="async"` | Decode off main thread |
| `fetchpriority="high"` | Prioritize loading (LCP images) |
| `width` / `height` | Prevent layout shift (CLS) |

### Video

```html
<video controls width="640" height="360" poster="thumb.jpg"
       preload="metadata" playsinline>
  <source src="video.mp4" type="video/mp4">
  <source src="video.webm" type="video/webm">
  <track kind="subtitles" src="subs-en.vtt" srclang="en" label="English" default>
  <track kind="subtitles" src="subs-es.vtt" srclang="es" label="Spanish">
  <p>Your browser doesn't support video. <a href="video.mp4">Download</a>.</p>
</video>
```

| Attribute | Purpose |
|-----------|---------|
| `controls` | Show playback controls |
| `autoplay` | Auto-start (requires `muted` in most browsers) |
| `muted` | Start muted |
| `loop` | Loop playback |
| `poster` | Preview image |
| `preload` | `none`, `metadata`, `auto` |
| `playsinline` | Inline on mobile (no fullscreen) |

### Audio

```html
<audio controls preload="metadata">
  <source src="audio.mp3" type="audio/mpeg">
  <source src="audio.ogg" type="audio/ogg">
  <p>Your browser doesn't support audio.</p>
</audio>
```

### Embed / Iframe

```html
<!-- Iframe (external content) -->
<iframe src="https://example.com" width="600" height="400"
        title="Description for accessibility"
        loading="lazy"
        sandbox="allow-scripts allow-same-origin"
        allow="fullscreen; picture-in-picture"
        referrerpolicy="no-referrer">
</iframe>

<!-- Sandbox values: allow-forms, allow-modals, allow-popups,
     allow-scripts, allow-same-origin, allow-top-navigation -->
```

---

## Tables

```html
<table>
  <caption>Monthly Sales 2026</caption>
  <colgroup>
    <col style="width: 40%">
    <col style="width: 30%">
    <col style="width: 30%">
  </colgroup>
  <thead>
    <tr>
      <th scope="col">Product</th>
      <th scope="col">Q1</th>
      <th scope="col">Q2</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th scope="row">Widget A</th>
      <td>1,200</td>
      <td>1,450</td>
    </tr>
    <tr>
      <th scope="row">Widget B</th>
      <td>800</td>
      <td>920</td>
    </tr>
  </tbody>
  <tfoot>
    <tr>
      <th scope="row">Total</th>
      <td>2,000</td>
      <td>2,370</td>
    </tr>
  </tfoot>
</table>
```

| Attribute | Purpose |
|-----------|---------|
| `scope="col"` | Header for column |
| `scope="row"` | Header for row |
| `colspan="2"` | Span columns |
| `rowspan="3"` | Span rows |

---

## Interactive Elements

### Details / Summary (native accordion)

```html
<details>
  <summary>Click to expand</summary>
  <p>Hidden content revealed on click.</p>
</details>

<!-- Open by default -->
<details open>
  <summary>Already expanded</summary>
  <p>Visible content.</p>
</details>

<!-- Exclusive accordion (name attribute) -->
<details name="faq">
  <summary>Question 1</summary>
  <p>Answer 1</p>
</details>
<details name="faq">
  <summary>Question 2</summary>
  <p>Answer 2</p>
</details>
```

### Dialog (native modal)

```html
<dialog id="myDialog">
  <h2>Dialog Title</h2>
  <p>Dialog content</p>
  <form method="dialog">
    <button value="cancel">Cancel</button>
    <button value="confirm">Confirm</button>
  </form>
</dialog>

<button onclick="document.getElementById('myDialog').showModal()">
  Open Dialog
</button>
```

```javascript
const dialog = document.getElementById('myDialog')
dialog.showModal()    // Modal (with backdrop, traps focus)
dialog.show()         // Non-modal
dialog.close()        // Close
dialog.returnValue    // The button value that closed it
```

### Popover (new in HTML)

```html
<button popovertarget="mypopover">Toggle Popover</button>
<div id="mypopover" popover>
  <p>Popover content</p>
</div>

<!-- Manual popover (doesn't auto-close on outside click) -->
<div id="mypopover" popover="manual">...</div>

<!-- Show/hide actions -->
<button popovertarget="pop" popovertargetaction="show">Show</button>
<button popovertarget="pop" popovertargetaction="hide">Hide</button>
```

---

## Accessibility (ARIA)

### Landmark Roles (prefer semantic elements)

```html
<!-- Semantic elements have implicit roles -->
<header>    <!-- role="banner" -->
<nav>       <!-- role="navigation" -->
<main>      <!-- role="main" -->
<aside>     <!-- role="complementary" -->
<footer>    <!-- role="contentinfo" -->
<form>      <!-- role="form" (when named) -->
<section>   <!-- role="region" (when named) -->
```

### Essential ARIA Attributes

```html
<!-- Labels -->
<button aria-label="Close dialog">X</button>
<nav aria-label="Main navigation">...</nav>
<section aria-labelledby="section-title">
  <h2 id="section-title">Features</h2>
</section>
<input aria-describedby="help-text">
<p id="help-text">Must be at least 8 characters.</p>

<!-- States -->
<button aria-expanded="false" aria-controls="menu">Menu</button>
<div id="menu" aria-hidden="true">...</div>
<button aria-pressed="true">Bold</button>
<input aria-invalid="true" aria-errormessage="err1">
<span id="err1">Email is required</span>

<!-- Live regions (dynamic content updates) -->
<div aria-live="polite">Status messages appear here</div>
<div aria-live="assertive">Urgent alerts appear here</div>
<div role="status">Items loaded: 42</div>
<div role="alert">Error: connection lost</div>

<!-- Navigation -->
<a href="/page" aria-current="page">Current Page</a>
<li aria-current="step">Step 2</li>

<!-- Relationships -->
<div role="tablist">
  <button role="tab" aria-selected="true" aria-controls="panel1">Tab 1</button>
</div>
<div role="tabpanel" id="panel1" aria-labelledby="tab1">Content</div>
```

### Common ARIA Patterns

```html
<!-- Skip to content link -->
<a href="#main-content" class="skip-link">Skip to main content</a>
<main id="main-content">...</main>

<!-- Visually hidden (screen reader only) -->
<span class="sr-only">Additional context for screen readers</span>

<!-- Icon button -->
<button aria-label="Delete item">
  <svg aria-hidden="true">...</svg>
</button>

<!-- Loading state -->
<div aria-busy="true" aria-live="polite">
  <p>Loading results...</p>
</div>

<!-- Required field -->
<label for="email">Email <span aria-hidden="true">*</span></label>
<input id="email" type="email" required aria-required="true">
```

---

## Script Loading

```html
<!-- Defer: download in parallel, execute after parsing (preserves order) -->
<script src="app.js" defer></script>

<!-- Async: download in parallel, execute immediately (no order guarantee) -->
<script src="analytics.js" async></script>

<!-- Module: deferred by default, strict mode, import/export -->
<script type="module" src="app.mjs"></script>

<!-- Inline module -->
<script type="module">
  import { init } from './app.mjs'
  init()
</script>

<!-- Import map (resolve bare specifiers) -->
<script type="importmap">
{
  "imports": {
    "react": "https://esm.sh/react@19",
    "react-dom": "https://esm.sh/react-dom@19"
  }
}
</script>
```

| Strategy | Download | Execute | Order | Use Case |
|----------|----------|---------|-------|----------|
| `<script>` | Blocks | Blocks | Yes | Inline scripts |
| `defer` | Parallel | After DOM parsed | Yes | App code |
| `async` | Parallel | When ready | No | Analytics, ads |
| `type="module"` | Parallel | After DOM parsed | Yes | ES modules |

---

## Global Attributes (available on all elements)

| Attribute | Purpose |
|-----------|---------|
| `id` | Unique identifier |
| `class` | CSS classes |
| `style` | Inline styles |
| `title` | Tooltip text |
| `lang` | Language code |
| `dir` | Text direction (`ltr`, `rtl`, `auto`) |
| `hidden` | Hide element |
| `tabindex` | Tab order (`0` = focusable, `-1` = programmatic only) |
| `contenteditable` | Make editable |
| `draggable` | Enable drag |
| `spellcheck` | Spell checking |
| `translate` | Should content be translated |
| `data-*` | Custom data attributes |
| `inert` | Disable all interaction and accessibility |
| `autofocus` | Focus on page load |
| `enterkeyhint` | Virtual keyboard enter key label |
| `inputmode` | Virtual keyboard type |
| `popover` | Make element a popover |
| `anchor` | Anchor positioning reference |

---

## Best Practices

1. **Always set `lang` attribute** on `<html>` — screen readers need it
2. **One `<h1>` per page** — heading hierarchy must be logical (h1 > h2 > h3)
3. **All images need `alt`** — empty `alt=""` for decorative images
4. **Use semantic elements** — `<nav>`, `<main>`, `<article>` over generic `<div>`
5. **Labels for all inputs** — every form control needs a visible `<label>`
6. **Set `width` and `height` on images** — prevents layout shift (CLS)
7. **Use `loading="lazy"`** for offscreen images and iframes
8. **Use `fetchpriority="high"`** for LCP (largest contentful paint) images
9. **Scripts: `defer` by default** — `async` only for independent scripts
10. **Forms: use native validation** — `required`, `type`, `pattern`, `min/max`
11. **Tables: use `<caption>`, `<thead>`, `<th scope>`** — accessible data tables
12. **Don't use ARIA if a native element works** — `<button>` beats `<div role="button">`
13. **Interactive elements must be keyboard accessible** — focusable, activatable with Enter/Space
14. **Color alone must not convey meaning** — add text, icons, or patterns
15. **Minimum touch target: 44x44px** — mobile accessibility
