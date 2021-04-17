"""
Entra un any per teclat entre el 1900 i el 1999
No avancis fins que l’any entrat està dins de l’interval
Calcula la suma de les xifres de l’any
Resta de l’any la suma de les xifres
Comprova que el resultat és divisible per 9
"""
valid=True
llista=[]
while valid == True:
    num = int(input("Entra un any per teclat entre el 1900 i el 1999 "))
    
    if num < 1900 or num > 1999:
        for el in range(4):
            llista.append(num[el])
        print(llista)