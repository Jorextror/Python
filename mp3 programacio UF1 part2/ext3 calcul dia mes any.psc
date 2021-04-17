Algoritmo sin_titulo
	Definir D, mes, A Como Real
	Definir d Como Entero
	
	Escribir "Introdueix el dia"
	leer D
	Escribir "Introdueix el mes"
	leer mes
	Escribir "Introdueix el any"
	leer A
	
	si D >= 1 y D <= 31
		si mes >= 1 y mes <= 12
			si A >= 1900 y A <= 2100
				
				d=((A-1)%7+((A-1)/4-(3*((A-1)/100+1)/4))%7+mes%7+D%7)%7
				
				
				
			SiNo
				Escribir "Error: any"
			FinSi
		SiNo
			Escribir "Error: mes"
		FinSi
	sino
		Escribir "Error: dia"
	FinSi
FinAlgoritmo
