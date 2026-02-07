from fastapi import FastAPI,Form
from typing import Annotated
from pydantic import BaseModel

app = FastAPI()


@app.post("/login")
async def loginn(username:Annotated[str,Form()],password:Annotated[str,Form()]):
  return {"username":username}


# here we can also use pydantic model to create a FORM
class FormData(BaseModel):
  username : str
  password : str
  model_config = {"extra":"forbid"}

@app.post("/logins/")
async def loggin2(data:Annotated[FormData,Form()]):
  return {"username":data.username,"data":data}