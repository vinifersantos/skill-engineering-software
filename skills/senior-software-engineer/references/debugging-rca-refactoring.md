# Debugging, Root-Cause Analysis & Refactoring

Load for complex defects, intermittent failures, production incidents, regressions, flaky tests, technical debt or behavior-preserving refactoring.

## 1. Evidence-Led Debugging

Use:

**Symptom -> Scope -> Timeline -> Hypotheses -> Probe -> Root Cause -> Fix -> Regression Protection**

- Define expected versus actual behavior, affected users/data, start time, frequency and reproducibility.
- Determine blast radius and whether the failure is correctness, security, availability, performance or data integrity.
- Build a timeline of code, dependency, configuration, data, infrastructure and deployment changes.
- Rank hypotheses by evidence, probability and blast radius. Record evidence for and against each.
- Choose the cheapest reliable probe: reproduction, minimal failing test, targeted log/trace/metric, query plan, config diff, lockfile diff or safe commit bisect.
- Change one relevant variable at a time where practical. Do not confuse correlation with causation.

## 2. Root-Cause Analysis

Separate:

- **Trigger:** event that exposed the failure.
- **Root cause:** underlying condition that made the failure possible.
- **Contributing factors:** design, process, dependency or operational conditions that increased likelihood/impact.
- **Detection gap:** why existing tests/telemetry/alerts did not catch it earlier.
- **Corrective actions:** prevention, detection, containment and recovery improvements.

Use Five Whys or fault-tree analysis as aids, not rituals. Avoid blame and avoid declaring a root cause without evidence. For incidents, preserve evidence and prioritize containment/data integrity before refactoring.

## 3. Minimal Safe Fix

- Correct the underlying cause with the smallest change that restores the required invariant.
- Add a regression test that would fail before the fix.
- Check adjacent contracts and failure paths.
- Validate in the safest available environment; never reproduce destructive effects against production without authorization.
- State residual uncertainty when the issue cannot be fully reproduced.

## 4. Refactoring Without Behavioral Drift

- Establish observable behavior and contracts before changing structure.
- Add characterization tests when behavior is legacy, undocumented or surprising.
- Refactor in small steps: extract, rename, move or simplify one coherent responsibility at a time.
- Preserve public APIs, serialized formats, database behavior, error semantics and timing assumptions unless change is requested.
- Compare before/after tests and, for critical behavior, outputs or traces.
- Remove code smells when they materially raise defect risk, cognitive load or change cost; do not refactor for aesthetic preference alone.
- Keep refactoring separate from feature changes when it improves reviewability and rollback.

## 5. Circuit Breaker

Follow the master Code-First rule: after two unsuccessful correction attempts, stop speculative edits, preserve repository state and report the exact blocker. Undo only changes attributable to the current task; never restore whole files over user work.

## 6. Debugging/Refactoring Deliverable

Report symptom, scope, timeline, ranked hypotheses, probes and evidence, confirmed or probable cause, minimal fix, regression coverage, residual uncertainty and operational follow-up.
