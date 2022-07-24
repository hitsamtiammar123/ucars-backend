from fastapi import  FastAPI, Request
from fastapi.responses import JSONResponse
from .router import brand, model
from .exception import UnicornException

app = FastAPI()

app.include_router(brand.router)
app.include_router(model.router)

app.exception_handler(UnicornException)
def unicorn_exception_handler(request: Request, exc: UnicornException):
  return JSONResponse(
    status_code = exc.status_code,
    content = {'message': exc.message, 'data': exc.data }
  )

@app.get('/')
async def index():
  return {"message": "Hello World"}
