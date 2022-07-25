import jwt
import os
from fastapi import Header
from .database import session
from .exception import UnicornException

def get_db():
  yield session
  

async def validate_token(x_token: str = Header(default=None)):
  pass
  # if(x_token == None):
  #   raise UnicornException(message='Please add X-TOKEN to header', status_code=401)
  
  # try:
  #   jwt.decode(x_token, os.environ.get('JWT_SECRET', 'uC@rsJWTForTesting'), algorithms=['HS256'])
  # except jwt.ExpiredSignatureError:
  #   raise UnicornException(message='Token Expired', status_code=401, data = {'status': 1})
  # except Exception:
  #   raise UnicornException(message='Token invalid', status_code=401, data = {'status': 0})