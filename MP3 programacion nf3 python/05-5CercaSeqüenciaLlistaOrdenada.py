"""Jordi Oliveda
Programa l’algorisme de cerca seqüencial amb llista ordenada. Prova’l amb L3.
"""

L1 = [10, 8, 6, 4, 2, 1, 3, 5, 7, 9]
L2 = [12, 1, 12, 1, 8, 5, 1, 3]
L3 = [1, 3, 6, 8, 9, 12, 13, 15, 16, 17]

A=L3

e=int(input("que vols cerca? "))

i=0
while (e > A[i]) and (i < len(A)):#si el valor que volem buscar és més petit de la longitut de la llista i la posicio és més grand que la longitut surtira del bucle
    i+=1 #aumenta la posicio per buscar
if (e != A[i] or (i == len(A))): #si el valor que volem és diferent el valor actual o el index es igual a la longitut el resultaat és que no s'ha trobat
    print("no trobat")
else: #si no el elemnt que cerquem s'ha trobat
    print("trobat a la posició",i+1)