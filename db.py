import os
from databases import Database
from dotenv import load_dotenv
import sqlalchemy

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
load_dotenv(os.path.join(BASE_DIR, ".env"))

database = Database(os.environ["POSTGRES_URL"])
metadata = sqlalchemy.MetaData()