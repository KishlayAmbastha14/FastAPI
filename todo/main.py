from fastapi import FastAPI
from contextlib import asynccontextmanager
from .database import init_db
# from routers import book_router


@asynccontextmanager
async def life_span(app:FastAPI):
  print("Server Started")
  await init_db()
  yield
  print("Server Stopped")


versions = 'v1'

app = FastAPI(title="BOOK_TODO",description="hii this my simple pract project",
  # version = versions
  lifespan = life_span
)

# app.include_router(book_router,prefix=f"/api/todo",tags=["todo"])

print("hiii")
