from flask import Flask,render_template
from pymongo import MongoClient, collection

app = Flask(__name__)
@app.route('/')
@app.route('/<name>')
def hello(name=None):
	client=MongoClient()
	with MongoClient('localhost',27017,username='Jordi',password='Admin@123',authSource='JordiOlivedaBD') as client:
		print("Conectado a MongoDB") #Connectar con el servidor de MongoDB
		db= client.JordiOlivedaBD #database
		col=db["tasca4"] #crear collection
		return render_template('hola.html',lista=col.find())