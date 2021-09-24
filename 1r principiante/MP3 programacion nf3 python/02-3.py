C_NUMS = "0123456789"
C_ESPEC = "()/!$%&"
"""contadors"""
conte_num = False
conte_espec = False
valid = False
print("hola")
while valid == False:

    pas = input("Introdueix un pass segur: ")

    long=len(pas)
    if long < 6 or long > 16:
        print("El password ha de tenir entre 6 i 16 caracters.")

    else:
        if pas[0] == "A":
            
            long_nums = len(C_NUMS)
            long_espec = len(C_ESPEC)
            i = 1
            while i < long:
                caract = pas[i]
                
                if conte_num == False:
                    j = 0
                    while j < long_nums and conte_num == False:
                        if caract == C_NUMS[j]:
                            conte_num = True
                        else:
                            j = j + 1

                j=0
                while j < long_espec and conte_espec == False:
                    if caract == C_ESPEC[j]:
                        conte_espec = True
                    else:
                        j = j +1
                i = i + 1
            
            if conte_num == False:
                print("El password ha de contenir almenys una xifra.")
            if conte_espec == False:
                print("El password ha de contenir almenys un caracter especial.")
            if conte_num == True and conte_espec == True:
                print("El password es correcte.")
                valid = True
        else:
            print("El password ha de comencar per A.")
            
