# 10 · Projects

Portfolio projects built on the [Tasks API](../app/). Each project **reuses and extends the previous one**, so the repository tells one story: from a local app to a production-grade, observable platform.

## 🎯 Objectives

- Apply each group of modules on a realistic, end-to-end case instead of isolated labs
- Build one coherent story that a recruiter can follow in a few minutes
- Show evidence (diagrams, pipeline runs, dashboards, postmortems), not just claims

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

## Project 3 — Infrastructure as Code and security

**After modules:** 06 – 07

Takes the Project 2 infrastructure and **rewrites it entirely in Terraform**, then secures the whole delivery chain.

- [ ] All Project 2 infrastructure in Terraform, with remote state and `dev` / `prod` environments
- [ ] `terraform plan` on pull requests, `apply` after approval
- [ ] Security gates in CI: secrets, CVEs, IaC misconfigurations, signed images
- [ ] Full stack destroyed and recreated from the pipeline

**Demonstrates:** Infrastructure as Code, GitOps-style workflows for infrastructure, DevSecOps.

## Project 4 — Kubernetes and GitOps

**After module:** 08

- [ ] Tasks API packaged as a Helm chart
- [ ] Deployed on EKS (provisioned with the Project 3 Terraform code) by Argo CD
- [ ] Autoscaling, network policies, least-privilege service accounts

**Demonstrates:** Kubernetes, Helm, GitOps, cloud-native operations.

## Project 5 — Observability and incident response (capstone)

**After module:** 09

Makes the platform from Projects 3 – 4 observable and operable, then proves it under failure.

- [ ] Observability stack: Loki (logs), Prometheus (metrics), Tempo (traces), Grafana dashboards as code
- [ ] SLO-based alerts routed by Alertmanager, each linked to a runbook
- [ ] At least 3 game days (DB down, bad deploy, latency) with blameless postmortems
- [ ] At least 2 postmortem action items implemented and linked

**Demonstrates:** observability, SRE practices, incident response.
