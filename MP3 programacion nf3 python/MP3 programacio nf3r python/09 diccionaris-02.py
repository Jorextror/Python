"""
Demana una cadena per teclat  i genera  un diccionari amb la quantitat aparicions de cada caràcter en la cadena.
"""

cadena = input("Introdueix una cadena:")

ex2 = {c:cadena.count(c) for c in set(cadena)}
print(ex2)
