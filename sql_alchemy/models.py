from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship

Base = declarative_base()

class Phone(Base):
    __tablename__ = 'phone'
    ptype = Column(String, primary_key=True)
    number = Column(String, primary_key=True)
    person_id = Column(Integer, ForeignKey('person.id'), primary_key=True)

class Person(Base):
    __tablename__ = 'person'
    id = Column(Integer, primary_key=True)
    age = Column(Integer)
    name = Column(String)
    phones = relationship("Phone", cascade="all, delete-orphan")

