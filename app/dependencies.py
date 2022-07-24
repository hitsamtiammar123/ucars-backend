from .database import session

def get_db():
  yield session