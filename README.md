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
  ```

#### Run project
- Run with docjer-compose:
  ```
  docker-compose build
  docker-compose up
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
- Create .env file wit the following contents (defaults are given, feel free to change them):
  ```
  POSTGRES_DB=spartan_api
  POSTGRES_USER=postgres
  POSTGRES_PASSWORD=postgres
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
