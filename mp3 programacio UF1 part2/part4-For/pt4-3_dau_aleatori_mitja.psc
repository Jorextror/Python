Algoritmo sin_titulo
	Definir dau,daud,contador Como Entero
	Definir mitjana Como Real
	
	contador=0
	para dau=Aleatorio(1,6) hasta 100 hacer
		contador= contador + dau
		Escribir dau
		Escribir contador
	FinPara
	
	para daud=Aleatorio(1,6) hasta 100 hacer
		contador= contador + daud
	FinPara
	
	mitjana= contador / 100
	Escribir "Mitjana de 2 daus tirats 100 vegades ",mitjana 
	
FinAlgoritmo
