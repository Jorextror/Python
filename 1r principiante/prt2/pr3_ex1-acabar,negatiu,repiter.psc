Algoritmo pr3_ex1
	//Fes un algorisme que vagi demanant números per 
	//teclat fins que introduïm un número negatiu i 
	//mostri per pantalla per cada número si és parell o és senar.
	Definir num Como Entero
	
	num = 0
	
	Repetir	
		Escribir "Introdueix un num (negatiu x acabar): "
		Leer num
		Si num >= 0 Entonces
			Escribir num " es " Sin Saltar
			Si num mod 2 == 0
				Escribir "parell"
			SiNo				
				Escribir "senar"
			FinSi
		FinSi
  Hasta Que num < 0
FinAlgoritmo
