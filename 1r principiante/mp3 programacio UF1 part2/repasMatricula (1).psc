Algoritmo circulaPerBarcelona
		
	definir matricula, dia Como Caracter
	Escribir "Introdueix la matrícula del teu cotxe format :"
	leer matricula
	
	// aquí el teu codi
	// ajuda hi ha funcions integrades pseint que et poden ajudar
	
	definir i,n Como Entero
	definir x1 como entero
	definir esXifra,esPrimer Como Logico
	esXifra = Falso
	esPrimer= Verdadero
	para i=0 hasta 9 hacer
		si Subcadena(matricula,0,0)==ConvertirATexto(i)
			esXifra= Verdadero
		FinSi
	FinPara
	
	SI esXifra Entonces
		n=ConvertirANumero(Subcadena(matricula,0,3))
		si n%2 == 0 Entonces
			dia ="Dilluns, Dimecres i Divendres"
		SiNo
			dia = "Dimarts i Dijous"
		FinSi
		si ConvertirANumero(Subcadena(matricula,0,0))%2 ==  0  y ConvertirANumero(Subcadena(matricula,3,3))%2 ==  0
			dia = dia + ", dissabte"
		FinSi
		para i=2 hasta n-1 Hacer
			si n%i ==0 Entonces
				esPrimer=Falso
			FinSi
		FinPara
		si esPrimer Entonces
			dia=dia+",diumenge"
		FinSi
	FinSi
	
	Escribir "Pots circular els: " dia
	
FinAlgoritmo
