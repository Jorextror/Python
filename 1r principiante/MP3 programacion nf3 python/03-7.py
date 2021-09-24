"""Escriviu un programa per eliminar duplicats d'una llista.
Bucle i funció integrada de python.

Per exemple: llista = [1,2,3,1,3,1,4,2], sortida = [1,2,3,4]
Jordi Oliveda
"""
"""llistes"""
ll=[1,2,3,1,3,1,4,2]
llu=[]

"""affexim elements que no tingui la llista amb (not in) de la altre llista"""
for el in ll:
    if el not in llu: 
        llu+=[el]
print(llu)