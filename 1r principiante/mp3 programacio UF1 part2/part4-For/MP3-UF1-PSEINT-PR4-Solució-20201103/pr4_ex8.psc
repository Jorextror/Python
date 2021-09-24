Algoritmo pr4_ex8
	Definir MAX_COLS, MAX_FILS Como Entero
	MAX_COLS = 10
	MAX_FILS = 10
	Definir SIMB1, SIMB2 Como Caracter
	SIMB1 = " "
	SIMB2 = "$"
	Definir i, j, k Como Entero
	
	Escribir "Versio 1:"
	Para i = 1 Hasta MAX_FILS Hacer
		//Escriure tants espais com 10-num fila
		Para j = 1 Hasta MAX_COLS-i Con Paso 1 Hacer	    	
			Escribir SIMB1 Sin saltar 
		FinPara
		
		//Escriure la diferència fins a 10 amb $
		Para k = MAX_COLS-i+1 Hasta MAX_COLS Con Paso 1 Hacer					
			Escribir SIMB2 Sin Saltar
		FinPara
		Escribir ""
	FinPara
	
	
	Escribir ""
	Escribir "Versio 2:"
	Definir num_espais, num_dolars Como Entero
	
	Para i = 1 Hasta MAX_FILS Hacer
		num_dolars = i
		num_espais = MAX_COLS - num_dolars
		
		//Escriure tants espais com número de 10-num fila
		Para j = 1 Hasta num_espais Con Paso 1 Hacer	    	
			Escribir SIMB1 Sin saltar 
		FinPara
		
		//Escriure la diferència fins a 10 amb $
		Para k = 1 Hasta num_dolars Con Paso 1 Hacer					
			Escribir SIMB2 Sin Saltar
		FinPara
		Escribir ""
	FinPara	
FinAlgoritmo
