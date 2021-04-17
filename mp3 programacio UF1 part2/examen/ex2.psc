Algoritmo sin_titulo
	Definir dni Como Caracter
	Definir fi Como logico
	Definir num Como Entero
	
	Escribir "Introdueix un nombre de dies: "
	leer dni
	
	si Longitud(dni) <> 9
		Escribir "8 digits més la letra"
	SiNo
		num = Subcadena(dni,0,7)
		num=ConvertirANumero(num)
			
		FinPara
	FinSi
	
	
	
FinAlgoritmo
