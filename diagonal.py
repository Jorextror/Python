def dibujaMatriz(M):
    for i in range(len(M)):
        print ('[',)
        for j in range(len(M[i])):
            print ('{:>3s}'.format(str(M[i][j])),)
        print (']')

def determinante(matriz):
    '''
    Calcula el determinante poniendo ceros debajo
    de la diagonal principal
    '''
    m = copy(matriz)
    n=len(m)
    det=1
    for i in range(n):
        j=primeroNoNulo(m,i)
        if j == n:
            return 0
        if i!=j:
            det=-1*det
        intercambiaFilas(m,i,j)
        det=det*m[i][i]
        multiplicaFila(m,i,1./m[i][i])
        for k in range(i+1,n):
            combinacion(m,i,k,-m[k][i])
    return det
'''
A partir de la fila i, busca la primera fila j cuya entrada
(i,j) es nula
'''
def primeroNoNulo(m,i):
    result=i
    while result<len(m) and m[result][i]==0:
        result=result+1
    return result

m=input("m: ")
matriz=dibujaMatriz(m)
print(determinante(matriz))