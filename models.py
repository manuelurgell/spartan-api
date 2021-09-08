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
from sqlalchemy.sql.schema import UniqueConstraint

from db import metadata

associations = Table(
    'association',
    metadata,
    Column("id", Integer, primary_key=True, index=True),
    Column('team_id', ForeignKey('team.id'), nullable=False),
    Column('user_id', ForeignKey('user.id'), nullable=False),
    UniqueConstraint('team_id', 'user_id')
)

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
    Column("email", String(250), nullable=False, unique=True),
    # password
    Column("name", String(250), nullable=False),
    Column("last_name", String(250), nullable=False),
    Column("birthdate", Date, nullable=False),
    Column("phone", String(10)),
    Column("created_at", DateTime(timezone=True), server_default=func.now()),
    Column("last_modified", DateTime(timezone=True), onupdate=func.now())
    # last_login
)
