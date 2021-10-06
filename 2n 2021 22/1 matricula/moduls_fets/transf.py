"""Aquest m`odul encapsula diverses funcions que permeten fer transformacions a les imatges. Les
funcions s ́on les seg ̈uents:"""
from PIL import Image
from img import subimg

def vtrim(img):
    """Donada una imatge img en blanc i negre, retorna l’imatge resultant de retallar-la verticalment.
    Per retall vertical s’ent ́en extreure la sub-imatge que, en la dimensi ́o vertical encabeix de
    forma exacta els digits. Amb aixo s’aconsegueix que els d ́ıgits de la matricula quedin ben
    “enquadrats” verticalment. Si la imatge nom ́es cont ́e blancs, retorna una imatge nul.
    la."""
    for i in range(len(img[1])):
        for j in range(len(i)):
            if img[1][i][j] == (0,0,0):

            

def htrim(img):
    """Fa una feina similar a la funci ́o vtrim() per`o en la direcci ́o horitzontal."""
    for i in range(len(img[1])): 
        wp = 0
    for j in range(len(img[1][j])):
        if img[1][j][i]==(0,0,0):
            oh = 0
            ow = j-1
            #Una vegada que es detecta un píxel negre, fa que la vegada que es detecti una línea completament blanca
            #Es retalli el caracter
            detectat = True
        elif img[1][j][i]==(255,255,255):
            #White pixel o wp, compta els píxels blancs en una línea
            wp += 1
            #Si tota la línea es de píxels blancs, vol dir que el caracter ja ha terminat, així que ho retallem
            if wp == len(img[1][j]) and detectat:
                w=j
                h=len(img[1])
    if not detectat:
        return null
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
    dst = [ [sm[int(round(fh*h))][int(round(fh*w))] for w in range(dst_w)] 
            for h in range(dst_h)]             

    return img.img(dst, '1')
