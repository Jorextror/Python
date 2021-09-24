Algoritmo sin_titulo
	Definir tx,ty,tz Como Real
	
	Escribir "triangle x"
	Leer tx
	Escribir "triangle y"
	leer ty
	Escribir "tringle z"
	leer tz
	
	si tx == ty y ty == tz
		Escribir "És un triangle equilàter"
	FinSi
	
	si tx <> ty y ty <> tz y tx <> tz
		Escribir "És un triangle escalè"
	FinSi
	
	si tx == ty y ty <> tz o ty == tz y tz <> tx o tx == tz y tx <> ty
		Escribir "És un triangle isòscel"
	FinSi
	
FinAlgoritmo
//jordi oliveda