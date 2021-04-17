"""Jordi Oliveda
Programa l’algorisme d’ordenació per inserció. Prova’l amb L1 i L2.
"""
"""llistes"""
L1 = [10, 8, 6, 4, 2, 1, 3, 5, 7, 9]
L2 = [12, 1, 12, 1, 8, 5, 1, 3]
L3 = [1, 3, 6, 8, 9, 12, 13, 15, 16, 17]
"""variable per canviar de llista"""
"""
A=L1
"""
A=L2

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