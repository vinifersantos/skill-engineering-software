# Data, Runtime and Performance Playbook

Load for slow requests, database bottlenecks, memory or concurrency bugs, high-throughput workloads, caching, or capacity decisions. Prefer measurement and smallest safe optimization over speculative infrastructure.

## 1. Evidence Before Tuning

Capture baseline and target: load distribution, RPS/throughput, queueing time, p50/p95/p99 latency, error rate, CPU, memory/GC pauses, DB connections, query duration, cache hit rate and saturation. Segment by route, tenant and request size only with privacy-safe low-cardinality labels. For load tests use realistic concurrency, data and think times; guard production from uncontrolled stress.

Tail latency often dominates user experience under fan-out; do not optimize solely for mean latency. Distinguish throughput from response time and look for bottlenecks moved elsewhere. Estimate marginal cost before capacity changes.

## 2. Database Read/Write Efficiency

- Diagnose with query plans and actual execution metrics, not just SQL appearance.
- Check missing/selectivity-mismatched indexes, unnecessary scans, bad sort/joins, lock contention, N+1 access patterns, unbounded queries and overfetching.
- Compare batching, proper pagination, preloading and selective caching; verify behavior with representative data.
- Size connection pools against database maximum, app replicas and serverless concurrency; avoid connection storms and unbounded retries.
- Evaluate read replicas only when read volume and stale-read tolerance justify them; monitor replication lag.
- Use partitioning when lifecycle/maintenance or access patterns warrant it; use sharding only after proving a single logical database is inadequate.
- Treat migrations as expand -> migrate/backfill -> verify -> contract; respect locks and long-running jobs; maintain compatible readers/writers during rolling deployments.
- Treat schema version as a contract; verify old and new consumers during rollout. Call a specialist PostgreSQL/Supabase skill if available.

## 3. Cache Correctness

Select a cache only for a demonstrated hot read/expensive computation. Define cache key/tenant scope, TTL, consistency expectation, invalidation event, stampede control, max memory, eviction and cold miss fallback. If a CDN is involved, verify public/private headers. Include tests for stale and cross-tenant data. Cache invalidation is a correctness problem, not merely a latency optimization.

## 4. Concurrency, Thread Safety, Memory

For race conditions, reproduce with concurrency, identify shared mutable state and atomicity boundaries, then use transactions, locks, immutability or serial ownership as appropriate. Distinguish thread safety from process or distributed safety. For deadlocks, list lock order and hold duration. For memory leaks and GC pressure, measure allocation/retention, open connections, event listeners, stale caches and unbounded buffers; compare profiles under a sustained workload.

For asynchronous systems enforce bounded work-in-progress and backpressure (reject, buffer with limits, pause producers or shed load explicitly). Test recovery after saturation rather than simply adding workers. Use horizontal vs vertical scaling according to bottleneck, statefulness, startup cost and operational constraints.

## 5. Serverless and Cold Starts

When runtime is serverless, check provider limits, concurrency caps, cold-start distribution, DB pool amplification, long-tail latency, job duration, retries and spend. Optimize initialization only if observed user-visible impact warrants it. Do not treat serverless as infinitely scalable or as requiring zero operational planning.

## 6. Performance Change Deliverable

Provide a profile/trace and baseline hypothesis, proposed bottleneck fix, controlled benchmark, before/after results, statistical caveats, correctness/rollback tests and capacity/cost delta. Do not claim a speedup without measurement.

For entity modeling, PostgreSQL/Supabase RLS, migration sequencing and data lifecycle, also load `database-engineering.md`.
