Algoritmo sin_titulo
	Definir nom Como Caracter
	Definir nonima Como Real
	
	Escribir "Nom: "
	leer nom
	
	Escribir "Hores realitzades: "
	leer hores
	
	si hores >= 160
		hnormals=160*15
		hextraordinaries=hores-160
		htotalsextraordinaries=hextraordinaries*25
		Escribir "La N�mina de ", nom ," �s:"
		Escribir "	* Hores Ordin�ries: 40h equivalen a ", hnormals," euros"
		Escribir "	* Hores Extraordin�ries ", hextraordinaries, "h equivalen a ", htotalsextraordinaries," euros"
		Escribir "En total aquest m�s XX cobrar� " hnormals+htotalsextraordinaries " euros"
	SiNo
		hnormals=hores*15
		Escribir "La N�mina de ", nom ," �s:"
		Escribir "	* Hores Ordin�ries: " hores " equivalen a ", hnormals," euros"
		Escribir "	* Hores Extraordin�ries 0h equivalen a 0 euros"
		Escribir "En total aquest m�s XX cobrar� " hnormals " euros"
	FinSi
		
FinAlgoritmo
//jordi oliveda