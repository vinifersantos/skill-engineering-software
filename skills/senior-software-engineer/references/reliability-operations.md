# Observability, SRE and Incident Operations

Load for production observability, incident response, monitoring/alert design, SLI/SLO/error budgets, DR, failover, chaos testing, capacity or postmortems. Choose operational sophistication proportional to customer impact and team resources.

## 1. Measure User-Facing Reliability

1. Name a user journey or service boundary (e.g. 'successful checkout'), not just an infrastructure metric.
2. Define a measurable **SLI** and numerator/denominator, source, exclusions, aggregation window and owners. Common SLIs: successful request ratio, latency below threshold, job completion before deadline, data freshness.
3. Negotiate an **SLO** target and rolling window from business expectation and realistic baselines. Never invent a percentage.
4. An **error budget** is tolerable failure implied by the SLO for the window; use it to inform release/reliability trade-offs only after agreed measurement and policy exist.
5. Distinguish **SLA** (contractual undertaking) from SLO (engineering objective).

Use p50/p95/p99, throughput, saturation and queue age for diagnosis, but don't label a percentile as an SLO without an explicit user experience target.

Google SRE workbook example: https://sre.google/workbook/error-budget-policy/

## 2. Signal Design and Alert Quality

- **Metrics:** traffic, errors, latency, saturation, resource utilization, dependency health, queue age, retry/timeout rates and critical business effects. Avoid unbounded-cardinality labels and PII in telemetry.
- **Logs:** structured, time-aligned events with correlation/request ID, relevant error context and environment; redact secrets, tokens and sensitive payloads. Set useful retention.
- **Traces:** propagate context across service/process boundaries; sample deliberately and connect requests to expensive database and dependency spans.
- **Alerting:** page on actionable user impact or fast SLO burn, not every CPU fluctuation; define severity, threshold, runbook, owning team, route and clear recovery condition. Create dashboards for diagnosis before proliferating alerts.

OpenTelemetry reference: https://opentelemetry.io/docs/concepts/signals/

## 3. Active Incident Procedure

1. Assess severity, affected users and potential data/security impact; establish incident owner and communications.
2. Contain: stop risky changes, scale/rate-limit safely, disable feature or rollback where safe. Preserve critical evidence.
3. Triage timeline: deploy/config/infra/provider changes, logs, metrics, traces and dependency health; isolate the fault domain.
4. Verify remediation through user-visible SLIs and business operations, not only service restarts.
5. Document incident timeline, immediate cause, contributing factors, blast radius, detection delay, recovery time and uncertainties.
6. Conduct a blameless **postmortem** proportionate to severity; choose measurable corrective actions with owners/dates and verification of effectiveness.

If on-call/plantao is in scope, define coverage, escalation, paging fatigue limits, runbook access and handoff. Avoid recommending a 24/7 burden to a team that cannot staff it without discussing alternatives.

## 4. Disaster Recovery and Chaos Engineering

- **Backup:** define scope, frequency, retention, access control and integrity; **test actual restores** on a meaningful cadence.
- **RPO:** maximum tolerable data loss; **RTO:** maximum tolerable recovery duration. Establish with stakeholder, not by guesswork.
- **Failover:** test data and traffic switch, reconciliation, dependencies, credential accessibility and failback; multi-region is not automatically safer or needed.
- **Chaos engineering:** form a hypothesis tied to resilience, scope blast radius, have abort conditions and explicit authorization, test in lower-risk environments first. Never inject faults into production without controls and permission.
- **Clock skew/network partitions:** validate time assumptions, replay and consistency for distributed systems with important invariants.

## 5. Operational Review Output

Include reliability objective and measurement, symptom/impact, telemetry sources, proposed fix, test/drill, alert/runbook owner, release gate, rollback/restore plan and estimated operation cost. State where evidence is missing.

For concrete structured logging, SSR/Edge instrumentation, Sentry/OpenTelemetry, privacy-safe telemetry and alert design, also load `observability-telemetry.md`. For backup policy, restore drills, secondary storage, RPO/RTO and recovery runbooks, load `disaster-recovery.md`.
