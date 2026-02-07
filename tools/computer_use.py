#!/usr/bin/env python3
"""
Computer Use (Windows) - minimal GUI automation helpers.

This is intentionally conservative:
- screenshot is always allowed
- click/type/key require an explicit --confirm flag

Implementation uses PowerShell/.NET to avoid extra Python deps.
"""

from __future__ import annotations

import argparse
import os
import subprocess
import sys
from pathlib import Path


def die(msg: str, code: int = 2) -> "None":
    print(f"ERROR: {msg}", file=sys.stderr)
    raise SystemExit(code)


def run_ps(script: str, timeout: int = 30) -> subprocess.CompletedProcess:
    cmd = [
        "powershell",
        "-NoProfile",
        "-NonInteractive",
        "-ExecutionPolicy",
        "Bypass",
        "-Command",
        script,
    ]
    return subprocess.run(cmd, capture_output=True, text=True, encoding="utf-8", errors="replace", timeout=timeout)


def cmd_screenshot(args: argparse.Namespace) -> None:
    out = Path(args.out).resolve()
    out.parent.mkdir(parents=True, exist_ok=True)
    # Note: System.Drawing.Common is Windows-only on modern runtimes; PowerShell 5.1
    # on Windows still supports this usage.
    script = rf"""
$ErrorActionPreference = "Stop"
Add-Type -AssemblyName System.Windows.Forms
Add-Type -AssemblyName System.Drawing
$bounds = [System.Windows.Forms.Screen]::PrimaryScreen.Bounds
$bmp = New-Object System.Drawing.Bitmap $bounds.Width, $bounds.Height
$g = [System.Drawing.Graphics]::FromImage($bmp)
$g.CopyFromScreen($bounds.Location, [System.Drawing.Point]::Empty, $bounds.Size)
$bmp.Save("{str(out).replace('"','""')}", [System.Drawing.Imaging.ImageFormat]::Png)
$g.Dispose()
$bmp.Dispose()
""".strip()

    r = run_ps(script, timeout=30)
    if r.returncode != 0:
        die((r.stderr or r.stdout).strip(), code=3)
    print(f"OK: wrote {out}")


def _require_confirm(args: argparse.Namespace) -> None:
    if not bool(args.confirm):
        die("Refusing to act without --confirm (dry-run safety).")


def cmd_click(args: argparse.Namespace) -> None:
    _require_confirm(args)
    x = int(args.x)
    y = int(args.y)
    script = rf"""
$ErrorActionPreference = "Stop"
Add-Type -TypeDefinition @"
using System;
using System.Runtime.InteropServices;
public static class Mouse {{
  [DllImport("user32.dll")] public static extern bool SetCursorPos(int X, int Y);
  [DllImport("user32.dll")] public static extern void mouse_event(int dwFlags, int dx, int dy, int cButtons, int dwExtraInfo);
}}
"@
[Mouse]::SetCursorPos({x},{y}) | Out-Null
# left down/up
[Mouse]::mouse_event(0x02, 0, 0, 0, 0)
Start-Sleep -Milliseconds 50
[Mouse]::mouse_event(0x04, 0, 0, 0, 0)
""".strip()
    r = run_ps(script, timeout=10)
    if r.returncode != 0:
        die((r.stderr or r.stdout).strip(), code=3)
    print(f"OK: clicked {x},{y}")


def cmd_type(args: argparse.Namespace) -> None:
    _require_confirm(args)
    text = args.text or ""
    # Escape for PowerShell single-quoted string.
    t = text.replace("'", "''")
    script = rf"""
$ErrorActionPreference = "Stop"
Add-Type -AssemblyName System.Windows.Forms
[System.Windows.Forms.SendKeys]::SendWait('{t}')
""".strip()
    r = run_ps(script, timeout=10)
    if r.returncode != 0:
        die((r.stderr or r.stdout).strip(), code=3)
    print("OK: typed")


def cmd_key(args: argparse.Namespace) -> None:
    _require_confirm(args)
    key = (args.key or "").strip()
    if not key:
        die("--key is required")
    k = key.replace("'", "''")
    script = rf"""
$ErrorActionPreference = "Stop"
Add-Type -AssemblyName System.Windows.Forms
[System.Windows.Forms.SendKeys]::SendWait('{k}')
""".strip()
    r = run_ps(script, timeout=10)
    if r.returncode != 0:
        die((r.stderr or r.stdout).strip(), code=3)
    print("OK: key sent")


def main(argv: list[str]) -> int:
    p = argparse.ArgumentParser(prog="computer_use", add_help=True)
    sub = p.add_subparsers(dest="cmd", required=True)

    s = sub.add_parser("screenshot", help="Capture a PNG screenshot of the primary screen")
    s.add_argument("--out", default=str(Path.cwd() / "screenshot.png"))
    s.set_defaults(func=cmd_screenshot)

    c = sub.add_parser("click", help="Click at screen coordinates (requires --confirm)")
    c.add_argument("x")
    c.add_argument("y")
    c.add_argument("--confirm", action="store_true")
    c.set_defaults(func=cmd_click)

    t = sub.add_parser("type", help="Type text via SendKeys (requires --confirm)")
    t.add_argument("text")
    t.add_argument("--confirm", action="store_true")
    t.set_defaults(func=cmd_type)

    k = sub.add_parser("key", help="Send a key chord via SendKeys (example: ^l, {ENTER}) (requires --confirm)")
    k.add_argument("key")
    k.add_argument("--confirm", action="store_true")
    k.set_defaults(func=cmd_key)

    args = p.parse_args(argv)
    args.func(args)
    return 0


if __name__ == "__main__":
    raise SystemExit(main(sys.argv[1:]))
