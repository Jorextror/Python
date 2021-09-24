criba=[]
num=int(input("num: "))
for valor in range(1,1001):
    criba.append(valor)

contador=0
total=len(criba)
esprimo=1

while(contador<=total):
    auxiliar=2
    esprimo=1
    while(auxiliar<=contador/2 and esprimo!=0):
        esprimo=contador%auxiliar
        if esprimo==0: #print (“% no es primo”, contador)
            criba.remove(contador)
        auxiliar=auxiliar+1
    contador=contador+1
if num in criba:
    print("primo")
else:
    print("no primo")
print("PRIMOS", criba)