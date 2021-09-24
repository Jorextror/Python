Algoritmo jordi_oliveda
	Definir num, NC,ND,NU Como Entero
	Definir numRoma Como Caracter
	Definir NU0,NU1,NU2,NU3,NU4,NU5,NU6,NU7,NU8,NU9 Como Caracter
	Definir ND0,ND1,ND2,ND3,ND4,ND5,ND6,ND7,ND8,ND9 Como Caracter
	Definir NC0,NC1,NC2,NC3,NC4,NC5,NC6,NC7,NC8,NC9 Como Caracter
	
	Escribir "num"
	Leer num
	
	//errors de números no valits introduits 
	si num = 0 Entonces
		Escribir "no té simbol per representar 0"
		si num > 1000 Entonces
			Escribir "núm massa gran"
			si num < 0 Entonces
				Escribir "error: núm negatiu"
			FinSi
		FinSi
	FinSi
	
	//operació
	si num < 0 o num > 1000
		si num=1000
			Escribir "M"
		FinSi
	SiNo
		NU0=""
		NU1="I"
		NU2="II"
		NU3="III"
		NU4="IV"
		NU5="V"
		NU6="VI"
		NU7="VII"
		NU8="VIII"
		NU9="IX"
		
		ND0=""
		ND1="X"
		ND2="XX"
		ND3="XXX"
		ND4="XL"
		ND5="L"
		ND6="LX"
		ND7="LXX"
		ND8="LXXX"
		ND9="XC"
		
		NC0=""
		NC1="C"
		NC2="CC"
		NC3="CCC"
		NC4="CD"
		NC5="D"
		NC6="DC"
		NC7="DCC"
		NC8="DCCC"
		NC9="CM"
		
		NC=trunc(num/100)mod 10
		ND=trunc(num/10)mod 10
		NU=num mod 10
		
		Segun NC hacer
			0:
				numC = NC0
			1:
				numC = NC1
			2:
				numC = NC2
			3:
				numC = NC3
			4:
				numC = NC4
			5:
				numC = NC5 
			6:
				numC = NC6 
			7:
				numC = NC7 
			8:
				numC = NC8  
			9:
				numC = NC9
		FinSegun
		
		Segun ND hacer
			0:
				numD = ND0
			1:
				numD = ND1
			2:
				numD = ND2
			3:
				numD = ND3
			4:
				numD = ND4
			5:
				numD = ND5 
			6:
				numD = ND6 
			7:
				numD = ND7 
			8:
				numD = ND8  
			9:
				numD = ND9
		FinSegun
		
		Segun NU hacer
			0:
				numU = NU0
			1:
				numU = NU1
			2:
				numU = NU2
			3:
				numU = NU3
			4:
				numU = NU4
			5:
				numU = NU5 
			6:
				numU = NU6 
			7:
				numU = NU7 
			8:
				numU = NU8  
			9:
				numU = NU9
		FinSegun
		numRoma = numD + numC + numU
		Escribir num," ÉS " , numRoma
	FinSi

FinAlgoritmo
