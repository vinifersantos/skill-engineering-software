# Coverage of the 111 Engineering Topics (User-Supplied Images)

This file is an optional traceability index and study roadmap, **not** a list of requirements to deploy every technique. The canonical operating instructions live in `../SKILL.md` and the topical playbooks below. The numbering preserves the images and maps each topic to a primary reference. Related subjects may also appear in other references.

## API, Networking and Delivery Contracts (`api-networking.md`)

1. Limite de Requisições — request rate limiting and burst policy.
2. Cache — purpose, scope, freshness and invalidation.
3. Balanceamento de Carga — ingress and backend load distribution.
4. Proxies Reversos — routing, TLS termination and origin protection.
5. API Gateways — API control plane and request governance.
9. Descoberta de Serviços — runtime service resolution.
22. WebSockets — bidirectional event connection.
23. Long Polling — server-held request updates.
24. Server-Sent Events — one-way server stream.
48. CDN — content delivery and origin reduction.
49. Cache na Borda — shared edge cache correctness.
50. Invalidação de Cache — freshness and event invalidation.
97. DNS — resolution, TTL, stale records and failover.
98. TCP vs UDP — transport and behavior trade-offs.
99. HTTP/2 e HTTP/3 — capabilities and infrastructure compatibility.
100. gRPC — typed RPC and streaming.
101. Webhooks — signature, replay, duplicate and delayed delivery handling.
102. Versionamento de API — contract compatibility and lifecycle.
103. Versionamento Semântico — appropriate use for package/release contracts.

## Distributed Systems, Reliability Patterns and Coordination (`distributed-systems.md`)

10. Circuit Breakers — failure isolation.
11. Timeouts — deadlines and cancellation.
12. Retries — eligible retry semantics.
13. Backoff Exponencial — jitter and bounded attempts.
14. Idempotência — safe repeated side effects.
15. Filas de Mensagens — workers, queue age and backpressure.
16. Pub/Sub — fan-out and subscriber responsibilities.
17. Arquitetura Orientada a Eventos — event contracts and ordering.
18. Transações Distribuídas — invariants and cross-service consistency.
19. Padrão Saga — compensating business workflows.
20. Dead Letter Queues — poison-message analysis and redrive.
21. Cron Jobs — recurrent, concurrent and retried work.
32. Replicação — availability, lag and data copies.
33. Eleição de Líder — exclusive ownership and split-brain risks.
34. Teorema CAP — trade-offs under partitions.
35. Consistência Eventual — convergence and stale reads.
36. Lock Otimista — atomic version compare and conflict handling.
37. Lock Pessimista — bounded lock critical sections.
38. Locks Distribuídos — leases, fencing and safety.
39. Condições de Corrida — shared state and atomicity.
40. Deadlocks — lock ordering and contention.
44. Backpressure — control work-in-progress.
95. Partições de Rede — partially connected failure mode.
96. Clock Skew — time uncertainty and lease assumptions.

## Database, Runtime and Performance (`data-performance.md`)

25. Índices no Banco — verified query plans and selectivity.
26. Otimização de Queries — profile before tuning.
27. Queries N+1 — batch/prefetch and bounded access.
28. Pool de Conexões — limit DB concurrency.
29. Réplicas de Leitura — lag and read-after-write contracts.
30. Sharding — distribution only after bottleneck evidence.
31. Particionamento — data lifecycle and access plans.
41. Vazamento de Memória — retained objects and capacity growth.
42. Coleta de Lixo — GC pressure and allocation profiles.
43. Thread Safety — shared mutable state and concurrency.
81. Migrações de Banco — expand/migrate/contract and recovery.
82. Versionamento de Schema — compatibility between app versions.
89. Cold Starts — initialization and tail latency.
90. Limites do Serverless — concurrency, duration, connections and cost.
91. Latência — request delay and queueing.
92. Throughput — sustained completed work over time.
93. Latência p99 — high-percentile latency.
94. Latência de Cauda — long-tail service behavior.

## CI/CD, Cloud Infrastructure and Release Engineering (`deployment-platform.md`)

6. CI/CD — automated validation and delivery.
7. Docker — reproducible container lifecycle.
8. Kubernetes — orchestration when justified.
45. Autoscaling — demand signals and bounds.
46. Escala Horizontal — add instances safely.
47. Escala Vertical — increase per-instance resources.
51. Feature Flags — exposure control and flag retirement.
52. Deploy Blue-Green — cutover and rollback behavior.
53. Releases Canário — progressive rollout with metrics.
54. Rolling Deploys — overlapping app versions and readiness.
55. Rollbacks — reversibility of code, config and data.
56. Health Checks — meaningful service health.
57. Liveness e Readiness Probes — safe Kubernetes restart/routing semantics; also startup probes.
88. Otimização de Custos — quantify capacity and reliability trade-off.
104. Infraestrutura como Código — reviewable reproducible changes.
105. Terraform — state, plan, lock and secrets.
106. Helm Charts — templating and rendered-manifest checks.
107. Cache de Build — correct cache invalidation and reproducibility.
108. Inferno de Dependências — version pinning, compatibility and supply chain.

## Observability, SRE and Production Operations (`reliability-operations.md`)

58. Monitoramento — useful health signals and dashboards.
59. Logs — structured events and sensitive-data redaction.
60. Rastreamento Distribuído — context propagation and spans.
61. Métricas — rates, errors, saturation and business signals.
62. Alertas — actionable paging and runbooks.
63. SLOs — explicit reliability targets.
64. SLIs — user-facing measurable indicators.
65. Error Budgets — failure allowance and release policy.
66. Observabilidade — diagnose unknown failure conditions.
83. Recuperação de Desastres — planned and exercised recovery.
84. Backups — retention, integrity and restoration tests.
85. Failover — tested controlled switching and failback.
86. Deploy Multirregião — data, routing, resilience and operational cost.
87. Engenharia do Caos — controlled hypotheses and fault drills.
109. Incidentes em Produção — containment, diagnosis and communications.
110. Plantão — ownership, escalation, fatigue and runbooks.
111. Postmortems — blameless learning and verified corrective actions.

## Security and Access Control (`security-application.md`)

67. Gestão de Segredos — lifecycle, storage and audit.
68. IAM — roles, least privilege and trust boundaries.
69. OAuth — delegated authorization and correct flows.
70. Rotação de JWT — key/token validity, renewal and revocation.
71. TLS — secure transport and certificate management.
72. Criptografia em Repouso — encrypted persisted data and access policy.
73. Criptografia em Trânsito — encryption between communication endpoints.
74. WAF — perimeter filtering with limits.
75. Proteção contra DDoS — layered edge and capacity controls.
76. CORS — browser origin policy, not an authorization system.
77. CSRF — browser session and cross-site request protection.
78. SQL Injection — query parameterization and privileges.
79. XSS — context-sensitive encoding and trusted UI handling.
80. SSRF — safe outbound requests and egress boundaries.

## How to Prioritize for a Project

- **Always inspect** regardless of scale: requirements, secure trust boundaries, data integrity, errors/timeouts for network dependencies, testability, secrets, least privilege, deterministic builds and rollback implications.
- **When going to production:** add meaningful monitoring, safe deployment, schema migration, backups/restore validation, basic abuse controls and incident ownership, proportional to customer impact.
- **When workload or architecture warrants:** apply queues/DLQs, streaming, observability tracing, SLOs, caches, rate limiting, replica consistency, autoscaling, canary and capacity tests.
- **Only with proven need and operator capability:** sharding, distributed locks/consensus, service mesh, Kubernetes, multiregion active-active and production chaos exercises.

For each candidate technique, ask: **Which verified problem does it solve? What new failure modes and ongoing costs does it create? How would we test that it improved the outcome?**
