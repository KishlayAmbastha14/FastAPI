from pydantic import BaseModel,ValidationError
from datetime import datetime


class User(BaseModel):
  ids: int
  name:str
  signup_ts : datetime | None


datas = {
  'ids':1,
  'name':'rohan',
  'signup_ts' : '2020-03-04 12:34'

}
try:
  user = User(**datas)

except ValidationError as e:
  print(e.errors())

finally:
  print(user.model_dump())



