Algoritmo sin_titulo
	Definir n Como Entero
	Escribir "escribe un n�mero"
	leer n
	
	si n >= 1 y n <= 9
		
		n2 = n * 11
		n3 = n * 111
		
		nt= n+n2+n3
		
		// sense forza bruta
		Escribir n " + " n2 " + " n3 " = " nt
	Sino
	Escribir "no �s un n�mero del 1 entre 9"
	FinSi

	
FinAlgoritmo
//Jordi OLiveda