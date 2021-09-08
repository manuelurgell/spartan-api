from sqlalchemy import (
    Column,
    Date,
    DateTime,
    ForeignKey,
    Integer,
    String,
    Table
)
from sqlalchemy.sql import func

from db import metadata

teams = Table(
    'team',
    metadata,
    Column("id", Integer, primary_key=True, index=True),
    Column("name", String(250), nullable=False, unique=True),
    Column("created_at", DateTime(timezone=True), server_default=func.now()),
    Column("last_modified", DateTime(timezone=True), onupdate=func.now())
)

users = Table(
    'user',
    metadata,
    Column("id", Integer, primary_key=True, index=True),
    Column("team_id", Integer, ForeignKey(
        "team.id", ondelete='CASCADE'
    ), nullable=False),
    Column("email", String(250), nullable=False, unique=True),
    # password
    Column("name", String(250), nullable=False),
    Column("last_name", String(250), nullable=False),
    Column("birthdate", Date, nullable=False),
    Column("phone", Integer),
    Column("created_at", DateTime(timezone=True), server_default=func.now()),
    Column("last_modified", DateTime(timezone=True), onupdate=func.now())
    # last_login
)
