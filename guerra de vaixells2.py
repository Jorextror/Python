import random
def creaTauler():
    x = 10
    y = 10
    m=[]
    for i in range(x):
        fila=[]
        for j in range(y):
            fila.append([False,"~"])
        m.append(fila)
    return m

def imprimeixTauler(m,dev=True):
    fila=" ABCDEFGHIJ"
    for el in fila:
        for el2 in el:
            print(el2,end=' ')
    print()
    for i in range(len(m)):
        print(i,end=' ')
        for j in range(len(m[0])):
            if m[i][j][0]== False and not dev:
                print("·",end=' ')
            else:
                print(m[i][j][1],end=' ')
        print()

def tradueixIndex(fila,columna):
    filas="ABCDEFGHIJ"
    x=fila
    for el in range(len(filas)):
        if filas[el] == columna:
            y=el
    return x,y

def aigua(tauler, fila, columna):
    return tauler[fila][columna][1]=="~"

def comprovaAreaH(m,f,c,mida):
    if c!=0:
        c+=-1
    if f!=0:
        f+=-1
    for i in range(3):
        for j in m[f][c], m[f][mida]:
            print("f:",f,"c:",c,end=" ")
            if j[1]!="~":
                return False
        print()
        f+=1
    return True

def colocaVaixellHoritzontal(m,f,c,mida):
    f,c=tradueixIndex(f,c)
    
    if c+mida>10:
        return False
    else:
        if not comprovaAreaH(m,f,c,mida):
            return False
        
        for i in range(c,c+mida):
            m[f][i][1]="@"
        return True
def colocaVaixellVertical(m,f,c,mida):
    f,c=tradueixIndex(f,c)
    
    if f+mida>10:
        return False
    else:
        if not comprovaAreaH(m,f,c,mida):
            return False
        
        for i in range(f,f+mida):
            m[c][i][1]="@"
        return True
    
def colocaFlota(m, flota):
    for vaixell in flota:
        orientaH=random.randint(0,1)
        filas="ABCDEFGHIJ"
        if orientaH:
            valit=False
            while not valit:
                f=random.randint(0,9)
                c=random.choise(filas)
                valit= colocaVaixellHoritzontal(m,f,c,vaixell)
        else:
            valit=False
            while not valit:
                f=random.randint(0,9)
                c=random.choise(filas)
                valit= colocaVaixellVertical(m,f,c,vaixell)
    
#def tret(tauler,f,c):
    
#def troba1acasellaH(m,x,y):
#def trobaVaixellH(m,x,y):
#def troba1acasellaV(m,x,y):
#def trobaVaixellV(m,x,y):
#def tocatIEnfonsat(m,f,c):
    
#def partidaAcabada(tauler):


tauler=creaTauler()
#imprimeixTauler(tauler)
#fila =input("fila ")
#columna = input("columna ")
# (aigua(tauler,8,0))
#print(comprovaAreaH(tauler,4,4,2))
#print(colocaVaixellHoritzontal(tauler,4,4,2))

if (colocaVaixellHoritzontal(tauler,0,"A",4)):
    imprimeixTauler(tauler)
else:
    print("Coordenades incorrectes")

if (colocaVaixellHoritzontal(tauler,0,"B",4)):
    imprimeixTauler(tauler)
else:
    print("Coordenades incorrectes")

if (colocaVaixellHoritzontal(tauler,0,"F",4)):
    imprimeixTauler(tauler)
else:
    print("Coordenades incorrectes")

if (colocaVaixellHoritzontal(tauler,1,"A",4)):
    imprimeixTauler(tauler)
else:
    print("Coordenades incorrectes")

if (colocaVaixellHoritzontal(tauler,1,"B",4)):
    imprimeixTauler(tauler)
else:
    print("Coordenades incorrectes")

if (colocaVaixellHoritzontal(tauler,1,"F",4)):
    imprimeixTauler(tauler)
else:
    print("Coordenades incorrectes")
    
if (colocaVaixellHoritzontal(tauler,2,"A",4)):
    imprimeixTauler(tauler)
else:
    print("Coordenades incorrectes")
    
if (colocaVaixellHoritzontal(tauler,2,"B",4)):
    imprimeixTauler(tauler)
else:
    print("Coordenades incorrectes")
    
    
if (colocaVaixellHoritzontal(tauler,2,"F",5)):
    imprimeixTauler(tauler)
else:
    print("Coordenades incorrectes")
    
if (colocaVaixellHoritzontal(tauler,9,"A",2)):
    imprimeixTauler(tauler)
else:
    print("Coordenades incorrectes")
    
if (colocaVaixellHoritzontal(tauler,9,"B",4)):
    imprimeixTauler(tauler)
else:
    print("Coordenades incorrectes")
    
if (colocaVaixellHoritzontal(tauler,9,"F",5)):
    imprimeixTauler(tauler)
else:
    print("Coordenades incorrectes")
