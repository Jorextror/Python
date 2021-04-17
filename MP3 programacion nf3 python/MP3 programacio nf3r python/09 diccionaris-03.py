"""
T’encarreguen programar una bàscula d’una fruiteria. L’objectiu serà fer el tiquet de de cada venda. Declara un diccionari.  El diccionari tindrà com a clau  el nom de les fruites, i com a valor el preu per kg de la fruita indicada (fes un diccionari que tingui 5 tipus de fruites diferents). Un cop creat el diccionari demana per cada fruita el pes, i acumula en una variable import. Has d’imprimir: “la fruiteria, import total de la teva compra : import en €”
"""
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