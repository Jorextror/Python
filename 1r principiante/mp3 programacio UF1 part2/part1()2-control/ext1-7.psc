Algoritmo sin_titulo
	Definir n, a Como Entero
	
	Escribir "num"
	leer n
	
	a = Aleatorio(1,9)
	
	si n = a
		Escribir "ENHORABONA!! Ets un crack!"
	FinSi
	
	si a = (n-1) o a = (n+1)
		Escribir "quasi, pels p�ls!"
	FinSi
	
	si a <= (n-4) o a >= (n+4)
		Escribir "dedicat al parx�s"
	FinSi
	
	Si a < (n-4) o a > (n+4)
		Escribir "la propera vegada ho far�s millor"
	FinSi
	
	Escribir "era un ", a
	
FinAlgoritmo
//jordi oliveda