from fastapi.testclient import TestClient
from sqlalchemy.orm import Session
from app import models


def test_create_user(client: TestClient):
    response = client.post(
        "/create-user", json={"username": "test6", "password": "test6"}
    )
    data = response.json()

    assert response.status_code == 200
    assert data["id"] is not None


def test_create_user_raises_username_taken(session: Session, client: TestClient):
    user_1 = models.User(username="test1", password="test1")
    session.add(user_1)
    session.commit()

    response = client.post(
        "/create-user", json={"username": "test1", "password": "test1"}
    )
    data = response.json()

    assert response.status_code == 409
    assert data["detail"] == "Username already registered"
