from fastapi import FastAPI,Body
from typing import List,Literal,Annotated
from pydantic import BaseModel,Field

app = FastAPI()

# HERE WE ARE USING FIELD

class Item(BaseModel):
  name:str
  description:str | None = Field(
    default=None,title="the discription of the items",max_length=3000
  )
  price: float = Field(gt=0, description="The price must be greater than zero")
  tax: float | None = None


@app.put("/items_func/{item_id}")
async def fuction_item(item_id:int,item:Annotated[Item,Body(emded=True)]):
  results = {"item_id":item_id,"items":item}
  return results