from fastapi import FastAPI
from sqlalchemy.sql.functions import user
from db import models
from db.database import engine
from routers import user

app = FastAPI()

app.include_router(user.router)

@app.get("/")

def root():
  return "Hello me!"


models.Base.metadata.create_all(engine)
