"""Jordi Oliveda
(1 punt) Demana una cadena per teclat  i genera  un diccionari amb la quantitat aparicions de cada caràcter en la cadena.
"""
teclat=input("introdueix una cadena: ")
dic={el:teclat.count(el) for el in set(teclat)}
print(dic)