#!/usr/bin/env python
# -*- coding: utf-8 -*-

from tkinter import *
from tkinter import ttk, font
import getpass


# Gestor de geometría (place)

class Aplicacion():
    def __init__(self):
        self.arrel = Tk()

        # Definiex la dimensió de la finestra

        self.arrel.geometry("430x200")

        # Estableix que no es pot canviar el tamany de la finestra

        self.arrel.resizable(0, 0)
        self.arrel.title("Accés")
        self.font1 = font.Font(weight='bold')
        self.etiq1 = ttk.Label(self.arrel, text="Usuari:",
                               font=self.font1)
        self.etiq2 = ttk.Label(self.arrel, text="Contrasenya:",
                               font=self.font1)

        # Declarem una variable que se li assigna
        # l'opció 'textvariable' d'un widget 'Label' per
        # mostrar missatges a la finestra. S'assigna el color
        # blau a l'opció 'foreground' per el missatge.

        self.mensa = StringVar()
        self.etiq3 = ttk.Label(self.arrel, textvariable=self.mensa,
                               font=self.font1, foreground='blue')

        self.Usuari = StringVar()
        self.clave = StringVar()
        self.Usuari.set(getpass.getuser())
        self.ctext1 = ttk.Entry(self.arrel,
                                textvariable=self.Usuari, width=30)
        self.ctext2 = ttk.Entry(self.arrel,
                                textvariable=self.clave,
                                width=30,
                                show="*")
        self.separ1 = ttk.Separator(self.arrel, orient=HORIZONTAL)
        self.boton1 = ttk.Button(self.arrel, text="Aceptar",
                                 padding=(5, 5), command=self.aceptar)
        self.boton2 = ttk.Button(self.arrel, text="Cancelar",
                                 padding=(5, 5), command=quit)

        # Es defineixen les ubicacions dels widgets a la
        # finestra assignant els valors de les opciones 'x' e 'y'
        # en píxels.

        self.etiq1.place(x=30, y=40)
        self.etiq2.place(x=30, y=80)
        self.etiq3.place(x=150, y=120)
        self.ctext1.place(x=150, y=42)
        self.ctext2.place(x=150, y=82)
        self.separ1.place(x=5, y=145, bordermode=OUTSIDE,
                          height=10, width=420)
        self.boton1.place(x=170, y=160)
        self.boton2.place(x=290, y=160)
        self.ctext2.focus_set()

        # El metode 'bind()' associa l'event de 'fer click
        # esquerre del ratolí a la caixa d'entrada
        # de la Contrasenya' expressat amb '<button-1>' amb el
        # mètode 'self.borrar_mensa' que esborra el missatge i la
        # Contrasenya i torna el focus al mateix control.
        # Altres exemples d'accions que es poden capturar:
        # <double-button-1>, <buttonrelease-1>, <enter>, <leave>,
        # <focusin>, <focusout>, <return>, <shift-up>, <key-f10>,etc


        self.ctext2.bind('<Button-1>', self.borrar_mensa)
        self.arrel.mainloop()

    # Declarem mètode per validar el Password i mostrar
    # un missatge a la propia finestra, utilizant l'etiqueta
    # 'self.mensa'. Quan el password es correcte
    # assignem el color blau a la etiqueta 'self.etiq3' i
    # quan és incorrecte el color vermell. Per això, s'emplea
    # el mètode 'configure()' que permet canviar els valors
    # de les opcions dels widgets.

    def aceptar(self):
        if self.clave.get() == 'tkinter':
            self.etiq3.configure(foreground='blue')
            self.mensa.set("Accés permés")
        else:
            self.etiq3.configure(foreground='red')
            self.mensa.set("Accés denegat")

    # Declara un mètode per esborrar el missatge anterior i
    # la caixa d'entrada de la Contrasenya

    def borrar_mensa(self, evento):
        self.clave.set("")
        self.mensa.set("")


def main():
    mi_app = Aplicacion()
    return 0


main()