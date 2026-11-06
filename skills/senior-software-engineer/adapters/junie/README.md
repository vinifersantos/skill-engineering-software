# Junie installation

Junie supports the open Agent Skills format in both Junie CLI and the JetBrains IDE integration.

Install globally:

```bash
python scripts/install_skill.py --agent junie --scope user
```

Install only for the current project:

```bash
python scripts/install_skill.py --agent junie --scope workspace
```

Default locations are `~/.junie/skills/senior-software-engineer/` and `.junie/skills/senior-software-engineer/`. In Junie, run `/skills` and confirm the skill appears. Do not copy the pointer adapter into `AGENTS.md` unless you need additional persistent guidelines; the skill itself is discovered natively.

The `AGENTS.md` adapter remains available for older Junie configurations or hosts that only load instruction files. Preserve existing global and project guidelines.
