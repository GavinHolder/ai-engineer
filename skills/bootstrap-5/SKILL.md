---
name: bootstrap-5
description: Comprehensive Bootstrap 5.3.8 reference and rules for building production-grade, creative Bootstrap interfaces. Covers all components, utilities, grid system, color modes, CSS variables, forms, helpers, accessibility, and best practices. Use this skill for ALL Bootstrap-based frontend work.
---

# Bootstrap 5.3 — Complete Reference & Rules

**CDN (latest stable 5.3.8):**
```html
<link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.8/dist/css/bootstrap.min.css" rel="stylesheet">
<script src="https://cdn.jsdelivr.net/npm/bootstrap@5.3.8/dist/js/bootstrap.bundle.min.js"></script>
```

**Bootstrap Icons:**
```html
<link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/bootstrap-icons@1.11.3/font/bootstrap-icons.min.css">
```

**Required meta:**
```html
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
```

---

## Grid System

### Breakpoints

| Breakpoint | Class infix | Dimensions |
|---|---|---|
| Extra small | (none) | <576px |
| Small | `sm` | >=576px |
| Medium | `md` | >=768px |
| Large | `lg` | >=992px |
| Extra large | `xl` | >=1200px |
| XXL | `xxl` | >=1400px |

### Containers

| Class | xs | sm | md | lg | xl | xxl |
|---|---|---|---|---|---|---|
| `.container` | 100% | 540px | 720px | 960px | 1140px | 1320px |
| `.container-sm` | 100% | 540px | 720px | 960px | 1140px | 1320px |
| `.container-md` | 100% | 100% | 720px | 960px | 1140px | 1320px |
| `.container-lg` | 100% | 100% | 100% | 960px | 1140px | 1320px |
| `.container-xl` | 100% | 100% | 100% | 100% | 1140px | 1320px |
| `.container-xxl` | 100% | 100% | 100% | 100% | 100% | 1320px |
| `.container-fluid` | 100% | 100% | 100% | 100% | 100% | 100% |

### Columns

```html
<div class="container">
  <div class="row">
    <div class="col-12 col-md-6 col-lg-4">Responsive column</div>
  </div>
</div>
```

- `.col` — equal width
- `.col-{1-12}` — specific width
- `.col-{breakpoint}-{1-12}` — responsive width
- `.col-auto` — natural width
- `.row-cols-{1-6}` / `.row-cols-{breakpoint}-{1-6}` — columns per row
- `.offset-{breakpoint}-{0-11}` — column offsets
- `.g-{0-5}` — gutters (both), `.gx-{0-5}` — horizontal, `.gy-{0-5}` — vertical

### Alignment

- `.align-items-{start|center|end|baseline|stretch}` — row vertical align
- `.align-self-{start|center|end|baseline|stretch}` — column vertical align
- `.justify-content-{start|center|end|between|around|evenly}` — horizontal align
- `.order-{0-5|first|last}` — column ordering

---

## All Components

### Accordion

```html
<div class="accordion" id="acc1">
  <div class="accordion-item">
    <h2 class="accordion-header">
      <button class="accordion-button" type="button" data-bs-toggle="collapse" data-bs-target="#c1" aria-expanded="true" aria-controls="c1">Item 1</button>
    </h2>
    <div id="c1" class="accordion-collapse collapse show" data-bs-parent="#acc1">
      <div class="accordion-body">Content here</div>
    </div>
  </div>
</div>
```
Variants: `.accordion-flush` (no borders/rounded corners)

### Alerts

```html
<div class="alert alert-primary" role="alert">Primary alert</div>
```
Colors: `alert-{primary|secondary|success|danger|warning|info|light|dark}`
Extras: `.alert-dismissible`, `.alert-link`, `.alert-heading`
Dismiss: `<button class="btn-close" data-bs-dismiss="alert" aria-label="Close"></button>`

### Badge

```html
<span class="badge text-bg-primary">Badge</span>
<span class="badge rounded-pill text-bg-danger">Pill</span>
```
Colors: `text-bg-{primary|secondary|success|danger|warning|info|light|dark}`

### Breadcrumb

```html
<nav aria-label="breadcrumb">
  <ol class="breadcrumb">
    <li class="breadcrumb-item"><a href="#">Home</a></li>
    <li class="breadcrumb-item active" aria-current="page">Current</li>
  </ol>
</nav>
```

### Buttons

```html
<button class="btn btn-primary">Primary</button>
<button class="btn btn-outline-primary">Outline</button>
<button class="btn btn-lg">Large</button>
<button class="btn btn-sm">Small</button>
```
Colors: `btn-{primary|secondary|success|danger|warning|info|light|dark|link}`
Outlines: `btn-outline-{same colors}`
Sizes: `btn-lg`, `btn-sm`
States: `.active`, `.disabled`, `aria-disabled="true"`

### Button Group

```html
<div class="btn-group" role="group" aria-label="Label">
  <button class="btn btn-primary">Left</button>
  <button class="btn btn-primary">Middle</button>
  <button class="btn btn-primary">Right</button>
</div>
```
Variants: `.btn-group-lg`, `.btn-group-sm`, `.btn-group-vertical`

### Card

```html
<div class="card">
  <img src="..." class="card-img-top" alt="...">
  <div class="card-body">
    <h5 class="card-title">Title</h5>
    <h6 class="card-subtitle mb-2 text-body-secondary">Subtitle</h6>
    <p class="card-text">Text content</p>
    <a href="#" class="card-link">Link</a>
  </div>
  <div class="card-footer">Footer</div>
</div>
```
Parts: `.card-header`, `.card-body`, `.card-footer`, `.card-img-top`, `.card-img-bottom`, `.card-img-overlay`
Layouts: `.card-group`, `.row-cols-*` with cards

### Carousel

```html
<div id="carousel1" class="carousel slide" data-bs-ride="carousel">
  <div class="carousel-indicators">
    <button data-bs-target="#carousel1" data-bs-slide-to="0" class="active" aria-current="true"></button>
    <button data-bs-target="#carousel1" data-bs-slide-to="1"></button>
  </div>
  <div class="carousel-inner">
    <div class="carousel-item active"><img src="..." class="d-block w-100" alt="..."></div>
    <div class="carousel-item"><img src="..." class="d-block w-100" alt="..."></div>
  </div>
  <button class="carousel-control-prev" data-bs-target="#carousel1" data-bs-slide="prev">
    <span class="carousel-control-prev-icon" aria-hidden="true"></span>
    <span class="visually-hidden">Previous</span>
  </button>
  <button class="carousel-control-next" data-bs-target="#carousel1" data-bs-slide="next">
    <span class="carousel-control-next-icon" aria-hidden="true"></span>
    <span class="visually-hidden">Next</span>
  </button>
</div>
```
Options: `data-bs-interval="5000"`, `.carousel-fade`, `.carousel-dark` (deprecated, use `data-bs-theme="dark"`)

### Collapse

```html
<button class="btn btn-primary" data-bs-toggle="collapse" data-bs-target="#collapseExample">Toggle</button>
<div class="collapse" id="collapseExample">
  <div class="card card-body">Collapsible content</div>
</div>
```
Horizontal: `.collapse-horizontal`

### Dropdowns

```html
<div class="dropdown">
  <button class="btn btn-secondary dropdown-toggle" data-bs-toggle="dropdown" aria-expanded="false">Dropdown</button>
  <ul class="dropdown-menu">
    <li><h6 class="dropdown-header">Header</h6></li>
    <li><a class="dropdown-item" href="#">Action</a></li>
    <li><a class="dropdown-item active" href="#">Active</a></li>
    <li><a class="dropdown-item disabled" href="#">Disabled</a></li>
    <li><hr class="dropdown-divider"></li>
    <li><a class="dropdown-item" href="#">Separated</a></li>
  </ul>
</div>
```
Directions: `.dropup`, `.dropend`, `.dropstart`, `.dropdown-center`
Alignment: `.dropdown-menu-end`, `.dropdown-menu-{breakpoint}-end`
Auto close: `data-bs-auto-close="true|inside|outside|false"`

### List Group

```html
<ul class="list-group">
  <li class="list-group-item active" aria-current="true">Active</li>
  <li class="list-group-item">Item</li>
  <li class="list-group-item list-group-item-success">Success</li>
</ul>
```
Variants: `.list-group-flush`, `.list-group-numbered`, `.list-group-horizontal`
Colors: `list-group-item-{primary|secondary|success|danger|warning|info|light|dark}`
Actionable: `<a class="list-group-item list-group-item-action" href="#">`

### Modal

```html
<button class="btn btn-primary" data-bs-toggle="modal" data-bs-target="#modal1">Open</button>
<div class="modal fade" id="modal1" tabindex="-1" aria-labelledby="modal1Label" aria-hidden="true">
  <div class="modal-dialog">
    <div class="modal-content">
      <div class="modal-header">
        <h1 class="modal-title fs-5" id="modal1Label">Title</h1>
        <button class="btn-close" data-bs-dismiss="modal" aria-label="Close"></button>
      </div>
      <div class="modal-body">Content</div>
      <div class="modal-footer">
        <button class="btn btn-secondary" data-bs-dismiss="modal">Close</button>
        <button class="btn btn-primary">Save</button>
      </div>
    </div>
  </div>
</div>
```
Sizes: `.modal-sm`, `.modal-lg`, `.modal-xl`, `.modal-fullscreen`, `.modal-fullscreen-{breakpoint}-down`
Options: `.modal-dialog-centered`, `.modal-dialog-scrollable`
Backdrop: `data-bs-backdrop="static"` (no close on outside click)

### Navbar

```html
<nav class="navbar navbar-expand-lg bg-body-tertiary">
  <div class="container-fluid">
    <a class="navbar-brand" href="#">Brand</a>
    <button class="navbar-toggler" type="button" data-bs-toggle="collapse" data-bs-target="#navbarNav" aria-controls="navbarNav" aria-expanded="false" aria-label="Toggle navigation">
      <span class="navbar-toggler-icon"></span>
    </button>
    <div class="collapse navbar-collapse" id="navbarNav">
      <ul class="navbar-nav me-auto mb-2 mb-lg-0">
        <li class="nav-item"><a class="nav-link active" aria-current="page" href="#">Home</a></li>
        <li class="nav-item"><a class="nav-link" href="#">Link</a></li>
        <li class="nav-item dropdown">
          <a class="nav-link dropdown-toggle" data-bs-toggle="dropdown" href="#">Dropdown</a>
          <ul class="dropdown-menu">
            <li><a class="dropdown-item" href="#">Action</a></li>
          </ul>
        </li>
      </ul>
      <form class="d-flex" role="search">
        <input class="form-control me-2" type="search" placeholder="Search" aria-label="Search">
        <button class="btn btn-outline-success" type="submit">Search</button>
      </form>
    </div>
  </div>
</nav>
```
Color schemes: Use `data-bs-theme="dark"` on the nav element
Placement: `.fixed-top`, `.fixed-bottom`, `.sticky-top`, `.sticky-bottom`

### Navs & Tabs

```html
<!-- Tabs -->
<ul class="nav nav-tabs" role="tablist">
  <li class="nav-item" role="presentation">
    <button class="nav-link active" data-bs-toggle="tab" data-bs-target="#tab1" type="button" role="tab" aria-selected="true">Tab 1</button>
  </li>
</ul>
<div class="tab-content">
  <div class="tab-pane fade show active" id="tab1" role="tabpanel">Content 1</div>
</div>

<!-- Pills -->
<ul class="nav nav-pills">...</ul>

<!-- Underline (5.3+) -->
<ul class="nav nav-underline">...</ul>
```
Layout: `.nav-fill`, `.nav-justified`, `.flex-column`

### Offcanvas

```html
<button class="btn btn-primary" data-bs-toggle="offcanvas" data-bs-target="#offcanvas1">Open</button>
<div class="offcanvas offcanvas-start" tabindex="-1" id="offcanvas1" aria-labelledby="offcanvas1Label">
  <div class="offcanvas-header">
    <h5 class="offcanvas-title" id="offcanvas1Label">Title</h5>
    <button class="btn-close" data-bs-dismiss="offcanvas" aria-label="Close"></button>
  </div>
  <div class="offcanvas-body">Content</div>
</div>
```
Placement: `.offcanvas-start`, `.offcanvas-end`, `.offcanvas-top`, `.offcanvas-bottom`
Responsive: `.offcanvas-{breakpoint}` (offcanvas below breakpoint, normal above)
Options: `data-bs-scroll="true"`, `data-bs-backdrop="static"`

### Pagination

```html
<nav aria-label="Page navigation">
  <ul class="pagination">
    <li class="page-item disabled"><a class="page-link" href="#">Previous</a></li>
    <li class="page-item active" aria-current="page"><a class="page-link" href="#">1</a></li>
    <li class="page-item"><a class="page-link" href="#">2</a></li>
    <li class="page-item"><a class="page-link" href="#">Next</a></li>
  </ul>
</nav>
```
Sizes: `.pagination-lg`, `.pagination-sm`
Alignment: wrap in `.justify-content-center` or `.justify-content-end`

### Progress

```html
<div class="progress" role="progressbar" aria-valuenow="75" aria-valuemin="0" aria-valuemax="100">
  <div class="progress-bar" style="width: 75%">75%</div>
</div>
```
Variants: `.progress-bar-striped`, `.progress-bar-animated`, `.bg-{color}`
Stacked: Multiple `.progress-bar` inside one `.progress`

### Spinners

```html
<div class="spinner-border text-primary" role="status"><span class="visually-hidden">Loading...</span></div>
<div class="spinner-grow text-primary" role="status"><span class="visually-hidden">Loading...</span></div>
```
Sizes: `.spinner-border-sm`, `.spinner-grow-sm`

### Toasts

```html
<div class="toast" role="alert" aria-live="assertive" aria-atomic="true">
  <div class="toast-header">
    <strong class="me-auto">Title</strong>
    <small>Just now</small>
    <button class="btn-close" data-bs-dismiss="toast" aria-label="Close"></button>
  </div>
  <div class="toast-body">Message body</div>
</div>
```
Container: `.toast-container` with positioning classes
Options: `data-bs-autohide="false"`, `data-bs-delay="5000"`
JS: `const toast = new bootstrap.Toast(el); toast.show();`

### Tooltips (opt-in, requires JS init)

```html
<button data-bs-toggle="tooltip" data-bs-title="Tooltip text">Hover me</button>
<script>
  document.querySelectorAll('[data-bs-toggle="tooltip"]').forEach(el => new bootstrap.Tooltip(el));
</script>
```
Placement: `data-bs-placement="top|right|bottom|left"`
HTML: `data-bs-html="true"`

### Popovers (opt-in, requires JS init)

```html
<button data-bs-toggle="popover" data-bs-title="Title" data-bs-content="Content">Click me</button>
<script>
  document.querySelectorAll('[data-bs-toggle="popover"]').forEach(el => new bootstrap.Popover(el));
</script>
```
Trigger: `data-bs-trigger="hover|focus|click|manual"`
Dismiss on next click: `data-bs-trigger="focus"`

### Scrollspy

```html
<nav id="navbar-example" class="navbar bg-body-tertiary">...</nav>
<div data-bs-spy="scroll" data-bs-target="#navbar-example" data-bs-root-margin="0px 0px -40%" data-bs-smooth-scroll="true" tabindex="0">
  <div id="section1">...</div>
  <div id="section2">...</div>
</div>
```

### Placeholders (loading skeletons)

```html
<p class="placeholder-glow">
  <span class="placeholder col-6"></span>
  <span class="placeholder col-8"></span>
</p>
<a class="btn btn-primary disabled placeholder col-4" aria-disabled="true"></a>
```
Animations: `.placeholder-glow`, `.placeholder-wave`
Sizes: `.placeholder-lg`, `.placeholder-sm`, `.placeholder-xs`

---

## Forms

### Form Controls

```html
<div class="mb-3">
  <label for="email" class="form-label">Email</label>
  <input type="email" class="form-control" id="email" placeholder="name@example.com">
  <div class="form-text">Help text</div>
</div>
<div class="mb-3">
  <label for="textarea" class="form-label">Message</label>
  <textarea class="form-control" id="textarea" rows="3"></textarea>
</div>
```
Sizes: `.form-control-lg`, `.form-control-sm`
Readonly: `readonly`, `.form-control-plaintext` (readonly no border)
Color: `<input type="color" class="form-control form-control-color">`

### Select

```html
<select class="form-select" aria-label="Select">
  <option selected>Choose...</option>
  <option value="1">One</option>
</select>
```
Sizes: `.form-select-lg`, `.form-select-sm`
Multiple: `multiple`, `size="3"`

### Checks, Radios, Switches

```html
<!-- Checkbox -->
<div class="form-check">
  <input class="form-check-input" type="checkbox" id="check1">
  <label class="form-check-label" for="check1">Check me</label>
</div>

<!-- Radio -->
<div class="form-check">
  <input class="form-check-input" type="radio" name="radios" id="radio1">
  <label class="form-check-label" for="radio1">Radio</label>
</div>

<!-- Switch -->
<div class="form-check form-switch">
  <input class="form-check-input" type="checkbox" role="switch" id="switch1">
  <label class="form-check-label" for="switch1">Switch</label>
</div>

<!-- Inline -->
<div class="form-check form-check-inline">...</div>
```

### Floating Labels

```html
<div class="form-floating mb-3">
  <input type="email" class="form-control" id="floatingEmail" placeholder="name@example.com">
  <label for="floatingEmail">Email address</label>
</div>
```

### Input Group

```html
<div class="input-group mb-3">
  <span class="input-group-text">@</span>
  <input type="text" class="form-control" placeholder="Username">
</div>
<div class="input-group mb-3">
  <input type="text" class="form-control" placeholder="Search">
  <button class="btn btn-outline-secondary" type="button">Search</button>
</div>
```

### Range

```html
<input type="range" class="form-range" min="0" max="5" step="0.5" id="range1">
```

### Validation

```html
<form class="needs-validation" novalidate>
  <div class="mb-3">
    <input type="email" class="form-control" required>
    <div class="valid-feedback">Looks good!</div>
    <div class="invalid-feedback">Please enter a valid email.</div>
  </div>
  <button class="btn btn-primary" type="submit">Submit</button>
</form>
<script>
document.querySelectorAll('.needs-validation').forEach(form => {
  form.addEventListener('submit', e => {
    if (!form.checkValidity()) { e.preventDefault(); e.stopPropagation(); }
    form.classList.add('was-validated');
  });
});
</script>
```
Server-side: `.is-valid`, `.is-invalid` classes directly on inputs

---

## Color Modes (Dark Mode — 5.3+)

### Setup

```html
<html lang="en" data-bs-theme="light">
```

### Toggle via JS

```javascript
function setTheme(theme) {
  document.documentElement.setAttribute('data-bs-theme', theme);
  localStorage.setItem('theme', theme);
}
// Auto-detect system preference
const preferred = window.matchMedia('(prefers-color-scheme: dark)').matches ? 'dark' : 'light';
setTheme(localStorage.getItem('theme') || preferred);
```

### Color-mode-aware classes (adapt per theme)

- `text-bg-{color}` — combined text + background
- `.bg-body`, `.bg-body-secondary`, `.bg-body-tertiary` — adapt to mode
- `.text-body`, `.text-body-emphasis`, `.text-body-secondary`, `.text-body-tertiary`
- `.bg-{color}-subtle` — subtle background per color
- `.text-{color}-emphasis` — emphasis text per color
- `.border-{color}-subtle` — subtle border per color

### Scoped themes

```html
<!-- Dark section inside light page -->
<div data-bs-theme="dark" class="p-4 bg-body text-body">
  This section and all Bootstrap components inside adapt to dark mode
</div>
```

---

## Utility Classes — Quick Reference

### Spacing
`{m|p}{t|b|s|e|x|y}-{0|1|2|3|4|5|auto}` — margin/padding, sides, sizes
Responsive: `{m|p}{side}-{breakpoint}-{size}`

### Display
`.d-{none|inline|inline-block|block|grid|inline-grid|table|table-row|table-cell|flex|inline-flex}`
Responsive: `.d-{breakpoint}-{value}`
Print: `.d-print-{value}`

### Flex
`.flex-{row|column|row-reverse|column-reverse}`, `.flex-wrap`, `.flex-nowrap`
`.justify-content-{start|end|center|between|around|evenly}`
`.align-items-{start|end|center|baseline|stretch}`
`.align-self-{start|end|center|baseline|stretch}`
`.flex-grow-{0|1}`, `.flex-shrink-{0|1}`, `.gap-{0-5}`

### Text
`.text-{start|end|center}`, `.text-{breakpoint}-{start|end|center}`
`.fs-{1|2|3|4|5|6}` — font sizes
`.fw-{bold|bolder|semibold|medium|normal|light|lighter}`, `.fst-{italic|normal}`
`.text-decoration-{none|underline|line-through}`
`.text-{lowercase|uppercase|capitalize}`
`.text-truncate`, `.text-break`, `.text-nowrap`
`.lh-{1|sm|base|lg}`

### Colors
`.text-{primary|secondary|success|danger|warning|info|light|dark|body|body-emphasis|body-secondary|body-tertiary|black|white|muted}`
`.bg-{primary|secondary|success|danger|warning|info|light|dark|body|body-secondary|body-tertiary|black|white|transparent}`
`.text-opacity-{25|50|75|100}`, `.bg-opacity-{10|25|50|75|100}`

### Borders
`.border`, `.border-{top|end|bottom|start}`, `.border-0`, `.border-{side}-0`
`.border-{primary|secondary|success|danger|warning|info|light|dark|white|black}`
`.border-{1|2|3|4|5}` — width
`.rounded`, `.rounded-{0|1|2|3|4|5|circle|pill|top|end|bottom|start}`

### Shadows
`.shadow-none`, `.shadow-sm`, `.shadow`, `.shadow-lg`

### Position
`.position-{static|relative|absolute|fixed|sticky}`
`.top-{0|50|100}`, `.start-{0|50|100}`, `.bottom-{0|50|100}`, `.end-{0|50|100}`
`.translate-middle`, `.translate-middle-x`, `.translate-middle-y`

### Sizing
`.w-{25|50|75|100|auto}`, `.h-{25|50|75|100|auto}`
`.mw-100`, `.mh-100`, `.min-vw-100`, `.min-vh-100`, `.vw-100`, `.vh-100`

### Overflow
`.overflow-{auto|hidden|visible|scroll}`
`.overflow-x-{auto|hidden|visible|scroll}`, `.overflow-y-{auto|hidden|visible|scroll}`

### Visibility
`.visible`, `.invisible`
`.visually-hidden`, `.visually-hidden-focusable`

### Z-index
`.z-{n1|0|1|2|3}` (n1 = -1)

### Opacity
`.opacity-{0|25|50|75|100}`

### Object Fit
`.object-fit-{contain|cover|fill|scale|none}`, `.object-fit-{breakpoint}-{value}`

### Float
`.float-{start|end|none}`, `.float-{breakpoint}-{start|end|none}`

### Interactions
`.user-select-{all|auto|none}`, `.pe-{none|auto}` (pointer events)

---

## Helpers

- `.clearfix` — clear floats
- `.text-truncate` — single-line ellipsis
- `.vstack` — vertical flex stack with gap
- `.hstack` — horizontal flex stack with gap
- `.stretched-link` — make parent clickable
- `.ratio.ratio-{1x1|4x3|16x9|21x9}` — aspect ratios
- `.visually-hidden` — screen reader only
- `.focus-ring` / `.focus-ring-{color}` — custom focus styles
- `.icon-link` / `.icon-link-hover` — icon + text links
- `.link-opacity-{10|25|50|75|100}` — link transparency
- `.link-underline-{color}` — colored underlines
- `.link-offset-{1|2|3}` — underline offset

---

## Data Attributes Quick Reference

| Attribute | Use |
|---|---|
| `data-bs-toggle="collapse\|modal\|dropdown\|tab\|pill\|offcanvas\|tooltip\|popover\|button"` | Toggle components |
| `data-bs-dismiss="alert\|modal\|offcanvas\|toast"` | Dismiss components |
| `data-bs-target="#id"` | Target element |
| `data-bs-parent="#id"` | Accordion parent |
| `data-bs-ride="carousel"` | Auto-start carousel |
| `data-bs-slide="prev\|next"` | Carousel direction |
| `data-bs-theme="light\|dark"` | Color mode |
| `data-bs-backdrop="static"` | Prevent dismiss on click outside |
| `data-bs-scroll="true"` | Allow body scroll (offcanvas) |
| `data-bs-spy="scroll"` | Enable scrollspy |
| `data-bs-smooth-scroll="true"` | Smooth scroll (scrollspy) |
| `data-bs-placement="top\|right\|bottom\|left"` | Tooltip/popover position |
| `data-bs-trigger="hover\|focus\|click"` | Tooltip/popover trigger |
| `data-bs-title="text"` | Tooltip text |
| `data-bs-content="text"` | Popover body |
| `data-bs-interval="5000"` | Carousel interval |
| `data-bs-autohide="false"` | Persistent toast |
| `data-bs-delay="5000"` | Toast auto-hide delay |
| `data-bs-config='{...}'` | JSON options (any component) |

---

## JS Initialization Pattern

```javascript
document.addEventListener('DOMContentLoaded', () => {
  // Tooltips (opt-in)
  document.querySelectorAll('[data-bs-toggle="tooltip"]').forEach(el => new bootstrap.Tooltip(el));
  // Popovers (opt-in)
  document.querySelectorAll('[data-bs-toggle="popover"]').forEach(el => new bootstrap.Popover(el));
  // Form validation
  document.querySelectorAll('.needs-validation').forEach(form => {
    form.addEventListener('submit', e => {
      if (!form.checkValidity()) { e.preventDefault(); e.stopPropagation(); }
      form.classList.add('was-validated');
    });
  });
});
```

---

## CSS Variables Customization (No Sass Required)

Override Bootstrap's look with CSS variables directly:

```css
:root {
  --bs-primary: #your-color;
  --bs-primary-rgb: r, g, b;
  --bs-body-font-family: 'Your Font', sans-serif;
  --bs-body-bg: #0a0a0a;
  --bs-body-color: #e0e0e0;
  --bs-border-radius: 0.5rem;
  --bs-link-color: #your-accent;
}
```

Per-component overrides:
```html
<button class="btn btn-primary" style="--bs-btn-padding-y: .5rem; --bs-btn-font-size: .875rem;">Custom</button>
<div class="card" style="--bs-card-border-radius: 1rem; --bs-card-border-color: hotpink;">...</div>
```

---

## Starter Template

```html
<!doctype html>
<html lang="en" data-bs-theme="light">
<head>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width, initial-scale=1">
  <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.8/dist/css/bootstrap.min.css" rel="stylesheet">
  <link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/bootstrap-icons@1.11.3/font/bootstrap-icons.min.css">
  <title>Page Title</title>
</head>
<body class="d-flex flex-column min-vh-100">

  <!-- Navbar -->
  <nav class="navbar navbar-expand-lg bg-body-tertiary sticky-top">
    <div class="container">
      <a class="navbar-brand fw-bold" href="#">Brand</a>
      <button class="navbar-toggler" type="button" data-bs-toggle="collapse" data-bs-target="#mainNav" aria-controls="mainNav" aria-expanded="false" aria-label="Toggle navigation">
        <span class="navbar-toggler-icon"></span>
      </button>
      <div class="collapse navbar-collapse" id="mainNav">
        <ul class="navbar-nav me-auto mb-2 mb-lg-0">
          <li class="nav-item"><a class="nav-link active" aria-current="page" href="#">Home</a></li>
          <li class="nav-item"><a class="nav-link" href="#">About</a></li>
        </ul>
      </div>
    </div>
  </nav>

  <!-- Main -->
  <main class="container py-4 flex-grow-1">
    <h1 class="display-4 fw-bold text-body-emphasis">Hello World</h1>
    <p class="lead text-body-secondary">Start building here.</p>
  </main>

  <!-- Footer -->
  <footer class="bg-body-tertiary mt-auto py-3">
    <div class="container text-center text-body-secondary">
      <p class="mb-0">&copy; 2026</p>
    </div>
  </footer>

  <script src="https://cdn.jsdelivr.net/npm/bootstrap@5.3.8/dist/js/bootstrap.bundle.min.js"></script>
</body>
</html>
```

---

## Rules for Creative Bootstrap Work

1. **ALWAYS use the latest CDN** (5.3.8) — never hardcode older versions
2. **ALWAYS use color-mode-aware classes** (`bg-body`, `text-body-emphasis`, `bg-body-tertiary`) instead of hardcoded colors — these adapt to light/dark mode automatically
3. **ALWAYS use `text-bg-{color}`** for badges, alerts, and colored elements — combines text + bg correctly
4. **ALWAYS initialize tooltips and popovers** with JS — they are opt-in
5. **ALWAYS add `aria-*` attributes** for interactive components (modals, accordions, dropdowns, navbars)
6. **ALWAYS use `.visually-hidden`** for accessible text in icon-only buttons and spinners
7. **Use `data-bs-theme` for dark mode** — not deprecated `.navbar-dark` or `.carousel-dark`
8. **Customize via CSS variables** — not inline styles for colors. Override `--bs-*` variables.
9. **Combine with animation libraries** — Bootstrap handles layout and components; pair with GSAP, AOS, or CSS animations for motion
10. **Override the default look** — Bootstrap is a starting point, not the finish. Custom fonts, colors, and spacing make it distinctive
