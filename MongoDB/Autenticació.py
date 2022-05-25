from pymongo import MongoClient, collection

client=MongoClient()

with MongoClient('localhost',27017) as client:
    print("Conectado a MongoDB") #Connectar con el servidor de MongoDB
    db= client.JordiOlivedaBD #database