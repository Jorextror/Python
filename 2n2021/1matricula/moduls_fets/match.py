"""Es el m`odul que s’encarrega de determinar a quina xifra representa una imatge concreta."""
from typing import ForwardRef
from PIL import Image
from img import subimg
import os

def load_patterns(prefix):
    """Aquesta funci ́o rep com a par`ametre el prefix dels noms dels fitxers que contenen els patrons
    dels d ́ıgits i retorna la llista d’imatges corresponent als patrons dels d ́ıgits ordenats de 0 a 9.
    Per exemple, si l’argument  ́es patro voldr`a dir que els arxius dels patrons que s’hauran de
    llegir s’anomenaran: patro_0.jpeg, patro_1.jpeg, . . . , patro_9.jpeg."""

    contenido = os.listdir('2n2021/1matricula/patrons')
    print(contenido)

# def match(img,patlst):
    
load_patterns(prefix=2)