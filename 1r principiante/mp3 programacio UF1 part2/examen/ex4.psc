Algoritmo sin_titulo
	Definir num,i,j Como Entero
	Definir carac Como Caracter
	
	//a
	Repetir
		Escribir "Introdueix la mida entra 11 i 31 i nomes senars:"
		leer num
	Hasta Que num >= 11 y num <= 31 y num mod 2 <> 0
	//b
	Repetir
		Escribir "Introdueix el simbol:"
		leer carac
	Hasta Que carac == "*" o carac == "·" o carac == "-"
	//c
	para i=1 hasta num
		para j = 1 hasta num
			si	i == 1 o i == num
				Escribir carac," " Sin Saltar
			SiNo
				si j == 1 o j == num
					Escribir carac," " Sin Saltar
				SiNo
					Escribir " "," " Sin Saltar
				FinSi
			FinSi
			
		FinPara
		Escribir ""
	FinPara
	
FinAlgoritmo
