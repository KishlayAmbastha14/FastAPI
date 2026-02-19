from fastapi import FastAPI
from contextlib import asynccontextmanager
from todo.core.database import init_db
# from .routers import book_router
from .routers import book_router
from fastapi.middleware.cors import CORSMiddleware
from fastapi import Request
from slowapi.errors import RateLimitExceeded
from slowapi.util import get_remote_address
from slowapi.middleware import SlowAPIMiddleware
from fastapi.responses import JSONResponse

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

app.state.request_count = 0


import json
import time

@app.middleware("http")
async def logging_middleware(request:Request,call_next):
    try:
      print(request['path'])
      print(request['method'])
      payload = await request.body()
      app.state.request_count += 1
      if payload:
        print(json.loads(payload))
      start = time.time()

      response = await call_next(request)
      duration = time.time() - start
      print(f"the total time is taken is ({duration}.2f)")
      return response
    except Exception as e: 
      print(e)
   

# RATE LIMITER WITH EXCEPTION HANDLER
@app.exception_handler(RateLimitExceeded)
async def rate_limit_handler(request:Request, exc:RateLimitExceeded):
    return JSONResponse(
       status_code=429,
       content={"detail":"Too many request"}
    )

