---
name: javascript-es2025
description: Comprehensive modern JavaScript reference covering ES2024/2025 syntax, all built-in methods (Array, Object, String, Promise, Map, Set), async patterns, modules, error handling, iterators, proxies, and best practices. Use this skill for ALL JavaScript work.
---

# Modern JavaScript — Complete Reference (ES2025)

---

## Variables & Scope

```javascript
const x = 1          // Block-scoped, cannot reassign (preferred default)
let y = 2            // Block-scoped, can reassign
var z = 3            // Function-scoped, hoisted (avoid)

// Destructuring
const { name, age = 25 } = person
const { name: userName } = person          // Rename
const { address: { city } } = person       // Nested
const [first, second, ...rest] = array
const [, second] = array                   // Skip first

// Spread
const merged = { ...obj1, ...obj2 }        // Object spread (later wins)
const combined = [...arr1, ...arr2]        // Array spread
```

---

## Data Types & Operators

### Primitives
```javascript
typeof 'hello'       // 'string'
typeof 42            // 'number'
typeof 42n           // 'bigint'
typeof true          // 'boolean'
typeof undefined     // 'undefined'
typeof null          // 'object' (historical bug)
typeof Symbol()      // 'symbol'
```

### Equality
```javascript
===                  // Strict equality (no coercion) — always use this
!==                  // Strict inequality
==                   // Loose equality (coerces types) — avoid
Object.is(a, b)     // Same-value equality (NaN === NaN is true)
```

### Nullish & Optional

```javascript
// Nullish coalescing — only null/undefined trigger fallback
value ?? 'default'           // '' and 0 are NOT nullish

// Optional chaining — short-circuits to undefined
user?.address?.city          // Property access
user?.getName?.()            // Method call
arr?.[0]                     // Array access

// Logical assignment
x ??= 5             // x = x ?? 5 (assign if null/undefined)
x ||= 5             // x = x || 5 (assign if falsy)
x &&= 5             // x = x && 5 (assign if truthy)
```

---

## Strings

### Template Literals

```javascript
const greeting = `Hello ${name}`
const multiline = `
  Line 1
  Line 2
`

// Tagged templates
function highlight(strings, ...values) {
  return strings.reduce((result, str, i) =>
    result + str + (values[i] ? `<mark>${values[i]}</mark>` : ''), '')
}
const html = highlight`Hello ${name}, you are ${age} years old`
```

### String Methods

```javascript
// Search
str.includes('hello')          // boolean
str.startsWith('http')         // boolean
str.endsWith('.js')            // boolean
str.indexOf('x')               // index or -1
str.search(/regex/)            // index or -1

// Extract
str.slice(1, 5)                // substring by index (negative ok)
str.substring(1, 5)            // like slice but no negative
str.at(0)                      // first char
str.at(-1)                     // last char

// Transform
str.toUpperCase()
str.toLowerCase()
str.trim()                     // both ends
str.trimStart()                // left
str.trimEnd()                  // right
str.padStart(10, '0')          // '0000000042'
str.padEnd(10, '.')            // '42........'
str.repeat(3)                  // 'abcabcabc'
str.replace('old', 'new')     // first occurrence
str.replaceAll('old', 'new')  // all occurrences

// Split / Join
str.split(',')                 // to array
arr.join(', ')                 // to string

// Regex
str.match(/pattern/g)          // array of matches or null
str.matchAll(/pattern/g)       // iterator of match objects

// Type checking
str.isWellFormed()             // ES2024: check valid unicode
str.toWellFormed()             // ES2024: fix invalid unicode
```

---

## Numbers & Math

```javascript
// Parsing
Number('42')                   // 42
Number.parseInt('42px', 10)    // 42
Number.parseFloat('3.14')      // 3.14

// Checking
Number.isFinite(42)            // true
Number.isNaN(NaN)              // true (unlike global isNaN)
Number.isInteger(42.0)         // true
Number.isSafeInteger(n)        // within -(2^53-1) to 2^53-1

// Formatting
(1234.5).toFixed(2)            // '1234.50'
(1234.5).toLocaleString()      // '1,234.5' (locale-aware)
new Intl.NumberFormat('en-US', { style: 'currency', currency: 'USD' })
  .format(1234.50)             // '$1,234.50'

// Math
Math.floor(4.7)                // 4
Math.ceil(4.2)                 // 5
Math.round(4.5)                // 5
Math.trunc(4.7)                // 4 (remove decimal)
Math.abs(-5)                   // 5
Math.max(1, 2, 3)              // 3
Math.min(1, 2, 3)              // 1
Math.random()                  // 0 to 1 (exclusive)
Math.pow(2, 3)                 // 8 (or 2 ** 3)
Math.sqrt(16)                  // 4
Math.sign(-5)                  // -1, 0, or 1

// BigInt (arbitrary precision)
const big = 9007199254740993n
big + 1n                       // 9007199254740994n
```

---

## Arrays

### Creation

```javascript
const arr = [1, 2, 3]
Array.from({ length: 5 }, (_, i) => i)     // [0, 1, 2, 3, 4]
Array.from('hello')                         // ['h', 'e', 'l', 'l', 'o']
Array.of(1, 2, 3)                           // [1, 2, 3]
new Array(5).fill(0)                        // [0, 0, 0, 0, 0]
```

### Iteration (return new array — immutable)

```javascript
arr.map(x => x * 2)                        // [2, 4, 6]
arr.filter(x => x > 1)                     // [2, 3]
arr.reduce((acc, x) => acc + x, 0)         // 6
arr.reduceRight((acc, x) => acc + x, 0)    // 6 (right to left)
arr.flatMap(x => [x, x * 2])              // [1, 2, 2, 4, 3, 6]
arr.flat(depth)                             // flatten nested arrays
arr.slice(1, 3)                             // [2, 3] (doesn't modify)
arr.concat([4, 5])                          // [1, 2, 3, 4, 5]
arr.toSorted((a, b) => a - b)              // ES2023: sorted copy
arr.toReversed()                            // ES2023: reversed copy
arr.toSpliced(1, 1, 'x')                  // ES2023: spliced copy
arr.with(1, 'x')                           // ES2023: [1, 'x', 3]
```

### Search

```javascript
arr.find(x => x > 1)                       // 2 (first match or undefined)
arr.findIndex(x => x > 1)                  // 1 (first index or -1)
arr.findLast(x => x > 1)                   // 3 (ES2023: last match)
arr.findLastIndex(x => x > 1)              // 2 (ES2023: last index)
arr.includes(2)                             // true
arr.indexOf(2)                              // 1
arr.lastIndexOf(2)                          // 1
arr.some(x => x > 2)                       // true
arr.every(x => x > 0)                      // true
```

### Mutation (modify in place)

```javascript
arr.push(4)                    // add to end, returns length
arr.pop()                      // remove from end, returns removed
arr.unshift(0)                 // add to start, returns length
arr.shift()                    // remove from start, returns removed
arr.splice(1, 1, 'x')         // remove 1 at index 1, insert 'x'
arr.sort((a, b) => a - b)     // sort in place (numeric)
arr.reverse()                  // reverse in place
arr.fill(0, 1, 3)             // fill indices 1-2 with 0
arr.copyWithin(0, 2)          // copy from index 2 to index 0
```

### Grouping (ES2024)

```javascript
// Object.groupBy — returns plain object
const grouped = Object.groupBy(people, person => person.age >= 18 ? 'adult' : 'minor')
// { adult: [...], minor: [...] }

// Map.groupBy — returns Map
const map = Map.groupBy(items, item => item.category)
```

### Array-like to Array

```javascript
Array.from(nodeList)
[...nodeList]
Array.from(arguments)
```

---

## Objects

### Creation & Access

```javascript
// Shorthand properties
const obj = { name, age, greet() { return `Hi ${this.name}` } }

// Computed property names
const key = 'dynamic'
const obj = { [key]: 'value', [`${key}2`]: 'value2' }

// Access
obj.name                       // dot notation
obj['name']                    // bracket notation
obj?.nested?.prop              // optional chaining
```

### Object Static Methods

```javascript
Object.keys(obj)               // ['name', 'age']
Object.values(obj)             // ['Taylor', 25]
Object.entries(obj)            // [['name', 'Taylor'], ['age', 25]]
Object.fromEntries(entries)    // reverse of entries

Object.assign(target, ...sources)  // shallow merge (mutates target)
structuredClone(obj)               // deep clone

Object.freeze(obj)             // cannot add/remove/change properties
Object.isFrozen(obj)
Object.seal(obj)               // cannot add/remove, can change values
Object.isSealed(obj)

Object.hasOwn(obj, 'prop')    // ES2022: preferred over hasOwnProperty
Object.is(a, b)               // strict equality (NaN === NaN)

Object.defineProperty(obj, 'prop', {
  value: 42,
  writable: true,
  enumerable: true,
  configurable: true,
})

Object.getOwnPropertyDescriptor(obj, 'prop')
Object.getOwnPropertyNames(obj)    // all own props (including non-enumerable)
Object.getPrototypeOf(obj)
```

---

## Functions

```javascript
// Arrow functions (lexical this)
const add = (a, b) => a + b
const greet = name => `Hello ${name}`
const getObj = () => ({ key: 'value' })    // return object literal

// Default parameters
function create(name, age = 25) { }

// Rest parameters
function sum(...numbers) { return numbers.reduce((a, b) => a + b, 0) }

// IIFE
;(function() { })()
;(() => { })()
```

---

## Classes

```javascript
class Animal {
  // Public field
  name

  // Private field (ES2022)
  #sound

  // Static field
  static count = 0

  // Static private field
  static #instances = []

  constructor(name, sound) {
    this.name = name
    this.#sound = sound
    Animal.count++
    Animal.#instances.push(this)
  }

  // Public method
  speak() {
    return `${this.name} says ${this.#sound}`
  }

  // Private method
  #validate() { }

  // Getter
  get info() { return `${this.name}: ${this.#sound}` }

  // Setter
  set nickname(value) { this.name = value }

  // Static method
  static getCount() { return Animal.count }

  // Static block (ES2022)
  static {
    console.log('Animal class initialized')
  }
}

// Inheritance
class Dog extends Animal {
  constructor(name) {
    super(name, 'Woof')
  }

  // Override
  speak() {
    return `${super.speak()}!`
  }
}

const dog = new Dog('Rex')
dog.speak()                // 'Rex says Woof!'
dog instanceof Dog         // true
dog instanceof Animal      // true
```

---

## Promises & Async/Await

### Promise API

```javascript
// Creating
const p = new Promise((resolve, reject) => {
  resolve(value)
  reject(new Error('reason'))
})

// Static methods
Promise.resolve(value)         // Resolved promise
Promise.reject(error)          // Rejected promise
Promise.all([p1, p2, p3])     // All must resolve (rejects on first failure)
Promise.allSettled([p1, p2])   // Wait for all, regardless of result
Promise.race([p1, p2])        // First to settle (resolve or reject)
Promise.any([p1, p2])         // First to resolve (AggregateError if all reject)
Promise.withResolvers()        // ES2024: { promise, resolve, reject }

// Chaining
fetch('/api/data')
  .then(res => res.json())
  .then(data => process(data))
  .catch(err => handleError(err))
  .finally(() => cleanup())
```

### Promise.withResolvers (ES2024)

```javascript
const { promise, resolve, reject } = Promise.withResolvers()

// Use resolve/reject from outside the constructor callback
setTimeout(() => resolve('done'), 1000)
await promise  // 'done'
```

### Async/Await

```javascript
async function fetchData(url) {
  try {
    const response = await fetch(url)
    if (!response.ok) throw new Error(`HTTP ${response.status}`)
    return await response.json()
  } catch (error) {
    console.error('Fetch failed:', error)
    throw error
  }
}

// Parallel
const [users, posts] = await Promise.all([
  fetchData('/api/users'),
  fetchData('/api/posts'),
])

// Sequential with for...of
for (const url of urls) {
  const data = await fetchData(url)
  results.push(data)
}

// Top-level await (ES modules)
const config = await loadConfig()

// Async iteration
for await (const chunk of stream) {
  process(chunk)
}
```

---

## Iterators & Generators

```javascript
// Generator function
function* range(start, end) {
  for (let i = start; i < end; i++) {
    yield i
  }
}

for (const n of range(0, 5)) {
  console.log(n)  // 0, 1, 2, 3, 4
}

// Async generator
async function* fetchPages(url) {
  let page = 1
  while (true) {
    const response = await fetch(`${url}?page=${page}`)
    const data = await response.json()
    if (data.length === 0) return
    yield data
    page++
  }
}

for await (const page of fetchPages('/api/items')) {
  processPage(page)
}

// Iterator helpers (ES2025)
const iter = [1, 2, 3, 4, 5].values()
iter.filter(x => x > 2).map(x => x * 2).toArray()  // [6, 8, 10]
iter.take(3)           // first 3
iter.drop(2)           // skip first 2
iter.find(x => x > 3) // first match
iter.some(x => x > 4) // boolean
iter.every(x => x > 0)
iter.reduce((a, b) => a + b, 0)
iter.flatMap(x => [x, x])
```

---

## Map & Set

### Map

```javascript
const map = new Map()
map.set('key', 'value')
map.get('key')                 // 'value'
map.has('key')                 // true
map.delete('key')              // true
map.clear()
map.size                       // 0

// Initialize with entries
const map = new Map([['a', 1], ['b', 2]])

// Iteration
for (const [key, value] of map) { }
map.forEach((value, key) => { })
map.keys()                     // iterator
map.values()                   // iterator
map.entries()                  // iterator of [key, value]
```

### WeakMap

```javascript
const wm = new WeakMap()       // Keys must be objects, GC-friendly
wm.set(obj, metadata)
wm.get(obj)
wm.has(obj)
wm.delete(obj)
// Not iterable, no size
```

### Set

```javascript
const set = new Set([1, 2, 3, 2])  // {1, 2, 3}
set.add(4)
set.has(2)                     // true
set.delete(2)                  // true
set.clear()
set.size                       // 3

// Set operations (ES2025)
const a = new Set([1, 2, 3])
const b = new Set([2, 3, 4])

a.union(b)                     // {1, 2, 3, 4}
a.intersection(b)              // {2, 3}
a.difference(b)                // {1}
a.symmetricDifference(b)       // {1, 4}
a.isSubsetOf(b)                // false
a.isSupersetOf(b)              // false
a.isDisjointFrom(b)            // false

// Unique array values
const unique = [...new Set(array)]
```

---

## Modules (ES Modules)

```javascript
// Named exports
export const name = 'value'
export function greet() { }
export class User { }

// Default export (one per module)
export default function main() { }

// Named imports
import { name, greet } from './module.js'
import { name as alias } from './module.js'

// Default import
import main from './module.js'

// Namespace import
import * as utils from './utils.js'

// Dynamic import (code splitting)
const module = await import('./heavy-module.js')

// Re-export
export { name, greet } from './module.js'
export { default } from './module.js'
export * from './module.js'
export * as utils from './utils.js'
```

---

## Error Handling

```javascript
try {
  riskyOperation()
} catch (error) {
  if (error instanceof TypeError) {
    handleTypeError(error)
  } else {
    throw error  // re-throw unknown errors
  }
} finally {
  cleanup()  // always runs
}

// Custom errors
class AppError extends Error {
  constructor(message, code) {
    super(message)
    this.name = 'AppError'
    this.code = code
  }
}

// Error cause (ES2022)
throw new Error('Failed to fetch user data', { cause: originalError })

// AggregateError (multiple errors)
throw new AggregateError(errors, 'Multiple failures')
```

---

## Proxy & Reflect

```javascript
const handler = {
  get(target, prop, receiver) {
    console.log(`Getting ${prop}`)
    return Reflect.get(target, prop, receiver)
  },
  set(target, prop, value, receiver) {
    console.log(`Setting ${prop} = ${value}`)
    return Reflect.set(target, prop, value, receiver)
  },
}

const proxy = new Proxy(target, handler)
```

---

## Regular Expressions

```javascript
// Flags
/pattern/g           // global (all matches)
/pattern/i           // case-insensitive
/pattern/m           // multiline (^ and $ per line)
/pattern/s           // dotAll (. matches newlines)
/pattern/u           // unicode
/pattern/v           // unicodeSets (ES2024, superset of u)
/pattern/d           // indices (match positions)

// Named groups
const match = /(?<year>\d{4})-(?<month>\d{2})-(?<day>\d{2})/.exec('2026-02-12')
match.groups.year    // '2026'

// Lookbehind / Lookahead
/(?<=\$)\d+/         // Lookbehind: digits after $
/\d+(?=%)/           // Lookahead: digits before %

// matchAll
for (const match of str.matchAll(/pattern/g)) {
  console.log(match[0], match.index)
}
```

---

## Web APIs (Browser)

### Fetch

```javascript
// GET
const response = await fetch('/api/data')
const data = await response.json()

// POST
const response = await fetch('/api/data', {
  method: 'POST',
  headers: { 'Content-Type': 'application/json' },
  body: JSON.stringify({ name: 'Taylor' }),
})

// With abort controller
const controller = new AbortController()
setTimeout(() => controller.abort(), 5000)
await fetch('/api/data', { signal: controller.signal })
```

### DOM

```javascript
// Selection
document.getElementById('id')
document.querySelector('.class')
document.querySelectorAll('.class')
element.closest('.parent')
element.matches('.selector')

// Manipulation
element.textContent = 'text'
element.innerHTML = '<p>html</p>'
element.classList.add('active')
element.classList.remove('active')
element.classList.toggle('active')
element.dataset.id                       // data-id attribute
element.style.setProperty('--color', 'red')

// Creation
const el = document.createElement('div')
parent.append(el, 'text', otherEl)
el.before(siblingEl)
el.after(siblingEl)
el.replaceWith(newEl)
el.remove()

// Events
el.addEventListener('click', handler, { once: true, passive: true })
el.removeEventListener('click', handler)
el.dispatchEvent(new CustomEvent('myevent', { detail: data, bubbles: true }))
```

### Storage

```javascript
// LocalStorage (persistent)
localStorage.setItem('key', JSON.stringify(value))
JSON.parse(localStorage.getItem('key'))
localStorage.removeItem('key')

// SessionStorage (per tab, cleared on close)
sessionStorage.setItem('key', value)
```

---

## Best Practices

1. **Use `const` by default**, `let` when reassignment needed, never `var`
2. **Use strict equality** `===` and `!==` always
3. **Use optional chaining** `?.` and nullish coalescing `??` instead of manual checks
4. **Use `for...of`** for arrays, `for...in` for object keys (with `hasOwn` check)
5. **Use arrow functions** for callbacks, regular functions for methods needing `this`
6. **Use template literals** over string concatenation
7. **Use destructuring** for function parameters and return values
8. **Use `Promise.all()`** for parallel async, not sequential awaits
9. **Always handle Promise rejections** — use try/catch with async/await
10. **Use `structuredClone()`** for deep cloning, not JSON round-trip
11. **Use immutable array methods** (`.toSorted()`, `.toReversed()`, `.with()`) when possible
12. **Use `Map` over plain objects** when keys are dynamic or non-string
13. **Use `Set` for unique collections** — `[...new Set(arr)]` for dedup
14. **Use `Object.groupBy()`** instead of manual reduce-based grouping
