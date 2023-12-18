import tkinter as tk
from Pessoa import Pessoa
from datetime import datetime as dt
from tkinter import messagebox as meme

# criar frame principal 

janela = tk.Tk()
janela.geometry('1460x960')
janela.title('ler de tras para frante')
janela.resizable(False, False)
janela.anchor(anchor='center')

# criar lables

palavra = tk.Label(text = 'Enter a word:',height=2, font= ('Arial', 20))
palavra.grid(column=0, row=1)

# criar campos (fields)

campoPalavra = tk.Entry(font= ('Arial', 15))
campoPalavra.grid(column= 1, row=1)

# comando inverter

def inverter() -> None:
    palavrareversa = campoPalavra[::-1]
    palavrareversa = str(palavrareversa)
    return palavrareversa
    
# Botão calcular

bIverter = tk.Button(janela, text = "inverter", command= inverter, width=10)
bIverter.grid(column=0, row= 18)

# começar a gui

janela.mainloop()