from learnabc.database import Base
from typing import List, Optional, Union
from pydantic import BaseModel, validator
from .base import User


class UserEmail(BaseModel):
    email: str


class RequestCourse(BaseModel):
    name: str
    description: str


class InscriptionUser(BaseModel):
    user: User
    calification: int

    class Config():
        orm_mode = True


class ShowCourse(BaseModel):
    id: int
    name: str
    description: str
    creator: User
    code: Optional[str]
    delegate: Optional[User]
    inscriptions: List[InscriptionUser] = []

    @validator('delegate')
    def valid_delegate(cls, v):
        if v is not None:
            return v

    @validator('code')
    def valid_code(cls, v):
        if v is not None:
            return v

    class Config():
        orm_mode = True


class CalificationRequest(BaseModel):
    calification: int
