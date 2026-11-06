# Distributed Systems and Resilience Playbook

Load when calls cross process/network boundaries, state is replicated, events are asynchronous, multiple writers compete, or an outage demonstrates partial failure. Prefer a single reliable service when distribution adds no business value.

## 1. Classify the Failure Model Before Choosing Patterns

Ask what fails: slow dependency, dropped/reordered/duplicated message, overloaded queue, process crash, network partition, stale read, clock skew, conflicting write, partial transaction or region outage. State correctness guarantees separately from availability goals.

For every external dependency define: deadline (end-to-end and per hop), cancel propagation, max concurrent requests, bounded queue/backpressure, retryability, circuit-breaker threshold if warranted, fallback semantics and user-visible behavior. Avoid retry multiplication across multiple layers.

### Safe retry policy

- Retry *transient* failures only when the operation is idempotent or has a correct deduplication strategy.
- Bound attempt count or total elapsed deadline, use exponential backoff **with jitter** and respect server throttling signals.
- Propagate deadline/cancellation; apply a concurrency limit and expose attempt metrics.
- Do not retry blindly on authentication errors, invalid input or payment/webhook effects without idempotency guarantees.
- Test retry storm and downstream outage scenarios; favor SDK policy if known correct for the workload.

See AWS Reliability guidance on retries: https://docs.aws.amazon.com/wellarchitected/latest/framework/rel_mitigate_interaction_failure_limit_retries.html

## 2. Async Message and Event Patterns

Choose deliberately:
- **Work queue:** distribute independent jobs to workers; throughput/backpressure/retry/DLQ concerns.
- **Pub/sub:** fan out notifications to multiple consumers; consumers manage idempotency and ordering assumptions.
- **Domain events:** represent facts that occurred; evolve schemas compatibly and avoid leaking internal state.
- **Scheduled jobs:** recurrent tasks requiring concurrency, retry and idempotency controls.
- **Saga:** coordinate a multi-step business process with compensations when a single ACID transaction is unavailable; not an automatic rollback guarantee.

Specify delivery guarantees (commonly at-least-once), retention, ordering key, reprocessing policy, poison-message handling, DLQ inspection/redrive, schema evolution and observability (queue age, retries, failures). Distinguish command versus event semantics.

For DB change + message publication, consider **transactional outbox** to avoid lost publication and **inbox/deduplication** to manage duplicate consumption. Make side effects safe on replay. Do not promise end-to-end exactly-once without proving the entire chain.

## 3. Consistency, Replication and Coordination

- **CAP:** a network partition forces a trade-off between availability and strong consistency for the affected operation; it does not mean any system always chooses only two of three in normal operation.
- **Eventual consistency:** state expected convergence conditions and acceptable staleness; expose reconciliation/status instead of assuming immediate reads.
- **Read replica:** may lag; do not route read-after-write-critical operations to a potentially stale replica without a consistency strategy.
- **Sharding/partitioning:** first prove scale bottleneck; document cross-shard joins/transactions, key choice, migrations and hot partitions.
- **Leader election and distributed locks:** scrutinize leases, fencing tokens, failover, split-brain and expired ownership; a mutex across processes is not a durable exclusive-work guarantee.
- **Optimistic locking:** compare a version/etag in an atomic write; handle conflict/retry; suitable for moderate contention.
- **Pessimistic locking:** use only when required by contention/invariant; keep lock duration bounded and plan for deadlock handling.
- **Clock skew:** do not use wall clocks as the sole arbiter of exclusive ownership; use monotonic time for elapsed durations where available and server-controlled timestamps/sequence guarantees when needed.

## 4. Network Partition and Chaos Test Matrix

Test where proportional to risk:
- downstream delay or timeout; circuit open/half-open and recovery;
- duplicates, reordering, poison payload and replay after crash;
- queue surge and worker slowdown (backpressure, capacity, eventual recovery);
- simultaneous writes, stale replicas, partial transaction and lost acknowledgment;
- leader/lock lease expiry, network split, clock drift and restart;
- regional failure, failover and data reconciliation if architecture uses regions.

Measure lost or duplicated business effects, backlog age, tail latency, available capacity and recovery time, not only whether a process survived. Use staged fault injection and explicit authorization for production chaos experiments.

## 5. Decision Output

Report: requirement/invariant -> failure mode -> chosen mechanism -> consistency/delivery guarantee -> operator cost -> negative test -> monitoring signal. Make explicit what is **not** needed yet (e.g. Kafka, Saga, cross-region consensus, distributed locks).
