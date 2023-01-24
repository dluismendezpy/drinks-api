# Drinks API

This project is a web application built with Django, using the Django REST Framework to construct a RESTful API. Docker
and Docker Compose have been used to facilitate the setup and deployment of the application.

In addition, linter and code formatter tools such as flake8, black, and isort have been implemented to ensure that the
code is standardized and easy to maintain. pre-commit is used to automate the linting and formatting process before
making any commits to the repository.

The project is based on software development best practices to ensure code quality and scalability of the application.
Additionally, the use of Docker and linting and formatting tools help to ensure that the code is easy to understand and
maintain.

<div align="center">

![Python](https://img.shields.io/badge/-Python-black?style=flat-square&logo=Python)
![Django](https://img.shields.io/badge/-Django-black?style=flat-square&logo=Django)
![Docker](https://img.shields.io/badge/-Docker-black?style=flat-square&logo=Docker)
</div>

## Setup

#### Cone repo (HTTPS, SSH or GH)

    git clone https://github.com/dluismendezpy/drinks-api.git
    git@github.com:dluismendezpy/drinks-api.git
    gh repo clone dluismendezpy/drinks-api

#### Create and activate virtualenv

    virtualenv venv
    source venv/bin/activate

#### Install dependencies

    pip install -r dev_requirements.txt

#### Env variables

- Create .env and add your values for:
    - SECRET_KEY=
    - DEBUG=
    - ALLOWED_HOSTS=
    - POSTGRES_DB=
    - POSTGRES_USER=
    - POSTGRES_PASSWORD=
    - POSTGRES_HOST=db
    - POSTGRES_PORT=
- If you use docker, you need export POSTGRES_DB, POSTGRES_USER and POSTGRES_PASSWORD in Terminal.

#### Start dev server

    python manage.py makemigrations
    python manage.py migrate
    python manage.py runserver

### Docker commands

    export POSTGRES_DB= export POSTGRES_USER= export POSTGRES_PASSWORD=
    docker-compose up --build

#### *Important*

- If you are using windows (PS), activate the virtual environment using `venv\Scripts\activate.ps1`
- If you have postgresql installed locally on your computer, you may need to change the default port, for example, 5433.
