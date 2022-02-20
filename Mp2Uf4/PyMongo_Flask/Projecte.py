import requests
# ---- para guardarlo en un arxivo csv ----
# import csv
from bs4 import BeautifulSoup

def extrac():
    # un get de la pagina
    page = requests.get('https://www.ebay.es/b/Ordenadores-de-sobremesa/171957/bn_16553696')#Ordenadores de sobremesa

    # trasforma en html
    soup = BeautifulSoup(page.text, 'html.parser')

    # ---- para guardarlo en un arxivo csv ----
    # f = csv.writer(open('frases.csv', 'w'))
    # f.writerow(['Autor', 'Categoria', 'Frase'])

    # lo hacemos en una array diviendolo por la etiqueta
    blockquote_items = soup.find_all(class_='s-item s-item--large s-item--bgcolored')
    # recoremos la array
    # print(blockquote_items)
    for blockquote in blockquote_items:
        title = blockquote.find(class_='s-item__title').text
        price = blockquote.find(class_='s-item__price').text
        img = blockquote.find(class_='s-item__image-img').text
        return([title,price,img])#array dicc
        # ---- para guardarlo en un arxivo csv ----
        # f.writerow([autor, categoria])
