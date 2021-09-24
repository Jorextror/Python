"""Jordi Oliveda"""

num = 0

while num >= 0:
    num = int(input("Introdueix un num (negatiu x acabar): "))
    if num >= 0:
        if num % 2 == 0:
            print(num,"és parell")
        else:
            print(num,"és senar")