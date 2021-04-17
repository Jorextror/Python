"""Escriviu un programa que elimina l’element n-èssim
d’una llista introduïda per teclat.

Llista de mostres: ['Vermell', 'Verd', 'Blanc', 'Negre', 'Rosa', 'Groc']
Element = 0
Sortida ['Verd', 'Blanc', 'Negre', 'Rosa', 'Groc']
Jordi Oliveda
"""

"""llista"""
ll=['Vermell', 'Verd', 'Blanc', 'Negre', 'Rosa', 'Groc']
print(ll)

r=int(input("Introdueix un num que quieres borrar(0/6) "))
"""r és un numero instem la posisio de la llista a la posicio i la borrem"""
ll.remove(ll[r])

print(ll)