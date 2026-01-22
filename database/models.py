from .database import Base
from sqlalchemy import Column,Integer, String


# here we make a table like in sql but here we say python class

class User(Base):
  __tablename__ = "users"
  ids = Column(Integer,primary_key=True,index=True)
  email = Column(String,unique=True,index=True,nullable=False)
  password = Column(String,nullable=False)


### -------- SAME AS IT IS ----------
#   CREATE TABLE users (
#     id SERIAL PRIMARY KEY,
#     email VARCHAR UNIQUE NOT NULL,
#     password VARCHAR NOT NULL
# );