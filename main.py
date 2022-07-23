from typing import Union
from fastapi import  FastAPI
from pydantic import BaseModel, Required
from router import brand, model

app = FastAPI()

app.include_router(brand.router)
app.include_router(model.router)

@app.get('/')
async def index():
  return {"message": "Hello World"}