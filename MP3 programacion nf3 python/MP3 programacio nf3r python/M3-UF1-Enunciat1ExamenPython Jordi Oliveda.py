"""Jordi Oliveda
Donat un nombre natural k, es defineix la seqüència de Collatz com una successió de nombres que
comença per k, i a cada pas aplica la següent lògica:

si el nombre és parell es divideix entre dos,
si el nombre és senar es multiplica per 3 i se li suma 1.

"""

num=1
while num <= 1:
    num = int(input("introdueix un núm més grand que 1: "))
    
print("la seqüència de Collatz de ",num,"és:")
print(num,end="")
while num > 1:
    print("->",end='')
    if num%2==0:
        num = num // 2
    else:
        num = num * 3+1
    print(num,end='')