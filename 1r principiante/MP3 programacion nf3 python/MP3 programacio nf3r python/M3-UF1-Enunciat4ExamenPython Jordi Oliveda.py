"""Jordi Oliveda
Encara hi ha places lliures per treballar al creuer i decideixen obrir inscripcions,
t'encarreguen fer el formulari d'inscripció: 
"""
tripulants=[]
"""A
Demana per teclat el nom, i no permet avançar fins que el nom no sigui correcte
(permet qualsevol string sempre que no hi hagi números i la primera lletra sigui en majúscules)
"""
valid=False
while valid==False:
    nom= input("Escriu un nom ")
#    for i in range(len(nom)):
#        if nom[0] not .lower()
    valid=True
"""B
Demana per teclat el gènere, i no permet avançar fins que és M (masculí), F (femení) o I (indefinit)
"""
validG=False
while validG==False:
    genere=input("Escriu el gènere(F/M/I): ")
    if genere == "F" or genere == "M" or genere == "I":
        validG=True
"""C
Demana per teclat el grup_sanguini, i no permet avançar fins que el grup sanguini sigui un dels correctes
(O+,O-,A+,A-,B+,B-,AB+,AB-)
"""
grup_sanguini=('O+','O-','A+','A-','B+','B-','AB+','AB-')
validS=False
while validS==False:
    sang=input("Escriu grup_sanguini(O+,O-,A+,A-,B+,B-,AB+,AB-): ")
    if sang in grup_sanguini:
        validS=True

"""D
Demana per teclat l'any de naixement i no deixa avançar fins el tripulant és major d'edat i menor de 65
"""
validA=False
while validA==False:
    anys=int(input("Escriu l'any de naixement: "))
    if anys < 2003 and anys > 1956:
        validA=True
"""E
Demana per teclat el sou i no deixa avançar fins que sigui un nombre positiu
"""
validS=False
while validS==False:
    sou=int(input("Escriu sou: "))
    if sou > 1:
        validS=True
"""F
Finalment afegeix el tripulant a la llista de tripulants,
comprova-ho amb un print del darrer element de la llista tripulants
"""
