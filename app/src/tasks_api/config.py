"""Configuration is read from environment variables (12-factor style)."""

import os
from dataclasses import dataclass


@dataclass(frozen=True)
class Settings:
    app_name: str = os.getenv("APP_NAME", "tasks-api")
    environment: str = os.getenv("APP_ENV", "local")
    # SQLite by default so the app runs with zero setup.
    # In Docker / AWS, point it to PostgreSQL, e.g.:
    # postgresql+psycopg://user:password@db:5432/tasks
    database_url: str = os.getenv("DATABASE_URL", "sqlite:///./tasks.db")
    log_level: str = os.getenv("LOG_LEVEL", "INFO")


settings = Settings()
