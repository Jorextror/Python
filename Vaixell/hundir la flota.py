import random
x = 10
y = 10
lletres=" ABCDEFGHIJ"
flota = [5,4,4,3,3,3,2,2]

def creaTauler():
    m=[]
    for i in range(x):
        fila=[]
        for j in range(y):
                fila.append([False,"~"])
        m.append(fila)
    return m

def imprimeixTauler(m,dev=False):
    print("  ",end=" ")  
    for el in lletres):
        print(lletres[i],end=" ")
    print()

    for j in range(len(m)):
        print(j,end=" ")
        for k in range(len(m[0])):
            if m[j][k][0] == False and not dev:
                print("·",end=" ")
            else:
                print(m[j][k][1],end=" ")   
        print() 

def tradueixIndex(f,c):
    for i in range(len(lletres)):
        if lletres[i]==c:
            return int(f),int(i)

def aigua(m,f,c):
        return m[f][c][1]=="~"

def comprovaAreaH(m,f,c,mida):
    principi=c
    final=mida
    voltes=3
    if c+mida>10:
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

def colocaVaixellHoritzontal(tauler,f,c,mida):
    if comprovaAreaH(tauler,f,c,mida):
      for i in range(c,c+mida):
          tauler[f][i][1]="@"  
    else:
        return False
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

def colocaVaixellVertical(tauler,f,c,mida):
    if comprovaAreaV(tauler,f,c,mida):
      for i in range(f,f+mida):
          tauler[i][c][1]="@"  
    else:
        return False
    return True


def colocaFlota(m,flota):
    for el in flota:
        VvsH=random.randint(0,1)
        i=0
        if VvsH==1 :
            acabat=False
            while not acabat:
                i+=1
                f=random.randint(0,9)
                c=random.choice(lletres)
                T=tradueixIndex(f,c)
                f,c=T
                if aigua(m,f,c):
                    acabat=colocaVaixellHoritzontal(m,f,c,el)
        
        elif VvsH==0:
            acabat=False
            while not acabat:
                f=random.randint(0,9)
                c=random.choice(lletres)
                T=tradueixIndex(f,c)
                f,c=T
                if aigua(m,f,c):
                    acabat=colocaVaixellVertical(m,f,c,el)

def tret(m,f,c):
    m[f][c][0]=True
    if aigua(m,f,c):
        imprimir=("~  "*6)+"\n"+"     AIGUA    "+"\n"+("~  "*6)    
    else:
        if  m[f][c][1]=="X":
            imprimir="Aquesta posició ja ha estat elegida"
        elif m[f][c][1]=="#":
            imprimir="Aquest vaixell ja ha estat enfonsat"
        else:
            m[f][c][1]="X"
            if tocatIEnfonsat(m,f,c):
                imprimir=("=  "*6)+"\n"+"     ENFONSAT    "+"\n"+("=  "*6)
            else:
                imprimir=("-  "*6)+"\n"+"     TOCAT   "+"\n"+("-  "*6)
    print(imprimir)

def troba1acasellaH(m,x,y):
    principi=y
    final=-1
    for i in range(principi,final,-1):
        if m[x][i][1]=="~":
            return x,i+1
        elif i==0:
            return x,i

def trobaVaixellH(m,x,y):
    mida=0
    principi=y
    final=len(m[x])
    for i in range(principi,final):
        print(i,"/",final)
        if m[x][i][1]=="@" or m[x][i][1]=="X":
            mida+=1
        elif m[x][i][1]=="~":
            break
        elif i==final:
            mida+=1
            break
    return x,y,mida

def troba1acasellaV(m,x,y):
    principi=x
    final=-1
    for i in range(principi,final,-1):
        if m[i][y][1]=="~":
            return i+1,y
        elif i==0:
            return i,y

def trobaVaixellV(m,x,y):
    mida=0
    principi=x
    final=len(m[x])
    for i in range(principi,final):
        if m[i][y][1]=="@" or m[i][y][1]=="X" :
            mida+=1
        elif m[i][y][1]=="~":
            break
        elif i==final:
            mida+=1
            break
    return x,y,mida


def orientacio(m,f,c):
    if c==0 and not aigua(m,f,c+1):
        return True
    elif c==9 and not aigua(m,f,c-1):
        return True
    elif (c!=0 and c!=9) and (not aigua(m,f,c-1) or not aigua(m,f,c+1)):
        return True
    return False
        
def tocatIEnfonsat(m,f,c):
    tocats=0
    if orientacio(m,f,c):
        x,y=troba1acasellaH(m,f,c)
        vaixell=trobaVaixellH(m,x,y)
        for i in range (vaixell[1],(vaixell[1]+vaixell[2])):
            print(m[x][i][1])
            if m[x][i][1]=="X":
                tocats+=1
        if tocats==vaixell[2]:
            for i in range (vaixell[1],(vaixell[1]+vaixell[2])):
                m[x][i][1]="#"
            return True
        else:
            return False
    else:
        x,y=troba1acasellaV(m,f,c)
        vaixell=trobaVaixellV(m,x,y)
        for i in range (vaixell[0],(vaixell[0]+vaixell[2])):
            if m[i][y][1]=="X":
                tocats+=1
        if tocats==vaixell[2]:
            for i in range (vaixell[0],(vaixell[0]+vaixell[2])):
                m[i][y][1]="#"
            return True
        else:
            return False

def partidaAcabada(m):
    Quantitat=0
    for fila in m:
        for el in fila:
            if el[1]=="#":
                Quantitat+=1
    return Quantitat==sum(flota)


m=creaTauler()
colocaFlota(m,flota)
while partidaAcabada(m) is not True:
    imprimeixTauler(m)
    print("Coordenades del tret")
    f=input("Fila: ")
    c=input("Columna: ")
    T=tradueixIndex(f,c)
    f,c=T
    tret(m,f,c)
imprimeixTauler(m)
imprimir=("$  "*6)+"\n"+"\tGOOD ENDING \n YOU WON    "+"\n"+("$  "*6)    
print(imprimir)