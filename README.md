# Autobots Fastapi Todo Api

This repo is in conjuction with autobots.

## Setup

- Clone the repo
- Run `poetry install`

## How to start the uvicorn server:

- Run the following command in your terminal `poetry run uvicorn app.main:app --reload`

## Request Body Data

- **User**
  - username: str
  - password: str
  - create_at: date_time
  - updated_at: date_time
  - todos: Array[Todos]
- **Todo**
  - title: str
  - done: Bool
