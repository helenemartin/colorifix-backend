from sqlalchemy.orm.session import Session
from routers.schemas import CompanyBase, CompanyDisplay
from fastapi import APIRouter, Depends
from db.database import get_db
from db import db_company

router = APIRouter(
  prefix='/company',
  tags=['company']
)

@router.post('', response_model=CompanyDisplay)
def create_company(request: CompanyBase, db: Session = Depends(get_db)):
  return db_company.create_company(db, request)

@router.get('/all')
def companies(db: Session = Depends(get_db)):
  return db_company.get_all(db)

