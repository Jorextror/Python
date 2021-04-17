"""Jordi Oliveda
Fes un programa en python que imprimeix les
taules de multiplicar de l’1 a 10 amb un for niuat."""
""""""
"""constants"""
taula= 10
multi=1
"""bucle per annar multiplicant entre ells per fer una taula
he posat i+=1 i j+=1 perque el for comença per 0 i multiplicar per 0 no volem"""
for i in range(taula):
    i+=1
    print("Taula de",i )
    for j in range(taula):
        j+=1
        multi = (i)*(j)
        print(multi)