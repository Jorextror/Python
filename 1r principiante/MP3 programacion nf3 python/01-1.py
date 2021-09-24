"""Jordi Oliveda
Fes un programa que donat un número sencer que
introduïm per teclat ens digui si és parell o és senar

definir num,r como Entero"""

num = int(input("Escriu un número: "))

r = num%2 ''' mira el residu de la divisio, si és 0 és
parell perque és una diviso de 2 el parell mes baix, si no
és 0 el residu és senat.'''
if r == 0: """traduit de pseint en python es fa amb ingles i un si és un if"""
    print("El número és ", num ," és parell ")
else:
    print("El número és ", num ," és senat")