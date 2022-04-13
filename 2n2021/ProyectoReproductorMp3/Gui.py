from re import S
from telnetlib import SE
from function import *
import tkinter as tk
from tkinter import N, SW, Button, ttk
class Reproductor(ttk.Frame):
    def __init__(self, master):
        super().__init__()
        #Configuració de la finestra
        self.master = master
        master.title("SoundGround")
        master.geometry("923x905") #tamaño

        master.rowconfigure(1, weight=1)
        # Button(master, text="grid1").grid(pady=5, row=0, column=0)
        # Button(master, text="grid2").grid(pady=5, row=1, column=0)

        #buttons
        Button(master, text="◄◄",width=15).grid(pady=5, row=3, column=0)
        Button(master, text="Reproduir/pausar",width=15).grid(pady=5, row=3, column=1)
        Button(master, text="►►",width=15).grid(pady=5, row=3, column=2)
        Button(master, text="+",width=5).grid(pady=5, row=3, column=3)
        Button(master, text="-",width=5).grid(pady=5, row=3, column=4)
        Button(master, text="Reset",width=15).grid(pady=5, row=3, column=5)
        # Button(master, text="◄◄",width=15).place(x=0,y=270)
        # Button(master, text="Reproduir/pausar",width=15).place(x=100,y=270)
        # Button(master, text="►►",width=15).place(x=200,y=270)
        # Button(master, text="+",width=5).place(x=300,y=270)
        # Button(master, text="-",width=5).place(x=340,y=270)
        # Button(master, text="Reset",width=15).place(x=500,y=270)

        #Listar música
        # self.treeview = ttk.Treeview(self)
        # item = self.treeview.insert("", tk.END, text="Elemento 1")
        # subitem = self.treeview.insert(item,tk.END, text="Subelemento 1")
        # self.treeview.insert(subitem, tk.END, text="Otro elemento")
        # self.treeview.pack()
        # self.pack()

        master.mainloop()