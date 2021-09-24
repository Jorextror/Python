'''Jordi OLiveda
Escriu un programa que donat un string que cal introduir
per teclat, comprovi si:
	
És de mida superior a 10 caràcters
És de mida inferior a 10 caràcters i conté algun dels següents caràcters: * + / -
És de mida 10 caràcters i comença per -
És de mida 10 caràcters i acaba per .

definir x como caracter'''

x= input("Introdueix frase: ")

if len(x) > 10:
    print(x," és superior de 10")
elif len(x) < 10:
    if ("*" in x or "+" in x or "/" in x or "-" in x):
        print(x, " és inferior de 10 amb un caracter (*x/-)")
else:
    if x[0] == "-":
        print(x, " comenza per "-" i és de mida 10")
    elif x[-1]==".":
        print(x," acaba en punt i és de mida 10")
    if [0] == "-" and x[-1]==".":
        print(x," comenza per - tambe acaba en punt i és de mida 10")
    else:
        print(x," és de mida 10")
