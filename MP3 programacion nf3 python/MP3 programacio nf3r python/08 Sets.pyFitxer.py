"""
*********************Exercici 1*********************
Afegiu una llista d'elements a un conjunt determinat:

sampleSet = {"Yellow", "Orange", "Black"}
sampleList = ["Blue", "Green", "Red"]

sortida:
{'Green', 'Yellow', 'Black', 'Orange', 'Red', 'Blue'}
"""
sampleSet = {"Yellow", "Orange", "Black"}
sampleList = ["Blue", "Green", "Red"]

sortida = set(sampleList) | sampleSet
print(sortida)


"""
*********************Exercici 2*********************
Retorna un conjunt d’elements repetits

set1 = {10, 20, 30, 40, 50}
set2 = {30, 40, 50, 60, 70}

Sortida:
{40, 50, 30}
"""
set1 = {10, 20, 30, 40, 50}
set2 = {30, 40, 50, 60, 70}

sortida = set1 & set2
print(sortida)

"""
*********************Exercici 3*********************
Retorna un conjunt nou amb tots els elements dels dos conjunts eliminant els duplicats.

set1 = {10, 20, 30, 40, 50}
set2 = {30, 40, 50, 60, 70}
 
Sortida
{70, 40, 10, 50, 20, 60, 30}
"""
set1 = {10, 20, 30, 40, 50}
set2 = {30, 40, 50, 60, 70}

sortida = set1 | set2
print(sortida)


"""
*********************Exercici 4*********************
Tenint en compte dos conjunts de Python, actualitzeu el primer conjunt amb elements que només existeixen al primer conjunt i no al segon conjunt.


set1 = {10, 20, 30}
set2 = {20, 40, 50}
Sortida:
set1 = {10, 30}
"""
set1 = {10, 20, 30}
set2 = {20, 40, 50}

sortida = set1 - set2
print(sortida)

"""
*********************Exercici 5*********************
Traieu 10, 20, 30 element d'un conjunt següent alhora

set1 = {10, 20, 30, 40, 50}
Sortida:
{40, 50}

"""
set1 = {10, 20, 30, 40, 50}
treure = {10, 20, 30}

sortida = set1 - treure
print(sortida)
"""
*********************Exercici 6*********************
Cerqueu si una cadena introduïda per teclat té caràcters únics.

entrada de mostra
Just => té caràcters únics
Alexander => té duplicats
"""
cadena = input("Introdueix el text:")
if len(cadena)== len(set(cadena)):
  print(f"{cadena} => té caracters únics")
else:
  print(f"{cadena} => té duplicats")

"""
*********************Exercici 7*********************
Donades les variables TEX1 i TEX2  que trobaràs a https://repl.it/join/ontzbvzb-pilarmote que contenen textos de Josep Carner i Manuel de Pedrolo respectivament, utilitzeu de manera òptima els coneixements apresos fins ara per respondre a les següents preguntes:

Elimina en ambdues variables els signes de puntuació (,.;) i transforma a minúscules (mètode lower).
Quantes paraules té TEXT1? I quantes TEXT2?
Quines paraules té TEXT1 que continguin 2 lletres ‘a’ que també té TEXT2?
Quines paraules hi ha AMB ACCENT que estan en ambdós variables TEXT1 i TEXT2? 
Quines paraules que contenen un apòstrof, un guió o bé un punt volat (·) estan a TEXT1 i no a TEXT2?
Quines paraules que tenen almenys 4 vocals hi ha TEXT1 o TEX2 però no comparteixen?

"""
TEXT1 = "Com les maduixes Menja maduixes l'àvia d'abans de Sant Joan; per més frescor, les vol collides d'un infant. Per això la néta més petita, que és Pandara, sabeu, la que s'encanta davant d'una claror i va creixent tranquil·la i en ‘admiració i a voltes, cluca d'ulls, aixeca al cel la cara, ella, que encar no diu paraules ben ardides i que en barreja en una música els sentits, cull ara les maduixes arrupides, tintat de rosa el capciró dels dits. Les prunes d'or Aglaia té una set que eixuga el seny, la parla… Superbament s'aixeca, damnant el seu descans, i enfonsa en la prunera les cobejoses mans i enlaira tot el rostre, com si volgués besar-la. I l'arbre, que amb un lleu serpejament de branques sembla oferir-nos l'or, la mel d'algun pecat, s'estremeix un moment de la ferocitat del gran perfum impúdic i de les dents tan blanques. XVI Els codonys tardorals Però ja saps com elles es tornen malgirbades  per fills i feines, o perquè no n'han tingut, i amb cara tediosa caminen desmarxades i són codonys, diries, el fruit més boterut—. I l'altre amic que deia: —Quan fina tot esclat, nosaltres rondinem, esgarriant les passes, i flagel·lem el dia amb folles amenaces, saturns a la memòria del goig mal escampat. Llavores, el codony, que es féu vell en la branca,  dins el calaix perfuma la nostra roba blanca, i si l'amorosim al caliu de la llar i l'acostem als llavis sorruts, és dolç, encar."

TEXT2 = "Ho havia planificat tot durant 20 anys. S'havia desfet de tot i de tothom. Estava segur que, en aquells moments, ja no el coneixia ningú. No quedava cap fotografia amb el seu veritable físic. I havia tingut tantes identitats diferents que ni ell es recordava de totes. Ara havia decidit començar una nova vida en un lloc on no el coneixia ningú. Era un poble qualsevol que un dia va veure mentre feia un viatge. Havia pensat que seria un bon lloc per començar de zero. El trajecte era la part més difícil. A l'estació va comprar un bitllet de tren nocturn amb destinació a Manchester. No volia que el busquessin enlloc. Baixaria al poble que havia triat abans d'arribar a la ciutat. També s'havia preocupat pel físic: ara duia bigoti i inflava les galtes d'una manera que li canviava la cara. Dret al passadís va esperar la sortida del tren. I va encendre l'última cigarreta, perquè a la nova vida pensava desfer-se d'aquest costum. El tabac li va semblar més bo que altres vegades i va fumar lentament, per fer durar el plaer." 

PUNTUACIO = ",;.:—"
ACCENTS="àèéíòóú"
GUIO ="-·'’"
VOCALS = "aeiou" + ACCENTS

'''
a) Elimina en ambdues variables els signes de puntuació (,.;) i transforma a minúscules (mètode lower).
'''
TEXT1 = ''.join([c for c in TEXT1 if c not in PUNTUACIO ])
TEXT2 = ''.join([c for c in TEXT2 if c not in PUNTUACIO ])
TEXT1 = TEXT1.lower()
TEXT2 = TEXT2.lower()

"""
b) Quantes paraules té TEXT1? I quantes TEXT2?
Sortida:
TEXT1 té 246 paraules
TEXT1 té 184 paraules
"""
TEXT1 = TEXT1.split()
TEXT2 = TEXT2.split()

print(f"b) TEXT1 té {len(TEXT1)} paraules")
print(f"b) TEXT1 té {len(TEXT2)} paraules")

"""
c) Quines paraules té TEXT1 que continguin 2 lletres ‘a’ que també té TEXT2?
Sortida: {'cara', 'ara'}
"""
dosAs = set([paraula for paraula in TEXT1 if paraula.count('a')==2]) & set([paraula for paraula in TEXT2 if paraula.count('a')==2])
print(f"c) Les paraules que tenen 2 as que estan a TEXT1 i a TEXT2 són {dosAs}")

"""
d) Quines paraules hi ha AMB ACCENT que estan en ambdós variables TEXT1 i TEXT2? 
Sortida: {'més', 'perquè'}
"""
ambAccent = set([paraula for paraula in TEXT1 for c in paraula if c in ACCENTS]) & set([paraula for paraula in TEXT2 for c in paraula if c in ACCENTS])
print(f"d) Les paraules que tenen accents que estan a TEXT1 i a TEXT2 són {ambAccent}")

"""
e) Quines paraules que contenen un apòstrof, un guió o bé un punt volat (·) estan a TEXT1 i no a TEXT2?
Sortida: {"d'algun", "d'abans", "l'altre", "d'ulls", "s'estremeix", "s'aixeca", 'flagel·lem', 'besar-la', 'oferir-nos', "n'han", "d'or", "s'encanta", "l'arbre", "l'amorosim", "d'un", "l'àvia", "l'or", 'tranquil·la', "l'acostem"}
"""
guioPuntApostrof = set([paraula for paraula in TEXT1 for c in paraula if c in GUIO]) - set([paraula for paraula in TEXT2 for c in paraula if c in GUIO])
print(f"e) Les paraules que tenen (-·'’) que estan a TEXT1 i no a TEXT2 són {guioPuntApostrof}")

"""
f) Quines paraules que tenen almenys 4 vocals hi ha a TEXT1 o TEXT2 però no comparteixen?
Sortida: {'superbament', 'fotografia', 'enlaira', 'identitats', "s'estremeix", "s'aixeca", 'veritable', '‘admiració', "l'estació", 'amenaces', 'preocupat', 'aixeca', 'coneixia', 'oferir-nos', 'canviava', 'planificat', 'maduixes', 'destinació', 'recordava', 'cobejoses', 'memòria', 'quedava', 'busquessin', "l'amorosim", 'arrupides', 'ferocitat', 'tediosa', 'paraules', 'aglaia', 'esgarriant', 'eixuga', 'serpejament', 'tranquil·la', 'cigarreta', 'desmarxades', 'baixaria', 'qualsevol', 'malgirbades'}
"""
quatreVocals = set([paraula for paraula in TEXT1 if sum([paraula.count(v) for v in VOCALS])>=4 ]) ^ set([paraula for paraula in TEXT2 if sum([paraula.count(v) for v in VOCALS])>=4 ])
print(f"f) Les paraules que tenen almenys 4 vocals hi ha a TEXT1 o a TEXT2 però no comparteixen {quatreVocals}")