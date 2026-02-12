---
name: react-19
description: Comprehensive React 19 API reference covering all hooks, components, patterns, Server Components, Actions, and the latest APIs (use, useActionState, useOptimistic, useFormStatus). Use this skill for ALL React development.
---

# React 19 — Complete API Reference & Patterns

**Latest stable:** React 19 (2024+)

```bash
npm install react react-dom
```

---

## Hooks — State

### useState

```jsx
const [state, setState] = useState(initialState)
```

- `initialState` — value or initializer function (called once)
- Returns `[currentState, setFunction]`
- `setState(newValue)` or `setState(prev => newValue)` — triggers re-render
- Updates are batched and asynchronous — value not available until next render
- Uses `Object.is()` comparison — same reference = skip re-render

```jsx
// Basic
const [count, setCount] = useState(0)

// Lazy initialization (expensive computation only runs once)
const [data, setData] = useState(() => computeExpensiveDefault())

// Updater function (use when next state depends on previous)
setCount(prev => prev + 1)

// Objects — always replace, never mutate
setForm({ ...form, name: 'Taylor' })

// Nested objects — copy each level
setPerson({
  ...person,
  artwork: { ...person.artwork, title: 'New Title' }
})

// Arrays — create new arrays, never push/splice/mutate
setItems([...items, newItem])                    // add
setItems(items.filter(i => i.id !== targetId))   // remove
setItems(items.map(i =>                          // update
  i.id === targetId ? { ...i, done: true } : i
))

// Reset component state with key prop
<Form key={version} />
```

**Caveats:**
- Top level only — not in loops, conditions, or nested functions
- Strict Mode calls initializers/updaters twice to detect impurities
- `setState` has stable identity — safe to omit from Effect deps

---

### useReducer

```jsx
const [state, dispatch] = useReducer(reducer, initialArg, init?)
```

- `reducer(state, action)` — pure function returning next state
- `initialArg` — initial state value
- `init?` — optional initializer function: `init(initialArg)` = initial state
- `dispatch(action)` — triggers reducer, causes re-render

```jsx
function reducer(state, action) {
  switch (action.type) {
    case 'increment': return { count: state.count + 1 }
    case 'decrement': return { count: state.count - 1 }
    case 'reset':     return { count: 0 }
    default: throw new Error(`Unknown action: ${action.type}`)
  }
}

const [state, dispatch] = useReducer(reducer, { count: 0 })

dispatch({ type: 'increment' })
dispatch({ type: 'reset' })
```

**When to use over useState:**
- Complex state logic with multiple sub-values
- Next state depends on previous state + action
- State transitions need to be testable in isolation

---

## Hooks — Context

### useContext

```jsx
const value = useContext(SomeContext)
```

- Reads the nearest `<SomeContext.Provider value={...}>` above in the tree
- Re-renders when the context value changes
- Starts from the component that calls it, searches upward

```jsx
// Create context
const ThemeContext = createContext('light')

// Provide value
function App() {
  const [theme, setTheme] = useState('dark')
  return (
    <ThemeContext.Provider value={theme}>
      <Page />
    </ThemeContext.Provider>
  )
}

// Consume value
function Button() {
  const theme = useContext(ThemeContext)
  return <button className={theme}>Click</button>
}
```

**Optimization — avoid unnecessary re-renders:**

```jsx
// Split contexts: one for state, one for dispatch
const StateCtx = createContext(null)
const DispatchCtx = createContext(null)

function Provider({ children }) {
  const [state, dispatch] = useReducer(reducer, initialState)
  return (
    <StateCtx.Provider value={state}>
      <DispatchCtx.Provider value={dispatch}>
        {children}
      </DispatchCtx.Provider>
    </StateCtx.Provider>
  )
}
```

---

## Hooks — Refs

### useRef

```jsx
const ref = useRef(initialValue)
```

- Returns `{ current: initialValue }` — persists across renders
- Changing `ref.current` does NOT trigger re-render
- Most common: hold DOM nodes

```jsx
// DOM reference
const inputRef = useRef(null)
<input ref={inputRef} />
inputRef.current.focus()

// Mutable value that survives re-renders
const intervalRef = useRef(null)
intervalRef.current = setInterval(() => { ... }, 1000)
clearInterval(intervalRef.current)

// Previous value pattern
const prevCountRef = useRef(count)
useEffect(() => {
  prevCountRef.current = count
})
```

**Rules:**
- Don't read/write `ref.current` during rendering (except initialization)
- Read/write in event handlers and effects

---

### useImperativeHandle

```jsx
useImperativeHandle(ref, createHandle, dependencies?)
```

Customizes the handle exposed to parent via `ref`:

```jsx
const MyInput = forwardRef(function MyInput(props, ref) {
  const inputRef = useRef(null)

  useImperativeHandle(ref, () => ({
    focus() { inputRef.current.focus() },
    scrollIntoView() { inputRef.current.scrollIntoView() },
  }), [])

  return <input ref={inputRef} {...props} />
})

// Parent can call:
ref.current.focus()
ref.current.scrollIntoView()
```

---

## Hooks — Effects

### useEffect

```jsx
useEffect(setup, dependencies?)
```

- `setup` — function with effect logic, optionally returns cleanup function
- `dependencies` — array of reactive values; effect re-runs when any change
- Runs after browser paint (async)

```jsx
// Runs after every render
useEffect(() => { ... })

// Runs once on mount
useEffect(() => { ... }, [])

// Runs when deps change
useEffect(() => { ... }, [dep1, dep2])

// With cleanup
useEffect(() => {
  const handler = () => { ... }
  window.addEventListener('resize', handler)
  return () => window.removeEventListener('resize', handler)
}, [])
```

**Data fetching with race condition handling:**

```jsx
useEffect(() => {
  let ignore = false
  async function fetchData() {
    const result = await fetch(`/api/items/${id}`)
    const data = await result.json()
    if (!ignore) setData(data)
  }
  fetchData()
  return () => { ignore = true }
}, [id])
```

**Dependency rules:**
- Include ALL reactive values used inside the effect
- Move static values outside the component (no longer reactive)
- Move objects/functions inside the effect to avoid reference changes
- Use updater functions to avoid depending on state: `setCount(c => c + 1)`

**When NOT to use useEffect:**
- Transforming data for rendering (do it during render)
- Handling user events (use event handlers)
- Resetting state on prop change (use `key` prop)
- Derived state (use `useMemo` or compute during render)

---

### useLayoutEffect

```jsx
useLayoutEffect(setup, dependencies?)
```

Same as `useEffect` but fires **before browser paint**. Use for:
- Measuring DOM layout (element dimensions, positions)
- Preventing visual flicker (tooltip positioning, animations)

```jsx
useLayoutEffect(() => {
  const { height } = ref.current.getBoundingClientRect()
  setTooltipHeight(height)
}, [])
```

**Warning:** Blocks painting — keep it fast.

---

### useInsertionEffect

```jsx
useInsertionEffect(setup, dependencies?)
```

Fires before DOM mutations. For CSS-in-JS libraries to inject `<style>` tags.
You almost certainly don't need this directly.

---

## Hooks — Performance

### useMemo

```jsx
const memoizedValue = useMemo(() => computeExpensiveValue(a, b), [a, b])
```

- Caches computation result between re-renders
- Only recomputes when dependencies change
- First render: calls the function and returns result
- Subsequent renders: returns cached result if deps unchanged

```jsx
// Expensive filtering
const visibleItems = useMemo(
  () => items.filter(item => item.isVisible).sort(sortFn),
  [items]
)

// Memoize JSX to skip child re-renders
const chart = useMemo(() => <Chart data={data} />, [data])
```

**When to use:**
- Slow computations (>1ms) — profile with `console.time()`
- Value passed as dependency to another hook
- Value passed as prop to `memo()` wrapped component

---

### useCallback

```jsx
const memoizedFn = useCallback(fn, dependencies)
```

- Caches a function definition between re-renders
- Returns same function reference if deps unchanged
- Equivalent to `useMemo(() => fn, deps)`

```jsx
const handleSubmit = useCallback((data) => {
  post('/api/submit', { body: data })
}, [])

// Useful when passing callbacks to memoized children
<MemoizedList onItemClick={handleSubmit} />
```

**When to use:**
- Passing callbacks to `memo()` wrapped children
- Callback used as dependency in another hook
- Custom hooks returning functions to consumers

---

### memo

```jsx
const MemoizedComponent = memo(Component, arePropsEqual?)
```

- Wraps component to skip re-renders when props haven't changed
- Uses shallow comparison (`Object.is`) by default
- Optional `arePropsEqual(oldProps, newProps)` for custom comparison

```jsx
const ItemCard = memo(function ItemCard({ item, onSelect }) {
  return (
    <div onClick={() => onSelect(item.id)}>
      <h3>{item.title}</h3>
    </div>
  )
})
```

**Breaks when:** Props include new object/array/function references each render.
**Fix:** Use `useMemo`/`useCallback` for prop values.

---

### useTransition

```jsx
const [isPending, startTransition] = useTransition()
```

- Marks state updates as non-blocking transitions
- `isPending` — boolean, true while transition is in progress
- `startTransition(action)` — wraps state updates as low-priority

```jsx
function TabContainer() {
  const [tab, setTab] = useState('home')
  const [isPending, startTransition] = useTransition()

  function selectTab(nextTab) {
    startTransition(() => {
      setTab(nextTab)
    })
  }

  return (
    <div style={{ opacity: isPending ? 0.7 : 1 }}>
      <TabButton onClick={() => selectTab('home')}>Home</TabButton>
      <TabButton onClick={() => selectTab('posts')}>Posts</TabButton>
      {tab === 'home' ? <Home /> : <Posts />}
    </div>
  )
}
```

**Async transitions (React 19):**

```jsx
startTransition(async () => {
  const result = await saveData(formData)
  // Post-await updates need their own startTransition
  startTransition(() => {
    setResult(result)
  })
})
```

**Key behaviors:**
- User input interrupts pending transitions
- Multiple transitions are batched
- Cannot control text inputs (use `useDeferredValue` instead)
- Prevents Suspense fallback from replacing visible content

---

### useDeferredValue

```jsx
const deferredValue = useDeferredValue(value)
```

- Defers updating a value until higher-priority updates complete
- During urgent updates, returns old value; background re-render uses new value
- Built-in debouncing without a timer

```jsx
function SearchPage({ query }) {
  const deferredQuery = useDeferredValue(query)
  const isStale = query !== deferredQuery

  return (
    <div style={{ opacity: isStale ? 0.5 : 1 }}>
      <Suspense fallback={<Spinner />}>
        <SearchResults query={deferredQuery} />
      </Suspense>
    </div>
  )
}
```

---

## Hooks — React 19 New APIs

### use

```jsx
const value = use(resource)
```

- Reads a Promise or Context value
- **Unlike other hooks:** can be called inside conditionals and loops
- With Promise: suspends component until resolved (works with Suspense)
- With Context: same as `useContext` but more flexible placement

```jsx
// Reading a promise (suspends until resolved)
function Message({ messagePromise }) {
  const message = use(messagePromise)
  return <p>{message}</p>
}

// Reading context conditionally
function HorizontalRule({ show }) {
  if (show) {
    const theme = use(ThemeContext)
    return <hr className={theme} />
  }
  return false
}

// Server-to-client data streaming
// Server Component passes promise, Client Component reads it
export default function App() {
  const dataPromise = fetchData()
  return (
    <Suspense fallback={<Loading />}>
      <ClientComponent dataPromise={dataPromise} />
    </Suspense>
  )
}
```

**Caveats:**
- Cannot be used in try-catch (use Error Boundary instead)
- Must be called in component/hook body (not event handlers)
- Resolved Promise values must be serializable

---

### useActionState

```jsx
const [state, formAction, isPending] = useActionState(fn, initialState, permalink?)
```

- Manages state based on form action results
- `fn(previousState, formData)` — action receives previous state as first arg
- `formAction` — pass to `<form action={formAction}>` or `<button formAction={formAction}>`
- `isPending` — true while action is executing

```jsx
import { useActionState } from 'react'

async function submitForm(prevState, formData) {
  const name = formData.get('name')
  if (!name) return { error: 'Name is required' }
  await saveUser(name)
  return { success: true, name }
}

function UserForm() {
  const [state, formAction, isPending] = useActionState(submitForm, {})

  return (
    <form action={formAction}>
      <input name="name" />
      <button type="submit" disabled={isPending}>
        {isPending ? 'Saving...' : 'Save'}
      </button>
      {state.error && <p className="error">{state.error}</p>}
      {state.success && <p>Saved {state.name}</p>}
    </form>
  )
}
```

---

### useOptimistic

```jsx
const [optimisticState, addOptimistic] = useOptimistic(state, updateFn?)
```

- Shows optimistic UI while async action completes
- Automatically reverts if action fails
- Must be called inside an Action (`startTransition` or form action)

```jsx
import { useOptimistic, startTransition } from 'react'

function TodoList({ todos, addTodo }) {
  const [optimisticTodos, addOptimisticTodo] = useOptimistic(
    todos,
    (currentTodos, newTodo) => [
      ...currentTodos,
      { ...newTodo, pending: true }
    ]
  )

  async function handleAdd(text) {
    startTransition(async () => {
      addOptimisticTodo({ id: Date.now(), text })
      await addTodo(text) // If this fails, optimistic state reverts
    })
  }

  return (
    <ul>
      {optimisticTodos.map(todo => (
        <li key={todo.id} style={{ opacity: todo.pending ? 0.5 : 1 }}>
          {todo.text}
        </li>
      ))}
    </ul>
  )
}
```

---

### useFormStatus (react-dom)

```jsx
const { pending, data, method, action } = useFormStatus()
```

- Reads the submission status of the **parent** `<form>`
- Must be called from a component **inside** a `<form>` (not the same component)
- `pending` — true while form is submitting
- `data` — FormData being submitted (null if idle)

```jsx
import { useFormStatus } from 'react-dom'

function SubmitButton() {
  const { pending } = useFormStatus()
  return (
    <button type="submit" disabled={pending}>
      {pending ? 'Submitting...' : 'Submit'}
    </button>
  )
}

// MUST be a child component of the form
function MyForm({ action }) {
  return (
    <form action={action}>
      <input name="email" type="email" />
      <SubmitButton />
    </form>
  )
}
```

---

## Hooks — Other

### useId

```jsx
const id = useId()
```

Generates unique IDs for accessibility attributes:

```jsx
function PasswordField() {
  const id = useId()
  return (
    <>
      <label htmlFor={id}>Password:</label>
      <input id={id} type="password" />
    </>
  )
}
```

- Stable across server and client rendering
- Don't use for list keys

---

### useDebugValue

```jsx
useDebugValue(value, format?)
```

Adds a label in React DevTools for custom hooks:

```jsx
function useOnlineStatus() {
  const isOnline = useSyncExternalStore(subscribe, getSnapshot)
  useDebugValue(isOnline ? 'Online' : 'Offline')
  return isOnline
}
```

---

### useSyncExternalStore

```jsx
const snapshot = useSyncExternalStore(subscribe, getSnapshot, getServerSnapshot?)
```

Subscribe to external stores (third-party state, browser APIs):

```jsx
function useWindowWidth() {
  return useSyncExternalStore(
    (callback) => {
      window.addEventListener('resize', callback)
      return () => window.removeEventListener('resize', callback)
    },
    () => window.innerWidth,
    () => 1024 // server snapshot
  )
}
```

---

## Components

### Suspense

```jsx
<Suspense fallback={<Loading />}>
  <SomeComponent />
</Suspense>
```

Displays fallback while children are loading (lazy components, `use()` with promises).

```jsx
// Lazy loading
const HeavyComponent = lazy(() => import('./HeavyComponent'))

<Suspense fallback={<Spinner />}>
  <HeavyComponent />
</Suspense>

// Nested boundaries (progressive loading)
<Suspense fallback={<PageSkeleton />}>
  <Header />
  <Suspense fallback={<ContentSkeleton />}>
    <MainContent />
  </Suspense>
</Suspense>

// With transitions (don't hide already-visible content)
const [isPending, startTransition] = useTransition()

function navigate(url) {
  startTransition(() => setPage(url))
}
// Suspense won't show fallback for transition updates
```

---

### Fragment

```jsx
<Fragment key={id}>  or  <>...</>
```

Group elements without a wrapper DOM node:

```jsx
// Short syntax
<>
  <h1>Title</h1>
  <p>Content</p>
</>

// With key (for lists)
{items.map(item => (
  <Fragment key={item.id}>
    <dt>{item.term}</dt>
    <dd>{item.definition}</dd>
  </Fragment>
))}
```

---

### StrictMode

```jsx
<StrictMode>
  <App />
</StrictMode>
```

Development-only checks:
- Double-invokes render, effects, and reducers to detect impurities
- Warns about deprecated APIs
- No production impact

---

### Profiler

```jsx
<Profiler id="App" onRender={onRender}>
  <App />
</Profiler>
```

Measures render performance programmatically.

---

## React APIs

### createContext

```jsx
const SomeContext = createContext(defaultValue)
```

```jsx
const ThemeContext = createContext('light')

// Provider (React 19 shorthand)
<ThemeContext value="dark">
  <App />
</ThemeContext>

// Legacy provider syntax (still works)
<ThemeContext.Provider value="dark">
  <App />
</ThemeContext.Provider>
```

---

### forwardRef

```jsx
const Component = forwardRef((props, ref) => { ... })
```

Lets a component receive a ref from its parent:

```jsx
const MyInput = forwardRef(function MyInput({ label }, ref) {
  return (
    <label>
      {label}
      <input ref={ref} />
    </label>
  )
})

// Parent
const ref = useRef(null)
<MyInput ref={ref} label="Name" />
ref.current.focus()
```

**Note:** React 19 supports `ref` as a regular prop — `forwardRef` may become optional in future.

---

### lazy

```jsx
const LazyComponent = lazy(() => import('./Component'))
```

Code-splits a component, loading it on first render:

```jsx
const Settings = lazy(() => import('./Settings'))

function App() {
  return (
    <Suspense fallback={<Spinner />}>
      {showSettings && <Settings />}
    </Suspense>
  )
}
```

---

### startTransition (standalone)

```jsx
import { startTransition } from 'react'

startTransition(() => {
  setState(newValue)
})
```

Same as `useTransition`'s `startTransition` but usable outside components (e.g., in data libraries).

---

## Server Components & Actions (React 19)

### Server Components

```jsx
// This component runs on the server only
// No 'use client' directive = server component by default
async function BlogPosts() {
  const posts = await db.posts.findMany()
  return (
    <ul>
      {posts.map(post => <li key={post.id}>{post.title}</li>)}
    </ul>
  )
}
```

- Default in React 19 frameworks (Next.js App Router)
- Can use `async/await` directly
- Cannot use hooks or browser APIs
- Can import and render Client Components

### Client Components

```jsx
'use client'

import { useState } from 'react'

export function Counter() {
  const [count, setCount] = useState(0)
  return <button onClick={() => setCount(count + 1)}>{count}</button>
}
```

- Add `'use client'` directive at top of file
- Can use hooks, event handlers, browser APIs
- Cannot import Server Components (but can receive them as children)

### Server Actions

```jsx
'use server'

export async function createPost(formData) {
  const title = formData.get('title')
  await db.posts.create({ data: { title } })
}
```

```jsx
// Used in a form
<form action={createPost}>
  <input name="title" />
  <button type="submit">Create</button>
</form>

// Or called directly
const result = await createPost(formData)
```

---

## Patterns & Best Practices

### Component Organization

```
src/
  components/           # Reusable UI
    Button/
      Button.tsx
      Button.test.tsx
      index.ts
  hooks/                # Custom hooks
  pages/                # Route-level components
  core/                 # Business logic (no React)
    types.ts
    services/
  api/                  # API client, queries
  store/                # Global state (Zustand, etc.)
```

### Custom Hook Pattern

```jsx
function useLocalStorage(key, initialValue) {
  const [stored, setStored] = useState(() => {
    try {
      const item = window.localStorage.getItem(key)
      return item ? JSON.parse(item) : initialValue
    } catch {
      return initialValue
    }
  })

  const setValue = useCallback((value) => {
    const valueToStore = value instanceof Function ? value(stored) : value
    setStored(valueToStore)
    window.localStorage.setItem(key, JSON.stringify(valueToStore))
  }, [key, stored])

  return [stored, setValue]
}
```

### Error Boundary Pattern

```jsx
import { Component } from 'react'

class ErrorBoundary extends Component {
  state = { hasError: false, error: null }

  static getDerivedStateFromError(error) {
    return { hasError: true, error }
  }

  componentDidCatch(error, errorInfo) {
    console.error('Error caught:', error, errorInfo)
  }

  render() {
    if (this.state.hasError) {
      return this.props.fallback || <h1>Something went wrong.</h1>
    }
    return this.props.children
  }
}

// Usage
<ErrorBoundary fallback={<ErrorPage />}>
  <App />
</ErrorBoundary>
```

### Data Fetching Patterns

```jsx
// React Query (recommended for client-side fetching)
import { useQuery, useMutation, useQueryClient } from '@tanstack/react-query'

function useItems() {
  return useQuery({
    queryKey: ['items'],
    queryFn: () => fetch('/api/items').then(r => r.json()),
    staleTime: 5 * 60 * 1000,
  })
}

function useCreateItem() {
  const queryClient = useQueryClient()
  return useMutation({
    mutationFn: (item) => fetch('/api/items', {
      method: 'POST',
      body: JSON.stringify(item),
    }),
    onSuccess: () => queryClient.invalidateQueries({ queryKey: ['items'] }),
  })
}
```

### Form Handling

```jsx
// React Hook Form + Zod
import { useForm } from 'react-hook-form'
import { zodResolver } from '@hookform/resolvers/zod'
import { z } from 'zod'

const schema = z.object({
  email: z.string().email(),
  password: z.string().min(8),
})

function LoginForm() {
  const { register, handleSubmit, formState: { errors } } = useForm({
    resolver: zodResolver(schema),
  })

  return (
    <form onSubmit={handleSubmit(onSubmit)}>
      <input {...register('email')} />
      {errors.email && <span>{errors.email.message}</span>}
      <input type="password" {...register('password')} />
      {errors.password && <span>{errors.password.message}</span>}
      <button type="submit">Login</button>
    </form>
  )
}
```

---

## Anti-Patterns to Avoid

- Never mutate state directly — always create new objects/arrays
- Never use index as key in dynamic lists — use stable IDs
- Never fetch data in useEffect without race condition handling
- Never use useEffect for derived state — compute during render or useMemo
- Don't prop drill more than 2 levels — use context or state management
- Don't put logic in render — extract to custom hooks
- Don't create new objects/functions in JSX — use useMemo/useCallback
- Don't use useEffect to sync state with props — calculate during render
- Don't ignore the exhaustive-deps ESLint rule — fix the actual problem
