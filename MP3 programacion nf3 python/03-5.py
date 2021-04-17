"""Escriviu un programa per obtenir el nombre més gran,
més petit i la mitjana d'una llista de sencers.
Cal introduir la llista per teclat. Fer versió bucle i versió mètodes.
Jordi Oliveda
"""
"""constat i llista buida"""
ll=[]
suma=0
"""la mida per el bucle de introduir una llista"""
mida= int(input("Llargada de la llista: "))

"""bucle per afexir els valors en una llista i annar suman"""
for i in range(mida):
    el=int(input("Introdueix un número: "))
    suma += el
    ll.append(el)
"""constants del priemr valor de la llista introduida abans"""
mi=ll[0]
ma=ll[0]

"""sortida de max,min,mitja amb metodes de python"""
print("mètodes: max:",max(ll),"min:",min(ll),"mitjana:",int(sum(ll)/mida))

"""bucle per calcular manualment el max,min,mitjana"""
for i in range(len(ll)):
    if ll[i] > ma:
        ma=ll[i]
    elif ll[i] < mi:
        mi=ll[i]
print("bucle: max:",mi,"min:",ma,"mitjana:",int(suma/mida))