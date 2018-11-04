from pymongo import MongoClient
from matplotlib import pyplot
from collections import Counter #https://www.geeksforgeeks.org/counters-in-python-set-2-accessing-counters/


uri = "mongodb://admin:admin@ds021182.mlab.com:21182/c4e"

client = MongoClient(uri)

db=client.get_database()

customers=db["customers"]
customers_list=customers.find()

ads = 0
events =0
wom = 0

for i in customers_list :
    if i["ref"] =="ads":
        ads +=1
    elif i["ref"] == "events":
        events +=1
    elif i["ref"] == "wom" :
        wom += 1
print("count ads: " ,ads)
print("count events :", events)
print("count wom :", wom)

machine_count = [ads,events,wom]  

machine_name = ["ads","events","wom"]

pyplot.pie(machine_count, labels=machine_name,autopct="%.2f%%",shadow=True,explode=[0,0.08,0.1])
pyplot.title("Percentage of each reference")
pyplot.axis("equal")

pyplot.show()



