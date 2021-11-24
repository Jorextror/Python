#Joel Farell i Jordi Oliveda
import os

def Play_Pause():
    os.system("mpc toggle")

def Next():
    os.system("mpc next")

def Anterior():
    os.system("mpc prev")

def ValumeMas(num):
    os.system("mpc volume + ".num)

def ValumeMenos(num):
    os.system("mpc volume - ".num)

if __name__=="__main__":
    menu=0
    while menu != 9:
        try:
            menu=int(input("1. Reproduir/pausar.\n2. Cançó següent.\n3. Cançó anterior.\n4. Augmentar volum.\n5. Disminuir volum.\n6. Editar àlbums. Afegir o eliminar cançons\n7. Reproduir una llista de reproducció.\n8. Crear llistes de reproducció\n9. Sortir.\n10.Reset.\n"))
        except ValueError:
            print("Entrada no valida")
        except:
            print("Error desconegut")
