from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from models import Person, Phone, Base
from time import sleep
url = open('/home/apoorv/.elephant/url').read()
engine = create_engine(url)

Session = sessionmaker(bind=engine)
session = Session()

Base.metadata.create_all(engine)

p1 = Person(
    id=1,
    name="Apoorv",
    age=26,
    phones=[ Phone(ptype='home', number=123), Phone(ptype='office', number=234)])


p2 = Person(
    id=2,
    name="Billy",
    age=26,
    phones=[Phone(ptype='home', number=444), Phone(ptype='office', number=555)])

session.add_all([p1, p2])
session.commit()

session = Session()
persons = session.query(Person).filter(Person.id.in_([1,2]))
# inefficient row by row delete (but doesn't need db level cascade)
for person in persons:
    session.delete(person)

p1 = Person(
    id=1,
    name="ApoorvN",
    age=26,
    phones=[ Phone(ptype='home', number=123), Phone(ptype='office', number=234)])


p2 = Person(
    id=2,
    name="BillyN",
    age=26,
    phones=[Phone(ptype='home', number=445), Phone(ptype='office', number=556)])

session.add_all([p1, p2])

session.commit()