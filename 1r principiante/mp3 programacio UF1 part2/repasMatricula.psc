Algoritmo circulaPerBarcelona
	Definir num,cadenamatricula Como Entero
	definir matricula, dia Como Caracter
	Escribir "Introdueix la matrícula del teu cotxe format :"
	leer matricula
	
	// aquí el teu codi
	// ajuda hi ha funcions integrades pseint que et poden ajudar
	para i<-1 hasta 4
		cadenamatricula= ConvertirANumero(matricula)
	FinPara
	num = ConvertirANumero(matricula)
	parell= num mod 2
	
	para i<-1 Hasta num Hacer
		si num%i=0 Entonces //dividir per cada numero en aumento por el número para ver si es divisible
			cont=cont+1 //tiene que ser dibisible por ell y por ell mismo y eso sumara hasta dos
		FinSi
	FinPara
	
	si parell == 0
		Escribir "podra circular dilluns, dimecres, divendres"
		si cont == 2
			Escribir "podra circular al diumenge"
		FinSi
	SiNo
		Escribir "podra circular dimarts i dijous"
	FinSi
	
	
	Escribir "Pots circular el: " dia
	
FinAlgoritmo
