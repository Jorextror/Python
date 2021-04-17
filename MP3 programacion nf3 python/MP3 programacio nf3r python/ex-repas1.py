"""
Programa en python els passos següents:
Entra un any per teclat entre el 1900 i el 1999
No avancis fins que l’any entrat està dins de l’interval
Calcula la suma de les xifres de l’any
Resta de l’any la suma de les xifres
Comprova que el resultat és divisible per 9
"""
any = 0
while any < 1900 or any > 1999:
  any = int(input("Introdueix un any entre 1900-1999: "))

xifres = [int(xifra) for xifra in str(any)]
sumaXifres = sum(xifres)
joinAny =  "+".join(str(any))

print("La suma de les xifres dóna :", joinAny  ,"=", sumaXifres)
print("La resta dóna :", any ,"-", sumaXifres ," =", any-sumaXifres)

if (sumaXifres-any)%9 == 0 :
  print(any-sumaXifres ," és divisible per 9")