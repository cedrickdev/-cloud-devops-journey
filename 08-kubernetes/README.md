# 08 · Kubernetes

**Estimate:** 8 weeks · **Application:** [Tasks API](../app/)

## 🎯 Objectives

By the end of this module, I can:

- Explain the Kubernetes architecture and its core objects
- Deploy, configure, scale and update an application with Deployments, Services, ConfigMaps and Secrets
- Configure health probes, resource limits and autoscaling
- Expose and secure workloads with Ingress, NetworkPolicies and RBAC
- Package an application with Helm and deploy it the GitOps way with Argo CD
- Run a workload on Amazon EKS provisioned with Terraform
- Troubleshoot failing pods quickly

**Prerequisites:** [03 · Docker](../03-docker/), [06 · IaC](../06-iac/)

> **Cost rule:** labs 08.1 → 08.5 run **locally** (kind or k3d). EKS is only used in lab 08.6, and destroyed right after.

## Labs and checkpoints

### Lab 08.1 — Local cluster and core objects

- [ ] Create a local cluster with **kind** or **k3d**
- [ ] Explain the control plane, nodes, kubelet and etcd
- [ ] Deploy the Tasks API with a **Deployment** and a **Service**, using `kubectl` only

### Lab 08.2 — Configuration and storage

- [ ] Pass configuration with a **ConfigMap** and the DB password with a **Secret**
- [ ] Run PostgreSQL with a PersistentVolumeClaim (for learning; RDS in real life)
- [ ] Explain why Kubernetes Secrets are not encrypted by default

### Lab 08.3 — Health, scaling and resources

- [ ] Configure **liveness** (`/health`) and **readiness** (`/ready`) probes
- [ ] Set resource requests and limits
- [ ] Autoscale with a **HorizontalPodAutoscaler** and prove it under load
- [ ] Perform a rolling update and a `kubectl rollout undo`

### Lab 08.4 — Networking and access

- [ ] Expose the API through an **Ingress** controller
- [ ] Restrict traffic with a **NetworkPolicy** (only the API can reach the database)
- [ ] Create a ServiceAccount with minimal **RBAC** permissions

### Lab 08.5 — Helm and GitOps

- [ ] Package the Tasks API as a **Helm chart** with `values-dev.yaml` and `values-prod.yaml`
- [ ] Install **Argo CD** and deploy the chart from Git
- [ ] Change the image tag in Git and watch Argo CD sync automatically

### Lab 08.6 — Amazon EKS

- [ ] Provision an EKS cluster with **Terraform** (reuse module 06)
- [ ] Deploy the Helm chart on EKS
- [ ] Use IAM roles for service accounts (IRSA or EKS Pod Identity) to read Secrets Manager
- [ ] `terraform destroy` and confirm the cost of the lab

### Lab 08.7 — Troubleshooting

- [ ] Diagnose `CrashLoopBackOff`, `ImagePullBackOff`, `Pending` and failing probes
- [ ] Write a troubleshooting cheatsheet (`describe`, `logs --previous`, `events`, `exec`, `port-forward`)

## Module done when

- [ ] A Git commit is the only thing needed to deploy a new version
- [ ] I can fix a broken deployment without searching online

## Free courses and labs

- [Introduction to Kubernetes (LFS158)](https://training.linuxfoundation.org/training/introduction-to-kubernetes/) — free Linux Foundation course (**main course**)
- [Kubernetes tutorials](https://kubernetes.io/docs/tutorials/) — official
- [Killercoda — Kubernetes](https://killercoda.com/kubernetes) and [CKAD scenarios](https://killercoda.com/killer-shell-ckad) — free browser clusters, exam-style exercises
- [Amazon EKS Workshop](https://www.eksworkshop.com/) — official free labs for lab 08.6
- [Kubernetes The Hard Way](https://github.com/kelseyhightower/kubernetes-the-hard-way) — optional, to understand every component
- [Helm documentation](https://helm.sh/docs/) · [Argo CD getting started](https://argo-cd.readthedocs.io/en/stable/getting_started/)
