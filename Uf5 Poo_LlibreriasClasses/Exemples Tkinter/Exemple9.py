#!/usr/bin/env python
# -*- coding: utf-8 -*-

from tkinter import *
from tkinter import ttk


class Aplicacio():
    finestra = 0
    posx_y = 0

    def __init__(self):
        self.arrel = Tk()
        self.arrel.geometry('300x200+500+50')
        self.arrel.resizable(0, 0)
        self.arrel.title("Finestra d'aplicació")
        boton = ttk.Button(self.arrel, text='Obrir',
                           command=self.abrir)
        boton.pack(side=BOTTOM, padx=20, pady=20)
        self.arrel.mainloop()

    def abrir(self):
        ''' Construeix una finestra de diàlog'''

        self.dialeg = Toplevel()
        Aplicacio.finestra += 1
        Aplicacio.posx_y += 50
        tamypos = '200x100+' + str(Aplicacio.posx_y) + \
                  '+' + str(Aplicacio.posx_y)
        self.dialeg.geometry(tamypos)
        self.dialeg.resizable(0, 0)
        ident = self.dialeg.winfo_id()
        titol = str(Aplicacio.finestra) + ": " + str(ident)
        self.dialeg.title(titol)
        boton = ttk.Button(self.dialeg, text='Tancar',
                           command=self.dialeg.destroy)
        boton.pack(side=BOTTOM, padx=20, pady=20)

        # Convertim la finestra 'self.dialeg' en
        # transitoria respecte la finestra mare
        # 'self.arrel'.
        # Una finestra transitoria sempre es mostra sobre
        # la mare i s'ocultarà quam la mare sigui minimitzada.
        # Si l'argument 'master' es
        # omés el valor, per defecte, serà la finestra
        # mare.

        self.dialeg.transient(master=self.arrel)

        # El mètode grab_set() assegura que no hi han events
        # de ratolí o teclat que s'enviín a l'altre finestra
        # diferent a 'self.dialeg'. S'utilitza per
        # crear una finestra de tipus modal que serà
        # necessari tancar per poder trabajar amb un altre
        # diferent. Amb això, també impedim que la
        # mateixa finestra s'obri diverses vegades.

        self.dialeg.grab_set()
        self.arrel.wait_window(self.dialeg)


def main():
    mi_app = Aplicacio()
    return (0)


if __name__ == '__main__':
    main()