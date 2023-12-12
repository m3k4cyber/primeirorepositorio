import tkinter as tk
from Pessoa import Pessoa
from datetime import datetime as dt
from tkinter import messagebox as meme

# criar frame principal 

janela = tk.Tk()
janela.geometry('320x430')
janela.title('age Calculator 2000')


# criar lables

nome = tk.Label(text = 'Nome:',height=2, font= ('Arial', 15))
nome.grid(column=0, row=1)

dia = tk.Label(text = 'Dia:',height=2, font= ('Arial', 15))
dia.grid(column=0, row=3)

mes = tk.Label(text = 'Mês:',height=2, font= ('Arial', 15))
mes.grid(column=0, row=5)

ano = tk.Label(text = 'Ano:',height=2, font= ('Arial', 15))
ano.grid(column=0, row=7)

# criar campos (fields)

campoNome = tk.Entry(font= ('Arial', 15))
campoNome.grid(column= 1, row=1)

campoDia = tk.Entry(font= ('Arial', 15))
campoDia.grid(column= 1, row=3)

campoMes = tk.Entry(font= ('Arial', 15))
campoMes.grid(column= 1, row=5)

campoAno = tk.Entry(font= ('Arial', 15))
campoAno.grid(column= 1, row=7)

# Comando limpar

def limpar() -> None:
    campoNome.delete(0,tk.END)
    campoDia.delete(0,tk.END)
    campoMes.delete(0,tk.END)
    campoAno.delete(0,tk.END)
    
# Botão Limpar

bLimpar = tk.Button(janela, text = "Limpar", command= limpar, width=10)
bLimpar.grid(column=1, row= 20)

# comando calcular

def confirma() -> None:
    humano = Pessoa(campoNome.get(), dt(campoAno.get(),campoMes.get(),int(campoDia.get())))
    meme.showinfo(title = 'resultado', message=humano)
    
# Botão calcular

bCalcular = tk.Button(janela, text = "Confirma", command= confirma, width=10)
bCalcular.grid(column=0, row= 20)

# começar a gui

janela.mainloop()