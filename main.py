from typing import List

from asyncpg.exceptions import ForeignKeyViolationError, UniqueViolationError

from fastapi import HTTPException

from app import app

from db import database

from models import associations, teams, users

from schemas.association import (
    BaseAssociation,
    CreateAssociation,
    RetrieveTeamAssociation,
    RetrieveUpdatedAssociation,
    RetrieveUserAssociation,
    UpdateAssociation
)
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


# Association CRUD
@app.get("/associations/", response_model=List[BaseAssociation])
async def association_list():
    query = associations.select()
    return await database.fetch_all(query)


@app.post("/associations/", response_model=BaseAssociation)
async def association_create(association: CreateAssociation):
    query = associations.insert().values(**association.dict())
    try:
        obj_id = await database.execute(query)
    except UniqueViolationError:
        raise HTTPException(
            status_code=400, detail="Relation already exists"
        )
    except ForeignKeyViolationError:
        raise HTTPException(
            status_code=400, detail="model_id is not associated with a model"
        )
    return {**association.dict(), "id": obj_id}


@app.get("/associations/{association_id}", response_model=BaseAssociation)
async def association_retrieve(association_id: int):
    query = associations.select().where(associations.c.id == association_id)
    record = await database.fetch_one(query)
    if record is None:
        raise HTTPException(status_code=404, detail="User not found")
    return record


@app.get("/associations/by-user/{user_id}",
         response_model=RetrieveUserAssociation,
         response_model_exclude_none=True)
async def association_retrieve_by_user(user_id: int):
    query = users.select().where(users.c.id == user_id)
    user = await database.fetch_one(query)
    if user is None:
        raise HTTPException(status_code=404, detail="User not found")
    user = {k: v for k, v in user.items()}

    query = teams.select().where(associations.c.user_id == user_id).join(
        associations, associations.c.team_id == teams.c.id
    )
    team_list = await database.fetch_all(query)
    team_list = [{
        "id": team.get("id"),
        "name": team.get("name")
    } for team in team_list]

    return {**user, "teams": team_list}


@app.get("/associations/by-team/{team_id}",
         response_model=RetrieveTeamAssociation,
         response_model_exclude_none=True)
async def association_retrieve_by_team(team_id: int):
    query = teams.select().where(teams.c.id == team_id)
    team = await database.fetch_one(query)
    if team is None:
        raise HTTPException(status_code=404, detail="Team not found")
    team = {k: v for k, v in team.items()}

    query = users.select().where(associations.c.team_id == team_id).join(
        associations, associations.c.user_id == users.c.id
    )
    user_list = await database.fetch_all(query)
    user_list = [{
        "id": user.get("id"),
        "email": user.get("email"),
        "name": user.get("name"),
        "last_name": user.get("last_name"),
        "birthdate": user.get("birthdate"),
        "phone": user.get("phone")
    } for user in user_list]

    return {**team, "users": user_list}


@app.patch("/associations/{association_id}",
           response_model=RetrieveUpdatedAssociation,
           response_model_exclude_none=True)
async def association_update(association_id: int,
                             association: UpdateAssociation):
    query = associations.update().values(
        **association.dict(exclude_unset=True)
    ).where(associations.c.id == association_id)

    await database.execute(query)
    return {**association.dict(), "id": association_id}


@app.delete("/associations/{association_id}")
async def association_delete(association_id: int):
    query = associations.delete().where(associations.c.id == association_id)
    await database.execute(query)
    return {"deleted": association_id}
