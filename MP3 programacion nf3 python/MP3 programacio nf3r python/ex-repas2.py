"""
Fes un bucle que demani un nombre enter 
Surt del bucle quan l’usuari entri un enter entre 1 i 20 per teclat
Calcula el resultat de la fórmula n·(n+1) / 2. 
Compte: el resultat de la fórmula ha de ser enter
Imprimeix per pantalla el resultat anterior
Fes un bucle que sumi els enters des d’1 fins al nombre entrat per teclat
Compara el resultat de la fórmula amb la suma calculada en el bucle
Si són iguals escriu “Carl Friedrich Gauss tenia raó”
Sinó escriu “Alguna cosa ha fallat”

"""
n = 0
while n < 1 or n > 20:
  n = int(input("Introdueix un número enter entre 1 i 20: "))

resultat = int((n*(n+1))/2)
print(f"El resultat de la fórmula és {resultat}")
suma = sum([i for i in range(1,n+1)])

if suma == resultat:
  print("Carl Friedrich Gauss tenia raó")
else:
  print("Alguna cosa ha fallat")



