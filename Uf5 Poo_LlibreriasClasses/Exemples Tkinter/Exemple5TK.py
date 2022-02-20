#!/usr/bin/env python
# -*- coding: utf-8 -*-

from tkinter import *
from tkinter import ttk, font
import getpass


# Gestor de geometría (grid). Finestra no dimensionable

class Aplicacio():
    def __init__(self):
        self.arrel = Tk()
        self.arrel.title("Accés")

        # Fem que no es pugui modificar el tamany de la
        # finestra. El metode resizable(0,0) és la forma abreujada
        # de resizable(width=False,height=False).

        self.arrel.resizable(0, 0)
        font1 = font.Font(weight='bold')

        # Definim un widget de tipus 'Frame' (marc) que serà el
        # contenidor de la resta de widgets. El marc el situem
        # a la finestra 'self.arrel' ocupant tota l'extensió.
        # El marc es defineix amb un voltant de 2 píxels i la
        # opció 'relief' amb el valor 'raised' (elevat) afegeix
        # un efecto 3D a su voltant.
        # La opció 'relief' permet els següents valors:
        # FLAT (pla), RAISED (elevat), SUNKEN (enfonsat),
        # GROOVE (forat) y RIDGE (voltant elevat).
        # L'opció 'padding' afegeix espai extra interior per
        # a que els widgets no quedin pegats al voltant del marc.

        self.marc = ttk.Frame(self.arrel, borderwidth=2,
                               relief="raised", padding=(10, 10))

        # Definim la resta de widgets però en aquest cas el primer
        # paràmetre indica que es situaà en el widget del
        # marc anterior 'self.marc'.

        self.etiq1 = ttk.Label(self.marc, text="usuari:",
                               font=font1, padding=(5, 5))
        self.etiq2 = ttk.Label(self.marc, text="Contraseña:",
                               font=font1, padding=(5, 5))

        # Definim variables per les opcions 'textvariable' de
        # cada caixa d'entrada 'ttk.Entry()'.

        self.usuari = StringVar()
        self.clau = StringVar()
        self.usuari.set(getpass.getuser())
        self.ctext1 = ttk.Entry(self.marc, textvariable=self.usuari,
                                width=30)
        self.ctext2 = ttk.Entry(self.marc, textvariable=self.clau,
                                show="*",
                                width=30)
        self.separ1 = ttk.Separator(self.marc, orient=HORIZONTAL)
        self.boton1 = ttk.Button(self.marc, text="Aceptar",
                                 padding=(5, 5), command=self.aceptar)
        self.boton2 = ttk.Button(self.marc, text="Cancelar",
                                 padding=(5, 5), command=quit)

        # Definim la ubicació de cada widget al grid (cuadrícula).
        # En aquest exemple tenim dos grid (cuadrícules):
        # Una cuadrícula de 1fx1c que està a la finestra
        # que ocuparà el Frame; i l'altre en el Frame de 5fx3c per
        # la resta de controls.
        # La primera filera i primera columna seran la número 0.
        # L'opció 'column' indica el número de columna i
        # l'opció 'row' indica el número de fila on s'ha de col·locar el widget.
        # L'opción 'columnspan' indica al gestor que el
        # widget ocuparà en total un número determinat de
        # columnes. Les caixes per entrades 'self.ctext1' i
        # 'self.ctext2' ocuparan dues columnes i la barra
        # de separació 'self.separ1' tres.

        self.marc.grid(column=0, row=0)
        self.etiq1.grid(column=0, row=0)
        self.ctext1.grid(column=1, row=0, columnspan=2)
        self.etiq2.grid(column=0, row=1)
        self.ctext2.grid(column=1, row=1, columnspan=2)
        self.separ1.grid(column=0, row=3, columnspan=3)
        self.boton1.grid(column=1, row=4)
        self.boton2.grid(column=2, row=4)

        # Fiquem el focus a la caixa d'entrada del
        # password.

        self.ctext2.focus_set()
        self.arrel.mainloop()

    def aceptar(self):
        if self.clau.get() == 'tkinter':
            print("Accés permès")
            print("Usuari:   ", self.ctext1.get())
            print("Contrasenya:", self.ctext2.get())
        else:
            print("Accés denegat")
            self.clau.set("")
            self.ctext2.focus_set()


def main():
    mi_app = Aplicacio()
    return 0



main()