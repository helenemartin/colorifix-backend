from fastapi import HTTPException, status
from db.models import DbUser
from routers.schemas import UserBase
from sqlalchemy.orm.session import Session

def create_user(db: Session, request: UserBase):
  new_user = DbUser(
    username = request.username
  )
  db.add(new_user)
  db.commit()
  db.refresh(new_user)
  return new_user


def get_all(db: Session):
  return db.query(DbUser).all()