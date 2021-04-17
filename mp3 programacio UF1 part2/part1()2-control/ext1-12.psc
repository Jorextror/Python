Algoritmo jordi_oliveda
	Definir num1,num2,num3 Como Real
	
	Escribir "num1"
	leer num1
	Escribir "num2"
	leer num2
	Escribir "num3"
	leer num3
	
	si num1 < num2
		si num1 < num3
			si num2 < num3
				Escribir num1," " num2," " num3 
			SiNo
				Escribir num1," " num3," " num2
			FinSi
		FinSi
	FinSi
	si num2 < num1
		si num2 < num3
			si num1 < num3
				Escribir num2," " num1," " num3
			SiNo
				Escribir num2," " num3," " num1
			FinSi
		FinSi
	FinSi
	si num3 < num1
		si num3 < num2
			si num1 < num2
				Escribir num3," " num1," " num2
			SiNo
				Escribir num3," " num2," " num1
			FinSi
		FinSi
	FinSi
FinAlgoritmo
//jordi oliveda