import datetime
from typing import Optional

from pydantic import BaseModel


class BaseTeam(BaseModel):
    id: int
    name: str
    created_at: datetime.datetime
    last_modified: Optional[datetime.datetime]


class CreateTeam(BaseModel):
    name: str


class RetrieveTeam(BaseModel):
    id: int
    name: str


class RetrieveUpdatedTeam(BaseModel):
    id: int
    name: str
