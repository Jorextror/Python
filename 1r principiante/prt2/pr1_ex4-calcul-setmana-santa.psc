Algoritmo pr1_ex4
	//Utilitza l’algorisme de Butcher per calcular el mes i
	//el dia en què cau diumenge de Setmana Santa, d’un any 
	//del segle XXI que introduïm per teclat.	
	
	Definir any, dia, mes_num Como Entero
	Definir mes Como Caracter
	Definir A, B, C, D, E, F, G, H, I, K, L, M, N Como Real
	
	Escribir "Escriu un any del segle XXI: "
	Leer any
	
	//s XXI va del 01/01/2001 a 31/12/2100
	si any < 2001 o any >2100
		Escribir "Any introduït incorrecte"
	SiNo
		
		//Algorisme de Butcher
		A = any MOD 19
		B = trunc(any / 100)
		C = any MOD 100
		D = trunc(B / 4)
		E = B MOD 4
		F = trunc((B + 8) / 25)
		G = trunc((B - F + 1) / 3)
		H = (19 * A + B - D - G + 15) MOD 30
		I = trunc(C / 4)
		K = C MOD 4
		L = (32 + 2 * E + 2 * I - H - K) MOD 7
		M = trunc((A + 11 * H + 22 * L) / 451)
		N = H + L - 7 * M + 114
		mes_num = trunc( N / 31)
		dia = 1 + (N MOD 31)
				
		Segun mes_num Hacer
			1: mes = "gener"
			2: mes = "febrer"						
			3: mes = "marc"						
			4: mes = "abril"						
			5: mes = "maig"						
			6: mes = "juny"						
			7: mes = "juliol"						
			8: mes = "agost"						
			9: mes = "setembre"						
		   10: mes = "octubre"						
		   11: mes = "novembre"						
		De otro modo:
		   mes_= "desembre"						
		Fin Segun
				
		Escribir "El diumenge de Setmana Santa de " any " cau en " dia " de " mes 
	FinSi
	
FinAlgoritmo
