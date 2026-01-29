from fastapi import FastAPI,HTTPException,Query,Path
from typing import List,Dict,Literal,Annotated,Optional



app = FastAPI()

# @app.get("/items/{item_id}")
# async def getitems(item_id : Annotated[int, Path(title = "enter the id of the items")],
#                    q: Annotated[str|None, Query(alias="item-query")] = None):
#   results = {"item_Id":item_id}
#   if q:
#     results.update({"q":q})

#   return results

@app.get("/itemsss/{item_idd}")
async def get_results(q:str, item_idd:int = Path(title="The ID of the item to get")):
  result = {"item_id": item_idd}
  if q:
    result.update({"q": q})
  return result

@app.get("/data/{data_id}")
async def data_result(data_id:Annotated[int,Path(title="enter the title")],q:str):
  results = {"data_id is ":data_id}

  if q:
    results.update({"q":q})
  return results



# Expected URLs:
@app.get("/users/{user_id}")
async def user_finding(user_id:Annotated[int,Path(title="enter the user id to find",ge=1,le=100)],active:Annotated[bool|None,Query()] = None):
  result = {"user_id is ":user_id}
  if active is False:
    result.update({"description":"this things is not avalailabe"})
  return result


@app.get("/product/{product_id}")
async def product_finding(product_id:Annotated[int,Path(title="enter the prodcut_id",gt=0,le=500)],
                          # category:Annotated[Optional[str],Query(alias='cat')]):
                          category:Annotated[str|None,Query(alias="cat")] = None):
  result = {"the product id is ": product_id}

  if category:
    result.update({"the category is":{category}})
  return result

# Q3

# Create:

# GET /search/{page_no}
# Rules:
# page_no → Path
# int
# ge=1
# q → Query
# required
# strin
# ⚠️ If user hits:
# /search/1

@app.get("/search/{page_no}")
async def searching_page(page_no:Annotated[int,Path(title='enter the page_no',ge=1)],q:Annotated[str,Query(title="required q")]):
  result = {"the current page you fetch is ":page_no}

  if q:
    result.update({"q":q})
  return result


# FastAPI should throw validation error.

# Q4

# Create:
# GET /orders/{order_id}
# Rules:
# order_id → Path
# int
# gt=100
# discount → Query
# optional float
# ge=0, le=50

@app.get("/orderss/{order_id}")
async def ordering(order_id:Annotated[int,Path(title="enter the order_id want to fetch",gt=100)],
                   discount:Annotated[float | None,Query(title="neter the discount",ge=0,le=50)] = None):
  result = {"user picked this user_id":order_id}

  if discount is not None:
    result.update({"the discount on this id is":discount})

  return result


# reate:
# GET /rating/{movie_id}
# Rules:
# movie_id → Path
# int
# ge=1
# rating → Query
# float
# must be > 0 and < 10
#Test cases:
@app.get("/ratings/{movie_id}")
async def fetchin_movie_id(movie_id:Annotated[int,Path(title='proivde here movie_id',ge=1)],
                           rating: Annotated[float,Query(title="provide me rating for particular movie is",gt=0,lt=10)]):
  # result = {"you fetched this particular movie id " :{movie_id}}

  # if rating:
  #   result.update({"the particular rating of this movie id is ":rating})
  # return result
  return{
    "movie_id":movie_id,
    "rating" : rating
  }
# /rating/10?rating=8.5   ✅
# /rating/10?rating=0     ❌
# /rating/10?rating=10    ❌



# 🔵 LEVEL 4: Order + Annotated Confidence
# Q6
# Create:
# GET /students/{student_id}
# Rules:
# Use Annotated
# student_id → Path
# int
# gt=0
# marks → Query
# optional int
# ge=0, le=100
# subject → Query
# # required string

@app.get("/students/{student_id}")
async def student_finding(student_id:Annotated[int,Path(title="provide me id ",gt=0)],
                          # marks: Annotated[int|None,Query(title="provde me marks otherewise its default",ge=0,le=100)] = None,
                          subject:Annotated[str,Query(title="provide me subject name")],
                          marks: Annotated[Optional[int],Query(title="provide me marks",ge=0,le=100)] = None):

  return {
    "subject_id" : student_id,
    "subject" : subject,
    "marks" : marks
  }
    


# 🔴 LEVEL 5: Trick Question (Exam Favorite)
# Q7
# Create:
# GET /items/{item_id}
# Rules:
# Do NOT use Query() for q
# q must still be required
# item_id must use Path
# Use Annotated
# Any order of parameters should work

@app.get("/items/{item_id}")
async def items_founding(item_id:Annotated[int,Path(title="provide me item_id")],
                         q:str):
  return {
    "item_id is fetched is " : item_id,
    "q is ": q
        }