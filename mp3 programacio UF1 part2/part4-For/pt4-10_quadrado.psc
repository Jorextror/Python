Algoritmo sin_titulo
	Definir i,j,x Como Entero
	
	Para j<-1 Hasta 10 Hacer
		
		Para i<-1 Hasta 8 Hacer //8 voltes perque en el seguent bugle completa les columnes
							//aquest bugle es per les filas adalt i abaix
			si j=1 o j=10
				Escribir "* " Sin Saltar
			FinSi
			
		FinPara
		
		Para x<-1 Hasta 10 Hacer
			
			si j!=1 o j!=10 //el bugle de les columnes de dreta i esquera
				
				si x=1 o x=10
					
					Escribir "* " Sin Saltar
					
				SiNo 
					si j=2 o j=3 o j=4 o j=5 o j=6 o j=7 o j=8 o j=9
						//el si perque no introdueixi espais en la columne de adalt de tot i abaix
						Escribir "  " Sin Saltar
						
					FinSi
					//Escribir "  ",j Sin Saltar
				FinSi
			FinSi
			
		FinPara
		
		Escribir ""
	FinPara
	
FinAlgoritmo
