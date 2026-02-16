from pydantic import BaseModel,ConfigDict
from datetime import date,datetime
from typing import Optional,Annotated
from uuid import UUID

class BookBase(BaseModel):
  title : str
  author : str
  publisher : str
  language : str
  page_count : int
  published_date : date

class BookCreate(BookBase):
  pass

class BookUpdate(BaseModel):
  title : Optional[str] = None
  author : Optional[str] = None
  publisher: Optional[str] = None
  language : Optional[str] = 'English'
  page_count : Optional[int] = None
  published_date : Optional[date] = None

class BookModel(BookBase):
  # uid : uuid.UUID
  # uid : UUID
  uid : str
  created_at : datetime
  updated_at : datetime


  model_config = ConfigDict(from_attributes=True)