from audioop import mul
from tkinter import *
from tkinter import ttk
from turtle import width

# from click import command

root = Tk()
root.title("CALCULADORA")
root.geometry("287x290")
root.resizable(width=False, height=False)
#root.iconbitmap("../icon/calculator_3534.ico")

def setTextInput(text):
   anterior = entry.get()
   entry.delete(0, END)
   entry.insert(0, str(anterior) + str(text))   

def suma():
   global num1
   global operacio
   num1 = entry.get()
   num1 = float(num1)
   entry.delete(0,END)
   operacio = "+"

def resta():
   global num1
   global operacio
   num1 = entry.get()
   num1 = float(num1)
   entry.delete(0,END)
   operacio = "-"

def multiplicacio():
   global num1
   global operacio
   num1 = entry.get()
   num1 = float(num1)
   entry.delete(0,END)
   operacio = "*"

def dividir():
   global num1
   global operacio
   num1 = entry.get()
   num1 = float(num1)
   entry.delete(0,END)
   operacio = "/"

def MOD():
   global num1
   global operacio
   num1 = entry.get()
   num1 = float(num1)
   entry.delete(0,END)
   operacio = "%"


def igual():
    global num2
    num2 = entry.get()
    entry.delete(0, END)

    if operacio == "+":
        entry.insert(0, num1 + float(num2))
    if operacio == "-":
        entry.insert(0, num1 - float(num2))
    if operacio == "*":
        entry.insert(0, num1 * float(num2))
    if operacio == "/":
        entry.insert(0, num1 / float(num2))
    if operacio == "%":
        entry.insert(0, num1 % float(num2))


def buidar():
   entry.delete(0, END)

### BOTONS ###
entry = ttk.Entry(root)
entry.place(x=5, y=5, width=275, height=50)

btt1 = ttk.Button(text="C", command=buidar)
btt1.place(x=5, y=60, width=65, height=40)

btt2 = ttk.Button(text="7", command=lambda:setTextInput("7"))
btt2.place(x=5, y=105, width=65, height=40)

btt2 = ttk.Button(text="4", command=lambda:setTextInput("4"))
btt2.place(x=5, y=150, width=65, height=40)

btt3 = ttk.Button(text="1",command=lambda:setTextInput("1"))
btt3.place(x=5, y=195, width=65, height=40)

btt4 = ttk.Button(text="DEL")
btt4.place(x=75, y=60, width=65, height=40)

btt5 = ttk.Button(text="8", command=lambda:setTextInput("8"))
btt5.place(x=75, y=105, width=65, height=40)

btt6 = ttk.Button(text="5", command=lambda:setTextInput("5"))
btt6.place(x=75, y=150, width=65, height=40)

btt7 = ttk.Button(text="2", command=lambda:setTextInput("2"))
btt7.place(x=75, y=195, width=65, height=40)

btt8 = ttk.Button(text="0", command=lambda:setTextInput("0"))
btt8.place(x=75, y=240, width=65, height=40)

btt9 = ttk.Button(text="0", command=lambda:setTextInput("0"))
btt9.place(x=75, y=240, width=65, height=40)

btt10 = ttk.Button(text="%", command=MOD)
btt10.place(x=145, y=60, width=65, height=40)

btt11 = ttk.Button(text="9", command=lambda:setTextInput("9"))
btt11.place(x=145, y=105, width=65, height=40)

btt12 = ttk.Button(text="6", command=lambda:setTextInput("6"))
btt12.place(x=145, y=150, width=65, height=40)

btt13 = ttk.Button(text="3", command=lambda:setTextInput("3"))
btt13.place(x=145, y=195, width=65, height=40)

btt14 = ttk.Button(text=".", command=lambda:setTextInput("."))
btt14.place(x=145, y=240, width=65, height=40)

btt15 = ttk.Button(text="/", command=dividir)
btt15.place(x=215, y=60, width=65, height=40)

btt16 = ttk.Button(text="x", command=multiplicacio)
btt16.place(x=215, y=105, width=65, height=40)

btt17 = ttk.Button(text="-", command=resta)
btt17.place(x=215, y=150, width=65, height=40)

btt18 = ttk.Button(text="+", command=suma)
btt18.place(x=215, y=195, width=65, height=40)

btt19 = ttk.Button(text="=", command=igual)
btt19.place(x=215, y=240, width=65, height=40)

root.mainloop()