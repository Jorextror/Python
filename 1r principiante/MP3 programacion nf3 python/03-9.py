"""Escriviu un programa per imprimir els números
d'una llista especificada per teclat i després
d'eliminar-ne els números parells.
Jordi Oliveda
"""

"""la mida per el bucle per annar omplir la llista"""
mida= int(input("Llargada de la llista: "))
"""llista buida"""
llu=[]
"""els valors introduits els afexim en una llista"""
for i in range(mida):
    ll=int(input("Introdueix números: "))
    llu.append(ll)
print("la llista introduida",llu)

"""treiem els numeros parells"""
for i in range(mida):
    if llu[i] %2 == 0:
        llu.remove(llu[i])
print("la llista sense els parells:",llu)