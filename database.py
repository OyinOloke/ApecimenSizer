from sqlalchemy import create_engine, MetaData
from databases import Database
from dotenv import load_dotenv
import os

# Load environment variables from .env file
load_dotenv()

DATABASE_URL = os.getenv("DATABASE_URL")

database = Database(DATABASE_URL)
engine = create_engine(DATABASE_URL.replace("+asyncpg", ""))
metadata = MetaData()
