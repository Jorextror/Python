"""El modul conte les operacions primaries pel treball amb imatges, 
ja siguin imatges RGB, d’escala de grisos o de blanc i negre. """
#from typing_extensions import _AnnotatedAlias
from PIL import Image

def null():
    return ("NULL",None)

def is_null(i):
    return i == ('NULL',None)

def white_rgb(w,h):
    return("RGB",[[(255,255,255)]*w]*h)

def white_grey(w,h):
    return("L",[[(255,165,255)]*w]*h)

def white_bw(w,h):
    return("1",[[(255,255,255)]*w]*h)

def format(img):
    return img[0]

def matrix(img):
    return img[1]

def img(matrix,model='DISCOVER'):
    bn=False
    gris=False
    for i in matrix:
        for j in i:
            if j == (255,255,255) or j == (0,0,0):
                bn=True
            elif j[0]==j[1] and j[1]==j[2]:
                gris=True
            else:
                return "RGB",matrix

    if gris:
        return "1",matrix
    elif bn and gris:
        return "L",matrix

def get_w(img):
    return len(img[1][0])

def get_h(img):
    return len(img[1])

def subimg(img,ow,oh,w,h):
    total=[]
    for i in img:
        for j in i:
            if i < ow:
                if j < oh:
                    total.append(img[i][j])
    return total


matrix=[(255,255,255),(255,255,255),(255,255,255),(255,255,255)]

print(img(matrix))