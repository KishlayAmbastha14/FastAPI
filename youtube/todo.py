from fastapi import FastAPI,Request
from fastapi.responses import JSONResponse
from crud import todo_router
import time,json
app = FastAPI()


@app.middleware("http")
async def logging_middleware(request:Request,call_next):
  try:
    print(request['path'])
    print(request['method'])
    payload = await request.body()
    if payload:
      print(json.loads(payload))
    start = time.time()
    response = await call_next(request)
    duration = time.time() - start
    print(f"the total time is taken is ({duration}.2f)")
    return response
  except Exception as e: 
    print(e)


##  ye check krega ki like maine khi route wla code me koi problem nhi na krdiya hai 
@app.middleware("http")
async def error_middleware(request:Request,call_next):
  try:
    return await call_next(request)
  except Exception:
    return JSONResponse ( status_code = 500, content = {"error":"internal server error"})


for route in [todo_router]:
  app.include_router(router=route,prefix="/api/todo")







