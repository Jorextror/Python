"""Jordi Oliveda
Fes un programa que suma un valor introduït per
teclat a tots els elements de la llista [1,2,3,4,5,6,7,8,9,10]
utilitzant un bucle for, cal modificar la llista original.
"""
"""llista"""
llista = [1,2,3,4,5,6,7,8,9,10]
"""introduxio per teclat"""
teclat = int(input("Intrdueix un número: "))
"""un bucle per annar suman cada elemnt de la llista"""
for i in range(len(llista)):
    llista[i]+=teclat
    

print("la suma és",llista)