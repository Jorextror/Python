"""Jordi Oliveda
Programa l’algorisme d’ordenació per nan. Prova’l amb L1 i L2.
"""
L1 = [10, 8, 6, 4, 2, 1, 3, 5, 7, 9]
L2 = [12, 1, 12, 1, 8, 5, 1, 3]
L3 = [1, 3, 6, 8, 9, 12, 13, 15, 16, 17]

A=L1
"""
A=L2
"""
pos=0
while pos < len(A):#si la constant pos no és més gran de la longitut de la llista entra en el bucle
    if (pos == 0 or A[pos] >= A[pos-1]):#si pos és igual a "0" o la posicio que tingui el num en "pos" ensenya aquella linea sigui
        pos+=1
    else: #si no és res de lo anterior pues es remplazara
        C=A[pos] #guardem el valor en una variable
        A[pos]=A[pos-1] #posem el valor B al A
        A[pos-1]=C # i en la possicio B li posem la variable que era el valor de la posicio A
        pos-=1 
        print(A)