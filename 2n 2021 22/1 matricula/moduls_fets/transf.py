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
    im=subimg(img)
    for i in range(len(im)):
        for j in range(len(i)):
            

def htrim(img):
    """Fa una feina similar a la funci ́o vtrim() per`o en la direcci ́o horitzontal."""
    

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
