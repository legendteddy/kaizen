---
name: godot-expert
description: Expert protocols for Godot 4.x development (GDScript, Nodes, Architecture).
---

# Godot Expert

> "Signals Up, Calls Down."

## Activation Trigger
- Developing Godot (4.x) games or tools.
- Writing GDScript code.
- Designing game architecture (Nodes/Scenes).

## Architecture Principles

### 1. Communication Flow
- **Down:** Use function calls. Parents call methods on children.
  - `child.do_thing()`
- **Up:** Use Signals. Children emit signals; parents connect to them.
  - `child.emit_signal("thing_done")` -> `parent._on_child_thing_done()`
- **Sideways:** Use Signals or a shared Autoload (Global). Never `get_node("../../Sibling")`.

### 2. Composition Over Inheritance
- **Don't** create deep class hierarchies (`Enemy` -> `FlyingEnemy` -> `BossFlyingEnemy`).
- **Do** use Components (Nodes).
  - Add a `HealthComponent` node to handle health.
  - Add a `HitboxComponent` node to handle collisions.
- This makes scenes modular and reusable.

## GDScript Best Practices (Godot 4.x)

### Static Typing
Always use static typing for performance and safety.
```gdscript
# Bad
var health = 100
func take_damage(amount):
    health -= amount

# Good
var health: int = 100
func take_damage(amount: int) -> void:
    health -= amount
```

### Lifecycle Checks
- `_ready()`: Setup logic. Access children here (they are guaranteed ready).
- `_physics_process(delta)`: Movement, collision, reliable timing. Use `delta`.
- `_process(delta)`: UI updates, visual effects. Variable timing.

### Godot 4 Specifics
- **Tweens:** Use `create_tween()`. Forget `Tween` node.
- **Callables:** `connect("signal", self, "method")` is dead. Use `signal.connect(method)`.
- **Exports:** Use `@export` annotation. `@export var speed: float = 10.0`.

## Common Pitfalls (Anti-Patterns)
- **The "God Node":** Putting all logic in the root script. Break it down.
- **Hardcoded Paths:** `get_node("Node2D/Sprite")`. Use `@onready` vars or `%UniqueName`.
  - `@onready var sprite: Sprite2D = $Sprite2D` 
- **Physics in Process:** Moving `CharacterBody` in `_process` causes jitter. Use `_physics_process`.

## Debugging Check
- Is the signal actually connected? (Check logic or UI icons).
- Is `delta` being applied to movement? (If not, framerate affects speed).
- Is the script attached to the right node?

## Self-Improvement
- Did I write a hardcoded path? -> Use `%UniqueName` next time.
- Did a signal fail? -> Check signal syntax (Godot 4 vs 3).


## Action Checklist
- [ ] **Context:** Have I read the necessary files?
- [ ] **Protocol:** Did I follow the steps above?
- [ ] **Safety:** Is the action reversible?
- [ ] **Quality:** Does the output meet Standard Standards?


## Related Skills
- [Agent Identity](../agent-identity/SKILL.md)
- [Python Automation Expert](../python-automation-expert/SKILL.md)
- [Python Development](../python-development/SKILL.md)
- [React Ts Expert](../react-ts-expert/SKILL.md)
