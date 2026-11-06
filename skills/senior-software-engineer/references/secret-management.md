# Secret Management & Credential Lifecycle

Load when handling API keys, database credentials, Supabase keys, VAPID keys, OAuth secrets, signing keys, CI/CD credentials, webhooks or cloud identities.

## 1. Classify Credentials Correctly

Not every configuration value is a secret. Identify purpose, exposure model, permissions, owner, environment and rotation impact.

- **Public/client configuration:** values intentionally exposed to browsers, such as a Supabase publishable/anon key or a VAPID public key. These are safe only under their documented model and with correct RLS, authorization and key restrictions.
- **Server secrets:** Supabase service-role/secret keys, database passwords, VAPID private keys, OAuth client secrets, webhook signing secrets, private signing keys and unrestricted third-party API keys. Keep server-side.
- **Scoped credentials:** keys designed for a specific public API/client may be exposed only with restrictions such as allowed origins, operations, quotas and limited permissions.

Never label a credential public or private based only on its name. Verify the provider's current documentation and actual permissions.

## 2. Storage and Delivery

Prefer managed secret stores appropriate to the environment:

- Hosting/cloud secret manager.
- GitHub Actions Secrets and protected environments.
- GitLab CI/CD variables with masked/protected settings.
- Supabase Vault for database-side secret use where supported and appropriate.
- KMS/HSM-backed key management for cryptographic key lifecycle when required.

Controls:

- Encrypt secrets at rest and use protected, authenticated channels for delivery.
- Restrict access by identity, environment, workload and action; use least privilege.
- Prefer short-lived OIDC/federated credentials over long-lived static CI keys where supported.
- Keep production, staging and development credentials separate.
- Do not commit secrets, put them in Docker build args/layers, frontend bundles, source maps, logs, screenshots, issue comments or prompts.
- `.env` may be used for local development if protected, excluded from version control and never shared. `.env.example` contains placeholders only.
- Environment variables are a delivery mechanism, not a vault by themselves. Once injected into a process, they may be visible to that process and privileged diagnostics; do not assume automatic end-to-end secrecy.

## 3. Rotation, Revocation and Incident Response

- Maintain an inventory of credential owner, purpose, scopes, consumers, environment, expiry and rotation procedure.
- Rotate according to provider capability, sensitivity, exposure and policy; do not invent a universal interval.
- Use overlap/dual-key windows where supported: create new credential, deploy consumers, verify, then revoke old credential.
- Test recovery and rollback before rotation when availability is critical.
- Revoke immediately when compromise is suspected; preserve audit evidence and inspect access logs.
- Do not rotate or revoke production credentials automatically without explicit authorization.

## 4. Validation Checklist

- Search repository history and current files for accidental secrets using approved scanners; never print the secret value in the report.
- Confirm `.env*` ignore rules without opening or exposing secret contents.
- Confirm CI logs, artifacts, build cache, source maps and telemetry do not leak credentials.
- Verify client bundles contain only intentionally public configuration.
- Verify server-side access, scopes, rotation and revocation behavior.
- Use synthetic credentials and safe test environments for tests.

## 5. Secret Incident Deliverable

Report credential class, affected environments/consumers, exposure evidence, containment/revocation status, rotation plan, audit scope, downtime risk and verification. If exposure is suspected, do not claim containment until revocation and consumer verification are confirmed.
