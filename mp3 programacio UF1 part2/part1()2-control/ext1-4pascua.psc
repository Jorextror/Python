Algoritmo sin_titulo
	Definir a,b,c,k,p,q,M,N,d,e Como Real
	
	Escribir "Año del que queremos calcular la Pascua"
	Leer Any
	
	a=Any mod 19
	b=trunc(A/100)
	c=A mod 100
	d=trunc(B/100)
	e=b mod 4
	f=trunc((b+8)/25)
	g=trunc((b-f+1)/3)
	h=(19*a+b-d-g+15)mod 30
	i=trunc(c/4)
	k=c mod 4
	l= (32+2*e+2*i-h-k)mod 7
	m=trunc((a+11*h+22-l)/451)
	n=h+l-7*m+114
	mes=trunc(n/31)
	dia=1+(n mod 31)
	Escribir "El dia ",dia," mes " mes
	
FinAlgoritmo
