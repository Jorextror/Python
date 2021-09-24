Algoritmo pr2_ex3
	//Fes un algorisme que calculi les n primeres potències 
	//d’un nombre. Haurem d'introduir per teclat el nombre 
	//i quantes potències volem calcular (màxim 5).
	
	Definir base, pot, res Como Entero
	Definir i Como Entero
	
	Escribir "Introdueix el nombre base: "
	Leer base
	Escribir "Introdueix la potencia (entre 1 i 5): "
	Leer pot
	
	Si pot <= 0 o pot > 5 Entonces
		Escribir "La potencia ha de ser entre 1 i 5, ambdos inclosos"
		
	SiNo
			
		i = 0
		Mientras i < pot Hacer			
			res = base^i
			Escribir base " elevat a " i " es " res
			i = i + 1
		FinMientras
	FinSi

FinAlgoritmo