# Cua
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
# Pila
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
    
c = Cua()
p = Pila()
correcta=True
l1="25+3*(1+2+(30*4))/2"
l2="25+3*(1+2+(30*4))/(2"
l3="25+3*(1+2+(30*4))/)2("
l4="25+3*(1+2)+(30*4))/2"

#cua
print("-- Cua --")
# c.encua(10)
# c.encua(23)
# c.encua(79)
# num = c.desencua()
# print (num)

#pila
print("-- Pila --")
# p.apila(10)
# p.apila(23)
# p.apila(79)
# num = p.desapila()
# print (num)
# p.mostraPrimerElement()

# -- PART 2
# 1
for i in l3:
    if i==")" or i=="(":
        c.encua(i)
# 2
for j in range(len(c.items)):
    el=c.desencua()
    if el == "(":
        p.apila("(")
    elif el == ")":
        if p.esbuida():
            correcta=False
            break
        else:
            p.desapila()
        
if p.esbuida() and correcta:
    print("l'expressió esta corecte")
else:
    print("l'expressió és erroni")