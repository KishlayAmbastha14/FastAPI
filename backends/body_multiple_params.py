from fastapi import FastAPI,Query,Path,Body
from typing import List,Annotated,Optional

from pydantic import BaseModel

app = FastAPI()

## here we are using both QUERY and PARAMS in same place with BODY

class Item(BaseModel):
  name: str
  description: str | None = None
  price: float
  tax: float | None = None

@app.put("/query_params/{item_id}")
async def querying_paraming(item_id:Annotated[int,Path(title="enter the item_id",ge=1,le=100)],
                            q:Annotated[Optional[str] , Query(title="enter the something")]=None,
                            item:Item|None = None):
  results = {"item_id is ":item_id}

  if q:
    results.update({"the q is given is ": q})
  if item:
    results.update({"item":Item})
  return results


class User(BaseModel):
    username: str
    full_name: str | None = None


@app.put("/items/{item_id}")
async def update_item(item_id: int, item: Item, user: User):
    results = {"item_id": item_id, "item": item, "user": user}
    return results


# ------------------
class a1(BaseModel):
    name: str
    description: str | None = None
    price: float
    tax: float | None = None

class User(BaseModel):
    username: str
    full_name: str | None = None

@app.put("/items_fetch/{item_id}")
async def updating_items(
   item_id:int,
   item:Item,
   user:User,
   importance:Annotated[int,Body(gt=0)],
   q:str|None = None
):
  results = {"item_Id":item_id,"item":item,"user_id":user,"importance":importance}

  if q:
    results.update({"q":q})
  return results