---
name: react-ts-expert
description: Protocols for React 19, Server Components, TypeScript, and State Management.
---

# React TypeScript Expert

> "UI as a function of State."

## Activation Trigger
- Building React components (Client or Server).
- Managing complex state (Zustand/Context).
- Optimizing frontend performance.

## 1. React 19 & Server Components (RSC)
The paradigm has shifted. Data fetching belongs on the server.

```tsx
// Server Component (Default in Next.js 14+)
async function userProfile({ id }: { id: string }) {
  const user = await db.user.findUnique({ where: { id } });
  
  return (
    <div>
      <h1>{user.name}</h1>
      <ClientButton userId={user.id} />
    </div>
  );
}
```

## 2. Server Actions (The New Mutation)
No more `useEffect` for data fetching. No more API routes for simple mutations.

```tsx
// action.ts
'use server'
export async function updateUser(id: string, data: FormData) {
  await db.user.update(...)
  revalidatePath('/profile')
}
```

## 3. State Management Decision Matrix

| State Type | Solution | Library |
|:---|:---|:---|
| **Server Data** | React Query / SWR | `@tanstack/react-query` |
| **Global Client** | Atomic Store | `Zustand` / `Jotai` |
| **Form State** | Uncontrolled | `react-hook-form` |
| **Local UI** | `useState` / `useReducer` | Native |

## 4. TypeScript Patterns

### Advanced Props
```tsx
// Polymorphic Component (render as 'a' or 'button')
type ButtonProps<T extends React.ElementType> = {
  as?: T;
  children: React.ReactNode;
} & React.ComponentPropsWithoutRef<T>;
```

### Discriminated Unions (The "State Machine" of Types)
```ts
type State = 
  | { status: 'idle' }
  | { status: 'loading' }
  | { status: 'success'; data: User }
  | { status: 'error'; error: Error };
```

## 5. Performance Checklist
- [ ] **Virtualization:** List > 100 items? Use `react-window`.
- [ ] **Code Splitting:** `import("dynamic")` for heavy charts/modals.
- [ ] **Stability:** `useCallback` on event handlers passed to optimized children.


## Related Skills
- [Identity](../sovereign-identity/SKILL.md): The core constraints.
- [Python Automation Expert](../python-automation-expert/SKILL.md)
- [Python Development](../python-development/SKILL.md)
- [Fastapi Expert](../fastapi-expert/SKILL.md)
