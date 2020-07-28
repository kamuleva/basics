import pymongo
from bson.objectid import ObjectId
my_mongo_client=pymongo.MongoClient("mongodb://localhost:27017/")
my_database=my_mongo_client["practice"]
mycollection=my_database["arr_update"]
my_document=[{"id":10,"name":"user","subjects_learning":[{"lan":"python"},{"lan":"mongodb"},{"lan":"electronis"}]}]
#my_inserted_data=mycollection.insert_many(my_document)
# my_appender=[]
# for i in range(1,26):
#     my_appender.append([{"name":"user"+str(i),"no.of users":i,"subjects_learning":[{"name":"python"},{"name":"mongodb"},{"name":"electronics"}]}])
# print(my_appender)
# myname={"name":"kitna"}
# myinsert=mycollection.insert_one(myname)
# mynamechange={"$set":{"name":"krishna"}}
# myupdater=mycollection.update_one(myname,mynamechange)
myupdate=mycollection.update_one({"_id" : ObjectId("5f200ad4514fad9b63bae43e"),"subjects_learning.lan":"python"},{"$set":{"subjects_learning.$.lan":"ML"}})
