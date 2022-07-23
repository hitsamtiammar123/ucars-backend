from fastapi import APIRouter, Path

router = APIRouter(
  prefix = '/model',
  tags = ['model'],
  responses = { 404: {'description': 'not found'}}
)

@router.get('/')
def index():
  return {'index': "Model index"}

@router.post('/')
def create():
  return {'index': "Model Post"}

@router.put('/{id}')
def update(id: int = Path('ID of a model')):
  return {'index': "Model Update: " + id}

@router.delete('/{id}')
def delete(id: int = Path(title = 'The ID of a model')):
  return {'index': "Model index: " + id}