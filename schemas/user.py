import datetime
from typing import Optional

from pydantic import BaseModel


class BaseUser(BaseModel):
    id: int
    email: str
    name: str
    last_name: str
    birthdate: datetime.date
    phone: Optional[str]
    created_at: datetime.datetime
    last_modified: Optional[datetime.datetime]
    # last_login: Optional[datetime.datetime]


class CreateUser(BaseModel):
    email: str
    # password: str
    name: str
    last_name: str
    birthdate: datetime.date
    phone: Optional[str]


class RetrieveUser(BaseModel):
    id: int
    email: str
    name: str
    last_name: str
    birthdate: datetime.date
    phone: Optional[str]


class UpdateUser(BaseModel):
    name: Optional[str]
    last_name: Optional[str]
    birthdate: Optional[datetime.date]
    phone: Optional[str]


class RetrieveUpdatedUser(BaseModel):
    id: int
    name: Optional[str]
    last_name: Optional[str]
    birthdate: Optional[datetime.date]
    phone: Optional[str]
