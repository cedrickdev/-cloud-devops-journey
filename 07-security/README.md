# 07 · Security (DevSecOps)

**Estimate:** 3 weeks · **Application:** [Tasks API](../app/)

## 🎯 Objectives

By the end of this module, I can:

- Remove every long-lived secret from code, CI and laptops (OIDC, Secrets Manager, rotation)
- Apply and audit least privilege for every human and machine identity
- Secure the supply chain: SBOM, image signing, pinned dependencies
- Run automated security checks in CI: secrets, code, dependencies, IaC, DAST
- Protect data at rest and in transit, and enable AWS threat detection
- Write a threat model for an application

**Prerequisites:** [04 · CI/CD](../04-cicd/), [05 · AWS](../05-aws/), [06 · IaC](../06-iac/)

> Security is also practised in every module. This module reviews the whole chain end to end and fills the gaps.

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

## Free courses and labs

- [flAWS](http://flaws.cloud/) and [flAWS 2](http://flaws2.cloud/) — free AWS security challenges (S3, IAM, metadata, Lambda) — attacker and defender paths (**main lab**)
- [OWASP Top 10](https://owasp.org/www-project-top-ten/)
- [OWASP Juice Shop](https://owasp.org/www-project-juice-shop/) — vulnerable app to practise ZAP scans (lab 07.4)
- [AWS Workshops](https://workshops.aws/) — filter by *Security* for IAM, GuardDuty and secrets workshops
- [Trivy documentation](https://trivy.dev/) · [Checkov](https://www.checkov.io/) · [gitleaks](https://github.com/gitleaks/gitleaks) · [Sigstore cosign](https://docs.sigstore.dev/)
