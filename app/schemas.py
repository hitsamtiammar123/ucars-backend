from tokenize import Number
from typing import List, Union
from xmlrpc.client import Boolean
from pydantic import BaseModel

class UserLogin(BaseModel):
  email: str
  password: str
class Base(BaseModel):
  name: str
  description: Union[str, None] = None
  image_url: Union[str, None] = None
  status: Union[Boolean, None] = None
  

class BrandBase(Base):
  pass

class ModelBase(Base):
  brand_id:  Union[int, None] = None
  brand: Union[BrandBase, None] = None
  price: Union[float, None] = None

class BrandInput(BrandBase):
  pass

class ModelInput(ModelBase):
  pass

class Brand(BrandBase):
  models: List[ModelBase] = []
  
  class Config:
        orm_mode = True
        
class Model(ModelBase):
  brand: Union[BrandBase, None] = None
  
  class Config:
        orm_mode = True