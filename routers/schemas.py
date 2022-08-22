from pydantic import BaseModel


class UserBase(BaseModel):
    username: str


class UserDisplay(BaseModel):
    username: str
    class Config():
        orm_mode = True
