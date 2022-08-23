from pydantic import BaseModel


class UserBase(BaseModel):
    username: str
    companyname: str


class CompanyBase(BaseModel):
    name: str


class UserDisplay(BaseModel):
    username: str
    class Config():
        orm_mode = True


class CompanyDisplay(BaseModel):
    name: str
    class Config():
        orm_mode = True