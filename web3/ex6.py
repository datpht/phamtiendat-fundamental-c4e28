from pymongo import MongoClient

mongo_uri = "mongodb://admin:admin@ds021182.mlab.com:21182/c4e"

client = MongoClient(mongo_uri)

db = client.c4e

rivers = db['river']

sAmerica_rivers = rivers.find({"continent":"S. America"})
for sar in sAmerica_rivers:
    if sar['length'] < 1000 :
        print(sar)
    else:
        continue
