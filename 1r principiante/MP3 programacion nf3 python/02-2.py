import random
rand = random.randint(0, 9)
trobat = False
while trobat == False:
    
    num = int(input("Introdueix un numero entre 1 i 9: "))
    
    if num == rand:
        print("ENHORABONA!! Ets un crack!")
        trobat = True
    elif (num-1) == rand or (num+1) == rand:   
        print("quasi, pels pels!") 
    elif rand <= (num-4) or rand >= (num+4):
        print("dedicat al parxis")
    else:
        print("la propera vegada ho faras millor")
