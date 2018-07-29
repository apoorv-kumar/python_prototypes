from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship

Base = declarative_base()

'''
cascade='all' is handled at ORM level
ondelete='CASCADE' is handled at DB level
'''

class Phone(Base):
    __tablename__ = 'phone'
    ptype = Column(String, primary_key=True)
    number = Column(String, primary_key=True)
    # ON DELETE CASCADE - to make sure phones are deleted for a person.
    person_id = Column(Integer, ForeignKey('person.id', ondelete='CASCADE'), primary_key=True)

class Person(Base):
    __tablename__ = 'person'
    id = Column(Integer, primary_key=True)
    age = Column(Integer)
    name = Column(String)
    # cascade
    phones = relationship("Phone", cascade="all, delete-orphan")

