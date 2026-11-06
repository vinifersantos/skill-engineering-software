# Test Engineering & Quality Strategy

Load when designing test strategy, creating substantial suites, validating critical business rules or improving test reliability. For small changes, use the relevant project conventions and the master skill's risk-proportionate validation rules.

## 1. Derive Tests from Requirements

For each changed behavior, identify:

- Expected successful behavior.
- Invalid input and authorization failures.
- Boundary values, empty states and missing data.
- Concurrency, retries, partial failure and duplicate execution where relevant.
- Compatibility with existing consumers and persisted data.
- Observable acceptance criteria.

Do not optimize for coverage percentage alone. A test should detect a meaningful regression and fail when the behavior is broken.

## 2. Select the Right Level

| Level | Use for | Main risk addressed |
| --- | --- | --- |
| Unit | Pure logic, transformations, validation, calculations | Incorrect local rules and edge cases |
| Integration | Database, services, filesystem, queues, module boundaries | Contract and persistence failures |
| Contract | API, events, RPC, schema and consumer compatibility | Silent producer/consumer drift |
| E2E | Critical user journeys and browser/runtime behavior | Integration and real workflow failures |
| Security | Authentication, authorization, tenant isolation, abuse and secrets | Unauthorized access and data exposure |
| Migration | Schema transitions, backfills, rollback/forward-fix | Data loss and mixed-version failures |
| Performance | Measured bottlenecks, concurrency and capacity | Latency, saturation and cost regression |

## 3. Determinism and Isolation

- Use controlled fixtures, clocks, random seeds and external-service fakes where appropriate.
- Avoid tests that depend on order, shared mutable state, live credentials or uncontrolled network calls.
- Reset database state safely and isolate tenants/test identities.
- Make asynchronous tests await actual completion; avoid arbitrary sleeps when event/state synchronization is available.
- Keep test data synthetic or masked. Never use production personal/clinical/financial data by default.

## 4. Critical Data and Authorization Tests

- Test tenant A cannot read/write tenant B data across direct queries, joins, RPCs, storage and exports.
- Test role boundaries, anonymous requests, expired/invalid sessions and service-role paths.
- Test transaction invariants, duplicate requests, retries, concurrent updates and idempotency.
- For migrations, test both old/new application compatibility, backfill restart, constraint validation and recovery path.

## 5. Property, Fuzz and Mutation Testing

Use property-based or fuzz testing when input space is broad or parsing/validation is complex. Use mutation testing only when it helps assess whether important assertions are meaningful and the cost is justified. Do not add advanced testing frameworks solely to increase process complexity.

## 6. Failure Handling and Reporting

- Run the narrowest relevant test first; expand based on risk.
- Record exact commands and results.
- Separate pre-existing failures, flaky tests, environment failures and regressions.
- Follow the master two-attempt circuit breaker for corrective edits.
- Report missing test coverage as a risk, not as a successful validation.
