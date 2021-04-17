Algoritmo pr1_ex9
    
    //Fes un algorisme pseInt per calcular el resultat d’una
    //equació de 2n grau. L’usuari ha d’introduir per teclat:
    
    //-el coeficient de X² - variable a
    //-el coeficient de X - variable b
    //-el terme lliure - variable c
    
    Definir a, b, c, discri, x, x2  Como Real
    
    Escribir "Escriu el valor a: "
    Leer a
    Escribir "Escriu el valor b: "
    Leer b
    Escribir "Escriu el valor c: "
    Leer c
    
    discri = b^2 - 4 * a * c
    
    Si discri = 0 Entonces
		x = - b / (2 * a)
		Escribir "La solucio es " x
    Sino si discri > 0
			x  = ( - b + rc(discri) ) / (2 * a)
			x2 = (- b - rc(discri) ) / (2 * a)
			Escribir "Les solucions son " x " i " x2
		Sino
			Escribir "No hi ha solucio"
     	FinSi
    FinSi
    
FinAlgoritmo
