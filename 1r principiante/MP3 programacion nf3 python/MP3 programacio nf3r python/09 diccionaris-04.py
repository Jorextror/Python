"""
Ets un professor que acabes d’aprendre python i decideixes utilitzar els teus coneixements. El programa ha de tenir les següents funcionalitats: Afegir Alumne, Eliminar alumne, Afegir  notes a alumne (mòdul, nota), llistat de tots els alumnes (la llista de tots els alumnes), llistat d’un alumne (el nom de l’alumne i totes les seves notes), estadístiques (que responen a les qüestions més avall) i sortir.
Demana els noms dels alumnes per teclat, els noms dels alumnes  d'una classe i les notes que han obtingut. Cada alumne pot tenir diferent quantitat de notes, que també  s’introduiran per teclat, valida que siguin notes entre 0 i 10. Guarda la informació en un diccionari la claus seran els noms dels alumnes i els valors seran llistes de tuples amb les notes de cada alumne. 
Les estadístiques. Quant alumnes ho han aprovat tot?  Quants alumnes tenen 3 suspeses? Qui porta la millor mitjana? Qui haurà de repetir-ho tot?  
Nota: si s'introdueix el nom d'un alumne que ja hi ha el programa ens donarà un error. Recomanació per fer proves fes un diccionari amb unes quantes dades ja introduïdes. 
"""
sortir= False
classe = {
    "Maria":[(1,5),(2,7),(3,10),(4,6)],
    "Jan":[(1,3),(2,3),(3,3)],
    "Carles":[(1,9),(2,10),(3,10)],
    "Carla":[(1,4),(2,1),(3,1),(4,6)]  
    }

MODULS = (1,2,3,4,11,12)
LITERAL = ["D","D","D","D","D","C","C","B","B","A","A",]

while not sortir:

  print("\n1. Afegir  Alumne:")
  print("2. Eliminar Alumne:")
  print("3. Afegir notes a Alumne")
  print("4. Llistat de tots els alumnes")
  print("5. Llistat d'un alumne'")
  print("6. Estadístiques")
  print("7. Sortir")

  opcio = int(input("Introdueix una opció : "))

  if opcio == 1:
    print("Afegir alumne ")
    alumne = input("Introdueix el nom d'un alumne : ")
    classe.setdefault(alumne,[])
    for alumne in classe.keys():
      print(alumne,", ")
    
  elif opcio == 2:
    print("Elimnar alumne ")
    for alumne in classe.keys():
      print(alumne,", ")
    
    alumne = input("Introdueix el nom d'un alumne : ")
    classe.pop(alumne)
    for alumne in classe.keys():
      print(alumne,", ")
    
  elif opcio == 3:
    print("Afegir notes a l'alumne")
    for alumne in classe.keys():
      print(alumne,", ")
    
    alumne = input("Introdueix el nom d'un alumne : ")
    notes = True
    while notes and alumne in classe.keys():
      print("Escriu 0 per finalitzar")
      modul = int(input("Introdueix el mòdul "+str(MODULS)+" : "))
      if modul in MODULS:
        nota = -1
        while nota<0 or nota>10:
          nota = int(input("Introdueix la nota del mòdul M"+str(modul)+" : "))
        classe[alumne] += [(modul,nota)]
        print(classe[alumne])
      else:
        notes = False

  elif opcio == 4:
    print("\nLlistat de tots els alumnes ")
    alumnes = classe.keys()
    for alumne in alumnes:
      print(f"* - {alumne}")
    print()
    
  elif opcio == 5:
    print("Llistat d'un alumne")
    for alumne in classe.keys():
      print(alumne,", ")
    
    alumne = input("\nIntrodueix el nom d'un alumne : ")
    if alumne in classe.keys():
      totAprovat = True
      for nota in classe.get(alumne):
        print(f'La nota del mòdul M{nota[0]} és {nota[1]} que correspon a {"aprovat" if nota[1]>=5 else "suspès"} amb {LITERAL[nota[1]]}')
        if nota[1]<5:
          totAprovat = False
      if totAprovat:
        print("\nEnhorabona!! tot aprovat\n\n")

  elif opcio == 6:
    """
    Les estadístiques. Quant alumnes ho han aprovat tot?  Quants alumnes tenen 3 suspeses? Qui porta la millor mitjana? Qui haurà de repetir-ho tot?  
    """
    print("\nEstadístiques")
    totApropvat = 0
    milloraMitjana = ["",0]
    tresSuspeses = 0
    alumnesRepetirTot = []
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
          tresSuspeses +=1
        if suspeses == len(classe[alumne]):
          alumnesRepetirTot += [alumne]
        if suspeses == 0:
            totApropvat +=1
        if milloraMitjana[1] < notaMitjana:
          milloraMitjana[0] = alumne
          milloraMitjana[1] = notaMitjana
        
    print (f"El nombre d'alumnes que ho han aprovat tot és: {totApropvat}")
    print (f"El nombre d'alumnes amb 3 suspeses és: {tresSuspeses}")
    print (f"L'alumne amb la millor mitjana és: {milloraMitjana[0]} amb una nota de {'{:.2f}'.format(milloraMitjana[1])}")
    print(f"Els alumnes que ho hauran de repetir tot són: {alumnesRepetirTot}")

  elif opcio == 7:
    print("Adéu")
    sortir = True