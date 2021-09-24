"""Jordi Oliveda
El programa generarà una seqüència aleatòria de mida 4 que serà una combinació
de les següents possibles lletres “ABCDE”, pot haver-hi lletres repetides, per exemple AABB, ACBD, ADAB, BBDC, etc.

L'usuari té 5 vides, és a dir 5 possibilitats per intentar encertar la combinació.
Mentre no hagi encertat la combinació, i encara tingui vides fer:
Resta una vida. Mostra les vides restants..
Mostra els intents que ha fet fins el moment. (fer al final)

Demana una combinació de lletres per teclat i no avança fins que no sigui una combinació possible
(mida 4 i formada per les lletres possibles)
Compta quantes lletres encertades estan en la posició correcta.
Marca aquestes posicions per evitar comptar-les dues vegades.
Compta quantes lletres encertades en posició incorrecta hi ha.
Marca aquestes posicions per evitar comptar-les dues vegades.
Si la combinació és guanyadora,
Mostra missatge d’enhorabona i finalitza el programa.
En altre cas:
Mostra quines lletres en posició correcta hi ha amb el símbol ‘#’.
Mostra quines lletres encertades hi ha en posició incorrecta amb el símbol ‘*’.
Mostra les lletres no existents a la combinació amb el símbol ‘-’.
Per exemple si la combinació guanyadora és AACB i l’usuari entra ACDE ha de mostrar # * - -.
La A és correcta i està en la posició correcta #, la C és correcta en posició incorrecta * i la resta D E no encertades, per tant - -.
"""
import random

"""listes, constants, contadors i logics"""
ll=["A","B","C","D","E"]
teclat=[]
antes=[]
vida=5
valid=False
save=""

"""Crea el valor"""
for i in range(0,4):
    sortida=""
    rando=random.randint(0,4)
    teclat+=ll[rando]
print(teclat)

"""Bucles"""
print("Vida restatns:", str(vida))
while valid==False:

    master=input("Introdueix una combinació de 4 lletras formada per ABCDE:")
    
    if len(master) == 4: #si la longitut de lo que em introduit no és de 4 caracters no entra en el bucle i aixi tampoc conta les vides
        sortida=""#cream i anem borran el contingut del seu contingut
        teclat1=teclat#creem un altre llista igual per no borrar la llista
        for i in range(0,4):
            if master[i]==teclat1[i]:#si és igual el caracter li escriu "#"
                sortida+="#"
                teclat1[i]="#"
            else:
                if teclat1[i] in master:#si el carcter esta en la llista pero no en la pocisio corecta "*"
                    sortida+="*"
                    teclat1[i]="*"
                else:
                    sortida+="-"
                    
        #sistema de convinacions gurdades dels intents
        save= master + " => " + sortida
        antes.append(save)
        vida-=1
        #Sortides del script
        print("Resultat:",master,"=>",sortida)
        print("Vida restatns:", str(vida))
        #bucles per mirar si esta encertat o si la vida s'ha acabat
        for i in range(len(antes)):
            print(antes[i])
        if sortida=="####":
            valid=True
            print("Uau enhorabona!! Ets un geni!!!!!!!!")
        if vida == 1:
            valid=True
            print("GAME OVER")
