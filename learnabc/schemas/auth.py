from learnabc.database import Base
from typing import List, Optional
from pydantic import BaseModel


class Login(BaseModel):
    username: str
    password: str


class Token(BaseModel):
    access_token: str
    token_type: str


class TokenOAuth(BaseModel):
    token: str


class TokenData(BaseModel):
    email: Optional[str] = None
