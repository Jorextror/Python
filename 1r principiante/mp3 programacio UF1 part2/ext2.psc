Algoritmo sin_titulo
	Definir Temperatura Como Real
	Definir Convertir Como Caracter
	
	Escribir "Escribe la temperatura en C(centígrads)"
	leer Temperatura
	Escribir "Escribe en que quieres convertir la temperatura F(Fahrenheit) o K(kelvin)"
	leer Convertir
	
	si Convertir = "F" o Convertir = "f"
		Resultat= Temperatura * 9/5 + 32
		Escribir "La temperatura ", Temperatura " ºC equival a ", Resultat " ºF"
	SiNo
		Resultat= Temperatura + 273.15
		Escribir "La temperatura ", Temperatura " ºC equival a ", Resultat " K"
	FinSi

FinAlgoritmo
//jordi OLiveda