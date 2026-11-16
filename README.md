# Cloud & DevOps Journey

> Learning Cloud and DevOps engineering through hands-on labs, practical projects, and clear technical documentation.

## About this repository

I'm a backend developer expanding my skills into **Cloud & DevOps engineering with AWS**.

This repository is my public learning journal. It contains the concepts I study, the experiments I run, the problems I solve, and the projects I build along the way.

**Primary goal:** design, deploy, automate, secure, and monitor reliable cloud applications — not just complete courses or collect certificates.

**Learning pace:** around 8 hours per week, alongside my studies (estimated ~42 weeks — see the [schedule](./00-roadmap/)).  
**Learning approach:** understand → practice → document → repeat without a tutorial.

## The common thread: one application, end to end

Every lab works on the same small application: the **[Tasks API](./app/)**, a Python / FastAPI REST API with PostgreSQL.  
The app is intentionally simple, so the effort goes into **operating** it rather than writing it:

```text
local run → Docker → CI/CD → AWS (ECR + ECS + RDS) → Terraform → security gates → Kubernetes → observability → incidents
```

## Learning roadmap

Each module has its own README with **labs and checkpoints**. A checkbox is ticked only when the checkpoint is actually completed.

| Module                                         | Main topics                                              | Estimate | Progress   |
| ---------------------------------------------- | -------------------------------------------------------- | -------- | ---------- |
| [00 · Roadmap](./00-roadmap/)                  | Goals, schedule, weekly reviews                          | —        | ⬜ Planned |
| [01 · Linux](./01-linux/)                      | CLI, users, permissions, systemd, SSH, Bash              | 3 weeks  | ⬜ Planned |
| [02 · Networking](./02-networking/)            | TCP/IP, CIDR, DNS, HTTP(S), TLS, reverse proxy, firewall | 2 weeks  | ⬜ Planned |
| [03 · Docker](./03-docker/)                    | Dockerfile, images, volumes, Compose, image scanning     | 3 weeks  | ⬜ Planned |
| [04 · CI/CD](./04-cicd/)                       | GitHub Actions, tests, build, registry, environments     | 3 weeks  | ⬜ Planned |
| [05 · AWS](./05-aws/)                          | IAM, VPC, EC2, S3, RDS, ECR, ECS Fargate, CloudWatch     | 8 weeks  | ⬜ Planned |
| [06 · Infrastructure as Code](./06-iac/)       | Terraform, remote state, modules, IaC in CI, Ansible     | 6 weeks  | ⬜ Planned |
| [07 · Security](./07-security/)                | Least privilege, OIDC, secrets, SBOM, scanning           | 3 weeks  | ⬜ Planned |
| [08 · Kubernetes](./08-kubernetes/)            | Workloads, probes, HPA, Ingress, Helm, Argo CD, EKS      | 8 weeks  | ⬜ Planned |
| [09 · Observability & incidents](./09-monitoring/) | Loki, Prometheus, Grafana, Tempo, SLOs, alerting, runbooks, incident response, postmortems | 6 weeks  | ⬜ Planned |
| [10 · Projects](./10-projects/)                | End-to-end portfolio projects                            | ongoing  | ⬜ Planned |

> **Note:** All milestones are initially marked _Planned_. I update them only when the work is actually completed.

## 🛠️ Tech stack I'm learning

| Area                   | Tools and technologies                                   |
| ---------------------- | -------------------------------------------------------- |
| Operating systems      | Linux (Ubuntu), Bash, SSH, systemd                       |
| Version control        | Git, GitHub                                              |
| Containers             | Docker, Docker Compose                                   |
| CI/CD                  | GitHub Actions                                           |
| Cloud                  | Amazon Web Services (AWS)                                |
| Infrastructure as Code | Terraform / OpenTofu, Ansible                            |
| Security               | IAM, OIDC, Secrets Manager, Trivy, Checkov, gitleaks     |
| Orchestration          | Kubernetes, Helm, Argo CD                                |
| Observability          | Prometheus, Grafana, Loki, Tempo, Alertmanager, OpenTelemetry, Amazon CloudWatch |
| Incident management    | SLOs and error budgets, runbooks, game days, blameless postmortems |
| Lab application        | Python, FastAPI, PostgreSQL                              |

The list above describes the **learning scope**, not technologies I claim to have mastered.

## Repository structure

```text
cloud-devops-journey/
├── 00-roadmap/       # Goals, schedule, weekly reviews
├── 01-linux/         # Linux notes, labs, Bash scripts
├── 02-networking/    # Networking fundamentals and exercises
├── 03-docker/        # Dockerfiles and Compose labs
├── 04-cicd/          # CI/CD pipelines and GitHub Actions
├── 05-aws/           # Cloud infrastructure and AWS labs
├── 06-iac/           # Terraform and Ansible
├── 07-security/      # DevSecOps
├── 08-kubernetes/    # Kubernetes manifests, Helm, GitOps
├── 09-monitoring/    # Observability, runbooks, incidents and postmortems
├── 10-projects/      # End-to-end projects
├── app/              # Tasks API — the application used in every lab
└── README.md
```

Each module contains:

- `README.md` — objectives, labs, **checkpoints** and the "module done when" criteria;
- `notes/` — concise explanations in my own words;
- `labs/` — reproducible exercises with commands and results (one file per lab, e.g. `labs/03.2-dockerfile.md`);
- `scripts/` or configuration files — when relevant;
- `cheatsheet.md` — useful commands and quick references, when needed.

## Planned portfolio projects

The projects build on each other — see [10 · Projects](./10-projects/) for full checkpoints.

1. **Containerised Tasks API** — Dockerfile, Compose stack with PostgreSQL, health checks, image scanning.
2. **Automated deployment to AWS** — GitHub Actions → ECR → ECS Fargate + RDS, OIDC, documented rollback.
3. **IaC, security and observability** — Project 2 rewritten in Terraform, security gates in CI, Grafana/Loki/Prometheus stack, SLO alerts, runbooks, game days and postmortems.
4. **Kubernetes and GitOps (stretch)** — Helm chart on EKS, deployed by Argo CD.

> These are **planned projects**, not completed work. Finished projects will include architecture diagrams, setup instructions, and evidence of testing.

## How I document each lab

Every lab should answer these questions:

1. **Objective:** What am I trying to achieve?
2. **Environment:** Which operating system, tools, and versions am I using?
3. **Steps:** Which commands and configuration changes are required?
4. **Validation:** How can I prove that it works?
5. **Troubleshooting:** What failed, why, and how did I fix it?
6. **Takeaways:** What did I learn, and can I repeat it without a tutorial?

## Learning milestones

- [ ] Administer a Linux server from the terminal.
- [ ] Write Bash scripts for routine tasks.
- [ ] Explain common network protocols and troubleshoot connectivity.
- [ ] Dockerize and run a multi-service application.
- [ ] Build a test-and-deploy CI/CD pipeline.
- [ ] Deploy and secure an application on AWS.
- [ ] Provision and manage cloud infrastructure with Terraform, from a pipeline.
- [ ] Remove every long-lived secret from code and CI.
- [ ] Deploy and troubleshoot a Kubernetes workload.
- [ ] Collect logs, metrics and traces, and alert on SLOs.
- [ ] Respond to an incident with a runbook and publish a blameless postmortem.
- [ ] Publish at least one documented, end-to-end portfolio project.

## Certifications (planned)

- **Optional fundamentals:** AWS Certified Cloud Practitioner.
- **Primary target:** AWS Certified CloudOps Engineer – Associate, once my hands-on skills are ready.
- **Optional:** HashiCorp Terraform Associate, CKAD.
- **Long-term goal:** AWS Certified DevOps Engineer – Professional.

Certifications will be marked as earned **only after passing the official exam**.

## Official learning resources

- [Ubuntu Server documentation](https://documentation.ubuntu.com/server/)
- [Docker documentation](https://docs.docker.com/get-started/)
- [GitHub Actions documentation](https://docs.github.com/en/actions)
- [AWS Skill Builder](https://skillbuilder.aws/)
- [AWS documentation](https://docs.aws.amazon.com/)
- [Terraform tutorials](https://developer.hashicorp.com/terraform/tutorials)
- [Ansible documentation](https://docs.ansible.com/)
- [Kubernetes tutorials](https://kubernetes.io/docs/tutorials/)
- [Prometheus documentation](https://prometheus.io/docs/)
- [Grafana documentation](https://grafana.com/docs/) (Grafana, Loki, Tempo)
- [Google SRE book](https://sre.google/sre-book/table-of-contents/)

## Security and cost awareness

This is a learning repository. I will **never commit credentials, private keys, `.env` files containing secrets, or AWS access keys**. CI authenticates to AWS with **OIDC** instead of stored keys, secrets live in AWS Secrets Manager, and a secret scanner runs before every commit.

On the cost side: an **AWS Budget alert** is set before the first lab, Kubernetes is practised locally before EKS, and every lab ends with a documented **teardown** (`terraform destroy` or manual cleanup).

---

_Learning in public, one lab at a time._
