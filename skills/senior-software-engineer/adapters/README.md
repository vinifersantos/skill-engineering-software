# Runtime adapters

The master skill is portable, but each host discovers skills and plugins differently. Keep the complete `skills/senior-software-engineer/` folder intact so relative references resolve.

## Plugin-native hosts

- **Codex:** use the repository marketplace or install the skill into `~/.agents/skills/`.
- **Claude Code:** use the Claude marketplace or install the skill into `~/.claude/skills/`.
- **GitHub Copilot CLI and VS Code:** use the GitHub Copilot marketplace and the root Agent Plugins 1.0 manifest.
- **Cursor:** use the Cursor plugin marketplace/source or install the skill into `~/.cursor/skills/`.
- **Antigravity:** install the full repository plugin with `agy plugin install` or place the plugin directory in `.agents/plugins/` or `~/.gemini/config/plugins/`.
- **Gemini CLI:** use `gemini skills install` or the interoperable `~/.agents/skills/` directory.
- **JetBrains Junie:** install into `~/.junie/skills/` or `.junie/skills/`.

## Instruction-based hosts

The `AGENTS.md`, `CLAUDE.md`, Copilot instructions and Cursor/Junie rules in the repository are small routing adapters. When using the skill in another repository, add a short pointer to the installed skill path in the host's instruction file if the host does not discover Agent Skills natively.

## Important

Do not install both the plugin and a manually copied version into the same runtime unless duplicate copies are intentional. Plugin updates and copied-file updates have different mechanisms. Check the host's current documentation before assuming automatic updates.
