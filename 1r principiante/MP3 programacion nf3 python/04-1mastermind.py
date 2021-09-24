"""El programa generarà una seqüència aleatòria de mida 4 que serà una combinació
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
ll=["A","B","C","D","E"]
c=[]
for i in range(0,4):
    rando=random.randint(0,4)
    c+=ll[rando]
print(c)

for i in range(0,4):
    i+=1
    print("Vida restatns:", str(i))
    input("Introdueix una combinació de 4 lletras formada per ABCDE:")
    
