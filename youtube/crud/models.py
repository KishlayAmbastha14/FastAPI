from pydantic import BaseModel,Field
from typing import List,Dict,Annotated,Optional
from uuid import UUID,uuid4


## OVERALL SCHEMA
class Todo(BaseModel): 
  id : UUID = Field(default_factory = uuid4)
  name : str = 'kishlay'
  category : str = "GENERAL"
  status : bool

## SCHEMA FOR GETT
class GetTodo(BaseModel):
  # todos : list[Todo]
  todos : list[Todo]
  msg : str

## SCHEMA FOR POST
class PostTodo(BaseModel):
  post : Todo
  
  msg : str
  api_count : int

class UpdateTodo(BaseModel):
  name : Optional[str] = None
  category : Optional[str] = None
  status : Optional[bool] = None

class UpdateTodoReturn(BaseModel):
  update_todo : Todo
  msg : str

class DeleteTodo(BaseModel):
  delete_todo : Todo
  msg : str