from fastapi import FastAPI,HTTPException
from pydantic import BaseModel
from typing import List,Union

app = FastAPI()

class Item(BaseModel):
  name : str
  description : str | None = None
  price : float
  tax : float | None = None


@app.post("/items")
async def data(item:Item):
  return item

# put 
@app.put("/itemss/{item_id}")
async def update_items(item_id:int,item:Item):
  return {"item_id":item_id, **item.model_dump()}

@app.post("/tax")
async def price_tag(item:Item):
  item_dict = item.model_dump()

  if item.tax is not None:
    total = item.price + item.tax

    item_dict.update(total)
  return item_dict

# request body with path params

@app.put("/update_items/{item_id}")
async def updating(item_id:int,item:Item):
  return {"item_id":item_id, **item.model_dump()}


# request body with path and query
@app.put("/update_2/{item_id}")
async def update(item_id:int,item:Item,q:str|None = None):
  result = {"item_id":item_id, **item.model_dump()}
  if q:
    result.update({"q":q})
  return result