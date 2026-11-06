# Repository Engineering Rules

This repository maintains one canonical, portable software-engineering skill and distributes it through compatible plugin and Agent Skills surfaces. For any change to engineering behavior, read `skills/senior-software-engineer/SKILL.md` and only the relevant internal references.

## Source of truth

- The only installable engineering skill is `skills/senior-software-engineer/SKILL.md`.
- `references/` are internal playbooks, not independent skills.
- Do not recreate Code-First, Harness Engineering, Grill-Me, Test Engineering, Security or Agent Orchestration as separately installed packages.
- Root `plugin.json` is the portable Agent Plugins manifest. Host-specific manifests point to the same skill folder and version.
- Keep the master skill as an orchestrator; load deep domain playbooks only when relevant.

## Change discipline

- Preserve original technical content unless a change is intentional and documented.
- Update `skills/senior-software-engineer/CHANGELOG.md` for meaningful behavior changes.
- Keep relative references and marketplace source paths valid.
- Do not add dependencies merely to validate Markdown, parse AST or locate code.
- Never add real credentials, `.env` files, personal data or secrets.
- Do not claim compatibility with an agent/runtime without verifying its current loading mechanism.
- Keep plugin and marketplace names stable. Changing them changes installation identifiers.
- Do not overwrite user installations or global agent instructions from installer scripts without explicit `--replace` or preserving existing content.

## Required checks

```bash
python scripts/sync_version.py --check
python scripts/validate_repository.py
python -m unittest discover -s skills/senior-software-engineer/scripts -p 'test_*.py' -v
python -m unittest discover -s scripts -p 'test_*.py' -v
python scripts/package_skill.py --output-dir dist
python scripts/package_plugin.py --output-dir dist
```

Review the final diff and package contents before merging. Releases are created from `vX.Y.Z` tags after all manifests and marketplace metadata are synchronized.
