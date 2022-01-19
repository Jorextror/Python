def tokenitzar(string):
    token=[]
    obert=False
    letra=""
    for e in string:
        if obert and e!=">":
            if e =="/":
                token.append(e)
            else:
                letra=letra+e
        elif e=="<":
            obert=True
            token.append(e)
        elif e==">":
            obert=False
            token.append(letra)
            letra=""
            token.append(e)
    return token
# Cua i pila
class Cua(object):
    def __init__(self):
        self.items=[]
    def encua(self, x):
        #agregar al final de la lista.
        self.items.append(x)
    def desencua(self):
        #Elimina el primer elemento. si esta vacio salta el exept
        try:
            return self.items.pop(0)
        except:
            raise ValueError("La cola está vacía")
    def esbuida(self):
        return self.items == []
class Pila(object):
    def __init__(self):
        self.items=[]
    def apila(self, x):
        #agregar al final de la lista.
        self.items.append(x)
    def desapila(self):
        #Devuelve el elemento tope y lo elimina de la pila. pero si esta vacia salta el except
        try:
            return self.items.pop()
        except IndexError:
            raise ValueError("La pila está vacía")
    def mostraPrimerElement(self):
        print(self.items[0])
    def esbuida(self):
        return self.items == []

html="<html><head><title>Exemple</title></head><body><h1>Hola món</h1></body></html>"
correcta=True#per cuan es validi mostri error perque falta <
tancar=True#per saber si esta tancan un tag "/"
tags=[]#noms dels tags

#print("---- tokenitzar ----")
ll=tokenitzar(html)
#print(ll)

print("---- Comprovar Codi HTML ----")
c = Cua()
p = Pila() #pila per ("<",">")
pt = Pila() #pila per els tags
#omple la cua
for i in ll:
    c.encua(i)
#comproba si esta tot correcta
for j in range(len(c.items)):
    el=c.desencua()
    if el == "<":
        p.apila(el)
    elif el == ">":
        tancar=True
        if p.esbuida():
            correcta=False
            break
        else:
            p.desapila()
    elif el != "/" and tancar:#si no es / o abans era una / no entra
        pt.apila(el)
        tags.append(el)
    elif tancar==False:#si abans era una / entrara
        if pt.esbuida():
            correcta=False
            break
        else:
            tag=pt.desapila()
            try:
                tags.remove(el)
            except:
                correcta=False
                break
    elif el == "/":
        tancar=False

if p.esbuida() and correcta and pt.esbuida():
    print("El tag esta corecte")
else:
    print("El tag esta erroni")