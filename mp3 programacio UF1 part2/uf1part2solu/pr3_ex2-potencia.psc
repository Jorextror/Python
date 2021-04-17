Algoritmo pr3_ex2
	//Fes un algorisme que calculi les n primeres potències 
	//d’un nombre. Haurem d'introduir per teclat el nombre 
	//i quantes potències volem calcular (màxim 5).
	
	Definir base, pot, res Como Entero
	Definir dada_ok Como Logico
	Definir i Como Entero
	
	Repetir
		Escribir "Introdueix el nombre base (entre 1 i 10): "
		Leer base
		dada_ok = (base >= 1 y base <= 10)
		Si !dada_ok Entonces
			Escribir "Error: la base ha de ser entre 1 i 10, ambdos inclosos"
		FinSi		
	Hasta Que dada_ok
	
	Repetir
		Escribir "Introdueix la potencia (entre 1 i 5): "
		Leer pot
		dada_ok = (pot >= 1 y pot <= 5)
		Si !dada_ok Entonces
			Escribir "Error: la potencia ha de ser entre 1 i 5, ambdos inclosos"
		FinSi		
	Hasta Que dada_ok
	
	i = 0
	Repetir
		res = base^i
		Escribir base " elevat a " i " es " res
		i = i + 1			
	Hasta Que i == pot		
	
FinAlgoritmo