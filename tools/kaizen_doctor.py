#!/usr/bin/env python3
"""
Kaizen Doctor - local diagnostics for Sovereign Kaizen.

Checks:
- Engine health endpoints
- Dashboard port
- MCP port (optional)
"""

from __future__ import annotations

import argparse
import json
import socket
import sys
import urllib.error
import urllib.request
from typing import Any, Dict, Optional, Tuple


def http_get_json(url: str, timeout: int = 2) -> Tuple[bool, Any, str]:
    try:
        req = urllib.request.Request(url, headers={"Accept": "application/json"})
        with urllib.request.urlopen(req, timeout=timeout) as resp:
            raw = resp.read()
            if not raw:
                return True, None, ""
            return True, json.loads(raw.decode("utf-8")), ""
    except urllib.error.HTTPError as e:
        try:
            body = e.read().decode("utf-8", errors="replace")
        except Exception:
            body = ""
        return False, None, f"HTTP {e.code}: {body[:200]}"
    except Exception as e:
        return False, None, str(e)


def port_open(host: str, port: int, timeout: float = 0.5) -> bool:
    try:
        with socket.create_connection((host, port), timeout=timeout):
            return True
    except Exception:
        return False


def main(argv: list[str]) -> int:
    ap = argparse.ArgumentParser(prog="kaizen_doctor", add_help=True)
    ap.add_argument("--engine", default="http://localhost:8787")
    ap.add_argument("--dashboard-port", type=int, default=5173)
    ap.add_argument("--mcp-port", type=int, default=8791)
    ap.add_argument("--timeout", type=float, default=2.0)
    args = ap.parse_args(argv)

    engine = args.engine.rstrip("/")
    timeout = float(args.timeout)

    ok_engine_port = port_open("127.0.0.1", 8787, timeout=0.5)
    ok_dash_port = port_open("127.0.0.1", int(args.dashboard_port), timeout=0.5)
    ok_mcp_port = port_open("127.0.0.1", int(args.mcp_port), timeout=0.5)

    print("Kaizen Doctor")
    print("")
    print(f"- Engine port 8787: {'OK' if ok_engine_port else 'NO'}")
    print(f"- Dashboard port {int(args.dashboard_port)}: {'OK' if ok_dash_port else 'NO'}")
    print(f"- MCP port {int(args.mcp_port)}: {'OK' if ok_mcp_port else 'NO'}")
    print("")

    ok, data, err = http_get_json(f"{engine}/health", timeout=int(timeout))
    print(f"/health: {'OK' if ok else 'FAIL'}")
    if ok:
        print(json.dumps(data, indent=2)[:1200])
    else:
        print(f"  error: {err}")
    print("")

    ok, data, err = http_get_json(f"{engine}/capabilities", timeout=int(timeout))
    print(f"/capabilities: {'OK' if ok else 'FAIL'}")
    if ok:
        # Show a compact subset.
        features = (data or {}).get("features") if isinstance(data, dict) else None
        paths = (data or {}).get("paths") if isinstance(data, dict) else None
        print(json.dumps({"features": features, "paths": paths}, indent=2)[:1200])
    else:
        print(f"  error: {err}")
    print("")

    ok, data, err = http_get_json(f"{engine}/marketplace/index", timeout=int(timeout))
    print(f"/marketplace/index: {'OK' if ok else 'FAIL'}")
    if ok and isinstance(data, dict):
        pkgs = data.get("packages") or []
        print(f"  packages: {len(pkgs)}")
        for p in pkgs[:10]:
            name = p.get("name", "")
            ver = p.get("version", "")
            print(f"  - {name} {ver}".rstrip())
        if len(pkgs) > 10:
            print("  ...")
    else:
        print(f"  error: {err}")
    print("")

    ok, data, err = http_get_json(f"{engine}/learning/status", timeout=int(timeout))
    print(f"/learning/status: {'OK' if ok else 'FAIL'}")
    if ok and isinstance(data, dict):
        enabled = data.get("enabled")
        overrides = data.get("overrides") or []
        print(f"  adaptive_prompts_enabled: {bool(enabled)}")
        print(f"  overrides: {len(overrides)}")
    else:
        print(f"  error: {err}")

    return 0


if __name__ == "__main__":
    raise SystemExit(main(sys.argv[1:]))
