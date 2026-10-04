from fastapi.testclient import TestClient
from ailogs.main import app

client = TestClient(app)


def test_labels():
    assert client.post("/classify", json={"text": 'container was oom killed'}).json()["label"] == "oom"
    assert client.post("/classify", json={"text": 'upstream timeout deadline'}).json()["label"] == "timeout"


def test_empty_is_refused():
    assert client.post("/classify", json={"text": "  "}).status_code == 422
