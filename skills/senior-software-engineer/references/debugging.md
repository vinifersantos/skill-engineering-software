# Debugging and Incident Workflow

Use this for bugs, failing tests, regressions, production incidents, flaky tests, and performance problems.

## Core Rule

Do not guess broadly. Reduce uncertainty with the cheapest reliable probe.

## Workflow

1. Define the symptom precisely.
   - What failed?
   - What was expected?
   - Who or what is affected?
   - When did it start?
   - Is it deterministic or intermittent?

2. Establish a timeline.
   - Recent deployments.
   - Config changes.
   - Dependency changes.
   - Data changes.
   - Infrastructure events.

3. Create hypotheses.
   Rank by probability and blast radius. Include evidence for and against each hypothesis.

4. Verify with probes.
   Prefer:
   - reproduction case;
   - minimal failing test;
   - targeted log query;
   - trace inspection;
   - metric comparison;
   - config diff;
   - dependency lockfile diff;
   - binary search through commits.

5. Fix minimally.
   The first fix should address root cause with the smallest safe change. Avoid opportunistic refactors during an incident unless necessary.

6. Prevent recurrence.
   Add:
   - regression test;
   - better validation;
   - metric or alert;
   - safer default;
   - runbook update;
   - rollout guardrail.

## Output Template

```text
Highest-probability hypothesis:
<claim>

Evidence:
- Supports:
- Contradicts/unknown:

Verification:
<fastest check>

Root cause:
<confirmed cause or current best explanation>

Fix:
<minimal safe fix>

Regression coverage:
<tests/checks>

Operational follow-up:
<logs/metrics/alerts/runbook>
```

## Common Failure Patterns

- Environment drift between local, CI, staging, and production.
- Stale caches or incorrectly scoped cache keys.
- Timezone, clock skew, date truncation, or DST errors.
- Race conditions from non-atomic writes.
- Missing idempotency in retries or webhooks.
- Pagination and partial-failure bugs.
- Connection pool exhaustion.
- Unbounded queries or N+1 access patterns.
- Inconsistent dependency versions or transitive upgrades.
- Silent exception swallowing.
- Incorrect auth context or tenant boundary leakage.

## Additional Production Probes (2026 Revision)

When errors, latency or saturation are involved, inspect route-by-route p95/p99, queue age, retry attempts, network timeout rates, GC pauses, connection-pool occupancy, DB query plans, trace fan-out and dependency service-level behavior. Build a timeline of changes; do not confuse a correlated deploy with proven causation.

During an incident, prioritize blast-radius containment and data integrity; verify the fix against a user-facing SLI before closing. Treat outages involving duplicated side effects, dropped messages, cache cross-tenant leakage, replica staleness, clock skew or failed failover as correctness incidents, not only operational noise. Use `reliability-operations.md` for severity, response and postmortem; `distributed-systems.md` for resilience and ordering.

For formal root-cause analysis, contributing factors, detection gaps and behavior-preserving refactoring, also load `debugging-rca-refactoring.md`.
