#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Compatible amb versions anteriors

from tkinter import *    # Carga módulo tk (widgets estándar)
from tkinter import ttk  # Carga ttk (per widgets nous 8.5+)

# Primera aplicació TKinter
# Definim finestra principal aplicació

arrel = Tk()

# Defineix dimensions de la finestra. Si s'omet aquesta esta linea la
# finestra d'adapta al contingut que coloquem

arrel.geometry('300x200') # ample x alt

# Assignem un color de fons. Si s'omet, será gris

arrel.configure(bg = 'beige')

# Assignem títol

arrel.title('Aplicació')

# Definim un botó a la part inferior per finalitzar el programa
# El primer paràmetre indica el nom de la finestra 'arrel'
# on estarà el botó

ttk.Button(arrel, text='Sortir', command=quit).pack(side=BOTTOM)

# Després de definir la finestra principal i un widget botó,
# fem que quan s'executi el programa.
# Construeix i mostra la finestra i queda a l'espera de
# que alguna persona interactui amb ella.

# Si clickem el botó Sortir o 'X' es tanca el programa.

arrel.mainloop()