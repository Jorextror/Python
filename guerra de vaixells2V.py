import random
#Constants
x = 10
y = 10
lletres=["A","B","C","D","E","F","G","H","I","J"]
flota = [5,4,4,3,3,3,2,2]

def creaTauler():
    m=[]
    for i in range(x):
        fila=[]
        for j in range(y):
                fila.append([False,"~"])
        m.append(fila)
    return m

def imprimeixTauler(m,dev=True):
    s= " "
    print("  ",end="")  
    for i in range(len(m)):
        print(lletres[i],end=s)
    print()

    for j in range(len(m)):
        print(j,end=s)
        for k in range(len(m[0])):
            if m[j][k][0] == False and not dev:
                print("·",end=s)
            else:
                print(m[j][k][1],end=s)   
        print() 

def tradueixIndex(f,c):
    for i in range(len(lletres)):
        if lletres[i]==c:
            return f,i

def aigua(m,f,c):
    if m[f][c][1]=="~":
        return True

def comprovaAreaH(m,f,c,mida):
    principi=c
    final=mida
    voltes=3
    if c+mida>10:
        return False
    if c+mida<8:
        final=mida+1
    if f!=0:
        f-=1
    else:
        voltes=2
    if c!=0:
        principi=c-1
    for i in range(voltes):
        print("mida: ",principi,"-",c+final)
        for i in range(principi,c+final):
            print(m[f][i][1])
            if m[f][i][1]!="~":
                return False
        f+=1
        if f==10:
            return True
    return True

def colocaVaixellHoritzontal(tauler,f,c,mida):
    f,c=tradueixIndex(f,c)
    if comprovaAreaH(tauler,f,c,mida):
      for i in range(c,c+mida):
          tauler[f][i][1]="@"  
    else:
        return False
    return True
"""
def comprovaAreaV(m,f,c,mida):
    principi=f
    final=mida
    voltes=3
    if f+mida>10:
        return False
    if f+mida<8:
        final=mida+1
    if c!=0:
        c-=1
    else:
        voltes=2
    if f!=0:
        principi=f-1
    for i in range(voltes):
        for i in range(principi,f+final):
            print("f:",f,"c:",c,end=" ")
            print(m[c][i][1])
            if m[c][i][1]!="~":
                return False
        print()
        c+=1
        if c==10:
            return True
    return True
"""
def comprovaAreaV(m,f,c,mida):
    principi=f
    final=mida
    if f+mida>10:
        return False
    if f+mida<9:
        final=mida+1

    if f!=0:
        principi=f-1
    if c!=0:
        x=c-1
    else:
        x=c
    if c+3>9:
        y=c+2
    for i in range(c,final):
        print("mida: ",principi,"-",f+final)
        for j in range(principi,f+final):
            print(m[i][j][1])
            if m[i][j][1]!="~":
                return False
        c+=1
        if f==10:
            return True
    return True

def colocaVaixellVertical(tauler,f,c,mida):
    f,c=tradueixIndex(f,c)
    if comprovaAreaV(tauler,f,c,mida):
      for i in range(f,f+mida):
          tauler[i][c][1]="@"  
    else:
        return False
    return True
"""
def colocaFlota(m,flota):
    AvsH=random.randint(0,1)
    for el in flota:
        if AvsH==1 :
            acabat=False
            while not acabat:
                f=random.randint(0,9)
                c=random.choice(lletres)
                T=tradueixIndex(f,c)
                f,c=T
                print(f,c)
                if aigua(m,f,c):
                    acabat=colocaVaixellHoritzontal(m,f,c,el)
        
        elif AvsH==0:
            acabat=False
            while not acabat:
                f=random.randint(0,9)
                c=random.choice(lletres)
                T=tradueixIndex(f,c)
                f,c=T
                print(f,c)
                if aigua(m,f,c):
                    acabat=colocaVaixellVertical(m,f,c,el)
"""
m=creaTauler()
tauler=m
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
#colocaFlota(m,flota)

