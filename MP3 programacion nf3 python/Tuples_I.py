'''Pag 9'''
'''En aquest exercici, crearem una tupla. 
Crearem una tupla de nom vehicle, afegirem els elements que es mostren a continuació i verificarem el tipus d’objecte. 
Els elements són els següents: Toyota BMW Benz'''

vehicle=('Toyota', 'BMW', 'Benz')
print(type(vehicle))



'''Pag 11'''
'''Creeu una nova tupla per a mascotes amb els elements gos, gat i lloro:'''
mascotes=('gos', 'gat', 'lloro')

'''Executeu mascotes [1] per accedir al segon índex:'''
print (mascotes [1])

'''Intenteu accedir a un índex que no es troba a la tupla. Python generarà un error. De quin tipus ?'''
#print (mascotes [3])

'''Els índexs també poden ser negatius. Si utilitzeu un índex negatiu, -1 farà referència a l’últim element de la tupla, -2 es referirà al penúltim etc.  Accediu al primer, segon i últim amb índexs negatius'''
print (mascotes [-3])
print (mascotes [-2])
print (mascotes [-1])

'''Què passa si fem mascotes[‘1’] ? Quin és el problema??
L’error menciona dues maneres d’accedir als elements de la tupla, quins?'''
#print (mascotes ['1'])



'''Pag 13'''
'''Crea una tupla amb tots els nombres de l’1 al 10.'''
tupla= tuple([i for i in range(1,11)])
print(tupla)
'''Crea una tupla a partir de l’anterior amb només els nombres parells.'''
tuplaParells = tupla[1::2]
print(tuplaParells)
'''Crea una tupla a partir de l’anterior amb només els nombres senars.'''
tuplaSenars = tupla[::2]
print(tuplaSenars)



'''Pag 18'''
mascotes = ('cat', 'cat', 'cat', 'dog', 'horse')

'''Utilitzeu un mètode de tupla per comptar el nombre de vegades que apareix l’element gat a les mascotes de tupla i assigneu-lo a una variable, c.'''

c=mascotes.count("cat")
print (c)

'''Utilitzeu un mètode de tupla per calcular la longitud de les mascotes de tupla i assigneu-lo a una variable, d.'''

d=len(mascotes)
print (d)

'''Si el nombre de vegades que apareix l'element “cat” a les mascotes de la tupla és superior al 50%, imprimeix ‘Hi ha massa gats aquí’ al terminal. Si no, imprimiu ‘Tot ok’ al terminal.'''

if c*100/d > 50:
 print ("Hi ha massa gats aquí")
else: print("Tot ok")