Algoritmo pr4_ex10
	Definir MAX_COLS, MAX_FILS Como Entero
	MAX_COLS = 10
	MAX_FILS = 10
	Definir SIMB1, SIMB2 Como Caracter
	SIMB1 = "*"
	SIMB2 = " "
	Definir i, j Como Entero
	
	Para i = 1 Hasta MAX_FILS Hacer
		
		Para j = 1 Hasta MAX_COLS Con Paso 1 Hacer	    	
			Si i == 1 o i == MAX_FILS Entonces 
				Escribir SIMB1 SIMB2 Sin saltar 
			SiNo 
				Si j == 1 o j == MAX_COLS Entonces 
					Escribir SIMB1 SIMB2 Sin saltar 
				SiNo 
					Escribir SIMB2 SIMB2 Sin saltar 
				FinSi								
			FinSi		
			
		FinPara

		Escribir ""
	FinPara
	
FinAlgoritmo
