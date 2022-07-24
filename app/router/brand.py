from datetime import datetime
from fastapi import APIRouter, Path, Depends, HTTPException
from sqlalchemy import update
from ..dependencies import get_db
from ..database import Session, Brand
from ..schemas import BrandInput
from ..exception import UnicornException
from ..util import filterNoneDictValue

router = APIRouter(
  prefix = '/brand',
  tags = ['brand'],
  dependencies = [],
  responses = { 404: {'description': 'not found'}}
)

@router.get('/')
def index(db: Session = Depends(get_db) ):
  brands = db.query(Brand).all()
  return {'status': 200, 'brand': brands}

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
  
  return {'status': 201, 'message': "Brand has been created", 'brand': brand}

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
    raise UnicornException(status_code=500, detail="An error occured")
  return {'status': 200, 'message': "Brand Update: " + str(id), 'brand': input, 'result': d}

@router.delete('/{id}')
def delete(db: Session = Depends(get_db), id: int = Path(title = 'The ID of a brand')):
  try:
    d = db.query(Brand).filter(Brand.id == id).delete()
    db.commit()
  except:
    raise UnicornException(status_code=500, detail="An error occured")
  return {'status': 200, 'message': "Brand Delete: " + str(id), 'brand_id': id, 'result': d}