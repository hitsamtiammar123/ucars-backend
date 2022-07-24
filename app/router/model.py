from fastapi import APIRouter, Path, Depends, Query
from datetime import datetime
from ..dependencies import get_db, validate_token
from ..database import Session, Model, Brand
from ..schemas import ModelInput
from ..exception import UnicornException
from ..util import filterNoneDictValue

router = APIRouter(
  prefix = '/model',
  tags = ['model'],
  dependencies = [Depends(validate_token)],
  responses = { 404: {'description': 'not found'}}
)

@router.get('/')
def index(
  db: Session = Depends(get_db),
  page: int = Query(default = 1),
  limit: int = Query(default = 10),
  search: str = Query(default = None)
):
  offset = (page - 1) * limit
  models = db.query(Model)
  if(search is not None):
    models = models.filter(Model.name.ilike('%' + search + '%'))
  
  models_count = models.count()
  models = models.limit(limit).offset(offset)
  models = models.all()
  
  return {'status': 200, 'models': models, 'page': page, 'count': models_count}

@router.get('/{id}')
def detail(db: Session = Depends(get_db), id: int = Path('ID of a brand')):
  model = db.query(Model).filter(Model.id == id).first()
  if(model == None):
    raise UnicornException(message='Model not found', status_code=404)
  model.brand = db.query(Brand).filter(Brand.id == model.brand_id).first()
  return {'status': 200, 'model': model }

@router.post('/')
def create(model: ModelInput, db: Session = Depends(get_db)):
  db_model = Model(
    name = model.name,
    description = model.description,
    image_url = model.image_url,
    status = model.status,
    brand_id = model.brand_id,
    price = model.price
  )
  try:
    db.add(db_model)
    db.commit()
    db.refresh(db_model)
  except:
    raise UnicornException(status_code=500, message="An error occured")
  
  return {'status': 201, 'message': "Model has been created", 'model': db_model}

@router.put('/{id}')
def update(
  input: ModelInput,
  db: Session = Depends(get_db),
  id: int = Path('ID of a model')
):
  try:
    filterNoneDictValue(input.__dict__)
    query_find = db.query(Model).filter(Model.id == id)
    d = query_find.update({**input.__dict__, 'updated_at' : datetime.now() })
    db.commit()
  except:
    raise UnicornException(status_code=500, message="An error occured")
  return {'status': 200, 'message': "Model Update: " + str(id), 'model': input, 'result': d}

@router.delete('/{id}')
def delete(
  db: Session = Depends(get_db),
  id: int = Path(title = 'The ID of a model')
):
  try:
    d = db.query(Model).filter(Model.id == id).delete()
    db.commit()
  except:
    raise UnicornException(status_code=500, message="An error occured")
  return {'status': 200, 'message': "Model Delete: " + str(id), 'model_id': id, 'result': d}