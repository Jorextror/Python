"""Jordi Oliveda
2. Fes un altre programa en python amb un menú per fer la crida a les
següents funcions:

1-Nom funció:  factorial. Funcionalitat: Calcula el factorial d'un número
(un enter no negatiu). La funció accepta el nombre com a paràmetre i
retorna el factorial, o bé un error (-1), el missatge d’error s’imprimirà
després de la crida.
"""
def factorial(a):
    x = int(a)
    count = 1
    z = 1
    while z <= x:
        count = count * z
        z = z + 1
    return count
"""
2-Nom funció:  comptaMajusMinus. Funcionalitat: accepta una cadena com a
paràmetre  i retorna el nombre de lletres majúscules i minúscules.
Cadena de mostra: ‘Una Cadena De Prova' Sortida esperada: (4,12).
El missatge es mostra després de la crida.
"""
def comptaMajusMinus(a):
    indice=0
    mayusculas=0
    minusculas=0
    while indice < len(a):
        letra = a[indice]
        if letra.isupper() == True:
            mayusculas +=1
        else:
            minusculas +=1
        indice += 1
    return (mayusculas,minusculas)
"""
3-Nom funció:  llistaUnitaria. Funcionalitat: Donada una  llista que
li passem com paràmetre, retorna una nova llista amb elements únics
de la primera llista. Llista de mostres: [1,2,3,3,3,3,4,5] Llista unitària:
[1, 2, 3, 4, 5]. No es pot utilitzar la comanda set.
"""
def llistaUnitaria(a):
    b=[]
    for i in range(len(a)):
        if a[i] not in b:
            b.append(a[i])
    return b
"""
4-Nom funció:  primer. Funcionalitat: Escriu una funció Python
que pren un nombre com a paràmetre menor que 10000 i comproveu
si el número és primer o no, o bé error.
(podeu utilitzar l’algoritme del sedàs d’Eratòstanes)
"""
def primer(a):
    criba=[]
    for valor in range(1,1001):
        criba.append(valor)

    contador=0
    total=len(criba)
    esprimo=1

    while(contador<=total):
        auxiliar=2
        esprimo=1
        while(auxiliar<=contador/2 and esprimo!=0):
            esprimo=contador%auxiliar
            if esprimo==0: #print (% no es primo, contador)
                criba.remove(contador)
            auxiliar=auxiliar+1
        contador=contador+1
    if a in criba:
        return True
    else:
        return False
"""
5-Nom funció parells: Funcionalitat: Retorna els números parells
d'una llista determinada passada com paràmetre. Llista de mostres:
[1, 2, 3, 4, 5, 6, 7, 8, 9] Resultat esperat: [2, 4, 6, 8] 
"""
def parells(a):
    b=[]
    for i in range(len(a)):
        if a[i]%2 == 0:
            b.append(a[i])
    return b
"""
6-Nom funció perfecte: Funcionalitat: Escriviu una funció Python
per comprovar si un número és perfecte o no. Segons Wikipedia:
En la teoria de nombres, un nombre perfecte és un enter positiu
que és igual a la suma dels seus divisors positius correctes, és a dir,
la suma dels seus divisors positius excloent el nombre en si
(també conegut com la seva suma alíquota). De forma equivalent,
un nombre perfecte és un nombre que és la meitat de la suma de tots
els seus divisors positius (incloent-hi). Exemple: el primer nombre
perfecte és 6, perquè 1, 2 i 3 són els seus divisors positius correctes,
i 1 + 2 + 3 = 6. Igualment, el número 6 és igual a la meitat de la
suma de tots els seus divisors positius: (1 + 2 + 3 + 6) / 2 = 6.
El següent número perfecte és 28 = 1 + 2 + 4 + 7 + 14. 
"""
def perfecte(a):
    suma = 0
    for i in range(1,a):
        if (a % i == 0):
            suma += i
     
    if a == suma:
        return True
    else:
        return False
"""
7-Nom funció palíndrom: Funcionalitat: verifica si una cadena passada
com paràmetre és palíndrom o no.
"""
def palíndrom(a):
    b = ''.join(reversed(a))
    if a == b:
        return True
    else:
        return False

print("\tFuncions 1\n",20*"=","\n1. factorial\n2. compta Majus Minus\n3. llista Unitaria\n4. primer\n5. parells\n6. perfecte\n7. palíndrom\n8. Sortir")

opcio="0"
while opcio != "8":
    
    opcio = input("opcio(1-8) ")
    if opcio == "1":
        a=input("introdueix un número: ")
        print(factorial(a))
        
    elif opcio == "2":
        a = input("introdueix una cadena: ")
        print(comptaMajusMinus(a))

    elif opcio == "3":
        a= [1,2,3,3,3,3,4,5]
        print(llistaUnitaria(a))
        
    elif opcio == "4":
        valid=False
        while not valid==True:
            a = int(input("Introdueix un valor menor de 10000: "))
            if a <= 10000:
                valid= True
        if primer(a):
            print("És un nombre Primer el",a)
        else:
            print("No és un nombre primer el",a)
            
    elif opcio == "5":
        a=[1, 2, 3, 4, 5, 6, 7, 8, 9]
        print(parells(a))
    
    elif opcio == "6":
        a=int(input("introdueix un número: "))
        if perfecte(a):
            print("És un número perfecte el",a)
        else:
            print("No és un número perfecte el",a)
            
    elif opcio == "7":
        a=input("introdueix una cadena: ")
        if palíndrom(a):
            print("la cadena",a,"és un palíndrom")
        else:
            print("la cadena",a,"NO és un palíndrom")