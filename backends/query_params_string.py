from fastapi import FastAPI,HTTPException,Query
from pydantic import BaseModel
from typing import List,Union,Annotated,Optional
from enum import Enum

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


@app.get("/items5")
async def reading5(hidden_querys:Annotated[str|None,Query(include_in_schema=False)] = None,):
  results = {"items":[{"items_name":"rohan"},{"item_id":"455"}]}

  if hidden_querys:
    results.update({"hidden_query":hidden_querys})
  else:
    results.update({"hidden":"not found"})

  return results


# 🟡 INTERMEDIATE LEVEL (Real API Thinking)
# Q5. Write an API that:
# Accepts search query
# Minimum length = 3
# Maximum length = 20
# Optional

@app.get("/api1")
async def calling(search:Annotated[str|None,Query(min_length=3,max_length=20)] = None):
  results = {"items":[{"items_id":"rohan","items_store":"papaya"}]}

  if search:
    results.update({"search_Input":search})
  return results



# 🔹 Task 1
# Create an endpoint /users:
# name: required, min length 3
# role: optional, only "admin" or "user"\

class Role(str,Enum):
  admin = "admin"
  user = "user"


@app.get("/users")
async def userfind(name:Annotated[str,Query(min_length=3)],
                   role:Optional[Role] = None):
  # return {"name": name, "role": role}
  
  items = {"item_No":"hloo"}    

  if name:
    # items.update(name,)
    items = {"items_name":name,**items.model_dump()}
    if role == "user":
      # items.update(role)
      items = {"items_name":role,**items.model_dump()}

  #   else:
  #     items.update(role)


# 🔹 Task 2

# Create /products:

# price: optional, must be ≥ 100

# category: optional, alias = cat

@app.get("/products")
async def productfind(price:Optional[int]):
  items = {"item":[{"item_name":"rohan","item_id":34}]}

  if price > 100:
    items.update({"price is ":price})
  return items


# 🔹 Task 3

# Create /search:

# q: optional

# Should reject special characters using regex