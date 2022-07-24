from typing import List, Union
from datetime import datetime
from xmlrpc.client import Boolean
from pydantic import BaseModel

class Base(BaseModel):
  name: Union[str, None] = None
  description: str = None
  image_url: str = None
  status: Boolean = None
  

class BrandBase(Base):
  pass

class ModelBase(Base):
  brand_id: Union[int, None] = None
  brand: BrandBase = None

class BrandInput(BrandBase):
  pass

class Brand(BrandBase):
  models: List[ModelBase] = []
  
  class Config:
        orm_mode = True

class Model(Base):
  brand: Union[BrandBase, None] = None
  
  class Config:
        orm_mode = True
  