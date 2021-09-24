Algoritmo sin_titulo
	Definir a,b,c,k,p,q,M,N,d,e Como Real
	
	Escribir "Año del que queremos calcular la Pascua"
	Leer A
	
	a=A mod 19
	b=A/4
	c=A/7
	k=A/100
	p=13+8k/25
	q=k/4
	M=15-p+k-q/30
	N=4+k-q/7
	d=19a+M/30
	e=2b+4c+6d+N/7
	
	
FinAlgoritmo
