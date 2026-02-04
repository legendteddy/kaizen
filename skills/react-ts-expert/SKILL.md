---
name: react-ts-expert
description: Protocols for React 19, Server Components, TypeScript, and State Management.
---

# React TypeScript Expert

> "UI is a function of State."

## Activation Trigger
- Building React components (Client or Server).
- Managing complex state (Zustand/Context).
- Optimizing frontend performance.

## Protocols

### 1. First Principle: Render on Server, Interact on Client
Move as much logic to the server (`async function`) as possible.

### 2. React 19 Pattern (RSC)
No more `useEffect` for data fetching.
```tsx
// Server Component
async function UserProfile({ id }) {
  const user = await db.user.find(id);
  return <ClientButton user={user} />;
}
```

### 3. State Management Matrix
- **Server Data**: Use `React Query` or Server Components.
- **Global UI**: Use `Zustand` (Atomic).
- **Form State**: Use `react-hook-form` (Uncontrolled).
- **Local State**: Use `useState`.

## Code Patterns

### Strictly Typed Props
```tsx
type Props<T> = {
  data: T;
  renderItem: (item: T) => React.ReactNode;
};
```

### Server Actions
```tsx
'use server'
export async function update(formData: FormData) {
  await db.save(formData);
  revalidatePath('/profile');
}
```

## Safety Guardrails
- **No useEffect for Data**: Banned. Use Server Components or React Query.
- **No Prop Drilling**: Max 2 levels. Use Context or Composition.
- **Responsive Check**: Always verify mobile layout (375px).
- **Accessibility**: All interactive elements need `aria-label`.
- **Key Stability**: Never use `index` as key in lists.
