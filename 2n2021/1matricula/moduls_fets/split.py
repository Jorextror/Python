"""Aquesta funcio rebra una imatge img en blanc i negre retallada verticalment i retorna una
tupla (D,R) on la que D  ́es una imatge amb el dıgit de mes a l’esquerra i R  ́es la resta de la
imatge. La imatge corresponent al dıgit extret D es retorna convenientment retallada en la
direccio horitzontal. La resta R esdeve una imatge nul.

la quan s’han extret tots els dıgits.

return tubla(D,R)
D= digit mes l'esquerra
R= resta imag
"""
from PIL import Image
from img import subimg

def split_digit(img):
    for i in range(len(img[1])): 
        wp = 0
    for j in range(len(img[1][j])):
        if img[1][j][i]==(0,0,0):
            oh = 0
            ow = j-1
            detectat = True
        elif img[1][j][i]==(255,255,255):
            wp += 1
            if wp == len(img[1][j]) and detectat:
                w=j
                h=len(img[1])
    if not detectat:
        return null
    return subimg(img,ow,oh,w,h)
