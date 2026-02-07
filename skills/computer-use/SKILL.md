---
name: computer-use
description: Skill for controlling the cursor and keyboard to automate GUI tasks (Anthropic/OpenAI Computer Use).
---

# Protocol: Computer Use Automation (v1.0)

> "The hands of the agent."

## Purpose
Guide the agent on how to effectively use "Computer Use" tools (screenshot -> coordinate -> click) without getting lost or stuck.

## Activation Trigger
- User asks to "click," "type," "open browser," or "navigate."
- Tasks that cannot be done via API/Terminal (e.g., "Log into this legacy website").

---

## Local Tooling (Kaizen Repo)

This repo includes a conservative Windows helper that uses PowerShell/.NET (no extra Python deps):

```powershell
# take a screenshot
python tools\computer_use.py screenshot --out C:\Users\thoma\Documents\kaizen\dist\screenshot.png

# click/type require explicit confirmation
python tools\computer_use.py click 500 500 --confirm
python tools\computer_use.py type "hello" --confirm
```

Safety: `click/type/key` refuse to run without `--confirm`.

## Protocol: The "See-Think-Click" Loop

### 1. SEE (Screenshot)
**Action:** Take a screenshot of the current state.
**Guard:** Verify the screenshot is not black/blank.

### 2. THINK (Coordinate Mapping)
**Action:** Identify the XY coordinates of the target element.
**Heuristic:** "Center of the button," not the edge.

### 3. CLICK (Action)
**Action:** Move cursor and click.
**Guard:** Wait 500ms after clicking for UI to react.

### 4. VERIFY (Did it work?)
**Action:** Take another screenshot.
**Check:** Did the screen change? If not, retry with slightly different coordinates.

---

## Protocol: Resilience

| Failure Mode | Fix |
|:---|:---|
| **Popup Blocker** | Always look for "X" or "Close" icons first. |
| **Loading Spinner** | Loop: "Wait 1s -> Screenshot" until spinner is gone. |
| **Ambiguous UI** | Use "Computer Use" + "Keyboard" (Ctrl+F) to highlight text. |

---

## Example: Login Flow

```python
def login(username, password):
    # 1. Focus
    computer.click(element="Username Field")
    
    # 2. Type
    computer.type(username)
    computer.key("Tab") # Move to password
    
    # 3. Secure Type
    computer.type(password)
    computer.key("Enter")
    
    # 4. Verify
    screen = computer.screenshot()
    if "Dashboard" not in ocr(screen):
        raise LoginError("Failed to login")
```

## Action Checklist
- [ ] **See:** Did you take a screenshot before acting?
- [ ] **Think:** Are coordinates centered on the element?
- [ ] **Click:** Did you wait 500ms after action?
- [ ] **Verify:** Did the screen change state?
- [ ] **Rescue:** If stuck, did you try keyboard shortcuts (Tab/Enter)?


## Related Skills
- [Agent Identity](../agent-identity/SKILL.md)
