# spartan-api
Coding Challenge. You must be here because you are a [developer](#development), or want to [review](#review-project) the project.
***
## Review project

#### Install project
- Prerequisites:
  - docker (20.10.7 recommended)
  - docker-compose (1.29.2 recommended)

#### Clone from Github
- Clone:
  ```
  git clone https://github.com/manuelurgell/spartan-api.git
  ```

#### Environment
- Create .env file wit the following contents (default values are given, feel free to change them):
  ```
  POSTGRES_DB=spartan_api
  POSTGRES_USER=postgres
  POSTGRES_PASSWORD=postgres
  POSTGRES_HOST=database
  POSTGRES_PORT=5432

  POSTGRES_URL="postgresql+psycopg2://${POSTGRES_USER}:${POSTGRES_PASSWORD}@${POSTGRES_HOST}:${POSTGRES_PORT}/${POSTGRES_DB}"
  ```

#### Run project
- Run with docker-compose:
  ```
  docker-compose build
  docker-compose up
  docker-compose run app alembic upgrade head (in another terminal)
  ```
***
## Development

#### Install project
- Prerequisites:
  - python 3.9 (3.9.5 recommended)
  - docker (20.10.7 recommended)
  - docker-compose (1.29.2 recommended)

#### Clone from Github
- Clone:
  ```
  git clone https://github.com/manuelurgell/spartan-api.git
  ```

#### Environment
- Create .env file wit the following contents (default values are given, feel free to change them):
  ```
  POSTGRES_DB=spartan_api
  POSTGRES_USER=postgres
  POSTGRES_PASSWORD=postgres
  POSTGRES_HOST=database
  POSTGRES_PORT=5432

  POSTGRES_URL="postgresql+psycopg2://${POSTGRES_USER}:${POSTGRES_PASSWORD}@${POSTGRES_HOST}:${POSTGRES_PORT}/${POSTGRES_DB}"
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

### Running locally
- You can also run the api locally, use:
  ```
  uvicorn main:app --host 0.0.0.0 --port 8000 --reload
  ```
- If you have a postgresql database running in your machine, simply change the according variables in the .env file, for example:
  ```
  POSTGRES_DB=spartan_db
  ...
  POSTGRES_HOST=localhost
  ```
- This will also allow to create and update migrations locally, like so:
  ```
  alembic revision --autogenerate -m "my_migration"
  alembic upgrade head
  ```
- Running locally has the most flexibility while developing, but you can find errors that vary from operating system to operating system, so be careful.