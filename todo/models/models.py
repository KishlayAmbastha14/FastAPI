# from base import Base
from sqlalchemy import Column,Integer,String,Date,DateTime,func,Text
import uuid

from sqlalchemy.orm import declarative_base

Base = declarative_base()


class Book(Base):
  __tablename__ = "books"
  
  uid = Column(String,primary_key=True,default=lambda:str(uuid.uuid4()))
  # uid = Column(UUID(as_uuid=True),primary_key=True,default=uuid.uuid4())
  title = Column(Text,nullable=False,index=True)
  author = Column(String(100),nullable=False,index=True)
  publisher = Column(String(100),nullable=False,index=True)
  language = Column(String(50),default='English')
  page_count = Column(Integer,default=0)
  published_date = Column(Date,nullable=True)
  created_at = Column(DateTime,server_default=func.now())
  updated_at = Column(DateTime,server_default = func.now(),onupdate=func.now())
  def __repr__(self):
    return f"<Book(title='{self.title}',author='{self.author}')>"

