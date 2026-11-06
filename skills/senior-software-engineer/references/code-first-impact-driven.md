# Code-First & Impact-Driven - Detailed Protocol

Use this reference for implementation, debugging, refactoring, code review or any task that changes executable code, types or build-affecting configuration. The master `SKILL.md` keeps the core rules active; this file provides the detailed checklist.

## Execution sequence

**Locate -> Analyze Impact -> Implement -> Validate -> Deliver**

### 1. Direct code location

1. Identify the files, components, functions, types, schemas, routes and dependencies directly related to the request.
2. Prefer repository search, targeted text search, symbol/reference lookup and existing AST/LSP capabilities when available and relevant.
3. Use AST or symbol-analysis tools only when already available and useful. Do not install packages, invoke `npx` utilities or introduce dependencies merely to locate code.
4. Do not navigate the application UI to discover code that can be located directly in the repository.
5. Expand the search only when evidence reveals dependencies, shared behavior or risk that requires it.

### 2. Contract and boundary impact

Before changing a contract, map relevant consumers and implementations:

- Component props, exports and shared UI contracts.
- TypeScript interfaces, types, generics and function signatures.
- Zod schemas and validation at input, API and persistence boundaries.
- API, event, webhook and message contracts.
- Supabase/PostgreSQL functions, RPC signatures, generated types, queries, grants and RLS policies.
- Server Components, Client Components (`"use client"`), Server Actions, route handlers and server-only modules.

Preserve compatibility where required. Do not assume a UI restriction is authorization. Never move server-only logic or secret credentials into client code.

### 3. Minimum necessary context

- Read the smallest useful portions of files first; inspect whole files only when needed.
- Avoid unrelated modules, generated output, vendor directories, build artifacts and repeated reads.
- Reuse project instructions and conventions when they materially affect the change.
- If evidence is insufficient, identify the unknown and inspect only the next relevant source.

### 4. Surgical, type-safe modification

- Modify the smallest set of files that safely solves the request.
- Preserve architecture, naming, formatting, dependency choices and established patterns.
- Avoid speculative abstractions, dependencies, refactors and unrelated cleanup.
- Do not hide type errors with `any`, `@ts-ignore` or `@ts-expect-error` without an explicit, technically sound justification. Prefer fixing the underlying model or boundary.
- Explain any necessary scope expansion beyond the request.

### 5. Working-tree and environment protection

- Inspect Git state before editing when Git is available (`git status --short`).
- Preserve staged, unstaged and untracked user changes.
- Do not overwrite, discard, reset, clean or revert unrelated work.
- Do not modify `.env` files or expose their contents. Keep local environment files untracked and protected; never commit real secrets.
- Do not run destructive commands (`git reset`, `git clean`, `git checkout --`, bulk deletion or equivalent) without explicit authorization.
- Keep edits attributable to the current task and inspect the final diff.

### 6. Contextual static validation

**Applicability**

- For executable code, types or build-affecting configuration, run available type-check and lint commands.
- Purely documentary changes (for example Markdown or prose-only comments) do not require `tsc` or lint unless those files are executable inputs.

**Discover real project commands**

1. Inspect the relevant `package.json`, workspace configuration, lockfiles and scripts.
2. Identify the actual package manager (`pnpm`, `npm`, `yarn`, `bun` or another toolchain); do not guess.
3. In monorepos, run checks in the affected package and use intended workspace commands.
4. Run configured type-check and linter commands.
5. If a check is not configured, report it. Do not install packages or change project configuration solely to satisfy this rule.
6. Distinguish pre-existing failures from regressions where possible.

Never claim a check passed unless it actually ran and completed successfully.

### 7. Risk-proportionate tests

- Unit tests for isolated rules and transformations.
- Integration tests for module, persistence, API and service boundaries.
- Contract tests for public APIs, events, schemas and compatibility.
- E2E tests for critical journeys or behavior requiring a real runtime.

Start with targeted tests. Expand when changes cross boundaries, affect shared contracts, touch critical business rules or have a broad failure surface. Avoid unrelated expensive suites. Report missing or unavailable tests.

### 8. Safe circuit breaker

When validation or tests fail after the change:

1. Inspect the failure and identify the likely root cause before editing again.
2. Separate failures caused by the current change from pre-existing/environmental failures.
3. Make corrections only from a reasoned diagnosis.
4. If failure persists after **two correction attempts**, stop further edits and report the blocker and evidence.
5. If undoing an unsuccessful attempt is necessary, revert only the specific lines or changes made by this task. Never restore an entire file from an earlier Git version merely to undo a local attempt.
6. If ownership cannot be determined confidently, do not reverse automatically; preserve repository state and report the issue.

The circuit breaker does not authorize destructive cleanup.

### 9. Restricted visual validation

Use browser or visual inspection only for visual hierarchy, responsive behavior, browser-specific rendering or real flows that cannot be established through source and automated tests. Inspect only the relevant screen or flow.

### 10. Evidence-based completion

Report:

- Exact files changed.
- Technical summary of implementation.
- Actual validation commands and outcomes, or why checks were unnecessary/unavailable.
- Risks, limitations and pending work.

Never imply that a test, build, visual check, deployment or review occurred without evidence.

## Integration with the master skill

- Harness governance and risk levels are in `agent-harness-orchestration.md` and `risco-e-autonomia.md`.
- Discovery and requirement challenge are in `grill-me-mode.md`.
- Security, data, testing, release and operations details live in their respective internal references.
