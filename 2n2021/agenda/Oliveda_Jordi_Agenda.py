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
from datetime import datetime

class Client:
#  - les dades per un sol client: nom, cognoms, data_naixement, telefon
    def __init__(self,nom,cognoms,data_naixement,telefon):
        self.nom,self.cognoms,self.data_naixement,self.telefon = "","","","",""
        self.dades={}
#  - els mètodes d'entrada: un per a cada atribut
    def inputNom(self,nom):  
        self.nom=nom
    def inputCognoms(self,cognoms):
        self.cognoms=cognoms
    def inputData_naixement(self,data_naixement):
        self.data_naixement=data_naixement
    def inputTelefon(self,telefon):
        self.telefon=telefon
# - els mètodes d'impressió de dades: un per a cada atribut
    def retornaNom(self):  
        return self.nom
    def retornaCognoms(self):  
        return self.cognoms
    def retornaData_naixement(self):  
        return self.data_naixement
    def retornaTelefon(self):  
        return self.telefon
#contigunt de la agenda
    def insertar(self):
        informacion = f'nom: {self.retornaNom(self)}, cognoms: {self.retornaCognoms(self)}, data_naixement: {self.retornaData_naixement(self)}, telefon: {self.retornaTelefon(self)}'
        return informacion
#combrova si arxiu existeix per evitar problemas
def ComprovaArxiu(arxiu):
    try:
        with open (arxiu,"r") as f:
            return True
    except FileNotFoundError:
        return False
#programa principal
if __name__=="__main__":
    c=[]
    menu=0
    while menu != 5:
        menu=int(input("1: Introdueix dades a l'agenda.\n2: Importa agenda de l'arxiu desitjat.\n3: Mostra dades de l'agenda actual.\n4: Exporta l'agenda actual a l'arxiu desitjat.\n5: Sortir\n\nOpcion: "))
        if menu==1:
            #inputs
            try:
                nom = input("Nom: ")
                cognom = input("Cognoms: ")
                data = input("data naixement(DD-MM-YYYY): ")
                datetime.strptime(data, '%d-%m-%Y')
                telefon = input("teléfon: ")
                if len(nom) < 25 and len(nom) > 0 and nom.strip().isalpha():
                    if len(cognom) < 50 and len(cognom) > 0 and cognom.strip().isalpha():
                            if telefon.strip().isdigit():
                                #introduin dades
                                Client.inputNom(Client,nom)
                                Client.inputCognoms(Client,cognom)
                                Client.inputData_naixement(Client,data)
                                Client.inputTelefon(Client,telefon)
                                c.append(Client.insertar(Client))
                            else:
                                print("\n-Telefon no Valida!!")
                    else:
                        print("\n-Cognom no Valida!!")
                else:
                    print("\n-Nom no Valida!!")
            except ValueError:
                print("\n-Entrada no Valida!!")
        elif menu==2:
            arxiu = input("Ruta a arxiu desitjat: ")
            if ComprovaArxiu(arxiu):
                with open (arxiu,"r") as f:
                    c.extend(f.readlines())
            else:
                print("Ruta del arxivo no encontrada")
        elif menu==3:
            for i in c:
                print(i)
        elif menu==4:
            arxiu = input("Ruta a arxiu desitjat: ")
            with open (arxiu,"w") as f:
                f.writelines(c)
        elif menu ==5:
            print("Bona tarde!")
        else:
            print("No es una opcion validad")
        print("-"*30)