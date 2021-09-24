""" Jordi Oliveda
Programa l’algorisme de cerca seqüencial. Prova’l amb L1 i L2.
"""

L1 = [10, 8, 6, 4, 2, 1, 3, 5, 7, 9]
L2 = [12, 1, 12, 1, 8, 5, 1, 3]
L3 = [1, 3, 6, 8, 9, 12, 13, 15, 16, 17]

A=L2 #constant

e=int(input("que vols cerca? ")) #variables
i=0
while (i < len(A)) and (e != A[i]): #bucle de que si i és més petit que la llargada de la llsita i si no és el mateix element el que busquem
    i+=1#més un fins que ja no cumpleixi la llargada de la llista o que es trobi
if i == len(A):
    print("no trobat")
else:
    print("trobat a la posició",i+1)