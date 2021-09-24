Algoritmo pr1_ex7
	//Fes un algorisme  pseInt per endevinar un 
	//nombre entre 0 i 9 (ambdós inclosos) que 
	//es genera aleatòriament (fes servir la funció azar).
	//L’usuari introduirà el nombre per teclat i el programa 
	//retornarà:
  //si l’ha encertat : ENHORABONA!! Ets un crack!
	//sinó. Si la diferència és només d’1:
	//		quasi, pels pèls!
	//	si la diferència és més 4: dedica’t al parxís
	//		si no: la propera vegada ho faràs millor
	
	definir num, num_rand, diff como entero
	
	Escribir "Introdueix un número entre 0 i 9: "
	leer num
	
	num_rand = azar(10) //Genera un número aleatori entre 0 i n-1
	diff = abs(num_rand - num)
	
	Segun diff Hacer
		0: Escribir "ENHORABONA!! Ets un crack!"
		1: Escribir "quasi, pels pèls!"	
		De Otro Modo:
			Si diff > 4 Entonces
				Escribir "dedicat al parxís"
			SiNo
				Escribir "la propera vegada ho faràs millor"
			FinSi
	Fin Segun
	
	si diff <> 0
		Escribir "El número generat era el " num_rand
	FinSi
		
FinAlgoritmo
