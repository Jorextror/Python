# Dissenyeu una aplicació anomenada cognom_nom_agenda.py que permeti entrar dades de clients en una agenda, 
# mostrar-les i enregistrar-les en un arxiu (amb el format que vulgueu). 
# Cal verificar que totes les dades entrades tinguin el format i la longitud correctes.

# Crea una classe Client que contingui:
#  - les dades per un sol client: nom, cognoms, data_naixement, telefon
#  - els mètodes d'entrada: un per a cada atribut
#  - els mètodes d'impressió de dades: un per a cada atribut

# L'aplicació principal ha de mostrar el següent menú:
# 1: Introdueix dades a l'agenda.
# 2: Importa agenda de l'arxiu desitjat.
# 3: Mostra dades de l'agenda actual.
# 4: Exporta l'agenda actual a l'arxiu desitjat.
# 5: Sortir

class agenda(object):
    def __init__(self,nom, cognoms, data_naixement, telefon):
        self.nom= nom
    def modificar(self,valor):
        self.modificar=valor
    alumnes=["pep","joan","jordi"]
    d={}
    for x in alumnes:
        # <object type agenda>
        aa=agenda("nom","ol")
        d[x]=aa
        print aa,mavaa

class Client(object):

if __name__=="__main__":
    while menu != 5:
        menu=input("1: Introdueix dades a l'agenda.\n2: Importa agenda de l'arxiu desitjat.\n3: Mostra dades de l'agenda actual.\n4: Exporta l'agenda actual a l'arxiu desitjat.\n5: Sortir\n")
    