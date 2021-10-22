import uvicorn
from fastapi import Depends, FastAPI
from sqlalchemy.orm import Session

from app import crud, models, schemas
from app.database import engine, get_db

models.Base.metadata.create_all(bind=engine)

app = FastAPI()


@app.post("/create-user", response_model=schemas.User)
def create_user(user: schemas.UserCreate, db: Session = Depends(get_db)):
    return crud.create_user(db, user)


@app.post("/create-todo", response_model=schemas.Todo)
def create_todo(todo: schemas.TodoCreate, db: Session = Depends(get_db)):
    return crud.create_todo(db, todo)


if __name__ == "__main__":  # pragma: nocover
    uvicorn.run(app, host="0.0.0.0", port=8000)
