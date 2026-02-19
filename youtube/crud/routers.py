from fastapi import FastAPI,Path,Query,APIRouter,HTTPException,Response,Request
from typing import List
from .models import Todo,PostTodo,GetTodo,UpdateTodo,UpdateTodoReturn,DeleteTodo

from slowapi import Limiter
from slowapi.util import get_remote_address

app = FastAPI(title="PRACTISE TODO APP WITHOUT DB")

# get_router = APIRouter(prefix="/get",tags=['GET ROUTE'])
# post_router = APIRouter(prefix="/post",tags=["POST ROUTE"])
# put_router = APIRouter(prefix="/put",tags=["PUT ROUTE"])
# delete_router = APIRouter(prefix="/delete",tags=['DELETE ROUTE'])

todo_router = APIRouter()

limiter = Limiter(key_func=get_remote_address)

db : List[Todo] = []

@todo_router.get("/")
async def mesage():
  return {"msg":"hello to crud"}

@todo_router.post("/create",tags=["POST"],response_model=PostTodo)
async def creating_post(request:Request , todo:Todo) -> PostTodo:
  db.append(todo)
  return PostTodo(post=todo, 
                  msg="data is stored in db",
                  api_count = request.app.state.request_count)


@todo_router.get("/todos",tags=["GET"]) 
@limiter.limit("2/minute")
async def getting_todos(request:Request):
  try: 
    if not db:
      return {"msg":"no data is available"}
    
    return Response(content=GetTodo(todos=db,msg="total todo db is shown").model_dump_json(),
    status_code=200)
  
  except Exception as e:
    print(e)
 


@todo_router.get("/todos/{s_id}",tags=["GET"],response_description="student {id} is fetched ")
async def fetching_id(s_id:str):
  try:
    for i in db:
      if float(i.id) == s_id:
        return {'message':f"Todo with id {s_id} is found", "data": i}
      # if i.get("id") == s_id:
        # return {"message":" is found"}
    raise HTTPException(status_code=404,detail="Todo not found")
  except Exception as e:
    print(e)
    raise HTTPException(status_code=500, detail=str(e))
  
@todo_router.put("/todos/{s_id}",tags=["PUT"],response_model=UpdateTodoReturn)
async def updating_todo(s_id:str,todo_upd:UpdateTodo) -> UpdateTodoReturn:
  for i in db:
    if str(i.id) == s_id:
      if todo_upd.name is not None:
        i.name = todo_upd.name
      if todo_upd.category is not None:
        i.category = todo_upd.category
      if todo_upd.status is not None:
        i.status = todo_upd.status
      return UpdateTodoReturn(update_todo=i,msg="new todo updated")
  raise HTTPException(status_code=404, detail="no id is found ")


@todo_router.delete("/todos/{s_id}",tags=["DELETE"],response_model=DeleteTodo)
async def deleting_todo(s_id:str) -> DeleteTodo:
  for i in db:
    if str(i.id) == s_id:
      db.remove(i)
      return DeleteTodo(delete_todo=i,msg="delete {s_id} from database")
  
  raise HTTPException(status_code=404, detail="ID not found") 


  
# routers = [get_router,post_router,put_router,delete_router]

# for route in routers:
#   app.include_router(router=route,prefix="/api")