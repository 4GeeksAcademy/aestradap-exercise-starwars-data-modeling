
import os
import sys
from sqlalchemy import Column, ForeignKey, Integer, String, Boolean, Enum, ARRAY, Table
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
    favorites = relationship('Favorite', uselist=True, backref='favorites')
    # user_to_id = Column(ARRAY, ForeignKey('favorite.id'))
    
favorite_character_association = Table(
    'favorite_character',
    Base.metadata,
    Column('favorite_id', Integer, ForeignKey('favorite.id')),
    Column('character_id', Integer, ForeignKey('character.id'))
)

favorite_planet_association = Table(
    'planet_character',
    Base.metadata,
    Column('favorite_id', Integer, ForeignKey('favorite.id')),
    Column('planet_id', Integer, ForeignKey('planet.id'))
)

class Favorite(Base):
    __tablename__ = 'favorite'
    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey('user.id'))
    planets = relationship('Planet', secondary=favorite_planet_association, back_populates='favorites')
    characters = relationship('Character', secondary=favorite_character_association, back_populates='favorites')
    
class Character(Base):
    __tablename__ = 'character'
    id = Column(Integer, primary_key=True)
    character_name = Column(String(20), unique=False)
    favorites = relationship('Favorite', secondary=favorite_character_association, back_populates='characters')

class Planet(Base):
    __tablename__ = 'planet'
    id = Column(Integer, primary_key=True)
    planet_name = Column(String(20), unique=False)
    favorites = relationship('Favorite', secondary=favorite_planet_association, back_populates='planets')



   
    
#     article_author_association = Table(
#     'article_author',
#     Base.metadata,
#     Column('article_id', Integer, ForeignKey('articles.id')),
#     Column('author_id', Integer, ForeignKey('users.id'))
# )

# class User(Base):
#     __tablename__ = 'users'
#     id = Column(Integer, primary_key=True)
#     name = Column(String)
#     articles = relationship('Article', secondary=article_author_association, back_populates='authors')

# class Article(Base):
#     __tablename__ = 'articles'
#     id = Column(Integer, primary_key=True)
#     title = Column(String)
#     authors = relationship('User', secondary=article_author_association, back_populates='articles')
 
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


