# Aquesta tasca consisteix en implementar una calculadora simple (*, /, +, -) 
# utilitzant Tkinter i funcions lambda.

# Ha de tenir àrees de text i botons; i l'àrea de text no ha de ser editable 
# (els valors els introduïm amb els botons).

from tkinter import *    # Carga módulo tk (widgets estándar)
from tkinter import ttk  # Carga ttk (per widgets nous 8.5+)
from tkinter import Text,Button,END

class Aplicacion():
    def __init__(self):
        self.arrel = Tk()
        self.arrel.geometry('320x510') # ample x alt
        self.arrel.title("Calculadora")

        self.cadena = StringVar()

        self.pantalla=Text(state="disabled", width=40, height=3, background="orchid", foreground="white", font=("Helvetica",15))

        #Crear los botones de la calculadora
        self.boton1 = ttk.Button(self.arrel, text="=",
                                 command=self.operar)
        



        self.arrel.mainloop()

    def operar(self):
        pass

def main():
    mi_app = Aplicacion()
    return 0

main()