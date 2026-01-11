from fastapi import FastAPI,HTTPException
from enum import Enum
from typing import List,Union
from pydantic import BaseModel

app = FastAPI()


# @app.get("/user/{namess}")
# async def user1(namess):
#   return f"hello {namess}"

# @app.get("/user2")
# async def userr(names:str):
#   return {"messages": f"hello {names}"}

# @app.get("/user3/{name}")
# async def userr2(name:str,age:int) -> dict:
#   return {"messages" : f"hello my name is {name} is and my age is {age}"}


from typing import Dict

app = FastAPI(title="CRUD Practice")

# Fake database (dictionary)
students_db: Dict[int, dict] = {
    1: {
        "name": "Rohan",
        "age": 21,
        "course": "Data Science"
    },
    2: {
        "name": "Kishlay",
        "age": 22,
        "course": "AI & ML"
    }
}

# print(students_db)

@app.get("/all_students")
async def all_students():
  return students_db

@app.get("/students/{students_id}")
async def particular_students(students_id:int):
  if students_id in students_db:
    return students_db[students_id]
  raise HTTPException(status_code=404,detail="studtetns not there ")



class ModelName(str,Enum):
  alexnet = "alexnate"
  resnet = "resnet"
  lenet = "lenet"



@app.get("/models/{model_name}")
async def get_model(model_name:ModelName):
  if model_name is ModelName.alexnet:
    return {"model_name":model_name, 'message': 'DEEP LEARNING FTW'}
  
  if model_name.value == "lenet":
    return {"model_name":model_name, "message": "CNN "}
  
  raise HTTPException(status_code=404,detail="no model name is defined")



fake_items_db = [{"item_name": "Foo"}, {"item_name": "Bar"}, {"item_name": "Baz"}]


# print(fake_items_db[0]['item_name'])

for i in fake_items_db:
  for key,value in i.items():
    print(value)

@app.get("/items")
async def read_items(data : int = 0, limit: int = 10):
  return fake_items_db[data:data+limit]




@app.get("/items2/{items_id}")
async def readitems(items_id:str,q:Union[str,None] = None):
  if q:
    return {"item_id":items_id,"q":q}
  
  return {"items_id":items_id}


user_id = [1,2,3,4]

@app.get("/items3/{item_id}")
async def reading_items(
  item_id:int,
  q:str|None = None, 
  short:bool=False):

  item = {"item_id":item_id,
   "owner_id":user_id[1]}

  if q:
    # item.update({"q":q})
    item["q"] = q
  if not short:
      item["description"] = "this is amazing items"

  return item

product_ids = [101,102,103]

@app.get("/products/{product_id}")
async def product(product_id:int,search:str|None=None,details:bool=True):
  if product_id in product_ids:
    # if not details:
    # return product_ids[product_id]
      response = {"product_id":product_id,     "available_products":product_ids
                  }
      if details:
        response['description'] = "this is the premium product"
  else: 
    raise HTTPException(status_code=404,detail="no product with this number")
  return response