from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from models import Person, Phone, Base
from time import sleep
url = open('/home/apoorv/.elephant/url').read()
engine = create_engine(url)

Session = sessionmaker(bind=engine)
session = Session()

# Base.metadata.create_all(engine)
# print("done with createall")
session.query(Person).delete(synchronize_session=False)  # cascades
print("deleted initial contents.")
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

p3 = Person(
    id=3,
    name="John",
    age=26,
    phones=[Phone(ptype='home', number=888), Phone(ptype='office', number=889)])


session.add_all([p1, p2, p3])
session.commit()
print("reinstantiated values")
# -------- BASE STATE ---------


session = Session()
print("updating new values")
session.query(Person).filter(Person.id.in_([p1.id, p2.id])).delete(synchronize_session=False)
p1 = Person(
    id=1,
    name="ApoorvN",
    age=26,
    phones=[ Phone(ptype='home', number=124), Phone(ptype='office', number=235)])


p2 = Person(
    id=2,
    name="BillyN",
    age=26,
    phones=[Phone(ptype='home', number=445), Phone(ptype='office', number=556)])

session.add_all([p1, p2])

session.commit()
print("updated")