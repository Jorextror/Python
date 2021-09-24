Algoritmo pr4_ex4	
	//Fes un algorisme que calculi tots els divisors d’un nombre.
	Definir num, i Como Entero
	
	Escribir "Introdueix un nombre: "
	Leer num
	
	Si num == 0 Entonces			
		Escribir "0 no te divisors"
	SiNo
		Escribir "Els divisors de " num " son: "
		Para i=1 Hasta num Hacer
			Si num MOD i == 0
				//Divisor trobat
				Escribir i " " Sin Saltar
			FinSi
		Fin Para
		Escribir ""	
	FinSi
	
FinAlgoritmo