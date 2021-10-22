from sqlalchemy.orm import Session
from sqlalchemy.exc import IntegrityError
from fastapi import HTTPException, status
from app import models, schemas


def create_user(db: Session, user: schemas.UserCreate) -> models.User:
    db_user = models.User(username=user.username, password=user.password)
    db.add(db_user)
    try:
        db.commit()
    except IntegrityError as err:
        raise HTTPException(
            status_code=status.HTTP_409_CONFLICT, detail="Username already registered"
        )
    db.refresh(db_user)
    return db_user


def create_todo(db: Session, todo: schemas.TodoCreate):
    db_todo = models.Todo(title=todo.title, done=todo.done)
    db.add(db_todo)
    db.commit()
    db.refresh(db_todo)
    return db_todo
