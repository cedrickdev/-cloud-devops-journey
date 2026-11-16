# 10 · Projects

Portfolio projects built on the [Tasks API](../app/). Each project **reuses and extends the previous one**, so the repository tells one story: from a local app to a production-grade, observable platform.

Each finished project gets its own folder with:

- an architecture diagram;
- setup and teardown instructions;
- evidence it works (screenshots, pipeline runs, test output);
- what went wrong and how it was fixed;
- the AWS cost of running it.

---

## Project 1 — Containerised Tasks API

**After modules:** 01 – 03

- [ ] Multi-stage, non-root Dockerfile with a health check
- [ ] Docker Compose stack: API + PostgreSQL with a persistent volume
- [ ] Environment-based configuration, `.env.example` provided
- [ ] Image scanned with Trivy
- [ ] One-command setup documented

**Demonstrates:** Docker, networking, configuration, debugging, documentation.

## Project 2 — Automated deployment to AWS

**After modules:** 04 – 05

- [ ] GitHub Actions pipeline: lint → test → build → scan → push to **ECR**
- [ ] Deployment to **ECS Fargate** behind an ALB, with **RDS PostgreSQL**
- [ ] Database password in Secrets Manager
- [ ] CI authenticates to AWS with OIDC
- [ ] Rollback procedure documented and tested

**Demonstrates:** AWS, CI/CD, IAM, containers, deployment automation.

## Project 3 — Infrastructure as Code, security and observability

**After modules:** 06 – 07, 09

Takes the Project 2 infrastructure and **rewrites it entirely in Terraform**, then makes it secure and observable.

- [ ] All Project 2 infrastructure in Terraform, with remote state and `dev` / `prod` environments
- [ ] `terraform plan` on pull requests, `apply` after approval
- [ ] Security gates in CI: secrets, CVEs, IaC misconfigurations
- [ ] Logs, metrics, dashboard, SLO-based alert
- [ ] One simulated incident with a postmortem
- [ ] Full stack destroyed and recreated from the pipeline

**Demonstrates:** Infrastructure as Code, DevSecOps, monitoring, operations.

## Project 4 (stretch) — Kubernetes and GitOps

**After module:** 08

- [ ] Tasks API on EKS, packaged with Helm
- [ ] Deployed by Argo CD from Git
- [ ] Autoscaling, network policies, least-privilege service accounts

**Demonstrates:** Kubernetes, Helm, GitOps, cloud-native operations.
