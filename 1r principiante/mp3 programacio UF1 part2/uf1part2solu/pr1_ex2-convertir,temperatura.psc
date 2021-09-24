Algoritmo pr1_ex2
	//Fes un  algorisme  pseInt  que passi una temperatura introduïda per teclat 
	//de graus centígrads a graus Fahrenheit o bé graus kelvin en funció del que 
	//digui l’usuari per teclat. La temperatura s’haurà d’introduir per teclat. 
	//El programa dirà la següent frase per la consola:	
	
	//La temperatura XX ºC equival a YY ºF 
     //o
     //La temperatura XX ºC equival a YY K
	
	Definir opcio Como Entero
	definir C, K, F Como Real
	
	opcio = 0
	Mientras opcio <> 1 y opcio <> 2 hacer
		Escribir "Introdueix la opció a realitzar (1: ºC a ºF, 2: ºC a K)"
		Leer opcio
		si opcio <> 1 y opcio <> 2 Entonces
			escribir "Error: opció incorrecta."	
		FinSi		
	FinMientras
	
	Escribir "Introdueix el graus centígrads: "
	leer C
	
	si C < -273.15 Entonces
		escribir "Error: el valor ha de ser més gran o igual a -273.15ºC"
	SiNo
		
		Segun opcio Hacer
			1:
				F = C * (9 / 5) + 32 
				Escribir "La temperatura " C "ºC equival a " F "ºF"
			2:
				K = C + 273.15
				Escribir "La temperatura " C "ºC equival a " K " Kelvin"
		Fin Segun
	FinSi
		
FinAlgoritmo
