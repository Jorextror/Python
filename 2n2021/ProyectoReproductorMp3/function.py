#Joel Farell i Jordi Oliveda
import os
<<<<<<< HEAD
directori="2n/MP03/Projecte-UF2"
=======
#ruta del directori del programa
directori="/home/joel/Escritorio/python/2n/MP03/Projecte-UF2"
>>>>>>> bd80f65d237f5f2b944e060df344ddd1cb5bb700
albums={}

class album:
    def __init__(self,ruta,cançons,genere,any,autor,numero_cops):
        self.ruta,self.cançons,self.genere,self.any,self.autor,self.numero_cops=ruta,cançons,genere,any,autor,numero_cops
    def mostra(self):
        return ",".join((self.ruta,"|".join(self.cançons),self.genere,str(self.any),self.autor,str(self.numero_cops)))
    
    def get_cançons(self):
        return self.cançons

    def set_cançons(self,new_cançons):
        self.cançons=new_cançons

    def get_numero_cops(self):
        return self.numero_cops

    def set_numero_cops(self,new_numero_cops):
        self.numero_cops=new_numero_cops
    

#comprovem si hi ha algun error a l'arxiu
def ComprovaArchiu(Arxiu):
    try:
        with open (Arxiu,"r") as f:
            return True
    except FileNotFoundError:
        return False

def init_dir():
    for base, dirs, files in os.walk(directori+'/music',topdown=True):#"base" Recorre els directoris, "files" els arxius. De la ruta amb walk
        if files:
            song=[file for file in files if file.split(".")[1]=="mp3"]#Un list comprension de tots els arxius amb un split per identificar l'extensió mp3
            if ComprovaArchiu(base+"/info.txt"):
                with open (base+"/info.txt","r") as f:
                    info=f.read()
                    albums[base]=album(base,song,info.split(":")[0],info.split(":")[2],info.split(":")[1],0)#Creem en un diccionari, la clau és la ruta del album per si hi ha dos àlbums iguals. split de ":" perquè està separat amb ":" en info.txt
    with open (directori+"/backups.txt","w") as f:
        f.writelines(":".join(['{0}:{1}'.format(key,albums[key].mostra()) for key in albums]))#guardem el diccionari

def init():
    if ComprovaArchiu(directori+"/backups.txt"):
        with open (directori+"/backups.txt","r") as f:
            text=f.read()
            list=text.split(":")
            for i in range(len(list)):
                if i%2!=0:
                    info=list[i].split(",")
                    albums[list[i-1]]=album(info[0],info[1].split("|"),info[2],int(info[3]),info[4],int(info[5]))
    #Mira al fitxer de l'estat que s'ha quedat al tancar el programa
    if ComprovaArchiu(directori+"/estat_reproductor.txt"):
        with open (directori+"/estat_reproductor.txt","r") as f:
            info=f.readlines()#Oh llegeix per línies, la primera per la cançó la segona pel percentatge de volum
            if len(info)>1:
                os.system("mpc add "+directori+'/music/'+info[0])
                os.system('mpc seek '+info[1].split("(")[1].replace(")",""))
                os.system("mpc volume 30")
    return albums

def Play_Pause():
    os.system("mpc toggle")

def Next():
    os.system("mpc next")

def Anterior():
    os.system("mpc prev")

def ValumeMas():
    os.system("mpc volume +5")

def ValumeMenos():
    os.system("mpc volume -5")

<<<<<<< HEAD
def Reproduir(nom):
    os.system("mpc load "+nom)

def crear_llistes(param,songs=[],pers=False):
    #Passem per parámetre una llista de totes les cançóns que volem afegir a la llista de reproducció 
    #Si pers no es fals, es creará una llista de reproducció per: génere,autor,anys o vegades de reproducció
    os.system("mpc clear")
    if not pers:
        if param[0]=="genere":
            for key in albums:
                if albums[key].genere.lower() == param[1].lower():#filtre per genere
                    albums[key].set_numero_cops(albums[key].get_numero_cops()+1)#Actualitza el album, afegint-hi +1 al contador de cops de reproducció
                    for cancion in albums[key].cançons:
                        os.system("mpc add "+key+"/"+cancion)#crea la playlist
            os.system("mpc save "+param[1])
        elif param[0]=="autor":
            for key in albums:
                if albums[key].autor.lower() == param[1].lower():
                    albums[key].set_numero_cops(albums[key].get_numero_cops()+1)
                    for cancion in albums[key].cançons:
                        os.system("mpc add "+albums[key].ruta+"/"+cancion)
            os.system("mpc save "+param[1])
                
        elif param[0]=="anys":
            for key in albums:
                if int(albums[key].any) >= int(param[1][0]) and int(albums[key].any) <= int(param[1][1]):
                    albums[key].set_numero_cops(albums[key].get_numero_cops()+1)
                    for cancion in albums[key].cançons:
                        os.system("mpc add "+albums[key].ruta+"/"+cancion)
            os.system("mpc save "+"_".join(param[1]))
        
        elif param[0]=="cops":
            cops=input("Cops: ")
            for key in albums:
                if int(albums[key].numero_cops) >= int(cops.split(" ")[0]) and int(albums[key].numero_cops) <= int(cops.split(" ")[1]):
                    for cancion in albums[key].cançons:
                        os.system("mpc add "+albums[key].ruta+"/"+cancion)
            os.system("mpc save "+"_".join(cops.split(" ")))
        else:
            print("no existeix la opcio")

def sortir():
    text="mpc status"+' > '+directori+"/estat_reproductor.txt"
    #os.system(text)
=======
#crar llistas de reproducció segons pel que es pasa per parámatre
#@param tupla on la posicio 0 és el tipus de llista de reproducció i
#la posició 1 és la caracteristica especifica per la creacio de la llista 
def crear_llistes(param):
    os.system("mpc clear")
    if param[0]=="genere":
        for key in albums:
            if albums[key].genere.lower() == param[1].lower():#filtre per genere
                albums[key].set_numero_cops(albums[key].get_numero_cops()+1)#Actualitza el album, afegint-hi +1 al contador de cops de reproducció
                for cancion in albums[key].cançons:
                    os.system("mpc add "+key+"/"+cancion)#crea la playlist
        os.system("mpc save "+param[1])
    elif param[0]=="autor":
        for key in albums:
            if albums[key].autor.lower() == param[1].lower():
                albums[key].set_numero_cops(albums[key].get_numero_cops()+1)
                for cancion in albums[key].cançons:
                    os.system("mpc add "+albums[key].ruta+"/"+cancion)
        os.system("mpc save "+param[1])
            
    elif param[0]=="anys":
        for key in albums:
            if int(albums[key].any) >= int(param[1][0]) and int(albums[key].any) <= int(param[1][1]):
                albums[key].set_numero_cops(albums[key].get_numero_cops()+1)
                for cancion in albums[key].cançons:
                    os.system("mpc add "+albums[key].ruta+"/"+cancion)
        os.system("mpc save "+"_".join(param[1]))
    
    elif param[0]=="cops":
        cops=param
        for key in albums:
            if int(albums[key].numero_cops) >= int(cops[1][0]) and int(albums[key].numero_cops) <= int(cops[1][1    ]):
                for cancion in albums[key].cançons:
                    os.system("mpc add "+albums[key].ruta+"/"+cancion)
        os.system("mpc save "+"_".join(cops[1]))
    else:
        print("no existeix la opcio")

def sortir():
    text="mpc status"+' > '+directori+"/estat_reproductor.txt"
>>>>>>> bd80f65d237f5f2b944e060df344ddd1cb5bb700
    init_dir()
    
def reset():
    os.system("rm -r "+directori+"/playlist/*")
    init_dir()
    os.system("/etc/init.d/mpd restart")
    os.system("mpc update")
    init()

<<<<<<< HEAD
def aggregate(path,path_album):
    os.system("mv "+path+" "+path_album)
=======
#pasem el path origen de la canço i al desti amb el cp ho copiem
def aggregate(path,path_album):
    os.system("cp "+path+" "+path_album)

#pasem el path de la canço per eliminar-lo
def deleteSong(path):
    os.system("rm "+path)
    
#rerodueix la lista de cançons pasades per parámetre
def carrega(list):
    print(list)
    os.system("mpc load "+list)
>>>>>>> bd80f65d237f5f2b944e060df344ddd1cb5bb700
