from fastapi import FastAPI,Header,HTTPException,Cookie
from pydantic import BaseModel

from typing import List,Annotated

app = FastAPI()

class Cookies(BaseModel):
  session_id : str
  fatebook_traker : str | None = None
  googall_tracker : str | None = None


@app.get("/items/")
async def read_items(cookies: Annotated[Cookies, Cookie()]):
  return cookies


class Cookies(BaseModel):
    session_id: str | None = None
    fatebook_tracker: str | None = None
    googall_tracker: str | None = None


@app.get("/items2/")
async def read_items(cookies: Annotated[Cookies, Cookie()]):
    return cookies