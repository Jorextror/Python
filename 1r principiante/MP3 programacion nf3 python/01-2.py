'''Jordi Oliveda
Escriviu un programa Python per comprovar que un nombre
que introduïm per teclat és múltiple de 7 i múltiple de 5.

definir x, c, s como entero'''
x = int(input("Introdueix un número: "))

c= x/5
s= x/7
if c == 0 and s == 0: """mira si és divisible de 5 i 7
al mateix temps amb un and"""
    print("El número és divisible de 5 i 7")
else:
    print("No és divisible de 5 i 7")