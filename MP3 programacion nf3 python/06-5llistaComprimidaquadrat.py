"""Jordi Oliveda
Mitjançant la comprensió de la llista,
construïu una llista a partir dels quadrats de cada element de la llista,
si el quadrat és superior a 50.
llista=[1,2,3,7,9,10]
"""

llista = [i**2 for i in range(1,7) if i < 50]
print(llista)