from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()


class UserIn(BaseModel):
    username: str
    password: str


class UserOut(BaseModel):
    username: str


@app.get("/")
def hello_world():
    return "Hello World!"


@app.post("/create-user", response_model=UserOut)
def create_user(user: UserIn):
    return user
