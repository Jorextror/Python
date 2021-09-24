Algoritmo sin_titulo
	Definir dia,setmana,mesos,any,i Como Entero

	Repetir
		Escribir "Introdueix un nombre de dies: "
		leer dia
	Hasta Que dia >= 0
	
	setmana=trunc(dia/7)
	mesos=trunc(dia/30)
	any=trunc(dia/365)
	
	Escribir "anys: " any
	Escribir "mesos: " mesos
	Escribir "setmanes: " setmana
	
FinAlgoritmo
