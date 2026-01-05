from fastapi import FastAPI,HTTPException,Query
from pydantic import BaseModel
from typing import List,Union,Annotated

app = FastAPI()

@app.get("/items")
async def read_items(q:str | None = None):
  results = {"items":[{"items_id":"Foo"},{"item_id":"Bar"}]}

  if q:
    results.update({"q":q})
  return results

# here we can also do with settting the max or min length 

@app.get("/items2")
async def reading_items(age:int,q:Annotated[str|None, Query(max_length=50)] = None):
  results = {"items":[{"items_id":"rohan"},{"item_id":"choco"}]}

  if q:
    results.update({"q": q})
  if age:
    results.update({"age":age})
  return results

@app.get("/items3")
async def readingg(q:Annotated[str|None,Query(min_length=6,max_length=50,description="write correct")] = None):
  results = {"items":[{"items_name":"rohit"},{"item_id":"choclate"}]}

  if q:
    results.update({"q":q})
  return results

@app.get("/items4")
async def readding4(q:Annotated[Union[str,None],
                                Query(alias='item_query',title="query string",description="query string for the items search ",min_length=3, max_length=50,pattern="^fixedquery$"),]=None):
  
  results = {"items":[{"items_name":"rohit"},{"item_id":"choclate"}]}

  if q:
    results.update({"q":q})
  return results