from sqlalchemy.ext.asyncio import create_async_engine,async_sessionmaker
from sqlalchemy.ext.asyncio import AsyncSession
from .models.models import Base
from .config import settings
from fastapi import Depends
from sqlalchemy.pool import NullPool
## engine se DB k connnection 
# try:
engine = create_async_engine(
  settings.DATABASE_URL.strip(),
  echo = True,
  # pool_size = 5,
  poolclass = NullPool,
  # max_overflow = 10,
  # statement_cache_size=0,
  connect_args={
        "ssl": True,                 # ✅ asyncpg SSL
        "statement_cache_size": 0,
        # "command_timeout" : 60   # ✅ Neon pooler
    }
)
# SEESION MAKING
AsyncSessionLocal = async_sessionmaker(
  engine,
  class_=AsyncSession,
  expire_on_commit = False,
  autocommit=False,
  autoflush=False 
)

async def get_db():
  async with AsyncSessionLocal() as session:
    try:
      yield session
    finally:
      await session.close()


async def init_db():
  async with engine.begin() as conn:
    await conn.run_sync(Base.metadata.create_all)

