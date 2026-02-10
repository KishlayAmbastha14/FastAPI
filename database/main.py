from fastapi import FastAPI, Depends,HTTPException
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

# def get_db():
#   db = SessionLocal()
#   try: 
#     yield db
#   finally:
#     db.close()

# from sqlalchemy.ext.asyncio import AsyncSession
# from fastapi import Depends

# async def get_db() -> AsyncSession:
#   async with AsyncSessionLocal() as session():
#     try:
#       yield session
#     finally:
#       await session.close()


@app.post("/user_post",response_model = schemas.UserResponse)
async def create_user(user:schemas.UserCreate,
                      db : Session = Depends(get_db)):
  return crud.create_user(db,user)

@app.get("/user_get",response_model=list[schemas.UserResponse])
async def get_user(db: Session = Depends(get_db)):
  return crud.get_users(db)

# @app.delete("/deleted_user/{user_id}",response_description='this user id is delted')
# async def delted_user(user_id:int,db:Session=Depends(get_db)):
#   db_delete_user = crud.delete_user(db,user_id)

#   print(db_delete_user)

#   if not db_delete_user:
#     raise HTTPException(status_code=404,detail="No user found sorry")
  
@app.delete("/delete_user/{user_id}")
async def delete_user(user_id: int,
                      db: Session = Depends(get_db)):
    deleted_user = crud.delete_user(db, user_id)

    if not deleted_user:
        return {"message": "User not found"}

    return {
        "message": "User deleted successfully",
        "deleted_user_id": deleted_user.id
    }

  
@app.post("/login_user",response_description="you are allowed to enter")
async def login_user(user:schemas.Login_user,
                     db : Session = Depends(get_db)):
  
  db_user = crud.login_user(db,user)
  print(db_user)
  if not db_user:
    return {"message":"invalid email or password"}
  
  
  return {
    "Message":"Login Successfully",
    # "user_id" : db_user.id,
    "email" : user.email,
    "password" : user.password
  }