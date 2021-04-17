import random
Score=""
lletres=["A","B","C","D","E"]
encertat=False
contador=1
string=[]
vides=5
UserInput=[]
mida=4
for i in range (mida):
    num=random.randint(0,4)
    string.append(lletres[num])

while encertat!=True:
    contador=contador+1
    Final=""
    print("Vides restants: ",vides)
    Resp=input("Introdueix una combinació de 4 lletres formades per ABCDE: ")

    for el in Resp:
        UserInput.append(el)
    el=""
    if contador>1:
        print(Score)

    print(Resp,"=>",end=" ")

    for i in range (mida):
        if UserInput[i]==string[i]:
            Final=Final+"#"
        else:
            if UserInput[i] in string:
                Final=Final+"*"
            else:
                Final=Final+"-"

    print(Final)
    Score=Resp+" => "+Final

    if Final=="####":
        encertat=True
        print("Has encertat!!")
    else:
        vides=vides-1

    UserInput.clear()