---
name: design-architect
description: Establishing premium visual systems (Tokens, Hierarchy, Glassmorphism).
---

# Protocol: Design Architect (Visual Systems)

> "Design is not just what it looks like. Design is how it feels."

## Activation Trigger
- "Make it look premium"
- "Fix the aesthetics"
- "Update the design system"
- "It looks cheap"

## Protocols

### 1. First Principle: Tokenization
Never use raw hex codes (e.g., `#FFD700`) in component files. Define them in `:root` variables first.
*   **Correct**: `color: var(--gold-primary)`
*   **Wrong**: `color: #FFD700`

### 2. High-Fidelity Theming (The "Trillion Dollar" Standard)
For premium interfaces, flat colors are insufficient. Use **Texture Layers**:
1.  **Base**: Semi-transparent background (`rgba`).
2.  **Blur**: `backdrop-filter: blur()`.
3.  **Border**: Subtle, lighter than background.
4.  **Highlight**: Inner/Outer shadows or Shine effects.

### 3. Visual Hierarchy
Every page must have:
*   **One Primary Action**: The "Hero" button (e.g., Solid/Glass Gold).
*   **Secondary Actions**: Outlined or Muted buttons.
*   **Tertiary Actions**: Text links.
*   *Never compete for attention.*

## Code Patterns

### The "Glassmorphism" Token Set
```css
:root {
    --glass-bg: rgba(255, 255, 255, 0.05);
    --glass-border: 1px solid rgba(255, 255, 255, 0.1);
    --glass-blur: blur(10px);
    --glass-shadow: 0 4px 30px rgba(0, 0, 0, 0.1);
}

.card-glass {
    background: var(--glass-bg);
    border: var(--glass-border);
    backdrop-filter: var(--glass-blur);
    box-shadow: var(--glass-shadow);
}
```

### The "Premium Button" (CSS)
```css
.btn-premium {
    position: relative;
    overflow: hidden; /* For shine effect */
    transition: all 0.4s cubic-bezier(0.25, 1, 0.5, 1);
}

/* Shine Animation */
.btn-premium::after {
    content: '';
    position: absolute;
    top: 0;
    left: -100%;
    width: 100%;
    height: 100%;
    background: linear-gradient(90deg, transparent, rgba(255,255,255,0.2), transparent);
    transition: 0.5s;
}

.btn-premium:hover::after {
    left: 100%;
}
```

## Safety Guardrails
- **Contrast Ratios**: Gold text on White background often fails WCAG. Use darker golds or black backgrounds.
- **Performance**: Excessive `backdrop-filter` breaks mobile GPUs. Use sparingly or disable on mobile.
- **Hit Areas**: All interactive elements must be at least 44x44px.
