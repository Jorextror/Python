"""Jordi Oliveda
Programa l’algorisme dEuclides (les dues versions). Prova’l amb 1071 i 462.
"""

a=1071
b=462

#versio residu
while b != 0:
    t=b #guardm el valor en un temporal
    b=a % b #treiem el residu de la divisio entre equets dos caracters
    a=t #tornem a donarli el valor el caracter i tornara a treure un altre residu en el b fins que sigui 0
print("El mcd de",a,"i",b,"és",a)

#versio resta
while b != 0:
    if a > b: #si és a més petit que b entra a restar la b si no resta la a fins que un dels dos sigui 0
        a = a - b
    else:
        b = b - a
print("El mcd de",a,"i",b,"és",a)