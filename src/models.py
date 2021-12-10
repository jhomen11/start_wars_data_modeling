import os
import sys
from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy import create_engine
from eralchemy import render_er

Base = declarative_base()

class User(Base):
    __tablename__ = 'user'
    id = Column(Integer, primary_key=True)
    name = Column(String(250), nullable=False)
    email = Column(String(250), nullable=False)
    password = Column(String(250), nullable=False)

class People(Base):
    __tablename__ = 'people'
    uid = Column(Integer, primary_key=True)
    name = Column(String(250), nullable=False)
    gender = Column(String(250), nullable=False)
    height = Column(String(250), nullable=False)
    eye_color = Column(String(250), nullable=False)
    
class Planets(Base):
    __tablename__ = 'planets'
    uid = Column(Integer, primary_key=True)
    name = Column(String(250), nullable=False)
    terrain = Column(String(250), nullable=False)
    climate = Column(String(250), nullable=False)

class Starships(Base):
    __tablename__ = 'starships'
    uid = Column(Integer, primary_key=True)
    model = Column(String(250), nullable=False)
    starship_class = Column(String(250), nullable=False)
    passengers = Column(Integer, nullable=False)

class FavoriteList(Base):
    __tablename__ = 'favoriteList'
    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey('user.id'))
    people_id = Column(Integer, ForeignKey('people.uid'))
    planets_id = Column(Integer, ForeignKey('planets.uid'))
    starships_id = Column(Integer, ForeignKey('starships.uid'))
    people = relationship(People)
    planets = relationship(Planets)
    starships = relationship(Starships)
    user = relationship(User)

    def to_dict(self):
        return {}

## Draw from SQLAlchemy base
render_er(Base, 'diagram.png')