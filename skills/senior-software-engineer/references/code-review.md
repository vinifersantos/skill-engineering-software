# Code Review Standard

Use this for reviewing pull requests, patches, snippets, diffs, refactors, or generated code.

## Severity Model

- **Blocker**: must fix before merge. Includes exploitable security flaws, data loss, broken migrations, severe correctness bugs, production outage risk, or invalid public contract changes.
- **Major**: should fix before merge unless explicitly accepted. Includes important edge-case failures, scalability issues, missing tests for risky behavior, brittle design, race conditions, and unclear ownership boundaries.
- **Minor**: useful improvement. Includes readability, local simplification, naming, test ergonomics, or better decomposition.
- **Nit**: optional style issue.

## Review Checklist

Correctness:
- Are edge cases handled?
- Are errors explicit rather than silently ignored?
- Are API contracts preserved?
- Are migrations safe and reversible?

Security:
- Are inputs validated?
- Are secrets protected?
- Are permissions and tenant boundaries correct?
- Is sensitive data excluded from logs and telemetry?
- Are injection risks addressed?

Reliability:
- Are side effects idempotent where retries are possible?
- Are timeouts, retries, and partial failures handled?
- Are concurrent operations safe?
- Is rollback possible?

Performance:
- Are queries bounded and indexed?
- Are loops, memory usage, and network calls reasonable?
- Are caching semantics correct?

Maintainability:
- Is responsibility localized?
- Is naming clear?
- Is behavior testable?
- Are abstractions justified by current complexity?

Tests:
- Are success, failure, and edge paths covered?
- Would the tests fail without the code change?
- Are tests deterministic and isolated?

## Comment Pattern

```text
[Severity] <short title>

Why it matters:
<risk or consequence>

Suggested fix:
<concrete change, code sketch, or test case>
```

## Summary Pattern

```text
Overall assessment:
<merge recommendation>

Blockers:
- <finding>

Major:
- <finding>

Minor/Nits:
- <finding>

Positive notes:
- <important good design choice>

Tests to request:
- <test>
```

## Risk-Triggered Deep Checks (2026 Revision)

For external calls or asynchronous handlers: verify deadlines, safe bounded retries, idempotency, dedupe/replay, event ordering and poison-message behavior. For caches: verify tenant/key isolation, freshness and invalidation. For persistence: review query plans/pools when changed, schema evolution against mixed deploy versions and reversal path for destructive migrations.

For release/infra changes: verify secret scope, artifact reproducibility, health probe semantics, rollout/rollback signal, configuration drift and operational ownership. For security-relevant routes: verify authorization per object, token verification, webhook signatures, output encoding, SSRF boundaries and logging redaction.

Only flag issues that apply to the actual stack and diff; avoid cargo-cult checklists. Consult the topical references from `SKILL.md` only if a finding requires deeper verification.
