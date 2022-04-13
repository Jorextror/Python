from flask import Flask,render_template,redirect,request
import pymongo
from pymongo import MongoClient, collection

#scraps
import requests
from bs4 import BeautifulSoup

#db
clien = pymongo.MongoClient('mongodb://localhost:27017/')
db= clien["JordiOlivedaBD"] #database
col=db["Usuaris"] #crear collection
dades= db["dades"]

#flask
app = Flask(__name__)

@app.route('/')
def inci():
   return render_template('index.html')

@app.route('/login', methods=['GET', 'POST'])
def login():
   if request.method == 'POST':
      username = request.form['user']
      pasw = request.form['pass']
      try:
         for user in col.find({"user": username}):
            if user['user'] == username and user['password'] == pasw:
               return redirect('/base')
            else:
               return redirect('/')
      except:
         return redirect('/')

@app.route('/registrar')
def registrar():
	return render_template('registrar.html')

@app.route('/registrarV',methods = ['POST', 'GET'])  
def registrarV():
    if request.method == 'POST':
       username = request.form['user']
       pasw = request.form['pass']
       pasw2 = request.form['pass2']
       for user in col.find():
          if user['user'] != username and pasw == pasw2:
             col.insert({"user": username, "password": pasw, "veces": +1})
             return redirect('/')
          else:
             return redirect('/registrar')

@app.route('/base')
def main():
    return render_template('base.html')

@app.route('/scrap', methods = ['POST', 'GET'])
def aprenentatge():
	url = request.form['url']
	url = "https://betterandbest.es/400-sillas-butacas-y-sofas/"
	page = requests.get(url)
	soup = BeautifulSoup(page.text, 'html.parser')
	blockquote_items = soup.find_all(class_='product-miniature')

	for blockquote in blockquote_items:
		# title = blockquote.find(class_='s-item__title').text
		price = blockquote.find(class_='h3 product-title').text
		img = blockquote.find(class_='thumbnail-img')["src"]
		dades.insert({'price': price, 'img' : img})
	return redirect('/base')

@app.route('/aprenentatge')
def aprenentatges():
   dades.delete_many({})
   return render_template('/aprenentatge.html')

@app.route('/consultes')
def consultes():
   consulta = dades.find()
   return render_template('consultes.html', consulta=consulta)

@app.route('/reset')
def reset():
   dades.delete_many({})
   return redirect('/base')