"""El modul conte les operacions primaries pel treball amb imatges, 
ja siguin imatges RGB, d’escala de grisos o de blanc i negre. """
#from typing_extensions import _AnnotatedAlias
# import PIL
# from PIL import Image, ImageChops, ImageEnhance, ImageOps
import Image


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

def format(im):
    return im[0]

def matrix(img):
    return img[1]

def im(matrix,model='DISCOVER'):
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

def get_w(im):
    return len(im[1][0])

def get_h(im):
    return len(im[1])

def subimg(im,ow,oh,w,h):
    total=[]
    total.append(im[0])
    for i in range(ow,w):
        for j in range(oh,h):
            total.append(im[1][j][i])
    return total

matrix=[[(255,255,255),(255,255,255)],[(255,255,255),(255,255,255)]]

grey= [[255, 255, 0 ],
[255, 128, 255],
[191, 255, 255],
[255, 255, 0 ],
[255, 128, 255],
[191, 255, 255]]

print(subimg(grey,1,0,1,5))