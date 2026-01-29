from datetime import datetime,time,timedelta
from typing import Annotated
from uuid import UUID
from fastapi import FastAPI,Body
from pydantic import BaseModel


app = FastAPI()

@app.put("/items/{item_id}")
async def read_items(
  item_id : int,
  start_datetime : Annotated[datetime,Body()],
  end_datetime : Annotated[datetime,Body()],
  process_after : Annotated[timedelta,Body()],
  repeat_at : Annotated[time | None, Body()]  = None
):
  start_process = start_datetime + process_after
  duration = end_datetime - start_process
  return {
      "item_id": item_id,
      "start_datetime": start_datetime,
      "end_datetime": end_datetime,
      "process_after": process_after,
      "repeat_at": repeat_at,
      "start_process": start_process,
      "duration": duration,
    }