'''
Calcula la seqüència de Collatz d'un nombre. Partint del nombre natural entrat > 1, el divideix entre 2 si és parell i si és senar el multiplica per 3 i li suma 1, successivament fins arribar a 1.
'''

num=1
while(num<=1):
    num=int(input("Introdueix un nombre natural més gran que 1: "))

num2=num

print(f"La seqüència de Collatz de {num} és:")
print(num2,end="")

while num2 > 1:
    print("->",end="")
    if num2%2==0:
        #Si és parell es divideix entre 2        
        num2=num2//2 #amb // evitem que converteixi a float
    else:
        #Si és senar es multiplica per 3 i se li suma 1
        num2=num2*3+1         
    print(num2,end="")
print()