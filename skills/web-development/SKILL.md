---
name: web-development
description: Skill for web-development tasks and workflows.
---

# Skill: Web Development (v1.0)

> Modern, component-driven, and accessible web engineering.

## Purpose
Build production-grade web interfaces using React, Tailwind, and Vite.

## Activation Trigger
- User mentions: "website," "web app," "frontend," "dashboard"
- Task involves HTML/CSS/JS generation.

---

## Protocol: The Stack

| Layer | Choice | Rationale |
|:---|:---|:---|
| **Framework** | React + Vite | Fast HMR, massive ecosystem |
| **Language** | TypeScript | Prevents 90% of runtime errors |
| **Styling** | Tailwind CSS | Colocated styles, design system tokens |
| **Icons** | Lucide React | Clean, consistent SVG icons |

---

## Protocol: Component Implementation

### 1. Component Structure
**Rule:** One component per file. PascalCase naming.

```tsx
// src/components/Button.tsx
import { ReactNode } from 'react';

interface ButtonProps {
  children: ReactNode;
  variant?: 'primary' | 'secondary';
  onClick?: () => void;
}

export function Button({ children, variant = 'primary', onClick }: ButtonProps) {
  const baseStyles = "px-4 py-2 rounded-md font-medium transition-colors";
  const variants = {
    primary: "bg-blue-600 text-white hover:bg-blue-700",
    secondary: "bg-gray-200 text-gray-900 hover:bg-gray-300"
  };

  return (
    <button 
      className={`${baseStyles} ${variants[variant]}`}
      onClick={onClick}
    >
      {children}
    </button>
  );
}
```

### 2. State Management
**Rule:** Use `useState` for local, `Zustand` for global. Avoid Redux unless requested.

### 3. File Organization
```
src/
├── components/   # Reusable UI atoms (Button, Card)
├── features/     # Domain specific logic (Auth, Dashboard)
├── hooks/        # Custom React hooks
└── lib/          # Utilities (API clients, formatters)
```

---

## Checklist: Before Shipping

- [ ] **Mobile Responsive**: Does it work on 375px width?
- [ ] **Accessibility**: Are `aria-labels` used on icon buttons?
- [ ] **Clean Console**: No React unique key warnings?
- [ ] **Type Check**: `tsc --noEmit` passes?