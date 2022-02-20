#!/usr/bin/env python
# -*- coding: utf-8 -*-

from tkinter import *
from tkinter import ttk


class Aplicacio():
    ''' Classe Aplicacio '''

    # Declarem una variable de classe per contar finestres

    finestra = 0

    # Declamrem una variable de classe para fer servir
    # per la posició de la finestra

    posx_y = 0

    def __init__(self):
        ''' Creem finestra d'aplicació '''

        # Declarem finestra d'aplicació

        self.arrel = Tk()

        # Definim dimensió de la finestra 300x200
        # que la situarem en la coordenada x=500,y=50

        self.arrel.geometry('300x200+500+50')

        self.arrel.resizable(0, 0)
        self.arrel.title("Finestra d'aplicació")

        # Defim botó 'Obrir' que es farà servir per
        # oobrir les finestres de diàleg. El botó
        # està vinculat amb el metòde 'self.obrir'

        boto = ttk.Button(self.arrel, text='Obrir',
                           command=self.obrir)
        boto.pack(side=BOTTOM, padx=20, pady=20)
        self.arrel.mainloop()

    def obrir(self):
        ''' Creem finestra de diàlog '''

        # Definim nova finestra de diàleg

        self.dialeg = Toplevel()

        # Incrementem en 1 el contador de finestres

        Aplicacio.finestra += 1

        # Recalculem posició de la finestra

        Aplicacio.posx_y += 50
        tamipos = '200x100+' + str(Aplicacio.posx_y) + \
                  '+' + str(Aplicacio.posx_y)
        self.dialeg.geometry(tamipos)
        self.dialeg.resizable(0, 0)

        # Obtenim identificador de la nova finestra

        ident = self.dialeg.winfo_id()

        # Construim un missatge per la barra de títol

        titol = str(Aplicacio.finestra) + ": " + str(ident)
        self.dialeg.title(titol)

        # Defiim el botó 'Tancar' que quan clickem
        # tanqui la finestra
        # 'self.dialeg' fent la crida al metòde
        # 'self.dialeg.destroy'

        boto = ttk.Button(self.dialeg, text='Tancar',
                           command=self.dialeg.destroy)
        boto.pack(side=BOTTOM, padx=20, pady=20)

        # Quan l'execució del programa arriba a aquest
        # punt, utilitzem el metòde wait_window() per
        # esperar que la finestra 'self.dialeg' sigui tancada.
        # També anem atenent events locals
        # que es produeixin. L'aplicació seguirà funcionant.
        # Si hi ha codi després d'aquesta linea, s'executarà
        # quan la finestra 'self.dialeg' ssigui tancada.

        self.arrel.wait_window(self.dialeg)


def main():
    mi_app = Aplicacio()
    return (0)


if __name__ == '__main__':
    main()