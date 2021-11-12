from typing import Generator
from fastapi.testclient import TestClient
from sqlalchemy.orm import Session
from app import models, schemas
from app import crud, database


def test_create_user(client: TestClient):
    response = client.post(
        "/create-user", json={"username": "test6", "password": "test6"}
    )
    data = response.json()

    assert response.status_code == 200
    assert data["id"] is not None


def test_create_user_raises_username_taken(client: TestClient, user: models.User):
    response = client.post(
        "/create-user", json={"username": user.username, "password": user.password}
    )
    data = response.json()

    assert response.status_code == 409
    assert data["detail"] == "Username already registered"


def test_todo_model(session: Session):
    todo = models.Todo(title="Buy Milk", done=False)
    session.add(todo)
    session.commit()

    todo_db = session.query(models.Todo).filter(models.Todo.id == 1).first()

    assert todo_db.title == "Buy Milk"


def test_todo_model_default_done(session: Session):
    todo = models.Todo(title="Buy Milk")
    session.add(todo)
    session.commit()

    todo_db = session.query(models.Todo).filter(models.Todo.id == 1).first()
    assert todo_db.done is False


def test_todo_model_done_is_none(session: Session):
    todo = models.Todo(title="Buy Milk", done=None)
    session.add(todo)
    session.commit()

    todo_db = session.query(models.Todo).filter(models.Todo.id == 1).first()
    assert todo_db.done is False


def test_create_todo(session: Session):
    todo_dict = {"title": "Buy Milk", "done": False}
    todo = crud.create_todo(db=session, todo=schemas.TodoCreate(**todo_dict))

    assert todo.id == 1


def test_create_todo_route(client: TestClient):
    response = client.post("/create-todo", json={"title": "Buy Milk", "done": False})
    data = response.json()

    assert response.status_code == 200
    assert data["id"] == 1
    assert data["title"] == "Buy Milk"
    assert data["done"] is False


def test_get_db():
    db = database.get_db()
    session = next(db)
    assert isinstance(db, Generator)
    assert isinstance(session, Session)

    # assert session.bind.engine.name == "sqlite"
    # assert session.autocommit is False
    # assert session.autoflush is False


def test_get_user_by_username(session: Session, user: models.User):
    response = crud.get_user_by_username(db=session, username=user.username)
    assert response.username == user.username


def test_get_user_by_username_returns_none_when_not_found(session: Session):
    user = crud.get_user_by_username(db=session, username="test1")
    assert user is None


def test_get_user_by_username_route(client: TestClient, user: models.User):
    response = client.get(f"/get-user-by-username/{user.username}")
    data = response.json()

    assert response.status_code == 200
    assert data["username"] == "test1"


def test_get_user_by_username_route_returns_user_not_found(client: TestClient):
    response = client.get("/get-user-by-username/test1")
    data = response.json()

    assert response.status_code == 404
    assert data["detail"] == "User not found"


def test_get_todo_by_id(session: Session, todo: models.Todo):
    response = crud.get_todo_by_id(db=session, todo_id=todo.id)
    assert response.id == todo.id


def test_get_todo_by_id_returns_none_when_not_found(session: Session):
    todo = crud.get_todo_by_id(db=session, todo_id=1)
    assert todo is None


def test_get_todo_by_id_route(client: TestClient, todo: models.Todo):
    response = client.get(f"/get-todo-by-id/{todo.id}")
    data = response.json()

    assert response.status_code == 200
    assert data["id"] == todo.id
    assert data["title"] == todo.title
    assert data["done"] is todo.done


def test_get_todo_by_id_route_returns_todo_not_found(client: TestClient):
    response = client.get("/get-todo-by-id/1")
    data = response.json()

    assert response.status_code == 404
    assert data["detail"] == "Todo not found"
