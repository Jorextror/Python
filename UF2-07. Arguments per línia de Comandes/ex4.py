"""Jordi Oliveda
"""
import sys

sys.argv.pop(0)
llista=[]

abc="ABCDEFGHIJKLMNÑOPQRSTUVWXYZabcdefghijklmnñopqrstuvwxyz"
if len(sys.argv) > 0:
    for i in sys.argv:
        for el in i:
            if el in abc:
                llista.append(el)
            else:
                print(el,": no és una letra del abecedario""\n")
    llista.sort()
print(llista)