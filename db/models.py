from sqlalchemy.orm import relationship
from .database import Base
from sqlalchemy import Column, Integer, String, ForeignKey


class DbUser(Base):
    __tablename__ = 'user'
    id = Column(Integer, primary_key=True, index=True)
    username = Column(String)
    company_id = Column(Integer, ForeignKey("company.id"))

class DbCompany(Base):
    __tablename__ = 'company'
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, unique=True)
    users = relationship(DbUser)

