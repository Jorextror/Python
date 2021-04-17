"""Jordi Oliveda
PROGRAMES EN PYTHON-6
Podeu fer tots els exercicis en un sol programa. Realitzeu un menú que permeti executar cada exercici.
"""
ex=input("Quin exercici de 1-10? ")
print("---- El Exercici",ex,"----")

if ex == "1":
    print("Creeu una llista idèntica a llistaExemple mitjançant la comprensió de la llista.")
    print("llistaExemple=[1,2,3,4,5,6]")
    print(" ")
    llista = [i for i in range(1,7)] #va afexin el valor de i a la llista fins el 7 que és 6(comenza per el 0)
    print(llista)
    
elif ex == "2":
    print("Creeu una llista a partir dels elements d'un interval de 1200 a 1980 ambdós inclosos, amb passos de 130, mitjançant la comprensió de la llista.")
    print(" ")
    
    llista = [i for i in range(1200,1981,130)] #entra el valor primer(primer valor) i el valor ultim(segon valor) te un interval de salt de 130 (tercer valor)
    print(llista)
    
elif ex == "3":
    print("Utilitzeu la comprensió de la llista per construir una llista nova a partir de l’anterior,però sumeu 6 a cada element.")
    print(" ")
    
    llista = [i+6 for i in range(1200,1981,130)] #lo mateix del anterior pero amb una suma de 6 a cada element per el i+6
    print(llista)
    
elif ex == "4":
    print("Mitjançant la comprensió de la llista, construïu una llista que sigui els quadrats de cada element de la llista.")
    print("llista=[1,2,3,4,5,6]")
    print("")
    
    llista = [i**2 for i in range(1,7)] #podem fer que sigui al quadran posan al principi i**2
    print(llista)
    
elif ex == "5":
    print("Mitjançant la comprensió de la llista, construïu una llista a partir dels quadrats de cada element de la llista, si el quadrat és superior a 50.")
    print("llista=[1,2,3,7,9,10]")
    print("")
    
    llista = [i**2 for i in range(1,11) if i**2 > 50] #un if del valor que suert i elevat al quadran amb un mes gran de 50 perque surti valors de mes de 50
    print(llista)
    
elif ex =="6":
    print("Fes una llista amb tots els números de l’1 al 1000 que són divisibles per 7.")
    print()
    
    llista = [i for i in range(1,1001) if i%7==0] #un if que deixi pasar si és divisible per saber que ho es el resultat és 0 i aixi fem quest if
    print(llista)
    
elif ex=="7":
    print("Fes una llista amb tots els números de l’1 al 1000 que tinguin un 3.")
    print()
    
    llista = [i for i in range(1,1001) if "3" in str(i)] #oh fem amb un if que contingui 3 in str per mirar si hi ha el valor en el string
    print(llista)
    
elif ex=="8":
    print("Fent servir list comprehensions compteu el nombre d'espais d'una cadena")
    """ unString = 'Un string qualsevol que té molts espais' """
    print()
    
    unString = 'Un string qualsevol que té molts espais'
    llista = [i for i in range(len(unString)) if unString[i] == " " ] #un if per contar els spais
    print("hi han ",len(llista),"spais")
    
elif ex=="9":
    print("Traieu totes les vocals d'una cadena.")
    print()
    
    string=("Traieu totes les vocals duna cadena.")
    vocal="AEIOUaeiou"
    llista = [string[i] for i in range(len(string)) if string[i] not in vocal] #un if que mira caracter per caracter i no printea si te alguna vocal
    print(llista)
    
elif ex=="10":
    print("Cerqueu totes les paraules d’una cadena de menys de 4 lletres. (mirar funcio split)")
    print()
    
    unString="Un string qualsevol que té molts espais"
    
    llista = [unString.split()[i] for i in range(len(unString)) if i < 4] #amb la funcio split ajuntem les paraule de una llista i la variable (i) fara de contar fins a quant parar
    print(llista)
    
else:
    print("Error. Prova de posan un número del 1 al 10 ")