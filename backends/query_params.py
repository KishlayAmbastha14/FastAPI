from fastapi import FastAPI,HTTPException,Path,Query

from typing import List,Literal,Optional,Annotated

from pydantic import BaseModel,Field

app = FastAPI()


class FiltterParams(BaseModel):
  limit: int = Field(100,gt=0,le=100)
  offset: int = Field(0,ge=0)
  order_by: Literal["created_at","updated_at"] = "created_at"
  tags: list[str] = []

@app.get("/items/")
async def read_items(filter_query: Annotated[FiltterParams, Query()]):
  return filter_query



class FilterParams(BaseModel):
    model_config = {"extra": "forbid"}

    limit: int = Field(100, gt=0, le=100)
    offset: int = Field(0, ge=0)
    order_by: Literal["created_at", "updated_at"] = "created_at"
    tags: list[str] = []


@app.get("/items/")
async def read_items(filter_query: Annotated[FilterParams, Query()]):
    return filter_query



# Create an API:

class PaginationParams(BaseModel):
   page:int=Field(default=1,ge=1)
   size:int = Field(default=10,ge=1,le=50)

@app.get("/page/")
async def read_page(paging: Annotated[PaginationParams, Query()]):
   return paging


# GET /products
# Create a model SortParams:

# Field	Rule
# sort_by	"price" or "rating"
# order	"asc" or "desc"

# 🔹 Default sorting → price, asc

class SortParams(BaseModel):
  sort_by: Literal["price","rating"] = "price"
  order: Literal['asc','desc'] = "asc"

@app.get("/products")
async def getting_products(product:Annotated[SortParams,Query()]):
   return {
      "sort_by" : product.sort_by,
      "order" : product.order
   }


# GET /users/filter
# Create model UserFilter:

# Field	Rule
# min_age	optional int, ge=0
# max_age	optional int, le=100
# active	optional bool
# role	optional "admin", "user"

# 🔹 Return filters received

class UserFilter(BaseModel):
   min_age: Optional[int] = Field(None,ge=0)
   max_age: Optional[int] = Field(None,le=100)
   active: Optional[bool] = None
   role: Optional[Literal["admin","user"]] = None


@app.get("/userss/filter")
async def filter_users(filtered:Annotated[UserFilter,Query()]):
   return filtered