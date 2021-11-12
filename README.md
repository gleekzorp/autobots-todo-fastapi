# Autobots Fastapi Todo Api

This project is a todo api with fastapi that we built at autobots. Come join in on the fun on [slack](https://join.slack.com/t/qautah/shared_invite/zt-4cbb6q78-J8opsCMlPqOKdef42x9kUw)

## Setup

- Clone the repo
- Run `poetry install`
  - Don't have poetry? You can download it at https://python-poetry.org/
  - Don't have python? You can download it at https://www.python.org/

## Start the uvicorn server:

- Run the following command in your terminal `poetry run uvicorn app.main:app --reload`

## Pytest cov command

You can read more about pytest cov at https://pytest-cov.readthedocs.io/en/latest/

- Run the tests and display the coverage in the terminal
  - `poetry run pytest --cov-report term --cov=app tests/`
- Run the tests and create an html report for a more in depth look
  - `poetry run pytest --cov-report html:html_cov_report --cov=app tests/`

## Current Homework

Finish the following tasks:

- Toggle Todo Complete
- Delete Todo
