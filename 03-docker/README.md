# 03 · Docker

**Estimate:** 3 weeks · **Application:** [Tasks API](../app/)

## Objectives

- Package the Tasks API into a small, secure, reproducible image.
- Run a multi-service stack (API + PostgreSQL) with Docker Compose.
- Debug containers confidently.

## Labs and checkpoints

### Lab 03.1 — Docker fundamentals

- [ ] Explain image vs container vs layer vs registry
- [ ] Use `run`, `ps`, `logs`, `exec`, `inspect`, `stop`, `rm`
- [ ] Explain that containers are Linux processes (namespaces + cgroups)

### Lab 03.2 — Dockerfile for the Tasks API

- [ ] Write `app/Dockerfile` from scratch (no copy-paste)
- [ ] Use a **multi-stage build** and a slim base image
- [ ] Run as a **non-root user**
- [ ] Add a `.dockerignore`
- [ ] Add a `HEALTHCHECK` on `/health`
- [ ] Final image size documented (target: under 200 MB)

### Lab 03.3 — Volumes and networks

- [ ] Explain bind mounts vs named volumes
- [ ] Persist PostgreSQL data in a named volume and prove it survives `docker compose down`
- [ ] Explain how containers reach each other by service name

### Lab 03.4 — Docker Compose stack

- [ ] Write `app/compose.yaml` with `api` + `db` (PostgreSQL)
- [ ] Configure the API with environment variables from `.env` (never committed)
- [ ] Use `depends_on` with a database health condition
- [ ] `GET /ready` returns 200 when the DB is up and 503 when it is stopped

### Lab 03.5 — Debugging and image hygiene

- [ ] Debug a container that exits immediately (logs, `exec`, override entrypoint)
- [ ] Tag images with a version and the Git commit SHA
- [ ] Scan the image with **Trivy** and fix at least one finding

## Module done when

- [ ] `docker compose up` starts the full stack from a clean clone with one command
- [ ] Setup steps documented in [`app/README.md`](../app/README.md)

## Resources

- [Docker documentation](https://docs.docker.com/get-started/)
- [Dockerfile best practices](https://docs.docker.com/build/building/best-practices/)
