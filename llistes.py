"""Jordi Oliveda
"""
import random
def omple_llista(w,lon,mi,ma):
    ll=[random.randrange(mi,ma) for i in range(lon)]
    return ll

def demana_llista(a):
    ll=[int(input("introdueix un caracter per la llista: ")) for i in range(a)]
    return(ll)

def imprimeix_llista(a):
    print(a)

def ordena_llista(a):
    return a.sort()

def suma_llistes(a,b):
    return [a[el]+b[el] for el in range(len(a))]