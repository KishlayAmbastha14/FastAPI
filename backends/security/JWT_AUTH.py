# first install pyjwt ( to generate JWT TOKENS )
# now install this for hashing and this is best for python hashing "pwdlib[argon2]"

# AB ye install kr o "from pwdlib import PasswordHash" for password ko hash krne k liye and verify k liye

from fastapi import FastAPI,Depends,HTTPException,status
from fastapi.security import OAuth2PasswordBearer,OAuth2PasswordRequestForm
from pydantic import BaseModel
import jwt 
from datetime import datetime,timedelta,timezone
from typing import Annotated
from jwt.exceptions import InvalidTokenError
# its used when 1. Expired ho 2.Tampered ho 3. Wrong signature ho
from pwdlib import PasswordHash


SECRET_KEY = "09d25e094faa6ca2556c818166b7a9563b93f7099f6f0f4caa6cf63b88e8d3e7"
ALGORITHM = "HS256"
ACCESS_TOKEN_EXPIRE_MINUTES = 30