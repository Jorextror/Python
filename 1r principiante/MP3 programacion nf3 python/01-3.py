'''Jordi Oliveda
Fes un programa per endevinar un nombre entre
l’1 i el 9 (ambdós inclosos) que es genera aleatòriament.
L’usuari introduirà el nombre per teclat i el programa retornarà
'''

import random
'''definir x,a como entero'''
x = int(input("Introdueix un número: "))

a = random.randint(0, 9) """hagafa un número aleatori entre 0 a 9"""

if x == a:
    print("ENHORABONA!! Ets un crack!")
elif x == a-1 or x == a+1:
    print("quasi, pels pèls!")
elif x <= a-4 or x >= a+4:
    print("dedica’t al parxís")
else:
    print("la propera vegada ho faràs millor")
print(a)