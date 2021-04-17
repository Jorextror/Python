Algoritmo pr1_ex8	
	//Fes un algorisme pseInt que donat un número que has 
	//de comprobar que sigui més gran o igual que 1 i més
	//petit o igual que 1000 i escriu el seu equivalent en 
	//números romans.
	
	Definir num, centenes, desenes, unitats como Entero
	Definir num_aux Como Entero
	Definir numRoma Como Caracter
	
	Definir	NU0, NU1, NU2, NU3, NU4, NU5, NU6, NU7, NU8, NU9 Como Caracter
	Definir	ND0, ND1, ND2, ND3, ND4, ND5, ND6, ND7, ND8, ND9 Como Caracter
	Definir	NC0, NC1, NC2, NC3, NC4, NC5, NC6, NC7, NC8, NC9 Como Caracter
	
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

	Escribir "Introdueix un numero entre 1 i 1000"
	Leer num
	
	Si num == 0 Entonces
		Escribir "No hi ha cap simbol per representar el 0"
	Sino
		Si num >= 1000 Entonces
			Escribir "Numero massa gran"
		Sino 
			Si num < 0 Entonces
				Escribir "Numero no valid, es negatiu"
			
			Sino
		
				//Realitzar la conversió
				//Si es pot convertir aleshores...
				Si num = 1000 Entonces            
					numRoma = "M"
				SiNo		
					
					desenes = 0
					centenes = 0
					num_aux = num
					
					//# Calcular unitats 
					unitats = num_aux MOD 10
					num_aux = trunc( num_aux / 10 )
					//# Calcular desenes
					Si num_aux > 0 Entonces
						desenes	= num_aux MOD 10
						num_aux = trunc( num_aux / 10 )
						//# Calcular centenes
						Si num_aux > 0 Entonces
							centenes = num_aux MOD 10
						FinSi
					FinSi
					
					Segun centenes Hacer
						0: numRoma = NC0
						1: numRoma = NC1
						2: numRoma = NC2
						3: numRoma = NC3
						4: numRoma = NC4
						5: numRoma = NC5
						6: numRoma = NC6
						7: numRoma = NC7
						8: numRoma = NC8
						9: numRoma = NC9
					Fin Segun							
					
					Segun desenes Hacer
						0: numRoma = numRoma + ND0
						1: numRoma = numRoma + ND1
						2: numRoma = numRoma + ND2
						3: numRoma = numRoma + ND3
						4: numRoma = numRoma + ND4
						5: numRoma = numRoma + ND5
						6: numRoma = numRoma + ND6
						7: numRoma = numRoma + ND7
						8: numRoma = numRoma + ND8
						9: numRoma = numRoma + ND9
					Fin Segun
					
					Segun unitats Hacer
						0: numRoma = numRoma + NU0
						1: numRoma = numRoma + NU1
						2: numRoma = numRoma + NU2
						3: numRoma = numRoma + NU3
						4: numRoma = numRoma + NU4
						5: numRoma = numRoma + NU5
						6: numRoma = numRoma + NU6
						7: numRoma = numRoma + NU7
						8: numRoma = numRoma + NU8
						9: numRoma = numRoma + NU9
					Fin Segun
					
				FinSi	
				
				Escribir "El numero " num " sescriu " numRoma " en numeros romans"
				
			Finsi	
		Finsi	
	Finsi	

FinAlgoritmo
