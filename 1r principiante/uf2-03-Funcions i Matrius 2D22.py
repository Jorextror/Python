"""Kevin Moya i Jordi Oliveda
1. Programa la funció matriu2d, que li passes 2 nombres enters n1,
n2 i retorna una matriu m de 2 dimensions n1 x n2 plena de nombres
aleatoris entre l’1 i el 100.
"""
import random
def matriu2d(n1, n2):
    m=[]
    if n1>0 and n2>0:
        for i in range(n1):
            rando=[]
            for j in range(n2):
                rando.append(random.randint(1,100))
            m.append(rando)
    else:
        m=-1
    return m
"""
2. Programa la funció printMatriu, que imprimeix la matriu que
li passes com a paràmetre de manera similar a l’exemple:
"""
def printMatriu(m):
    for el in m:
        if el != m[0]:
            print("")
        for i in el:
            print("".join(str(i)),end=" ")
"""
3. Programa la funció llistaMultiples que li passes la matriu
m de 2 dimensions com a argument, i un enter e entre l’1 i el 10
i retorna una llista ll d’1 dimensió formada pels múltiples
d’e existents a la matriu.
"""
def llistaMultiples(m):
    ll=[]
    e=int(input("Introdueix un enter entre 1-10: "))
    if e>0 and e<=10:
        for el in m:
            for el2 in el:
                if el2%e == 0:
                    ll.append(el2)
    return ll
"""
4. Programa la funció llistaUnica que li passes la matriu m i
retorna una llista única (sense elements repetits) d’1 dimensió.
"""
def llistaUnica(m):
    ll=[]
    for el in m:
        for el2 in el:
            ll.append(el2)
    return set(ll)
"""
5. Programa la funció minMax que retorna el mínim i el màxim
de la matriu m que li passes com a paràmetre.
"""
def minMax(m):
    ll=[]
    for el in m:
        for el2 in el:
            ll.append(el2)
    return min(ll),max(ll)
"""
6. Programa la funció acabaEn que li passes la matriu m com a
argument, i un enter e entre l’0 i el 9 i retorna una llista
d’1 dimensió formada pels nombres que la seva última xifra és e.
"""
def acabaEn(m):
    ll=[]
    e=int(input("Introdueix un enter entre 0-9: "))
    if e>=0 and e<10:
        for el in m:
            for el2 in el:
                if el2-e==0 or (el2-e)%10==0:                   
                    ll.append(el2)
    return ll
"""
7. Programa la funció quadrat que donat un sencer s entre
10 i 20 retorna una matriu quadrada de 2 dimensions de mida
s x s inicialitzada al caràcter que li passes com a segon paràmetre.
"""
def quadrat(s,c):
    qua=""
    for el in range(s):
        qua+=(s*c+"\n")
    return qua
"""
8. Programa la funció inicialitza que inicialitza tots els
elements de la matriu al caràcter que li passes per argument.
(arguments, la matriu q i el caràcter c).
"""
def inicialitza(q,c):
    resultat=""
    for el in q:
        resultat+= len(el)*c+"\n"
    return resultat
"""
9. Programa la funció diagonal que posa en les diagonals de la
matriu quadrada q, el caràcter c. Es passen com a paràmetres de
la funció q i c.
"""
def diagonal(c,q):
    resultat=""
    d1= 0
    d2=-1
    for i in q:
        fila=[]
        for j in range(len(i)):
            fila.append("-")
        fila[d1]=c
        fila[d2]=c
        d1+=1
        d2-=1
        resultat+="".join(map(str,fila))+"\n"
    return resultat
"""
10. Programa la funció creu que rep 2 paràmetres n i c:
-Comprova que n sigui un nombre senar positiu sinó retorna “error”.
-Genera una matriu quadrada de mida n x n, amb tots el elements “ “.
-Forma una creu amb el caràcter c, és a dir, tots els elements de
la columna del mig han de ser el caràcter c i tots els elements de
la fila del mig han de ser el caràcter c.
"""
def creu(n,c):
    resultat=""
    d1=0
    d2=-1
    x=0
    for el in n:
        fila=[]
        x+=1
        for i in range(len(el)):
            if i==(len(el)//2):
                fila.append("|")
            else:   
                if x==(len(n)//2)+1:
                    fila.append("|")
                else:
                    fila.append("-")

        fila[d1]=c
        fila[d2]=c
        d1+=1
        d2-=1
        resultat+="".join(map(str,fila))+"\n"
    return resultat

print("\tFuncions i Matrius 2D\n",30*"=","\n1. matriu2d\n2. printMatriu\n3. llistaMultiples\n4. llistaUnica\n5. minMax\n6. acabaEn\n7. quadrat\n8. inicialitza\n9. diagonal\n10. creu\n11. Sortida")
m=[[34, 5, 56, 88, 9, 10, 64, 22, 41, 23, 75, 91, 38, 34, 40, 63, 91, 31, 32], [60, 23, 7, 98, 77, 12, 10, 31, 15, 38, 73, 36, 79, 94, 94, 30, 96, 59, 84], [47, 51, 60, 23, 27, 64, 52, 83, 87, 80, 18, 70, 24, 65, 53, 67, 88, 6, 16], [44, 36, 64, 76, 20, 85, 29, 39, 2, 23, 89, 62, 34, 2, 70, 32, 76, 12, 90], [88, 9, 16, 82, 89, 45, 80, 18, 63, 10, 63, 43, 25, 73, 7, 35, 28, 23, 97], [67, 21, 87, 17, 99, 82, 16, 39, 90, 75, 88, 94, 53, 24, 81, 48, 64, 90, 29], [45, 19, 26, 86, 100, 36, 32, 74, 32, 6, 62, 34, 87, 3, 71, 55, 66, 20, 13], [65, 80, 35, 70, 37, 92, 57, 76, 12, 73, 67, 53, 2, 5, 24, 21, 21, 71, 75], [54, 12, 97, 87, 91, 91, 93, 51, 74, 11, 56, 47, 19, 22, 25, 7, 21, 3, 73], [64, 67, 40, 17, 25, 12, 84, 23, 35, 27, 24, 23, 65, 19, 75, 31, 58, 100, 85], [48, 69, 50, 34, 82, 51, 44, 75, 14, 86, 23, 66, 62, 40, 64, 35, 71, 94, 4], [90, 71, 94, 46, 48, 83, 19, 20, 93, 36, 62, 65, 39, 96, 62, 14, 12, 16, 7], [47, 9, 23, 36, 21, 77, 56, 84, 88, 68, 5, 72, 58, 48, 27, 82, 10, 45, 94], [53, 68, 68, 82, 34, 52, 32, 78, 38, 12, 59, 12, 92, 76, 10, 97, 6, 36, 37], [20, 1, 32, 22, 25, 82, 39, 88, 69, 96, 94, 88, 90, 90, 22, 8, 91, 35, 86], [22, 32, 20, 92, 38, 8, 63, 44, 81, 17, 24, 12, 84, 86, 94, 87, 82, 100, 68], [69, 12, 34, 47, 12, 1, 86, 9, 14, 93, 79, 34, 34, 1, 31, 17, 89, 80, 10], [21, 26, 19, 25, 15, 88, 4, 43, 20, 46, 68, 12, 88, 48, 12, 95, 98, 38, 36], [11, 86, 68, 9, 82, 30, 98, 28, 18, 35, 8, 45, 2, 74, 53, 36, 19, 18, 4]]
opcio="0"
while opcio != "11":
    opcio = input("opcio(1-11) ")
    if opcio == "1":
        n1 =int(input("Introdueix un enter: "))
        n2 =int(input("Introdueix un segon enter: "))
        m=matriu2d(n1,n2)
        print(m)
    if opcio == "2":
        print(m)
        print(21*"=","Funció printMatriu",21*"=")
        printMatriu(m)
    if opcio == "3":
        print(llistaMultiples(m))
    if opcio == "4":
        print(llistaUnica(m))
    if opcio == "5":
        print(minMax(m))
    if opcio == "6":
        print(acabaEn(m))
    if opcio == "7":
        s=0
        while s <= 9 or s>=21:
            s=int(input("introdueix un número entre 10-20: "))
        c='11'
        while len(c)!=1:
            c=str(input("introdueix un caracter: "))
        print(quadrat(s,c))
        
    if opcio == "8":
        c='11'
        while len(c)!=1:
            c=str(input("introdueix un caracter: "))
        print(inicialitza(m,c))

    if opcio == "9":
        c='11'
        while len(c)!=1:
            c=str(input("introdueix un caracter: "))
        print(diagonal(c,m))
        #si la matri no té la mateixa dimencio de longitut i amplada dona error :(

    if opcio == "10":
        c='11'
        while len(c)!=1:
            c=str(input("introdueix un caracter: "))
        print(creu(m,c))
        #si la matri no té la mateixa dimencio de longitut i amplada dona error :(