Algoritmo sin_titulo
	Definir num,cont,i Como Entero
	num=1
	cont= 0
	para num<-1 Hasta 1000 Hacer //simplement posar un for hasta 1000 y un variable = 1 para emepzar en 1
		
		para i<-1 Hasta num Hacer
			si num%i=0 Entonces //dividir per cada numero en aumento por el número para ver si es divisible
				cont=cont+1 //tiene que ser dibisible por ell y por ell mismo y eso sumara hasta dos
			FinSi
		FinPara
		
		si cont=2 Entonces //mira si tiene el contados a 2 y si no no és un número primo
			Escribir num," És un número primer"
		//SiNo
		//	Escribir num," No és un número primer"
		FinSi
		cont=0
	FinPara
	
FinAlgoritmo
