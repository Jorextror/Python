Algoritmo sin_titulo
	Definir num,cont,i Como Entero
	Escribir "escriu un n�mero para saber si es primero"
	leer num
	
	cont= 0
	
	para i<-1 Hasta num Hacer
		si num%i=0 Entonces //dividir per cada numero en aumento por el n�mero para ver si es divisible
			cont=cont+1 //tiene que ser dibisible por ell y por ell mismo y eso sumara hasta dos
		FinSi
	FinPara
	
	si cont=2 Entonces //mira si tiene el contados a 2 y si no no �s un n�mero primo
		Escribir num," �s un n�mero primer"
	SiNo
		Escribir num," No �s un n�mero primer"
	FinSi
	
FinAlgoritmo
