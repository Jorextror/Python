Algoritmo pr5_ex1
//Fes un algorisme que:
//	
//Té 2 array:
//	Un de mida 10, de nombres reals, anomenat notesPrM3
//	Un de mida 2, de nombres reals, anomenat notesExM3
//	Demana totes les notes per teclat utilitzant bucles. No s'admeten notes menors que 0 ni majors que 10.
//	Presenti les notes de pràctiques en una sola línia separades per comes, indicant Notes de Practiques.
//	Igualment amb les notes dels examens
//	Calcula la nota maxima i la nota mínima de les practiques.
//	Calcula la mitjana de les notes dels examens i la mitjana de les notes de les practiques.
	//En digui si has aprovat o no el modul i amb quin literal, (Ex 9-10, Not 7-8, Be 6, 
//    Aprovat 5, suspès 1-4, no presentat 0. Per calcular la nota d’M3:
//		Les practiques compten un 40%, 
//		Els examens compte un 60%
//		Per fer mitja les notes de les practiques i dels examens ha de ser igual superior a 4.
	//		Si la nota surt suspesa, hi ha una darrera oportunitat, comprar un pernil al Jordi i a la Pilar.
	//    Si s’aprova per aquesta via cal indicar “Aprovat perniler”. Els no presentats (és a dir, 
	//    que porten una mitjana de 0 en les practiques i els examens) no tenen l’opció de l’aprovat perniler.
	Definir PRM3, EXM3 Como Entero
	PRM3 = 10
	EXM3 = 2
	Definir notesPrM3, notesExM3 Como Real
	Dimension notesPrM3[PRM3], notesExM3[EXM3]
	
	Definir i Como Entero
	Definir min, max, acum, pr_mitj, ex_mitj, nota, nota_final Como Real
	Definir resp Como Caracter
	Definir NOTA_MINIMA, PR_PERC, EX_PERC Como Real
	NOTA_MINIMA = 4
	PR_PERC = 40
	EX_PERC = 60
	
	//Demanar les notes de les pràctiques
	i = 0
	acum = 0
	min = 10
	max = 0
	
	Repetir
		Escribir "Introdueix la nota num." i+1 " de practiques: " 
		Leer nota
		Si nota < 0 o nota > 10 Entonces
			Escribir "Error: la nota ha de ser entre 0 i 10"
		SiNo
			notesPrM3[i] = nota
			//Càlcul de mínim, màxim i mitjana de la nota de pràctiques
			Si nota < min
				min = nota
			FinSi
			Si nota > max
				max = nota
			FinSi
			acum = acum + nota //per a la mitjana
			i = i + 1	
		FinSi
	Hasta Que i == PRM3
	
	pr_mitj = acum / PRM3
	
	//Demanar les notes dels exàmens
	i = 0
	acum = 0
	
	Repetir		
		Escribir "Introdueix la nota num." i+1 " dels examens: " 
		Leer nota
		Si nota < 0 o nota > 10 Entonces
			Escribir "Error: la nota ha de ser entre 0 i 10"
		SiNo
			notesExM3[i] = nota						
			acum = acum + nota //per a la mitjana
			i = i + 1
		FinSi
	Hasta Que i == EXM3
	
	ex_mitj = acum / EXM3
	
//Impressió notes pràctiques	
	Escribir "Notes de Practiques: "	Sin Saltar
	Para Cada nota de notesPrM3 Hacer
		Escribir nota ", " Sin Saltar
	FinPara
	Escribir ""
	Escribir "Mitjana practiques: " pr_mitj
	Escribir "Nota maxima de practiques: " max
	Escribir "Nota minima de practiques: " min
	
	//Impressió notes exàmens
	Escribir "Notes Examens: "	Sin Saltar
	Para Cada nota de notesExM3 Hacer
		Escribir nota ", " Sin Saltar
	FinPara	
	Escribir ""
	Escribir "Mitjana examens: " ex_mitj
	
	//Càlcul de la nota final ponderada
	nota_final = 0
	Si pr_mitj >= NOTA_MINIMA
	  nota_final = pr_mitj * PR_PERC / 100
  FinSi
  Si ex_mitj >= NOTA_MINIMA
	  nota_final = nota_final + ( ex_mitj * EX_PERC / 100 )
  FinSi
  
  //Mòdul aprovat o suspès?
	Escribir "Nota final: " nota_final
	Si nota_final >= 9 Entonces
		Escribir "Modul aprovat amb Ex"
	SiNo 
		Si nota_final >= 7 Entonces
			Escribir "Modul aprovat amb Not"
		SiNo			
			Si nota_final >= 6 Entonces
				Escribir "Modul aprovat amb Bé"
			SiNo			
				Si nota_final >= 5 Entonces
					Escribir "Modul aprovat amb Suf"
				SiNo
					// Suspès				
					Si nota_final == 0 Entonces
						Escribir "No presentat"
					SiNo
						//Aprovat perniler?
						Escribir "Has comprat un pernil pels profes (S/N)?"
						Leer resp
						Si resp == "S" o resp == "s"
							Escribir "Aprovat perniler"
						SiNo							
							Escribir "Modul suspes"
						FinSi		
					FinSi		
				FinSi		
			FinSi
		FinSi
	FinSi
	
FinAlgoritmo
