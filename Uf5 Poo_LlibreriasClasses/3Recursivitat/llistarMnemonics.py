def llistarMnemonics(cadena_inici,digit,num,dicc):
    if digit==-1:
        return cadena_inici+" "
    else:
        cadena=""
        for x in dicc[int(num[digit])]:
            cadena+=llistarMnemonics (cadena_inici +x,digit-1,num,dicc)
        return cadena

def llistarMnemonics2(cadena_inici,digit,num,dicc):
    if digit == -1:
        return cadena_inici+" "
    else:
        digitValor=int(num[digit])
        tecla=dicc[digitValor]
        cadena0=llistarMnemonics2(cadena_inici+tecla[0],digit-1,num,dicc)
        cadena1=llistarMnemonics2(cadena_inici+tecla[1],digit-1,num,dicc)
        cadena2=llistarMnemonics2(cadena_inici+tecla[2],digit-1,num,dicc)
        return cadena0+cadena1+cadena2

diccionari_teclat={2:"ABC",3:"DEF",4:"GHI",5:"JKL",6:"MNO",7:"PRS",8:"TUV",9:"WXY"}
# num=input("valor: ")
num="723"
digit=len(num)-1
print(llistarMnemonics("",digit, num, diccionari_teclat))
print()
print (llistarMnemonics2("",digit,num,diccionari_teclat))