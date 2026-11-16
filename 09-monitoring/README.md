# 09 · Observability and Incident Management

**Estimate:** 6 weeks · **Application:** [Tasks API](../app/)

## 🎯 Objectives

By the end of this module, I can:

- Explain monitoring vs observability, the golden signals and the RED/USE methods
- Collect **logs** with Loki, **metrics** with Prometheus and **traces** with OpenTelemetry/Tempo
- Build Grafana dashboards as code and link metrics, logs and traces
- Define SLOs and error budgets, and alert on user-facing symptoms with Alertmanager
- Write runbooks and run an incident process (severity, roles, MTTD/MTTR)
- Simulate incidents (game days) and write **blameless postmortems** with action items

**Prerequisites:** [08 · Kubernetes](../08-kubernetes/)

> Deploying is half of the job. A DevOps engineer is also responsible for what runs in production: knowing **when** it breaks, finding **why** quickly, fixing it, and making sure it **does not happen again**.

## Stack

| Signal      | Collect                        | Store                 | Visualise / alert              |
| ----------- | ------------------------------ | --------------------- | ------------------------------ |
| Logs        | Grafana Alloy                  | **Loki**              | Grafana                        |
| Metrics     | Prometheus (scrape `/metrics`) | Prometheus            | **Grafana**, **Alertmanager**  |
| Traces      | OpenTelemetry SDK              | Tempo (or Jaeger)     | Grafana                        |
| AWS-native  | CloudWatch agent / Container Insights | CloudWatch     | CloudWatch dashboards & alarms |

Local setup: Docker Compose (module 03) first, then kube-prometheus-stack + Loki on the Kubernetes cluster (module 08).

## Labs and checkpoints

### Lab 09.1 — Observability fundamentals (notes)

- [ ] Explain monitoring vs observability
- [ ] Explain the **golden signals** (latency, traffic, errors, saturation), RED and USE methods
- [ ] Explain what each signal answers: metrics → *is something wrong?*, logs → *what happened?*, traces → *where is it slow?*

### Lab 09.2 — Structured logs with Loki

- [ ] Switch the API to **JSON logs** with a request ID on every line
- [ ] Ship container logs to **Loki** with **Grafana Alloy**
- [ ] Write LogQL queries: errors by endpoint, slow requests, all lines for one request ID
- [ ] Explain why high-cardinality values (user IDs, request IDs) must not be Loki labels
- [ ] Set a log retention period and document it

### Lab 09.3 — Metrics with Prometheus

- [ ] Add a `/metrics` endpoint to the API (request count, latency histogram, errors)
- [ ] Scrape it with **Prometheus**, plus node and container metrics (node-exporter, cAdvisor)
- [ ] Explain counter, gauge and histogram with examples from the API
- [ ] Write PromQL queries: request rate, error ratio, p95 latency

### Lab 09.4 — Dashboards with Grafana

- [ ] Build a service dashboard with the golden signals for the Tasks API
- [ ] Link metrics → logs (jump from an error spike to the matching Loki lines)
- [ ] Provision dashboards and data sources **as code** (JSON/YAML in Git, no manual clicks)

### Lab 09.5 — SLOs and alerting

- [ ] Define SLIs and an SLO (e.g. 99.5% of requests succeed and 95% are under 300 ms, over 30 days)
- [ ] Calculate the **error budget** and explain how it guides release decisions
- [ ] Write Prometheus alert rules on symptoms (error rate, latency, burn rate), not only on causes (CPU)
- [ ] Route alerts with **Alertmanager** to email, Slack or Discord, with grouping and silences
- [ ] Every alert links to a **runbook** in [`runbooks/`](./runbooks/)

### Lab 09.6 — Distributed tracing

- [ ] Instrument the API with **OpenTelemetry** (HTTP + SQLAlchemy)
- [ ] Send traces to **Tempo** and view a request from HTTP call to SQL query
- [ ] Link traces ↔ logs with the trace ID

### Lab 09.7 — AWS-native monitoring

- [ ] CloudWatch dashboard for ALB, ECS and RDS
- [ ] CloudWatch alarms (ALB 5xx, RDS CPU and free storage) to SNS
- [ ] Enable Container Insights on ECS and compare it with the Prometheus/Grafana approach
- [ ] All of it defined in **Terraform**, not in the console

### Lab 09.8 — Incident management process

- [ ] Define **severity levels** (SEV1 → SEV3) with examples for the Tasks API
- [ ] Describe incident roles: incident commander, communications, responders
- [ ] Write the incident workflow: detect → triage → mitigate → resolve → postmortem
- [ ] Write at least 3 **runbooks** from the [template](./runbooks/TEMPLATE.md) (API down, DB unreachable, high latency)
- [ ] Explain MTTD, MTTA and MTTR, and how to measure them

### Lab 09.9 — Game days: incident simulations

Break the system on purpose, then respond as if it were real (timer on, runbook in hand).

- [ ] **Scenario 1:** database stopped → `/ready` fails, alert fires
- [ ] **Scenario 2:** bad deployment (bug in a new image) → error rate rises, rollback
- [ ] **Scenario 3:** latency injected (slow SQL query or `tc netem`) → latency SLO burns
- [ ] **Scenario 4:** disk or memory exhaustion → container restarts (OOMKilled)
- [ ] For each scenario: time to detect, time to mitigate, what helped, what was missing

### Lab 09.10 — Blameless postmortems

- [ ] Write a postmortem for each game day using the [template](./postmortems/TEMPLATE.md)
- [ ] Include a precise timeline, impact, root cause (5 whys) and **action items with an owner**
- [ ] Implement at least 2 action items (new alert, better runbook, code fix…) and link the commits
- [ ] Read 3 public postmortems (e.g. Cloudflare, GitLab, AWS) and write what I learned

## Folder structure

```text
09-monitoring/
├── notes/
├── labs/
├── runbooks/       # one runbook per alert
└── postmortems/    # one postmortem per incident or game day
```

## Module done when

- [ ] One dashboard tells me whether the API is healthy in under 10 seconds
- [ ] Every alert is actionable and has a runbook
- [ ] At least 3 incidents simulated, resolved and documented in a blameless postmortem
- [ ] I can explain an incident, from alert to fix, in a job interview

## Free courses and labs

**Courses and labs**

- [Loki tutorial](https://grafana.com/docs/loki/latest/get-started/quick-start/tutorial/) — Loki + Alloy + Grafana with Docker Compose, also as a [Killercoda sandbox](https://killercoda.com/grafana-labs) (**start here**)
- [Grafana Play](https://play.grafana.org/) — explore real dashboards for free
- [Prometheus — Getting started](https://prometheus.io/docs/prometheus/latest/getting_started/)
- [Getting Started with OpenTelemetry (LFS148)](https://training.linuxfoundation.org/training/getting-started-with-opentelemetry-lfs148/) — free Linux Foundation course with hands-on labs
- [Grafana documentation](https://grafana.com/docs/) — Grafana, Loki, Tempo, Alloy

**SRE, incidents and postmortems**

- [Google SRE book](https://sre.google/sre-book/table-of-contents/) — free online: monitoring, alerting, incident management, postmortems
- [Google SRE workbook](https://sre.google/workbook/table-of-contents/) — SLOs and alerting on SLOs
- [PagerDuty Incident Response guide](https://response.pagerduty.com/) — roles, severity, process
- [Collection of public postmortems](https://github.com/danluu/post-mortems) — real incidents to read for lab 09.10
