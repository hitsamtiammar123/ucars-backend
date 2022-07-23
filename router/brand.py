from fastapi import APIRouter, Path

router = APIRouter(
  prefix = '/brand',
  tags = ['brand'],
  responses = { 404: {'description': 'not found'}}
)

@router.get('/')
def index():
  return {'index': "Brand index"}

@router.post('/')
def create():
  return {'index': "Brand Post"}

@router.put('/{id}')
def update(id: int = Path('ID of a brand')):
  return {'index': "Brand Update: " + id}

@router.delete('/{id}')
def delete(id: int = Path(title = 'The ID of a brand')):
  return {'index': "Brand index: " + id}