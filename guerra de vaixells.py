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
    principi=c
    final=mida
    voltes=3
    if c+mida>=9:
        return False
    if c+mida<=9:
        final=mida+1
    else:
        final=mida
    if f!=0:
        f-=1
    else:
        voltes=2
    if c!=0:
        principi=c-1
    for i in range(voltes):
        for j in range(principi,c+final):
            if m[f][j][1]!="~":
                return False
        f+=1
        if f>=10:
            return True
    return True


def colocaVaixellHoritzontal(m,f,c,mida):
    f,c=tradueixIndex(f,c)
    

    if not comprovaAreaH(m,f,c,mida):
        return False
    else:
        for i in range(c,c+mida):
            m[f][i][1]="@"
    return True
    
def comprovaAreaV(m,f,c,mida):
    if f+mida>9:
        return False
    if c!=0:
        voltesP=c-1
    else:
        voltesP=c

    if voltesP+2<=9:
        voltesF=c+2
    else:
        voltesF=c+1
    if f!=0:
        principi=f-1
    else:
        principi=f
    if f+mida<=9:
        final=f+mida+1
    else:
        final=f+mida
    for i in range(principi,final):
        for j in range(voltesP,voltesF):
            if m[i][j][1]!="~":
                return False
    return True

def colocaVaixellVertical(m,f,c,mida):
    f,c=tradueixIndex(f,c)
    

    if not comprovaAreaH(m,f,c,mida):
        return False
    else:
        for i in range(f,f+mida):
            m[i][c][1]="@"
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
#(tradueixIndex(8,'B'))
#(aigua(tauler,8,0))
#print(comprovaAreaH(tauler,4,4,2))
#print(colocaVaixellHoritzontal(tauler,4,4,2))

if (colocaVaixellVertical(tauler,0,"A",4)):
    imprimeixTauler(tauler)
else:
    print("Coordenades incorrectes")

if (colocaVaixellVertical(tauler,1,"A",4)):
    imprimeixTauler(tauler)
else:
    print("Coordenades incorrectes")

if (colocaVaixellVertical(tauler,6,"A",4)):
    imprimeixTauler(tauler)
else:
    print("Coordenades incorrectes")

if (colocaVaixellVertical(tauler,0,"B",4)):
    imprimeixTauler(tauler)
else:
    print("Coordenades incorrectes")

if (colocaVaixellVertical(tauler,1,"B",4)):
    imprimeixTauler(tauler)
else:
    print("Coordenades incorrectes")

if (colocaVaixellVertical(tauler,6,"B",4)):
    imprimeixTauler(tauler)
else:
    print("Coordenades incorrectes")
    
if (colocaVaixellVertical(tauler,0,"C",4)):
    imprimeixTauler(tauler)
else:
    print("Coordenades incorrectes")
    
if (colocaVaixellVertical(tauler,1,"C",4)):
    imprimeixTauler(tauler)
else:
    print("Coordenades incorrectes")
    
    
if (colocaVaixellVertical(tauler,6,"C",5)):
    imprimeixTauler(tauler)
else:
    print("Coordenades incorrectes")
    
if (colocaVaixellVertical(tauler,0,"J",2)):
    imprimeixTauler(tauler)
else:
    print("Coordenades incorrectes")
    
if (colocaVaixellVertical(tauler,1,"J",4)):
    imprimeixTauler(tauler)
else:
    print("Coordenades incorrectes")
    
if (colocaVaixellVertical(tauler,6,"J",5)):
    imprimeixTauler(tauler)
else:
    print("Coordenades incorrectes")