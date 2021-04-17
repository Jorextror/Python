Algoritmo sin_titulo
	Definir n, a Como Entero
	
	Escribir "Escriu un numero de 1 al 9 per endevinar-lo "
	leer n
	
	a = Aleatorio(1,9)
	Mientras a<>n
		Escribir "Torna a intentar posar un numero "
		leer n
		
		si n = a
			Escribir "ENHORABONA!! Ets un crack!"
		FinSi
		
		si a = (n-1) o a = (n+1)
			Escribir "quasi, pels pèls!"
		FinSi
		
		si a <= (n-4) o a >= (n+4)
			Escribir "dedicat al parxís"
		FinSi
		
		Si a < (n-4) o a > (n+4)
			Escribir "la propera vegada ho faràs millor"
		FinSi
	FinMientras
	
FinAlgoritmo
//jordi oliveda