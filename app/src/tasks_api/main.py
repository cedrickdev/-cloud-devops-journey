"""HTTP API: health checks + a tiny CRUD on tasks."""

import logging
from contextlib import asynccontextmanager

from fastapi import Depends, FastAPI, HTTPException, Response, status
from pydantic import BaseModel, ConfigDict, Field
from sqlalchemy import select, text
from sqlalchemy.orm import Session

from . import __version__
from .config import settings
from .db import Task, get_session, init_db

logging.basicConfig(
    level=settings.log_level,
    format="%(asctime)s %(levelname)s %(name)s %(message)s",
)
logger = logging.getLogger("tasks_api")


@asynccontextmanager
async def lifespan(_: FastAPI):
    init_db()
    logger.info("startup env=%s version=%s", settings.environment, __version__)
    yield


app = FastAPI(title=settings.app_name, version=__version__, lifespan=lifespan)


class TaskIn(BaseModel):
    title: str = Field(min_length=1, max_length=200)
    done: bool = False


class TaskOut(TaskIn):
    model_config = ConfigDict(from_attributes=True)
    id: int


# --- Health checks -----------------------------------------------------------
# /health  -> liveness: the process is up (no dependency checks).
# /ready   -> readiness: the app can reach its database.


@app.get("/health")
def health():
    return {"status": "ok", "version": __version__, "env": settings.environment}


@app.get("/ready")
def ready(response: Response, session: Session = Depends(get_session)):
    try:
        session.execute(text("SELECT 1"))
        return {"status": "ready"}
    except Exception:  # noqa: BLE001 — any DB error means "not ready"
        logger.exception("readiness check failed")
        response.status_code = status.HTTP_503_SERVICE_UNAVAILABLE
        return {"status": "unavailable"}


# --- Tasks CRUD --------------------------------------------------------------


@app.get("/tasks", response_model=list[TaskOut])
def list_tasks(session: Session = Depends(get_session)):
    return session.scalars(select(Task).order_by(Task.id)).all()


@app.post("/tasks", response_model=TaskOut, status_code=status.HTTP_201_CREATED)
def create_task(payload: TaskIn, session: Session = Depends(get_session)):
    task = Task(**payload.model_dump())
    session.add(task)
    session.commit()
    return task


def _get_or_404(session: Session, task_id: int) -> Task:
    task = session.get(Task, task_id)
    if task is None:
        raise HTTPException(status_code=404, detail="Task not found")
    return task


@app.get("/tasks/{task_id}", response_model=TaskOut)
def get_task(task_id: int, session: Session = Depends(get_session)):
    return _get_or_404(session, task_id)


@app.put("/tasks/{task_id}", response_model=TaskOut)
def update_task(task_id: int, payload: TaskIn, session: Session = Depends(get_session)):
    task = _get_or_404(session, task_id)
    task.title, task.done = payload.title, payload.done
    session.commit()
    return task


@app.delete("/tasks/{task_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_task(task_id: int, session: Session = Depends(get_session)):
    session.delete(_get_or_404(session, task_id))
    session.commit()
