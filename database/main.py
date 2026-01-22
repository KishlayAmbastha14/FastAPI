from fastapi import FastAPI, Depends
from . import crud,models,schemas
from .database import Base,engine,SessionLocal
from sqlalchemy.orm import Session

Base.metadata.create_all(bind=engine)

app = FastAPI()

def get_db():
  db = SessionLocal()
  try:
    yield db
  finally:
    db.close()
  
@app.post("/user_post",response_model = schemas.UserResponse)
async def create_user(user:schemas.UserCreate,
                      db : Session = Depends(get_db)):
  return crud.create_user(db,user)

@app.get("/user_get",response_model=list[schemas.UserResponse])
async def get_user(db: Session = Depends(get_db)):
  return crud.get_users(db)
  
@app.post("/login_user",response_description="you are allowed to enter")
async def login_user(user:schemas.Login_user,
                     db : Session = Depends(get_db)):
  
  db_user = crud.login_user(db,user.email,user.password)
  print(db_user)
  if not db_user:
    return {"message":"invalid email or password"}
  
  
  return {
    "Message":"Login Successfully",
    # "user_id" : db_user.id,
    "email" : user.email,
    "password" : user.password
  }