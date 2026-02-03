---
name: react-ts-expert
description: Skill for building type-safe, performant React applications with TypeScript.
---

# Skill: React TypeScript Expert (v1.0)

## Purpose
Enforce strict typing and modern patterns in React development.

## Activation Trigger
- "Write a React component"
- "Fix this TS error"
- "React" or "TSX" mentioned.

---

## Protocol: Typing Patterns

### 1. Props Interface
**Rule:** Use `interface` over `type` for props (better error messages).

```tsx
interface UserProfileProps {
  id: string;
  name: string;
  role: 'admin' | 'user'; // Union type
  onUpdate: (user: User) => Promise<void>;
}
```

### 2. Generic Components
**Rule:** Use generics for flexible components.

```tsx
interface ListProps<T> {
  items: T[];
  renderItem: (item: T) => React.ReactNode;
}

export function List<T extends { id: string }>({ items, renderItem }: ListProps<T>) {
  return (
    <ul>
      {items.map(item => (
        <li key={item.id}>{renderItem(item)}</li>
      ))}
    </ul>
  );
}
```

---

## Protocol: Hooks Rules

1.  **Dependency Arrays:** ALWAYS verify exhaustive deps.
    *   *Bad:* `useEffect(() => { ... }, [])` (ignoring props)
    *   *Good:* `useEffect(() => { ... }, [prop])`
2.  **Custom Hooks:** Extract logic > 10 lines into `useFeatureName.ts`.

---

## Protocol: Performance

- **Memoization:** Don't premature optimize. Only use `useMemo`/`useCallback` when passing props to heavy children or context.
- **Code Splitting:** Use `lazy` for routes.
  ```tsx
  const Dashboard = lazy(() => import('./pages/Dashboard'));
  ```
