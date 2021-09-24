"""Jordi Oliveda
Programa l’algorisme d’ordenació de la bombolla. Prova’l amb L1 i L2.
"""

L1 = [10, 8, 6, 4, 2, 1, 3, 5, 7, 9]
L2 = [12, 1, 12, 1, 8, 5, 1, 3]
L3 = [1, 3, 6, 8, 9, 12, 13, 15, 16, 17]

A=L1
"""
A=L2"""

n=len(A)
valid = True
while valid != False: #mentres el valor logic no canvia no surtira del bucle
    for i in range(1,n):
        if A[i-1]>A[i]:#si és més gran la posicio anterior i la actual és mes petit el valor entra
            C=A[i] #comenza el remplaz de sempre, una variable guarda el valor despus la altra variable es posa a la a, despres la variable creada de abans en la b.
            A[i]=A[i-1]
            A[i-1]=C
            valid = True
            print(A)
        i=1#reiniciar el valor per el bucle perque torni a poder fer
    n-=1#canviar el valor del rang del bucle for per posicio que estiguem.