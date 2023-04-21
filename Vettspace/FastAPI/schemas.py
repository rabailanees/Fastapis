from pydantic import BaseModel
from typing import Optional, List


class Registration(BaseModel):
    first_name: str
    last_name: str
    email: str
    password: str


class RegistrationUpdate(BaseModel):
    first_name: Optional[str]
    last_name: Optional[str]
    email: Optional[str]
    password: Optional[str]


class ShowUser(BaseModel):
    first_name: str
    last_name: str
    email: str
    class Config():
        orm_mode = True


class Login(BaseModel):
    email: str
    password: str


class Token(BaseModel):
    access_token: str
    token_type: str


class TokenData(BaseModel):
    email: Optional[str] = None


# class PasswordUpdate(BaseModel):
#     email: str
#     password: str
#     status: bool = False
