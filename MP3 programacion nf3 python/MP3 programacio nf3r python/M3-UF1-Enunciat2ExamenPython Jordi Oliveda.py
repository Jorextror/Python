"""Jordi Oliveda
Donada una llista d’N enters que representen les diferents cotes d’una muntanya,
definim els cims d’aquesta muntanya com aquells punts on la cota puja i després baixa
(no necessàriament a continuació).

No es considera un cim el cas en què la cota puja però no baixa
(per exemple [1,3,3,3,3], quan la cota baixa però no puja (per exemple [3,1,1,1,1]),
o quan ni puja ni baixa (per exemple [1,1,1,1,1]).

generi una llista de 10 enters aleatoris entre 0 i 20, que representen les cotes d’una muntanya,
i a continuació determini quants cims té aquesta muntanya.
"""
import random
puja=False
llista=[]
c=0
for i in range(0,9):
    rando=random.randint(0,19)
    llista.append(rando)
llista=[11,20,19,3,13,18,20,17,4]
#llista=[0,10,13,13,4,17,2,7,9,11]
print(llista)
for el in range(len(llista)):
    if llista[el] > llista[el-1]:
        puja=True
        #print("prova",llista[el-1])
    elif llista[el] < llista[el-1]:
        if puja==True:
            print(llista[el-1])
            puja=False
            c+=1
print("La muntanya té",c,"cims.")