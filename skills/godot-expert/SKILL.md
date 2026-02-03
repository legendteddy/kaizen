---
name: godot-expert
description: Expert guidance for Godot 4.x game development.
---

# Godot Game Expert

Use this skill when the User wants to work on their Godot game.

## Vibe Check
-   **User Intent**: "Build a level", "Move the player", "Make a game".
-   **Goal**: Create high-performance, organized game code using Godot 4.x standards.

## Core Rules (The "Godot" Vibe)
1.  **Organization**: "Signals Up, Calls Down." Parents talk to children directly; children shout (signals) to parents.
2.  **Naming**: Use `snake_case` for files and variables. Use `PascalCase` for Nodes and Classes.
3.  **Typing**: Use Static Typing (e.g., `var health: int = 10`) for better performance and fewer bugs.
4.  **Simplicity**: If a simple visual trick works, don't build a complex simulation.

## Workflow
1.  **Scene Design**: Favor composition (adding small nodes together) over complex inheritance.
2.  **GDScript**: Follow the official style guide (Tabs for indentation, specific code order).
3.  **Optimization**: Only optimize when things get slow. Focus on readable code first.
