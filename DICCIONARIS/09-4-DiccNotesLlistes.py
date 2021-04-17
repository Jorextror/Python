"""JordiOliveda
(5 punts) Ets un professor que acabes d’aprendre python i decideixes utilitzar
els teus coneixements. El programa ha de tenir les següents funcionalitats:
Afegir Alumne, Eliminar alumne, Afegir  notes a alumne (mòdul, nota),
llistat de tots els alumnes (la llista de tots els alumnes),
llistat d’un alumne (el nom de l’alumne i totes les seves notes),
estadístiques (que responen a les qüestions més avall) i sortir.

Demana els noms dels alumnes per teclat, els noms dels alumnes
d'una classe i les notes que han obtingut. Cada alumne pot tenir diferent
quantitat de notes, que també  s’introduiran per teclat, valida que siguin
notes entre 0 i 10. Guarda la informació en un diccionari les claus seran
els noms dels alumnes i els valors seran llistes de tuples de  parelles de
tuples  (modul, nota) per emmagatzemar les notes de cada alumne. 

Les estadístiques. Quant alumnes ho han aprovat tot?
Quants alumnes tenen 3 suspeses? Qui porta la millor mitjana?
Qui haurà de repetir-ho tot?  

Nota: si s'introdueix el nom d'un alumne que ja hi és,
el programa ens donarà un error. Recomanació per fer proves fes
un diccionari amb unes quantes dades ja introduïdes. 
"""
classe = {
    "Maria":[(1,5),(2,7),(3,10),(4,6)],
    "Jan":[(1,3),(2,3),(3,3)],
    "Carles":[(1,9),(2,10),(3,10)],
    "Carla":[(1,4),(2,1),(3,1),(4,6)]}
valid=False
moduls = (1, 2, 3, 4)
letra=["S","S","S","S","S","B","B","N","N","E","E"]
while not valid:
    print("\n1. Afegir  Alumne:")
    print("2. Eliminar Alumne:")
    print("3. Afegir notes a Alumne")
    print("4. Llistat de tots els alumnes")
    print("5. Llistat d'un alumne'")
    print("6. Estadístiques")
    print("7. Sortir")
    
    num = int(input("Introdueix una opció : "))
    
    if num == 1:
        print("afageix un alumne")
        alumne = input("Nom del alumne: ")
        classe.setdefault(alumne,[])
        for alumne in classe.keys():
            print(alumne,", ")
    
    elif num == 2:
        print("Eliminar alumne")
        for alumne in classe.keys():
            print(alumne,", ")
            
        alumne = input("Quin usuari deseas borrar? ")
        classe.pop(alumne)
        
    elif num == 3:
        print("afegir nota alumne")
        for alumne in classe.keys():
            print(alumne,", ")
            
        alumne = input("Quin alumne vols afegir-li nota?" )
        llista=False
        while valid == False:
            modul = int(input("Introdueix el modul"))
            if modul in moduls:
                nota=-1
                while nota <0 or nota >10:
                    nota = int(input("nota del mòdul: "))
                classe[alumne] += [(modul,nota)]
                print(classe[alumne])
            else:
                llista=True

    elif num == 4:
        print("\nLlistat de tots els alumnes ")
        alumnes = classe.keys()
        for alumne in alumnes:
            print(alumne)
        print()
        
    elif num == 5:
        print("Llistat d'un alumne")
        for alumne in classe.keys():
            print(alumne,", ")
        
        alumne = input("\nIntrodueix el nom d'un alumne: ")
        if alumne in classe.keys():
            aprovatTot = True
            for nota in classe.get(alumne):
                nota1=nota[0]
                nota2=nota[1]
                if nota2 >= 5:
                    resultat= "aprovat"
                else:
                    resultat= "suspès"
                letraR={letra[nota[1]]}
                print("La nota del mòdul M", nota1 ," és ", nota2 ,"que correspon a ",resultat," amb", letraR)
            if nota[1]<5:
                aprovatTot = False
            if aprovatTot:
                print("\ntot aprovat\n\n")

    elif num == 6:
        print("\nEstadístiques")
        aprobatTot = 0
        millorMitjana = ["",0]
        Suspeses3 = 0
        repetirTot = []
        for alumne in classe.keys():
            notaMitjana=0
            suspeses = 0

            if len(classe[alumne])>0:
            
                for nota in classe[alumne]:
                    notaMitjana += nota[1]
                    if  nota[1] < 5:
                        suspeses += 1
            
            notaMitjana = notaMitjana/ len(classe[alumne])
            if suspeses == 3:
                Suspeses3 +=1
            if suspeses == len(classe[alumne]):
                repetirTot += [alumne]
            if suspeses == 0:
                aprobatTot +=1
            if millorMitjana[1] < notaMitjana:
                millorMitjana[0] = alumne
                millorMitjana[1] = notaMitjana
            
        print ("El nombre d'alumnes que ho han aprovat tot és:", aprobatTot)
        print ("El nombre d'alumnes amb 3 suspeses és:", Suspeses3)
        print ("L'alumne amb la millor mitjana és:", millorMitjana[0] ,"amb una nota de", millorMitjana[1])
        print("Els alumnes que ho hauran de repetir tot són:", repetirTot)

    elif num == 7:
        valid = True