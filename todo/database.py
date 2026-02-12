## ye mera database se connection rkhega and usse baat krega with an api 
# from sqlalchemy import create_engine 
# from sqlalchemy.orm import sessionmaker, declarative_base


from sqlalchemy.ext.asyncio import create_async_engine
from sqlalchemy.ext.asyncio import async_sessionmaker
from sqlalchemy.ext.asyncio import AsyncSession


from config import settings
from fastapi import Depends

## engine se DB k connnection 
# try:
engine = create_async_engine(
  settings.DATABASE_URL,
  echo = True,
  pool_size = 5,
  max_overflow = 10
)

# SEESION MAKING
AsyncSessionLocal = async_sessionmaker(
  engine,
  expire_on_commit = False
)

async def get_db():
  async with AsyncSessionLocal() as session:
    try:
      yield session
    finally:
      await session.close()



