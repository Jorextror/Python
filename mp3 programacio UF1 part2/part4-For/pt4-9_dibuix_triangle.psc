Algoritmo sin_titulo
	Definir i,j,c,c1 Como Entero
	Definir cont Como Caracter
	c= 9 //contador de espais
	c1=1
	
	para i<-1 Hasta 10 Hacer
		
		si c <> 0
			Para j<-1 Hasta c Hacer //mira el contador cuants spais te de posar
				Escribir " " Sin Saltar
			FinPara
		FinSi
		
		j=0
		para j<-1 Hasta c1 hacer
			Escribir "$ " Sin Saltar
		FinPara
		Escribir ""
		c=c-1 //desconta un numero
		c1=c1+1
	FinPara
FinAlgoritmo
