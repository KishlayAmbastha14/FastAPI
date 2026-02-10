from sqlalchemy.orm import Session
from . import models,schemas
from .security_file import hash_password,verify_password
from .models import User


def create_user(db:Session,user: schemas.UserCreate):
  print("Password length:", len(user.password))
  print("Password value:", user.password)

  hashed_pw = hash_password(user.password)
  new_user = models.User(
    email = user.email,
    password = hashed_pw
  )

  db.add(new_user)
  db.commit()
  db.refresh(new_user)

  return new_user


def get_users(db:Session):
  return db.query(models.User).all()



try: 
  def login_user(db:Session,user:schemas.Login_user):

    db_user = db.query(User).filter(User.email == user.email).first()
    # password = db.query(User).filter(user.password)
    if not db_user:
      return False
    if not verify_password(user.password,db_user.password):
      return False
  
    #return {"message": "you have given correct information"}
    
except Exception as e:
  print(e)

try:
  def delete_user(db:Session, user_id:int):
    db_user_delete = db.query(User).filter(User.id == user_id).first()
    if not db_user_delete:
      return {'message' : "sorry this user is not there "}
    
    db.delete(db_user_delete)

    db.commit()
    # print(db_user_delete)
    return db_user_delete
except Exception as e:
  print(e)


# def login_user(db:Session,user:schemas.UserCreate):
#   new_user = models.User(
#     email = user.email,
#     password = user.password
#   )
#   people1 = db.query(new_user).filter(user.email == new_user.email).first()

#   if not people1:
#     return False
#   if not verify_password(,new_user.password):
#     return False



# from sqlalchemy.orm import Session

# # liike here we import this beacaue har ek user k liye alaga laga session bnae  so that we can store in DB

# from . import models,schemas

# # iha hamne ye kiya hai models and schmeas ko iss file me bulaya ki like its uses like to works with moddels like kaisa mera table k structured hai and kya kya chiz hai table me and here we also call shcmeas because ki mera kaun sa or ky schmeans maine define kiya like when we are dealting with create_user and so ye sb ka kaam pdega

# def create_user(db:Session,user = schemas.UserCreate):
#   ## like hamne ek function ko bnaya hai or iska kaam hai ki like ye har time new user jo create krega usek liye ek seesion banaayega and uska vlaue bolegga dalanne ko hamne Usercreate me i.e schmeas me banaya like iha mera pass email and password hai 
#   new_user = models.User(
#     email = user.email,
#     password = user.password
#   )
#   ## now i want to say  that ki iha upar me kya kiya maine like here we store in new_user me like jobhi person apna email dega and password woo sb new_user me store hoga with the help of models.User se like we deifne in our model.py file joki hamanrar table hai bna hua static 
#   db.add(new_user)
#   ## iha hamne add kiya hai new_user ko session me 
#   db.commit()
#   ## iha hhamne commit isliye kyuki ye real insert data ko bhejta hai
#   db.refresh(new_user)
#   ## ab ye isliye kiyya kkyuki like db se koi vlaues lana hai to we can fetch through this and also ye auto generated ID ko bhi fill krta hai 

#   return new_user # now iha hamne data ko return kr diya

# def get_user(db:Session):
#   return db.query(models.User).all()















