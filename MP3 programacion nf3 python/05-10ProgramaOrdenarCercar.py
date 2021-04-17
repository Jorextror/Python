"""Jordi Oliveda
Fes un programa nou de la manera següent: 
    -agafa un programa d’ordenació dels que has fet (1 a 3), 
    -ordena L1 i 
    -fes-lo servir com a entrada del programa de cerca binària.
"""
#Ordenar
L1 = [10, 8, 6, 4, 2, 1, 3, 5, 7, 9]
L2 = [12, 1, 12, 1, 8, 5, 1, 3]
L3 = [1, 3, 6, 8, 9, 12, 13, 15, 16, 17]
"""variable per canviar de llista"""
A=L1

"""contador"""
i=1
"""bucle que no sha acaba fins que variable "i" sigue mes gran de la llargada de la llista"""
while i < len(A):
    x=A[i] #guardem valor en X
    j=i-1
    while j >= 0 and A[j] > x: #si el valor de la x és més grand que el altre
        A[j+1]=A[j]
        j=j-1
    A[j+1]=x # posem el valor una pocisio menys
    i+=1
    print(A)

#Cerca binari

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
    print("trobat a pocisio",inf+1)