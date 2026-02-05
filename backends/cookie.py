from fastapi import FastAPI,Cookie
from pydantic import BaseModel
from typing import Annotated

app = FastAPI()


@app.get("/items/")
async def read_items(ads_Id:Annotated[str|None, Cookie()]  = None):
  return {"ads_Id":ads_Id}