Algoritmo pr4_ex1
	//Fes un algorisme que demana 10 números per 
	//teclat i mostri per pantalla, per cada número
	//entrat, si és parell o és senar.
	Definir i, num Como Entero
	Definir MAX_NUM Como Entero
	MAX_NUM = 10
	
	Para i<-0 Hasta MAX_NUM-1 Hacer
		Escribir "Introdueix un número: "
		Leer num
		
		Si num MOD 2 == 0
			Escribir "El número " num " és parell."
		SiNo	
			Escribir "El número " num " és imparell."
		FinSi
  Fin Para
FinAlgoritmo
