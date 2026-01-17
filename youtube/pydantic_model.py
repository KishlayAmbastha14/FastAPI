from fastapi import FastAPI
from typing import List,Optional,Annotated

from pydantic import BaseModel,ConfigDict

app = FastAPI()

class Post(BaseModel):
  title : str
  description : str

  ## like iska matlb ye hua ki extra values hmm nhi de skte hai iha not allowed to give
  model_config = ConfigDict(extra='forbid')

class PostOut(BaseModel):
  post : Post
  msg : str

@app.post("/create_post",response_model=PostOut,summary="api to create post",tags=['POST'],status_code=201)
async def create_post(post:Post) -> PostOut:
  return PostOut(post=post, msg="Post Created")