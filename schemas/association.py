import datetime
from typing import List, Optional

from pydantic import BaseModel


class BaseAssociation(BaseModel):
    id: int
    team_id: int
    user_id: int


class CreateAssociation(BaseModel):
    team_id: int
    user_id: int


class UpdateAssociation(BaseModel):
    team_id: Optional[int]
    user_id: Optional[int]


class RetrieveUpdatedAssociation(BaseModel):
    id: int
    team_id: Optional[int]
    user_id: Optional[int]


class TeamAssociation(BaseModel):
    id: int
    name: str


class RetrieveUserAssociation(BaseModel):
    id: int
    email: str
    name: str
    last_name: str
    birthdate: datetime.date
    phone: Optional[str]
    teams: List[TeamAssociation]


class UserAssociation(BaseModel):
    id: int
    email: str
    name: str
    last_name: str
    birthdate: datetime.date
    phone: Optional[str]


class RetrieveTeamAssociation(BaseModel):
    id: int
    name: str
    users: List[UserAssociation]
