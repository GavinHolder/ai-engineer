#!/usr/bin/env python3
"""
Universal Skill Version Updater

Scans all skills with a versions.json, checks npm/PyPI for latest versions,
and updates SKILL.md version references.

Usage:
    python scripts/update-skills.py              # Interactive: choose what to update
    python scripts/update-skills.py --check      # Check only, no changes
    python scripts/update-skills.py --auto       # Auto-update all to latest
    python scripts/update-skills.py --skill react-19  # Update specific skill only

Supports both npm and PyPI registries (auto-detected from versions.json).
"""

import json
import re
import sys
import urllib.request
from datetime import date
from pathlib import Path
from typing import Optional


# ---------------------------------------------------------------------------
# Configuration
# ---------------------------------------------------------------------------

SCRIPT_DIR = Path(__file__).parent
REPO_ROOT = SCRIPT_DIR.parent
SKILLS_DIR = REPO_ROOT / "skills"

NPM_URL = "https://registry.npmjs.org/{package}/latest"
PYPI_URL = "https://pypi.org/pypi/{package}/json"
PYTHON_VERSIONS_URL = "https://www.python.org/api/v2/downloads/release/?is_published=true"


# ---------------------------------------------------------------------------
# Discovery
# ---------------------------------------------------------------------------

def find_versioned_skills() -> list[dict]:
    """Find all skills that have a versions.json file."""
    skills = []
    for versions_file in sorted(SKILLS_DIR.glob("*/versions.json")):
        skill_dir = versions_file.parent
        skill_name = skill_dir.name
        skill_file = skill_dir / "SKILL.md"

        try:
            data = json.loads(versions_file.read_text(encoding="utf-8"))
        except (json.JSONDecodeError, OSError) as e:
            print(f"  WARNING: Could not read {versions_file}: {e}")
            continue

        skills.append({
            "name": skill_name,
            "dir": skill_dir,
            "versions_file": versions_file,
            "skill_file": skill_file,
            "data": data,
            "registry": data.get("registry", "pypi"),
        })

    return skills


# ---------------------------------------------------------------------------
# Version fetching
# ---------------------------------------------------------------------------

def fetch_npm_version(package_name: str) -> Optional[str]:
    """Fetch latest version from npm registry."""
    try:
        url = NPM_URL.format(package=package_name)
        req = urllib.request.Request(url, headers={"Accept": "application/json"})
        with urllib.request.urlopen(req, timeout=10) as resp:
            data = json.loads(resp.read())
            return data.get("version")
    except Exception:
        return None


def fetch_pypi_version(package_name: str) -> Optional[str]:
    """Fetch latest version from PyPI."""
    try:
        url = PYPI_URL.format(package=package_name)
        req = urllib.request.Request(url, headers={"Accept": "application/json"})
        with urllib.request.urlopen(req, timeout=10) as resp:
            data = json.loads(resp.read())
            return data["info"]["version"]
    except Exception:
        return None


def fetch_latest_python_version() -> Optional[str]:
    """Fetch latest stable Python version from python.org API."""
    try:
        req = urllib.request.Request(
            PYTHON_VERSIONS_URL,
            headers={"Accept": "application/json"},
        )
        with urllib.request.urlopen(req, timeout=10) as resp:
            data = json.loads(resp.read())
            stable = []
            for release in data:
                name = release.get("name", "")
                match = re.match(r"Python (\d+\.\d+\.\d+)$", name)
                if match:
                    stable.append(match.group(1))
            if stable:
                stable.sort(
                    key=lambda v: tuple(int(x) for x in v.split(".")),
                    reverse=True,
                )
                return stable[0]
    except Exception:
        pass
    return None


def fetch_version(package_name: str, registry: str, pkg_info: dict) -> Optional[str]:
    """Fetch latest version from the appropriate registry."""
    if package_name == "Python":
        return fetch_latest_python_version()

    if registry == "npm":
        npm_name = pkg_info.get("npm", package_name)
        return fetch_npm_version(npm_name)
    else:
        pypi_name = pkg_info.get("pypi", package_name)
        return fetch_pypi_version(pypi_name)


# ---------------------------------------------------------------------------
# Version comparison
# ---------------------------------------------------------------------------

def parse_version(v: str) -> tuple:
    """Parse version string into comparable tuple."""
    parts = []
    for p in v.split("."):
        try:
            parts.append(int(p))
        except ValueError:
            parts.append(p)
    return tuple(parts)


def is_newer(latest: str, tracked: str) -> bool:
    """Check if latest version is newer than tracked."""
    try:
        return parse_version(latest) > parse_version(tracked)
    except (TypeError, ValueError):
        return latest != tracked


def check_skill(skill: dict) -> list[dict]:
    """Check all packages in a skill for updates. Returns list of updates."""
    packages = skill["data"].get("packages", {})
    registry = skill["registry"]
    updates = []

    for name, info in packages.items():
        tracked_ver = info.get("version", "?")
        latest_ver = fetch_version(name, registry, info)

        if latest_ver is None:
            status = "ERROR"
            latest_ver = "?"
        elif is_newer(latest_ver, tracked_ver):
            status = "UPDATE"
        else:
            status = "OK"

        marker = ">>" if status == "UPDATE" else "  "
        print(f"  {marker} {name:<35} {tracked_ver:<12} {latest_ver:<12} {status}")

        if status == "UPDATE":
            updates.append({
                "name": name,
                "tracked": tracked_ver,
                "latest": latest_ver,
                "docs_url": info.get("docs_url", ""),
                "role": info.get("role", ""),
            })

    return updates


# ---------------------------------------------------------------------------
# Updating files
# ---------------------------------------------------------------------------

def update_versions_json(skill: dict, updates: list[dict]) -> None:
    """Update versions.json with new versions."""
    data = skill["data"]
    packages = data["packages"]

    for upd in updates:
        if upd["name"] in packages:
            packages[upd["name"]]["version"] = upd["latest"]

    data["last_updated"] = date.today().isoformat()

    with open(skill["versions_file"], "w", encoding="utf-8") as f:
        json.dump(data, f, indent=2, ensure_ascii=False)
        f.write("\n")


def update_skill_md(skill: dict, updates: list[dict]) -> None:
    """Update version references in SKILL.md."""
    skill_file = skill["skill_file"]
    if not skill_file.exists():
        return

    content = skill_file.read_text(encoding="utf-8")

    for upd in updates:
        old_ver = re.escape(upd["tracked"])
        new_ver = upd["latest"]

        # Replace version in table rows: | Package | old_version | ... |
        pattern = re.compile(
            r"(\|\s*" + re.escape(upd["name"]) + r"\s*\|\s*)" +
            old_ver + r"(\s*\|)"
        )
        content = pattern.sub(r"\g<1>" + new_ver + r"\g<2>", content)

        # Replace version in CDN URLs: package@old_version -> package@new_version
        # Handle both scoped (@org/pkg) and unscoped packages
        pkg_name = upd["name"]
        cdn_pattern = re.compile(re.escape(pkg_name) + r"@" + old_ver)
        content = cdn_pattern.sub(pkg_name + "@" + new_ver, content)

        # Replace version in import maps and generic references
        content = content.replace(
            f"{pkg_name}/{upd['tracked']}",
            f"{pkg_name}/{new_ver}",
        )

    skill_file.write_text(content, encoding="utf-8")


# ---------------------------------------------------------------------------
# User interaction
# ---------------------------------------------------------------------------

def prompt_for_updates(all_updates: dict[str, list[dict]]) -> dict[str, list[dict]]:
    """Ask user which skills/packages to update."""
    total = sum(len(u) for u in all_updates.values())
    if total == 0:
        return {}

    print(f"\n  {total} update(s) available across {len(all_updates)} skill(s):\n")

    idx = 1
    index_map = {}
    for skill_name, updates in all_updates.items():
        print(f"    [{skill_name}]")
        for upd in updates:
            print(f"      {idx}. {upd['name']}: {upd['tracked']} -> {upd['latest']}")
            index_map[idx] = (skill_name, upd)
            idx += 1

    print(f"\n  Options:")
    print(f"    [A] Update ALL to latest")
    print(f"    [S] Select specific packages (by number)")
    print(f"    [N] Skip updates")

    choice = input("\n  Choice [A/S/N]: ").strip().upper()

    if choice in ("A", ""):
        return all_updates
    elif choice == "S":
        selected_input = input(
            "  Enter numbers (comma-separated, e.g. 1,3,5): "
        ).strip()
        try:
            indices = [int(x.strip()) for x in selected_input.split(",")]
        except ValueError:
            print("  Invalid selection. Skipping.")
            return {}

        result: dict[str, list[dict]] = {}
        for i in indices:
            if i in index_map:
                skill_name, upd = index_map[i]
                result.setdefault(skill_name, []).append(upd)
        return result
    else:
        return {}


# ---------------------------------------------------------------------------
# Main
# ---------------------------------------------------------------------------

def main():
    print()
    print("=" * 60)
    print("  AI Engineer - Universal Skill Updater")
    print("=" * 60)

    check_only = "--check" in sys.argv
    auto_update = "--auto" in sys.argv

    # Filter to specific skill if requested
    skill_filter = None
    if "--skill" in sys.argv:
        idx = sys.argv.index("--skill")
        if idx + 1 < len(sys.argv):
            skill_filter = sys.argv[idx + 1]

    # Find all skills with versions.json
    skills = find_versioned_skills()
    if skill_filter:
        skills = [s for s in skills if s["name"] == skill_filter]

    if not skills:
        print("\n  No versioned skills found.")
        if skill_filter:
            print(f"  Skill '{skill_filter}' not found or has no versions.json.")
        print("=" * 60)
        return

    print(f"\n  Found {len(skills)} versioned skill(s): "
          + ", ".join(s["name"] for s in skills))

    # Check each skill
    all_updates: dict[str, list[dict]] = {}

    for skill in skills:
        registry = skill["registry"].upper()
        print(f"\n  --- {skill['name']} ({registry}) ---")
        print(f"  {'Package':<35} {'Tracked':<12} {'Latest':<12} {'Status'}")
        print(f"  {'-'*35} {'-'*12} {'-'*12} {'-'*10}")

        updates = check_skill(skill)
        if updates:
            all_updates[skill["name"]] = updates

    # Summary
    total = sum(len(u) for u in all_updates.values())
    if total == 0:
        print("\n  All packages across all skills are up to date.")
        print("\n" + "=" * 60)
        return

    print(f"\n  {total} update(s) available.")

    if check_only:
        print("  (--check mode: no changes made)")
        print("\n" + "=" * 60)
        return

    # Choose what to update
    if auto_update:
        selected = all_updates
        print("  (--auto mode: updating all)")
    else:
        selected = prompt_for_updates(all_updates)

    if not selected:
        print("\n  No updates selected.")
        print("\n" + "=" * 60)
        return

    # Apply updates
    print("\n  Applying updates...")
    total_updated = 0

    # Build a lookup of skills by name
    skill_lookup = {s["name"]: s for s in skills}

    for skill_name, updates in selected.items():
        skill = skill_lookup[skill_name]
        update_versions_json(skill, updates)
        update_skill_md(skill, updates)
        total_updated += len(updates)
        print(f"    [{skill_name}] {len(updates)} package(s) updated")

    # Final summary
    print("\n" + "=" * 60)
    print("  Update Complete!")
    print("=" * 60)
    print(f"\n  Updated {total_updated} package(s) across {len(selected)} skill(s):")
    for skill_name, updates in selected.items():
        for upd in updates:
            print(f"    {skill_name}/{upd['name']}: {upd['tracked']} -> {upd['latest']}")

    print(f"\n  Run 'python scripts/install-skills.py' to push updates to ~/.claude/skills/")
    print()


if __name__ == "__main__":
    main()
