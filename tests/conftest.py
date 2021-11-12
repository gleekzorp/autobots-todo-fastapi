import pytest
from sqlalchemy import create_engine
from sqlalchemy.orm import Session
from sqlalchemy.pool import StaticPool
from fastapi.testclient import TestClient

from app import models
from app.database import get_db
from app.main import app


@pytest.fixture(name="session")
def session_fixture():
    engine = create_engine(
        "sqlite://", connect_args={"check_same_thread": False}, poolclass=StaticPool
    )
    models.Base.metadata.create_all(bind=engine)
    with Session(engine) as session:
        yield session


@pytest.fixture(name="client")
def client_fixture(session: Session):
    def get_session_override():
        return session

    app.dependency_overrides[get_db] = get_session_override
    client = TestClient(app)
    yield client
    app.dependency_overrides.clear()


@pytest.fixture()
def user(session: Session):
    user = models.User(username="test1", password="test1")
    session.add(user)
    session.commit()
    return user


@pytest.fixture()
def todo(session: Session):
    todo = models.Todo(title="Buy Milk", done=False)
    session.add(todo)
    session.commit()
    return todo
