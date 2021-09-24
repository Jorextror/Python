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
		Escribir "La Nòmina de ", nom ," és:"
		Escribir "	* Hores Ordinàries: 40h equivalen a ", hnormals," euros"
		Escribir "	* Hores Extraordinàries ", hextraordinaries, "h equivalen a ", htotalsextraordinaries," euros"
		Escribir "En total aquest més XX cobrarà " hnormals+htotalsextraordinaries " euros"
	SiNo
		hnormals=hores*15
		Escribir "La Nòmina de ", nom ," és:"
		Escribir "	* Hores Ordinàries: " hores " equivalen a ", hnormals," euros"
		Escribir "	* Hores Extraordinàries 0h equivalen a 0 euros"
		Escribir "En total aquest més XX cobrarà " hnormals " euros"
	FinSi
		
FinAlgoritmo
//jordi oliveda