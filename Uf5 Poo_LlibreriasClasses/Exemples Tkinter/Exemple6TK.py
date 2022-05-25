#!/usr/bin/env python
# -*- coding: utf-8 -*-

from tkinter import *
from tkinter import ttk, font
import getpass


# Gestor de geometría (grid). Finestra dimensionable

class Aplicacio():
    def __init__(self):
        self.arrel = Tk()
        self.arrel.title("Accés")
        font1 = font.Font(weight='bold')
        self.marc = ttk.Frame(self.arrel, borderwidth=2,
                               relief="raised", padding=(10, 10))
        self.etiq1 = ttk.Label(self.marc, text="Usuari:",
                               font=font1, padding=(5, 5))
        self.etiq2 = ttk.Label(self.marc, text="Contrasenya:",
                               font=font1, padding=(5, 5))
        self.usuari = StringVar()
        self.clau = StringVar()
        self.usuari.set(getpass.getuser())
        self.ctext1 = ttk.Entry(self.marc, textvariable=self.usuari,
                                width=30)
        self.ctext2 = ttk.Entry(self.marc, textvariable=self.clau,
                                show="*", width=30)
        self.separ1 = ttk.Separator(self.marc, orient=HORIZONTAL)
        self.boton1 = ttk.Button(self.marc, text="Aceptar",
                                 padding=(5, 5), command=self.aceptar)
        self.boton2 = ttk.Button(self.marc, text="Cancelar",
                                 padding=(5, 5), command=quit)

        # Per aconseguir que la quadricula i els widgets
        # s'adaptin al contenidor, si s'amplia o redueix el tamany
        # de la finestra, és necessari definir la opció 'sticky'.
        # Quan un widget s'ubica al grid es col·loca al
        # centre del quadre. Amb 'sticky' s'estableix
        # que s'enganxin els widgets dins del quadre.
        # Quan es modifiqua la dimensió de la finestra.
        # Per això, s'utilizen per expressar
        # els seus valors els punts cardinals: N (Nord),
        # S (Sud), (E) Est i (W) Oest (també es poden combinar)
        # El widget quedarà 'enganxat' als  costats de la seva cel·la
        # en la direcció que indiquem, Quan la finestra canvia de tamany.
        # No és suficient definir la opció 'sticky'
        # S'ha d'activar la propietat més endavant.

        self.marc.grid(column=0, row=0, padx=5, pady=5,
                        sticky=(N, S, E, W))
        self.etiq1.grid(column=0, row=0,
                        sticky=(N, S, E, W))
        self.ctext1.grid(column=1, row=0, columnspan=2,
                         sticky=(E, W))
        self.etiq2.grid(column=0, row=1,
                        sticky=(N, S, E, W))
        self.ctext2.grid(column=1, row=1, columnspan=2,
                         sticky=(E, W))
        self.separ1.grid(column=0, row=3, columnspan=3, pady=5,
                         sticky=(N, S, E, W))
        self.boton1.grid(column=1, row=4, padx=5,
                         sticky=(E))
        self.boton2.grid(column=2, row=4, padx=5,
                         sticky=(W))

        # A continuació, s'activa la propietat d'expandir-se
        # o contraure definida abans amb l'opció
        # 'sticky' del método grid().
        # L'activació es fa per contenidors i per files
        # i columnes assignant un pes a la opció 'weight'.
        # Aquesta opció assigna un pes (relatiu) que s'utiliza
        # per distribuir l'espai addicional entre columnes
        # i/o files. Quan fem gran la finestra, una columna
        # o fila con un pes 2 creixerà duos vegades més ràpid
        # que una columna (o fila) amb pes 1. El valor
        # predeterminat és 0 que significa que la columna o
        # o filera no creixerà res en absolut.
        # L'habitual és assignar pesos a files o columnes on
        # hi han cel·les amb widgets.

        self.arrel.columnconfigure(0, weight=1)
        self.arrel.rowconfigure(0, weight=1)
        self.marc.columnconfigure(0, weight=1)
        self.marc.columnconfigure(1, weight=1)
        self.marc.columnconfigure(2, weight=1)
        self.marc.rowconfigure(0, weight=1)
        self.marc.rowconfigure(1, weight=1)
        self.marc.rowconfigure(4, weight=1)

        # Fiquem el focus al password

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