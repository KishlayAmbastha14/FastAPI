## ye mera database se connection rkhega and usse baat krega with an api 
from sqlalchemy import create_engine 
from sqlalchemy.orm import sessionmaker, declarative_base
from core.config import config


## engine se DB k connnection 
# try:
engine = create_engine(
    config.DATABASE_URL,
    pool_pre_ping = True
  )


## SESSION FACTORY
SessionLocal = sessionmaker(
    bind = engine,
    autocommit = False,
    autoflush = False
)

Base = declarative_base()

