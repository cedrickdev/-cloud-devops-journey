# 05 · AWS

**Estimate:** 8 weeks · **Application:** [Tasks API](../app/)

## 🎯 Objectives

By the end of this module, I can:

- Set up an AWS account safely: MFA, SSO, budget alerts
- Apply least privilege with IAM roles and policies
- Design a VPC with public and private subnets across two Availability Zones
- Deploy the Tasks API on **ECS Fargate** behind an ALB, with **RDS PostgreSQL** and Secrets Manager
- Send logs to CloudWatch and alarm on errors
- Keep costs under control and clean up every resource

**Prerequisites:** [03 · Docker](../03-docker/), [04 · CI/CD](../04-cicd/)

> **Rule for this module:** build each service once in the **console** to understand it, then rebuild it with the **CLI**. In module 06, everything is rebuilt with Terraform.

## Labs and checkpoints

### Lab 05.0 — Account setup and cost safety (do this first)

- [ ] Enable MFA on the root user, then stop using root
- [ ] Use **IAM Identity Center** (SSO) for daily access, with the AWS CLI configured via `aws sso login`
- [ ] Create an **AWS Budget** alert (e.g. 10 USD/month) by email
- [ ] Choose one region and stick to it

### Lab 05.1 — IAM

- [ ] Explain users, groups, roles, policies, and identity vs resource policies
- [ ] Write a least-privilege policy by hand for a single S3 bucket
- [ ] Explain why applications use **roles**, never access keys

### Lab 05.2 — VPC

- [ ] Build a VPC with public and private subnets across two Availability Zones
- [ ] Configure an Internet Gateway, route tables and a NAT gateway (and delete it after: it is expensive)
- [ ] Explain security groups vs NACLs

### Lab 05.3 — EC2

- [ ] Launch an instance, connect with **SSM Session Manager** (no open SSH port)
- [ ] Run the Tasks API container on it with a user-data script
- [ ] Put an Application Load Balancer in front of it

### Lab 05.4 — Storage and database

- [ ] Use S3: versioning, lifecycle rules, blocked public access
- [ ] Create an **RDS PostgreSQL** instance in private subnets
- [ ] Connect the Tasks API to RDS; `GET /ready` returns 200

### Lab 05.5 — Containers on AWS (ECR + ECS Fargate)

- [ ] Push the image to **Amazon ECR**
- [ ] Deploy the Tasks API on **ECS Fargate** behind the ALB
- [ ] Read the DB password from **Secrets Manager**, not from a plain environment variable
- [ ] Perform a rolling update to a new image version and roll back

### Lab 05.6 — CloudWatch basics

- [ ] Send container logs to CloudWatch Logs
- [ ] Create a CloudWatch alarm on ALB 5xx errors

### Lab 05.7 — Cleanup

- [ ] Delete every resource created in this module and confirm on the billing page that nothing is left running

## Module done when

- [ ] The Tasks API runs on ECS Fargate + RDS, reachable through an ALB
- [ ] An architecture diagram is in `notes/`
- [ ] Total cost of the module documented

## Free courses and labs

- [AWS Skill Builder](https://skillbuilder.aws/) — free digital courses, start with *AWS Cloud Practitioner Essentials* (**main resource**)
- [AWS Cloud Quest: Cloud Practitioner](https://aws.amazon.com/training/digital/aws-cloud-quest/) — free 3D game with real labs in an AWS sandbox (no bill)
- [AWS Educate](https://aws.amazon.com/education/awseducate/) — free learning paths and labs for students
- [AWS Workshops](https://workshops.aws/) — hundreds of free official step-by-step workshops (ECS, VPC, IAM…)
- [Amazon ECS Workshop](https://ecsworkshop.com/) — for lab 05.5
- [AWS Well-Architected Framework](https://aws.amazon.com/architecture/well-architected/)
- [AWS documentation](https://docs.aws.amazon.com/)
