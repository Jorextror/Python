"""Jordi Oliveda
Exercicis Arguments-Línia de Comanades

Fes un programa en Python anomenat ex1.py que accepta 1 argument
per la línia de comandes i si està format per lletres mostra per
pantalla quantes vocals té.
"""
c=0
vocal="aeiouAEIOU"
teclat=input("Introdueix cadena: ")
for el in range(len(teclat)):
    if teclat[el] in vocal:
        c+=1
print("El strinc té ",c," vocals")