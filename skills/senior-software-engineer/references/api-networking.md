# API and Networking Decision Playbook

Load for public/private API design, gateway/proxy/CDN decisions, real-time communication, webhooks, contracts, load balancing, DNS or protocol questions. Do not suggest every component by default.

## 1. Start with the Request Path

Map the caller -> DNS -> CDN/WAF/load balancer/reverse proxy/API gateway -> application -> cache/database/dependency. Annotate which components actually exist, trust boundaries, authentication, rate limits, timeout budgets, failure domains and ownership. Distinguish **load balancing** (distribution), **reverse proxy** (fronting/origin routing), **API gateway** (API governance/routing/auth policies) and **CDN/edge cache** (content proximity); avoid overlapping products without a reason.

Prefer simpler application endpoints and managed ingress until multiple clients, services or requirements justify a gateway or service discovery. Establish where TLS terminates and whether internal hops need encryption.

## 2. Public API Contract and Abuse Safety

For external APIs specify:
- request/response schema and validation; standardized status and typed errors;
- authn versus per-resource authz and tenant boundaries;
- pagination and maximum payload size; deadlines and server resource limits;
- rate limiting policy by user/token/IP or operation as appropriate, burst behavior, `429` and `Retry-After` where supported;
- idempotency keys on retryable state-changing calls, with scoped durable deduplication and a clear expiration policy;
- versioning and deprecation policy, backward compatibility window and contract tests;
- input sanitization, safe error messages, access logs with correlation IDs and redaction.

**Do not equate semantic versioning of libraries with mandatory URL versioning of an API.** Prefer compatible additive changes; explicit major contract evolution if incompatible; test both old and new consumers. Document schema and operational limits.

## 3. Choose Communication Style by Behavior

| Need | Prefer | Trade-off/test |
| --- | --- | --- |
| Ordinary request/response and broad compatibility | HTTP REST/JSON | Validate schemas, rate limits, caching and error semantics |
| Low-latency internal RPC with typed schemas and streaming | gRPC where stack supports it | Verify client/browser/proxy compatibility, observability and deadlines |
| Occasional asynchronous updates | Polling with conditional requests / adaptive interval | Simplicity versus request overhead and freshness |
| Server -> browser continuous events | Server-Sent Events | One-way stream; reconnect/resume behavior and infrastructure timeouts |
| Bidirectional interactive events | WebSocket | Connection lifecycle, auth renewal, fan-out and horizontal scaling |
| Provider -> consumer event notification | Webhook | At-least-once deliveries, replay handling, signature verification and retries |

Don't select WebSockets merely to avoid polling. Decide based on directionality, concurrent connections, latency requirement, deployment limits and failure recovery. HTTP/2 and HTTP/3 are transport/protocol options; benchmark and check proxy/CDN support rather than building them as application logic. Know DNS TTL/staleness, connection reuse and TCP/UDP properties when diagnosing network effects.

## 4. Webhooks — Minimum Safe Consumer

1. Verify source signature against the raw request body, timestamp/nonce if provided, and valid credentials before business logic.
2. Validate event shape and ownership/authorization. Reject suspicious or oversized input.
3. Persist unique event ID or idempotency record with the business effect atomically or via a reliable inbox/outbox design.
4. Acknowledge according to provider contract; offload slow processing to a queue where justified.
5. Handle duplicates, out-of-order events, replay, provider retries and delayed delivery. Capture dead-letter or remediation signals.
6. Test valid signature, invalid signature, duplicate, late, reordered, timeout and downstream failure.

Never treat webhooks as exactly once. Avoid printing payloads containing personal or credential data.

## 5. Cache and Edge Rules

Define per-response freshness, public/private caching semantics, user/tenant cache key, TTL, invalidation event, stale behavior and stampede mitigation. Do not cache authenticated responses publicly; pay attention to `Vary`, `Cache-Control`, cookies and CDN rules. Measure cache hit rate and origin load before adding layers.

## 6. Review Deliverable

Supply: sequence diagram or request path; chosen protocol and rejected alternatives; security/auth boundary; timeout and rate-limit budgets; retry/idempotency behavior; compatibility/versioning strategy; telemetry; negative/contract/load test matrix.

Refer to `distributed-systems.md` for retries, consistency and messaging; `security-application.md` for API attacks; `data-performance.md` for cache internals.
