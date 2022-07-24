from datetime import datetime, timedelta
import traceback
import jwt
import os
from fastapi import  FastAPI, Request
from fastapi.responses import JSONResponse
from .router import brand, model
from .exception import UnicornException
from .schemas import UserLogin


app = FastAPI()

app.include_router(brand.router)
app.include_router(model.router)

@app.exception_handler(UnicornException)
def unicorn_exception_handler(request: Request, exc: UnicornException):
  return JSONResponse(
    status_code = exc.status_code,
    content = {'message': exc.message, 'data': exc.data, 'errors': traceback.format_exc() }
  )

@app.get('/')
async def index():
  return {"message": "Hello World"}


@app.post('/login')
async def login(input: UserLogin):
    data = { 'email': input.email, 'exp': datetime.now() + timedelta(hours=1)}
    if(input.email == 'admin@mail.com' and input.password == 'ucarsadmin'):
      try:
        encoded_jwt = jwt.encode(data, os.environ.get('JWT_SECRET', 'uC@rsJWTForTesting'))
      except Exception:
        raise UnicornException(message='Failed to encode token, please try again later', status_code=400)
    else:
      raise UnicornException(message='email or password is wrong, please try again later', status_code=401)
    
    return {'message': 'Successfully generated token', 'token': encoded_jwt}    