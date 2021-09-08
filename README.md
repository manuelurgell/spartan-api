# spartan-api
Coding Challenge. You must be here because you are a [developer](#development), or want to [review](#review-project) the project.
***
## Overview
This API is a simple RESTful asynchronous service that allows to create users and teams. Each team can have many users and each user can have many teams. The endpoints that you'll find will let you create, read, update and delete users, teams, as well as the association found between both.
***
## Index
- [Review project](#review-project)
  - [Install project](#install-project)
  - [Clone from GitHub](#clone-from-github)
  - [Environment](#environment)
  - [Run project](#run-project)
  - [API documentation](#api-documentation)
- [Development](#development)
  - [Install project](#install-project-1)
  - [Clone from GitHub](#clone-from-github-1)
  - [Environment](#environment-1)
  - [Install packages](#install-packages)
  - [Run project](#run-project-1)
  - [Models](#models)
  - [Unit Tests](#unit-tests)
  - [Running locally](#running-locally)
  - [API documentation](#api-documentation-1)
***
## Review project

#### Install project
- Prerequisites:
  - docker (20.10.7 recommended)
  - docker-compose (1.29.2 recommended)
- Ports:
  - The backend api runs on port `8000` by default.
  - The database for reviewing runs on port `5432` by default.

#### Clone from Github
- Clone:
  ```
  git clone https://github.com/manuelurgell/spartan-api.git
  ```

#### Environment
- Create .env file wit the following contents (default values are given, feel free to change them):
  ```
  POSTGRES_DB=spartan_db
  POSTGRES_USER=postgres
  POSTGRES_PASSWORD=postgres
  POSTGRES_HOST=database
  POSTGRES_PORT=5432

  POSTGRES_URL="postgresql://${POSTGRES_USER}:${POSTGRES_PASSWORD}@${POSTGRES_HOST}:${POSTGRES_PORT}/${POSTGRES_DB}"
  ```

#### Run project
- Run with docker-compose:
  ```
  docker-compose build
  docker-compose up
  docker-compose run app alembic upgrade head (in another terminal)
  ```

#### API documentation
- When the service is running, either via docker-compose, docker, or locally, you can go to http://localhost:8000/docs or http://localhost:8000/redoc to see the full API documentation of each and every endpoint declared in the RESTful API.
- From there you can make tests and see the possible inputs and outputs from every endpoint.
- If you are more used to using a tool like postman, please refer to [here](./docs/README.md).
***
## Development

#### Install project
- Prerequisites:
  - python 3.9 (3.9.5 recommended)
  - docker (20.10.7 recommended)
  - docker-compose (1.29.2 recommended)
- Ports:
  - The backend api runs on port `8000` by default.
  - The database for reviewing runs on port `5432` by default.
  - This ports must be available  when running the app.

#### Clone from Github
- Clone:
  ```
  git clone https://github.com/manuelurgell/spartan-api.git
  ```

#### Environment
- Create .env file wit the following contents (default values are given, feel free to change them):
  ```
  POSTGRES_DB=spartan_db
  POSTGRES_USER=postgres
  POSTGRES_PASSWORD=postgres
  POSTGRES_HOST=database
  POSTGRES_PORT=5432

  POSTGRES_URL="postgresql://${POSTGRES_USER}:${POSTGRES_PASSWORD}@${POSTGRES_HOST}:${POSTGRES_PORT}/${POSTGRES_DB}"
  ```

#### Install Packages
- Python:
  ```
  sudo apt-get update
  sudo apt-get install python3.9-dev
  sudo apt install python3.9-venv
  ```
- Virtual environment (folder at `~/.venvs` or equivalent must exist):
  ```
  python3 -m venv ~/.venvs/spartan-api
  source ~/.venvs/spartan-api/bin/activate
  pip install -r requirements/local.txt
  ```

#### Run project
- Run with docker-compose:
  ```
  docker-compose build
  docker-compose up
  ```
- Server auto-restarts on changes, so only when new packages are added, the previous commands will be needed again. To re-run on existing docker images, simply:
  ```
  docker start postgres_db
  docker start spartan_app
  ```

#### Models
- Database changes are managed through alembic, in order to migrate new changes you must generate a new migration:
  ```
  docker-compose run app alembic revision --autogenerate -m "my_migration"
  ```
- and migrate it:
  ```
  docker-compose run app alembic upgrade head
  ```
- Convention for auto-generated migrations like `my_migration` is `auto_${DATE}`, or `auto_${DATE}_{NUMBER}` if more than one, for example:
  ```
  docker-compose run app alembic revision --autogenerate -m "auto_20210907_2"
  ```
- You can also run this commands directly to the docker container:
  ```
  docker exec -it spartan_app alembic revision --autogenerate -m "my_migration"
  docker exec -it spartan_app alembic upgrade head
  ```

- Database service must be up and running.

#### Unit Tests
- Currently, unit tests are still being developed. The only test that exists checks code format and structure (using flake8). This tests run automatically on GitHub when a PULL_REQUEST is created or when a PUSH happens. Future development is required.

#### Running locally
- You can also run the api locally, even changing the port (see `--port` flag) use:
  ```
  uvicorn main:app --host 0.0.0.0 --port 8000 --reload
  ```
- If you have a postgresql database running in your machine, simply change the according variables in the .env file, for example:
  ```
  POSTGRES_DB=my_local_database
  ...
  POSTGRES_HOST=localhost
  ```
- This will also allow to create and update migrations locally, like so:
  ```
  alembic revision --autogenerate -m "my_migration"
  alembic upgrade head
  ```
- And to evaluate the unit tests by simply writing in root dir:
  ```
  tox
  ```
- Running locally has the most flexibility while developing, because it even allows to map each service (api and database) to a custom port. However, you can find errors that vary from operating system to operating system, so be careful.

#### API documentation
- When the service is running, either via docker-compose, docker, or locally, you can go to http://localhost:8000/docs or http://localhost:8000/redoc to see the full API documentation of each and every endpoint declared in the RESTful API.
- From there you can make tests and see the possible inputs and outputs from every endpoint.
- If you are more used to using a tool like postman, please refer to [here](./docs/README.md).
