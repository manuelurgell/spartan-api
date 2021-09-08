from typing import List

from asyncpg.exceptions import ForeignKeyViolationError, UniqueViolationError

from fastapi import HTTPException

from app import app

from db import database

from models import teams, users

from schemas.team import (
    BaseTeam,
    CreateTeam,
    RetrieveTeam,
    RetrieveUpdatedTeam
)
from schemas.user import (
    BaseUser,
    CreateUser,
    RetrieveUpdatedUser,
    RetrieveUser,
    UpdateUser
)


# Team CRUD
@app.get("/teams/",
         response_model=List[BaseTeam],
         response_model_exclude_none=True)
async def team_list():
    query = teams.select()
    return await database.fetch_all(query)


@app.post("/teams/", response_model=RetrieveTeam)
async def team_create(team: CreateTeam):
    query = teams.insert().values(**team.dict())
    try:
        obj_id = await database.execute(query)
    except UniqueViolationError:
        raise HTTPException(status_code=400, detail="Team name already exists")
    return {**team.dict(), "id": obj_id}


@app.get("/teams/{team_id}",
         response_model=BaseTeam,
         response_model_exclude_none=True)
async def team_retrieve(team_id: int):
    query = teams.select().where(teams.c.id == team_id)
    record = await database.fetch_one(query)
    if record is None:
        raise HTTPException(status_code=404, detail="Team not found")
    return record


@app.patch("/teams/{team_id}",
           response_model=RetrieveUpdatedTeam,
           response_model_exclude_none=True)
async def team_update(team_id: int, team: CreateTeam):
    query = teams.update().values(
        **team.dict(exclude_unset=True)
    ).where(teams.c.id == team_id)

    await database.execute(query)
    return {**team.dict(), "id": team_id}


@app.delete("/teams/{team_id}")
async def team_delete(team_id: int):
    query = teams.delete().where(teams.c.id == team_id)
    await database.execute(query)
    return {"deleted": team_id}


# User CRUD
@app.get("/users/",
         response_model=List[BaseUser],
         response_model_exclude_none=True)
async def user_list():
    query = users.select()
    return await database.fetch_all(query)


@app.post("/users/",
          response_model=RetrieveUser,
          response_model_exclude_none=True)
async def user_create(user: CreateUser):
    query = users.insert().values(**user.dict())
    try:
        obj_id = await database.execute(query)
    except UniqueViolationError:
        raise HTTPException(
            status_code=400, detail="User email already exists"
        )
    except ForeignKeyViolationError:
        raise HTTPException(
            status_code=400, detail="team_id is not associated with a team"
        )
    return {**user.dict(), "id": obj_id}


@app.get("/users/{user_id}",
         response_model=BaseUser,
         response_model_exclude_none=True)
async def user_retrieve(user_id: int):
    query = users.select().where(users.c.id == user_id)
    record = await database.fetch_one(query)
    if record is None:
        raise HTTPException(status_code=404, detail="User not found")
    return record


@app.patch("/users/{user_id}",
           response_model=RetrieveUpdatedUser,
           response_model_exclude_none=True)
async def user_update(user_id: int, user: UpdateUser):
    query = users.update().values(
        **user.dict(exclude_unset=True)
    ).where(users.c.id == user_id)

    await database.execute(query)
    return {**user.dict(), "id": user_id}


@app.delete("/users/{user_id}")
async def user_delete(user_id: int):
    query = users.delete().where(users.c.id == user_id)
    await database.execute(query)
    return {"deleted": user_id}
