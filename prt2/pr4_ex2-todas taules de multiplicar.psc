Algoritmo pr4_ex2
	//Fes un algorisme que imprimeix la taula de 
	//multiplicar dels nombres de l’1 al 10. Utilitza 
	//un for aniuat per mostrar la taula.
	Definir i, j Como Entero
	Definir MAX_TAULA Como Entero
	MAX_TAULA = 10
	
	Para i = 1 Hasta MAX_TAULA Hacer
		Escribir "Taula del " i
		Para j = 1 Hasta MAX_TAULA Hacer
			Escribir i "x" j "=" i*j	
		FinPara
		Escribir ""
	FinPara
	
FinAlgoritmo
