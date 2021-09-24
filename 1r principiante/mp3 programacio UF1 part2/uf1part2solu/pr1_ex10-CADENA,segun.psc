Algoritmo pr1_ex10
	//Fes un algorisme pseInt que comprovi que s’ha 
	//introduït una lletra per teclat (només d’una, 
	//pots utilitzar la funció de pseInt longitud(cadena) ) 
	//i després que comprovi si la lletra introduïda és una vocal.	
	Definir lletra Como Caracter
	
	Escribir "Introdueix una lletra: "
	Leer lletra
	
	si Longitud(lletra) <> 1
		Escribir "No has introduit una lletra"
	SiNo
		Segun lletra Hacer
			"a", "e", "i", "o", "u":
				Escribir "La lletra introduida és una vocal"		
			De Otro Modo:
				Escribir "La lletra introduida és una consonant"
		Fin Segun
	FinSi
FinAlgoritmo
