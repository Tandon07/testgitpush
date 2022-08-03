import pymongo



client = pymongo.MongoClient("mongodb+srv://Tandon78:Hellodude123@tandon.el8wcqy.mongodb.net/?retryWrites=true&w=majority")
db = client.test
print(db)

d={ "name":"sudhanshu","email":"sudh@gmail.com","surname":"kumar"} #IMPORTANT it should be dictionary only

db1=client['mongotest']
coll=db1['test']
coll.insert_one(d)


