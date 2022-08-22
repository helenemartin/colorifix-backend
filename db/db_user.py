from fastapi import HTTPException, status
from db.models import DbUser
from routers.schemas import UserBase
from sqlalchemy.orm.session import Session
import re
regex = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b'


def create_user(db: Session, request: UserBase):
  if not (re.fullmatch(regex, request.username)):
    raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=f'{request.username} user must be an email address ')


  new_user = DbUser(
    username = request.username
  )
  db.add(new_user)
  db.commit()
  db.refresh(new_user)
  return new_user


def get_all(db: Session):
  return db.query(DbUser).all()