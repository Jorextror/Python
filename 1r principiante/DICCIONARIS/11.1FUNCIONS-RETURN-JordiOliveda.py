"""
Modifica l’exercici anterior substituint els prints per returns:
"""
def multiplica(num1,num2):
    return num1 * num2
    
def Anys2000():
    anys=int(input("any actual: "))
    return anys - 2000
    
def NotaUF():
    notaEx =float(input("Nota de Examen: "))
    notaPr =float(input("Nota de Practica: "))
    if notaEx > 4 and notaPr > 4:
        notaMo= (70 / 100 * notaEx) + (30 / 100 * notaPr)
        notaMo= int(notaMo)
        if notaMo == 5:
            return "Aprovat"
        elif notaMo == 6:
            return "Bé"
        elif notaMo == 7 or notaMo == 8:
            return "Notable"
        elif notaMo == 9 or notaMo == 10:
            return "Excel·lent"
    else:
        pernill = input("has comprat un pernil al professor/a?(S/N) ")
        if pernill == "S" or pernill == "s":
            return "aprovat perniler"
            
print("\tFuncions 1\n",20*"=","\n1. Multiplica\n2. Anys 2000\n3. Nota UF\n4. SORTIR")
opcio="0"
while opcio != "4":
    opcio = input("opcio(1-4) ")
    if opcio == "1":
        num1 = int(input("num1"))
        num2 = int(input("num2"))
        print(multiplica(num1,num2))
        
    elif opcio == "2":
        print("Des del 2000 han passat", Anys2000() ,"anys")
        
    elif opcio == "3":
        print(NotaUF())
        
    elif opcio == "4":
        print("Bye")
    else:
        print("opcio incorrecta")