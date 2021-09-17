from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)


def test_root_route():
    response = client.get("/")
    assert response.text == '"Hello World!"'
