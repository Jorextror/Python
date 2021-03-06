#Jordi Olivceda i Kevin Moya
import random

# Variables Globals
x = 10
y = 10
index="ABCDEFGHIJ"
flota = [5,4,4,3,3,3,2,2]
acabada=0

def creaTauler():
    # Variable local
    m=[]
    for i in range(x): # De cada volta mira el valor de x i amb el valor de i afegeix una tupla
        fila=[]
        for j in range(y):
                fila.append([False,"~"])
        m.append(fila)
    return m

def imprimeixTauler(m,dev=False):
    print(" ",end=" ")  
    for el in index: # Passa de cada element les lletres que equivalen a les columnes
        for el2 in el:
            print(el2,end=' ')
    print()

    for i in range(len(m)): # Mira el rang de la mida de la matriu
        print(i,end=' ')
        for j in range(len(m[0])): # Mira si imprimeix la posició de la tupla a on està el valor de True o False 
            if m[i][j][0]== False and not dev:
                print("·",end=' ')
            else:
                print(m[i][j][1],end=' ')
        print()

def tradueixIndex(f,c):
    for i in range(len(index)): # Rang de la mida de les columnes
        if index[i]==c: # Tradueix l'índex fila/columna
            return int(f),int(i)

def aigua(tauler,fila,columna):
    return tauler[fila][columna][1]=="~" # Comprova si en el tauler, en la fila de la columna en la posició 1 és aigua

def comprovaAreaH(m,f,c,mida): # Comproba el ariea en horitzontal, mirant que no pasi fora del tauler 
    inici=c
    fi=mida
    cops=3
    if c+mida>10:
        return False
    if c+mida<=9:
        fi=mida+1
    else:
        fi=mida
    if f!=0:
        f-=1
    else:
        cops=2
    if c!=0:
        inici=c-1
    for i in range(cops):
        for j in range(inici,c+fi):
            if m[f][j][1]!="~":
                return False
        f+=1
        if f>=10:
            return True
    return True

def colocaVaixellHoritzontal(m,f,c,mida): # Col·loca el vaixell en horitzontal. Si es pot col·locar el vaixell retorna true
    if comprovaAreaH(m,f,c,mida):
      for i in range(c,c+mida):
          m[f][i][1]="@"  
    else:
        return False
    return True

def comprovaAreaV(m,f,c,mida):  # Comprova l'àrea en vertical, mirant que no passi fora del tauler
    if f+mida>9:
        return False
    if c!=0:
        iniciV=c-1
    else:
        iniciV=c
    if iniciV+2<=9:
        fiV=c+2
    else:
        fiV=c+1
    if f!=0:
        inici=f-1
    else:
        inici=f
    if f+mida<=9:
        fi=f+mida+1
    else:
        fi=f+mida
    for i in range(inici,fi):
        for j in range(iniciV,fiV):
            if m[i][j][1]!="~":
                return False
    return True

def colocaVaixellVertical(m,f,c,mida):  # Col·loca el vaixell en horitzontal. Si es pot col·locar el vaixell retorna true
    if comprovaAreaV(m,f,c,mida):
      for i in range(f,f+mida):
          m[i][c][1]="@"  
    else:
        return False
    return True

def colocaFlota(m,flota):  # Genera aleatòriament si és horitzontal o vertical amb un booleà
    for el in flota:
        orientacio=random.randint(0,1)
        if orientacio==1 : # Si el valor booleà és 1, equival a horitzontal
            valit=False
            while not valit: 
                f=random.randint(0,9)
                c=random.choice(index)
                f,c=tradueixIndex(f,c)
                if aigua(m,f,c): # Continuarà el bucle fins que vàlid sigui true
                    valit=colocaVaixellHoritzontal(m,f,c,el)
        
        elif orientacio==0:  # Si el valor booleà és 0, equival a vertical
            valit=False
            while not valit:
                f=random.randint(0,9)
                c=random.choice(index)
                f,c=tradueixIndex(f,c)
                if aigua(m,f,c):
                    valit=colocaVaixellVertical(m,f,c,el)

def tret(m,f,c):
    m[f][c][0]=True # Mostra el valor que anteriorment era ocult
    if aigua(m,f,c):
        print(8*"~ ","\n     AIGUA    \n"+8*"~ ")    
    else:
        m[f][c][1]="X"
        if tocatIEnfonsat(m,f,c): # 
            global acabada
            acabada+=1
            print(14*"= ","\n    TOCAT I ENFONSAT   \n"+14*"= ")
        else:
            print(8*"- ","\n     TOCAT   \n"+8*"- ")

def troba1acasellaH(m,x,y):
    inici=y
    fi=-1
    for i in range(inici,fi,-1):
        if m[x][i][1]=="~":
            return x,i+1
        elif i==0:
            return x,i

def trobaVaixellH(m,x,y):
    mida=0
    inici=y
    fi=len(m[x])
    for i in range(inici,fi):
        if m[x][i][1]=="@" or m[x][i][1]=="X":
            mida+=1
        elif m[x][i][1]=="~":
            return x,y,mida
        elif i==fi:
            mida+=1
            return x,y,mida
    return x,y,mida

def troba1acasellaV(m,x,y):
    inici=x
    fi=-1
    for i in range(inici,fi,-1):
        if m[i][y][1]=="~":
            return i+1,y
        elif i==0:
            return i,y

def trobaVaixellV(m,x,y):
    mida=0
    inici=x
    fi=len(m[x])
    for i in range(inici,fi):
        if m[i][y][1]=="@" or m[i][y][1]=="X":
            mida+=1
        elif m[i][y][1]=="~":
            return x,y,mida
        elif i==fi:
            mida+=1
            return x,y,mida
    return x,y,mida

def tocatIEnfonsat(m,f,c): # Comprova l'orientació del vaixell amb la posició inicial i els voltants del vaixell
    impacte=0
    orientacio= False
    if c==0 and not aigua(m,f,c+1): 
        orientacio = True
    elif c==9 and not aigua(m,f,c-1):
        orientacio = True
    elif (c!=0 and c!=9) and (not aigua(m,f,c-1) or not aigua(m,f,c+1)):
        orientacio = True

    if orientacio:
        x,y=troba1acasellaH(m,f,c)
        fila,columna,mida=trobaVaixellH(m,x,y)
        for i in range(columna,(columna+mida)):
            if m[x][i][1]=="X":
                impacte+=1
        if impacte==mida:
            for i in range (columna,(columna+mida)):
                m[x][i][1]="#"
            return True
        else:
            return False
    else:
        x,y=troba1acasellaV(m,f,c)
        fila,columna,mida=trobaVaixellV(m,x,y)
        for i in range(fila,(fila+mida)):
            if m[i][y][1]=="X":
                impacte+=1
        if impacte==mida:
            for i in range(fila,(fila+mida)):
                m[i][y][1]="#"
            return True
        else:
            return False

print("\n  Guerra de Vaixells\n")
m=creaTauler()
colocaFlota(m,flota)
fiPartida=False
while fiPartida is not True:
    imprimeixTauler(m)
    f=input("Fila (0-9): ")
    c=input("Columna (A-J): ")
    f,c=tradueixIndex(f,c)
    tret(m,f,c)
    if acabada == len(flota):
        fiPartida=True
imprimeixTauler(m)
print(14*"W "+"\n"+"\t Enorabuena! "+"\n"+14*"W ")