"""
1. Programa la funció matriu2d, que li passes 2 nombres enters n1,
n2 i retorna una matriu m de 2 dimensions n1 x n2 plena de nombres
aleatoris entre l’1 i el 100.
"""
import random
def matriu2d(n1, n2):
    m=[]
    rando=[]
    if n1>0 and n2>0:
        for i in range(n1):
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
#def llistaMultiples(m):
    
"""
4. Programa la funció llistaUnica que li passes la matriu m i
retorna una llista única (sense elements repetits) d’1 dimensió.
"""
#def llistaUnica():
    
"""
5. Programa la funció minMax que retorna el mínim i el màxim
de la matriu m que li passes com a paràmetre.
"""
#def minMax(m):
#    return min(m),max(m)
"""
6. Programa la funció acabaEn que li passes la matriu m com a
argument, i un enter e entre l’0 i el 9 i retorna una llista
d’1 dimensió formada pels nombres que la seva última xifra és e.
"""
#def acabaEn(m,5):
    
"""
7. Programa la funció quadrat que donat un sencer s entre
10 i 20 retorna una matriu quadrada de 2 dimensions de mida
s x s inicialitzada al caràcter que li passes com a segon paràmetre.
"""
#def quadrat():
    
"""
8. Programa la funció inicialitza que inicialitza tots els
elements de la matriu al caràcter que li passes per argument.
(arguments, la matriu q i el caràcter c).
"""
#def inicialitza():
    
"""
9. Programa la funció diagonal que posa en les diagonals de la
matriu quadrada q, el caràcter c. Es passen com a paràmetres de
la funció q i c.
"""
#def diagonal():
    
"""
10. Programa la funció creu que rep 2 paràmetres n i c:
-Comprova que n sigui un nombre senar positiu sinó retorna “error”.
-Genera una matriu quadrada de mida n x n, amb tots el elements “ “.
-Forma una creu amb el caràcter c, és a dir, tots els elements de
la columna del mig han de ser el caràcter c i tots els elements de
la fila del mig han de ser el caràcter c.
"""
#def creu():
    

n1 =int(input("n1"))
n2 =int(input("n1"))
m = matriu2d(n1, n2)
print(m)
print(21*"=","Funció printMatriu",21*"=")
printMatriu(m)
#llistaMultiples(m)

e=0
while e>-1:
    e =int(input("enter entre 1-10: "))
print("b")

    