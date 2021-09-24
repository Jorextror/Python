import tkinter as tk
import os
from tkinter import filedialog

my_filetypes = [('python', '.py'), ('html', '.html'), ('text files', '.txt')]
def open_folder():
    answer = filedialog.askopenfilename(parent=root,
                                    initialdir=os.getcwd(),
                                    title="Please select a file:",
                                    filetypes=my_filetypes)
    try:
        text.delete("1.0", tk.END)
        with open(answer) as file:
            text.insert("1.0", file.read())
    except FileNotFoundError:
        print("file not found")

def convert_reverse(x):
    tags = [
        ("</table>",""),
        ("<!-- table -->",""),
        ("<table border=1>",""),
        ("<td>","\t"),
        ("</td>", ""),
        ("<tr>", "\n")]
    for tag in tags:
        x = x.replace(tag[0], tag[1])
    return x

html = ""
def table(x):
    global html
    if "<table" in x:
        return convert_reverse(x)
    html = ""
    """ Create table with data in a multiline
    string as first argument x)"""
    html += "<table border=1>"
    for line in x.splitlines():
        for n in line.split("\t"):
            if n == "":
                continue
            html += f"<td>{n}</td>"
        html += "<tr>"
    html += "</table>"
    return html

def create(a):
    tab = table(text.get("1.0", tk.END))
    #text.delete("1.0", tk.END)
    text2.insert("1.0", tab)
    label['text'] = "Now you can copy the html code for the table (ctrl + a)"

def save_html():
    if html != "":
        with open("table.html", "w", encoding="utf-8") as file:
            file.write(text2.get("1.0", tk.END))

def show_html():
    if os.path.exists("table.html"):
        os.startfile("table.html")

def convert_to_html():
    html = table(text.get("1.0",tk.END))
    clear2()
    text2.insert("1.0", html)

def clear2():
    text2.delete("1.0", tk.END)

def clear():
    text.delete("1.0", tk.END)
    text2.delete("1.0", tk.END)

root = tk.Tk()
root.title("Html table converter")
label = tk.Label(root, text="Copy data from Excel and insert them here separated by tabs")
label.pack()
text = tk.Text(root)
text.pack(fill=tk.BOTH, expand=1)
text.bind("<Control-p>", create)
text.focus()
label2 = tk.Label(root, text="Press ctr+p and you'll get the html code here")
label2.pack()
text2 = tk.Text(root, bg='gold')
text2.pack(fill=tk.BOTH, expand=1)
# create a toplevel menu 
menubar = tk.Menu(root)
menubar.add_command(label="Open", command=open_folder)
menubar.add_command(label="Convert", command=convert_to_html)
menubar.add_command(label="Save", command=save_html)
menubar.add_command(label="Show", command=show_html)
menubar.add_command(label="Clear", command=clear)
# display the menu
root.config(menu=menubar)
root.mainloop()
1
2
3
4
5
6
7
8
9
10
11
12
13
14
15
16
17
18
19
20
21
22
23
24
25
26
27
28
29
30
31
32
33
34
35
36
37
38
39
40
41
42
43
44
45
46
47
48
49
50
51
52
53
54
55
56
57
58
59
60
61
62
63
64
65
66
67
68
69
70
71
72
73
74
75
76
77
78
79
80
81
82
83
84
85
86
87
88
89
90
91
92
93
94
95
96
97
import tkinter as tk
import os
from tkinter import filedialog

my_filetypes = [('python', '.py'), ('html', '.html'), ('text files', '.txt')]
def open_folder():
    answer = filedialog.askopenfilename(parent=root,
                                    initialdir=os.getcwd(),
                                    title="Please select a file:",
                                    filetypes=my_filetypes)
    try:
        text.delete("1.0", tk.END)
        with open(answer) as file:
            text.insert("1.0", file.read())
    except FileNotFoundError:
        print("file not found")

def convert_reverse(x):
    tags = [
        ("</table>",""),
        ("<!-- table -->",""),
        ("<table border=1>",""),
        ("<td>","\t"),
        ("</td>", ""),
        ("<tr>", "\n")]
    for tag in tags:
        x = x.replace(tag[0], tag[1])
    return x
 
html = ""
def table(x):
    global html
    if "<table" in x:
        return convert_reverse(x)
    html = ""
    """ Create table with data in a multiline
    string as first argument x)"""
    html += "<table border=1>"
    for line in x.splitlines():
        for n in line.split("\t"):
            if n == "":
                continue
            html += f"<td>{n}</td>"
        html += "<tr>"
    html += "</table>"
    return html

def create(a):
    tab = table(text.get("1.0", tk.END))
    #text.delete("1.0", tk.END)
    text2.insert("1.0", tab)
    label['text'] = "Now you can copy the html code for the table (ctrl + a)"

def save_html():
    if html != "":
        with open("table.html", "w", encoding="utf-8") as file:
            file.write(text2.get("1.0", tk.END))

def show_html():
    if os.path.exists("table.html"):
        os.startfile("table.html")

def convert_to_html():
    html = table(text.get("1.0",tk.END))
    clear2()
    text2.insert("1.0", html)

def clear2():
    text2.delete("1.0", tk.END)

def clear():
    text.delete("1.0", tk.END)
    text2.delete("1.0", tk.END)

root = tk.Tk()
root.title("Html table converter")
label = tk.Label(root, text="Copy data from Excel and insert them here separated by tabs")
label.pack()
text = tk.Text(root)
text.pack(fill=tk.BOTH, expand=1)
text.bind("<Control-p>", create)
text.focus()
label2 = tk.Label(root, text="Press ctr+p and you'll get the html code here")
label2.pack()
text2 = tk.Text(root, bg='gold')
text2.pack(fill=tk.BOTH, expand=1)
# create a toplevel menu 
menubar = tk.Menu(root)
menubar.add_command(label="Open", command=open_folder)
menubar.add_command(label="Convert", command=convert_to_html)
menubar.add_command(label="Save", command=save_html)
menubar.add_command(label="Show", command=show_html)
menubar.add_command(label="Clear", command=clear)
# display the menu
root.config(menu=menubar)
root.mainloop()