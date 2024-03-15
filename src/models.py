
import os
import sys
from sqlalchemy import Column, ForeignKey, Integer, String, Boolean, Enum, ARRAY
from sqlalchemy.orm import relationship, declarative_base
from sqlalchemy import create_engine
from eralchemy2 import render_er

Base = declarative_base()

class User(Base):
    __tablename__ = 'user'
    id = Column(Integer, primary_key=True)
    user_name = Column(String(20), unique=False)
    first_name = Column(String(20), unique=False)
    last_name = Column(String(20), unique=False)
    email = Column(String(100), unique=True)
    user_to_id = Column(ARRAY, ForeignKey('favorite.id'))
    
class Favorite(Base):
    __tablename__ = 'favorites'
    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey('user.id'))
    planet_id = Column(Integer, ForeignKey('planet.id'))
    character_id = Column(Integer, ForeignKey('character.id'))

class Planet(Base):
    __tablename__ = 'planet'
    id = Column(Integer, primary_key=True)
    planet_name = Column(String(20), unique=False)
    favorite_id = Column(Integer, ForeignKey('favorite.id'))

class character(Base):
    __tablename__ = 'character'
    id = Column(Integer, primary_key=True)
    character_name = Column(String(20), unique=False)
    favorite_id = Column(Integer, ForeignKey('favorite.id'))
    


 
    def to_dict(self):
        return {}

## Draw from SQLAlchemy base
try:
    result = render_er(Base, 'diagram.png')
    print("Success! Check the diagram.png file")
except Exception as e:
    print("There was a problem genering the diagram")
    raise e

# class Person(Base):
#     __tablename__ = 'person'
#     # Here we define columns for the table person
#     # Notice that each column is also a normal Python instance attribute.
#     id = Column(Integer, primary_key=True)
#     name = Column(String(250), nullable=False)

# class Address(Base):
#     __tablename__ = 'address'
#     # Here we define columns for the table address.
#     # Notice that each column is also a normal Python instance attribute.
#     id = Column(Integer, primary_key=True)
#     street_name = Column(String(250))
#     street_number = Column(String(250))
#     post_code = Column(String(250), nullable=False)
#     person_id = Column(Integer, ForeignKey('person.id'))
#     person = relationship(Person)


