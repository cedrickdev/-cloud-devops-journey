# Tasks API — the lab application

A deliberately small **Python / FastAPI** REST API used as the common thread of this repository.
The application stays simple on purpose: the learning goal is to **build, ship, secure and operate** it, not to write business logic.

The same app moves through every module:

```text
local run → Docker image → CI pipeline → AWS (ECR + ECS) → Terraform → Kubernetes → monitoring
```

## Endpoints

| Method | Path          | Purpose                                         |
| ------ | ------------- | ----------------------------------------------- |
| GET    | `/health`     | Liveness: the process is running                |
| GET    | `/ready`      | Readiness: the database is reachable (503 if not) |
| GET    | `/tasks`      | List tasks                                      |
| POST   | `/tasks`      | Create a task `{"title": "...", "done": false}` |
| GET    | `/tasks/{id}` | Get one task                                    |
| PUT    | `/tasks/{id}` | Replace a task                                  |
| DELETE | `/tasks/{id}` | Delete a task                                   |

Interactive docs: `http://localhost:8000/docs`

## Configuration

All configuration comes from environment variables (see `.env.example`):

| Variable       | Default                 | Notes                                      |
| -------------- | ----------------------- | ------------------------------------------ |
| `APP_NAME`     | `tasks-api`             |                                            |
| `APP_ENV`      | `local`                 | `local`, `dev`, `prod`…                    |
| `LOG_LEVEL`    | `INFO`                  |                                            |
| `DATABASE_URL` | `sqlite:///./tasks.db`  | Use PostgreSQL from module 03 onwards      |

PostgreSQL URL format: `postgresql+psycopg://USER:PASSWORD@HOST:5432/DBNAME`

## Run locally (no Docker)

```bash
cd app
python3 -m venv .venv && source .venv/bin/activate
pip install -r requirements-dev.txt
PYTHONPATH=src uvicorn tasks_api.main:app --reload
```

## Run the tests

```bash
cd app
pytest -q
```

## What is intentionally missing

These are **not** provided, because writing them is the point of the labs:

- `Dockerfile` and `compose.yaml` → module 03
- CI/CD workflow → module 04
- AWS infrastructure and Terraform code → modules 05 and 06
- Kubernetes manifests and Helm chart → module 08
- `/metrics` endpoint and dashboards → module 09
