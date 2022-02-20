#!/usr/bin/env python
# -*- coding: utf-8 -*-

from tkinter import *
from tkinter import ttk, font
import getpass


# Gestor de geometría (pack)

class Aplicacion():
    def __init__(self):
        self.arrel = Tk()
        self.arrel.title("Accés")

        # Canviem format de font a negreta per
        # resaltar les dos etiquetes que acompanyen a les caixes
        # d'entrada. S'ha d'importar llibreria font.

        font1 = font.Font(weight='bold')

        # Definim etiquetes que acompanyen a les caixes
        # d'entrada y assigna el format de font1 anterior:

        self.etiq1 = ttk.Label(self.arrel, text="Usuari:",
                               font=font1)
        self.etiq2 = ttk.Label(self.arrel, text="Contrasenya:",
                               font=font1)

        # Dos variables de tipus StringVar per contenir
        # usuari i la contrasenya:

        self.usuari = StringVar()
        self.clave = StringVar()

        # Realizem lectura del nom d'usuari que
        # ha iniciat sessió al sistema i assignem a la
        # variable 'self.usuari' (Per capturar aquesta
        # informació importem mòdul getpass
        # al inici del programa):

        self.usuari.set(getpass.getuser())

        # Definim dues caixes d'entrada que acceptaran cadenes
        # d'una longitud màxima de 30 caracters.
        # A la primera  'self.ctext1' fiquem
        # el nom d'usuari, amb la variable
        # 'self.usuari' a la opció 'textvariable'. 
        # A la segona caixa d'entrada, la del password,
        # es fa el mateix. A més, fem servir la opció
        # 'show' amb un "*" per ocultar el password:

        self.ctext1 = ttk.Entry(self.arrel,
                                textvariable=self.usuari,
                                width=30)
        self.ctext2 = ttk.Entry(self.arrel,
                                textvariable=self.clave,
                                width=30, show="*")
        self.separ1 = ttk.Separator(self.arrel, orient=HORIZONTAL)

        # Definim dos botons amb dos métodes: El botó
        # 'Acceptar' cridarà al mètode 'self.acceptar' quan sigui
        # clickat para validar la contrasenya; y el botó
        # 'Cancelar' finalitzarà l'aplicació si el clickem:

        self.boton1 = ttk.Button(self.arrel, text="Acceptar",
                                 command=self.acceptar)
        self.boton2 = ttk.Button(self.arrel, text="Cancelar",
                                 command=quit)

        # Definim les posicions els widgets dintre de
        # la finestra. Tots els controls es van colocant
        # a la part de dalt, excepte, els dos últims,
        # els botons, que estaran a la part de baix.
        # el primer botó cap a l'esquerra i el
        # segon la dreta.
        # Els valors possibles per la opció 'side' son:
        # TOP (a dalt), BOTTOM (a baix), LEFT (esquerra)
        # i RIGHT (dreta). Si s'omite, el valor serà TOP
        # La opció 'fill' s'utiliza per indicar al gestor
        # com expandir/reduir el widget si la finestra canvia
        # de tamany. Té tres possibles valors: BOTH
        # (Horitzontal i Vertical), X (Horizontal) e
        # Y (Vertical). Funcionarà si el valor de l'opció
        # 'expand' es True.
        # Por últim, les opciones 'padx' i 'pady' s'utilizan
        # per afegir espai extra extern horizontal i/o
        # vertical als widgets per separar-los entre ells i dels
        # marges de la finestra. Hi ha altres equivalents que
        # afegeixen espai extra intern: 'ipadx' y 'ipady':

        self.etiq1.pack(side=TOP, fill=BOTH, expand=True,
                        padx=5, pady=5)
        self.ctext1.pack(side=TOP, fill=X, expand=True,
                         padx=5, pady=5)
        self.etiq2.pack(side=TOP, fill=BOTH, expand=True,
                        padx=5, pady=5)
        self.ctext2.pack(side=TOP, fill=X, expand=True,
                         padx=5, pady=5)
        self.separ1.pack(side=TOP, fill=BOTH, expand=True,
                         padx=5, pady=5)
        self.boton1.pack(side=LEFT, fill=BOTH, expand=True,
                         padx=5, pady=5)
        self.boton2.pack(side=RIGHT, fill=BOTH, expand=True,
                         padx=5, pady=5)

        # Quan s'inicia el programa se li assigna el focus
        # a la caixa d'entrada de la contrasenya per a que es
        # pugui començar a escriure directament:

        self.ctext2.focus_set()

        self.arrel.mainloop()

    # El mètode 'acceptar' es fa servir per validar el
    # password introduit. Serà cridat quan es
    # presioni el botó 'Acceptar'. Si la contrasenya
    # coincideix amb la cadena 'tkinter' s'imprimirà
    # el mmissatge 'Acces permés' i els valors
    # acceptats. En cas contrari, es mostrarà el
    # mmissatge 'Accés denegat' i el focus tornarà al
    # mateix lloc.

    def acceptar(self):
        if self.clave.get() == 'tkinter':
            print("Accés permès")
            print("Usuari:   ", self.ctext1.get())
            print("Contrasenya:", self.ctext2.get())
        else:
            print("Accés denegat")

            # Inicialitzem la variable 'self.clave' per
            # que el widget 'self.ctext2' quedi net.
            # Per últim, es torna a assignar assignar el focus
            # a aquest widget per poder escriure un nou password

            self.clave.set("")
            self.ctext2.focus_set()


def main():
    mi_app = Aplicacion()
    return 0


main()