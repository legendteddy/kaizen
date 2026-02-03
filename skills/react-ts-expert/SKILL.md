---
name: react-ts-expert
description: Modern best practices for React 18+ with strict TypeScript integration.
---

# React TypeScript Expert
Modern best practices for React 18+ with strict TypeScript integration.

## Instructions
- **Components:**
  - Functional Components only (`const Comp = () => {}`).
  - PascalCase filenames matching component names.
- **Typing:**
  - Explicit `interface IProps` for all components.
  - No `any` type. Use `unknown` or specific Unions if unsure.
  - strict `tsconfig.json` settings enabled.
- **Hooks:**
  - Use custom hooks to separate logic from UI.
  - Follow `use` prefix convention.
- **State:**
  - Prefer `useReducer` for complex state objects.
  - Avoid large `useState` trees; split them up.

## Capabilities
- Can convert Class components to Functional.
- Can generate type-safe API hooks (TanStack Query/SWR).
- Can fix React "Prop Drilling" by implementing Context or Composition.