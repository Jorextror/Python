"""Jordi Oliveda
Escriviu un programa que mostri per pantalla el resultat
de sumar i el resultat de multiplicar tots els elements d'una llista.
Cal introduir la llista per teclat.
Ajuda: feu servir un bucle per afegir elements a la llista.
"""
vegades = int(input("vegades de introduxio un número: "))
"""llista buida"""
ll=[]
"""constants"""
suma=0
multi=1
"""bucle per annar demanan els numeros i afexir-li en una llista"""
for i in range(vegades):
    num = int(input("Número que vols que sumi i multipliqui entre els altres numeros: "))
    ll.append(num)
"""bucle per annar suman i multiplicar a tots de la llista"""
for j in range(len(ll)):
    suma = suma+ll[j]
    multi = multi*ll[j]
print("la suma:",suma,"la multiplicacio",multi)
