Algoritmo pr4_ex3
	//Fes un programa que simuli el llançament
	//de 2 daus 100 vegades. Calcula la mitjana 
	//de tots els llançaments.
	Definir NUM_TIRADES, i, dau_1, dau_2 Como Entero
	Definir mitjana Como Real
	
	NUM_TIRADES = 100
	mitjana = 0
	
	Escribir "Tirant dos daus 100 vegades..."
	Para i<-0 Hasta NUM_TIRADES-1 Hacer
		dau_1 = Aleatorio(1, 6) 
		dau_2 = Aleatorio(1, 6) 
		
		mitjana = mitjana + dau_1 + dau_2
	Fin Para
	
	mitjana = mitjana / NUM_TIRADES
	Escribir "La mitjana dels llencaments es " mitjana
	
FinAlgoritmo
