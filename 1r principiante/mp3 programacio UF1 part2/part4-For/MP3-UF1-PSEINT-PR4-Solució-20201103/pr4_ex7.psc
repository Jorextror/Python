Algoritmo pr4_ex7
	Definir MAX_COLS, MAX_FILS Como Entero
	MAX_COLS = 10
	MAX_FILS = 10
	Definir SIMB1, SIMB2 Como Caracter
	SIMB1 = "$"
	SIMB2 = "-"
	Definir i, j Como Entero
	
	Para i = 1 Hasta MAX_FILS Con Paso 1 Hacer
		
		Para j = 1 Hasta MAX_COLS Con Paso 2 Hacer
			Si i MOD 2 == 0 Entonces
				Escribir SIMB2 SIMB1 Sin Saltar
			SiNo
				Escribir SIMB1 SIMB2 Sin Saltar
			FinSi			
		FinPara
		
		Escribir ""
	FinPara
FinAlgoritmo
