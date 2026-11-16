# 04 · CI/CD

**Estimate:** 3 weeks · **Tool:** GitHub Actions · **Application:** [Tasks API](../app/)

## 🎯 Objectives

By the end of this module, I can:

- Explain workflows, jobs, runners and triggers in GitHub Actions
- Run lint and tests automatically on every push and pull request
- Build, tag, scan and publish a Docker image from CI
- Use environments, secrets and manual approvals for deployments
- Explain rolling, blue/green and canary deployments, and write a rollback procedure

**Prerequisites:** [03 · Docker](../03-docker/)

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

## Free courses and labs

- [GitHub Skills](https://skills.github.com/) — free interactive courses that run inside your own repository (**main resource**: start with the Actions courses)
- [GitHub Actions documentation](https://docs.github.com/en/actions)
- [GitHub Actions certification course (freeCodeCamp)](https://www.freecodecamp.org/news/pass-the-github-actions-certification-exam/) — full free video course
