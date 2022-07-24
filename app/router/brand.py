from datetime import datetime
from fastapi import APIRouter, Path, Depends, Query
from ..dependencies import get_db, validate_token
from ..database import Session, Brand, Model
from ..schemas import BrandInput
from ..exception import UnicornException
from ..util import filterNoneDictValue

router = APIRouter(
  prefix = '/brand',
  tags = ['brand'],
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
  brands = db.query(Brand)
  
  if(search is not None):
    brands = brands.filter(Brand.name.ilike('%' + search + '%'))
  
  brands_count = brands.count()
  brands = brands.limit(limit).offset(offset)
  brands = brands.all()
  
  for brand in brands:
    models_query =  db.query(Model).filter(Model.brand_id == brand.id)
    brand.model_count = models_query.count()
    
  
  return {'status': 200, 'brands': brands, 'page': page, 'count': brands_count}

@router.get('/{id}')
def detail(db: Session = Depends(get_db), id: int = Path('ID of a brand')):
  brand = db.query(Brand).filter(Brand.id == id).first()
  if(brand == None):
    raise UnicornException(message = 'Brand not found', status_code= 404)
  brand.models = db.query(Model).filter(Model.brand_id == id).all()
  return {'status': 200, 'brand': brand }

@router.post('/', status_code = 201)
def create(brand: BrandInput, db: Session = Depends(get_db)):
  db_user = Brand(
    name = brand.name,
    description = brand.description,
    image_url = brand.image_url,
    status = brand.status
  )
  try:
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
  except:
    raise UnicornException(status_code=500, message="An error occured")
  
  return {'status': 201, 'message': "Brand has been created", 'brand': db_user}

@router.put('/{id}')
def update(
  input: BrandInput,
  db: Session = Depends(get_db),
  id: int = Path('ID of a brand')
):
  try:
    filterNoneDictValue(input.__dict__)
    query_find = db.query(Brand).filter(Brand.id == id)
    d = query_find.update({**input.__dict__, 'updated_at' : datetime.now() })
    db.commit()
  except:
    raise UnicornException(status_code=500, message="An error occured")
  return {'status': 200, 'message': "Brand Update: " + str(id), 'brand': input, 'result': d}

@router.delete('/{id}')
def delete(db: Session = Depends(get_db), id: int = Path(title = 'The ID of a brand') ):
  try:
    d = db.query(Brand).filter(Brand.id == id).delete()
    db.commit()
  except:
    raise UnicornException(status_code=500, message="An error occured")
  return {'status': 200, 'message': "Brand Delete: " + str(id), 'brand_id': id, 'result': d}