"""El modul conte les operacions primaries pel treball amb imatges, 
ja siguin imatges RGB, d’escala de grisos o de blanc i negre. """
import discret
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
    return img.mode

def matrix(img):
    m = [[img[x,y] for x in range(len(y))] for y in range(len(img))]

def img(matrix,model='DISCOVER'):
    if model == "DISCOVER":
        model.format(matrix)
    m = [[matrix[x,y] for x in range(len(y))] for y in range(len(matrix))]

def get_w(img):
    return img.size[0]

def get_h(img):
    return img.size[1]
