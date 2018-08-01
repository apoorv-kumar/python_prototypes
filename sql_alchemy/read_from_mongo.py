from pymongo import MongoClient

url = open('/home/apoorv/.mlab/url').read()
#mongodb://<u>:<p>@<srv>:<prt>/?authSource=<db>&authMechanism=SCRAM-SHA-1
client = MongoClient(url)
db = client.get_database('arktest')
persons = db.get_collection('persons')
import json
# d = json.load(open('sample.json', 'r'))
#
# persons.insert_one(d)

print(list(persons.find()))