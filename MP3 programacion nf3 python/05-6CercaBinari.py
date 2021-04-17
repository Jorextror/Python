"""Jordi Oliveda
Programa l’algorisme de cerca binària. Prova’l amb L3 i un valor entrat per teclat.
"""

L1 = [10, 8, 6, 4, 2, 1, 3, 5, 7, 9]
L2 = [12, 1, 12, 1, 8, 5, 1, 3]
L3 = [1, 3, 6, 8, 9, 12, 13, 15, 16, 17]

A=L3

e=int(input("Que vols trobar? "))

trobat=False
inf=0
sup=len(A)
while (inf <= sup) and trobat == False:#si el valor inf és més petit que la longitut de la llista i no s'ha trobat continua el bucle
    mig=(sup-inf)//2+inf
    if e == A[mig]: #si element és igual el valor canvia trobat a True i s'ha acabara el bucle
        trobat=True
    else:
        if e < A[mig]:#si elemnt és més petit que el valor resta 1 a la mig i si no el suma
            sup = mig-1
        else:
            inf = mig+1
if trobat == False: #si trobat es false no la trobat i si no la trobat en la posicio x
    print("no trobat")
else:
    print("trobat a",inf)