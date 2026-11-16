# 09 · Monitoring and Observability

**Estimate:** 4 weeks · **Application:** [Tasks API](../app/)

## Objectives

- Know at any moment whether the Tasks API works for its users.
- Get alerted before users notice a problem.
- Find the cause of an incident quickly using logs, metrics and traces.

## Labs and checkpoints

### Lab 09.1 — Structured logs

- [ ] Switch the API to **JSON logs** with a request ID
- [ ] Centralise logs (CloudWatch Logs on AWS, Loki on Kubernetes)
- [ ] Write three useful queries: errors by endpoint, slow requests, one request by ID

### Lab 09.2 — Metrics with Prometheus

- [ ] Add a `/metrics` endpoint to the API (request count, latency, errors)
- [ ] Scrape it with **Prometheus** (kube-prometheus-stack on the local cluster)
- [ ] Explain counter, gauge and histogram with examples from the API

### Lab 09.3 — Dashboards with Grafana

- [ ] Build a dashboard with the **golden signals**: traffic, errors, latency, saturation
- [ ] Store the dashboard as JSON in Git

### Lab 09.4 — SLOs and alerting

- [ ] Define an SLI and an SLO (e.g. 99% of requests under 300 ms over 30 days)
- [ ] Create alerts on symptoms (error rate, latency), not only on causes (CPU)
- [ ] Route alerts to email, Slack or Discord

### Lab 09.5 — Tracing

- [ ] Instrument the API with **OpenTelemetry**
- [ ] View a trace from HTTP request to database query (Tempo or Jaeger)

### Lab 09.6 — Incident simulation

- [ ] Break something on purpose (stop the DB, add latency, exhaust memory)
- [ ] Detect it through an alert, diagnose it with dashboards and logs, fix it
- [ ] Write a blameless **postmortem** in `notes/`

## Module done when

- [ ] One dashboard tells me whether the API is healthy in under 10 seconds
- [ ] At least one realistic incident detected, resolved and documented

## Resources

- [Prometheus documentation](https://prometheus.io/docs/)
- [Grafana documentation](https://grafana.com/docs/)
- [OpenTelemetry documentation](https://opentelemetry.io/docs/)
- [Google SRE book](https://sre.google/sre-book/table-of-contents/)
