from fastapi import FastAPI
from contextlib import asynccontextmanager
from todo.core.database import init_db
# from .routers import book_router
from .routers import book_router
from fastapi.middleware.cors import CORSMiddleware

# {
#   "title": "NLP",
#   "author": "KISHALY KUMAR",
#   "publisher": "KK",
#   "language": "ENGLISH",
#   "page_count": 20,
#   "published_date": "2026-02-06"
# }

@asynccontextmanager
async def lifespan(app:FastAPI):
  print("Server Started")
  await init_db()
  yield
  print("Server Stopped")


app = FastAPI(
    title="BOOK_TODO",
    description="Simple Book CRUD practice project",
    version="1.0.0",
    lifespan=lifespan
)


app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(book_router,
                   prefix=f"/api/todo",
                   tags=["todo"])

