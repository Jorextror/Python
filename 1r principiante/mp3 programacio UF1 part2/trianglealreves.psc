Algoritmo triangle_al_reves
	
	definir i,j,k,mida Como Entero
	Repetir
		Escribir "Introdueix un numero: "
		leer mida
	Hasta Que mida%2==1 y mida>=5 y mida<=15
	
	para i=mida hasta 1 Con Paso -2 Hacer
		para j= mida hasta i con paso -2 Hacer
			Escribir "  " Sin Saltar
		FinPara
		
		para j= 1 hasta i con paso 1 Hacer
			Escribir "* " Sin Saltar
		FinPara
		Escribir ""
	FinPara
	
FinAlgoritmo