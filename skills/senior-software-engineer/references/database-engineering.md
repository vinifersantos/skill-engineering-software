# Data Engineering & Persistence Playbook

Load for relational modeling, PostgreSQL/Supabase, schema evolution, data integrity, tenant isolation, migrations or persistence design. Treat the database as a business contract and source of truth.

## 1. Model the Domain and Invariants

- Identify entities, ownership, relationships, lifecycle, cardinality, tenant scope and retention requirements.
- Use primary keys, foreign keys, unique constraints, check constraints and not-null constraints to enforce invariants close to the data.
- Normalize to avoid update anomalies; denormalize only for a measured access pattern or justified read model, with a clear consistency/rebuild strategy.
- Define deletion semantics (restrict, cascade, soft delete, anonymize) deliberately. Consider auditability and legal retention before destructive cascades.
- Use explicit timestamps/time zones, currency/decimal types and stable identifiers appropriate to the domain. Avoid floating point for exact monetary values.
- Treat schema, generated types, migrations, API DTOs and application models as related but distinct contracts.

## 2. Multi-Tenancy and PostgreSQL/Supabase RLS

- Define the tenant source of truth and membership/role model. Do not trust a tenant ID supplied by the client without server-side verification.
- Enforce tenant boundaries in database policies and server-side authorization, not only UI filters.
- Test SELECT, INSERT, UPDATE and DELETE separately for anonymous, authenticated, tenant member, wrong tenant, elevated role and service role where relevant.
- Check both `USING` and `WITH CHECK` behavior for policies; ensure updates cannot move rows across tenants.
- Review joins, views, RPCs, functions and storage policies for indirect data exposure.
- For `SECURITY DEFINER` functions, review owner, grants, `search_path`, input validation and the exact privileges required. Avoid broad grants and service-role use in clients.
- Verify that generated database types and application contracts match the deployed schema.

## 3. Safe Schema Evolution

Prefer:

**Expand -> Migrate/Backfill -> Verify -> Contract**

1. Expand: add backward-compatible columns/tables/indexes or optional fields; avoid immediately removing old contracts.
2. Deploy compatible readers/writers that tolerate old and new schema states.
3. Backfill in bounded, resumable, observable batches. Make the operation idempotent and safe to retry.
4. Verify counts, constraints, nulls, relationships, application behavior, access policies and old/new consumer compatibility.
5. Contract: remove obsolete columns/paths only after all consumers and deployed versions have migrated.

Before a risky migration, assess table size, lock behavior, write amplification, long transactions, replication lag, downtime, index build strategy, rollback and forward-fix. `CREATE INDEX CONCURRENTLY` has transaction and operational constraints; verify the PostgreSQL version and migration runner behavior. A destructive data migration may not be safely reversible; plan forward recovery or tested restore.

Never apply a production migration, delete data or change production RLS without explicit authorization for the target environment and action.

## 4. Query and Index Engineering

- Start with query shape, cardinality, realistic data volume and observed latency.
- Inspect `EXPLAIN` plans first. `EXPLAIN ANALYZE` executes the statement; use it only in a safe environment or when execution is explicitly safe and authorized.
- Check selectivity, sequential/index scans, join order, sort, filters, row estimates, lock contention and N+1 patterns.
- Add indexes for demonstrated query paths; account for write cost, storage, maintenance, composite column order, partial indexes and duplicate indexes.
- Use bounded pagination, appropriate ordering, selective projections and batch access. Avoid unbounded queries and overfetching.
- Size connection pools across instances and serverless concurrency; prevent connection storms.
- Introduce replicas, partitioning, sharding or caching only after evidence and a consistency plan.

## 5. Transactions, Concurrency and Idempotency

- Identify the invariant and the atomic boundary before choosing transaction isolation or locks.
- Prefer database constraints and atomic writes over read-then-write application checks vulnerable to races.
- Use optimistic version checks for appropriate contention; use row/advisory locks only with bounded duration and deadlock handling.
- Make retries safe with idempotency keys or deduplication records where side effects can repeat.
- For DB writes plus event publication, consider transactional outbox/inbox patterns when loss/duplication matters.

## 6. Privacy, LGPD and Sensitive Data

- Minimize collection, access, copies, exports and log exposure.
- Define purpose, ownership, access, retention, deletion/anonymization, audit and backup lifecycle.
- Treat health, financial and identifying data as sensitive. Use synthetic or masked data in development and tests.
- Do not claim LGPD compliance from a schema or policy review alone. Legal basis, notices, contracts, processor roles and retention obligations require appropriate organizational/legal review.

## 7. Data Change Deliverable

Provide: model/invariants, affected contracts, migration sequence, tenant/RLS matrix, performance evidence, data backfill/reconciliation plan, validation, rollback/forward-fix and production authorization requirements.
