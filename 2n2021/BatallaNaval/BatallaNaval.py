# Fes un joc de batalla naval per jugar contra l'ordinador.

# Especificacions:

# Taulell de 10x10 posicions.
# Hi col·locarem aleatòriament els següents vaixells ( no es poden tocar entre ells):
# 1 portaavions de 4 caselles.
# 2 cuirassats de 3 caselles.
# 3 fragates de 2 caselles.
# 4 patrulleres d'1 casella.
# A cada pas es mostrarà la matriu indicant les cel·les ocultes, tocades i buides.
# L'usuari introduirà fila i columna.
# Quan s'enfonsin tots els vaixells la partida s'acaba i sortim del programa (amb un missatge de congratulations!).
# Opció en català, anglès i alguna altra llengua.
# Cal que puguis jugar diverses partides simultànies (diferents taulells). El jugador ha de poder anar canviant entre les diverses partides i reprendre on l'ha deixat.
# Cal fer-ho amb OOP i, per tant, primer cal definir els objectes i les estructures de dades i decidir com utilitzar-les en el codi principal. Com a mínim, heu d'implementar les següents classes: class Tauler(), class Vaixell() i class Casella().
from random import randint
x = 10
y = 10
lletres=["A","B","C","D","E","F","G","H","I","J"]
flota = [4,3,3,2,2,2,1,1,1,1]

class Tauler(object):
    def __init__(self, taulell):
        self.taulell=taulell
        
    def creaTauler():
        m=[]
        for i in range(x):
            fila=[]
            for j in range(y):
                    fila.append([False,"~"])
            m.append(fila)
        return m

    def returnTaulell(self):
        return self.taulell