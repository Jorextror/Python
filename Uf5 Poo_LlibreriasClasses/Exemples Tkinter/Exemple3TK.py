#!/usr/bin/env python
# -*- coding: utf-8 -*-

from tkinter import *
from tkinter import ttk


# Un altre exemple que inclou nous widgets # i el constructor __init__():
# Afegim botó 'Info'  que farà la crida a al mètode 'veureinfo' per mostrar info a un altre
# widget, una caixa de text: un event executa una acció:

class Aplicacio():
    def __init__(self):
        # A l'exemple s'utilitzem el 'self' per
        # declarar variables asociades al objecte
        # ('mi_app')  de la classe 'Aplicacio'.

        self.arrel = Tk()
        self.arrel.geometry('300x200')

        # Impedim que es pugui canviar el tamany de la finestra 'self.arrel':

        self.arrel.resizable(width=False, height=False)
        self.arrel.title('Veure info')

        # Defineix el widget Text 'self.tinfo '
        # Podem introduir diverses línies de text:

        self.tinfo = Text(self.arrel, width=40, height=10)

        # Sitúem la caixa de text 'self.tinfo' a la part
        # superior de la finestra 'self.arrel':

        self.tinfo.pack(side=TOP)

        # Definim el widget Button 'self.binfo' que cridará
        # al metode 'self.veureinfo' quan el clickem

        self.binfo = ttk.Button(self.arrel, text='Info',
                                command=self.veureinfo)

        # Coloquem el botó 'self.binfo' a sota i a la esquerra
        # del widget anterior

        self.binfo.pack(side=LEFT)

        # Definim el botó 'self.bsalir'. En aquest cas
        # al clickar, el mètode tanca l'aplicació

        self.bsalir = ttk.Button(self.arrel, text='Salir',
                                 command=self.arrel.destroy)

        # Coloquem el botó 'self.bsalir' a la dreta de
        # l'objecte anterior.

        self.bsalir.pack(side=RIGHT)

        # El focus de l'aplicació el situem al botó
        # 'self.binfo'. Si se presiona
        # la barra espaciadora el botón que té el focus
        # serà pulsat. El focus pot canviar d'un widget
        # a un altre amb la tecla tabulador [tab]

        self.binfo.focus_set()
        self.arrel.mainloop()

    def veureinfo(self):
        # Esborrem el contingut que tingui la caixa de text


        self.tinfo.delete("1.0", END)

        # Obtenim informació de la finestra 'self.arrel':

        info1 = self.arrel.winfo_class()
        info2 = self.arrel.winfo_geometry()
        info3 = str(self.arrel.winfo_width())
        info4 = str(self.arrel.winfo_height())
        info5 = str(self.arrel.winfo_rootx())
        info6 = str(self.arrel.winfo_rooty())
        info7 = str(self.arrel.winfo_id())
        info8 = self.arrel.winfo_name()
        info9 = self.arrel.winfo_manager()

        # Construim una cadena de text amb tota la informació

        texto_info = "Classe d'arrel': " + info1 + "\n"
        texto_info += "Resolució i posició: " + info2 + "\n"
        texto_info += "Amplada finestra: " + info3 + "\n"
        texto_info += "Altura finestra: " + info4 + "\n"
        texto_info += "Pos. Finestra X: " + info5 + "\n"
        texto_info += "Pos. Finestra Y: " + info6 + "\n"
        texto_info += "Id. d'arrel': " + info7 + "\n"
        texto_info += "Nom objecte: " + info8 + "\n"
        texto_info += "Gestor finestres: " + info9 + "\n"

        # Inserta informació a la caixa de text.

        self.tinfo.insert("1.0", texto_info)


def main():
    mi_app = Aplicacio()
    return 0



main()