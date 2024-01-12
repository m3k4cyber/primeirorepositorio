import tkinter as tk
from tkinter.messagebox import *
from tkinter import ttk

jane = tk.Tk()
jane.geometry('400x200')
jane.title('trabajo radiobutão kk')
jane.resizable(False, False)
jane.anchor(anchor='center')
#jane.tk.call('wm','iconphoto',jane._windowingsystem, tk.PhotoImage(file='Donald.png'))

def escolha():
    showinfo(title= 'resignificando', message=f'você é gay {tamanhoN.get()}')
    
pergunta =ttk.Label(text='escolha o tamanho: ',)
pergunta.pack(fill='x', padx=3,pady=3)


tamanhoN = tk.StringVar(jane, value='M')
tamanhos = (('pequeno','P'),('medio','M'),('grande','G'))

for tamanho in tamanhos:
    rd = ttk.Radiobutton(jane,text =tamanho[0], value=tamanho[1],variable = tamanhoN)
    rd.pack(fill ='x',padx=5,pady=5) 

confirmaresc = ttk.Button(jane, text='confirmar',command=escolha)
confirmaresc.pack(fill='x', padx=15,pady=5)

jane.mainloop()