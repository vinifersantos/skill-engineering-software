# Delivery, Infrastructure and Platform Playbook

Load when planning builds, CI/CD, infrastructure as code, container runtime, release strategies, autoscaling, cost or platform recovery. Start with actual provider and deployment constraints; do not presume Docker, Kubernetes or a multi-cloud topology.

## 1. Build/Delivery Pipeline

Recommend a proportional pipeline: reproducible dependency installation -> lint/typecheck -> unit/integration/contract tests -> security/dependency scans as warranted -> immutable artifact -> staging validation -> controlled release -> post-deploy verification. Check secret handling, provenance, build cache key correctness, artifact retention, environment parity and branch/protection policy. Never expose secret values in CI output.

Semantic versioning applies to releases where public compatibility promises make sense; define actual client/API compatibility separately. Avoid unreviewed automatic major upgrades and dependency drift. For incident rollback, retain previous artifacts and deployment config.

## 2. Select the Simplest Fitting Runtime

- **Managed PaaS/serverless:** often preferred for small teams and standard web apps; examine concurrency, cold starts, network/DB limits, region, reliability and cost.
- **Container/Docker:** use for reproducibility, isolation or provider requirements; small base image, multi-stage builds where useful, non-root runtime, pinned dependencies, health handling and supply-chain scanning.
- **Kubernetes:** justify via scale, multi-service needs, operational maturity and portability. Include resource requests/limits, scheduling, HPA, secrets, service discovery, rollout, network policies and runbooks only when relevant.
- **Helm:** treat charts and values as versioned templates; lint/template/diff and verify rendered manifests, secret injection and namespace-specific overrides.
- **Terraform/IaC:** version modules, review `plan`, secure remote state, locking, least-privilege credentials, drift detection, protected state/backups and explicit destructive-change approval. Never commit credentials or state with secrets.

## 3. Deploy Strategy: Select by Risk and Constraints

| Technique | Good fit | Operational caveat |
| --- | --- | --- |
| Rolling | Standard stateless service with compatible versions | Mixed app/schema versions, surge/unavailable capacity |
| Blue-green | Rapid environment switch/rollback when duplicate capacity affordable | Database/shared state cannot always be rolled back with traffic |
| Canary | Gradual exposure backed by metrics and fast rollback | Representative traffic, analysis windows and routing complexity |
| Feature flag | Decouple deployment from feature exposure | Flag lifecycle, ownership, authorization and consistency |
| Immediate rollback | Restore earlier known-good artifact/config | May be unsafe after destructive migration or irreversible write |

Use expand/migrate/contract for database schema transitions. Define deploy success as business and technical health (errors, p99, queue age, conversion if relevant), not simply 'pods running'. Prefer automatic rollback only with proven signals and guardrails.

## 4. Health, Capacity and Scaling

Distinguish:
- **Startup probe:** app initialization may be slow; protects against premature liveness failure.
- **Readiness:** remove unready instances from serving traffic, including during graceful shutdown.
- **Liveness:** restart irrecoverably stuck instances; do not tie directly to every transient downstream outage or trigger restart cascades.

Kubernetes reference: https://kubernetes.io/docs/tasks/configure-pod-container/configure-liveness-readiness-startup-probes/

Choose horizontal scaling for parallel/stateless work and vertical for per-instance resource pressure subject to provider limits. Understand saturation, cold starts, DB connection fan-out, queue consumers, sticky sessions, shared state and price curves. Set scale bounds and load-test capacity. Edge caching/CDN can reduce origin demand but introduces cache scope and invalidation concerns.

## 5. Regional Reliability, DNS, Backup and Spend

Before proposing multi-region, quantify RTO, RPO, residency, cost, data replication and conflict handling. Regional failover requires more than duplicate infrastructure: DNS/routing, secrets/config, consistency, health, data restoration and regular failover drills. Set explicit cutover/failback and operator procedures.

Review cost by actual drivers (compute idle, data egress, storage, logs, managed database, multi-AZ/region replication, retries and excessive traces). For cost optimization measure reliability/performance impact, not only invoice reduction.

## 6. Deliverable / Acceptance

Specify architecture rationale, infrastructure changes, CI gates, environmental checks, pre-deploy migration, rollout stages, observability gates, rollback/forward-fix strategy, credential handling, cost implication, failure drill and named owner. For any risky action, provide a safe dry-run first.

For detailed fail-fast pipeline design, GitHub Actions/GitLab CI, cache safety, Docker multi-stage builds, Conventional Commits and release automation, also load `ci-cd-release-engineering.md`. For tested backup restoration and business continuity, load `disaster-recovery.md`.
