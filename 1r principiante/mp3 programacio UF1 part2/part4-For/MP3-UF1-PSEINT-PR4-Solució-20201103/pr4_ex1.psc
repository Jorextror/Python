Algoritmo pr4_ex1
	//Fes un algorisme que demana 10 n�meros per 
	//teclat i mostri per pantalla, per cada n�mero
	//entrat, si �s parell o �s senar.
	Definir i, num Como Entero
	Definir MAX_NUM Como Entero
	MAX_NUM = 10
	
	Para i<-0 Hasta MAX_NUM-1 Hacer
		Escribir "Introdueix un n�mero: "
		Leer num
		
		Si num MOD 2 == 0
			Escribir "El n�mero " num " �s parell."
		SiNo	
			Escribir "El n�mero " num " �s imparell."
		FinSi
  Fin Para
FinAlgoritmo
