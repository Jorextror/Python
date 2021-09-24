"""
List Comprehension
"""
#1.Creeu una llista id�ntica a llistaExemple mitjan�ant la comprensi� de la llista.
enun1="Creeu una llista id�ntica a llistaExemple mitjan�ant la comprensi� de la llista."

llistaExemple=[1,2,3,4,5,6]
llistaDuplicada=[el for el in llistaExemple]

#2.Creeu una llista a partir dels elements d'un interval de 1200 a 2000 amb passos de 130, mitjan�ant la comprensi� de la llista.
enun2="Creeu una llista a partir dels elements d'un interval de 1200 a 2000 amb passos de 130, mitjan�ant la comprensi� de la llista."
llistaEx2 = [i for i in range(1200,2000+1,130)]

#3.Utilitzeu la comprensi� de la llista per construir una llista nova a partir de l�anterior, per� sumeu 6 a cada element.
enun3="Utilitzeu la comprensi� de la llista per construir una llista nova a partir de l�anterior, per� sumeu 6 a cada element."
llistaEx3 = [el+6 for el in llistaEx2]

#4.Mitjan�ant la comprensi� de la llista, constru�u una llista que sigui els quadrats de cada element de la llista.
enun4="Mitjan�ant la comprensi� de la llista, constru�u una llista que sigui els quadrats de cada element de la llista."
llista=[1,2,3,4,5,6]
llistaEx4 = [el**2 for el in llista]

#5.Mitjan�ant la comprensi� de la llista, constru�u una llista a partir dels quadrats de cada element de la llista, si el quadrat �s superior a 50.
enun5="Mitjan�ant la comprensi� de la llista, constru�u una llista a partir dels quadrats de cada element de la llista, si el quadrat �s superior a 50."
llista=[1,2,3,7,9,10]
llistaEx5 = [el**2 for  el in llista if el**2>50]

#6.Fes una llista amb tots els nmeros de l1 al 1000 que sn divisibles per 7.
enun6="Fes una llista amb tots els nmeros de l1 al 1000 que sn divisibles per 7."
llistaEx6 = [ i for i in range(1,1000+1) if i%7==0]

#7.Fes una llista amb tots els nmeros de l1 al 1000 que tinguin un 3.
enun7="Fes una llista amb tots els nmeros de l1 al 1000 que tinguin un 3."
llistaEx7 = [i for i in range(1,1000+1) if '3' in str(i)]

#8.Fent servir list comprehensions compteu el nombre d'espais d'una cadena
enun8="Fent servir list comprehensions compteu el nombre d'espais d'una cadena"
cadena="quants espais hi ha"
ex8=len([c for c in cadena if c==' '])

#9.Traieu totes les vocals d'una cadena.
enun9="Traieu totes les vocals d'una cadena."
ex9=''.join([ll for ll in cadena if ll.lower() not in "aeiou"])

#10.Cerqueu totes les paraules d'una cadena de menys de 4 lletres.
enun10="Cerqueu totes les paraules d'una cadena de menys de 4 lletres."
ex10=len([paraula for paraula in cadena.split() if len(paraula)<4])

sortir = False
while not sortir:
  for i in range(10):
    print(f"Exercici{i+1}")
  print("Qualsevol altra opció sortir")
  opcio= int(input("Introdueix el núm de l'Exercici que vols executar :"))
  if opcio==1:
    print(enun1)
    print(llistaExemple,llistaDuplicada)
  elif opcio==2:
    print(enun2)
    print(llistaEx2)
  elif opcio==3:
    print(enun3)
    print(llistaEx3)
  elif opcio==4:
    print(enun4)
    print(llista,llistaEx4)
  elif opcio==5:
    print(enun5)
    print(llistaEx5)
  elif opcio==6:
    print(enun6)
    print(llistaEx6)
  elif opcio==7:
    print(enun7)
    print(llistaEx7)
  elif opcio==8:
    print(enun8)
    print(f"Hi ha {ex8} espais en la cadena: {cadena}")
  elif opcio==9:
    print(enun9)
    print(f"La cadena : {cadena} sense vocals és: {ex9}")
  elif opcio==10:
    print(enun10)
    print(f"hi ha {ex10} paraules de menys de 4 lletres en la cadena :{cadena}")
  else:
    sortir=True
  tecla=input("prem una tecla")