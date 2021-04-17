Algoritmo dia_setmana
	
	// declarem variables
	definir A,M,mes,D Como Entero
	definir deTraspas Como Logico
	
	// taules per mesos 
	definir t1,t2 Como Entero
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
	
	Escribir "Indrodueix dia 1-31: "
	Leer D
	
	Escribir "Indrodueix mes 1-12: "
	Leer mes
	
	Escribir "Introdueix any 1900-2100: "
	Leer A
	
	// Validar dades
	si D≥1 y D≤31
		si mes ≥ 1 y mes ≤ 12
			si A ≥ 1900 y A ≤ 2100
				
				// Cal comprovar si l’any és de traspàs :
				// Un anyo es bisiesto en el calendario Gregoriano, si es divisible entre 4 y no
				//divisible entre 100, y tambien si es divisible entre 400.
				
				deTraspas = (A %4 == 0 y A%100 ≠ 100 ) o  (A%400==0)
				
				M = mes-1
				
				si deTraspas Entonces
					M = t2[M]
				sino 
					M = t1[M]
				FinSi
				
				d =((A-1)%7 + (trunc((A-1)/4) - (3*trunc((trunc((A-1)/100)+1)/4)))%7+ M + D%7)%7
				
				Escribir d
				
				// convertir dia en dia setmana
				// …
				
				// si dades vàlides
			SiNo
				Escribir "Error: any"
			FinSi
		SiNo
			Escribir "Error: mes"
		FinSi
	sino
		Escribir "Error: dia"
	FinSi
	

	

FinAlgoritmo
