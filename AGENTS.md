# Repository Engineering Rules

The only installable engineering skill is skills/senior-software-engineer/SKILL.md. Read it and only relevant references before changing skill behavior.

- references/ are internal modules, not independent skills.
- Do not recreate Code-First, Harness Engineering, Grill-Me, Test Engineering, Security or Agent Orchestration as separately installed packages.
- Keep plugin.json and marketplace manifests synchronized with the version in SKILL.md.
- Preserve user changes. Never add secrets, .env files or personal data.
- Keep local links valid and update CHANGELOG.md for meaningful behavior changes.
- Do not claim compatibility, tests or runtime activation without evidence.

Required checks:

    python scripts/validate_repository.py
    python -m unittest discover -s scripts -p 'test_*.py' -v
    python scripts/package_skill.py --output-dir dist
    python scripts/package_plugin.py --output-dir dist
