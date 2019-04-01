from pymongo import MongoClient


mongo_uri = "mongodb+srv://admin:admin@c4e28-ido4u.mongodb.net/test?retryWrites=true"

#1 . connect to cluster
client = MongoClient(mongo_uri)

#2. create database
service_database = client.db_service

#3. create collection
bike_rental = service_database['bike_rental']