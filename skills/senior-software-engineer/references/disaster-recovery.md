# Disaster Recovery & Business Continuity

Load for backup design, restore testing, data corruption, ransomware, regional outage, failover, business continuity or RPO/RTO planning.

## 1. Establish Recovery Requirements

- Identify critical business processes, datasets, dependencies, owners and acceptable service interruption.
- Define **RPO** (maximum tolerable data loss) and **RTO** (maximum tolerable recovery duration) with business and technical stakeholders.
- Do not invent RPO/RTO values or assume a provider's default plan satisfies them.
- Classify data sensitivity, residency, retention and deletion obligations, especially health, financial and personal data.

## 2. Backup Strategy

Define:

- Scope: database, object storage, uploaded files, configuration, schema/migrations, encryption keys and required operational metadata.
- Frequency and recovery points based on approved RPO.
- Retention, lifecycle and legal holds.
- Encryption at rest and protected transport; separate backup credentials and least-privilege access.
- Storage separation from the primary account/region where appropriate, with immutable or deletion-protected copies when risk justifies them.
- Monitoring for backup completion, size anomalies, integrity and missed schedules.

For Supabase or any managed database, verify the current plan, provider features, retention, point-in-time recovery, export limits and restore procedure. Do not assume all projects have identical backup capabilities.

Encrypted exports to secondary storage can improve resilience but create additional copies of sensitive data. Assess LGPD purpose, access, region, processor terms, encryption, retention, deletion and cost before enabling them. Do not create routine exports by default.

## 3. Restore Drills

A backup is not proven until a restore has succeeded.

Run restore drills at a cadence appropriate to business risk and provider capability:

1. Select a known recovery point and record its timestamp.
2. Restore into an isolated environment, never over production during a test.
3. Validate schema, migration state, row counts, checksums or business invariants, referential integrity and file/object availability.
4. Verify RLS, grants, identities, secrets, encryption keys, application compatibility and required dependencies.
5. Run critical read/write workflows with synthetic or approved data.
6. Measure actual recovery time and data loss; compare with agreed RTO/RPO.
7. Record failures, owners, corrective actions and the next drill.

Protect restored data as carefully as production data. Restrict access and securely dispose of temporary restore environments according to policy.

## 4. Failover, Failback and Incident Runbooks

Document:

- Trigger/decision owner and abort conditions.
- Provider/account/region/target verification.
- DNS, routing, credentials, encryption keys, queues, storage and external dependencies.
- Data replication lag, consistency and reconciliation.
- Application version/schema compatibility.
- Communication, user impact and operational roles.
- Failback criteria and prevention of split-brain or conflicting writes.

Do not assume that switching traffic reverses database changes. Plan recovery for code, schema, data and configuration separately.

## 5. Privacy and Retention

Backup retention must account for data-subject rights and organizational retention policy. A delete/anonymize request may require a defined process for active data, replicas, exports and backup expiry/restoration. Do not promise immediate physical erasure from immutable backups unless the actual architecture supports it; obtain legal/privacy guidance for policy and exceptions.

## 6. Authorization and Acceptance

Production backup export, restore, failover, failback, snapshot deletion or key changes are consequential actions. Require explicit authorization for the exact target and operation.

Report approved RPO/RTO, backup coverage, encryption/access controls, restore-drill evidence, measured recovery, unresolved gaps, runbook owner and next corrective action. Never claim recoverability from backup creation alone.
