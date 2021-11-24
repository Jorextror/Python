from pymongo import MongoClient, collection

client=MongoClient()
#llista de objectos
mylist=[{"nom":"pepe","equip":1},{"nom":"jony","equip":2}]

with MongoClient('localhost',27017,username='Jordi',password='Admin@123',authSource='JordiOlivedaBD') as client:
    print("Conectado a MongoDB") #Connectar con el servidor de MongoDB
    db= client.JordiOlivedaBD #database
    col=db["tasca4"] #crear collection

    #añadimos los registros a la collecion
    x = col.insert_many(mylist)
    # col.delete_many({})#eliminar

    #leemos los documentos de la BD
    print("----4----")
    for x in col.find():
        print(x)

    #update
    myquery={"nom":"jony"}
    newvalues={"$set":{"nom":"jose"}}
    col.update_one(myquery, newvalues)

    #mostrem al anterior update que he fet
    print("----8----")
    for x in col.find({},{"nom":"jose"}):
        print(x)

    #borrem un objecte
    col.delete_one({"nom":"pepe"})

    #connecion cerrada(abriendo una connecion con with no hace falta cerrar la connecion, lo cierra solo es mas seguro)
    MongoClient.close()