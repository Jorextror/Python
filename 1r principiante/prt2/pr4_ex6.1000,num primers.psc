Algoritmo pr4_ex6
	//Fes un algorisme que mostri per pantalla tots els 
	//primers entre 1 i 1000.
	Definir num, i Como Entero
	Definir divisors, MAX_NUM Como Entero
	
	MAX_NUM = 1000
	
	Escribir "Mostrant els " MAX_NUM " primers nombres primers:"	
	
	Para num<-1 Hasta MAX_NUM Hacer
		
		//Primer si només divisible entre ell mateix i la unitat.
		//L'1 no és primer per conveni.
		divisors = 0
		Para i<-1 Hasta num Hacer
			Si num MOD i == 0
				//Divisor trobat
				divisors = divisors + 1
			FinSi
		Fin Para
		
		Si divisors == 2 //És primer
			Escribir num " " Sin Saltar
		FinSi
		
	Fin Para
FinAlgoritmo