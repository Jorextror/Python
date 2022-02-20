#!/usr/bin/env python
# -*- coding: utf-8 -*-

from tkinter import *
from tkinter import ttk

# Creem una classe Python per definir la interfaç d'usuari de
# l'aplicació. Quan es crea un objete del tipus 'Aplicacio'
# s'executa automàticament el mètode __init__() que
# construeix i mostra la finestra amb tots els seus widgets:

class Aplicacio():
    def __init__(self):
        arrel = Tk()
        arrel.geometry('300x200')
        arrel.configure(bg = 'beige')
        arrel.title('Aplicació')
        ttk.Button(arrel, text='Sortir',
                   command=arrel.destroy).pack(side=BOTTOM)
        arrel.mainloop()

# Defineix la funció main() que es en realitat la que indica
# l'inici del programa. A dins creem l'objete
# aplicació 'mi_app' basat en la classe 'Aplicacio':

def main():
    mi_app = Aplicacio()
    return 0


main()