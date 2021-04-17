Algoritmo pr1_ex11
	//Escriu un programa per comprovar si un triangle
	//és equilàter, isòsceles o escalè. L’usuari introduirà 
	//els tres costats dels triangle per teclat.
	
	//equilàter = els tres costats són iguals.
	//escalè = tres costats diferents.
	//isòscel = amb (almenys) dos costats iguals.	
	Definir xx, yy, zz Como Real
	
  Escribir "Longitud de entrada dels costats del triangle:"
	Escribir "x: "; Leer xx
	Escribir "y: "; Leer yy
	Escribir "z: "; Leer zz
	
	Si xx > 0 y yy > 0 y zz > 0 Entonces
		
		Si xx == yy y xx == zz Entonces
			// tres costats iguals
			Escribir "Triangle equilater"
			
		SiNo si xx == yy o yy == zz
			// dos costats iguals
				Escribir "Triangle isoscel"
				
			SiNo 
				// tres costats diferents
				Escribir "Triangle escale"
			FinSi
			
		FinSi
	
	SiNo
	
		Escribir "Els valors introduits no son correctes"
		
	FinSi
	
FinAlgoritmo
