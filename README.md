# Cloud & DevOps Journey

> Learning Cloud and DevOps engineering through hands-on labs, practical projects, and clear technical documentation.

## About this repository

I'm a backend developer expanding my skills into **Cloud & DevOps engineering with AWS**.

This repository is my public learning journal. It contains the concepts I study, the experiments I run, the problems I solve, and the projects I build along the way.

**Primary goal:** design, deploy, automate, secure, and monitor reliable cloud applications — not just complete courses or collect certificates.

**Learning pace:** around 8 hours per week, alongside my studies.  
**Learning approach:** understand → practice → document → repeat without a tutorial.

## Learning roadmap

Progress is tracked with checkboxes. A checked item means I have completed the corresponding lab or learning milestone.

| Module                              | Main topics                                   | Progress   |
| ----------------------------------- | --------------------------------------------- | ---------- |
| [00 · Roadmap](./00-roadmap/)       | Goals, weekly plans, learning reviews         | ⬜ Planned |
| [01 · Linux](./01-linux/)           | CLI, users, permissions, processes, SSH, Bash | ⬜ Planned |
| [02 · Networking](./02-networking/) | TCP/IP, DNS, HTTP(S), ports, firewalls        | ⬜ Planned |
| [03 · Docker](./03-docker/)         | Images, containers, volumes, Compose          | ⬜ Planned |
| [04 · CI/CD](./04-cicd/)            | GitHub Actions, tests, build, deployment      | ⬜ Planned |
| [05 · AWS](./05-aws/)               | IAM, EC2, S3, VPC, CloudWatch, ECS            | ⬜ Planned |
| [06 · Terraform](./06-terraform/)   | Infrastructure as Code, state, modules        | ⬜ Planned |
| [07 · Kubernetes](./07-kubernetes/) | Pods, Deployments, Services, Helm             | ⬜ Planned |
| [08 · Monitoring](./08-monitoring/) | Logs, metrics, alerts, Prometheus, Grafana    | ⬜ Planned |
| [09 · Projects](./09-projects/)     | End-to-end portfolio projects                 | ⬜ Planned |

> **Note:** All milestones are initially marked _Planned_. I update them only when the work is actually completed.

## 🛠️ Tech stack I'm learning

| Area                       | Tools and technologies                 |
| -------------------------- | -------------------------------------- |
| Operating systems          | Linux (Ubuntu), Bash, SSH              |
| Version control            | Git, GitHub                            |
| Containers                 | Docker, Docker Compose                 |
| CI/CD                      | GitHub Actions                         |
| Cloud                      | Amazon Web Services (AWS)              |
| Infrastructure as Code     | Terraform                              |
| Orchestration              | Kubernetes, Helm                       |
| Observability              | Amazon CloudWatch, Prometheus, Grafana |
| Applications used for labs | PHP / CodeIgniter, REST APIs, MySQL    |

The list above describes the **learning scope**, not technologies I claim to have mastered.

## Repository structure

```text
cloud-devops-journey/
├── 00-roadmap/       # Goals, schedules, weekly reviews
├── 01-linux/         # Linux notes, labs, Bash scripts
├── 02-networking/    # Networking fundamentals and exercises
├── 03-docker/        # Dockerfiles and Compose labs
├── 04-cicd/          # CI/CD pipelines and GitHub Actions
├── 05-aws/           # Cloud infrastructure and AWS labs
├── 06-terraform/     # Infrastructure as Code
├── 07-kubernetes/    # Kubernetes manifests and labs
├── 08-monitoring/    # Monitoring and observability
├── 09-projects/      # End-to-end projects
└── README.md
```

Each module is intended to include:

- `README.md` — objectives, topics, and module progress;
- `notes/` — concise explanations in my own words;
- `labs/` — reproducible exercises with commands and results;
- `scripts/` or configuration files — when relevant;
- `cheatsheet.md` — useful commands and quick references, when needed.

## Planned portfolio projects

### Project 1 — Containerized backend application

Containerize a **Java SpingBoot API** using Docker Compose. Include persistent storage, environment configuration, health checks, and clear setup instructions.

**Demonstrates:** Docker fundamentals, networking, debugging, and documentation.

### Project 2 — Automated AWS deployment

Build a CI/CD pipeline with **GitHub Actions**, publish a Docker image to **Amazon ECR**, and deploy the application to **Amazon ECS**. Manage permissions securely and document deployment and rollback steps.

**Demonstrates:** AWS, CI/CD, IAM, containers, and deployment automation.

### Project 3 — Infrastructure as Code and observability

Provision infrastructure with **Terraform**, deploy a sample workload, and add logging, metrics, and alerts. Practice troubleshooting and cost cleanup.

**Demonstrates:** Infrastructure as Code, monitoring, security, and operations.

> These are **planned projects**, not completed work. Finished projects will link to their own folders and include architecture diagrams, setup instructions, and evidence of testing.

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
- [ ] Provision cloud resources with Terraform.
- [ ] Deploy and troubleshoot a Kubernetes workload.
- [ ] Configure logs, metrics, alerts, and basic incident diagnostics.
- [ ] Publish at least one documented, end-to-end portfolio project.

## Certifications (planned)

- **Optional fundamentals:** AWS Certified Cloud Practitioner.
- **Primary target:** AWS Certified CloudOps Engineer – Associate, once my hands-on skills are ready.

Certifications will be marked as earned **only after passing the official exam**.

## Official learning resources

- [Ubuntu Server documentation](https://documentation.ubuntu.com/server/)
- [Docker documentation](https://docs.docker.com/get-started/)
- [GitHub Actions documentation](https://docs.github.com/en/actions)
- [AWS Skill Builder](https://skillbuilder.aws/)
- [AWS documentation](https://docs.aws.amazon.com/)
- [Terraform tutorials](https://developer.hashicorp.com/terraform/tutorials)
- [Kubernetes tutorials](https://kubernetes.io/docs/tutorials/)
- [Prometheus documentation](https://prometheus.io/docs/)

## Security and cost awareness

This is a learning repository. I will **never commit credentials, private keys, `.env` files containing secrets, or AWS access keys**. I will use safe credential handling, follow least-privilege principles, monitor AWS costs, and remove temporary lab resources after use.

---

_Learning in public, one lab at a time._
