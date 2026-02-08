# Django & Python Skill

Comprehensive Django and Python development reference with auto-updating package versions.

## What It Does

Provides Claude with a complete Django development reference:

- **Project structure**: Standard Django project layout and conventions
- **Models**: ORM patterns, migrations, relationships, managers
- **Views**: Class-based and function-based views, middleware
- **URLs**: URL routing patterns and namespacing
- **Forms**: Form handling, validation, ModelForms
- **DRF APIs**: Django REST Framework serializers, viewsets, authentication
- **Celery tasks**: Async task queues, scheduling, error handling
- **HTMX SPA patterns**: Single-page-app feel without a JS framework
- **Testing**: pytest-django, factories, fixtures
- **Security**: CSRF, XSS, SQL injection prevention, auth patterns
- **Docker deployment**: Containerization, docker-compose, production configs
- **Service layer architecture**: Business logic separation patterns

## Plugin Relationship

Claude Code ships with a built-in `django-framework` skill, but it's minimal. This is a **much more comprehensive replacement** covering the full Django ecosystem (DRF, Celery, HTMX, Docker deployment, service layers) plus auto-updating package versions. The `install-skills.py` script installs this alongside the built-in skill.

### Auto-Updated Versions

Package versions are tracked in `versions.json` and can be auto-updated using the Version Scout script at the repo root. See [Version Scout](#version-scout) below.

## How to Use

### Automatic
Claude activates this skill when you're working on Django projects:
```
"Create a Django model for blog posts"
"Add a DRF API endpoint for users"
"Set up Celery for email sending"
```

### Slash Command
```
/Django Framework
```

## Version Scout

The `update-django-skill.py` script (at the repo root) keeps package versions current:

```bash
python update-django-skill.py              # Interactive: choose what to update
python update-django-skill.py --check      # Check only, no changes
python update-django-skill.py --auto       # Auto-update all to latest
```

It checks PyPI for latest versions, compares against `versions.json`, and updates both `versions.json` and `SKILL.md` with release notes scraped from official docs.

**Requirements**: `pip install requests beautifulsoup4` (auto-installed if missing)

## Files

| File | Purpose |
|---|---|
| `SKILL.md` | Full Django & Python reference (models, views, DRF, Celery, testing, deployment) |
| `versions.json` | Tracked package versions (Python, Django, DRF, Celery, etc.) |

## Installation

Installed automatically by `install-skills.py`. Copies to `~/.claude/skills/django-python/`.
