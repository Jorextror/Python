Algoritmo pr1_ex12
	//Escriu un programa que donats 3 números introduïts
	//per teclat, els imprimeix de manera ordenada.
	//Cal fer-ho utilitzant sentències Si, SiNo.	
	Definir n1, n2, n3 Como Real
	Definir r1, r2, r3 Como Real
	
	Escribir "Introdueix el primer nombre: "; Leer n1
	Escribir "Introdueix el segon nombre: ";	 Leer n2
	Escribir "Introdueix el tercer nombre: "; Leer n3
		
// Casos (per ordre d'ordenació):	
//	1 2 3 x
//	1 3 2 x
//	2 1 3   x
//	2 3 1 x
//	3 2 1   x
//	3 1 2   x

	Si n1 >= n2 Entonces		
		Si n1 >= n3 Entonces		
			r1 = n1
		 Si n2 >= n3 Entonces
			 //1 2 3			 
			 r2 = n2
			 r3 = n3
			Sino
				//1 3 2				
				r2 = n3
				r3 = n2	
			FinSi
			
		Sino
			//2 3 1 
			r1 = n3
			r2 = n1
			r3 = n2
		FinSi			
		
	SiNo
		// n1 < n2
		Si n2 >= n3 Entonces
			r1 = n2
			Si n3 >= n1 Entonces
				//3 1 2			
				r2 = n3
				r3 = n1
			Sino
				//2 1 3
				r2 = n1
				r3 = n3				
			FinSi
			
		Sino
			//3 2 1 
			r1 = n3
			r2 = n2
			r3 = n1
		FinSi			
		
	FinSi
			
	Escribir r1 " >= " r2 " >= " r3
	
FinAlgoritmo