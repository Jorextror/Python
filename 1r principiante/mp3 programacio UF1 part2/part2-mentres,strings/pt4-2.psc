Algoritmo sin_titulo
	Definir num Como Entero
	num=0
	multi=0
	
	Mientras multi < 10 Hacer
		//suma el contador de multi que sera fin taula 10
		multi = multi +1
		num=0
		Escribir "La taula del " multi
		Escribir "---------------"
		Mientras num < 10 Hacer
			//suma el numero fins al 10 per la taula que toqui
			num = num +1
			Escribir num, " X ", multi, " = ", multi*num
			
		FinMientras
	FinMientras
FinAlgoritmo
//Jordi_Oliveda