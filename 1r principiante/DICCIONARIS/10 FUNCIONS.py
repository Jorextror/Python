"""Jordi Oliveda
1r-ASIX-MP3-UF2-FUNCIONS
"""
def Multiplica(num1,num2):
    multi= num1 * num2
    print(multi)
    
def Anys2000():
    anys=int(input("any actual: "))
    x= anys - 2000
    print("Des del 2000 han passat", x ,"anys")

def tiquetFruita():
    fruites = {
    "pomes     ": 1.60,
    "peres     ": 2.10,
    "mandarines": 3.20,
    "maduixes  ": 5.10,
    "taronges ": 2.50
    } 
    tiquet =  "\n\nLa Fruiteria: Tiquet de Compra"
    tiquet += "\n======================================\n"

    total = 0
    items = 0
    for fruita in fruites:
      pes = float(input("Introdueix el pes de la fruita "+fruita+ " en kg (format n.n): "))
      if pes > 0:
        tiquet += fruita + "\t : \t" + str(fruites[fruita]) + "€/kg\t => \t" + "{:.2f}".format(fruites[fruita] * pes) +"€\n"
        total += fruites[fruita] * pes
        items +=1

    print(tiquet)
    print("========================================")
    print("Import total :\tnum ítems",items,"\t","{:.2f}".format(total),"€" )

def NotaUF():
    literal = ["S","S","S","S","S","A","B","N","N","E","E",]
    notaEx =float(input("Nota de Examen: "))
    notaPr =float(input("Nota de Practica: "))
    if notaEx > 4 and notaPr > 4:
        notaMo= (70 / 100 * notaEx) + (30 / 100 * notaPr)
        notaMo= int(notaMo)
        if notaMo == 5:
            print("5 Aprovat")
        elif notaMo == 6:
            print("6 Bé")
        elif notaMo == 7 or notaMo == 8:
            print(notaMo ,"Notable")
        elif notaMo == 9 or notaMo == 10:
            print(notaMo,"Excel·lent")
    else:
        pernill = input("has comprat un pernil al professor/a?(S/N) ")
        if pernill == "S":
            print("aprovat perniler")
            
print("\tFuncions 1\n",20*"=","\n1. Multiplica\n2. Anys 2000\n3. Factura\n4. Nota UF\n5. SORTIR")
opcio="0"
while opcio != "5":
    opcio = input("opcio(1-5) ")
    if opcio == "1":
        num1 = int(input("num1"))
        num2 = int(input("num2"))
        Multiplica(num1,num2)

    elif opcio == "2":
        Anys2000()
        
    elif opcio == "3":
        tiquetFruita()
        
    elif opcio == "4":
        NotaUF()
        
    elif opcio == "5":
        print("Bye")
    else:
        print("opcio incorrecta")
