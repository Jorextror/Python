Algoritmo pr3_ex1
	//Fes un algorisme que vagi demanant n�meros per 
	//teclat fins que introdu�m un n�mero negatiu i 
	//mostri per pantalla per cada n�mero si �s parell o �s senar.
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
