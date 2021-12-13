from pymongo import MongoClient, collection
from flask import Flask, url_for, request, redirect
# Instancia de Flask. Aplicación
app = Flask(__name__)

@app.route('/<name>')
def success(name):
   return 'welcome %s' % name

@app.route('/login',methods = 'POST')
def login():
   if request.method == 'POST':
      user = request.form['nm']
      passs= request.form['contraseña']

      client=MongoClient()
      #### Conectar con DB
      with MongoClient('localhost',27017,username='Jordi',password='Admin@123',authSource='JordiOlivedaBD') as client:
          print("Conectado a MongoDB") #Connectar con el servidor de MongoDB
          db= client.JordiOlivedaBD #database
          col=db["usuari"] #crear collection usuari o seleccionem

          for x in col.find():
              if x == ("usuari": user, "pass": passs):
                  return redirect(url_for(name = "ok"))
          #connecion cerrada(abriendo una connecion con with no hace falta cerrar la connecion, lo cierra solo es mas seguro)    
      return redirect(url_for(name = "error"))
#### PROGRAMA PRINCIPAL
if __name__ == '__main__':
 # Iniciamos la apicación en modo debug
 app.run(debug=True)