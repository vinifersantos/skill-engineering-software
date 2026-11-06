## Summary

Describe the change and why it belongs in the single master skill or its distribution infrastructure.

## Scope

- [ ] Updated the master `skills/senior-software-engineer/SKILL.md`
- [ ] Updated one or more internal references
- [ ] Updated host adapters or installation documentation
- [ ] Updated plugin and marketplace manifests when needed
- [ ] Updated changelog and synchronized versions when needed

## Validation

- [ ] `python scripts/sync_version.py --check`
- [ ] `python scripts/validate_repository.py`
- [ ] Skill helper tests
- [ ] Repository tooling tests
- [ ] Standalone skill ZIP generated and inspected
- [ ] Cross-host plugin ZIP generated and inspected

## Safety and compatibility

- [ ] No real secrets, `.env` files or personal data added
- [ ] Relative references and marketplace source paths remain valid
- [ ] Exactly one installable skill entry point remains
- [ ] Plugin and marketplace versions are synchronized
- [ ] Platform compatibility claims are evidence-based
