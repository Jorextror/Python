Algoritmo sin_titulo
	Definir i,j,c Como Entero
	Definir cont Como Caracter
	cont="$"
	c= 10 //contador de espais
	
	para i<-1 Hasta 10 Hacer
		
		Para j<-1 Hasta c Hacer //mira el contador cuants spais te de posar
			Escribir " " Sin Saltar
		FinPara
		
		Escribir cont
		cont=cont+"$" //suma un contador para completar el triangulo
		c=c-1 //desconta un numero
	FinPara
FinAlgoritmo
