#Joel Farell i Jordi Oliveda
import os
directori="E:/Documentos/python/2n2021/ProyectoReproductorMp3"
albums={}

class album:
    def __init__(self,ruta,cançons,genere,any,autor,numero_cops):
        self.ruta,self.cançons,self.genere,self.any,self.autor,self.numero_cops=ruta,cançons,genere,any,autor,numero_cops
    
    def mostra(self):
        return self.ruta,self.cançons,self.genere,self.any,self.autor,self.numero_cops
    
    def get_cançons(self):
        return self.cançons

    def set_cançons(self,new_cançons):
        self.cançons=new_cançons

    def set_numero_cops(self,new_numero_cops):
        self.numero_cops=new_numero_cops
    
    def get_numero_cops(self):
        return self.numero_cops

#comprovem si hi ha algun error a l'arxiu
def ComprovaArchiu(Arxiu):
    try:
        with open (Arxiu,"r") as f:
            return True
    except FileNotFoundError:
        return False

def init_dir():
    for base, dirs, files in os.walk(directori+'/music'):#"base" Recorre els directoris, "files" els arxius. De la ruta amb walk
        if files:
            song=[file for file in files if file.split(".")[1]=="mp3"]#Un list comprencion de tots els arxius amb un split per identificar l'extensió mp3
            if ComprovaArchiu(base+"/info.txt"):
                with open (base+"/info.txt","r") as f:
                    info=f.read()
                    albums[base]=album(base,song,info.split(":")[0],info.split(":")[2],info.split(":")[1],0)#Creem en un diccionari, la clau és la ruta del album per si hi ha dos àlbums iguals. split de ":" perquè està separat amb ":" en info.txt
    with open (directori+"/music/backups.txt","w") as f:
        f.writelines(" : ".join(['{0} : {1}'.format(key,albums[key].mostra()) for key in albums]))#guardem el diccionari

def init():
    if ComprovaArchiu(directori+"/backups.txt"):
        with open (directori+"/backups.txt","r") as f:
            text=f.read()
            list=text.split(":")
            for i in range(len(list)):
                if i%2!=0:
                    info=list[i].split(",")
                    albums[list[i-1]]=album(info[0],info[1].split("|"),info[2],info[3],info[4],info[5])
    #Mira al fitxer de l'estat que s'ha quedat al tancar el programa
    if ComprovaArchiu(directori+"/estat_reproductor.txt"):
        with open (directori+"/estat_reproductor.txt","r") as f:
            info=f.readlines()#Oh llegeix per línies, la primera per la cançó la segona pel percentatge de volum
            os.system("mpc add directori"+'/'+info[0])
            os.system('mpc seek'+info[1].split("(")[1].replace(")",""))
            os.system("mpc volume 30")

def Play_Pause():
    os.system("mpc toggle")

def Next():
    os.system("mpc next")

def Anterior():
    os.system("mpc prev")

def ValumeMas():
    os.system("mpc volume + 5")

def ValumeMenos():
    os.system("mpc volume - 5")

def Editar_albums():
    print("|".join([el.split("/")[-1] for el in albums.keys()]))#Per mostrar els àlbums fem el split per "/" i mostrem l'última posició de ñes keys que son el path del directori
    albu=input("Quin album vols editar? ")
    for key in albums:
        if key.split("/")[-1].lower()==albu.lower():
            opcio=input("1. Afegir cançons\n2. Eliminar cançons\n")
            if opcio==1:
                path=input("Direcció de cançó a afegir: ")
                os.system("mv"+path+" "+directori+"/music/album2/album6")
                reset()
            elif opcio==2:
                print("\n".join(albums[key].get_cançons()))
                cancion=input("Cançó a eliminar: ")
                llistaSongs=albums[key].get_cançons()
                if cancion in llistaSongs:
                    llistaSongs.remove(cancion)
                    albums[key].set_cançons(llistaSongs)
                else:
                    print("Cançó no existent")

def Reproduir():
    os.system("mpc ls "+directori+"/playlist")
    num=int(input("Quin vols reproduir?(número) "))
    os.system("mcp play "+num-1)

def crear_llistes(param):
    if param==1:
        genero=input("Genere: ")
        for key in albums:
            if albums[key].genere.lower() == genero.lower():#filtre per genere
                albums[key].set_numero_cops(albums[key].get_numero_cops()+1)#Actualitza el album, afegint-hi +1 al contador de cops de reproducció
                for cancion in albums[key].cançons:
                    os.system("mpc add "+albums[key].ruta+"/"+cancion)#crea la playlist
        os.system("mpc save "+genero)
            
    elif param==2:
        autor=input("Autor: ")
        for key in albums:
            if albums[key].autor.lower() == autor.lower():
                albums[key].set_numero_cops(albums[key].get_numero_cops()+1)
                for cancion in albums[key].cançons:
                    os.system("mpc add "+albums[key].ruta+"/"+cancion)
        os.system("mpc save "+autor)
            
    elif param==3:
        anys=input("Anys: ")
        for key in albums:
            if int(albums[key].any) >= int(anys.split(" ")[0]) and int(albums[key].any) <= int(anys.split(" ")[1]):
                albums[key].set_numero_cops(albums[key].get_numero_cops()+1)
                for cancion in albums[key].cançons:
                    os.system("mpc add "+albums[key].ruta+"/"+cancion)
        os.system("mpc save "+"_".join(anys.split(" ")))
    
    elif param==4:
        cops=input("Cops: ")
        for key in albums:
            if int(albums[key].numero_cops) >= int(cops.split(" ")[0]) and int(albums[key].numero_cops) <= int(cops.split(" ")[1]):
                albums[key].set_numero_cops(albums[key].get_numero_cops()+1)
                for cancion in albums[key].cançons:
                    os.system("mpc add "+albums[key].ruta+"/"+cancion)
        os.system("mpc save "+"_".join(cops.split(" ")))
    else:
        print("no existeis la opcio")

def sortir():
    text="mpc status"+' > '+directori+"estat_reproductor.txt"
    os.system(text)
    init_dir()
    
def reset():
    os.system("rm -r "+directori+"/playlist/")
    init_dir()
    os.system("/etc/init.d/mpd restart")
    os.system("mpc update")
    init()

def programa_principal(menu):
    if menu == 1:
        Play_Pause()
    elif menu ==2:
        Next()
    elif menu==3:
        Anterior()
    elif menu==4:
        ValumeMas()
    elif menu==5:
        ValumeMenos()
    elif menu==6:
        Editar_albums()
    elif menu==7:
        Reproduir()
    elif menu==8:
        menu8=int(input("Crear llistes de reproducció segons :\n1. Génere.\n2. Autor.\n3. Interval anys.\n4. Cops que s'ha reproduït l'album\n"))
        crear_llistes(menu8)
    elif menu==9:
        sortir()
    elif menu==10:
        reset()

if __name__=="__main__":
    init()
    menu=0
    while menu != 9:
        try:
            menu=int(input("1. Reproduir/pausar.\n2. Cançó següent.\n3. Cançó anterior.\n4. Augmentar volum.\n5. Disminuir volum.\n6. Editar àlbums. Afegir o eliminar cançons\n7. Reproduir una llista de reproducció.\n8. Crear llistes de reproducció\n9. Sortir.\n10.Reset.\n"))
            programa_principal(menu)
        except ValueError:
            print("Entrada no valida")
        except:
            print("Error desconegut")
            reset()
    sortir()