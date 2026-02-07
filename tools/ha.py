#!/usr/bin/env python3
"""
Home Assistant REST API CLI (local-first).

Auth:
  - HOME_ASSISTANT_URL (default: http://homeassistant.local:8123)
  - HOME_ASSISTANT_TOKEN (required)

Examples:
  python tools/ha.py states
  python tools/ha.py state --entity light.living_room
  python tools/ha.py call --domain light --service turn_on --data '{"entity_id":"light.living_room"}'
"""

from __future__ import annotations

import argparse
import json
import os
import sys
import urllib.error
import urllib.parse
import urllib.request
from typing import Any, Dict, Optional, Tuple


def die(msg: str, code: int = 2) -> "None":
    print(f"ERROR: {msg}", file=sys.stderr)
    raise SystemExit(code)


def env_bool(name: str, default: bool) -> bool:
    v = (os.environ.get(name) or "").strip().lower()
    if not v:
        return default
    return v in ("1", "true", "yes", "y", "on")


def ha_base_url() -> str:
    return (os.environ.get("HOME_ASSISTANT_URL") or "http://homeassistant.local:8123").rstrip("/")


def ha_token() -> str:
    tok = (os.environ.get("HOME_ASSISTANT_TOKEN") or "").strip()
    if not tok:
        die("HOME_ASSISTANT_TOKEN is required.")
    return tok


def request_json(method: str, path: str, body: Optional[Dict[str, Any]] = None, timeout: int = 20) -> Any:
    base = ha_base_url()
    url = base + path
    token = ha_token()

    data = None
    headers = {
        "Authorization": f"Bearer {token}",
        "Accept": "application/json",
    }
    if body is not None:
        data = json.dumps(body).encode("utf-8")
        headers["Content-Type"] = "application/json"

    req = urllib.request.Request(url, data=data, headers=headers, method=method)
    try:
        with urllib.request.urlopen(req, timeout=timeout) as resp:
            raw = resp.read()
            if not raw:
                return None
            return json.loads(raw.decode("utf-8"))
    except urllib.error.HTTPError as e:
        try:
            detail = e.read().decode("utf-8", errors="replace")
        except Exception:
            detail = str(e)
        die(f"HTTP {e.code} for {method} {url}: {detail}", code=3)
    except Exception as e:
        die(f"Request failed: {e}", code=4)


def cmd_states(_: argparse.Namespace) -> None:
    data = request_json("GET", "/api/states")
    print(json.dumps(data, indent=2))


def cmd_state(args: argparse.Namespace) -> None:
    entity = (args.entity or "").strip()
    if not entity:
        die("--entity is required")
    data = request_json("GET", f"/api/states/{urllib.parse.quote(entity)}")
    print(json.dumps(data, indent=2))


def cmd_call(args: argparse.Namespace) -> None:
    domain = (args.domain or "").strip()
    service = (args.service or "").strip()
    if not domain or not service:
        die("--domain and --service are required")
    body = {}
    if args.data:
        try:
            body = json.loads(args.data)
            if not isinstance(body, dict):
                die("--data must be a JSON object")
        except Exception as e:
            die(f"Invalid JSON for --data: {e}")

    data = request_json("POST", f"/api/services/{urllib.parse.quote(domain)}/{urllib.parse.quote(service)}", body=body)
    print(json.dumps(data, indent=2))


def cmd_toggle(args: argparse.Namespace) -> None:
    entity = (args.entity or "").strip()
    if not entity:
        die("--entity is required")
    # Best-effort domain inference.
    if "." not in entity:
        die("entity_id must be like 'light.kitchen'")
    domain = entity.split(".", 1)[0]
    # Many domains support toggle, but not all.
    body = {"entity_id": entity}
    data = request_json("POST", f"/api/services/{urllib.parse.quote(domain)}/toggle", body=body)
    print(json.dumps(data, indent=2))


def cmd_set_temp(args: argparse.Namespace) -> None:
    entity = (args.entity or "").strip()
    if not entity:
        die("--entity is required")
    temp = args.temp
    try:
        t = float(temp)
    except Exception:
        die("--temp must be numeric")
    body = {"entity_id": entity, "temperature": t}
    data = request_json("POST", "/api/services/climate/set_temperature", body=body)
    print(json.dumps(data, indent=2))


def main(argv: list[str]) -> int:
    p = argparse.ArgumentParser(prog="ha", add_help=True)
    sub = p.add_subparsers(dest="cmd", required=True)

    s = sub.add_parser("states", help="List all states")
    s.set_defaults(func=cmd_states)

    st = sub.add_parser("state", help="Get one entity state")
    st.add_argument("--entity", required=True)
    st.set_defaults(func=cmd_state)

    c = sub.add_parser("call", help="Call a Home Assistant service")
    c.add_argument("--domain", required=True)
    c.add_argument("--service", required=True)
    c.add_argument("--data", default="", help="JSON object string")
    c.set_defaults(func=cmd_call)

    t = sub.add_parser("toggle", help="Toggle an entity by entity_id")
    t.add_argument("--entity", required=True)
    t.set_defaults(func=cmd_toggle)

    ct = sub.add_parser("set-temp", help="Set climate temperature")
    ct.add_argument("--entity", required=True)
    ct.add_argument("--temp", required=True)
    ct.set_defaults(func=cmd_set_temp)

    args = p.parse_args(argv)
    args.func(args)
    return 0


if __name__ == "__main__":
    raise SystemExit(main(sys.argv[1:]))

