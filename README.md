# Autobots Fastapi Todo Api

This project is a todo api with fastapi that we built at autobots. Come join in on the fun on [slack](https://join.slack.com/t/qautah/shared_invite/zt-4cbb6q78-J8opsCMlPqOKdef42x9kUw)

## Setup

- Clone the repo
- Run `poetry install`
  - Don't have poetry? You can download it at https://python-poetry.org/
  - Don't have python? You can download it at https://www.python.org/

## Start the uvicorn server:

- Run the following command in your terminal `poetry run uvicorn app.main:app --reload`

## Planning

- **User**
  - username: str
  - password: str
  - create_at: date_time
  - updated_at: date_time
  - todos: Array[Todos]
- **Todo**
  - title: str
  - done: Bool
