# Observability, Structured Logging & Telemetry

Load when adding runtime monitoring, exception reporting, structured logs, metrics, traces, SSR/Edge instrumentation or production diagnostics.

## 1. Start from Questions and User Journeys

Define what operators need to know:

- Is the user journey succeeding?
- Which route, tenant-safe operation, dependency or job is failing?
- How often, how slowly and with what blast radius?
- Is the system saturated or accumulating work?
- Did a release/configuration change alter behavior?

Prefer user-facing signals over infrastructure vanity metrics. Define numerator, denominator, source, exclusions, aggregation window and owner for each SLI. Do not invent SLO values.

## 2. Structured Logs

Use consistent JSON/event fields where the runtime supports them:

- `timestamp` in UTC, `severity`, `service`, `environment`, `event` and version/release.
- `request_id`, `correlation_id` or `trace_id` for cross-boundary diagnosis.
- Route/operation, status, duration and safe error classification.
- Actor/tenant identifiers only when necessary, authorized and privacy-safe; prefer pseudonymous or non-identifying IDs.

Apply the same event model across SSR, API routes, background workers, Edge Functions and database-related logs where platform capabilities allow. Do not log passwords, access tokens, secret keys, raw clinical/financial payloads, unnecessary PII or full webhook bodies. Redact before export and set retention/access controls.

## 3. Metrics and Traces

- Track traffic, error rate, latency, saturation, queue age, retries, dependency health, DB pool occupancy, Edge Function invocation/duration/errors and relevant business outcomes.
- Use p50/p95/p99 where useful; do not use averages alone for tail-sensitive journeys.
- Avoid high-cardinality labels such as raw user IDs, email addresses, tokens or unbounded request values.
- Propagate trace context across HTTP, jobs, messaging and database spans when supported.
- Sample traces intentionally; preserve enough error/high-latency traces to diagnose without uncontrolled cost.
- Distinguish a metric, log and trace; use each for its intended diagnostic purpose.

## 4. Exception Monitoring (Sentry and Similar)

When useful, integrate an exception-monitoring SDK such as Sentry or an OpenTelemetry-compatible platform.

- Instrument the correct runtime: browser, server/SSR, API, workers and Edge Functions as supported.
- Configure release/environment tags and source-map upload securely.
- Filter known noise without suppressing real failures.
- Scrub sensitive fields and review SDK defaults for request bodies, headers, cookies, breadcrumbs and user context.
- Control sampling, quotas, retention, access and data residency.
- Verify both successful event delivery and intentional non-capture of sensitive data.

Do not add an SDK, export telemetry to a third party or change data collection without considering user privacy, provider terms and project authorization.

## 5. Alerts and Runbooks

Alert on actionable user impact, fast SLO burn, sustained saturation, queue age, data freshness or critical dependency failures. Every alert should have a threshold rationale, owner, severity, notification route, runbook and recovery condition. Avoid paging on every transient error or CPU fluctuation.

## 6. Observability Acceptance

Verify instrumentation in a non-production environment where possible. Confirm correlation across layers, correct release/environment attribution, redaction, retention, alert routing, dashboard usefulness and cost. Never claim telemetry works merely because an SDK dependency was added.
