Algoritmo pr4_ex9
	Definir POS_INI, MAX_FILES, MAX_VEGADES Como Entero
	POS_INI = 10 //El primer $ s'escriu a la posici� 10
	MAX_FILES = 10
	MAX_VEGADES = 10
	Definir SIMB1, SIMB2 Como Caracter
	SIMB1 = " "
	SIMB2 = "$"
	Definir i, j, k Como Entero
	
	//1a linia: el 1r $ apareix a la posici� central, la 10,
	//2a linia: el 2n $ apareix a la posici� central-1, la 9,
	//etc...
	//�s a dir, a la 1a linia pintar 9 espais, 2a linia pintar 8,...
	//Despr�s de pintar els espais escriure "$ " tants cops
	//com el n�mero de l�nia actual
	Para i = 1 Hasta MAX_FILES Hacer
		//Escriure tants espais com 10-num fila
		Para j = 1 Hasta POS_INI-i Con Paso 1 Hacer	    	
			Escribir SIMB1 Sin saltar 
		FinPara
		//Escriure tants "$ " com el n�mero de l�nia ens indiqui,
		//com a m�xim escriurem "$ " 10 cops, per tant 
		//fins a MAX_VEGADES
		Para k = POS_INI-i+1 Hasta MAX_VEGADES Con Paso 1 Hacer					
			Escribir SIMB2 SIMB1 Sin Saltar
		FinPara
		Escribir ""
	FinPara

FinAlgoritmo
