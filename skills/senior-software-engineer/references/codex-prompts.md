# Codex Prompt Patterns

Use these templates when the user wants Codex to modify, inspect, debug, or review a repository. Adapt them to the exact repo context. Prefer concrete acceptance criteria over broad requests.

## Implementation Prompt

```text
You are working in this repository as a senior software engineer.

Goal:
<clear business/technical objective>

Context:
<relevant modules, conventions, framework versions, architecture constraints, existing behavior>

Scope:
- Change only what is necessary to implement the goal.
- Preserve existing public APIs unless explicitly required.
- Keep the implementation readable, typed where applicable, and easy to test.

Implementation requirements:
1. Inspect the relevant files before editing.
2. Identify the minimal design that fits the current architecture.
3. Implement the change with explicit error handling and no silent failures.
4. Add or update tests covering success paths, failure paths, and edge cases.
5. Avoid leaking secrets or sensitive data in logs.
6. Keep changes backward-compatible unless the task explicitly requires a breaking change.

Acceptance criteria:
- <observable behavior 1>
- <observable behavior 2>
- Tests pass with <command>.
- Lint/typecheck pass with <command>.

Return:
- Summary of files changed.
- Tests run and results.
- Remaining risks or follow-up work.
```

## Debugging Prompt

```text
Investigate this bug systematically.

Symptom:
<error, failing test, incident behavior, logs, stack trace>

Expected behavior:
<expected behavior>

Known context:
<recent changes, environment, dependency versions, input data, affected users>

Instructions:
1. Reproduce or identify the narrowest failing path.
2. Form hypotheses and verify them with code inspection, tests, logs, or minimal probes.
3. Do not rewrite broad areas before proving the root cause.
4. Implement the smallest safe fix.
5. Add a regression test that fails before the fix and passes after it.
6. Report root cause, fix, tests, and any residual risk.
```

## Refactoring Prompt

```text
Refactor the targeted code without changing external behavior.

Target:
<files/functions/components>

Motivation:
<readability, duplication, performance, testability, architecture boundary, migration preparation>

Constraints:
- Preserve public behavior and API contracts.
- Keep the diff reviewable.
- Do not introduce new dependencies unless justified.
- Add/update tests if behavior could accidentally change.

Acceptance criteria:
- Existing tests pass.
- New tests cover refactored edge cases if applicable.
- Complexity is reduced or responsibilities are clearer.
- The final summary explains behavior preservation.
```

## PR Review Prompt

```text
Review this change as a senior engineer.

Focus areas:
- Correctness and edge cases.
- Security and data handling.
- Concurrency, idempotency, and race conditions.
- Performance and scalability.
- API compatibility and migrations.
- Test coverage and observability.
- Maintainability and repository conventions.

Output format:
- Blocker: issues that must be fixed before merge.
- Major: important issues that should be fixed.
- Minor: improvements that are useful but not blocking.
- Nit: optional style/readability comments.
- Positive notes: important things done well.

For each finding, include:
- File/location if known.
- Why it matters.
- Concrete suggested fix.
```

## Migration Prompt

```text
Plan and implement this migration safely.

Migration goal:
<schema/config/API/data migration objective>

Safety requirements:
- Migration must be backward-compatible during rollout when possible.
- Include rollback or remediation strategy.
- Avoid destructive operations without explicit confirmation.
- Consider large datasets, locks, timeouts, retries, and partial failures.
- Add observability to detect failure or data drift.

Required output:
- Migration sequence.
- Code/config changes.
- Tests or dry-run strategy.
- Rollout and rollback plan.
- Operational risks.
```

## Production Hardening Prompt (Risk-Based)

```text
Inspect the current repository and its deployment model before changing anything.

Goal:
<one specific production reliability, security, performance or operability gap>

Evidence:
<logs, failing scenario, profile, monitoring signal, repo files, observed load or incident>

Instructions:
1. Identify the smallest fix that addresses the verified failure mode. Do not add
   Kubernetes, queues, caching, sharding or third-party libraries without justification.
2. Preserve existing interfaces and avoid destructive or irreversible operations.
3. For affected cross-service calls, check timeouts, cancellation, idempotency,
   bounded retries with backoff/jitter, and overload behavior.
4. For affected data flows, check ownership/authz, atomicity, transaction or
   schema compatibility, sensitive logging and cache key isolation.
5. Add tests that fail before the change (where feasible), including important
   error paths, concurrency/replay tests and a measured baseline if performance-related.
6. Specify observability, rollout, recovery and rollback criteria proportional
   to the severity; state any unverified assumptions.

Deliver:
- Evidence and chosen minimal design.
- Actual files changed and rationale.
- Commands/tests executed with results; do not claim unrun checks passed.
- Measured or observable acceptance criteria, rollout and residual risks.
```
