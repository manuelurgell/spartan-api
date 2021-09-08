import datetime
from typing import Optional

from pydantic import BaseModel


class BaseUser(BaseModel):
    id: int
    email: str
    name: str
    last_name: str
    birthdate: datetime.date
    phone: Optional[int]
    created_at: datetime.datetime
    last_modified: Optional[datetime.datetime]
    # last_login: Optional[datetime.datetime]


class CreateUser(BaseModel):
    email: str
    # password: str
    name: str
    last_name: str
    birthdate: datetime.date
    phone: Optional[int]


class RetrieveUser(BaseModel):
    id: int
    email: str
    name: str
    last_name: str
    birthdate: datetime.date
    phone: Optional[int]


class UpdateUser(BaseModel):
    name: Optional[str]
    last_name: Optional[str]
    birthdate: Optional[datetime.date]
    phone: Optional[int]


class RetrieveUpdatedUser(BaseModel):
    id: int
    name: Optional[str]
    last_name: Optional[str]
    birthdate: Optional[datetime.date]
    phone: Optional[int]
