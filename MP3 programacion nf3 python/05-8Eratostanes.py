"""Jordi Oliveda
Programa l’algorisme del sedàs d’Eratòstanes.
Busca els nombres primers del 2 al 120. Busca els 50 primers nombres primers..
"""
enter=2
n=120
P=[]
num=[2,3,5,7]
tatjar=[]
consideix=0

for i in range(enter,n+1): #crea el rang de números
    P+=[i]
cont=0

#for t in range(0,3):
while cont!=4: #fins a 4 perque tenim de mirar els divisibles 2,3,5,7 i son 4
    for j in P:
        consideix=num[cont]*j#multipliquem el el 2 en la llista
        
        for k in P:
            if consideix == k:#si consideix és igual a k el num que anira pujan segons la llsita
                tatjar.append(consideix)#la posra en una llista per tatjar despres (si era directa donaba error)
        for l in P:#anem borrar els que estan en la llista
            if l in tatjar:
                P.remove(l)
    
    cont+=1#contador per suba les voltes del bucle i per multiplicar vaigui abançant
print(P)