from sqlalchemy import Column, DateTime, ForeignKey, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy.sql import func

Base = declarative_base()


class Team(Base):
    __tablename__ = 'team'
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(250), nullable=False)
    created_at = Column(DateTime(timezone=True), server_default=func.now())
    last_modified = Column(DateTime(timezone=True), onupdate=func.now())


class User(Base):
    __tablename__ = 'user'
    id = Column(Integer, primary_key=True, index=True)
    team_id = Column(Integer, ForeignKey('team.id'), nullable=False)
    team = relationship('Team', backref='users')
    email = Column(String(250), nullable=False, unique=True)
    # password
    name = Column(String(250), nullable=False)
    last_name = Column(String(250), nullable=False)
    birthdate = Column(DateTime(timezone=True), nullable=False)
    phone = Column(String(250))
    created_at = Column(DateTime(timezone=True), server_default=func.now())
    last_modified = Column(DateTime(timezone=True), onupdate=func.now())
    # last_login
