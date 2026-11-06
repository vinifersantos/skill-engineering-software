# Architecture Review Checklist

Use this reference for system design, service boundaries, integrations, platform choices, and technical decision support.

## 1. Clarify the Problem

Identify:
- users and consumers;
- current pain or business objective;
- functional requirements;
- non-functional requirements;
- constraints such as budget, team skill, deadline, compliance, vendor lock-in, and legacy systems;
- scale assumptions: requests per second, data volume, growth rate, latency, availability, and consistency needs.

If exact numbers are unknown, state reasonable assumptions and design so they can be revised later.

## 2. Evaluate the Design

Assess:
- service/module boundaries and ownership;
- data model and source of truth;
- synchronous vs asynchronous communication;
- consistency model and failure behavior;
- idempotency, retries, deduplication, and ordering;
- API contracts and versioning;
- authorization, tenant isolation, auditability, privacy, and secrets;
- operational complexity and on-call burden;
- cost drivers and scaling bottlenecks.

## 3. Compare Alternatives

For each relevant alternative, compare:
- simplicity;
- delivery speed;
- correctness risk;
- scalability ceiling;
- cost;
- operational burden;
- migration complexity;
- reversibility.

Recommend one option and explain why it fits the constraints better than the others.

## 4. Production Readiness

A design is not production-ready until it has:
- rollout plan and feature flag strategy where applicable;
- rollback path;
- metrics, logs, traces, dashboards, and alerts;
- SLO/SLA implications;
- failure-mode analysis;
- security review for sensitive data or trust boundaries;
- test strategy including unit, integration, contract, load, and migration tests as needed;
- ownership and runbook notes.

## 5. Output Template

```text
Recommendation:
<chosen design>

Assumptions:
- <assumption>

Design:
- Components:
- Data flow:
- API/contracts:
- Storage:
- Failure handling:

Alternatives considered:
1. <option>: pros/cons
2. <option>: pros/cons

Risks and mitigations:
- <risk> -> <mitigation>

Rollout:
1. <step>

Observability:
- Metrics:
- Logs:
- Alerts:

Validation:
- Tests:
- Load/performance checks:
```

## Conditional Decision Gates (2026 Revision)

Before recommending a new component, document the existing failure or measured bottleneck, scale/consistency target, simplest alternative, new operational costs and an acceptance test. This applies especially to message brokers, Kubernetes, sharding, multi-region replication and distributed locks. A managed modular monolith is a valid outcome.

When a distributed workflow is proposed, document timeouts, retry budget, backpressure, idempotency key/transaction boundary, dead-letter/replay policy and consistency guarantee. For production-critical endpoints, define measurable tail-latency and user-facing reliability signals; do not assert arbitrary SLO values.

Load `api-networking.md`, `distributed-systems.md`, `data-performance.md`, `deployment-platform.md`, `reliability-operations.md` or `security-application.md` when those topics materially affect the decision.

For deeper reviews, load the relevant internal modules: `database-engineering.md`, `secret-management.md`, `ci-cd-release-engineering.md`, `observability-telemetry.md`, `disaster-recovery.md` and `agent-harness-orchestration.md`.
