Algoritmo pr2_ex1
	//Fes un algorisme que vagi demanant números per 
	//teclat fins que introduïm un número negatiu i 
	//mostri per pantalla per cada número si és parell o és senar.
	Definir num Como Entero
	
	num = 0
	
	Mientras num >= 0 Hacer
		Escribir "Introdueix un nombre (negatiu per acabar): "
		Leer num
		Si num >= 0 Entonces
			Escribir "El numero " num " es " Sin Saltar
			Si num mod 2 == 0
				Escribir "parell"
			SiNo				
				Escribir "senar"
			FinSi
		FinSi
	Fin Mientras
	
FinAlgoritmo
