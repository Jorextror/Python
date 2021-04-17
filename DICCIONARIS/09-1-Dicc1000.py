"""Jordi Oliveda
(1 punt) Demana un nombre per teclat, comprova que sigui més gran que 1000, i no avancis fins que així sigui i després  crea un diccionari on  les claus siguin des del número 1 fins al número indicat, i que sigui múltiple de 10 , i els valors siguin la meitat de les claus. Fes dues versions, amb bucle for i amb dictionary comprehension 
"""
num=0
while num <= 1000:
    num=int(input("Introdueix un num de mes de 1000: "))

d={i:i/2 for i in range(1,num+1) if i%10==0}
print(d)