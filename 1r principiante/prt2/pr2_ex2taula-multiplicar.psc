Algoritmo pr2_ex2
	//Fes un algorisme que imprimeix la taula de 
	//multiplicar dels nombres de l’1 al 10. Utilitza 
	//un while per mostrar la taula.
	Definir i, j Como Entero
	Definir MAX_TAULA Como Entero
	MAX_TAULA = 10
	
	i = 1
	
	Mientras i <= MAX_TAULA Hacer
		Escribir "Taula del " i
		j = 1		
		Mientras j <= MAX_TAULA Hacer
			Escribir i "x" j "=" i*j
			j = j +1	
		FinMientras
		Escribir ""
		i = i + 1
	FinMientras
	
FinAlgoritmo
