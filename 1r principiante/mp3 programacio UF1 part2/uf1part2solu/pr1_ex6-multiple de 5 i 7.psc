Algoritmo pr1_ex6
	//Escriviu un algorisme pseInt per comprovar que un 
	//nombre que introdu�m per teclat �s m�ltiple de 7 
	//i m�ltiple de 5 a la vegada.	
	
	Definir num Como Entero
	
	Escribir "Introdueix un nombre enter: "
	Leer num
	
	si num MOD 7 == 0 y num MOD 5 == 0
		Escribir "El nombre " num " �s m�ltiple de 7 i de 5 a la vegada." 
	SiNo
		Escribir "El nombre " num " no �s m�ltiple de 7 i de 5 a la vegada." 
	FinSi
	
FinAlgoritmo
