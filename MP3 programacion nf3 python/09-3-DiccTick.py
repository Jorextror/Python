"""JordiOliveda
(3 punts) T’encarreguen programar una bàscula d’una fruiteria. L’objectiu serà fer el tiquet de de cada venda. Declara un diccionari.  El diccionari tindrà com a clau  el nom de les fruites, i com a valor el preu per kg de la fruita indicada (fes un diccionari que tingui 5 tipus de fruites diferents). Un cop creat el diccionari demana per cada fruita el pes, i acumula en una variable import. Has d’imprimir en un format net i polit un tiquet similar a l’exemple. Ajuda http://puntoflotante.org/languages/python/ 
"""
fruites = {" pomes ": 1.6,
         " peres ": 2.1,
         " mandarines ": 3.2,
         " maduixes ": 5.1,
         " taronges ": 2.5}
total=0
items = 0
tiquet =  "\n\nLa Fruiteria: Tiquet de Compra\n"
for fruita in fruites:
    pes=float(input("Introdueix el pes de la fruita" +fruita+ "en kg (format n.n): "))
    if pes > 0:
        tiquet += fruita + "\t : \t" + str(fruites[fruita]) + "€/kg\t => \t" + "{:.2f}".format(fruites[fruita] * pes) +"€\n"
        total += fruites[fruita] * pes
        items +=1

print(tiquet)
print("\n================================")
print("Import total :\tnum ítems",items,"\t",total,"€" )