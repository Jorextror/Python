"""Aquest m`odul encapsula diverses funcions que permeten fer transformacions a les imatges. Les
funcions s ́on les seg ̈uents:"""
from PIL import Image as img
import img 
import imgio

def vtrim(img):
    """Donada una imatge img en blanc i negre, retorna l’imatge resultant de retallar-la verticalment.
    Per retall vertical s’ent ́en extreure la sub-imatge que, en la dimensi ́o vertical encabeix de
    forma exacta els digits. Amb aixo s’aconsegueix que els d ́ıgits de la matricula quedin ben
    “enquadrats” verticalment. Si la imatge nom ́es cont ́e blancs, retorna una imatge nul.
    la."""
    for i in range(len(img[1])): 
        detectat=False
        for i in range(len(img[1])): 
              p = 0
        for j in range(len(img[1][j])):
            if img[1][i][j]==(0,0,0):
                ow = 0
                oh = p-1
                detectat = True
            elif img[1][i][j]==(255,255,255):
                i += 1
                if p == len(img[1][j]) and detectat:
                    w=len(img[1][j])
                    h=i
                    return subimg(img,ow,oh,w,h)

def htrim(img):
    """Fa una feina similar a la funci ́o vtrim() per`o en la direcci ́o horitzontal."""
    i=0
    j=0
    fi=len(img[1][0][1])
    fj=len(img[1])
    VI=False
    VF=False
    while not VI and not VF:
        if img[1][j][i] == (0,0,0) or not VI:
            oh=0
            ow=i-1
            VI=True
        
        if img[1][fj][fi] == (0,0,0) or not VF:
            h=len(img[1])
            w=i-1
            VF=True
        j+=1
        i+=1
        fi-=1
        fj-=1
    return subimg(img,ow,oh,w,h)

def scale(src, h):
    """
    Escala la imatge a l'alçada `h` conservant l'aspect ratio
    """
    # Compute src and dst sizes
    src_h = img.get_h(src)
    src_w = img.get_w(src)

    # Scaling factor
    fh = float(src_h) / h

    # dst dimension
    dst_h = h
    dst_w = int(round(src_w / fh))

    # Mostrejem matriu original
    sm = img.matrix(src)
    dst = [ [sm[int(round(fh*h))][int(round(fh*w))] for w in range(dst_w)] for h in range(dst_h)]
    return img.img(dst, '1')