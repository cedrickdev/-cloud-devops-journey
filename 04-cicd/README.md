# 04 · CI/CD

**Estimate:** 3 weeks · **Tool:** GitHub Actions · **Application:** [Tasks API](../app/)

## Objectives

- Every push is automatically linted, tested and built.
- Every merge to `main` produces a versioned, scanned Docker image.
- Understand deployment strategies and rollback.

## Labs and checkpoints

### Lab 04.1 — First workflow

- [ ] Explain workflows, jobs, steps, runners, triggers
- [ ] Run `ruff` and `pytest` on every push and pull request
- [ ] Block merging into `main` when CI fails (branch protection)

### Lab 04.2 — Build and publish the image

- [ ] Build the Docker image in CI
- [ ] Push it to **GitHub Container Registry** with tags `sha-<commit>` and the version
- [ ] Use dependency and Docker layer caching; document the time saved

### Lab 04.3 — Quality and security gates

- [ ] Scan the image with Trivy in CI and fail on critical vulnerabilities
- [ ] Enable Dependabot for Python dependencies and GitHub Actions
- [ ] Use a matrix to test on two Python versions

### Lab 04.4 — Environments and secrets

- [ ] Use GitHub environments (`dev`, `prod`) with a manual approval on `prod`
- [ ] Store configuration in GitHub secrets and variables; nothing sensitive in YAML
- [ ] Write a reusable workflow or composite action

### Lab 04.5 — Deployment strategies (theory + notes)

- [ ] Explain rolling, blue/green and canary deployments with their trade-offs
- [ ] Write a rollback procedure for the Tasks API

## Module done when

- [ ] A pull request shows lint + tests + scan results automatically
- [ ] A merge to `main` publishes a tagged image with zero manual steps

## Resources

- [GitHub Actions documentation](https://docs.github.com/en/actions)
