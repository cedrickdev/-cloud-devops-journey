# 07 · Security (DevSecOps)

**Estimate:** 3 weeks · **Application:** [Tasks API](../app/)

> Security is also practised in every module. This module reviews the whole chain end to end and fills the gaps.

## Objectives

- No long-lived secrets anywhere: in code, in CI or on laptops.
- Least privilege for every identity, human or machine.
- Security checks run automatically in the pipeline.

## Labs and checkpoints

### Lab 07.1 — Identity and least privilege

- [ ] Review every IAM role used by the project and remove unused permissions (use IAM Access Analyzer)
- [ ] CI authenticates to AWS with **OIDC**; no `AWS_ACCESS_KEY_ID` exists anywhere
- [ ] Document who or what can access production, and how

### Lab 07.2 — Secrets management

- [ ] Compare Secrets Manager and SSM Parameter Store (cost, rotation, use cases)
- [ ] Enable automatic rotation for the RDS password
- [ ] Add a **secret scanner** (gitleaks) as a pre-commit hook and in CI

### Lab 07.3 — Supply chain

- [ ] Generate an **SBOM** for the Docker image (Syft or Trivy)
- [ ] Sign the image with **cosign** and verify the signature before deployment
- [ ] Pin GitHub Actions to a commit SHA

### Lab 07.4 — Code and infrastructure scanning

- [ ] Static analysis of the Python code (Bandit or Semgrep) in CI
- [ ] `checkov` or `trivy config` on Terraform with zero high findings, or each exception documented
- [ ] Run a basic DAST scan (OWASP ZAP baseline) against the deployed API

### Lab 07.5 — Network and data protection

- [ ] Database reachable only from the application's security group
- [ ] Encryption at rest (RDS, S3) and in transit (HTTPS on the ALB with ACM)
- [ ] Enable CloudTrail and GuardDuty, and read one finding

## Module done when

- [ ] A threat model of the Tasks API (one page) is written in `notes/`
- [ ] The pipeline fails automatically on a leaked secret, a critical CVE or an insecure Terraform change

## Resources

- [OWASP Top 10](https://owasp.org/www-project-top-ten/)
- [AWS Security documentation](https://docs.aws.amazon.com/security/)
