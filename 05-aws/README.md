# 05 · AWS

**Estimate:** 8 weeks · **Application:** [Tasks API](../app/)

> **Rule for this module:** build each service once in the **console** to understand it, then rebuild it with the **CLI**. In module 06, everything is rebuilt with Terraform.

## Objectives

- Deploy the Tasks API on AWS with a production-like architecture.
- Apply least privilege with IAM.
- Keep costs under control.

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

## Resources

- [AWS Skill Builder](https://skillbuilder.aws/)
- [AWS documentation](https://docs.aws.amazon.com/)
- [AWS Well-Architected Framework](https://aws.amazon.com/architecture/well-architected/)
