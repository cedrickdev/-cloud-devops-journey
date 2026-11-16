import os
import sys
from pathlib import Path

# Use a throwaway SQLite database for tests.
os.environ["DATABASE_URL"] = "sqlite:///./test_tasks.db"
sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "src"))

import pytest  # noqa: E402
from fastapi.testclient import TestClient  # noqa: E402

from tasks_api.db import Base, engine  # noqa: E402
from tasks_api.main import app  # noqa: E402


@pytest.fixture()
def client():
    Base.metadata.drop_all(bind=engine)
    with TestClient(app) as c:
        yield c
    Base.metadata.drop_all(bind=engine)
