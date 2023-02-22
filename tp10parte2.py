from tkinter import *


inicio = Tk()
elemento = StringVar()

titulo_Superior = Label(inicio, text='Lista de lenguajes de programación', bg='purple', fg= 'white', padx= 20, pady= 20)
titulo_Superior.pack(fill= 'x')

lista = Listbox(inicio, border= 30, background= 'red', foreground= 'white')

for item in ['Python', 'Java', 'JavaScrip', 'C++', 'Goland', 'Ruby']:
    lista.insert(END, item)

lista.pack()

fin = Label(inicio, text='Gracias por evaluarme', bg='green', fg= 'white', padx= 20, pady= 20)
fin.pack(fill='x')

inicio.mainloop()