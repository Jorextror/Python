from operator import mul 
from tkinter import BOTTOM, DISABLED, LEFT,END, Text, Tk, Button, TkVersion

class Calculadora:
    def __init__(self, master):
        #Configuració de la finestra
        self.master = master     
        master.title("Calculadora")
        master.resizable(width=0, height=0)
        #Caixa de text
        self.entry=Text(master, state="disabled",width=40, height=1)
        #Ubicar l'entry a la finestra
        self.entry.grid(row=0,column=0,columnspan=4,padx=5,pady=5)
        #Creació de botons
        self.buttons=[Button(master, text=char,width=9,height=1,command=lambda:self.click(char)) for char in "123*456/789-.0+C="]
        self.posicionar()
        #Creació de variables
        self.calcul=""

    def posicionar(self):
        i=0
        for fila in range(1,5):
            for columna in range(4):
                self.buttons[i].grid(row=fila,column=columna)
                i+=1
        #Ubicar l'igual al final
        self.buttons[16].grid(row=5,column=0,columnspan=4)

    def mostra(self,char):
        self.entry.configure(state="normal")
        self.entry.insert(END, char)
        self.entry.configure(state="disabled")

    def neteja(self):
        self.entry.configure(state="normal")
        self.entry.delete("1.0",END)
        self.entry.configure(state="disabled")

    def click(self,char):
        if char not in "0123456789+-/*":
            if char == "=" and self.calcul!="":
                res = str(eval(self.calcul))
                self.calcul=""
                self.neteja()
                self.mostra(res)
        elif char == "C":
            self.neteja()
        else:
            self.calcul+=str(char)
            self.mostra(char)


if __name__=="__main__":
    root = Tk()   
    miVentana = Calculadora(root)
    root.mainloop()
