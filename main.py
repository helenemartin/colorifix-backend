from fastapi import FastAPI
from sqlalchemy.sql.functions import user
from db import models
from db.database import engine
from routers import user, company
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

app.include_router(user.router)
app.include_router(company.router)


@app.get("/")


def root():
  return "Hello me!"


origins = [
  'http://localhost:3000',
  'http://localhost:3001',
  'http://localhost:3002'
]

app.add_middleware(
  CORSMiddleware,
  allow_origins=origins,
  allow_credentials=True,
  allow_methods=['*'],
  allow_headers=['*']
)


models.Base.metadata.create_all(engine)
