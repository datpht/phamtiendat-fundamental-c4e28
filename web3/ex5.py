from pymongo import MongoClient

mongo_uri = "mongodb://admin:admin@ds021182.mlab.com:21182/c4e"

client = MongoClient(mongo_uri)

db = client.c4e

rivers = db['river']

africa_rivers = rivers.find({"continent":"Africa"})
for ar in africa_rivers:
    print(ar)
