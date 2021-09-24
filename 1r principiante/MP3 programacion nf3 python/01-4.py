'''Jordi Oliveda
Fes un programa en Python que comprovi que s’ha introduït
una lletra per teclat (no més d’una) i després que comprovi si
la lletra introduïda és una vocal o bé una consonant. (len)

definir x como caracter'''

vocals="aeiouAEIOU"
consonant="qwrtypsdfghjklñzxcvbnmQWRTYPSDFGHJKLÑZXCVBNM"

x= input("Introdueix: ")

if len(x)==1: """len mira la largada de un string amb ==1
fem que nomes una letra pugui entrar al if"""
    if x in vocals:
        print(x," és una vocal")
    elif x in consonant:
        print(x," és una consonat")
    else:
        print(x," No és una letra")
else:
    print("mida incorecta")
