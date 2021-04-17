Algoritmo sin_titulo
	Escribir "Número: "
	leer num
	
	num7= num %7
	num5= num %5
	
	si num7 = 0 o num5 = 0
		si num5 = 0
			si num7 = 0
				Escribir "Multiple de 7 i 5"
			sino
				Escribir "multiple de 5"
			FinSi
		SiNo
			Escribir "Múltiple de 7"
		FinSi
	FinSi
FinAlgoritmo
//jordi oliveda