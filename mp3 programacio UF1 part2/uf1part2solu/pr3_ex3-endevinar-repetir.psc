Algoritmo pr3_ex3
	//Modifica l’algorisme d’endevinar un nombre 
	//amb una estructura repetir.
	//El programa demanarà nombres fins que l’encertis.
	//
	//Fes un algorisme pseInt per endevinar un 
	//nombre entre 1 i 9 (ambdós inclosos) que 
	//es genera aleatòriament (fes servir la funció azar).
	//L’usuari introduirà el nombre per teclat i el programa 
	//retornarà:
  	//si l’ha encertat : ENHORABONA!! Ets un crack!
	//sinó. Si la diferència és només d’1:
	//		quasi, pels pèls!
	//	si la diferència és més 4: dedica’t al parxís
	//		si no: la propera vegada ho faràs millor
	
	Definir num, num_rand, diff Como Entero
	Definir trobat Como Logico
	
	num_rand = Aleatorio(1, 9) 
	trobat = Falso
	
	Repetir	
		
		Escribir "Introdueix un numero entre 1 i 9: "
		Leer num
	
		diff = abs(num_rand - num)
		
		Segun diff Hacer
			0: Escribir "ENHORABONA!! Ets un crack!"
				trobat = Verdadero
				
			1: Escribir "quasi, pels pels!"	
				
			De Otro Modo:
				Si diff > 4 Entonces
					Escribir "dedicat al parxis"
				SiNo
					Escribir "la propera vegada ho faras millor"
				FinSi
		Fin Segun
	
	Hasta Que trobat == Verdadero
		
FinAlgoritmo
