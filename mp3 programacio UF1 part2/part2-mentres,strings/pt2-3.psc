Algoritmo sin_titulo
	Definir num,quants Como Entero
	
	Escribir "Escriu el número que vols potenciar "
	leer num
	Escribir "Escriu qunts comps vols potencia(maxim 5)"
	leer quants
	si quants <= 5
		//els quants -1 perque en "para" le pusat 0 
		//perque comenci al 0 pero oh feia fins al 5 i al total eran 6
		quants=quants-1
		para potencia<-0 Hasta quants Hacer
			Escribir num,"^",potencia," = ",num^potencia
		FinPara
	SiNo
		Escribir "No pot ser mes de 5 cops"
	FinSi
	
FinAlgoritmo
//JordiOliveda