import tkinter as tk
import ctypes

def set_emoji(emoji):
    kernel32 = ctypes.windll.kernel32
    kernel32.SetConsoleTitleW(emoji)

janela = tk.Tk()
janela.geometry('1250x500')
janela.title('trabajo')
janela.resizable(False, False)
janela.anchor(anchor='center')

def mudar_cor():
    if janela.config()['bg'] == 'white':
        janela.config(bg='black')
    elif janela.config()['bg'] == 'white':
        janela.config(bg='black')

# =====================================
        
textoA = tk.Label(janela, text= 'Escreva palavra que será substituida:',height=1, font= ('Arial', 20))
textoA.place(x = 15, y = 30)

textoB = tk.Label(janela, text= 'Escreva palavra que substituirá:',height=1, font= ('Arial', 20))
textoB.place(x = 765, y = 30)

cEscA = tk.Entry(font= ('Arial', 20))
cEscA.place(x = 15, y = 70)

cEscB = tk.Entry(font= ('Arial', 20))
cEscB.place(x = 765, y = 70)

texto_G_A = tk.Label(janela, text= 'Escreva o texto Bruto:',height=1, font= ('Arial', 20))
texto_G_A.place(x = 15, y = 125)

ctextobruto = tk.Entry(font= ('Arial', 20))
ctextobruto.place(x = 15, y = 175)

texto_G_B = tk.Label(janela, text= '= Texto Modificado =',height=1, font= ('Arial', 20))
texto_G_B.place(x = 765, y = 125)

textoM = tk.Label(janela,height=1, font= ('Arial', 20))
textoM.place(x = 765, y = 175)

def modificar() ->str:
    #a = str(cEscA.get())
    #b = str(cEscB.get())
    #tb = str(ctextobruto.get())
    textoM["text"] = str(ctextobruto.get()).replace(str(cEscA.get()),str(cEscB.get()))
    #textoM.config(text=f"🖕")
    #return textoM["text"] = str(ctextobruto.get()).replace(str(cEscA.get()),str(cEscB.get()))

botaoMaster = tk.Button(text='MODIFICAR',bg='green',command= modificar,height=2,font= ('Arial', 20))
botaoMaster.place(x=525,y=225)

botao = tk.Button(janela, text='Mudar cor de fundo', command=mudar_cor)
botao.pack()

janela.mainloop()