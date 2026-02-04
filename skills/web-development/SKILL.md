---
name: web-development
description: Modern web engineering standards (Tailwind, Vite, Accessibility).
---

# Web Development

> "Fast, Accessible, Beautiful."

## Activation Trigger
- "Create a website"
- "Fix CSS issues"
- "Build a dashboard"

## Protocols

### 1. First Principle: Semantic HTML
Use `<button>`, not `<div onClick>`. Accessibility is not optional.

### 2. The Tech Stack
- **Framework**: React + Vite (Fast HMR)
- **Styling**: Tailwind CSS (Utility-first)
- **Icons**: Lucide React (SVG)

### 3. Component Architecture
One component, one file. PascalCase.

## Code Patterns

### The Reusable Component
```tsx
interface ButtonProps {
  variant?: 'primary' | 'secondary';
  children: React.ReactNode;
}

export function Button({ variant = 'primary', children }: ButtonProps) {
  return (
    <button className={clsx(
      "px-4 py-2 rounded",
      variant === 'primary' ? "bg-blue-500" : "bg-gray-200"
    )}>
      {children}
    </button>
  );
}
```

## Safety Guardrails
- **No Console Errors**: Zero tolerance for React warnings.
- **Mobile First**: Design for small screens, scale up.
- **Type Safety**: No `any`. Use generic types.
- **Performance**: Images must have `alt` and be optimized.
- **Zero Layout Shift**: Reserve space for images/loaders.
