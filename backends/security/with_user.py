from fastapi import FastAPI , Depends
from typing import List,Annotated
from pydantic import BaseModel
from fastapi.security import OAuth2PasswordBearer

app = FastAPI()

oauth_schchem2 = OAuth2PasswordBearer(tokenUrl="token")

class User(BaseModel):
  username : str
  email : str | None = None
  full_name : str | None = None
  disabled : bool | None = False

async def fake_decode_token(token):
  return User(username = token+"fakedecoded",email="kislay@gmail.com",full_name = " Kishlay ")

async def get_current_user(token: Annotated[str,Depends(oauth_schchem2)]):
  user = fake_decode_token(token)
  return user

@app.get("/users/me")
async def read_users_Me(current_user: Annotated[User,Depends(get_current_user)]):
  return current_user