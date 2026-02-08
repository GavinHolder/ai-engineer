# Bootstrap 5.3 Complete Reference

**Current Version:** v5.3.8 | **License:** MIT | **CSS Framework** | **Mobile-First, Responsive**

---

## CDN Quick Start

```html
<!doctype html>
<html lang="en" data-bs-theme="light">
<head>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width, initial-scale=1">
  <title>Bootstrap 5.3</title>
  <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.8/dist/css/bootstrap.min.css" rel="stylesheet"
        integrity="sha384-sRIl4kxILFvY47J16cr9ZwB07vP4J8+LH7qKQnuqkuIAvNWLzeN8tE5YBujZqJLB" crossorigin="anonymous">
</head>
<body>
  <h1>Hello, world!</h1>
  <script src="https://cdn.jsdelivr.net/npm/bootstrap@5.3.8/dist/js/bootstrap.bundle.min.js"
          integrity="sha384-FKyoEForCGlyvwx9Hj09JcYn3nv7wiPVlz7YYwJrWVcXK/BmnVDxM+D2scQbITxI" crossorigin="anonymous"></script>
</body>
</html>
```

**Separate JS files (if not using bundle):**
- Popper: `https://cdn.jsdelivr.net/npm/@popperjs/core@2.11.8/dist/umd/popper.min.js`
- Bootstrap JS: `https://cdn.jsdelivr.net/npm/bootstrap@5.3.8/dist/js/bootstrap.min.js`

---

## 1. GRID SYSTEM

### Breakpoints

| Breakpoint | Infix | Min-Width | Container Max |
|------------|-------|-----------|---------------|
| Extra small | (none) | <576px | 100% |
| Small | `sm` | >=576px | 540px |
| Medium | `md` | >=768px | 720px |
| Large | `lg` | >=992px | 960px |
| Extra large | `xl` | >=1200px | 1140px |
| XXL | `xxl` | >=1400px | 1320px |

### Containers

```
.container          - Responsive pixel-width at each breakpoint
.container-fluid    - 100% width at all breakpoints
.container-sm       - 100% until sm breakpoint
.container-md       - 100% until md breakpoint
.container-lg       - 100% until lg breakpoint
.container-xl       - 100% until xl breakpoint
.container-xxl      - 100% until xxl breakpoint
```

### Rows & Columns

```
.row                          - Flex container for columns
.col                          - Equal-width auto column
.col-{1-12}                   - Specific width (xs and up)
.col-auto                     - Natural content width
.col-{sm|md|lg|xl|xxl}-{1-12} - Responsive column widths
.col-{sm|md|lg|xl|xxl}-auto   - Responsive auto width
```

### Row Columns (control number of columns)

```
.row-cols-{1-6}                          - Set columns per row
.row-cols-auto                           - Auto width columns
.row-cols-{sm|md|lg|xl|xxl}-{1-6|auto}  - Responsive row columns
```

### Gutters

```
.g-{0-5}    - All gutters
.gx-{0-5}   - Horizontal gutters
.gy-{0-5}   - Vertical gutters
.g-{sm|md|lg|xl|xxl}-{0-5}   - Responsive gutters
```

### Offsets

```
.offset-{1-11}                          - Offset columns
.offset-{sm|md|lg|xl|xxl}-{0-11}       - Responsive offsets
```

### Alignment

```
.justify-content-{start|end|center|between|around|evenly}
.justify-content-{sm|md|lg|xl|xxl}-{start|end|center|between|around|evenly}
.align-items-{start|end|center|baseline|stretch}
.align-items-{sm|md|lg|xl|xxl}-{start|end|center|baseline|stretch}
.align-self-{start|end|center|baseline|stretch}
.align-self-{sm|md|lg|xl|xxl}-{start|end|center|baseline|stretch}
```

### Example

```html
<div class="container">
  <div class="row g-4">
    <div class="col-12 col-md-8">.col-12 .col-md-8</div>
    <div class="col-6 col-md-4">.col-6 .col-md-4</div>
  </div>
</div>
```

---

## 2. ALL COMPONENTS

### 2.1 Accordion

**Classes:** `.accordion`, `.accordion-item`, `.accordion-header`, `.accordion-button`, `.accordion-collapse`, `.accordion-body`, `.accordion-flush`
**States:** `.show`, `.collapsed`, `.collapse`, `.collapsing`

```html
<div class="accordion" id="myAccordion">
  <div class="accordion-item">
    <h2 class="accordion-header">
      <button class="accordion-button" type="button" data-bs-toggle="collapse"
              data-bs-target="#collapseOne" aria-expanded="true" aria-controls="collapseOne">
        Item #1
      </button>
    </h2>
    <div id="collapseOne" class="accordion-collapse collapse show" data-bs-parent="#myAccordion">
      <div class="accordion-body">Content here.</div>
    </div>
  </div>
</div>
```

**Variations:**
- Default (mutually exclusive): use `data-bs-parent="#id"`
- Flush: add `.accordion-flush` to `.accordion`
- Always open: omit `data-bs-parent`

---

### 2.2 Alerts

**Classes:** `.alert`, `.alert-{primary|secondary|success|danger|warning|info|light|dark}`, `.alert-dismissible`, `.alert-link`, `.alert-heading`
**Animation:** `.fade`, `.show`

```html
<div class="alert alert-success alert-dismissible fade show" role="alert">
  <h4 class="alert-heading">Well done!</h4>
  <p>Content with <a href="#" class="alert-link">a link</a>.</p>
  <button type="button" class="btn-close" data-bs-dismiss="alert" aria-label="Close"></button>
</div>
```

**JS:** `new bootstrap.Alert(el)` | Methods: `.close()`, `.dispose()`
**Events:** `close.bs.alert`, `closed.bs.alert`

---

### 2.3 Badges

**Classes:** `.badge`, `.rounded-pill`
**Colors:** Use `.text-bg-{primary|secondary|success|danger|warning|info|light|dark}`

```html
<span class="badge text-bg-primary">Primary</span>
<span class="badge rounded-pill text-bg-danger">99+</span>

<!-- Positioned badge -->
<button type="button" class="btn btn-primary position-relative">
  Inbox
  <span class="position-absolute top-0 start-100 translate-middle badge rounded-pill bg-danger">
    99+ <span class="visually-hidden">unread messages</span>
  </span>
</button>
```

---

### 2.4 Breadcrumb

**Classes:** `.breadcrumb`, `.breadcrumb-item`

```html
<nav aria-label="breadcrumb">
  <ol class="breadcrumb">
    <li class="breadcrumb-item"><a href="#">Home</a></li>
    <li class="breadcrumb-item active" aria-current="page">Library</li>
  </ol>
</nav>
```

**Custom divider:** `style="--bs-breadcrumb-divider: '>';"`

---

### 2.5 Buttons

**Base:** `.btn`
**Variants:** `.btn-{primary|secondary|success|danger|warning|info|light|dark|link}`
**Outline:** `.btn-outline-{primary|secondary|success|danger|warning|info|light|dark}`
**Sizes:** `.btn-lg`, `.btn-sm`
**States:** `.active`, `.disabled`, `disabled` attribute
**Toggle:** `data-bs-toggle="button"`, `aria-pressed="true"`

```html
<button type="button" class="btn btn-primary">Primary</button>
<button type="button" class="btn btn-outline-secondary btn-lg">Large Outline</button>
<a class="btn btn-primary disabled" role="button" aria-disabled="true">Disabled Link</a>

<!-- Block buttons -->
<div class="d-grid gap-2">
  <button class="btn btn-primary" type="button">Block Button</button>
</div>

<!-- Toggle button -->
<button type="button" class="btn btn-primary" data-bs-toggle="button">Toggle</button>
```

**Elements:** `<button>`, `<a role="button">`, `<input type="button|submit|reset">`

---

### 2.6 Button Group

**Classes:** `.btn-group`, `.btn-group-vertical`, `.btn-toolbar`, `.btn-group-lg`, `.btn-group-sm`

```html
<div class="btn-group" role="group" aria-label="Basic example">
  <button type="button" class="btn btn-primary">Left</button>
  <button type="button" class="btn btn-primary">Middle</button>
  <button type="button" class="btn btn-primary">Right</button>
</div>

<!-- Checkbox toggle group -->
<div class="btn-group" role="group">
  <input type="checkbox" class="btn-check" id="btncheck1">
  <label class="btn btn-outline-primary" for="btncheck1">Checkbox 1</label>
</div>

<!-- Toolbar -->
<div class="btn-toolbar" role="toolbar" aria-label="Toolbar">
  <div class="btn-group me-2" role="group">...</div>
  <div class="btn-group" role="group">...</div>
</div>
```

---

### 2.7 Card

**Classes:** `.card`, `.card-body`, `.card-header`, `.card-footer`, `.card-title`, `.card-subtitle`, `.card-text`, `.card-link`, `.card-img-top`, `.card-img-bottom`, `.card-img`, `.card-img-overlay`, `.card-group`, `.card-header-tabs`, `.card-header-pills`

```html
<div class="card" style="width: 18rem;">
  <img src="..." class="card-img-top" alt="...">
  <div class="card-body">
    <h5 class="card-title">Card title</h5>
    <h6 class="card-subtitle mb-2 text-body-secondary">Card subtitle</h6>
    <p class="card-text">Some text content.</p>
    <a href="#" class="card-link">Card link</a>
  </div>
</div>

<!-- Horizontal card -->
<div class="card mb-3" style="max-width: 540px;">
  <div class="row g-0">
    <div class="col-md-4">
      <img src="..." class="img-fluid rounded-start" alt="...">
    </div>
    <div class="col-md-8">
      <div class="card-body">
        <h5 class="card-title">Card title</h5>
        <p class="card-text">Content here.</p>
      </div>
    </div>
  </div>
</div>

<!-- Image overlay -->
<div class="card text-bg-dark">
  <img src="..." class="card-img" alt="...">
  <div class="card-img-overlay">
    <h5 class="card-title">Card title</h5>
  </div>
</div>

<!-- Card group with equal heights -->
<div class="row row-cols-1 row-cols-md-3 g-4">
  <div class="col"><div class="card h-100">...</div></div>
</div>
```

**Colors:** `.text-bg-{color}`, `.border-{color}`, `.bg-transparent`

---

### 2.8 Carousel

**Classes:** `.carousel`, `.carousel.slide`, `.carousel-fade`, `.carousel-inner`, `.carousel-item`, `.carousel-control-prev`, `.carousel-control-next`, `.carousel-control-prev-icon`, `.carousel-control-next-icon`, `.carousel-indicators`, `.carousel-caption`

```html
<div id="myCarousel" class="carousel slide" data-bs-ride="carousel">
  <div class="carousel-indicators">
    <button type="button" data-bs-target="#myCarousel" data-bs-slide-to="0" class="active"></button>
    <button type="button" data-bs-target="#myCarousel" data-bs-slide-to="1"></button>
  </div>
  <div class="carousel-inner">
    <div class="carousel-item active">
      <img src="..." class="d-block w-100" alt="...">
      <div class="carousel-caption d-none d-md-block">
        <h5>Slide Title</h5><p>Description</p>
      </div>
    </div>
    <div class="carousel-item" data-bs-interval="2000">
      <img src="..." class="d-block w-100" alt="...">
    </div>
  </div>
  <button class="carousel-control-prev" type="button" data-bs-target="#myCarousel" data-bs-slide="prev">
    <span class="carousel-control-prev-icon" aria-hidden="true"></span>
    <span class="visually-hidden">Previous</span>
  </button>
  <button class="carousel-control-next" type="button" data-bs-target="#myCarousel" data-bs-slide="next">
    <span class="carousel-control-next-icon" aria-hidden="true"></span>
    <span class="visually-hidden">Next</span>
  </button>
</div>
```

**Data attrs:** `data-bs-ride="carousel|true"`, `data-bs-interval="5000"`, `data-bs-touch="true|false"`, `data-bs-wrap="true|false"`, `data-bs-pause="hover|false"`
**Variations:** `.carousel-fade` for crossfade, per-item `data-bs-interval`
**JS:** `.cycle()`, `.pause()`, `.next()`, `.prev()`, `.to(index)`
**Events:** `slide.bs.carousel`, `slid.bs.carousel` (with `direction`, `from`, `to`)

---

### 2.9 Close Button

**Classes:** `.btn-close`

```html
<button type="button" class="btn-close" aria-label="Close"></button>
<button type="button" class="btn-close" disabled aria-label="Close"></button>

<!-- Dark variant -->
<div data-bs-theme="dark">
  <button type="button" class="btn-close" aria-label="Close"></button>
</div>
```

---

### 2.10 Collapse

**Classes:** `.collapse`, `.collapse.show`, `.collapsing`, `.collapse-horizontal`

```html
<button class="btn btn-primary" type="button" data-bs-toggle="collapse"
        data-bs-target="#collapseExample" aria-expanded="false" aria-controls="collapseExample">
  Toggle
</button>
<div class="collapse" id="collapseExample">
  <div class="card card-body">Collapsed content here.</div>
</div>
```

**Horizontal collapse:** Add `.collapse-horizontal` (animates width instead of height)
**Multiple targets:** `data-bs-target=".multi-collapse"` with class on targets
**JS Options:** `parent` (selector), `toggle` (boolean)
**JS Methods:** `.show()`, `.hide()`, `.toggle()`, `.dispose()`
**Events:** `show.bs.collapse`, `shown.bs.collapse`, `hide.bs.collapse`, `hidden.bs.collapse`

---

### 2.11 Dropdowns

**Containers:** `.dropdown`, `.dropup`, `.dropstart`, `.dropend`, `.dropdown-center`, `.dropup-center`
**Toggle:** `.dropdown-toggle`, `.dropdown-toggle-split`
**Menu:** `.dropdown-menu`, `.dropdown-menu-end`, `.dropdown-menu-{sm|md|lg|xl|xxl}-{start|end}`
**Items:** `.dropdown-item`, `.dropdown-item-text`, `.dropdown-header`, `.dropdown-divider`
**States:** `.active`, `.disabled`

```html
<div class="dropdown">
  <button class="btn btn-secondary dropdown-toggle" type="button"
          data-bs-toggle="dropdown" aria-expanded="false">
    Dropdown
  </button>
  <ul class="dropdown-menu">
    <li><h6 class="dropdown-header">Header</h6></li>
    <li><a class="dropdown-item active" href="#" aria-current="true">Active</a></li>
    <li><a class="dropdown-item" href="#">Action</a></li>
    <li><a class="dropdown-item disabled" aria-disabled="true">Disabled</a></li>
    <li><hr class="dropdown-divider"></li>
    <li><a class="dropdown-item" href="#">Separated</a></li>
  </ul>
</div>

<!-- Split button -->
<div class="btn-group">
  <button type="button" class="btn btn-danger">Action</button>
  <button type="button" class="btn btn-danger dropdown-toggle dropdown-toggle-split"
          data-bs-toggle="dropdown" aria-expanded="false">
    <span class="visually-hidden">Toggle Dropdown</span>
  </button>
  <ul class="dropdown-menu">...</ul>
</div>
```

**Auto close:** `data-bs-auto-close="true|inside|outside|false"`
**Dark mode:** `data-bs-theme="dark"` on parent
**JS Options:** `autoClose`, `boundary`, `display`, `offset`, `popperConfig`, `reference`
**Events:** `show.bs.dropdown`, `shown.bs.dropdown`, `hide.bs.dropdown`, `hidden.bs.dropdown`

---

### 2.12 List Group

**Classes:** `.list-group`, `.list-group-item`, `.list-group-item-action`, `.list-group-flush`, `.list-group-numbered`
**Horizontal:** `.list-group-horizontal`, `.list-group-horizontal-{sm|md|lg|xl|xxl}`
**Colors:** `.list-group-item-{primary|secondary|success|danger|warning|info|light|dark}`
**States:** `.active` (with `aria-current="true"`), `.disabled` (with `aria-disabled="true"`)

```html
<ul class="list-group">
  <li class="list-group-item active" aria-current="true">Active item</li>
  <li class="list-group-item">An item</li>
  <li class="list-group-item disabled" aria-disabled="true">Disabled</li>
</ul>

<!-- Actionable -->
<div class="list-group">
  <a href="#" class="list-group-item list-group-item-action active" aria-current="true">Active</a>
  <button type="button" class="list-group-item list-group-item-action">Button item</button>
</div>

<!-- With badges -->
<ul class="list-group">
  <li class="list-group-item d-flex justify-content-between align-items-center">
    Item <span class="badge text-bg-primary rounded-pill">14</span>
  </li>
</ul>

<!-- Tab behavior -->
<div class="list-group" role="tablist">
  <a class="list-group-item list-group-item-action active" data-bs-toggle="list"
     href="#home" role="tab">Home</a>
</div>
```

---

### 2.13 Modal

**Classes:** `.modal`, `.modal-dialog`, `.modal-content`, `.modal-header`, `.modal-title`, `.modal-body`, `.modal-footer`, `.modal-backdrop`
**Sizes:** `.modal-sm` (300px), default (500px), `.modal-lg` (800px), `.modal-xl` (1140px)
**Layout:** `.modal-dialog-centered`, `.modal-dialog-scrollable`
**Fullscreen:** `.modal-fullscreen`, `.modal-fullscreen-{sm|md|lg|xl|xxl}-down`
**Animation:** `.fade`

```html
<button type="button" class="btn btn-primary" data-bs-toggle="modal" data-bs-target="#myModal">
  Open Modal
</button>

<div class="modal fade" id="myModal" tabindex="-1" aria-labelledby="myModalLabel" aria-hidden="true">
  <div class="modal-dialog modal-lg modal-dialog-centered">
    <div class="modal-content">
      <div class="modal-header">
        <h1 class="modal-title fs-5" id="myModalLabel">Modal title</h1>
        <button type="button" class="btn-close" data-bs-dismiss="modal" aria-label="Close"></button>
      </div>
      <div class="modal-body">Content here.</div>
      <div class="modal-footer">
        <button type="button" class="btn btn-secondary" data-bs-dismiss="modal">Close</button>
        <button type="button" class="btn btn-primary">Save</button>
      </div>
    </div>
  </div>
</div>
```

**Static backdrop:** `data-bs-backdrop="static"` `data-bs-keyboard="false"`
**JS Options:** `backdrop` (true|false|'static'), `focus` (boolean), `keyboard` (boolean)
**JS Methods:** `.show()`, `.hide()`, `.toggle()`, `.handleUpdate()`, `.dispose()`
**Events:** `show.bs.modal`, `shown.bs.modal`, `hide.bs.modal`, `hidden.bs.modal`, `hidePrevented.bs.modal`

---

### 2.14 Navbar

**Classes:** `.navbar`, `.navbar-expand-{sm|md|lg|xl|xxl}`, `.navbar-brand`, `.navbar-nav`, `.nav-item`, `.nav-link`, `.navbar-toggler`, `.navbar-toggler-icon`, `.navbar-collapse`, `.navbar-text`, `.navbar-nav-scroll`

```html
<nav class="navbar navbar-expand-lg bg-body-tertiary">
  <div class="container-fluid">
    <a class="navbar-brand" href="#">Brand</a>
    <button class="navbar-toggler" type="button" data-bs-toggle="collapse"
            data-bs-target="#navbarNav" aria-controls="navbarNav"
            aria-expanded="false" aria-label="Toggle navigation">
      <span class="navbar-toggler-icon"></span>
    </button>
    <div class="collapse navbar-collapse" id="navbarNav">
      <ul class="navbar-nav me-auto mb-2 mb-lg-0">
        <li class="nav-item">
          <a class="nav-link active" aria-current="page" href="#">Home</a>
        </li>
        <li class="nav-item dropdown">
          <a class="nav-link dropdown-toggle" href="#" data-bs-toggle="dropdown">Dropdown</a>
          <ul class="dropdown-menu">
            <li><a class="dropdown-item" href="#">Action</a></li>
          </ul>
        </li>
      </ul>
      <form class="d-flex" role="search">
        <input class="form-control me-2" type="search" placeholder="Search">
        <button class="btn btn-outline-success" type="submit">Search</button>
      </form>
    </div>
  </div>
</nav>
```

**Placement:** default (static), `.fixed-top`, `.fixed-bottom`, `.sticky-top`, `.sticky-bottom`
**Color schemes:** `data-bs-theme="dark"` with `.bg-dark`, `.bg-primary`, etc.
**Offcanvas navbar:** Use `data-bs-toggle="offcanvas"` instead of `collapse`
**Scrolling:** `.navbar-nav-scroll` with `style="--bs-scroll-height: 100px;"`

---

### 2.15 Navs & Tabs

**Classes:** `.nav`, `.nav-item`, `.nav-link`, `.nav-tabs`, `.nav-pills`, `.nav-underline` (v5.3.0+), `.nav-fill`, `.nav-justified`
**Tab content:** `.tab-content`, `.tab-pane`, `.fade`, `.show`

```html
<!-- Tabs -->
<ul class="nav nav-tabs" id="myTab" role="tablist">
  <li class="nav-item" role="presentation">
    <button class="nav-link active" id="home-tab" data-bs-toggle="tab"
            data-bs-target="#home" type="button" role="tab"
            aria-controls="home" aria-selected="true">Home</button>
  </li>
  <li class="nav-item" role="presentation">
    <button class="nav-link" id="profile-tab" data-bs-toggle="tab"
            data-bs-target="#profile" type="button" role="tab"
            aria-controls="profile" aria-selected="false">Profile</button>
  </li>
</ul>
<div class="tab-content" id="myTabContent">
  <div class="tab-pane fade show active" id="home" role="tabpanel"
       aria-labelledby="home-tab" tabindex="0">Home content</div>
  <div class="tab-pane fade" id="profile" role="tabpanel"
       aria-labelledby="profile-tab" tabindex="0">Profile content</div>
</div>

<!-- Pills -->
<ul class="nav nav-pills">...</ul>

<!-- Underline (new in 5.3) -->
<ul class="nav nav-underline">...</ul>

<!-- Vertical pills -->
<div class="d-flex">
  <div class="nav flex-column nav-pills me-3" role="tablist" aria-orientation="vertical">...</div>
  <div class="tab-content">...</div>
</div>
```

**Layout:** `.flex-column` (vertical), `.justify-content-center`, `.justify-content-end`, `.nav-fill`, `.nav-justified`
**JS Events:** `show.bs.tab`, `shown.bs.tab`, `hide.bs.tab`, `hidden.bs.tab`

---

### 2.16 Offcanvas

**Classes:** `.offcanvas`, `.offcanvas-header`, `.offcanvas-title`, `.offcanvas-body`
**Placement:** `.offcanvas-start` (left), `.offcanvas-end` (right), `.offcanvas-top`, `.offcanvas-bottom`
**Responsive:** `.offcanvas-{sm|md|lg|xl|xxl}` (hidden below breakpoint)

```html
<button class="btn btn-primary" type="button" data-bs-toggle="offcanvas"
        data-bs-target="#myOffcanvas" aria-controls="myOffcanvas">
  Open Offcanvas
</button>

<div class="offcanvas offcanvas-start" tabindex="-1" id="myOffcanvas"
     aria-labelledby="myOffcanvasLabel">
  <div class="offcanvas-header">
    <h5 class="offcanvas-title" id="myOffcanvasLabel">Offcanvas</h5>
    <button type="button" class="btn-close" data-bs-dismiss="offcanvas" aria-label="Close"></button>
  </div>
  <div class="offcanvas-body">Content here.</div>
</div>
```

**Options:** `backdrop` (true|false|'static'), `keyboard` (boolean), `scroll` (boolean)
**Data attrs:** `data-bs-scroll="true"`, `data-bs-backdrop="false|static"`
**Events:** `show.bs.offcanvas`, `shown.bs.offcanvas`, `hide.bs.offcanvas`, `hidden.bs.offcanvas`, `hidePrevented.bs.offcanvas`

---

### 2.17 Pagination

**Classes:** `.pagination`, `.page-item`, `.page-link`, `.pagination-lg`, `.pagination-sm`
**States:** `.active` (with `aria-current="page"`), `.disabled`

```html
<nav aria-label="Page navigation">
  <ul class="pagination justify-content-center">
    <li class="page-item disabled"><span class="page-link">Previous</span></li>
    <li class="page-item"><a class="page-link" href="#">1</a></li>
    <li class="page-item active" aria-current="page"><a class="page-link" href="#">2</a></li>
    <li class="page-item"><a class="page-link" href="#">3</a></li>
    <li class="page-item"><a class="page-link" href="#">Next</a></li>
  </ul>
</nav>
```

---

### 2.18 Placeholders

**Classes:** `.placeholder`, `.placeholder-glow`, `.placeholder-wave`, `.placeholder-lg`, `.placeholder-sm`, `.placeholder-xs`

```html
<p class="placeholder-glow">
  <span class="placeholder col-6"></span>
  <span class="placeholder col-8 bg-primary"></span>
</p>
<p class="placeholder-wave">
  <span class="placeholder col-12"></span>
</p>

<!-- Placeholder button -->
<a class="btn btn-primary disabled placeholder col-6" aria-disabled="true"></a>
```

**Width:** Grid columns (`.col-{1-12}`), utilities (`.w-75`), or inline styles
**Colors:** `.bg-{primary|secondary|success|danger|warning|info|light|dark}`

---

### 2.19 Popovers

**Classes:** `.popover`, `.popover-arrow`, `.popover-header`, `.popover-body`

```html
<button type="button" class="btn btn-lg btn-danger" data-bs-toggle="popover"
        data-bs-title="Popover title" data-bs-content="Popover body content.">
  Click to toggle popover
</button>

<script>
// Must initialize manually
const popoverTriggerList = document.querySelectorAll('[data-bs-toggle="popover"]')
const popoverList = [...popoverTriggerList].map(el => new bootstrap.Popover(el))
</script>
```

**Data attrs:** `data-bs-placement="top|right|bottom|left"`, `data-bs-trigger="click|hover|focus|manual"`, `data-bs-custom-class`, `data-bs-html="true"`, `data-bs-content`, `data-bs-title`
**Requires:** Popper.js (included in bootstrap.bundle.min.js)
**JS Methods:** `.show()`, `.hide()`, `.toggle()`, `.enable()`, `.disable()`, `.dispose()`, `.update()`, `.setContent()`

---

### 2.20 Progress

**Classes:** `.progress`, `.progress-bar`, `.progress-stacked`, `.progress-bar-striped`, `.progress-bar-animated`

```html
<div class="progress" role="progressbar" aria-label="Example" aria-valuenow="75" aria-valuemin="0" aria-valuemax="100">
  <div class="progress-bar bg-success" style="width: 75%">75%</div>
</div>

<!-- Striped animated -->
<div class="progress" role="progressbar" aria-valuenow="75" aria-valuemin="0" aria-valuemax="100">
  <div class="progress-bar progress-bar-striped progress-bar-animated" style="width: 75%"></div>
</div>

<!-- Stacked -->
<div class="progress-stacked">
  <div class="progress" role="progressbar" style="width: 15%"><div class="progress-bar"></div></div>
  <div class="progress" role="progressbar" style="width: 30%"><div class="progress-bar bg-success"></div></div>
  <div class="progress" role="progressbar" style="width: 20%"><div class="progress-bar bg-info"></div></div>
</div>
```

**Colors:** `.bg-{success|info|warning|danger}` on `.progress-bar`

---

### 2.21 Scrollspy

```html
<nav id="navbar-example" class="navbar bg-body-tertiary">
  <ul class="nav nav-pills">
    <li class="nav-item"><a class="nav-link" href="#section1">Section 1</a></li>
    <li class="nav-item"><a class="nav-link" href="#section2">Section 2</a></li>
  </ul>
</nav>
<div data-bs-spy="scroll" data-bs-target="#navbar-example" data-bs-root-margin="0px 0px -40%"
     data-bs-smooth-scroll="true" tabindex="0">
  <div id="section1">...</div>
  <div id="section2">...</div>
</div>
```

**Data attrs:** `data-bs-spy="scroll"`, `data-bs-target`, `data-bs-root-margin`, `data-bs-smooth-scroll`
**JS Methods:** `.refresh()`, `.dispose()`
**Event:** `activate.bs.scrollspy`

---

### 2.22 Spinners

**Classes:** `.spinner-border`, `.spinner-grow`, `.spinner-border-sm`, `.spinner-grow-sm`
**Colors:** Use `.text-{primary|secondary|success|danger|warning|info|light|dark}`

```html
<div class="spinner-border text-primary" role="status">
  <span class="visually-hidden">Loading...</span>
</div>
<div class="spinner-grow text-success" role="status">
  <span class="visually-hidden">Loading...</span>
</div>

<!-- In button -->
<button class="btn btn-primary" type="button" disabled>
  <span class="spinner-border spinner-border-sm" aria-hidden="true"></span>
  <span role="status">Loading...</span>
</button>
```

---

### 2.23 Toasts

**Classes:** `.toast`, `.toast-container`, `.toast-header`, `.toast-body`

```html
<div class="toast-container position-fixed bottom-0 end-0 p-3">
  <div class="toast" role="alert" aria-live="assertive" aria-atomic="true">
    <div class="toast-header">
      <strong class="me-auto">Bootstrap</strong>
      <small>11 mins ago</small>
      <button type="button" class="btn-close" data-bs-dismiss="toast" aria-label="Close"></button>
    </div>
    <div class="toast-body">Hello, world!</div>
  </div>
</div>

<!-- Colored toast -->
<div class="toast align-items-center text-bg-primary border-0" role="alert">
  <div class="d-flex">
    <div class="toast-body">Hello, world!</div>
    <button type="button" class="btn-close btn-close-white me-2 m-auto" data-bs-dismiss="toast"></button>
  </div>
</div>
```

**Placement positions:** `.toast-container` with position utilities: `top-0 start-0`, `top-0 end-0`, `top-0 start-50 translate-middle-x`, `bottom-0 end-0`, etc.
**Options:** `animation` (boolean), `autohide` (boolean, default true), `delay` (5000ms default)
**JS Methods:** `.show()`, `.hide()`, `.isShown()`, `.dispose()`
**Events:** `show.bs.toast`, `shown.bs.toast`, `hide.bs.toast`, `hidden.bs.toast`

---

### 2.24 Tooltips

**Classes:** `.tooltip`, `.tooltip-arrow`, `.tooltip-inner`

```html
<button type="button" class="btn btn-secondary" data-bs-toggle="tooltip"
        data-bs-placement="top" data-bs-title="Tooltip text">
  Hover me
</button>

<script>
// Must initialize manually
const tooltipTriggerList = document.querySelectorAll('[data-bs-toggle="tooltip"]')
const tooltipList = [...tooltipTriggerList].map(el => new bootstrap.Tooltip(el))
</script>
```

**Data attrs:** `data-bs-placement="top|right|bottom|left"`, `data-bs-title`, `data-bs-html="true"`, `data-bs-trigger="hover focus|click|manual"`, `data-bs-custom-class`, `data-bs-delay`
**Requires:** Popper.js (included in bootstrap.bundle.min.js)
**Disabled elements:** Must wrap in `<span class="d-inline-block" tabindex="0">`
**JS Methods:** `.show()`, `.hide()`, `.toggle()`, `.enable()`, `.disable()`, `.dispose()`, `.update()`, `.setContent()`

---

## 3. FORMS

### Form Controls

```
.form-label          - Label styling
.form-control        - Text inputs, textareas
.form-control-lg     - Large input
.form-control-sm     - Small input
.form-control-plaintext - Readonly plain text
.form-control-color  - Color picker
.form-text           - Helper text
```

### Select

```
.form-select         - Custom select
.form-select-lg      - Large select
.form-select-sm      - Small select
```

### Checks & Radios

```
.form-check          - Wrapper
.form-check-input    - Checkbox/radio input
.form-check-label    - Label
.form-check-inline   - Inline layout
.form-switch         - Toggle switch style (add to .form-check)
```

### Range

```
.form-range          - Range slider
```

### Input Group

```
.input-group         - Wrapper
.input-group-text    - Text addon
.input-group-lg      - Large
.input-group-sm      - Small
```

### Floating Labels

```
.form-floating       - Wrapper (input must come before label)
```

```html
<div class="form-floating mb-3">
  <input type="email" class="form-control" id="floatingInput" placeholder="name@example.com">
  <label for="floatingInput">Email address</label>
</div>
```

### Validation

```
.was-validated       - On form, triggers validation styles
.is-valid            - On input, shows valid state
.is-invalid          - On input, shows invalid state
.valid-feedback      - Green success message
.invalid-feedback    - Red error message
.valid-tooltip       - Positioned valid message
.invalid-tooltip     - Positioned invalid message
```

---

## 4. ALL UTILITY CLASSES

### 4.1 Spacing

**Format:** `{m|p}{t|b|s|e|x|y}-{0|1|2|3|4|5|auto}`
**Responsive:** `{m|p}{t|b|s|e|x|y}-{sm|md|lg|xl|xxl}-{0|1|2|3|4|5|auto}`

| Size | Value |
|------|-------|
| 0 | 0 |
| 1 | 0.25rem |
| 2 | 0.5rem |
| 3 | 1rem |
| 4 | 1.5rem |
| 5 | 3rem |
| auto | auto (margin only) |

**Sides:** `t` (top), `b` (bottom), `s` (start/left), `e` (end/right), `x` (horizontal), `y` (vertical), blank (all)
**Negative margins:** `.m{side}-n{1-5}` (requires `$enable-negative-margins: true`)

**Gap (flexbox/grid):**
```
.gap-{0-5}          - All directions
.row-gap-{0-5}      - Vertical gap
.column-gap-{0-5}   - Horizontal gap
```

---

### 4.2 Colors

**Text colors:**
```
.text-{primary|secondary|success|danger|warning|info|light|dark}
.text-{primary|secondary|success|danger|warning|info|light|dark}-emphasis
.text-body, .text-body-emphasis, .text-body-secondary, .text-body-tertiary
.text-black, .text-white
.text-opacity-{25|50|75|100}
```

**Background colors:**
```
.bg-{primary|secondary|success|danger|warning|info|light|dark}
.bg-{primary|secondary|success|danger|warning|info|light|dark}-subtle
.bg-body, .bg-body-secondary, .bg-body-tertiary
.bg-black, .bg-white, .bg-transparent
.bg-gradient                    - Add gradient overlay
.bg-opacity-{10|25|50|75|100}
```

**Combined text+bg helpers:**
```
.text-bg-{primary|secondary|success|danger|warning|info|light|dark}
```

---

### 4.3 Display

```
.d-{none|inline|inline-block|block|grid|inline-grid|table|table-row|table-cell|flex|inline-flex}
.d-{sm|md|lg|xl|xxl}-{none|inline|inline-block|block|grid|inline-grid|table|table-row|table-cell|flex|inline-flex}
.d-print-{none|inline|inline-block|block|grid|inline-grid|table|table-row|table-cell|flex|inline-flex}
```

**Common patterns:**
- Hide on mobile, show on desktop: `.d-none .d-md-block`
- Show on mobile, hide on desktop: `.d-block .d-md-none`

---

### 4.4 Flex

```
.d-flex, .d-inline-flex
.flex-{row|row-reverse|column|column-reverse}
.flex-{sm|md|lg|xl|xxl}-{row|row-reverse|column|column-reverse}
.flex-{wrap|nowrap|wrap-reverse}
.flex-{sm|md|lg|xl|xxl}-{wrap|nowrap|wrap-reverse}
.justify-content-{start|end|center|between|around|evenly}
.justify-content-{sm|md|lg|xl|xxl}-{start|end|center|between|around|evenly}
.align-items-{start|end|center|baseline|stretch}
.align-items-{sm|md|lg|xl|xxl}-{start|end|center|baseline|stretch}
.align-self-{start|end|center|baseline|stretch}
.align-self-{sm|md|lg|xl|xxl}-{start|end|center|baseline|stretch}
.align-content-{start|end|center|between|around|stretch}
.align-content-{sm|md|lg|xl|xxl}-{start|end|center|between|around|stretch}
.flex-fill, .flex-{sm|md|lg|xl|xxl}-fill
.flex-{grow|shrink}-{0|1}
.flex-{sm|md|lg|xl|xxl}-{grow|shrink}-{0|1}
.order-{0|1|2|3|4|5|first|last}
.order-{sm|md|lg|xl|xxl}-{0|1|2|3|4|5|first|last}
```

---

### 4.5 Float

```
.float-{start|end|none}
.float-{sm|md|lg|xl|xxl}-{start|end|none}
```

---

### 4.6 Interactions

```
.user-select-all, .user-select-auto, .user-select-none
.pe-none, .pe-auto   (pointer-events)
```

---

### 4.7 Opacity

```
.opacity-{0|25|50|75|100}
```

---

### 4.8 Overflow

```
.overflow-{auto|hidden|visible|scroll}
.overflow-x-{auto|hidden|visible|scroll}
.overflow-y-{auto|hidden|visible|scroll}
```

---

### 4.9 Position

```
.position-{static|relative|absolute|fixed|sticky}
.top-{0|50|100}, .bottom-{0|50|100}
.start-{0|50|100}, .end-{0|50|100}
.translate-middle, .translate-middle-x, .translate-middle-y
```

**Common pattern (absolute center):** `.position-absolute .top-50 .start-50 .translate-middle`

---

### 4.10 Shadows

```
.shadow-none, .shadow-sm, .shadow, .shadow-lg
```

---

### 4.11 Sizing

```
.w-{25|50|75|100|auto}
.h-{25|50|75|100|auto}
.mw-100, .mh-100
.vw-100, .vh-100
.min-vw-100, .min-vh-100
```

---

### 4.12 Text

```
.text-{start|center|end}
.text-{sm|md|lg|xl|xxl}-{start|center|end}
.text-wrap, .text-nowrap, .text-break
.text-{lowercase|uppercase|capitalize}
.fs-{1|2|3|4|5|6}         (font sizes matching h1-h6)
.fw-{lighter|light|normal|medium|semibold|bold|bolder}
.fst-{italic|normal}
.lh-{1|sm|base|lg}
.font-monospace
.text-decoration-{underline|line-through|none}
.text-reset               (inherit color from parent)
```

---

### 4.13 Vertical Align

```
.align-{baseline|top|middle|bottom|text-top|text-bottom}
```

---

### 4.14 Visibility

```
.visible, .invisible
```

---

### 4.15 Z-Index

```
.z-n1, .z-0, .z-1, .z-2, .z-3
```

---

### 4.16 Borders

```
.border, .border-top, .border-end, .border-bottom, .border-start
.border-0, .border-top-0, .border-end-0, .border-bottom-0, .border-start-0
.border-{primary|secondary|success|danger|warning|info|light|dark|black|white}
.border-{primary|secondary|success|danger|warning|info|light|dark}-subtle
.border-opacity-{10|25|50|75|100}
.border-{1|2|3|4|5}
.rounded, .rounded-{0|1|2|3|4|5|circle|pill}
.rounded-{top|end|bottom|start}, .rounded-{top|end|bottom|start}-{0|1|2|3|4|5|circle|pill}
```

---

## 5. HELPERS

```
.visually-hidden, .visually-hidden-focusable
.stretched-link           - Makes containing block clickable
.text-truncate            - Truncate with ellipsis
.vstack                   - Vertical stack (flex-column + gap)
.hstack                   - Horizontal stack (flex-row + gap)
.vr                       - Vertical rule/divider
.clearfix                 - Clear floats
.ratio, .ratio-{1x1|4x3|16x9|21x9}  - Aspect ratios
.text-bg-{primary|secondary|success|danger|warning|info|light|dark}
.img-fluid                - Responsive image (max-width: 100%; height: auto)
.img-thumbnail            - Image with border
.object-fit-{contain|cover|fill|scale|none}
.object-fit-{sm|md|lg|xl|xxl}-{contain|cover|fill|scale|none}
```

---

## 6. COLOR MODES (Dark Mode) - New in v5.3

### Setting Color Mode

```html
<!-- Global (on <html> element) -->
<html lang="en" data-bs-theme="dark">

<!-- Per-component -->
<div data-bs-theme="dark">
  <div class="card">Dark card</div>
</div>
<div data-bs-theme="light">
  <div class="card">Light card</div>
</div>
```

### JavaScript Theme Toggler

```javascript
const getStoredTheme = () => localStorage.getItem('theme')
const setStoredTheme = theme => localStorage.setItem('theme', theme)

const getPreferredTheme = () => {
  const storedTheme = getStoredTheme()
  if (storedTheme) return storedTheme
  return window.matchMedia('(prefers-color-scheme: dark)').matches ? 'dark' : 'light'
}

const setTheme = theme => {
  if (theme === 'auto') {
    document.documentElement.setAttribute('data-bs-theme',
      window.matchMedia('(prefers-color-scheme: dark)').matches ? 'dark' : 'light')
  } else {
    document.documentElement.setAttribute('data-bs-theme', theme)
  }
}

// Apply on load
setTheme(getPreferredTheme())

// Listen for system preference changes
window.matchMedia('(prefers-color-scheme: dark)').addEventListener('change', () => {
  const storedTheme = getStoredTheme()
  if (storedTheme !== 'light' && storedTheme !== 'dark') {
    setTheme(getPreferredTheme())
  }
})
```

### Sass Configuration

```scss
$enable-dark-mode: true;       // Enable/disable dark mode (default: true)
$color-mode-type: data;        // "data" (data-bs-theme) or "media-query" (prefers-color-scheme)
```

### Color-Mode-Aware Classes

These classes automatically adapt to the active color mode:
```
.text-body, .text-body-emphasis, .text-body-secondary, .text-body-tertiary
.bg-body, .bg-body-secondary, .bg-body-tertiary
.border-{color}-subtle     - Subtle borders that adapt
.bg-{color}-subtle         - Subtle backgrounds that adapt
.text-{color}-emphasis     - Emphasis text that adapts
```

---

## 7. CSS VARIABLES SYSTEM

### Root-Level Variables

Bootstrap sets CSS custom properties on `:root` that adapt to color modes:

```css
:root, [data-bs-theme="light"] {
  --bs-blue: #0d6efd;
  --bs-indigo: #6610f2;
  --bs-purple: #6f42c1;
  --bs-pink: #d63384;
  --bs-red: #dc3545;
  --bs-orange: #fd7e14;
  --bs-yellow: #ffc107;
  --bs-green: #198754;
  --bs-teal: #20c997;
  --bs-cyan: #0dcaf0;

  --bs-primary: #0d6efd;
  --bs-secondary: #6c757d;
  --bs-success: #198754;
  --bs-info: #0dcaf0;
  --bs-warning: #ffc107;
  --bs-danger: #dc3545;
  --bs-light: #f8f9fa;
  --bs-dark: #212529;

  --bs-primary-rgb: 13, 110, 253;
  --bs-body-color: #212529;
  --bs-body-bg: #fff;
  --bs-body-color-rgb: 33, 37, 41;
  --bs-body-bg-rgb: 255, 255, 255;

  --bs-emphasis-color: #000;
  --bs-secondary-color: rgba(33, 37, 41, 0.75);
  --bs-secondary-bg: #e9ecef;
  --bs-tertiary-color: rgba(33, 37, 41, 0.5);
  --bs-tertiary-bg: #f8f9fa;

  --bs-link-color: #0d6efd;
  --bs-link-hover-color: #0a58ca;
  --bs-border-color: #dee2e6;
  --bs-border-width: 1px;
  --bs-border-radius: 0.375rem;
  --bs-border-radius-sm: 0.25rem;
  --bs-border-radius-lg: 0.5rem;
  --bs-border-radius-xl: 1rem;
  --bs-border-radius-xxl: 2rem;
  --bs-border-radius-pill: 50rem;

  --bs-font-sans-serif: system-ui, -apple-system, "Segoe UI", Roboto, "Helvetica Neue", ...;
  --bs-font-monospace: SFMono-Regular, Menlo, Monaco, Consolas, ...;
  --bs-body-font-family: var(--bs-font-sans-serif);
  --bs-body-font-size: 1rem;
  --bs-body-font-weight: 400;
  --bs-body-line-height: 1.5;
}
```

### Component-Level CSS Variables

Every component defines local CSS variables for customization:

```html
<!-- Override component variables inline -->
<button class="btn btn-primary"
        style="--bs-btn-padding-y: .25rem; --bs-btn-padding-x: .5rem; --bs-btn-font-size: .75rem;">
  Custom Button
</button>

<div class="alert alert-primary"
     style="--bs-alert-bg: transparent; --bs-alert-border-color: purple;">
  Custom Alert
</div>
```

---

## 8. UTILITIES API (Sass)

### Utility Map Structure

```scss
$utilities: (
  "utility-name": (
    property: css-property,       // Required: CSS property or array of properties
    values: (...),                // Required: list or map of values
    class: class-prefix,          // Optional: custom class prefix (null = value only)
    css-var: false,               // Optional: generate CSS variables instead
    css-variable-name: null,      // Optional: custom CSS variable name
    local-vars: (),               // Optional: local CSS vars in ruleset
    state: null,                  // Optional: pseudo-class variants (hover, focus)
    responsive: false,            // Optional: generate responsive variants
    rfs: false,                   // Optional: fluid rescaling
    print: false,                 // Optional: generate print classes
    rtl: true,                    // Optional: include in RTL output
  )
);
```

### Customizing Utilities

```scss
@import "bootstrap/scss/functions";
@import "bootstrap/scss/variables";
@import "bootstrap/scss/variables-dark";
@import "bootstrap/scss/maps";
@import "bootstrap/scss/mixins";
@import "bootstrap/scss/utilities";

// Add new utility
$utilities: map-merge($utilities, (
  "cursor": (
    property: cursor,
    class: cursor,
    responsive: true,
    values: auto pointer grab,
  )
));

// Remove utility
$utilities: map-merge($utilities, ("width": null));

// Modify existing (add responsive)
$utilities: map-merge($utilities, (
  "border": map-merge(map-get($utilities, "border"), (responsive: true)),
));

@import "bootstrap/scss/utilities/api";  // Must be last
```

---

## 9. FEATURES INTRODUCED IN 5.3.x

### v5.3.0 (Major)
- **Color modes system** with `data-bs-theme` attribute (light/dark/custom)
- **Dark mode** support built into all components
- **New `.nav-underline` variant** for nav/tab components
- **Custom color modes** support (beyond light/dark)
- Per-component theme overrides
- Color-mode-aware utility classes (`-subtle`, `-emphasis`)
- `.text-bg-*` helper classes for combined text+background
- Dark mode Sass variables in `_variables-dark.scss`
- `color-mode()` Sass mixin
- Deprecated: `.navbar-light` (use `data-bs-theme="light"`), `.navbar-dark` rewritten
- Deprecated: `.carousel-dark` (use `data-bs-theme="dark"`)
- Deprecated: `alert-variant()` mixin, `list-group-item-variant()` mixin

### v5.3.1
- Increased dark mode color contrast (gray-500 to gray-300)
- Improved disabled nav-link styling
- Home/End keyboard navigation for tabs

### v5.3.2
- Fixed multiple collapse target IDs
- Improved table state rendering in dark mode
- Increased form range track contrast

### v5.3.3 - v5.3.8
- Bug fixes, documentation improvements
- Security patches
- Maintenance releases

---

## 10. BEST PRACTICES & COMMON PATTERNS

### Responsive Design

```html
<!-- Mobile-first: stack on mobile, side by side on desktop -->
<div class="row">
  <div class="col-12 col-md-6 col-lg-4">Column</div>
  <div class="col-12 col-md-6 col-lg-4">Column</div>
  <div class="col-12 col-md-12 col-lg-4">Column</div>
</div>

<!-- Show/hide by breakpoint -->
<div class="d-none d-md-block">Visible on md and up</div>
<div class="d-block d-md-none">Visible only on mobile</div>
```

### Dark Mode Support

```html
<!-- Always add data-bs-theme to <html> -->
<html lang="en" data-bs-theme="light">

<!-- Use color-mode-aware classes -->
<div class="bg-body text-body">Adapts to color mode</div>
<div class="bg-body-secondary">Secondary background adapts</div>
<div class="text-body-emphasis">Emphasis text adapts</div>
<div class="border-primary-subtle">Subtle border adapts</div>
```

### Accessible Patterns

```html
<!-- Always use aria attributes -->
<button aria-expanded="false" aria-controls="target">Toggle</button>
<nav aria-label="Main navigation">...</nav>
<div role="alert" aria-live="assertive">...</div>

<!-- Screen reader only text -->
<span class="visually-hidden">Description for screen readers</span>

<!-- Skip navigation link -->
<a class="visually-hidden-focusable" href="#main">Skip to main content</a>
```

### Common Page Layout

```html
<body>
  <nav class="navbar navbar-expand-lg bg-body-tertiary sticky-top">
    <div class="container">...</div>
  </nav>

  <main class="container py-4">
    <div class="row">
      <div class="col-lg-8">
        <!-- Main content -->
      </div>
      <div class="col-lg-4">
        <!-- Sidebar -->
      </div>
    </div>
  </main>

  <footer class="bg-body-tertiary mt-auto py-3">
    <div class="container text-center text-body-secondary">
      <p>&copy; 2026 Company</p>
    </div>
  </footer>
</body>
```

### JavaScript Initialization Pattern

```javascript
// Initialize all tooltips
const tooltipTriggerList = document.querySelectorAll('[data-bs-toggle="tooltip"]')
const tooltipList = [...tooltipTriggerList].map(el => new bootstrap.Tooltip(el))

// Initialize all popovers
const popoverTriggerList = document.querySelectorAll('[data-bs-toggle="popover"]')
const popoverList = [...popoverTriggerList].map(el => new bootstrap.Popover(el))

// Initialize all toasts
const toastElList = document.querySelectorAll('.toast')
const toastList = [...toastElList].map(el => new bootstrap.Toast(el))
```

### Common Component Patterns

```html
<!-- Card with image, body, and footer -->
<div class="card h-100 shadow-sm">
  <img src="..." class="card-img-top" alt="...">
  <div class="card-body">
    <h5 class="card-title">Title</h5>
    <p class="card-text text-body-secondary">Description</p>
  </div>
  <div class="card-footer bg-transparent border-top-0">
    <a href="#" class="btn btn-primary">Action</a>
  </div>
</div>

<!-- Hero section -->
<div class="px-4 py-5 my-5 text-center">
  <h1 class="display-5 fw-bold text-body-emphasis">Hero Title</h1>
  <div class="col-lg-6 mx-auto">
    <p class="lead mb-4">Lead paragraph text.</p>
    <div class="d-grid gap-2 d-sm-flex justify-content-sm-center">
      <button type="button" class="btn btn-primary btn-lg px-4 gap-3">Primary</button>
      <button type="button" class="btn btn-outline-secondary btn-lg px-4">Secondary</button>
    </div>
  </div>
</div>

<!-- Login form -->
<div class="container" style="max-width: 400px;">
  <form>
    <div class="form-floating mb-3">
      <input type="email" class="form-control" id="email" placeholder="name@example.com">
      <label for="email">Email address</label>
    </div>
    <div class="form-floating mb-3">
      <input type="password" class="form-control" id="password" placeholder="Password">
      <label for="password">Password</label>
    </div>
    <div class="form-check mb-3">
      <input class="form-check-input" type="checkbox" id="remember">
      <label class="form-check-label" for="remember">Remember me</label>
    </div>
    <button class="btn btn-primary w-100 py-2" type="submit">Sign in</button>
  </form>
</div>
```

### Data Attributes Reference (All Components)

| Attribute | Components |
|-----------|-----------|
| `data-bs-toggle="collapse"` | Collapse, Accordion, Navbar |
| `data-bs-toggle="modal"` | Modal |
| `data-bs-toggle="dropdown"` | Dropdown |
| `data-bs-toggle="tab"` | Tabs |
| `data-bs-toggle="pill"` | Pills |
| `data-bs-toggle="list"` | List group tabs |
| `data-bs-toggle="offcanvas"` | Offcanvas |
| `data-bs-toggle="tooltip"` | Tooltip |
| `data-bs-toggle="popover"` | Popover |
| `data-bs-toggle="button"` | Toggle button |
| `data-bs-dismiss="alert"` | Alert |
| `data-bs-dismiss="modal"` | Modal |
| `data-bs-dismiss="offcanvas"` | Offcanvas |
| `data-bs-dismiss="toast"` | Toast |
| `data-bs-target="#id"` | All toggleable components |
| `data-bs-parent="#id"` | Accordion (mutual exclusion) |
| `data-bs-ride="carousel"` | Carousel autoplay |
| `data-bs-slide="prev\|next"` | Carousel controls |
| `data-bs-slide-to="0"` | Carousel indicators |
| `data-bs-spy="scroll"` | Scrollspy |
| `data-bs-theme="light\|dark"` | Color mode (any element) |
| `data-bs-backdrop="static"` | Modal, Offcanvas |
| `data-bs-keyboard="false"` | Modal, Offcanvas |
| `data-bs-scroll="true"` | Offcanvas body scroll |
| `data-bs-placement="top"` | Tooltip, Popover |
| `data-bs-auto-close="true"` | Dropdown |
