from flask import Flask,render_template,redirect
from pymongo import MongoClient, collection
import requests

app = Flask(__name__)
@app.route('/')
# @app.route('/<name>')
def hello(name=None):
	client=MongoClient()
	with MongoClient('localhost',27017,username='Jordi',password='Admin@123',authSource='JordiOlivedaBD') as client:
		print("Conectado a MongoDB") #Connectar con el servidor de MongoDB
		db= client.JordiOlivedaBD #database
		col=db["Usuaris"] #crear collection
		return render_template('index.html',lista=col.find())

@app.route('/index.html', methods=['GET', 'POST'])
def validarLogin():
	user=requests.post(user)

@app.route('/registrar')
def registrar():
	return render_template('registrar.html')