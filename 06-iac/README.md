# 06 · Infrastructure as Code

**Estimate:** 6 weeks · **Tools:** Terraform (or OpenTofu), Ansible

## 🎯 Objectives

By the end of this module, I can:

- Describe AWS infrastructure in Terraform (or OpenTofu) and run the plan/apply/destroy cycle
- Manage state safely: remote backend, locking, import and drift
- Write reusable modules and deploy several environments from the same code
- Run Terraform from a CI pipeline with OIDC, reviews and approvals
- Configure servers idempotently with Ansible playbooks and roles
- Compare Terraform with CloudFormation, CDK and Pulumi

**Prerequisites:** [05 · AWS](../05-aws/)

## Labs and checkpoints

### Lab 06.1 — Terraform fundamentals

- [ ] Explain providers, resources, data sources, variables, outputs and locals
- [ ] Run the `init → plan → apply → destroy` cycle on an S3 bucket
- [ ] Use `terraform fmt` and `terraform validate`

### Lab 06.2 — Remote state

- [ ] Explain what state is and why it must never be committed
- [ ] Store state in an **S3 backend** with versioning, encryption and locking
- [ ] Use `terraform import` on a resource created by hand
- [ ] Detect and fix **drift** after a change made in the console

### Lab 06.3 — Modules and environments

- [ ] Write a reusable `network` module (VPC + subnets)
- [ ] Use a public registry module and explain the trade-offs
- [ ] Deploy `dev` and `prod` from the same code with separate state
- [ ] Pin provider and module versions

### Lab 06.4 — The Tasks API in Terraform

- [ ] VPC, ALB, ECS Fargate, ECR, RDS and Secrets Manager all in Terraform
- [ ] `terraform destroy` then `terraform apply` rebuilds a working stack from scratch
- [ ] Document the time from zero to a working URL

### Lab 06.5 — Terraform in CI/CD

- [ ] Run `fmt`, `validate`, `tflint` and `checkov` on every pull request
- [ ] Post the `terraform plan` output as a pull request comment
- [ ] `apply` only after merge, with manual approval for `prod`
- [ ] Authenticate CI to AWS with **OIDC** (no stored access keys)
- [ ] Estimate cost changes with Infracost (optional)

### Lab 06.6 — Ansible

- [ ] Explain push-based configuration management and idempotence
- [ ] Write an inventory and a playbook that hardens an Ubuntu server (users, SSH, `ufw`, updates)
- [ ] Turn it into a reusable **role**
- [ ] Use a dynamic AWS inventory for EC2 instances

### Lab 06.7 — Other IaC tools (notes only)

- [ ] Compare Terraform, CloudFormation, AWS CDK and Pulumi in a short note
- [ ] Build a golden AMI with **Packer** (optional)

## Module done when

- [ ] The full Tasks API infrastructure can be destroyed and recreated with one pipeline run
- [ ] No resource exists in AWS that is not described in code

## Free courses and labs

- [HashiCorp Terraform tutorials — AWS track](https://developer.hashicorp.com/terraform/tutorials/aws-get-started) — official and free (**main resource**)
- [Getting Started with OpenTofu (LFEL1009)](https://training.linuxfoundation.org/resources/) — free Linux Foundation course (search "OpenTofu")
- [Terraform Best Practices](https://www.terraform-best-practices.com/) — free ebook on structure, naming, modules
- [Ansible — Getting started](https://docs.ansible.com/ansible/latest/getting_started/index.html)
- [Red Hat interactive labs — Ansible](https://www.redhat.com/en/interactive-labs/ansible) — free browser labs (Red Hat account)
- [OpenTofu documentation](https://opentofu.org/docs/)
