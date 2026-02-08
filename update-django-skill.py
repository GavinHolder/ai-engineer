#!/usr/bin/env python3
"""
Django/Python Skill Version Scout & Updater

Checks PyPI for latest package versions, compares against tracked versions,
prompts for update choices, scrapes official Django/Python docs for changes,
and updates the SKILL.md and versions.json.

Usage:
    python update-django-skill.py              # Interactive mode
    python update-django-skill.py --check      # Check only, no changes
    python update-django-skill.py --auto       # Auto-update all to latest

Requirements (auto-installed if missing):
    pip install requests beautifulsoup4
"""

import json
import re
import subprocess
import sys
import urllib.request
from datetime import date
from pathlib import Path
from typing import Optional


# ---------------------------------------------------------------------------
# Configuration
# ---------------------------------------------------------------------------

SCRIPT_DIR = Path(__file__).parent
SKILL_DIR = SCRIPT_DIR / "skills" / "django-python"
VERSIONS_FILE = SKILL_DIR / "versions.json"
SKILL_FILE = SKILL_DIR / "SKILL.md"

PYPI_URL = "https://pypi.org/pypi/{package}/json"
PYTHON_VERSIONS_URL = "https://www.python.org/api/v2/downloads/release/?is_published=true"

# Official doc URLs for scraping release notes
DJANGO_RELEASE_NOTES = "https://docs.djangoproject.com/en/{major}/releases/{version}/"
DJANGO_RELEASE_INDEX = "https://docs.djangoproject.com/en/stable/releases/"
PYTHON_WHATSNEW = "https://docs.python.org/3/whatsnew/{version}.html"


# ---------------------------------------------------------------------------
# Dependency check
# ---------------------------------------------------------------------------

def ensure_dependencies():
    """Check for requests and bs4, offer to install if missing."""
    missing = []
    try:
        import requests  # noqa: F401
    except ImportError:
        missing.append("requests")
    try:
        import bs4  # noqa: F401
    except ImportError:
        missing.append("beautifulsoup4")

    if not missing:
        return True

    print(f"\n  Optional dependencies missing: {', '.join(missing)}")
    print("  These are needed for doc scraping (release notes).")
    print("  Version checking works without them (uses stdlib).\n")

    answer = input("  Install them now? [Y/n]: ").strip().lower()
    if answer in ("", "y", "yes"):
        subprocess.check_call(
            [sys.executable, "-m", "pip", "install", *missing, "-q"]
        )
        print("  Installed successfully.\n")
        return True
    else:
        print("  Skipping doc scraping - version checks only.\n")
        return False


# ---------------------------------------------------------------------------
# Version checking
# ---------------------------------------------------------------------------

def load_tracked_versions() -> dict:
    """Load currently tracked versions from versions.json."""
    if not VERSIONS_FILE.exists():
        print(f"  ERROR: {VERSIONS_FILE} not found.")
        sys.exit(1)
    with open(VERSIONS_FILE, "r", encoding="utf-8") as f:
        return json.load(f)


def fetch_pypi_version(package_name: str) -> Optional[str]:
    """Fetch latest version from PyPI JSON API."""
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
            # Filter stable releases (not pre-release), find latest
            stable = []
            for release in data:
                name = release.get("name", "")
                # e.g. "Python 3.13.2"
                match = re.match(r"Python (\d+\.\d+\.\d+)$", name)
                if match:
                    stable.append(match.group(1))
            if stable:
                stable.sort(key=lambda v: tuple(int(x) for x in v.split(".")), reverse=True)
                return stable[0]
    except Exception:
        pass
    return None


def compare_versions(tracked: dict) -> list[dict]:
    """Check all tracked packages against PyPI. Returns list of updates."""
    packages = tracked.get("packages", {})
    updates = []

    print("\n  Checking versions against PyPI...\n")
    print(f"  {'Package':<30} {'Tracked':<12} {'Latest':<12} {'Status'}")
    print(f"  {'-'*30} {'-'*12} {'-'*12} {'-'*10}")

    for name, info in packages.items():
        tracked_ver = info.get("version", "?")

        if name == "Python":
            latest_ver = fetch_latest_python_version()
        else:
            pypi_name = info.get("pypi", name)
            latest_ver = fetch_pypi_version(pypi_name)

        if latest_ver is None:
            status = "ERROR"
            latest_ver = "?"
        elif latest_ver == tracked_ver:
            status = "OK"
        else:
            # Compare version tuples
            try:
                tracked_parts = tuple(int(x) for x in tracked_ver.split("."))
                latest_parts = tuple(int(x) for x in latest_ver.split("."))
                if latest_parts > tracked_parts:
                    status = "UPDATE"
                else:
                    status = "OK"
            except ValueError:
                status = "UPDATE" if latest_ver != tracked_ver else "OK"

        marker = "  " if status == "OK" else ">>"
        print(f"  {marker} {name:<28} {tracked_ver:<12} {latest_ver:<12} {status}")

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
# Doc scraping
# ---------------------------------------------------------------------------

def scrape_django_release_notes(version: str) -> str:
    """Scrape Django release notes from official docs."""
    try:
        import requests
        from bs4 import BeautifulSoup
    except ImportError:
        return f"(Install requests + beautifulsoup4 for release notes)\nSee: https://docs.djangoproject.com/en/stable/releases/{version}/"

    major = ".".join(version.split(".")[:2])
    url = DJANGO_RELEASE_NOTES.format(major=major, version=version)

    try:
        resp = requests.get(url, timeout=15)
        if resp.status_code != 200:
            # Try the release index page instead
            url = f"https://docs.djangoproject.com/en/{major}/releases/{version}/"
            resp = requests.get(url, timeout=15)
            if resp.status_code != 200:
                return f"Could not fetch release notes (HTTP {resp.status_code})\nURL: {url}"

        soup = BeautifulSoup(resp.text, "html.parser")

        # Get the main content area
        content = soup.select_one("#docs-content") or soup.select_one(".document")
        if not content:
            return f"Release notes page found but could not parse content.\nURL: {url}"

        # Extract key sections: What's new, backwards incompatible, deprecations
        sections = []
        for heading in content.find_all(["h2", "h3"]):
            text = heading.get_text(strip=True)
            lower = text.lower()
            if any(
                kw in lower
                for kw in [
                    "what's new",
                    "new feature",
                    "backward",
                    "deprecat",
                    "bug fix",
                    "minor feature",
                ]
            ):
                section_text = [f"### {text}"]
                # Get sibling elements until next heading
                for sibling in heading.find_next_siblings():
                    if sibling.name in ("h2", "h3"):
                        break
                    if sibling.name in ("p", "li", "ul"):
                        section_text.append(f"- {sibling.get_text(strip=True)[:200]}")
                if len(section_text) > 1:
                    sections.append("\n".join(section_text[:15]))  # Cap at 15 items

        if sections:
            return f"Source: {url}\n\n" + "\n\n".join(sections[:5])  # Cap at 5 sections
        return f"Release notes found but no key sections extracted.\nURL: {url}"

    except Exception as e:
        return f"Error fetching release notes: {e}\nURL: {url}"


def scrape_python_whatsnew(version: str) -> str:
    """Scrape Python What's New from official docs."""
    try:
        import requests
        from bs4 import BeautifulSoup
    except ImportError:
        return f"(Install requests + beautifulsoup4 for what's new)\nSee: https://docs.python.org/3/whatsnew/{version}.html"

    # Use major.minor for what's new page
    parts = version.split(".")
    short_ver = f"{parts[0]}.{parts[1]}"
    url = PYTHON_WHATSNEW.format(version=short_ver)

    try:
        resp = requests.get(url, timeout=15)
        if resp.status_code != 200:
            return f"Could not fetch what's new (HTTP {resp.status_code})\nURL: {url}"

        soup = BeautifulSoup(resp.text, "html.parser")
        content = soup.select_one("#whats-new-in-python") or soup.select_one(".document")
        if not content:
            return f"What's new page found but could not parse.\nURL: {url}"

        # Extract summary and new features
        sections = []
        for heading in content.find_all(["h2", "h3"]):
            text = heading.get_text(strip=True)
            lower = text.lower()
            if any(
                kw in lower
                for kw in [
                    "summary",
                    "new feature",
                    "new module",
                    "improved",
                    "deprecat",
                    "removed",
                    "notable",
                ]
            ):
                section_text = [f"### {text}"]
                for sibling in heading.find_next_siblings():
                    if sibling.name in ("h2", "h3"):
                        break
                    if sibling.name in ("p", "li", "ul"):
                        section_text.append(f"- {sibling.get_text(strip=True)[:200]}")
                if len(section_text) > 1:
                    sections.append("\n".join(section_text[:15]))

        if sections:
            return f"Source: {url}\n\n" + "\n\n".join(sections[:5])
        return f"What's new page found but no key sections extracted.\nURL: {url}"

    except Exception as e:
        return f"Error fetching what's new: {e}\nURL: {url}"


def scrape_package_changelog(name: str, version: str, docs_url: str) -> str:
    """Attempt to scrape changelog for a generic package."""
    try:
        import requests
    except ImportError:
        return f"See: {docs_url}"

    # Try common changelog locations
    changelog_urls = []
    if "github.com" in docs_url:
        # GitHub: try releases page
        changelog_urls.append(docs_url.rstrip("/") + "/blob/main/CHANGELOG.md")
        changelog_urls.append(docs_url.rstrip("/") + "/releases")
    if "readthedocs" in docs_url:
        changelog_urls.append(docs_url.rstrip("/") + "/changelog.html")

    # For now, just return the docs URL - full scraping for all packages
    # would be too aggressive. Django and Python are the key ones.
    return f"See: {docs_url}"


# ---------------------------------------------------------------------------
# Updating files
# ---------------------------------------------------------------------------

def update_versions_json(tracked: dict, updates: list[dict]) -> None:
    """Update versions.json with new versions."""
    packages = tracked["packages"]
    for upd in updates:
        if upd["name"] in packages:
            packages[upd["name"]]["version"] = upd["latest"]
    tracked["last_updated"] = date.today().isoformat()

    with open(VERSIONS_FILE, "w", encoding="utf-8") as f:
        json.dump(tracked, f, indent=2, ensure_ascii=False)
        f.write("\n")
    print(f"\n  Updated {VERSIONS_FILE.name}")


def update_skill_md(updates: list[dict], release_notes: dict) -> None:
    """Update the version table in SKILL.md and append release notes."""
    if not SKILL_FILE.exists():
        print(f"  ERROR: {SKILL_FILE} not found.")
        return

    content = SKILL_FILE.read_text(encoding="utf-8")

    # Update version table entries
    for upd in updates:
        # Match: | Package | old_version | Role |
        # Be flexible with spacing
        pattern = re.compile(
            r"(\|\s*" + re.escape(upd["name"]) + r"\s*\|\s*)" +
            re.escape(upd["tracked"]) +
            r"(\s*\|)"
        )
        content = pattern.sub(r"\g<1>" + upd["latest"] + r"\g<2>", content)

    # Remove old "Version Update Notes" section if it exists
    update_marker = "\n---\n\n## Version Update Notes"
    if update_marker in content:
        content = content[: content.index(update_marker)]

    # Append release notes section
    if release_notes:
        notes_section = "\n---\n\n## Version Update Notes\n\n"
        notes_section += f"*Last checked: {date.today().isoformat()}*\n\n"

        for pkg_name, notes in release_notes.items():
            notes_section += f"### {pkg_name}\n\n{notes}\n\n"

        content += notes_section

    SKILL_FILE.write_text(content, encoding="utf-8")
    print(f"  Updated {SKILL_FILE.name}")


# ---------------------------------------------------------------------------
# User interaction
# ---------------------------------------------------------------------------

def prompt_for_updates(updates: list[dict]) -> list[dict]:
    """Ask user which packages to update."""
    if not updates:
        return []

    print(f"\n  {len(updates)} update(s) available:\n")
    for i, upd in enumerate(updates, 1):
        print(f"    {i}. {upd['name']}: {upd['tracked']} -> {upd['latest']}")

    print(f"\n  Options:")
    print(f"    [A] Update ALL to latest")
    print(f"    [S] Select specific packages")
    print(f"    [N] Skip updates (keep current)")

    choice = input("\n  Choice [A/S/N]: ").strip().upper()

    if choice == "A" or choice == "":
        return updates
    elif choice == "S":
        selected = input(
            "  Enter package numbers (comma-separated, e.g. 1,3,5): "
        ).strip()
        try:
            indices = [int(x.strip()) - 1 for x in selected.split(",")]
            return [updates[i] for i in indices if 0 <= i < len(updates)]
        except (ValueError, IndexError):
            print("  Invalid selection. Skipping updates.")
            return []
    else:
        return []


# ---------------------------------------------------------------------------
# Main
# ---------------------------------------------------------------------------

def main():
    print()
    print("=" * 60)
    print("  Django/Python Skill - Version Scout")
    print("=" * 60)

    # Parse args
    check_only = "--check" in sys.argv
    auto_update = "--auto" in sys.argv

    # Load tracked versions
    tracked = load_tracked_versions()

    # Compare versions
    updates = compare_versions(tracked)

    if not updates:
        print("\n  All packages are up to date!")
        print("\n" + "=" * 60)
        return

    print(f"\n  {len(updates)} package(s) have updates available.")

    if check_only:
        print("\n  (--check mode: no changes made)")
        print("\n" + "=" * 60)
        return

    # Choose what to update
    if auto_update:
        selected = updates
        print("\n  (--auto mode: updating all)")
    else:
        selected = prompt_for_updates(updates)

    if not selected:
        print("\n  No updates selected.")
        print("\n" + "=" * 60)
        return

    # Check for scraping dependencies
    has_scraping = ensure_dependencies()

    # Fetch release notes for selected updates
    print("\n  Fetching release notes from official docs...\n")
    release_notes = {}

    for upd in selected:
        name = upd["name"]
        version = upd["latest"]
        print(f"  Fetching: {name} {version}...")

        if name == "Django":
            notes = scrape_django_release_notes(version)
        elif name == "Python":
            notes = scrape_python_whatsnew(version)
        else:
            notes = scrape_package_changelog(name, version, upd.get("docs_url", ""))

        if notes:
            release_notes[f"{name} {upd['tracked']} -> {version}"] = notes

    # Apply updates
    print("\n  Applying updates...")
    update_versions_json(tracked, selected)
    update_skill_md(selected, release_notes)

    # Summary
    print("\n" + "=" * 60)
    print("  Update Complete!")
    print("=" * 60)
    print(f"\n  Updated {len(selected)} package(s):")
    for upd in selected:
        print(f"    {upd['name']}: {upd['tracked']} -> {upd['latest']}")
    print(f"\n  Files modified:")
    print(f"    - {VERSIONS_FILE}")
    print(f"    - {SKILL_FILE}")
    if release_notes:
        print(f"\n  Release notes appended to SKILL.md ({len(release_notes)} package(s))")
    print()


if __name__ == "__main__":
    main()
