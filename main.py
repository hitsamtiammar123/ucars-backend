from typing import Union

from fastapi import FastAPI, Query, Path
from pydantic import BaseModel, Required

app = FastAPI()

class Item(BaseModel):
    name: str
    description: Union[str, None] = None
    price: float
    tax: Union[float, None] = None


@app.get("/")
async def read_root():
    return {"Hello": "World Hehehe test"}


@app.get("/items/{item_id}")
async def read_item(
  item_id: int =  Path(title="Id of an item"), 
  q: Union[str, None] = Query(default = Required, max_length = 4)
  ):
    print(q)
    print('test')
    return {"item_id": item_id, "q": q}
  

@app.post('/test-post')
async def test_post(item:Item):
  return item