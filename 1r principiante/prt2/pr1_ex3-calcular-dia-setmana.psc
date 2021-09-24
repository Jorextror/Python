Algoritmo pr1_ex3
	//Utilitza l’enllaç per calcular el dia de la setmana d’una data.
	//Introduiràs per teclat, el dia, el mes i l’any. Vigila que el 
	//dia és entre 1 i 31, el més és entre 1 i 12, i l’any entre 
	//1900 i 2100.	
		
		// declarem variables
		definir A, M, mes, D, d_aux Como Entero
		definir deTraspas Como Logico
		definir dia_set Como Caracter
		
		// taules per mesos 
		definir t1, t2 Como Entero
		Dimension t1[12], t2[12]
		
		t1[0] = 0
		t1[1] = 3
		t1[2] = 3
		t1[3] = 6
		t1[4] = 1
		t1[5] = 4
		t1[6] = 6
		t1[7] = 2
		t1[8] = 5
		t1[9] = 0
		t1[10] = 3
		t1[11] = 5
		
		t2[0] = 0
		t2[1] = 3
		t2[2] = 4
		t2[3] = 0
		t2[4] = 2
		t2[5] = 5
		t2[6] = 0
		t2[7] = 3
		t2[8] = 6
		t2[9] = 1
		t2[10] = 4
		t2[11] = 6
		
		// demanar dades
		Escribir "Introdueix dia 1-31: "
		Leer D
		
		Escribir "Introdueix mes 1-12: "
		Leer mes
		
		Escribir "Introdueix any 1900-2100: "
		Leer A
		
		// Validar dades
		Si D < 1 o D > 31 Entonces
			Escribir "El dia introduit no es valid"
		SiNo
			Si mes < 1 o mes > 12
				Escribir "El mes introduit no es valid"
			SiNo
				Si A < 1900 o A > 2100
						Escribir "Any introduit no es valid"
					SiNo
		
						// si dades vàlides
						
						// Cal comprovar si l’any és de traspàs:
						// Un año es bisiesto en el calendario Gregoriano, si es divisible entre 4 y no
						// divisible entre 100, y también si es divisible entre 400.
						
						deTraspas = (A % 4 == 0 y A % 100 <> 100) o (A % 400 == 0)
						M = mes-1
						
						si deTraspas Entonces
							M = t2[M]
						sino 
							M = t1[M]
						FinSi
						
						d_aux = ((A-1)%7 + (trunc((A-1)/4) - (3*trunc((trunc((A-1)/100)+1)/4)))%7+ M + D%7)%7
						
						// convertir dia en dia setmana
						// 0 és diumenge, 1 és dilluns,...
						Segun d_aux Hacer
							0: dia_set = "diumenge"
							1: dia_set = "dilluns"	
							2: dia_set = "dimarts"	
							3: dia_set = "dimecres"	
							4: dia_set = "dijous"	
							5: dia_set = "divendres"	
							6: dia_set = "dissabte"				
							De Otro Modo:
								dia_set = "ERROR"
						Fin Segun
						
						// Sortida esperada per 25 5 2007:
						// “ El 25 de maig de 2007 va ser divendres
						Escribir "El " D " del mes " mes " de " A " es " dia_set
						
					FinSi
				FinSi
			FinSi

FinAlgoritmo
