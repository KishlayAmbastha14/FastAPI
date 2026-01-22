from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker,declarative_base
from dotenv import load_dotenv
import os

load_dotenv()


DATABASE = os.getenv("DATABASE_URL")

engine = create_engine(
  DATABASE,
  pool_pre_ping = True
)
# print(DATABASE)

SessionLocal = sessionmaker(
  bind = engine,
  autocommit=False,
  autoflush=False
)

Base = declarative_base()