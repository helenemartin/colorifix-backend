from fastapi import HTTPException, status
from db.models import DbCompany
from routers.schemas import CompanyBase
from sqlalchemy.orm.session import Session


def create_company(db: Session, request: CompanyBase):
  new_company = DbCompany(
    name=request.name
  )
  db.add(new_company)
  db.commit()
  db.refresh(new_company)
  return new_company


def get_all(db: Session):
  return db.query(DbCompany).all()