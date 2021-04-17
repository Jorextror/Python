"""
Demana un nombre per teclat, comprova que sigui més gran que 1000, i no avancis fins que així sigui i després  crea un diccionari on  les claus siguin des del número 1 fins al número indicat, i que sigui múltiple de 10 , i els valors siguin la meitat de les claus. Fes dues versions, amb bucle for i amb dictionary comprehension
"""
n = 0
while n <= 1000:
  n = int(input("Introdueix un número més gran que 1000:")) 

ex1 = {i:i/2 for i in range(n) if i%10 == 0}
print(ex1)