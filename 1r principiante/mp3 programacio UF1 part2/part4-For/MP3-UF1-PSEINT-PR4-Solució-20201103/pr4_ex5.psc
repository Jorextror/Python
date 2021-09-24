Algoritmo pr4_ex5
	//Fes un algorisme que comprovi si un número és primer o no.
	Definir num, i Como Entero
	Definir divisors Como Entero
	divisors = 0
	
	Escribir "Introdueix un nombre: "
	Leer num
		
	//Primer si només divisible entre ell mateix i la unitat
	Si num <> 0 y num <> 1 Entonces
		Para i<-1 Hasta num Hacer
			Si num MOD i == 0
				//Divisor trobat
				divisors = divisors + 1
			FinSi
		Fin Para
	FinSi
	
	Si num == 0 o num == 1 o divisors > 2 //No és primer
		Escribir "El numero " num " no es primer."
	SiNo
		Escribir "El numero " num " es primer."
	FinSi
FinAlgoritmo