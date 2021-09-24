Algoritmo sin_titulo
	Definir pass,ce,num Como Caracter
	Definir c,v Como Entero
	Definir valid Como Logico
	
	valid=Falso
	Repetir
		Escribir "Escriu pasword segur"
		leer pass
		c=0
		v=0
		//los 0 son la posicio del caracter que quieres ver o manipular
		S=Subcadena(pass,1,1)
		l = Longitud(pass)
		//Comenci per letra A
		si s = "A"
			v=v+1
		SiNo
			Escribir "Tiene que empezar por (A)"
		FinSi
		//almenys tingui una xifra numerica
		mientras c<l Hacer
			num=Subcadena(pass,c,c)
			si num ="0" o num ="1" o num ="2" o num ="3" o num ="4" o num ="5" o num ="6" o num ="7" o num ="8" o num ="9"
				v=v+1
				c=l
			FinSi
			c=c+1
		FinMientras
		//llargada minima 6 y llargada maxima 16
		
		si l>6 y l < 16
			v=v+1
		SiNo
			Escribir "El pass té de tindre més de 6 i menys 16"
		FinSi
		//contingui un caracter especial
		c=0
		Mientras c<l Hacer
			ce=Subcadena(pass,c,c)
			si ce ="(" o ce=")" o ce="/"o ce="!"o ce ="$" o ce ="%" o ce ="&"
				v=v+1
				c=l
			FinSi
			c=c+1
		FinMientras
		
		//valid?
		si v==4
			valid=Verdadero
		FinSi
	Hasta Que valid=Verdadero
	
	Escribir "succesfull"
	
FinAlgoritmo
