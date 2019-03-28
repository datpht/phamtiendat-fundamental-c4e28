from pymongo import MongoClient
from matplotlib import pyplot

mongo_uri = "mongodb://admin:admin@ds021182.mlab.com:21182/c4e"

client = MongoClient(mongo_uri)

db = client.c4e

markerting_collection = db['customers']

all_customers = markerting_collection.find()

ref = []
for customer in all_customers:
    ref.append(customer['ref'])

event_customers = ref.count('events')
ads_customers = ref.count('ads')
wom_customers = ref.count('wom')

print("The number of events customers is: ",event_customers)
print("The number of ads customers is: ",ads_customers)
print("The number of wom customers is: ",wom_customers)    

customers_count = [event_customers,ads_customers,wom_customers]
customers_name = ['events','advertisement','word of mouth']

pyplot.pie(customers_count, labels=customers_name,autopct='%.1f%%')
pyplot.title("Percentage of 3 reference")
pyplot.axis("equal")

pyplot.show()
