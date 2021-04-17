#Crea una tupla nova que sigui la tupla girada (al revés)
print("1 Crea una tupla nova que sigui la tupla girada (al revés)")
aTuple = (10, 20, 30, 40, 50)
revesListC = tuple([aTuple[-(i + 1)] for i in range(len(aTuple))])
sliceReves = aTuple[::-1]
reversedT = tuple([el for el in reversed(aTuple)])
metodeReves = list(aTuple)
metodeReves.reverse()
metodeReves = tuple(metodeReves)

print(revesListC)
print(sliceReves)
print(reversedT)
print(metodeReves)

#Fes una tupla d’un sol element anomenada unSol i amb contingut 50
print("2. Fes una tupla d’un sol element anomenada unSol i amb contingut 50")

unSol = (50, )
print(unSol)

#Fes un swap de les següents tuples 2 versions, amb variable auxiliar i directament
print("3. Fes un swap de les següents tuples 2 versions, amb variable auxiliar i directament")
tuple1 = (99, 88)
tuple2 = (11, 22)

tuple1, tuple2 = tuple2, tuple1
print(tuple1, tuple2)

tupleAux = tuple1
tuple1 = tuple2
tuple2 = tupleAux
print(tuple1, tuple2)

# 4 Ordena la tupla pel segon element
print("4 Ordena la tupla pel segon element")
tuple1 = (('a', 23), ('b', 37), ('c', 11), ('d', 29))

lTup = list(tuple1)
print(lTup)

# Bombolla
"""
n = len(LL)
intercanvi = True
while intercanvi:
    intercanvi=False
    for i in range(1,n):
        if LL[i-1] > LL[i]:
            LL[i],LL[i-1]=LL[i-1],LL[i]
            intercanvi=True
    n-=1
print(LL)
"""
# sortida esperada
n = len(lTup)
intercanvi = True
while intercanvi:
    intercanvi = False
    for i in range(1, n):
        if lTup[i - 1][1] > lTup[i][1]:
            lTup[i], lTup[i - 1] = lTup[i - 1], lTup[i]
            intercanvi = True
    n -= 1
print(lTup)
tuple1 = tuple(lTup)

# 5 Digues quantes vegades apareix el valor 50 en la tupla, i quin % representa?
print("5 Digues quantes vegades apareix el valor 50 en la tupla, i quin % representa?")
tuple1 = (50, 10, 60, 70, 50)

print(
    f"El valor 50 apareix {tuple1.count(50)} i representa el {tuple1.count(50)*100/len(tuple1)}%"
)

print("6. Comprova si tots els ítems de la tupla tenen el mateix valor")
#6 Comprova si tots els ítems de la tupla tenen el mateix valor
tuple1 = (45, 45, 45, 45)
iguals = True
for el in tuple1:
    if el != tuple1[0]:
        iguals = False

if iguals:
    print(f"A la tupla {tuple1} tots els elements són iguals")
else:
    print(f"A la tupla {tuple1} NO tots els elements són iguals")

# 7 Com es crea una tupla buida? Com es converteix una tupla en una llista?
print("7 Com es crea una tupla buida? Com es converteix una tupla en una llista?")
my_tuple = ()
print(type(my_tuple))

tuplaALlista = list(tuple1)
llistaATupla = tuple(tuplaALlista)
print(tuplaALlista, llistaATupla)

# 8 Tenint una llista de números, escriviu un programa Python per crear una llista de tuples que tinguin el primer element com a número i el segon element com a cub del número.
print("8 Tenint una llista de números, escriviu un programa Python per crear una llista de tuples que tinguin el primer element com a número i el segon element com a cub del número.")
list = [1, 2, 3]
#Output: [(1, 1), (2, 8), (3, 27)]

tuplaCubs = [(el, el**3) for el in list]
print(tuplaCubs)

print("9  Fes una lllista de tuples de totes les combinacions  possibles de 2 tuples d'arguments.")

# 9 Fes una lllista de tuples de totes les combinacions  possibles de 2 tuples d'arguments.
t1 = (7, 2)
t2 = (7, 8)
# Output : [(7, 7), (7, 8), (2, 7), (2, 8), (7, 7), (7, 2), (8, 7), (8, 2)]
# sortida: [(7, 7), (7, 8), (2, 7), (2, 8), (7, 7), (8, 7), (7, 2), (8, 2)]

llistaCombinacions = [(et1, et2) for et1 in t1 for et2 in t2]
llistaCombinacions += [(et2, et1) for et1 in t1 for et2 in t2]

print(llistaCombinacions)

# 10 Escriviu un codi en Python per trobar els elements repetits d’una llista i construeix una llista de tuples on surti en primer terme l’element i en segon terme quantes vegades apareix.
print("10 Escriviu un codi en Python per trobar els elements repetits d’una llista i construeix una llista de tuples on surti en primer terme l’element i en segon terme quantes vegades apareix.")
llista = [1, 2, 3, 1, 2, 1, 1]
#   sortida = [(1,4),(2,2),(3,1)]
#   i per pantalla mostrar:
#       l’element 1 apareix 4 vegades en la llista
#       l’element 2 …

llistaU = set(llista)

aparicions = [(el, llista.count(el)) for el in llistaU]
for el in aparicions:
    print(f"L'element {el[0]} apareix {el[1]} vegadades a la lista")

#11 Troba en quina posició es troba l’element 20:
print("11 Troba en quina posició es troba l’element 20:")
aTuple = ("Orange", [10, 20, 30], (5, 15, 25))
#ajuda:
for i in range(len(aTuple)):
    try:
        iterator = iter(aTuple)
    except TypeError:
        pass
        # not iterable
    else:
        for j in range(len(aTuple[i])):
            if aTuple[i][j] == 20:
                pos = (i, j)
print(pos)