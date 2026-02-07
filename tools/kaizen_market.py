#!/usr/bin/env python3
"""
Kaizen Skill Marketplace (local-first)

Implements a simple `.kaizen` package format:
- A `.kaizen` file is a ZIP archive
- It must contain either:
  1) `<skill_dir>/SKILL.md` (recommended), optionally with other files under `<skill_dir>/...`
  2) `SKILL.md` at the ZIP root (will install into `skills/<name>/SKILL.md`)
- Optional `kaizen.json` manifest at ZIP root

Commands:
  - pack   : package a skill directory into a .kaizen zip
  - install: install a .kaizen into the local `skills/` directory
  - list   : list available packages from a local index JSON
  - install-index: install a package by name from a local index JSON
  - inspect: print manifest + discovered contents
"""

from __future__ import annotations

import argparse
import json
import os
import re
import shutil
import sys
import time
import zipfile
from dataclasses import dataclass
from pathlib import Path
from typing import Dict, List, Optional, Tuple


RE_SAFE_NAME = re.compile(r"^[a-z0-9][a-z0-9\\-]{1,62}[a-z0-9]$", re.IGNORECASE)


def _die(msg: str, code: int = 2) -> "None":
    print(f"ERROR: {msg}", file=sys.stderr)
    raise SystemExit(code)


def _read_json_optional(zf: zipfile.ZipFile, name: str) -> Optional[Dict]:
    try:
        with zf.open(name, "r") as f:
            return json.loads(f.read().decode("utf-8"))
    except KeyError:
        return None
    except Exception as e:
        _die(f"Failed to read {name}: {e}")


def _zip_names(zf: zipfile.ZipFile) -> List[str]:
    # Normalize to forward slashes.
    return [n.replace("\\", "/") for n in zf.namelist()]


def _is_path_traversal(name: str) -> bool:
    n = name.replace("\\", "/")
    return n.startswith("/") or n.startswith("../") or "/../" in n or n.endswith("/..")


@dataclass
class PackageLayout:
    manifest: Dict
    skill_dir_in_zip: Optional[str]  # e.g. "my-skill" or None when SKILL.md at root
    skill_name: str  # resolved final name
    files: List[str]  # zip entries that will be installed (normalized)


def _discover_layout(zf: zipfile.ZipFile, default_name: str) -> PackageLayout:
    names = _zip_names(zf)
    if any(_is_path_traversal(n) for n in names):
        _die("Package contains unsafe paths (path traversal).")

    manifest = _read_json_optional(zf, "kaizen.json") or {}

    # Find SKILL.md (root or under a single top-level dir).
    skill_md_root = "SKILL.md" if "SKILL.md" in names else None
    skill_md_paths = [n for n in names if n.endswith("/SKILL.md")]

    if skill_md_root and skill_md_paths:
        _die("Package contains multiple SKILL.md locations (root and subdir).")

    if not skill_md_root and not skill_md_paths:
        _die("Package missing SKILL.md.")

    if skill_md_root:
        skill_dir_in_zip = None
        skill_name = (manifest.get("name") or default_name).strip()
        files = [n for n in names if not n.endswith("/")]
    else:
        # Require exactly one SKILL.md under a top-level directory.
        if len(skill_md_paths) != 1:
            _die(f"Package must contain exactly one */SKILL.md (found {len(skill_md_paths)}).")

        skill_md = skill_md_paths[0]  # e.g. "my-skill/SKILL.md"
        parts = skill_md.split("/")
        if len(parts) < 2:
            _die("Invalid SKILL.md path.")
        skill_dir_in_zip = parts[0]
        skill_name = (manifest.get("name") or skill_dir_in_zip or default_name).strip()
        files = [n for n in names if n == skill_dir_in_zip or n.startswith(skill_dir_in_zip + "/")]
        files = [n for n in files if not n.endswith("/")]

    if not skill_name:
        _die("Could not determine skill name.")
    if not RE_SAFE_NAME.match(skill_name):
        _die(f"Invalid skill name '{skill_name}'. Use letters/numbers/hyphen, 3-64 chars.")

    return PackageLayout(
        manifest=manifest,
        skill_dir_in_zip=skill_dir_in_zip,
        skill_name=skill_name,
        files=sorted(set(files)),
    )


def cmd_inspect(args: argparse.Namespace) -> None:
    pkg = Path(args.package)
    if not pkg.exists():
        _die(f"Not found: {pkg}")

    with zipfile.ZipFile(pkg, "r") as zf:
        layout = _discover_layout(zf, default_name=pkg.stem)
        out = {
            "package": str(pkg),
            "skill_name": layout.skill_name,
            "skill_dir_in_zip": layout.skill_dir_in_zip,
            "manifest": layout.manifest,
            "file_count": len(layout.files),
            "files": layout.files[:50],
            "files_truncated": max(0, len(layout.files) - 50),
        }
        print(json.dumps(out, indent=2))


def cmd_pack(args: argparse.Namespace) -> None:
    src_dir = Path(args.skill_dir)
    if not src_dir.exists() or not src_dir.is_dir():
        _die(f"Not a directory: {src_dir}")

    skill_md = src_dir / "SKILL.md"
    if not skill_md.exists():
        _die(f"Missing SKILL.md: {skill_md}")

    skill_name = args.name.strip() if args.name else src_dir.name
    if not RE_SAFE_NAME.match(skill_name):
        _die(f"Invalid skill name '{skill_name}'. Use letters/numbers/hyphen, 3-64 chars.")

    out_path = Path(args.out) if args.out else Path(f"{skill_name}.kaizen")
    out_path.parent.mkdir(parents=True, exist_ok=True)

    manifest = {
        "name": skill_name,
        "version": args.version or "0.0.1",
        "description": args.description or "",
        "author": args.author or "",
        "created_at": time.strftime("%Y-%m-%dT%H:%M:%S"),
        "format": "kaizen-skill-zip-v1",
    }

    # Always pack as `<skill_name>/...` to avoid collisions.
    with zipfile.ZipFile(out_path, "w", compression=zipfile.ZIP_DEFLATED) as zf:
        zf.writestr("kaizen.json", json.dumps(manifest, indent=2))
        for path in src_dir.rglob("*"):
            if path.is_dir():
                continue
            rel = path.relative_to(src_dir).as_posix()
            arcname = f"{skill_name}/{rel}"
            zf.write(path, arcname)

    print(f"OK: wrote {out_path}")


def _backup_dir(target_dir: Path) -> Optional[Path]:
    if not target_dir.exists():
        return None
    ts = time.strftime("%Y%m%d-%H%M%S")
    backup = target_dir.with_name(target_dir.name + f".bak-{ts}")
    shutil.move(str(target_dir), str(backup))
    return backup


def cmd_install(args: argparse.Namespace) -> None:
    pkg = Path(args.package)
    if not pkg.exists():
        _die(f"Not found: {pkg}")

    repo_root = Path(args.root).resolve() if args.root else Path.cwd().resolve()
    skills_root = (repo_root / "skills").resolve()
    if not skills_root.exists():
        _die(f"skills/ directory not found at: {skills_root}")

    with zipfile.ZipFile(pkg, "r") as zf:
        layout = _discover_layout(zf, default_name=pkg.stem)
        target_dir = (skills_root / layout.skill_name).resolve()

        # Ensure we only write under skills_root
        if skills_root not in target_dir.parents and skills_root != target_dir:
            _die("Refusing to install outside skills/ directory.")

        backup = _backup_dir(target_dir)
        target_dir.mkdir(parents=True, exist_ok=True)

        for name in layout.files:
            if _is_path_traversal(name):
                _die("Refusing to extract unsafe path.")

            # Compute destination relative path.
            if layout.skill_dir_in_zip:
                rel = name[len(layout.skill_dir_in_zip) + 1 :] if name.startswith(layout.skill_dir_in_zip + "/") else ""
            else:
                rel = name
            if not rel:
                continue

            dest = (target_dir / rel).resolve()
            if target_dir not in dest.parents and target_dir != dest:
                _die("Refusing to write outside target skill directory.")

            dest.parent.mkdir(parents=True, exist_ok=True)
            with zf.open(name, "r") as src, open(dest, "wb") as out:
                shutil.copyfileobj(src, out)

        meta = {
            "installed_from": str(pkg),
            "installed_at": time.strftime("%Y-%m-%dT%H:%M:%S"),
            "manifest": layout.manifest,
        }
        (target_dir / ".kaizen-install.json").write_text(json.dumps(meta, indent=2), encoding="utf-8")

        msg = f"OK: installed {layout.skill_name} -> {target_dir}"
        if backup:
            msg += f" (backup: {backup})"
    print(msg)


def _load_index(path: Path) -> Dict:
    if not path.exists():
        _die(f"Index not found: {path}")
    try:
        return json.loads(path.read_text(encoding="utf-8"))
    except Exception as e:
        _die(f"Failed to read index: {e}")


def cmd_list(args: argparse.Namespace) -> None:
    idx = _load_index(Path(args.index))
    pkgs = idx.get("packages") or []
    if args.json:
        print(json.dumps({"packages": pkgs}, indent=2))
        return

    if not pkgs:
        print("No packages.")
        return

    for p in pkgs:
        name = p.get("name", "")
        ver = p.get("version", "")
        desc = p.get("description", "")
        print(f"- {name} {ver} :: {desc}")


def cmd_install_index(args: argparse.Namespace) -> None:
    idx_path = Path(args.index)
    idx = _load_index(idx_path)
    name = (args.name or "").strip()
    if not name:
        _die("--name is required")

    pkgs = idx.get("packages") or []
    match = None
    for p in pkgs:
        if str(p.get("name", "")).strip().lower() == name.lower():
            match = p
            break
    if not match:
        _die(f"Package not found in index: {name}")

    file_rel = str(match.get("file", "")).strip()
    if not file_rel:
        _die(f"Index entry missing 'file' for: {name}")

    pkg_path = (idx_path.parent / file_rel).resolve()
    # Delegate to install.
    install_args = argparse.Namespace(package=str(pkg_path), root=args.root)
    cmd_install(install_args)


def main(argv: List[str]) -> int:
    p = argparse.ArgumentParser(prog="kaizen_market", add_help=True)
    sub = p.add_subparsers(dest="cmd", required=True)

    p_ins = sub.add_parser("inspect", help="Inspect a .kaizen package")
    p_ins.add_argument("package")
    p_ins.set_defaults(func=cmd_inspect)

    p_pack = sub.add_parser("pack", help="Pack a skill directory into a .kaizen package")
    p_pack.add_argument("skill_dir")
    p_pack.add_argument("--name", default="")
    p_pack.add_argument("--version", default="")
    p_pack.add_argument("--description", default="")
    p_pack.add_argument("--author", default="")
    p_pack.add_argument("--out", default="")
    p_pack.set_defaults(func=cmd_pack)

    p_inst = sub.add_parser("install", help="Install a .kaizen package into skills/")
    p_inst.add_argument("package")
    p_inst.add_argument("--root", default="", help="Repo root (defaults to cwd)")
    p_inst.set_defaults(func=cmd_install)

    p_list = sub.add_parser("list", help="List packages from a local index json")
    p_list.add_argument("--index", default="marketplace/index.json")
    p_list.add_argument("--json", action="store_true")
    p_list.set_defaults(func=cmd_list)

    p_inst_idx = sub.add_parser("install-index", help="Install a package by name using a local index json")
    p_inst_idx.add_argument("--name", required=True)
    p_inst_idx.add_argument("--index", default="marketplace/index.json")
    p_inst_idx.add_argument("--root", default="", help="Repo root (defaults to cwd)")
    p_inst_idx.set_defaults(func=cmd_install_index)

    args = p.parse_args(argv)
    args.func(args)
    return 0


if __name__ == "__main__":
    raise SystemExit(main(sys.argv[1:]))
