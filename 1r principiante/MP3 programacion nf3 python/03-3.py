"""Jordi Oliveda
Fes un programa que calculi les n primeres potències
d’un nombre fent servir el bucle for. Per exemple si
li introduïm el 2 i 4 , la consola mostrarà:

2 elevat a 0 és 1
2 elevat a 1 és 2
2 elevat a 2 és 4
2 elevat a 3 és 8
2 elevat a 4 és 16
"""
"""entradas de valors per teclat"""
n = int(input("Introdueix el valor de potencia: "))
vegadas = int(input("Introdueix les vegadas que vols que es faci la potencia: "))
"""bucle per calcular consecutivament potencias"""
for i in range(vegadas+1):
    print(n,"elevat a",i,"és",n**i)