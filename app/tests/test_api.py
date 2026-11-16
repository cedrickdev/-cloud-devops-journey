def test_health(client):
    r = client.get("/health")
    assert r.status_code == 200
    assert r.json()["status"] == "ok"


def test_ready(client):
    r = client.get("/ready")
    assert r.status_code == 200
    assert r.json() == {"status": "ready"}


def test_task_lifecycle(client):
    r = client.post("/tasks", json={"title": "Write a Dockerfile"})
    assert r.status_code == 201
    task_id = r.json()["id"]

    assert client.get("/tasks").json()[0]["title"] == "Write a Dockerfile"

    r = client.put(f"/tasks/{task_id}", json={"title": "Write a Dockerfile", "done": True})
    assert r.json()["done"] is True

    assert client.delete(f"/tasks/{task_id}").status_code == 204
    assert client.get(f"/tasks/{task_id}").status_code == 404


def test_validation(client):
    assert client.post("/tasks", json={"title": ""}).status_code == 422
