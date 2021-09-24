Algoritmo pr3_ex4
	//Fes un algorisme que comprovi la validesa d’un password.
	//Comprovar que:
	//	Comenci per la lletra ‘A’
	//	Almenys tingui una xifra (del 0 al 9)
	//	Tingui una llargada mínima de 6 caràcters
	//	Tingui una llarga màxima de 16 caràcters
	//	Contingui 1 dels següents caràcters especials ( ) / ! $ % ∧
	
	Definir pass, caract Como Caracter
	Definir long, i, j Como Entero
	
	Definir long_nums, long_espec Como Entero
	Definir C_NUMS, C_ESPEC Como Caracter
	C_NUMS = "0123456789"
	C_ESPEC = "()/!$%&"
	
	Definir conte_num, conte_espec, valid Como Logico
	conte_num = Falso
	conte_espec = Falso
	valid = Falso
	
	Repetir
		
		Escribir "Entra un password: "
		Leer pass
		
		long = Longitud(pass)
		Si long < 6 o long > 16
			Escribir "El password ha de tenir entre 6 i 16 caracters."
			
		Sino
			
			//Comprovar que comença per A abans del bucle
			Si subcadena(pass, 0, 0)	 == 'A' Entonces
				
				long_nums  = Longitud(C_NUMS)
				long_espec = Longitud(C_ESPEC)
				i = 1
				Mientras i < long Hacer
					caract = subcadena(pass, i, i)	
					
					//Comprovar que tingui almenys una xifra
					Si conte_num == Falso Entonces
						j = 0			
						Mientras j < long_nums y conte_num == Falso Hacer
							Si caract = subcadena(C_NUMS, j, j)	 Entonces							
								// Ha trobar un número
								conte_num = Verdadero					
							SiNo
								j = j + 1
							FinSi
						FinMientras
					FinSi
					
					//Comprovar que tingui almenys un caracter especial
					j = 0			
					Mientras j < long_espec y conte_espec == Falso Hacer
						Si caract = subcadena(C_ESPEC, j, j)	 Entonces							
							// Ha trobar un caràcter especial
							conte_espec = Verdadero					
						SiNo
							j = j + 1
						FinSi
					FinMientras
					
					i = i + 1
				Fin Mientras
				
				Si conte_num == Falso Entonces
					Escribir "El password ha de contenir almenys una xifra."	
				FinSi
				
				Si conte_espec == Falso Entonces
					Escribir "El password ha de contenir almenys un caracter especial."	
				FinSi
				
				Si conte_num == Verdadero y conte_espec == Verdadero
					Escribir "El password es correcte."	
					valid = Verdadero
				FinSi
				
			SiNo
				Escribir "El password ha de comencar per A."
			FinSi
			
		FinSi
		
	Hasta Que valid == Verdadero
	
FinAlgoritmo
