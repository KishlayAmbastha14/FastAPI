from fastapi import FastAPI,Body
from pydantic import BaseModel,Field
from typing import List,Dict,Annotated


app = FastAPI()

class Item(BaseModel):
  name : str
  description : str | None = None
  price : float
  tax : float | None  = None

  model_config = {
    "json_schema_extra"  : {
      "examples " : [
        {
          "name": "Foo",
          "description" : "A very nice item",
          "price ": 34.5,
          "tax" : 1.5
        }
      ]
    }
  }

db : List[Item] = []

# @app.put("/items/{items_Id}")
# async def update_item(item_Id:int, item: Item):
#   results = {"item_id":item_Id,"item":item}
#   return results

@app.put("/put_items/{item_id}")
async def putting_items(item_id:int,item:Annotated[Item,
                                                   Body(
                                                     examples=[
                                                       {
                                                          "name": "Foo",
                                                          "description" : "A very nice item",
                                                          "price": 44.5,
                                                          "tax" : 2.5
                                                       }
                                                     ],
                                                   ),],):
  results = {"item_id":item_id,"item":item}
  return results



@app.put("/items/{item_id}")
async def update_item(
    item_id: int,
    item: Annotated[
        Item,
        Body(
            examples=[
                {
                    "name": "Foo",
                    "description": "A very nice Item",
                    "price": 35.4,
                    "tax": 3.2,
                }
            ],
        ),
    ],
):
    results = {"item_id": item_id, "item": item}
    return results

@app.post("/store_Items")
async def storing_itmes(item:Item):
  # stored = {"total_items":item,"msg":"item has saved there"}
  db.append(item)
  return {"total_items":item,"msg":"item has saved there"}

@app.get("/get_items")
async def getting_item():
  return db
