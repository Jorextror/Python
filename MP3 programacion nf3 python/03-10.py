"""Escriviu un programa que comprova si dues llistes tenen elements en comú.
Per exemple: llista1 = [1,2,3,4,5,6,7], llista2 = [4,1,20,100]
imprimeix per pantalla “Tenen 2 elements en comú i són: 1,4”
Jordi Oliveda
"""
"""llistes"""
ll1 = [1,2,3,4,5,6,7]
ll2 = [4,1,20,100]
ll = []

"""va miran els elements de llista1 i mira la llista2 si esta i si esta la posa
en un altre llista nova"""
for i in range(len(ll1)):
    if ll1[i] in ll2:
        ll.append(ll1[i])
print("Tenen",len(ll),"elemnts en comú i són:",ll)