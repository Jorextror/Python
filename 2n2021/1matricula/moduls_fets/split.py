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
import img

def split_digit(img):
    for i in range(len(img[1])):
        p = 0
    for j in range(len(img[1][i])):
        if img[1][j][i]==(0,0,0):
            oh = 0
            ow = j-1
            pixel = True
        elif img[1][j][i]==(255,255,255):
            p += 1
            if p == len(img[1][j]) and pixel:
                w=j
                h=len(img[1])
                return subimg(img,ow,oh,w,h),subimg(img,ow=w,oh=h,w=len(img[1][0]),h=len(img[1]))