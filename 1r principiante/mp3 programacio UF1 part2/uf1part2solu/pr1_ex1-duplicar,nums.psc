Algoritmo pr1_exp1
	//Escriviu un algorisme pseInt que accepti un nombre enter per teclat  (n) entre 1 i 9  
	//i calculi el valor de n + nn + nnn. Exemple: Si n és 5, el resultat esperat: 5+55+555=615.	
	
	Definir num, res Como Entero
	
	Escribir "Introdueix un nombre entre 1 i 9:"
	Leer num
	
	si num >= 1 y num <= 9 Entonces
		res = num + (num * 11) + (num * 111)
		Escribir "El resultat és " res
	sino 
		Escribir "El nombre ha de ser entre 1 i 9"
	FinSi
FinAlgoritmo
