from fastapi import FastAPI,Depends
from typing import Annotated
from pydantic import BaseModel


app = FastAPI()


async def common_params(q:str|None = None, skip : int = 0, limit: int = 100):
  return {"q":q,"skip":skip,"limit":limit}


@app.get("/items")
async def read_items(commons:Annotated[dict,Depends(common_params)]):
  return commons

@app.get("/users/")
async def read_users(commons: Annotated[dict, Depends(common_params)]):
    return commons