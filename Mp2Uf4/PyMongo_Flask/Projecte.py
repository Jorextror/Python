import requests
# ---- para guardarlo en un arxivo csv ----
import csv
from bs4 import BeautifulSoup

# un get de la pagina
# page = requests.get('https://www.ebay.es/b/Ordenadores-de-sobremesa/171957/bn_16553696/')#Ordenadores de sobremesa
page = requests.get('https://betterandbest.es/400-sillas-butacas-y-sofas/')

# trasforma en html
soup = BeautifulSoup(page.text, 'html.parser')

# ---- para guardarlo en un arxivo csv ----
# f = csv.writer(open('frases.csv', 'w'))
# f.writerow(['Autor', 'Categoria', 'Frase'])

# lo hacemos en una array diviendolo por la etiqueta
# blockquote_items = soup.find_all(class_='s-item s-item--large s-item--bgcolored')
blockquote_items = soup.find_all(class_='product-miniature')
# recoremos la array
# print(blockquote_items)
for blockquote in blockquote_items:
    # title = blockquote.find(class_='s-item__title').text
    price = blockquote.find(class_='h3 product-title').text
    img = blockquote.find(class_='thumbnail-img')["src"]

    print([price, img])

    #return([title,price,img])#array dicc
    # ---- para guardarlo en un arxivo csv ----