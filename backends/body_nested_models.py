from fastapi import FastAPI,Body
from typing import List,Literal,Annotated,Union
from pydantic import BaseModel,Field,HttpUrl


class Item(BaseModel):
  name : str
  description : Union[str,None]  = None
  price : float
  tax : Union[float,None]  = None
  tags : list = []


app = FastAPI()

@app.put("/items/{item_id}")
async def update_items(item_id:int, item:Item):
  results = {"item_id": item_id , "item" : item}
  return results

## Attributes with list of models
class Image(BaseModel):
  url : HttpUrl
  name : str

class Itemss(BaseModel):
  name : str
  description : str | None = None
  price : float
  tax : float | None = None
  tags : set[str] = set()
  images : list[Image] | None = None 


@app.put("/Images/{item_id}")
async def images_find(item_id:int, item : Itemss):
  results = {"item_id":item_id,"item":item}
  return results

store : List[Itemss] = []

@app.put("/Images1/{item_id}")
async def images_find(item_id:int, item : Itemss):
  results = {"item_id":item_id,"item":item}
  store.append(results)
  return store


class Image(BaseModel):
  url: HttpUrl
  name: str

class Item(BaseModel):
  name: str
  description: str | None = None
  price: float
  tax: float | None = None
  tags: set[str] = set()
  images: list[Image] | None = None


class Offer(BaseModel):
  name : str 
  description : str | None = None
  price : float
  items : list[Item]

@app.post("/offers",response_description="your data is stored in database")
async def offer_post(offfer : Offer):
  return offfer



