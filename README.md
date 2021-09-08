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
- Server auto-restarts on changes, so only when new packages are added, `docker-compose build` will be needed again

#### Models
- Database changes are managed through alembic, in order to migrate new changes you must generate a new migration:
  ```
  docker-compose run app alembic revision --autogenerate -m "my_migration"
  ```
- and migrate it:
  ```
  docker-compose run app alembic upgrade head
  ```
- Convention for auto-generated migrations like `my_migration` is `auto_${DATE}`, for example:
  ```
  docker-compose run app alembic revision --autogenerate -m "auto_20210907"
  ```
- Database service must be up and running.
