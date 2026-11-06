# Application, Identity and API Security Playbook

Load for API exposure, identity flows, authorization, sensitive data, multi-tenancy, web security, secrets/crypto, threat modeling or release hardening. Analyze defensive security; do not assert exploitability without a clear attack path and evidence.

## 1. Scope Trust Boundaries

Identify actors (anonymous user, customer, admin, worker, provider), entry points, data sensitivity, assets, authentication mechanism, authorization decisions, server-to-server connections and logging/backup exposure. Assume client requests and webhook payloads are untrusted. Distinguish who the user is (**authentication**) from what they can do to a particular resource (**authorization**).

## 2. Minimum Controls by Problem

| Problem | Control and validation |
| --- | --- |
| IAM / least privilege | Service identity, per-action role/permission and tenant isolation; deny-by-default; periodic access review |
| OAuth / OIDC | Select appropriate standardized flow (authorization code + PKCE for applicable public clients); validate state/nonce where relevant, scopes, issuer and token audience |
| JWT / key rotation | Validate signature, allowed algorithm, issuer, audience, expiry and key selection; short expiry/refresh/revocation strategy appropriate to risk; do not merely decode claims |
| Secret management | Store in managed secret storage/environment protection, scope permissions, rotate and revoke; never commit or log keys |
| Transport and at-rest encryption | TLS end-to-end where required, managed encryption, controlled key access, clear rotation/backup boundaries; distinguish encryption from access control |
| SQL injection | Parameterized queries, least-privilege DB access and schema validation; never concatenate untrusted values into SQL |
| XSS | Context-appropriate output encoding and safe templating; CSP as defense in depth; avoid unsafe HTML injection |
| CSRF | Correct cookie/SameSite and anti-CSRF strategy for credentialed cross-site state changes; verify origin where appropriate |
| CORS | Browser-origin access policy, not authentication or authorization; limit allowed origins/methods/credentials appropriately |
| SSRF | Constrain outbound destinations, reject private/internal address reachability and redirects as appropriate; validate after DNS resolution and guard against rebinding |
| WAF / DDoS | Layered edge controls, bot/rate limits, provider protection and resource caps; does not replace secure application logic |
| Authz / object access | Enforce server-side ownership/role per resource, including filtered searches and API properties; test cross-tenant access and privilege escalation |

For webhooks verify signature using provider's documented raw-body procedure, apply replay protection if supported, and deduplicate repeated deliveries. Check sensitive data in telemetry, queues and exports.

## 3. Review Cases

Add negative tests for: anonymous user, wrong tenant, wrong role, missing/expired/altered token, signature mismatch, mass assignment, malicious URL, SQL parameter attack, XSS input, CSRF context, abusive rate, compromised/stale key and incorrectly shared cache entry. Enforce rate limits at appropriate layers but protect business logic from unbounded resource consumption.

## 4. Security Standards: Living References

Use the latest applicable official standards and project/platform documentation; verify version and date when citing:
- OWASP Top 10 web applications: https://top10.owasp.org/
- OWASP API Security Top 10: https://owasp.org/API-Security/
- OWASP ASVS security requirements: https://asvs.owasp.org/

As observed when this reference was authored (Oct 2026), official sites identify OWASP Top 10:2025 and ASVS 5.0.0; do not assume those remain latest in future tasks. Use a relevant verification level and context, not every requirement for every app.

## 5. Security Review Deliverable

For each meaningful finding, describe trust boundary, affected asset, prerequisites, feasible impact, evidence, severity, precise fix, negative test, deployment/rollback implications and residual risk. Never represent speculative vulnerabilities as confirmed.

For credential classification, provider vaults, CI secret delivery, key rotation/revocation and secret incident response, also load `secret-management.md`.
