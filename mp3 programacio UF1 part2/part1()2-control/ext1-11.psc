Algoritmo sin_titulo
	Definir tx,ty,tz Como Real
	
	Escribir "triangle x"
	Leer tx
	Escribir "triangle y"
	leer ty
	Escribir "tringle z"
	leer tz
	
	si tx == ty y ty == tz
		Escribir "�s un triangle equil�ter"
	FinSi
	
	si tx <> ty y ty <> tz y tx <> tz
		Escribir "�s un triangle escal�"
	FinSi
	
	si tx == ty y ty <> tz o ty == tz y tz <> tx o tx == tz y tx <> ty
		Escribir "�s un triangle is�scel"
	FinSi
	
FinAlgoritmo
//jordi oliveda