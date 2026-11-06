# CI/CD & Release Engineering Playbook

Load for pipeline design, build automation, release governance, GitHub Actions, GitLab CI, Docker builds, artifact promotion, semantic versioning or rollback.

## 1. Pipeline Design: Fast Feedback Without Weakening Controls

A proportional pipeline commonly follows:

1. Validate event, branch, permissions and required inputs.
2. Install dependencies reproducibly from the lockfile.
3. Run formatting/lint, type-check and static validation.
4. Run focused unit tests, then integration/contract tests as appropriate.
5. Build an immutable artifact.
6. Run dependency, secret, container, license or supply-chain checks according to risk.
7. Deploy to a test/staging environment when configured and authorized.
8. Run smoke/acceptance checks and controlled production release.
9. Verify post-deploy health and business signals.

Fail fast on cheap deterministic checks, but do not skip necessary integration, security or migration gates. Do not disable checks merely to make a pipeline green.

## 2. GitHub Actions and GitLab CI

- Inspect the actual repository provider, branch protections, runners, environment rules and existing workflow conventions.
- Pin third-party actions/images to trusted versions or immutable references where appropriate; review permissions and supply-chain risk.
- Use least-privilege job permissions, isolated environments and protected deployment approvals.
- Avoid untrusted pull-request code receiving production secrets. Separate fork validation from privileged deployment workflows.
- Use OIDC federation/short-lived cloud credentials where supported instead of long-lived static keys.
- Masking is not a substitute for not printing secrets. Avoid shell tracing and commands that echo credentials.
- Keep artifacts immutable and traceable to commit, build, dependency lock and provenance.

## 3. Caching and Reproducibility

- Cache package downloads and build outputs only when keys include relevant lockfiles, runtime versions and build inputs.
- Define invalidation and restore-key behavior; stale caches must not change correctness.
- Do not cache secrets, private tokens or sensitive build artifacts in broadly accessible scopes.
- Prefer deterministic builds, pinned toolchains and lockfile-enforced installs. Document unavoidable nondeterminism.

## 4. Docker and Build Sandboxes

When containers are justified:

- Use multi-stage builds to separate build tools from runtime dependencies.
- Use minimal trusted base images, pinned versions/digests where practical, non-root runtime users and explicit health behavior.
- Avoid copying `.env`, credentials, `.git`, local caches or unrelated files into the build context; maintain `.dockerignore`.
- Scan images and dependencies where risk warrants; generate SBOM/provenance when supply-chain requirements justify it.
- Test the final runtime image, not only the builder stage.
- Use Docker/sandboxes for isolation and reproducibility, not as a default dependency for every project.

## 5. Versioning and Release Notes

- Use Conventional Commits only if adopted by the repository; keep scopes and breaking-change markers meaningful.
- Apply Semantic Versioning when a published package/API has explicit compatibility promises. Do not infer that every internal application requires SemVer.
- Automate changelog/version generation only after commit conventions and release policy are stable.
- Separate application versioning from database schema and API compatibility policies.

## 6. Deployment and Rollback

Select rolling, canary, blue-green or feature flags based on traffic, capacity, cost, compatibility and recovery speed. Define:

- Pre-deploy checks and migration order.
- Readiness, health and smoke checks.
- Success/failure thresholds tied to user impact.
- Rollback or roll-forward decision and responsible owner.
- Previous artifact/config retention.
- Compatibility of old/new application versions with the database and events.

Application rollback does not automatically reverse schema/data changes. Use expand-contract migrations and a forward-fix or restore plan when destructive rollback is unsafe.

## 7. Release Acceptance

Report workflow files changed, pipeline stages, permission model, secret handling, cache behavior, artifact provenance, environments, release/rollback strategy and checks actually run. Do not merge, publish or deploy without required authorization.
