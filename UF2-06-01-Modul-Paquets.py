"""Jordi Oliveda
"""
from assets import requadre
from assets import de_hores_a_segons
from llistes import *
#----1.-----
requadre(3,4)
print('Hola')
requadre(4,3)

#-----2.-----
hores = float( input('Quantes hores? '))
print(de_hores_a_segons(hores))

#----3.-----
n = int(input('Quants elements? '))
w = []
v = demana_llista(n)
imprimeix_llista(v)

print("----omple llista----")
w=omple_llista(w, n, -10, 10)
imprimeix_llista(w)

print("----suma----")
v = suma_llistes(v, w)
imprimeix_llista(v)
 
print("----Ordena----")
ordena_llista(v)
imprimeix_llista(v)
