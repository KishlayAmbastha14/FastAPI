from fastapi import FastAPI,Header,Cookie,HTTPException
from typing import List,Annotated,Dict
from pydantic import BaseModel


app = FastAPI()

class CommonHeaders(BaseModel):
  host : str
  save_data : bool
  if_modified : str | None = None
  traceparent : str | None = None
  x_tag : list[str]  = []



@app.get("/items")
async def get_items(headers: Annotated[CommonHeaders,Header()]):
  return headers


# Chalo, ek real-world scenario lete hain. Ye task aapki aaj ki saari learnings (Path, Body, Cookie, aur Header Models) ko test karega.

# Request Body: Ek Pydantic model (Book) jisme title, author, aur price ho.
class Book(BaseModel):
  title : str 
  author : str
  price : int

# Header Model: Ek SecurityHeaders model banao jisme x_api_key (required) aur x_client_id (optional) ho.
class SecurityHeaders(BaseModel):
  x_api_Key : str
  x_client_Id : int  | None = None
# Cookie Model: Ek UserSession model banao jisme session_id (required) aur last_visit (optional) ho.

class UserSession(BaseModel):
  session_Id : str
  last_visit : str | None = None


# 📜 The Challenge: "The Secure Library System"
# Aapko ek API banani hai jo ek Library ke liye books update kare. Isme niche di gayi conditions honi chahiye:
# Path Parameter: Book ki unique book_id (int) URL mein honi chahiye.

@app.put("/bookss/{book_id}")
async def gettting_books(book_id:int,book:Book, headers : Annotated[SecurityHeaders,Header()],
                         cookies : Annotated[UserSession,Cookie()]):
  if headers.x_api_key != "kishlay123":
        raise HTTPException(status_code=401, detail="Invalid API Key!")

  return {
        "message": "Book updated successfully",
        "book_id": book_id,
        "details": book,
        "auth_info": headers,
        "session_info": cookies
    }


# 2. Yaha Header ka Model banao
class SecurityHeaders(BaseModel):
    # Hint: underscore use karna, FastAPI hyphen mein convert kar dega
    x_api_key: str | None = None
    x_client_id: str | None = None

# 3. Yaha Cookie ka Model banao
class UserSession(BaseModel):
    session_id: str | None = None
    last_visit: str | None = None

@app.put("/library/update/{book_id}")
async def update_book_record(
    # Sab kuch yaha extract karo:
    # book_id (path), book (body), headers (Header model), cookies (Cookie model)
    book_id: int,
    book: Book,
    headers: Annotated[SecurityHeaders, Header()],
    cookies: Annotated[UserSession, Cookie()]
):
    # EK CHHOTA SA LOGIC: 
    # Agar x_api_key "kishlay123" nahi hai, toh 401 error raise karo.
    if headers.x_api_key != "kishlay123":
        raise HTTPException(status_code=401, detail="Invalid API Key!")

    return {
        "message": "Book updated successfully",
        "book_id": book_id,
        "details": book,
        "auth_info": headers,
        "session_info": cookies
    }