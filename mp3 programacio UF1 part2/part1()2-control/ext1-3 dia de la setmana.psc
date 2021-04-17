Algoritmo dia_setmana
	
	// declarem variables
	definir A,M,mes,D Como Entero
	definir deTraspas Como Logico
	
	//taules per mesos
	definir t1,t2 Como Entero
	Dimension t1[12], t2[12]
	
	t1[1] = 0
	t1[2] = 3
	t1[3] = 3
	t1[4] = 6
	t1[5] = 1
	t1[6] = 4
	t1[7] = 6
	t1[8] = 2
	t1[9] = 5
	t1[10] = 0
	t1[11] = 3
	t1[12] = 5
	
	t2[1] = 0
	t2[2] = 3
	t2[3] = 4
	t2[4] = 0
	t2[5] = 2
	t2[6] = 5
	t2[7] = 0
	t2[8] = 3
	t2[9] = 6
	t2[10] = 1
	t2[11] = 4
	t2[12] = 6
	
	// demanar dades
	
	Escribir "Indrodueix dia 1-31: "
	Leer D
	
	Escribir "Indrodueix mes 1-12: "
	Leer mes
	
	Escribir "Introdueix any 1900-2100: "
	Leer A
	
	//Validar dades
	si D >= 1 y D <= 31
		si mes >= 1 o mes <= 12
			si A >= 1900 y A <= 2100
				
				// Un año es bisiesto en el calendario Gregoriano, si es divisible entre 4 y no divisible entre 100, y también si es divisible entre 400.
				deTraspas = (A %4 == 0 y A%100 <> 100 ) o  (A%400==0)
				M = mes
				
				//convertir dia en dia setmana
				
				si deTraspas = Verdadero
					M = t2[M]
					dia =((A-1)%7 + (trunc((A-1)/4) - (3*trunc((trunc((A-1)/100)+1)/4)))%7+ M + D%7)%7
					Segun dia
						0:escribir "El ",D " de " mes " de " a " va ser diumenge"
						1:escribir "El ",D " de " mes " de " a " va ser dilluns"
						2:escribir "El ",D " de " mes " de " a " va ser dimarts"
						3:escribir "El ",D " de " mes " de " a " va ser dimecres"
						4:escribir "El ",D " de " mes " de " a " va ser dijous"
						5:escribir "El ",D " de " mes " de " a " va ser divendres"
						6:escribir "El ",D " de " mes " de " a " va ser dissabte"
					FinSegun
				sino 
					M = t1[M]
					d =((A-1)%7 + (trunc((A-1)/4) - (3*trunc((trunc((A-1)/100)+1)/4)))%7+ M + D%7)%7
					Segun dia
						0:escribir "El ",D " de " mes " de " a " va ser diumenge"
						1:escribir "El ",D " de " mes " de " a " va ser dilluns"
						2:escribir "El ",D " de " mes " de " a " va ser dimarts"
						3:escribir "El ",D " de " mes " de " a " va ser dimecres"
						4:escribir "El ",D " de " mes " de " a " va ser dijous"
						5:escribir "El ",D " de " mes " de " a " va ser divendres"
						6:escribir "El ",D " de " mes " de " a " va ser dissabte"
					FinSegun
				FinSi
				
				//si dades no vàlides
			SiNo
				Escribir "Error: any"
			FinSi
		SiNo
			Escribir "Error: mes"
		FinSi
	SiNo
		Escribir "Error: dia"
	FinSi
	
FinAlgoritmo
//jordi oliveda