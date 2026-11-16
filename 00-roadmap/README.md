# 00 · Roadmap

Goals, schedule and weekly reviews. This folder keeps the journey honest: what was planned, what was done, what slipped.

## 🎯 Objectives

By the end of this journey, I can:

- Take an application from a laptop to production on AWS, fully automated and described in code
- Secure it end to end, with no long-lived secrets
- Operate it: observe it, get alerted, respond to incidents and learn from them
- Prove all of this with a public, documented portfolio and an AWS certification

## Pace

- **~8 hours per week**, alongside my studies.
- Estimated total: **~42 weeks** (about 10 months) for modules 01 → 09, plus the projects.
- Estimates are a guide, not a deadline. If a module takes longer, I note why in the weekly review.

## Schedule (estimate)

| Module                                       | Estimate  | Weeks    |
| -------------------------------------------- | --------- | -------- |
| [01 · Linux](../01-linux/)                   | 3 weeks   | 1 – 3    |
| [02 · Networking](../02-networking/)         | 2 weeks   | 4 – 5    |
| [03 · Docker](../03-docker/)                 | 3 weeks   | 6 – 8    |
| [04 · CI/CD](../04-cicd/)                    | 3 weeks   | 9 – 11   |
| [05 · AWS](../05-aws/)                       | 8 weeks   | 12 – 19  |
| [06 · Infrastructure as Code](../06-iac/)    | 6 weeks   | 20 – 25  |
| [07 · Security](../07-security/)             | 3 weeks   | 26 – 28  |
| [08 · Kubernetes](../08-kubernetes/)         | 8 weeks   | 29 – 36  |
| [09 · Observability & incidents](../09-monitoring/) | 6 weeks | 37 – 42 |
| [10 · Projects](../10-projects/)             | continuous | built along the way |

## Certification plan

| Certification                                  | When                         | Status     |
| ---------------------------------------------- | ---------------------------- | ---------- |
| AWS Certified Cloud Practitioner (optional)    | During module 05             | ⬜ Planned |
| AWS Certified CloudOps Engineer – Associate    | After modules 05 – 06        | ⬜ Planned |
| HashiCorp Terraform Associate (optional)       | After module 06              | ⬜ Planned |
| CKAD (optional)                                | After module 08              | ⬜ Planned |
| AWS Certified DevOps Engineer – Professional   | Long-term goal               | ⬜ Planned |

## Weekly review

Create one file per week in [`weekly/`](./weekly/), named `YYYY-Www.md` (e.g. `2026-W47.md`):

```markdown
# Week 2026-W47

**Hours spent:** 8
**Module:** 01 · Linux

## Done
- Lab 01.2 — users, groups and permissions (all checkpoints ✅)

## Blocked / struggled with
- Sticky bit vs setgid on directories — re-read and wrote a note.

## Next week
- Lab 01.3 — processes and systemd
```

## General free resources

- [roadmap.sh — DevOps](https://roadmap.sh/devops) — visual map of the field
- [90DaysOfDevOps](https://github.com/MichaelCade/90DaysOfDevOps) — free community course covering the whole path
- [DevOps Exercises](https://github.com/bregman-arie/devops-exercises) — interview questions and exercises per topic
- Each module README lists its own **free courses and labs**.

## Checkpoints

- [ ] Weekly review habit running for 4 consecutive weeks
- [ ] Schedule reviewed and adjusted at the end of each module
